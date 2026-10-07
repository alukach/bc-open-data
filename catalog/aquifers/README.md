# Ground Water Aquifers

1,166 mapped and classified aquifers, with material, productivity, vulnerability and demand ratings. Published by Watershed Stewardship and Security (Province of British Columbia) as [Ground Water Aquifers](https://catalogue.data.gov.bc.ca/dataset/ground-water-aquifers) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![Canada](https://img.shields.io/badge/Canada-blue) ![Hydrology](https://img.shields.io/badge/Hydrology-blue) ![aquifer](https://img.shields.io/badge/aquifer-blue) ![groundwater](https://img.shields.io/badge/groundwater-blue)

## Spatial Coverage

- **Bounding Box**: [-132.20144848633245, 48.3089158, -114.8244539318539, 58.951101]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| GW_A_SYSID | int32 | GW_A_SYSID is a system generated unique identification number |
| AQUIFER_ID | int32 | System generated sequential number assigned to the aquifer. It is widely used by ground water administration staff as it is the only consistent unique identifier for a mapped aquifer. It is also commonly referred to as Aquifer Number, e.g. 1100. |
| NAME | string | Name assigned for a specific aquifer. Typically derived from geographic names or names in common use, but may also be lithologic or litho-stratigraphic units, e.g. Abbotsford-Sumas, McDougall Creek Deltaic. |
| MAPPING_YEAR | int32 | The year the aquifer was initially mapped or last updated. |
| LOCATION | string | Brief description of the geographic location of the aquifer. The description is usually referenced to a nearby major natural geographic area or community, e.g., Grand Forks. |
| MATERIAL | string | Describes the broad grouping of geological material found in the aquifer, i.e., Sand and Gravel, Sand, Gravel, Bedrock |
| SUBTYPE | string | Description that defines how the aquifer was formed geologically (depositional description), e.g., Unconfined sand and gravel - large river system, Confined sand and gravel - glacial, Flat-lying to gently-dipping volcanic bedrock. |
| AQUIFER_DETAILS_URL | string | Link to aquifer summary report within the Groundwater Wells and Aquifer (GWELLS) application. The aquifer summary provides the overall desription and history of the aquifer. |
| LITHO_STRATOGRAPHIC_UNIT | string | Permeable geologic unit (where available) that comprises the aquifer. It is typically either: the era of deposition, the name of a specific formation, and/or the broad material types, e.g., Paleozoic to Mesozoic Era, Cache Creek Complex, Intrusive Rock. |
| VULNERABILITY | string | The aquifer's relative intrinsic vulnerability to impacts from human activities on the land surface. Vulnerability is based on: the type, thickness, and extent of geologic materials above the aquifer, depth to water table (or to top of confined aquifer), and type of aquifer materials, i.e., Low, Moderate, High. |
| PRODUCTIVITY | string | The aquifer's productivity which represents an aquifer's ability to transmit and yield groundwater, i.e., Low, Moderate, High. |
| DEMAND | string | The level of groundwater use at the time the aquifer was mapped, i.e., High, Moderate, Low. |
| WATER_USE | string | The type of known water use of an aquifer at the time the aquifer was mapped. It indicates the variability or diversity of uses of the aquifer water as a supply source, e.g., Domestic, Multiple, Potential Domestic. |
| QUALITY_CONCERN | string | Standard terms used to represent the extent of documented concerns of contaminants in the aquifer at the time the aquifer was mapped. i.e. isolated, local, regional, none. |
| NOTES | string | Details about the mapped aquifer that the province deems important to maintain such as local knowledge about the aquifer or decisions for changes related to attributes of the mapped aquifer. |
| FEATURE_AREA_SQM | double | FEATURE_AREA_SQM is the system calculated area of a two-dimensional polygon in square meters. |
| FEATURE_LENGTH_M | double | FEATURE_LENGTH_M is the system calculated length or perimeter of a geometry in meters. |
| OBJECTID | int32 | OBJECTID is a column required by spatial layers that interact with ESRI ArcSDE. It is populated with unique values automatically by SDE. |
| SE_ANNO_CAD_DATA | string | SE_ANNO_CAD_DATA is a binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./aquifers.thumb.jpg | 11.1 KB | 12201c5e1d35... |
| ./README.md | 6.4 KB | 12207ef19587... |
| ./aquifers.parquet | 6.9 MB | 1220bba9dbd1... |
| ./aquifers.pmtiles | 12.1 MB | 12201484725a... |
| ./styles/default.json | 721 B | 122096f24b9d... |
| ./styles/material.json | 674 B | 1220ed327204... |
| ./styles/productivity.json | 702 B | 1220250fd38a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./aquifers.thumb.jpg")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/ground-water-aquifers](https://catalogue.data.gov.bc.ca/dataset/ground-water-aquifers)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: GW_AQUIFERS_CLASSIFICATION_SVW.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
