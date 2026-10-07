#!/usr/bin/env bash
# Extract BC Data Catalogue layers province-wide from the BCGW WFS into GeoParquet.
#
# Pages of 10,000 features (sortBy=OBJECTID, so paging is stable) are fetched 4 at a
# time; each page is converted to Parquet as it lands and its GeoJSON deleted, so peak
# disk stays near the size of the output. Pages are then merged into one spatially
# sorted GeoParquet per layer, in the source CRS (EPSG:3005, BC Albers), and the row
# count is checked against the server's numberMatched.
# Usage: scripts/extract.sh [all | <collection> <typename>]
set -uo pipefail  # no -e: a failed layer warns and the run continues
cd "$(dirname "$0")/.."

WFS="https://openmaps.gov.bc.ca/geo/pub/wfs"
WORK=.work; mkdir -p "$WORK"
PAGE=10000 JOBS=4

hits() {
  curl -sfG "$WFS" --data-urlencode service=WFS --data-urlencode version=2.0.0 \
    --data-urlencode request=GetFeature --data-urlencode "typeNames=pub:$1" \
    --data-urlencode resultType=hits | grep -oE 'numberMatched="[0-9]+"' | grep -oE '[0-9]+'
}

# page <typename> <start> <dir> <sort>: fetch one page, keep it only as Parquet.
# Sorting is only needed (and only possible: some tables lack OBJECTID) across pages.
page() {
  local out="$3/$(printf %09d "$2").parquet" json="$3/$(printf %09d "$2").json"
  [ -s "$out" ] && return
  for try in 1 2 3; do
    curl -sfG "$WFS" --data-urlencode service=WFS --data-urlencode version=2.0.0 \
      --data-urlencode request=GetFeature --data-urlencode "typeNames=pub:$1" \
      --data-urlencode count=$PAGE ${4:+--data-urlencode startIndex=$2 --data-urlencode sortBy=$4} \
      --data-urlencode outputFormat=json -o "$json" \
      && ogr2ogr -f Parquet "$out" "$json" -lco COMPRESSION=ZSTD -lco WRITE_COVERING_BBOX=NO && break
    rm -f "$out"; sleep $((try * 10))
  done
  rm -f "$json"
  [ -s "$out" ] || { echo "PAGE FAILED: $1 @ $2" >&2; return 1; }
}
export -f page; export WFS PAGE

# bc <collection> <typename>
bc() {
  local n dir="$WORK/pages/$1" out="catalog/$1/$1.parquet"
  n=$(hits "$2") || { echo "HITS FAILED: $2" >&2; return 1; }
  echo "bc: $1 ($2): $n features, $(( (n + PAGE - 1) / PAGE )) pages"
  mkdir -p "$dir" "catalog/$1"
  local sort=""; [ "$n" -gt $PAGE ] && sort=OBJECTID
  seq 0 $PAGE $((n - 1)) | xargs -P $JOBS -I{} bash -c 'page "$0" {} "$1" "$2"' "$2" "$dir" "$sort" || return 1
  # Merge pages, dropping GeoServer's synthetic `id` and lat/lon columns the geometry duplicates.
  rm -f "$out" "$dir.fgb"
  local nulls; nulls=$(duckdb -noheader -list -c "SELECT count(*) FILTER (WHERE geometry IS NULL) FROM read_parquet('$dir/*.parquet')")
  if [ "$nulls" != 0 ]; then
    # The DuckDB -> FlatGeobuf merge mis-writes null geometries (schools: 42 nulls in, 16 out,
    # 26 rows given another row's geometry), and a spatial sort isolates nulls in a row group
    # with no bbox stats. So null-geometry layers go straight from their single page to Parquet.
    [ "$(ls "$dir" | wc -l)" -eq 1 ] || { echo "UNSUPPORTED: $1 has $nulls null geometries across pages" >&2; return 1; }
    local cols; cols=$(duckdb -noheader -list -c "SELECT string_agg('\"' || column_name || '\"', ',') FROM (DESCRIBE SELECT * FROM read_parquet('$dir/*.parquet')) WHERE column_name NOT IN ('id', 'LATITUDE', 'LONGITUDE', 'geometry')")
    local pg; pg=$(ls "$dir"/*.parquet)
    ogr2ogr -f Parquet "$out" "$pg" -sql "SELECT $cols FROM \"$(basename "$pg" .parquet)\"" \
      -lco COMPRESSION=ZSTD -lco WRITE_COVERING_BBOX=YES || { echo "MERGE FAILED: $1" >&2; return 1; }
  else
    duckdb -c "LOAD spatial; COPY (SELECT COLUMNS(c -> c NOT IN ('id', 'LATITUDE', 'LONGITUDE'))
        FROM read_parquet('$dir/*.parquet', union_by_name = true))
      TO '$dir.fgb' WITH (FORMAT GDAL, DRIVER 'FlatGeobuf', SRS 'EPSG:3005');" || { echo "MERGE FAILED: $1" >&2; return 1; }
    ogr2ogr -f Parquet "$out" "$dir.fgb" -lco COMPRESSION=ZSTD -lco SORT_BY_BBOX=YES -lco WRITE_COVERING_BBOX=YES || return 1
    rm -f "$dir.fgb"
  fi
  local got; got=$(duckdb -noheader -list -c "SELECT count(*) FROM read_parquet('$out')")
  [ "$got" = "$n" ] && rm -rf "$dir" && echo "  -> $out ($got features, $(du -h "$out" | cut -f1))" \
    || echo "COUNT MISMATCH: $1 server=$n file=$got (pages kept in $dir)" >&2
}

run_all() {  # smallest first
  bc hospitals            WHSE_IMAGERY_AND_BASE_MAPS.GSR_HOSPITALS_SVW
  bc municipalities       WHSE_LEGAL_ADMIN_BOUNDARIES.ABMS_MUNICIPALITIES_SP
  bc parks                WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW
  bc aquifers             WHSE_WATER_MANAGEMENT.GW_AQUIFERS_CLASSIFICATION_SVW
  bc schools              WHSE_IMAGERY_AND_BASE_MAPS.GSR_SCHOOLS_K_TO_12_SVW
  bc hydrometric-stations WHSE_ENVIRONMENTAL_MONITORING.ENVCAN_HYDROMETRIC_STN_SP
  bc recreation-trails    WHSE_FOREST_TENURE.FTEN_RECREATION_LINES_SVW
  bc wildfire-perimeters  WHSE_LAND_AND_NATURAL_RESOURCE.PROT_HISTORICAL_FIRE_POLYS_SP
  bc fwa-rivers           WHSE_BASEMAPPING.FWA_RIVERS_POLY
  bc water-wells          WHSE_WATER_MANAGEMENT.GW_WATER_WELLS_WRBC_SVW
  bc culverts             WHSE_IMAGERY_AND_BASE_MAPS.MOT_CULVERTS_SP
  bc wildfire-incidents   WHSE_LAND_AND_NATURAL_RESOURCE.PROT_HISTORICAL_INCIDENTS_SP
  bc fwa-wetlands         WHSE_BASEMAPPING.FWA_WETLANDS_POLY
  bc fwa-lakes            WHSE_BASEMAPPING.FWA_LAKES_POLY
}

case "${1:-all}" in all) run_all ;; *) bc "$@" ;; esac
