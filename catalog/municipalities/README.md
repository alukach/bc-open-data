# Municipalities - Legally Defined Administrative Areas of BC

The legally defined boundaries of BC's 160 municipalities (cities, districts, towns, villages and other local governments). Published by Governance and Structure (Province of British Columbia) as [Municipalities - Legally Defined Administrative Areas of BC](https://catalogue.data.gov.bc.ca/dataset/municipalities-legally-defined-administrative-areas-of-bc) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![ABMS](https://img.shields.io/badge/ABMS-blue) ![Administrative boundaries](https://img.shields.io/badge/Administrative_boundaries-blue) ![jurisdicational boundaries](https://img.shields.io/badge/jurisdicational_boundaries-blue) ![local government](https://img.shields.io/badge/local_government-blue) ![metes and bounds](https://img.shields.io/badge/metes_and_bounds-blue) ![municipal boundaries](https://img.shields.io/badge/municipal_boundaries-blue) ![municipalities](https://img.shields.io/badge/municipalities-blue) ![municipality](https://img.shields.io/badge/municipality-blue)

## Spatial Coverage

- **Bounding Box**: [-132.3368728, 48.30621287949082, -114.62615630549348, 60.00478255729097]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| LGL_ADMIN_AREA_ID | int32 | An operationally-generated unique identification number, e.g., 1, 2,3. |
| ADMIN_AREA_NAME | string | The authoritative, officially approved name given to the Administrative Area, e.g., Corporation of the Village of Tofino. |
| ADMIN_AREA_ABBREVIATION | string | A short form or commonly-known acronym for the Administrative Area name, e.g., Tofino (Corporation of the Village of Tofino). |
| ADMIN_AREA_BOUNDARY_TYPE | string | BOUNDARY TYPE is a high-level grouping of Administrative Areas used to categorise features when reporting, e.g., Census, Legal, Administrative. |
| ADMIN_AREA_GROUP_NAME | string | The name given to the larger administrative area (if there is any) of which this feature is a member, e.g., Regional District of Alberni Clayquot (This would be the ADMIN_AREA_GROUP_NAME of the feature called "The Corporation of the Village of Tofino"). |
| CHANGE_REQUESTED_ORG | string | The government acronym of the Ministry or sub-org that last requested the change that resulted in the modification of the record, e.g., GeoBC, MMAH. |
| UPDATE_TYPE | string | A short description of the latest alteration of the feature's geographic or attribute content, e.g., Inserted (added new), Change in geometry. |
| WHEN_UPDATED | timestamp[ms] | The date and time the record was last modified. |
| MAP_STATUS | string | That the digital map has been appended to Letters Patent of the administrative area and has received cabinet or ministerial approval, i.e., "Appended": the digital map has been appended to Letters Patent of the municipality, electoral area, regional district or improvement district and has received cabinet or ministerial approval. The map is referred to as the legal map and forms Schedule 1 to Letters Patent. "Not Appended": the digital map exists but currently there is no legislative mechanism that enables the map to be appended to Letters Patent in the absence of a request for a boundary amendment. In other words, while the digital map is the exact representation of the administrative boundary, it is not considered legal until appended to Letters Patent. If there is a discrepancy in the boundary, the written metes and bounds prevail. Null values are permitted for Administrative Areas for which the map status does not apply. |
| OIC_MO_NUMBER | string | The most-recent Order-In-Council (OIC) or Ministerial Order (MO) identifier for a particular administrative area. This number is used in conjunction with the OIC_MO_YEAR and the OIC_MO_TYPE to determine the official OIC or MO Number, which is usually in the form ###/YY(YY), e.g., where OIC_MO_NUMBER is 245, the OIC_MO_YEAR is 2013 and the OIC_MO_TYPE is "OIC", the latest OIC for this administrative area is OIC 245/13 that was enacted into law in 2013. Similarily, where OIC_MO_NUMBER is 103 and the OIC_MO_YEAR is 2019 and the OIC_MO_TYPE is "MO", the latest Ministerial Order for this administrative area is MO 103/2019 enacted into law in 2019. |
| OIC_MO_YEAR | string | The four-digit year that the most recent Order-In-Council or Ministerial Order was approved, e.g., 2014. |
| OIC_MO_TYPE | string | The short acronym that determines the type of identifier used in the OIC_MO_NUMBER, e.g., OIC (Order-In-Council), MO (Ministerial Order), OTHER (The boundary was issued using a procedure outside of the traditional mechanisms). |
| WEBSITE_URL | string | An Internet URL link to additional project information and/or files related to the OIC_MO_NUMBER. |
| IMAGE_URL | string | An Internet URL link to additional image files related to the OIC_MO_NUMBER. |
| AFFECTED_ADMIN_AREA_ABRVN | string | A semicolon-delimited list of the abbreviations (ADMIN_AREA_ABBREVIATION) of Administrative Area boundaries that are affected by the OIC number in the OIC year, e.g., NCRD-EA E / NCRD-EA H. If a record has the value "NCRD-EA E / NCRD-EA H" for AFFECTED_ADMIN_AREA_ABRVN, an ADMIN_AREA_ABBREVIATION of Prince Rupert, an OIC/MO (OIC_MO_NUMBER) value of 501/14, an OIC/MO Year (OIC_MO_YEAR) value of 2014, and an Administrative Area Group Name (ADMIN_AREA_GROUP_NAME) of North Coast Regional District, then the interpretation is that OIC 501 in the year 2014 for Prince Rupert also affects the boundaries of Electoral Areas NCRD-EA E and NCRD-EA H in the North Coast Regional District. |
| FEATURE_AREA_SQM | double | The system calculated area of a two-dimensional polygon in square meters. |
| FEATURE_LENGTH_M | double | The system calculated length or perimeter of a geometry in meters. |
| OBJECTID | int32 | A column required by spatial layers that interact with ESRI ArcSDE. It is populated with unique values automatically by SDE. |
| SE_ANNO_CAD_DATA | string | A binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./municipalities.parquet | 1.3 MB | 122088381f6c... |
| ./municipalities.thumb.jpg | 8.8 KB | 12201cf64a55... |
| ./README.md | 8.0 KB | 1220cb6d60e8... |
| ./municipalities.pmtiles | 2.5 MB | 12202dc8927b... |
| ./styles/default.json | 735 B | 1220f67914f7... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./municipalities.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/municipalities-legally-defined-administrative-areas-of-bc](https://catalogue.data.gov.bc.ca/dataset/municipalities-legally-defined-administrative-areas-of-bc)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: ABMS_MUNICIPALITIES_SP.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
