# AGENTS.md — Freshwater Atlas Lakes

## Overview

386,025 lake polygons from the Freshwater Atlas, BC's 1:20,000 corporate watershed base.

## Accessing the data

- GeoParquet: `https://data.source.coop/alukach/bc-open-data/fwa-lakes/fwa-lakes.parquet`
- PMTiles (maps only, Web Mercator, zooms 0-13): `https://data.source.coop/alukach/bc-open-data/fwa-lakes/fwa-lakes.pmtiles`

```sql
SELECT * FROM read_parquet('https://data.source.coop/alukach/bc-open-data/fwa-lakes/fwa-lakes.parquet') LIMIT 5;
```

## Schema & field notes

- `WATERBODY_KEY` identifies the waterbody; `GNIS_NAME_1` is its official name (null for most small features); `AREA_HA` is area in hectares; `FWA_WATERSHED_CODE` encodes the watershed hierarchy.

Every column's description, copied from the BC Data Catalogue dictionary where the Province provides one, is in `table:columns` in [collection.json](collection.json).

## Data quality & usage notes

Geometry is **EPSG:3005 (NAD83 / BC Albers)**, metres, as the Province publishes it: `ST_Area`/`ST_Length` return m² and m directly. For lon/lat use `ST_Transform(geometry, 'EPSG:3005', 'EPSG:4326', always_xy := true)`.

Files are spatially sorted and carry a `geometry_bbox` covering column. Filter on it first (`geometry_bbox.xmin <= …`) so DuckDB reads only nearby row groups instead of the whole file.

Most features are small and unnamed. The stream network (lines) is not in this release; see the GitHub issues.

## Example queries

All queries below were run against this data. Spatial functions need `INSTALL spatial; LOAD spatial;` first.

Largest named features:

```sql
SELECT GNIS_NAME_1, round(AREA_HA) AS hectares
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/fwa-lakes/fwa-lakes.parquet')
WHERE GNIS_NAME_1 IS NOT NULL
ORDER BY AREA_HA DESC LIMIT 10;
```

Features around Kamloops (bbox pushdown):

```sql
SELECT count(*) AS features, round(sum(AREA_HA)) AS hectares
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/fwa-lakes/fwa-lakes.parquet')
WHERE geometry_bbox.xmax >= 1390000 AND geometry_bbox.xmin <= 1410000 AND geometry_bbox.ymax >= 637000 AND geometry_bbox.ymin <= 652000;
```

## Related collections

- [fwa-lakes](../fwa-lakes/AGENTS.md), [fwa-rivers](../fwa-rivers/AGENTS.md), [fwa-wetlands](../fwa-wetlands/AGENTS.md) share `WATERBODY_KEY` conventions.
- Cut any collection to one municipality with the [municipalities](../municipalities/AGENTS.md) boundaries (see the catalog [AGENTS.md](../AGENTS.md) for the pattern).
