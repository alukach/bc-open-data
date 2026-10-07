# AGENTS.md — Hydrometric Stations

## Overview

2,317 Water Survey of Canada water level and streamflow stations in BC.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/hydrometric-stations/hydrometric-stations.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/hydrometric-stations/hydrometric-stations.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/hydrometric-stations/hydrometric-stations.parquet') LIMIT 5;
```

## Schema & field notes

- `STATION_NUMBER`; `STATION_OPERATING_STATUS`: DISCONTINUED 1,857, ACTIVE-REALTIME 401, ACTIVE 35, NA 24. `REALTIME_URL`, `ARCHIVE_URL`, `START_DATE`, `END_DATE`.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Station list only; follow `ARCHIVE_URL` / `REALTIME_URL` for measurements.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Active real-time stations:

```sql
SELECT STATION_NUMBER, STATION_NAME, REALTIME_URL
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/hydrometric-stations/hydrometric-stations.parquet')
WHERE STATION_OPERATING_STATUS = 'ACTIVE-REALTIME'
ORDER BY STATION_NUMBER LIMIT 10;
```

## Related collections

- [fwa-rivers](../fwa-rivers/AGENTS.md).
