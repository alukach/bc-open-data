# Recreation Line

19,936 recreation trail and feature lines managed by Recreation Sites and Trails BC. Published by Recreation Sites and Trails BC (Province of British Columbia) as [Recreation Line](https://catalogue.data.gov.bc.ca/dataset/recreation-line) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![Canada](https://img.shields.io/badge/Canada-blue) ![FTA](https://img.shields.io/badge/FTA-blue) ![forest](https://img.shields.io/badge/forest-blue) ![forest tenure](https://img.shields.io/badge/forest_tenure-blue) ![recreation](https://img.shields.io/badge/recreation-blue)

## Spatial Coverage

- **Bounding Box**: [-134.99525281535426, 48.48632798265462, -114.04273921296817, 60.000363158278475]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| RMF_SKEY | int32 | The unique identifier (called an SKEY) for the Recreation Map Feature. |
| FOREST_FILE_ID | string | An identifier assigned to the recreation file, e.g., REC16098. |
| SECTION_ID | string | An identifier assigned to a section of a recreation trail, e.g., 1, 10, A, B, EATON LAKE. |
| RECREATION_MAP_FEATURE_CODE | string | Code that identifies the type of recreation feature, i.e., IF (interpretive forest trail), RTR (recreation trail). |
| PROJECT_TYPE | string | Description of the type of recreation feature, i.e., Interpretative Forest, Recreation Trail. |
| RETIREMENT_DATE | timestamp[ms] | For a retired recreation feature, this is the date and time the recreation feature was retired. |
| AMENDMENT_ID | int32 | The number of times a feature has been amended over its lifetime. |
| MAP_LABEL | string | The default label often used when displaying the feature on a map, and consists of the FOREST FILE ID and SECTION ID separated by a space, e.g., REC4531 15, REC3069 EATON LAKE. |
| PROJECT_NAME | string | The name of the area or trail network, usually a geographic name, e.g., OKEOVER TRAILS. |
| RECREATION_FEATURE_CODE | string | Code describing the type of natural or man made recreation feature, e.g., H3 (Historic Route). |
| RESOURCE_FEATURE_IND | string | Indicates whether this is a resource feature established under the Government Action Regulation. |
| RIGHT_OF_WAY | int32 | The entire width of the Right of Way for the linear feature. |
| ARCH_IMPACT_ASSESS_IND | string | Indicates if an archaeological impact assessment has been performed for the given project. |
| SITE_LOCATION | string | The closest town or city to the recreation feature, e.g. KELOWNA, BELLA COOLA. |
| PROJECT_ESTABLISHED_DATE | timestamp[ms] | This is the date on which the recreation project was legally established. |
| RECREATION_VIEW_IND | string |  |
| RECREATION_DISTRICT_CODE | string | A comma-separated list of codes relating to the recreation districts that the recreation feature is within, e.g., RDCO,RDKB,RDOS. |
| DEFINED_CAMPSITES | int32 | The total number of campsites. |
| LIFE_CYCLE_STATUS_CODE | string | The life cycle state of the feature, e.g., PENDING, ACTIVE, RETIRED. |
| FILE_STATUS_CODE | string | The current status of the recreation tenure, eg. AR (archived), HI (issued), PI (pending issuance). |
| DISTRICT_CODE | string | The code of the natural resource district associated with this feature. |
| DISTRICT_NAME | string | The name of the natural resource district associated with this feature. |
| FEATURE_CLASS_SKEY | int32 | Unique identifier for the spatial feature class. |
| FEATURE_LENGTH | double | Spatial perimeter length in metres. This value is calculated in the source system. |
| FEATURE_LENGTH_M | double | The system calculated length or perimeter of a geometry in meters. |
| OBJECTID | int32 | A column required by spatial layers that interact with ESRI ArcSDE. It is populated with unique values automatically by SDE. |
| SE_ANNO_CAD_DATA | string | A binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./recreation-trails.thumb.jpg | 15.9 KB | 122044f6c502... |
| ./README.md | 5.8 KB | 122050f0fa70... |
| ./recreation-trails.parquet | 29.8 MB | 1220acf2dd3e... |
| ./recreation-trails.pmtiles | 27.9 MB | 1220030cffcf... |
| ./styles/default.json | 939 B | 12207e0d994b... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./recreation-trails.thumb.jpg")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/recreation-line](https://catalogue.data.gov.bc.ca/dataset/recreation-line)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: FTEN_RECREATION_LINES_SVW.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
