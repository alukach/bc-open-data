# BC Wildfire Fire Incident Locations - Historical

200,479 historical wildfire incident locations recorded by the BC Wildfire Service, with cause, year, size and response. Published by BC Wildfire Service (Province of British Columbia) as [BC Wildfire Fire Incident Locations - Historical](https://catalogue.data.gov.bc.ca/dataset/bc-wildfire-fire-incident-locations-historical) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![emergency management](https://img.shields.io/badge/emergency_management-blue) ![fire location](https://img.shields.io/badge/fire_location-blue) ![fire point](https://img.shields.io/badge/fire_point-blue) ![incident location](https://img.shields.io/badge/incident_location-blue) ![incident points](https://img.shields.io/badge/incident_points-blue) ![wildfire](https://img.shields.io/badge/wildfire-blue)

## Spatial Coverage

- **Bounding Box**: [-139.5189999993196, 45.1788168, -112.23200000026732, 60.20100000041902]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| FIRE_NUMBER | string | A composite of the following fields: Zone, Fire ID and Fire Centre. |
| FIRE_YEAR | int32 | Represents the fiscal year, April 1 to March 31. |
| RESPONSE_TYPE_DESC | string | Describes the type of response an incident is receiving and is based on fire behaviour, potential risks and environmental factors. |
| IGNITION_DATE | timestamp[ms] | The discovery date of the fire. |
| FIRE_OUT_DATE | timestamp[ms] | The date the fire is deemed out. |
| FIRE_CAUSE | string | The suspected cause of the fire, e.g., Lightning, Person. |
| FIRE_LABEL | string | The concatenation of Fire Number and Fire Year. |
| FIRE_CENTRE | int32 | Represents the BC Wildfire Service Centre administrative area. |
| ZONE | int32 | A subset of the BC Wildfire Service Centre administrative area. |
| FIRE_ID | int32 | A unique number, system-generated, within a fire year and fire centre. |
| FIRE_TYPE | string | Defines the type of incident that occurred, e.g., Fire, Nuisance Fire, Smoke Chase. |
| INCIDENT_NAME | string | The official name of the wildfire. |
| GEOGRAPHIC_DESCRIPTION | string | A description of the approximate fire location: IC must note how far and in what direction the wildfire is in relation to a geographic reference. Note: for Railroad fires, actual railroad mileage is iuncluded as part of the geographic information, e.g., Sallus Creek, 172 mile-marker on railroad. |
| CURRENT_SIZE | double | The estimated size of the area within the outside perimeter of the incident, in hectares. |
| FEATURE_CODE | string | Contains an alphanumeric value based on the Canadian Council of Surveys and Mappingâ€™s (CCSM) system for classification of geographic features, e.g., AR82000110. |
| OBJECTID | int32 | A column required by spatial layers that interact with ESRI ArcSDE. It is populated with unique values automatically by SDE. |
| SE_ANNO_CAD_DATA | string | A binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./wildfire-incidents.parquet | 10.9 MB | 1220ca3e7508... |
| ./wildfire-incidents.thumb.jpg | 14.3 KB | 1220ffa7a4e9... |
| ./README.md | 5.1 KB | 12208bfcc225... |
| ./wildfire-incidents.pmtiles | 90.4 MB | 12205a1704a0... |
| ./styles/default.json | 794 B | 1220b9c74944... |
| ./styles/fire-year.json | 817 B | 1220fbc65fcd... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./wildfire-incidents.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/bc-wildfire-fire-incident-locations-historical](https://catalogue.data.gov.bc.ca/dataset/bc-wildfire-fire-incident-locations-historical)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: PROT_HISTORICAL_INCIDENTS_SP.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
