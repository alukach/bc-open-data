# AGENTS.md — Hospitals

## Overview

91 hospitals listed by HealthLinkBC.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/hospitals/hospitals.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/hospitals/hospitals.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/hospitals/hospitals.parquet') LIMIT 5;
```

## Schema & field notes

- `OCCUPANT_NAME`, `PHYSICAL_ADDRESS`, `LOCALITY`, `HOURS`, `WEBSITE_URL`, `CONTACT_PHONE` (switchboard).

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.



## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Hospitals by locality:

```sql
SELECT LOCALITY, count(*) AS hospitals FROM read_parquet('https://data.source.coop/alukach/bc-open-data/hospitals/hospitals.parquet') GROUP BY 1 ORDER BY 2 DESC LIMIT 10;
```

## Related collections

- [schools](../schools/AGENTS.md).
