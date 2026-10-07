# AGENTS.md — Ground Water Aquifers

## Overview

1,166 mapped and classified aquifers with material, productivity, vulnerability and demand.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/aquifers/aquifers.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/aquifers/aquifers.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/aquifers/aquifers.parquet') LIMIT 5;
```

## Schema & field notes

- `AQUIFER_ID`; `AQUIFER_DETAILS_URL` links to the aquifer report.
- `MATERIAL`: Sand and Gravel 791, Bedrock 375. `VULNERABILITY`: Moderate 428, Low 372, High 361. `PRODUCTIVITY`: Moderate 635, Low 261, High 179, null 91.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Only mapped aquifers appear; absence does not mean no groundwater.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Vulnerability by material:

```sql
SELECT MATERIAL, VULNERABILITY, count(*) AS aquifers, round(sum(ST_Area(geometry)) / 1e6) AS km2
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/aquifers/aquifers.parquet')
GROUP BY ALL ORDER BY MATERIAL, aquifers DESC;
```

## Related collections

- [water-wells](../water-wells/AGENTS.md) on `AQUIFER_ID`.
