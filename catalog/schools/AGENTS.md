# AGENTS.md — K-12 Schools

## Overview

1,914 K-12 schools with category, grade level, district and French-language programs.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/schools/schools.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/schools/schools.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/schools/schools.parquet') LIMIT 5;
```

## Schema & field notes

- `SCHOOL_CATEGORY`: Public School 1,568, Independent School 346. `SCHOOL_EDUCATION_LEVEL`: Elementary 1,259, Secondary 266, Elementary-Secondary 206, …
- `DISTRICT_NAME`, `SCHOOL_NUMBER`; French program flags `CORE_FRENCH_OFFERED`, `EARLY_FRENCH_IMMERSION_OFFERED`, `LATE_FRENCH_IMMERSION_OFFERED`, `FRANCOPHONE_PROGRAM_OFFERED`.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

16 schools have no location (null geometry) in the source. `CONTACT_*` columns are school switchboards.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Schools per municipality (spatial join):

```sql
SELECT m.ADMIN_AREA_ABBREVIATION AS municipality, count(*) AS schools
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/schools/schools.parquet') s
JOIN read_parquet('https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet') m ON ST_Within(s.geometry, m.geometry)
GROUP BY 1 ORDER BY schools DESC LIMIT 10;
```

## Related collections

- [municipalities](../municipalities/AGENTS.md).
