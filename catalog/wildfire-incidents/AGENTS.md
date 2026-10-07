# AGENTS.md — Historical Wildfire Incidents

## Overview

200,479 wildfire incidents recorded by the BC Wildfire Service, 1950 to 2025.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/wildfire-incidents/wildfire-incidents.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/wildfire-incidents/wildfire-incidents.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-incidents/wildfire-incidents.parquet') LIMIT 5;
```

## Schema & field notes

- `FIRE_NUMBER` + `FIRE_YEAR` identify an incident. `FIRE_CAUSE`: Lightning 75,220, Person 74,385, Unknown 50,874.
- `CURRENT_SIZE` in hectares; `FIRE_CENTRE`, `ZONE`; `IGNITION_DATE`, `FIRE_OUT_DATE`.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Points are reported ignition locations. Recording practice changed over 75 years; compare early decades with care.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Incidents by decade and cause:

```sql
SELECT (FIRE_YEAR // 10) * 10 AS decade, FIRE_CAUSE, count(*) AS incidents
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-incidents/wildfire-incidents.parquet')
GROUP BY ALL ORDER BY decade, incidents DESC;
```

Incidents with a mapped perimeter, joined on fire number and year:

```sql
SELECT i.FIRE_YEAR, count(*) AS with_perimeter
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-incidents/wildfire-incidents.parquet') i
JOIN read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-perimeters/wildfire-perimeters.parquet') p USING (FIRE_NUMBER, FIRE_YEAR)
WHERE i.FIRE_YEAR >= 2015
GROUP BY 1 ORDER BY 1;
```

## Related collections

- [wildfire-perimeters](../wildfire-perimeters/AGENTS.md) on `FIRE_NUMBER` + `FIRE_YEAR`.
