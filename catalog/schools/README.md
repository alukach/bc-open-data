# BC Schools - K-12 with Francophone Indicators

1,914 K-12 schools with category, grade level, district and French-language program indicators. Published by Education Analytics Office (Province of British Columbia) as [BC Schools - K-12 with Francophone Indicators](https://catalogue.data.gov.bc.ca/dataset/bc-schools-k-12-with-francophone-indicators) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![Elementary Junior Secondary](https://img.shields.io/badge/Elementary_Junior_Secondary-blue) ![Elementary Secondary](https://img.shields.io/badge/Elementary_Secondary-blue) ![Franocphone Program](https://img.shields.io/badge/Franocphone_Program-blue) ![High schools](https://img.shields.io/badge/High_schools-blue) ![Junior Secondary](https://img.shields.io/badge/Junior_Secondary-blue) ![Middle School](https://img.shields.io/badge/Middle_School-blue) ![Multi level mixed schools between K 12](https://img.shields.io/badge/Multi_level_mixed_schools_between_K_12-blue) ![core french](https://img.shields.io/badge/core_french-blue) ![early French immersion](https://img.shields.io/badge/early_French_immersion-blue) ![elementary](https://img.shields.io/badge/elementary-blue) ![elementary schools](https://img.shields.io/badge/elementary_schools-blue)

## Spatial Coverage

- **Bounding Box**: [-133.6091357, 48.36407280001382, -114.89155190039531, 59.92429599971936]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| CUSTODIAN_ORG_DESCRIPTION | string | CUSTODIAN_ORG_DESCRIPTION contains the name or description of the custodial organization (usually Ministry and Branch) |
| BUSINESS_CATEGORY_CLASS | string | BUSINESS_CATEGORY_CLASS designates the category of business, i.e., elementaryAndSecondarySchools |
| BUSINESS_CATEGORY_DESCRIPTION | string | BUSINESS_CATEGORY_DESCRIPTION describes the category of business, i.e., Elementary and secondary schools |
| OCCUPANT_TYPE_DESCRIPTION | string | OCCUPANT_TYPE_DESCRIPTION contains the description of the occupant type, e.g. Hospital |
| SOURCE_DATA_ID | string | SOURCE_DATA_ID is a unique occupant id either supplied by the source data system or produced by GSR, depending on the value of SUPPLIED_SOURCE_ID_IND |
| SUPPLIED_SOURCE_ID_IND | string | SUPPLIED_SOURCE_ID_IND is an indicator of whether the source data id was supplied by the supplier (Y) or DataBC (N) |
| OCCUPANT_NAME | string | OCCUPANT_NAME is a business name that can identify the occupant who provides the BC Government or BC Government related services to public. |
| DESCRIPTION | string | DESCRIPTION describes the Occupant in more detail |
| PHYSICAL_ADDRESS | string | PHYSICAL_ADDRESS contains the civic or non-civic address as a single string, structured according to the specification of the Physical Address and Geocoding Standard, e.g., 420 GORGE RD E, VICTORIA, BC. |
| ALIAS_ADDRESS | string | ALIAS_ADDRESS contains an address string, not a parsed address. It is the address that will be displayed for presentation purposes, e.g., 32900 Marshall Road, Abbotsford, BC |
| STREET_ADDRESS | string | STREET_ADDRESS is a free form expression of the site descriptor (e.g., unit) and the civic building number / street / street indicator portion of an address, e.g., Unit 1, 123 Main Street East. |
| POSTAL_CODE | string | POSTAL_CODE is the Canadian Postal code value associated with the physical address, e.g., V9Z 2K1 |
| LOCALITY | string | LOCALITY is the name of the municipality, community, Federal Indian Reserve (IR), subdivision, regional district, indigenous land or natural feature the occupant site is located in, e.g., Victoria, Saanich IR 1, Capital Regional District. |
| CONTACT_PHONE | string | CONTACT_PHONE contains the "general office" phone number of the Occupant, e.g., 250-555-1234 |
| CONTACT_EMAIL | string | CONTACT_EMAIL contains the "general office" email address of the Occupant. |
| CONTACT_FAX | string | CONTACT_FAX contains the "general office" fax number of the Occupant, e.g., 250-555-1234 |
| WEBSITE_URL | string | WEBSITE_URL contains the link to the Home page of the Occupant's Website |
| IMAGE_URL | string | IMAGE_URL contains a full URL link to a picture of the Occupant's Location. |
| KEYWORDS | string | KEYWORDS contains text strings supplied by the Custodian, to be used for search/query purposes. Keywords are separated by the ; delimiter. |
| DATE_UPDATED | date32[day] | DATE_UPDATED contains the date that the Occupant data was updated in the Occupant structure (system-generated) |
| SITE_GEOCODED_IND | string | SITE_GEOCODED_IND contains a Flag/indicator (Y/N) that the Occupant Physical Address has been geo-coded by the DataBC Address Geocoder and the results provide a valid site address, e.g., Y, N |
| CORE_FRENCH_OFFERED | string | CORE_FRENCH_OFFERED identifies whether the school offers a Core French program. Valid values are "YES" or "NO". |
| DISTRICT_NAME | string | DISTRICT_NAME is the name of the school district, e.g. Southeast Kootenay. |
| DISTRICT_NUMBER | string | DISTRICT_NUMBER is a 3 digit code used to identify school district, e.g. 005 |
| EARLY_FRENCH_IMMERSION_OFFERED | string | EARLY_FRENCH_IMMERSION_OFFERED identifies whether the school offers an early French Immersion program. Valid values are "YES" or "NO". |
| FACILITY_TYPE | string | FACILITY_TYPE is the type of school facility, e.g. District Distance Ed |
| FRANCOPHONE_PROGRAM_OFFERED | string | FRANCOPHONE_PROGRAM_OFFERED identifies whether the school offers a Francophone program. Valid values are "YES" or "NO". |
| LATE_FRENCH_IMMERSION_OFFERED | string | LATE_FRENCH_IMMERSION_OFFERED identifies whether the school offers a late French Immersion program. Valid values are "YES" or "NO". |
| SCHOOL_CATEGORY | string | SCHOOL_CATEGORY identifies if the school is public, independent, long distance, e.g. BC PUBLIC SCHOOL |
| SCHOOL_EDUCATION_LEVEL | string | SCHOOL_EDUCATION_LEVEL indicates the level of education offered by the school, e.g. ELEMENTARY, SECONDARY. |
| SCHOOL_NUMBER | string | SCHOOL_NUMBER is a code assigned to the school for this enrollment period. |
| SCHOOL_YEAR | string | SCHOOL_YEAR indicates the enrolment period, e.g. 2012/2013. |
| SEQUENCE_ID | int32 | SEQUENCE_ID contains a value to distinguish occupant instances. Where a single occupant can have multiple instances (representing different services, for example), this field distinguishes this occupant instance from other instances of the same or different occupants. |
| SE_ANNO_CAD_DATA | string | SE_ANNO_CAD_DATA is a binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./README.md | 8.6 KB | 122042193864... |
| ./schools.thumb.jpg | 5.9 KB | 12203e10a1db... |
| ./schools.parquet | 165.1 KB | 1220edec4e80... |
| ./schools.pmtiles | 2.5 MB | 1220799853d6... |
| ./styles/default.json | 726 B | 1220c986990f... |
| ./styles/education-level.json | 982 B | 12207442b01f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./README.md")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/bc-schools-k-12-with-francophone-indicators](https://catalogue.data.gov.bc.ca/dataset/bc-schools-k-12-with-francophone-indicators)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: GSR_SCHOOLS_K_TO_12_SVW.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

## Known Issues

CONTACT_* columns hold school switchboards, not personal contacts.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
