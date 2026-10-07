#!/usr/bin/env bash
# Build PMTiles next to each GeoParquet file, at province scale (zooms 0-13).
# -r1 turns off rate-based point thinning; --drop-densest-as-needed still keeps each
# tile under tippecanoe's size limit, so low zooms show the densest points thinned
# rather than a fixed fraction. Tiny-polygon reduction stays on: at province zooms the
# ~386k small lakes and wetlands accumulate into density specks, which is the overview.
# Usage: scripts/tile.sh [dir...]   (default: catalog)
set -uo pipefail
cd "$(dirname "$0")/.."

for pq in $(find "${@:-catalog}" -name '*.parquet' -not -name 'items.parquet' | sort); do
  out="${pq%.parquet}.pmtiles" layer=$(basename "$pq" .parquet)
  # Null geometries (42 ungeocoded schools) have nothing to draw and make GDAL's reprojection abort.
  ogr2ogr -f GeoJSONSeq /vsistdout/ "$pq" -t_srs EPSG:4326 -lco RS=NO \
      -dialect SQLite -sql "SELECT * FROM \"$layer\" WHERE geometry IS NOT NULL" |
    tippecanoe -q -f -o "$out" -l "$layer" -Z0 -z13 -r1 \
      --drop-densest-as-needed --extend-zooms-if-still-dropping -P \
    && echo "$out $(du -h "$out" | cut -f1)" || echo "FAILED: $pq" >&2
done
