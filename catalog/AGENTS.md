# AGENTS.md — British Columbia Open Data

## Overview

Province-wide mirrors of openly licensed BC Data Catalogue datasets as GeoParquet (query this) and PMTiles (maps). Independent mirror, extracted 2026-10-07; every collection is under the Open Government Licence – British Columbia. Build code and issues: <https://github.com/alukach/bc-open-data>.

## Accessing the data

Base URL `https://data.source.coop/alukach/bc-open-data/`; each collection is `<collection>/<collection>.parquet`. STAC root: `https://data.source.coop/alukach/bc-open-data/catalog.json`.

## Collections

| Collection | What |
|---|---|
| [municipalities](municipalities/AGENTS.md) | 160 municipal boundaries |
| [fwa-lakes](fwa-lakes/AGENTS.md) | 386,025 lakes |
| [fwa-rivers](fwa-rivers/AGENTS.md) | 37,083 double-line rivers |
| [fwa-wetlands](fwa-wetlands/AGENTS.md) | 375,178 wetlands |
| [water-wells](water-wells/AGENTS.md) | 130,946 groundwater wells |
| [aquifers](aquifers/AGENTS.md) | 1,166 aquifers |
| [wildfire-incidents](wildfire-incidents/AGENTS.md) | 200,479 fire incidents, 1950-2025 |
| [wildfire-perimeters](wildfire-perimeters/AGENTS.md) | 24,751 fire perimeters, 1917-2025 |
| [schools](schools/AGENTS.md) | 1,914 K-12 schools |
| [hospitals](hospitals/AGENTS.md) | 91 hospitals |
| [recreation-trails](recreation-trails/AGENTS.md) | 19,936 recreation trail lines |
| [culverts](culverts/AGENTS.md) | 186,427 highway culverts |
| [hydrometric-stations](hydrometric-stations/AGENTS.md) | 2,317 hydrometric stations |
| [parks](parks/AGENTS.md) | 930 parks and protected areas |

## Data quality & usage notes

- Every collection is **EPSG:3005 (BC Albers, metres)**, so collections combine without transforms.
- Files are spatially sorted with a `geometry_bbox` covering column. Filter on it before any spatial predicate to read only the row groups you need.
- Not refreshed automatically; check each collection's `updated`.

## Example queries

Cut any collection to one municipality: bbox filter on the covering column first, then the exact test.

```sql
WITH m AS (
  SELECT geometry AS g, ST_XMin(geometry) AS x0, ST_YMin(geometry) AS y0, ST_XMax(geometry) AS x1, ST_YMax(geometry) AS y1
  FROM read_parquet('https://data.source.coop/alukach/bc-open-data/municipalities/municipalities.parquet') WHERE ADMIN_AREA_ABBREVIATION = 'Nelson'
)
SELECT count(*) AS wells_in_nelson
FROM read_parquet('https://data.source.coop/alukach/bc-open-data/water-wells/water-wells.parquet') w, m
WHERE w.geometry_bbox.xmax >= m.x0 AND w.geometry_bbox.xmin <= m.x1
  AND w.geometry_bbox.ymax >= m.y0 AND w.geometry_bbox.ymin <= m.y1
  AND ST_Intersects(w.geometry, m.g);
```

## Related collections

Join keys: `AQUIFER_ID` (water-wells ↔ aquifers); `FIRE_NUMBER` + `FIRE_YEAR` (wildfire-incidents ↔ wildfire-perimeters); everything else joins spatially, usually through municipalities.
