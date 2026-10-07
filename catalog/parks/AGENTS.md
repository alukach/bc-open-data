# AGENTS.md — Parks, Ecological Reserves and Protected Areas

## Overview

930 BC Parks, ecological reserves and protected areas.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/parks/parks.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/parks/parks.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/parks/parks.parquet') LIMIT 5;
```

## Schema & field notes

- `PROTECTED_LANDS_DESIGNATION`: PROVINCIAL PARK 693, ECOLOGICAL RESERVE 148, PROTECTED AREA 87, RECREATION AREA 2. `PARK_CLASS`: Class A 678, null 237, Class C 13, Class B 2. `OFFICIAL_AREA_HA`, `ESTABLISHMENT_DATE`.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

The publisher's dictionary has no column comments for this table.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Area by designation:

```sql
SELECT PROTECTED_LANDS_DESIGNATION, count(*) AS areas, round(sum(OFFICIAL_AREA_HA)) AS hectares
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/parks/parks.parquet')
GROUP BY 1 ORDER BY hectares DESC;
```

## Related collections

- [recreation-trails](../recreation-trails/AGENTS.md).
