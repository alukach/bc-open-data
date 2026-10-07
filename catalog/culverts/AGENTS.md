# AGENTS.md — Highway Culverts

## Overview

186,427 culverts on Ministry of Transportation roads.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/culverts/culverts.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/culverts/culverts.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/culverts/culverts.parquet') LIMIT 5;
```

## Schema & field notes

- `CULVERT_MATERIAL`: Galvanized 167,458, Plastic 6,081, Concrete 5,422, Other 3,825, Wood 1,230, … `CULVERT_DIAMETER`, `CULVERT_TYPE`, `HIGHWAY_NUMBER`, `INSTALLATION_DATE`, fish-passage fields.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Provincial highway assets only.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Culverts by highway:

```sql
SELECT HIGHWAY_NUMBER, count(*) AS culverts
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/culverts/culverts.parquet')
GROUP BY 1 ORDER BY culverts DESC LIMIT 10;
```

## Related collections

- [fwa-rivers](../fwa-rivers/AGENTS.md), [fwa-lakes](../fwa-lakes/AGENTS.md).
