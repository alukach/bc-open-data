# AGENTS.md — Municipalities

## Overview

The legally defined boundaries of BC's 160 municipalities. Use them to cut any other collection to a city, district, town or village.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet') LIMIT 5;
```

## Schema & field notes

- `ADMIN_AREA_NAME` (e.g. 'The Corporation of the City of Nelson'), `ADMIN_AREA_ABBREVIATION` (e.g. 'Nelson'), `LGL_ADMIN_AREA_ID`.
- `ADMIN_AREA_GROUP_NAME`: the regional district (Metro Vancouver 21, Capital 13, Thompson-Nicola 11, …).

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Unincorporated areas (most of the province) belong to no municipality.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Municipalities per regional district:

```sql
SELECT ADMIN_AREA_GROUP_NAME, count(*) AS municipalities, round(sum(ST_Area(geometry)) / 1e6) AS km2
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet')
GROUP BY 1 ORDER BY municipalities DESC LIMIT 10;
```

One city's boundary:

```sql
SELECT ADMIN_AREA_NAME, round(ST_Area(geometry) / 1e6, 2) AS km2 FROM read_parquet('https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet') WHERE ADMIN_AREA_ABBREVIATION = 'Nelson';
```

## Related collections

- Every other collection: spatial join to these boundaries.
