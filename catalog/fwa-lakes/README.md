# Freshwater Atlas - Lakes

386,025 lake polygons from the Freshwater Atlas, BC's 1:20,000 corporate watershed base. Published by GeoBC Branch (Province of British Columbia) as [Freshwater Atlas - Lakes](https://catalogue.data.gov.bc.ca/dataset/freshwater-atlas-lakes) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![CWB](https://img.shields.io/badge/CWB-blue) ![corporate watershed base](https://img.shields.io/badge/corporate_watershed_base-blue) ![freshwater atlas](https://img.shields.io/badge/freshwater_atlas-blue)

## Spatial Coverage

- **Bounding Box**: [-138.58381882188417, 48.31870003724797, -114.07198314278287, 60.0000015]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| WATERBODY_POLY_ID | int32 | The WATERBODY POLY ID is the unique key for the waterbody polygon spatial layer. It is not applied to the warehouse model only, i.e., it originates with the source FWA system. |
| WATERSHED_GROUP_ID | int32 | An automatically generate id that uniquely identifies the watershed group feature. |
| WATERBODY_TYPE | string | The type of waterbody. Possible values include: 'L' (lake), 'R' (double lined river), 'W' (wetland), 'X' (manmade river or lake), or 'G' (glacier or icefield). |
| WATERBODY_KEY | int32 | A unique identifier associated with waterbodies in order to group polygons that make up a single waterbody. |
| AREA_HA | double | Area of polygon (hectares). |
| GNIS_ID_1 | int32 | A BCGNIS (BC Geographical Names Information System) feature id attached to a waterbody or island, if applicable. In a grouped system the feature id of the BCGNIS group is provided here and any subsequent names provided in gnis_id2 and gnis_id3. Note: For Vancouver Island, Graham Island, and Moresby Island the names are not attached to the label points. |
| GNIS_NAME_1 | string | The name of the first BCGNIS (BC Geographical Names Information System) feature id (an English name was used where available, otherwise another language was selected). |
| GNIS_ID_2 | string | A second BCGNIS (BC Geographical Names Information System) feature id attached to a waterbody or island, if applicable. |
| GNIS_NAME_2 | string | The name of the second BCGNIS (BC Geographical Names Information System) feature id (an English name was used where available, otherwise another language was selected). |
| GNIS_ID_3 | string | A third BCGNIS (BC Geographical Names Information System) feature id attached to a waterbody or island, if applicable. |
| GNIS_NAME_3 | string | The name of the third BCGNIS (BC Geographical Names Information System) feature id (an English name was used where available, otherwise another language was selected). |
| BLUE_LINE_KEY | int32 | The blue line key of the controlling route through the waterbody. |
| WATERSHED_KEY | int32 | The watershed key of the controlling rout through the waterbody. |
| FWA_WATERSHED_CODE | string | The watershed code of the controlling route through the waterbody. |
| LOCAL_WATERSHED_CODE | string | The local watershed code associated with the waterbody. |
| WATERSHED_GROUP_CODE | string | The watershed group codeof the watershed the feature is contained within. |
| LEFT_RIGHT_TRIBUTARY | string | A value attributed via the watershed code to all waterbodies indicating on what side of the watershed they drain into. |
| WATERBODY_KEY_50K | int32 | The 'best' matched waterbody from the 1:50K Watershed Atlas. In cases where there are multiple matches to features in the 1:50K watershed atlas the match with the greatest overlapping area was used. |
| WATERSHED_GROUP_CODE_50K | string | The group code from the 1:50K Watershed Atlas associated with the waterbody key 50k. |
| WATERBODY_KEY_GROUP_CODE_50K | string | The waterbody key 50K with the group code 50K concatenated. |
| WATERSHED_CODE_50K | string | The 1:50K Watershed Atlas watershed code associated with the waterbody key 50K. |
| FEATURE_CODE | string | FEATURE CODE contains a value based on the Canadian Council of Surveys and Mapping's (CCSM) system for classification of geographic features. |
| OBJECTID | int32 |  |
| SE_ANNO_CAD_DATA | string |  |
| FEATURE_AREA_SQM | double | FEATURE_AREA_SQM is the system calculated area of a two-dimensional polygon in square meters |
| FEATURE_LENGTH_M | double | FEATURE_LENGTH_M is the system calculated length or perimeter of a geometry in meters |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fwa-lakes.parquet | 146.9 MB | 1220f3a028fb... |
| ./README.md | 6.2 KB | 1220e7d02a26... |
| ./fwa-lakes.thumb.jpg | 10.9 KB | 1220ad8bc300... |
| ./fwa-lakes.pmtiles | 302.9 MB | 1220865e1a30... |
| ./styles/default.json | 469 B | 1220e8d33255... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fwa-lakes.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/freshwater-atlas-lakes](https://catalogue.data.gov.bc.ca/dataset/freshwater-atlas-lakes)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: FWA_LAKES_POLY.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
