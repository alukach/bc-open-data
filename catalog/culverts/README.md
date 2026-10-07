# Ministry of Transportation (MOT) Culverts

186,427 culverts on Ministry of Transportation roads, with material, size, installation date and fish-passage attributes. Published by Construction and Maintenance (Province of British Columbia) as [Ministry of Transportation (MOT) Culverts](https://catalogue.data.gov.bc.ca/dataset/ministry-of-transportation-mot-culverts) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![CULV](https://img.shields.io/badge/CULV-blue) ![MOT](https://img.shields.io/badge/MOT-blue) ![MOT asset](https://img.shields.io/badge/MOT_asset-blue) ![MOT inventory](https://img.shields.io/badge/MOT_inventory-blue) ![culvert](https://img.shields.io/badge/culvert-blue)

## Spatial Coverage

- **Bounding Box**: [-133.80811990818677, 48.3288435, -114.6792192471381, 59.999770105790645]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| CULVERT_ID | int32 | CULVERT ID is a system generated identifier to ensure row uniqueness. This is a primary key field. |
| CHRIS_CULVERT_ID | string | CHRIS CULVERT ID contains the identifier of the culvert inventory item derived by the CHRIS application. E.g., 2455305 |
| ADMIN_UNIT_CODE | string | ADMIN UNIT CODE contains the MoT Service Area identifier. There are 28 service areas in MoT's jurisdiction. Each Service Area represents a geographic area within the province. E.g., 13 |
| ADMIN_UNIT_NAME | string | ADMIN UNIT NAME contains the MoT Service Area Name identifier. |
| CROSS_SECTION_POSITION | string | CROSS SECTION POSITION contains the cross sectional position of the culvert in relationship to the road, E.g., Ditch - Left, Right of Way - Left, Shoulder - Left etc. |
| CULVERT_TYPE | string | CULVERT TYPE contains a physical description of the type of culvert, E.g., down drain, entrance, roadway etc. |
| CULVERT_DIAMETER | int32 | CULVERT DIAMETER contains the physical measure of the diameter of the culvert in millimetres. E.g., 100, 2999, etc. |
| CULVERT_MATERIAL | string | CULVERT MATERIAL contains a physical description of the type of material the culvert is made of. E.g., Concrete, Galvanized, Plastic etc. |
| CONFINED_SPACE_IND | string | CONFINED SPACE IND indicates whether the Culvert is enclosed or partially enclosed, not designed for human occupancy, and large enough so the worker can enter e.g., Yes or No |
| INSTALLATION_DATE | timestamp[ms] | INSTALLATION DATE indicates the date that the culvert was installed (YYYY-MM-DD). |
| FISH_SENSITIVE_CODE | string | FISH SENSITIVE CODE indicates whether a Culvert contains fish bearing water or not. e.g., Yes, No or Unknown |
| FISH_PASSAGE_TYPE | string | FISH PASSAGE TYPE contains a physical description of the fish passage type, E.g., bottomless, baffle, fish ladder etc. |
| GRATE_CODE | string | GRATE CODE indicates whether a culvert has a grate or not. e.g., Yes, No or Unknown |
| FLAP_GRATE_CODE | string | FLAP GRATE CODE indicates whether a culvert has a flap grate or not. e.g., Yes, No or Unknown |
| CHRIS_ANCHOR_SECTION_ID | int32 | CHRIS ANCHOR SECTON ID contains the CHRIS application internal unique identifier for the anchor section segment. E.g., 2777363 |
| EVENT_LOCATION | double | EVENT LOCATION contains the Measure for the Culvert along the Anchor Section. Measures are in Kilometers. e.g., 42.200 |
| HIGHWAY_NUMBER | string | HIGHWAY NUMBER is the MoT Numbered Route identifier only populated when the culvert is located on a MoT Numbered route. E.g., 99 If the culvert is not on a numbered route the field is blank. |
| OBJECTID | int32 | OBJECTID is a required attribute of feature classes and object classes in a geodatabase. |
| SE_ANNO_CAD_DATA | string | SE_ANNO_CAD_DATA is a binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./culverts.thumb.jpg | 18.8 KB | 12200452e6fc... |
| ./README.md | 5.8 KB | 122051214722... |
| ./culverts.parquet | 8.8 MB | 12209b0bd984... |
| ./culverts.pmtiles | 47.4 MB | 12202a1c572b... |
| ./styles/default.json | 981 B | 1220ba0c27c7... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./culverts.thumb.jpg")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/ministry-of-transportation-mot-culverts](https://catalogue.data.gov.bc.ca/dataset/ministry-of-transportation-mot-culverts)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: MOT_CULVERTS_SP.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

## Known Issues

Ministry of Transportation highway assets only; municipal culverts are not included.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
