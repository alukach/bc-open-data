# AGENTS.md — Historical Wildfire Perimeters

## Overview

24,751 mapped wildfire perimeters from 1917 to 2025.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/wildfire-perimeters/wildfire-perimeters.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/wildfire-perimeters/wildfire-perimeters.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-perimeters/wildfire-perimeters.parquet') LIMIT 5;
```

## Schema & field notes

- `FIRE_NUMBER`, `FIRE_YEAR`, `FIRE_CAUSE` (Person 15,612, Lightning 9,061, Unknown 78), `FIRE_SIZE_HECTARES` (area inside the perimeter).

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Only fires large enough to be mapped appear; most incidents have no perimeter.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Area burned per year, last decade:

```sql
SELECT FIRE_YEAR, count(*) AS fires, round(sum(FIRE_SIZE_HECTARES)) AS hectares
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/wildfire-perimeters/wildfire-perimeters.parquet')
WHERE FIRE_YEAR >= 2015
GROUP BY 1 ORDER BY 1;
```

## Related collections

- [wildfire-incidents](../wildfire-incidents/AGENTS.md).
