# AGENTS.md — Recreation Trails

## Overview

19,936 recreation trail and feature lines managed by Recreation Sites and Trails BC.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/recreation-trails/recreation-trails.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/recreation-trails/recreation-trails.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/recreation-trails/recreation-trails.parquet') LIMIT 5;
```

## Schema & field notes

- `PROJECT_TYPE`: Recreation Trail Reserve 16,468, Recreation Trail Established 3,436, plus a few interpretive types. `PROJECT_NAME`, `FOREST_FILE_ID`, `FEATURE_LENGTH_M`.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Provincially managed trails only; municipal and regional trails are not included.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Kilometres by project type:

```sql
SELECT PROJECT_TYPE, count(*) AS lines, round(sum(ST_Length(geometry)) / 1000) AS km
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/recreation-trails/recreation-trails.parquet')
GROUP BY 1 ORDER BY km DESC;
```

## Related collections

- [parks](../parks/AGENTS.md).
