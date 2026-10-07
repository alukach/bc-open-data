# Hospitals in BC

91 hospitals listed by HealthLinkBC, with address, hours and services. Published by HealthLinkBC (Province of British Columbia) as [Hospitals in BC](https://catalogue.data.gov.bc.ca/dataset/hospitals-in-bc) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![Directory](https://img.shields.io/badge/Directory-blue) ![FIND](https://img.shields.io/badge/FIND-blue) ![FIND Services and Resources](https://img.shields.io/badge/FIND_Services_and_Resources-blue) ![Health](https://img.shields.io/badge/Health-blue) ![HealthLink](https://img.shields.io/badge/HealthLink-blue) ![HealthLink BC](https://img.shields.io/badge/HealthLink_BC-blue) ![HealthLinkBC](https://img.shields.io/badge/HealthLinkBC-blue) ![Link](https://img.shields.io/badge/Link-blue) ![healthlinkbc](https://img.shields.io/badge/healthlinkbc-blue) ![hospital](https://img.shields.io/badge/hospital-blue) ![link](https://img.shields.io/badge/link-blue)

## Spatial Coverage

- **Bounding Box**: [-135.04361900081688, 48.4340609, -115.05660000070031, 60.71893900005339]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| CUSTODIAN_ORG_DESCRIPTION | string | CUSTODIAN_ORG_DESCRIPTION contains the name or description of the custodial organization (usually Ministry and Branch) |
| BUSINESS_CATEGORY_CLASS | string | BUSINESS_CATEGORY_CLASS designates the category of business, i.e., hospitals |
| BUSINESS_CATEGORY_DESCRIPTION | string | BUSINESS_CATEGORY_DESCRIPTION describes the category of business, i.e., Hospitals |
| OCCUPANT_TYPE_DESCRIPTION | string | OCCUPANT_TYPE_DESCRIPTION contains the description of the occupant type, e.g. Hospital |
| SOURCE_DATA_ID | string | A unique occupant id either supplied by the source data system or produced by GSR, depending on the value of SUPPLIED_SOURCE_ID_IND |
| SUPPLIED_SOURCE_ID_IND | string | SUPPLIED_SOURCE_ID_IND is an indicator of whether the source data id was supplied by the supplier (Y) or DataBC (N) |
| OCCUPANT_NAME | string | A business name that can identify the occupant who provides the BC Government or BC Government related services to public. |
| DESCRIPTION | string | Describes the Occupant in more detail. e.g., Burnaby General Hospital (BGH) that is managed by Fraser Health Authority provides a wide range of integrated health care services from acute care hospitals to community-based residential, home health, mental health and public health. |
| PHYSICAL_ADDRESS | string | PHYSICAL_ADDRESS contains the civic or non-civic address as a single string, structured according to the specification of the Physical Address and Geocoding Standard, e.g., 420 GORGE RD E, VICTORIA, BC. |
| ALIAS_ADDRESS | string | ALIAS_ADDRESS contains an address string, not a parsed address. It is the address that will be displayed for presentation purposes, e.g., 32900 Marshall Road, Abbotsford, BC |
| STREET_ADDRESS | string | A free form expression of the site descriptor (e.g., unit) and the civic building number / street / street indicator portion of an address, e.g., Unit 1, 123 Main Street East. |
| POSTAL_CODE | string | The Canadian Postal code value associated with the physical address, e.g., V9Z 2K1 |
| LOCALITY | string | The name of the municipality, community, Federal Indian Reserve (IR), subdivision, regional district, indigenous land or natural feature the occupant site is located in, e.g., Victoria, Saanich IR 1, Capital Regional District. |
| CONTACT_PHONE | string | Contains the "general office" phone number of the Occupant, e.g., 250-555-1234 |
| CONTACT_EMAIL | string | Contains the "general office" email address of the Occupant. |
| CONTACT_FAX | string | CONTACT_FAX contains the "general office" fax number of the Occupant, e.g., 250-555-1234 |
| WEBSITE_URL | string | Contains the link to the Home page of the Occupant's Website |
| IMAGE_URL | string | IMAGE_URL contains a full URL link to a picture of the Occupant's Location. |
| KEYWORDS | string | Contains text strings supplied by the Custodian, to be used for search/query purposes. Keywords are separated by the ; delimiter. |
| DATE_UPDATED | timestamp[ms] | Contains the date that the Occupant data was updated in the Occupant structure (system-generated) |
| SITE_GEOCODED_IND | string | SITE_GEOCODED_IND contains a Flag/indicator (Y/N) that the Occupant Physical Address has been geo-coded by the DataBC Address Geocoder and the results provide a valid site address, e.g., Y, N |
| HOURS | string | Indicates the hours of operation. |
| LANGUAGE | string | Indicates the languages available for the Service. |
| ORGANIZATION_NAME | string | Describes the Organization Name. |
| PROVINCE | string | Indicates the Province the service is located in, i.e., BC, YT. |
| URL_811 | string | URL Link to 811 Service Record. |
| WHEELCHAIR_ACCESSIBLE | string | Indicates whether Location is Wheelchair Accessible, i.e., Y, N. |
| SERVICE_REF | int32 | A unique number, called an Internal Service Key, that is assigned to uniquely identify the service or program, e.g., 17640736. |
| SEQUENCE_ID | int32 | SEQUENCE_ID contains a value to distinguish occupant instances. Where a single occupant can have multiple instances (representing different services, for example), this field distinguishes this occupant instance from other instances of the same or different occupants. |
| SE_ANNO_CAD_DATA | string | A binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./hospitals.thumb.jpg | 5.5 KB | 1220dd57ec3a... |
| ./README.md | 7.4 KB | 12200bfeb771... |
| ./hospitals.parquet | 32.0 KB | 122096db6589... |
| ./hospitals.pmtiles | 472.6 KB | 1220459df8cc... |
| ./styles/default.json | 514 B | 122043ffbd14... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./hospitals.thumb.jpg")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/hospitals-in-bc](https://catalogue.data.gov.bc.ca/dataset/hospitals-in-bc)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: GSR_HOSPITALS_SVW.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

## Known Issues

CONTACT_* columns hold institutional switchboards, not personal contacts.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
