# Hydrometric Stations - Active and Discontinued

2,317 active and discontinued Water Survey of Canada water level and streamflow stations in BC. Published by Environmental Monitoring and Analysis Branch (Province of British Columbia) as [Hydrometric Stations - Active and Discontinued](https://catalogue.data.gov.bc.ca/dataset/hydrometric-stations-active-and-discontinued) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![hydrology](https://img.shields.io/badge/hydrology-blue) ![hydrometric](https://img.shields.io/badge/hydrometric-blue) ![real-time monitoring](https://img.shields.io/badge/real--time_monitoring-blue) ![stream flow](https://img.shields.io/badge/stream_flow-blue)

## Spatial Coverage

- **Bounding Box**: [-135.01300000023087, 48.347, -114.53500000058915, 59.98900000038328]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| HYDROMETRIC_STATION_ID | int32 |  |
| STATION_NUMBER | string | STATION NUMBER is the unique identifier for a Hydrometric Station. |
| FEATURE_CODE | string | FEATURE CODE is a standard alphanumeric code to identify the type of feature represented by the spatial data. A feature code is most importantly a means of linking a feature to its name and definition. For example, the code GB15300120 on a digital geographic feature links it to the name "Lake - Dry" with the definition "A lake bed from which all water has drained or evaporated." The feature code does NOT mark when it was digitized, what dataset it belongs to, how accurate it is, what it should look like when plotted, or who is responsible for updating it. It only says what it represents in the real world. It also doesn't even matter how the lake is represented. If it is a very small lake, it may be stored as a point feature. If it is large enough to have a shape at the scale of data capture, it may be stored as an outline, or a closed polygon. The same feature code still links it to the same definition. |
| STATION_NAME | string | STATION_NAME is the Hydrometric Station Name. e.g., "LINDEMAN CREEK NEAR BENNETT", "ATLIN LAKE AT ATLIN". |
| FLOW_TYPE | string | FLOW_TYPE represents Natural or Regulated flow. i.e., "NATURAL" or "REGULATED". |
| WATERSHED_GROUP_CODE | string | WATERSHED_GROUP_CODE refers to Watershed Atlas Watershed Group. WATERSHED GROUP CODE will have null values for non-spatially verified stations. |
| WATERSHED_ID | string | WATERSHED_ID is used for Watershed Atlas Identification. WATERSHED ID will have null values for non-spatially verified stations. |
| STREAM_ORDER | string | STREAM_ORDER stores the stream order as a numeric value. The stream order is based on 1:50000 scale mapping. |
| ARCHIVE_URL | string | ARCHIVE_URL is a URL for Environment and Climate Change Canada web site showing archival flow information for a specific station. |
| REALTIME_URL | string | REALTIME_URL is a URL for Environment and Climate Change Canada web site showing real time water level data for a specific station. |
| STATION_OPERATING_STATUS | string | STATION_OPERATING_STATUS represents the Hydrometric Station Status. i.e., "ACTIVE”, “ACTIVE-REALTIME”, OR “DISCONTINUED”. |
| CAPTURE_SCALE | string | CAPTURE_SCALE is the scale at which a station point was mapped. e.g., 1:50,000. |
| START_DATE | timestamp[ms] | START_DATE is the earliest measurement date of approved hydrometric data for a station. |
| END_DATE | timestamp[ms] | END_DATE is the most recent measurement date of approved hydrometric data for a station. |
| OBJECTID | int32 | OBJECTID is a required attribute of feature classes and object classes in a geodatabase. |
| SE_ANNO_CAD_DATA | string | SE_ANNO_CAD_DATA is a binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./hydrometric-stations.thumb.jpg | 18.2 KB | 1220354a8c9b... |
| ./README.md | 5.9 KB | 1220c0add459... |
| ./hydrometric-stations.parquet | 174.7 KB | 12205b82ea05... |
| ./hydrometric-stations.pmtiles | 3.8 MB | 122020da92e9... |
| ./styles/default.json | 875 B | 122002130898... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./hydrometric-stations.thumb.jpg")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/hydrometric-stations-active-and-discontinued](https://catalogue.data.gov.bc.ca/dataset/hydrometric-stations-active-and-discontinued)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: ENVCAN_HYDROMETRIC_STN_SP.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

## Known Issues

This is the station list, not the measurements; follow ARCHIVE_URL / REALTIME_URL for the records.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
