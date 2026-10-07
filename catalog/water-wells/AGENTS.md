# AGENTS.md — Groundwater Wells

## Overview

130,946 wells from the provincial GWELLS registry: construction, depth, yield, water use and aquifer.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.parquet') LIMIT 5;
```

## Schema & field notes

- `WELL_TAG_NUMBER`: GWELLS id; `WELL_DETAILS_URL` links to the well's page.
- `INTENDED_WATER_USE`: Private Domestic 69,967, Unknown Well Use 29,221, Not Applicable 14,796, Commercial and Industrial 5,704, Water Supply System 5,487, Irrigation 4,209, …
- `WELL_CLASS`: Water Supply 92,140, Unknown 36,368, Monitoring 1,417, …
- Depths (`FINISHED_WELL_DEPTH`, `BEDROCK_DEPTH`, `STATIC_WATER_LEVEL`) are in **feet**, `YIELD` in **US gallons/minute**, per the publisher's dictionary.
- `AQUIFER_ID` joins to [aquifers](../aquifers/AGENTS.md).

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

**Personal information:** `STREET_ADDRESS` and `PERSON_RESPONSIBLE` can identify private individuals. They are published as-is by the Province; avoid combining them with other personal data.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Wells per aquifer material, via the aquifer join:

```sql
SELECT a.MATERIAL, count(*) AS wells, round(median(w.FINISHED_WELL_DEPTH)) AS median_depth_ft
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.parquet') w
JOIN read_parquet('https://data.source.coop/alukach/bc-open-data/aquifers/aquifers.parquet') a USING (AQUIFER_ID)
GROUP BY 1 ORDER BY wells DESC;
```

Wells in central Kamloops (bbox pushdown):

```sql
SELECT WELL_TAG_NUMBER, INTENDED_WATER_USE, FINISHED_WELL_DEPTH
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.parquet')
WHERE geometry_bbox.xmax >= 1390000 AND geometry_bbox.xmin <= 1410000 AND geometry_bbox.ymax >= 637000 AND geometry_bbox.ymin <= 652000
ORDER BY FINISHED_WELL_DEPTH DESC NULLS LAST LIMIT 10;
```

## Related collections

- [aquifers](../aquifers/AGENTS.md) on `AQUIFER_ID`.
- Cut any collection to one municipality with the [municipalities](../municipalities/AGENTS.md) boundaries (see the catalog [AGENTS.md](../AGENTS.md) for the pattern).
