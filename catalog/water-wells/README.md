# Groundwater Wells

130,946 groundwater wells registered in the provincial GWELLS registry, with construction, depth, yield and aquifer. Published by Watershed Stewardship and Security (Province of British Columbia) as [Groundwater Wells](https://catalogue.data.gov.bc.ca/dataset/groundwater-wells) in the BC Data Catalogue; this is a full province-wide mirror. Query recipes and field notes are in [AGENTS.md](AGENTS.md).

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![Canada](https://img.shields.io/badge/Canada-blue) ![groundwater](https://img.shields.io/badge/groundwater-blue) ![gwells](https://img.shields.io/badge/gwells-blue) ![hydrogeology](https://img.shields.io/badge/hydrogeology-blue) ![water well](https://img.shields.io/badge/water_well-blue) ![well](https://img.shields.io/badge/well-blue)

## Spatial Coverage

- **Bounding Box**: [-136.36817000048836, 48.31277999986317, -114.50764500065941, 59.96051300040553]

## Temporal Coverage

- **Start**: open
- **End**: ongoing

## Schema

| Column | Type | Description |
|--------|------|-------------|
| GW_WW_SYSID | int32 | A system generated unique identification number |
| WELL_TAG_NUMBER | int32 | The file number assigned to a particular well in the in the provincial Groundwater Wells and Aquifers application, e.g., 56809. |
| IDENTIFICATION_PLATE_NUMBER | int32 | Steel plate with a unique number that is attached to required wells under the groundwater protection regulations such as water supply wells, recharge or injection wells made by drilling or boring, and permanent dewatering wells, e.g., 691. |
| STREET_ADDRESS | string | Street address of the property that the well is physically located on. |
| CITY | string | The city, town, or general locality where the well is located, e.g. Oliver, Gabriola Island. |
| LEGAL_LOT | string | The smallest designation of land (the lot number) from the legal description of the land parcel where the well is located, e.g., B, 2. |
| LEGAL_PLAN | string | The plan number from the legal description of the land parcel where the well is located, e.g., 1261, 13604, LMP7728. |
| LEGAL_DISTRICT_LOT | string | The district lot number from the legal description of the land parcel where the well is located, e.g., 456, 1234s. |
| LEGAL_PID | int32 | The parcel identifier (PID) of the land parcel where the well is located, e.g., 014905736. |
| WELL_LOCATION_DESCRIPTION | string | An informal description of where the well is located on a property, e.g., 50m to the right of the house and behind the shed. |
| COORDINATE_ACQUISITION_CODE | string | The approximate accuracy of the geographic coordinates provided, e.g., H (default accuracy; (10 m accuracy) handheld GPS with accuracy of +/- 10 meters), A (10 m accuracy - cadastre and good location sketch), C (50 m accuracy - Digitized from 1:20,000 mapping), I (20 m accuracy - no cadastre but good location sketch or good written description), G (unknown, accuracy based on parcel size - No cadastre, poor or no location sketch; site located in center of primary parcel), J (unknown, accuracy based on parcel size - cadastre, poor or no location sketch, arbitrarily located in center of parcel). |
| WELL_STATUS | string | Description of the status of a well as defined in the Groundwater Protection Regulation of the Water Act, i.e. New, Abandoned, Alteration, Closure, Other. |
| WELL_CLASS | string | Valid classification as defined in the Groundwater Protection Regulation of the Water Sustainability Act, i.e., Water Supply, Monitoring, Recharge, Injection, Dewatering, Drainage, Remediation, Geotechnical, Closed-loop geoexchange. |
| WELL_SUBCLASS | string | Valid subclassification as defined in the Groundwater Protection Regulation of the Water Sustainability Act, e.g., Temporary, Permanent, Borehole, Artesian. |
| INTENDED_WATER_USE | string | The intended use of the water in a water supply well as reported by the driller at time of work completion on the well, e.g., private domestic, irrigation, water supply system, industrial commercial, unknown. |
| WELL_DETAILS_URL | string | Link to the well summary report within the Groundwater Wells and Aquifer (GWELLS) application, which provides the overall description and history of the well. |
| LICENCE_STATUS | string | Description of valid licencing option granted to a well under the Water Water Sustainability Act. This information comes from eLicensing, i.e. Unlicensed, Licensed, Historical |
| AQUIFER_ID | int32 | System generated unique sequential number assigned to each mapped aquifer. The aquifer ID identifies which aquifer a well is in. An aquifer can have multiple wells, while a single well can only be in one aquifer. |
| PERSON_RESPONSIBLE | string | Name (and registration ID) of the registered driller or pump installer responsible for constructing, altering, or decommissioning the well, e.g., Jane Doe (WD 06666666). |
| COMPANY_OF_PERSON_RESPONSIBLE | string | Name (and location) of the registered driller or pump installer company responsible for constructing, altering, or decommissioning the well, e.g., Geotech Drilling Services Ltd. (Vernon, BC). |
| FINISHED_WELL_DEPTH | double | The depth at which the well was finished, measured in units of feet bgl (below ground level), e.g. 157.0. It can be shallower than the total well depth which is the total depth at which the well was drilled. |
| TOTAL_DEPTH_DRILLED | double | The deepest depth a well was drilled to, reported as feet below ground level, e.g., 150. |
| BEDROCK_DEPTH | double | Depth below ground level at which bedrock starts, measured in feet, e.g. 132.0. |
| YIELD | double | An approximate estimate of the capacity of the well to produce groundwater. Estimated by the well driller during construction by conducting a well yield test. Measured in US Gallons/minute. |
| YIELD_ESTIMATION_DURATION | double | Length of time (in hours) over which a yield test was conducted by the driller during construction to determine well yield, e.g., 3.25. |
| ARTESIAN_COND | string | Indicates whether artesian conditions are present for a given well, i.e., Y, N. |
| ARTESIAN_FLOW | double | Measurement of the artesian well water flow that occurs naturally due to inherent water pressure in the well. Pressure within the aquifer forces the groundwater to rise above the land surface naturally without using a pump. Flowing artesian wells can flow on an intermittent or continuous basis. Measured in US Gallons per minute. |
| ARTESIAN_PRESSURE | double | Pressure of the water coming out of an artesian well as measured at the time of well construction, measured in PSI (pounds per square inch). |
| STATIC_WATER_LEVEL | double | The level (depth below top of casing) to which water will naturally rise in a well without pumping, measured in feet, e.g. 280.0 |
| DIAMETER | double | The diameter of the casing of the well, measured in inches, e.g. 6.62. There can be multiple casings in a well, e.g. surface casing, and production casing. Diameter of casing made available to the public is generally the production casing. |
| FINAL_CASING_STICK_UP | double | Tthe length of the production casing in the well that is above either (a) the surface of the ground adjacent to the well, or (b) the floor of the well sump, pump house or well pit. Measured as inches, e.g., 30. |
| GROUND_ELEVATION | double | The elevation of the well at ground level. Measured as feet above sea level, e.g., 1050 |
| GROUND_ELEVATION_METHOD | string | Description of how ground elevation of the well was measured, e.g., unknown, GPS, level, 20K_map, 5K_map, DIFF_GPS, altimeter, 10K_map, 50K_map. |
| SURFACE_SEAL_DEPTH | double | The total depth (length) of the protective surface seal installed around the outside of the outermost casing or between multiple casings, measured in feet, e.g. 16. |
| SURFACE_SEAL_THICKNESS | double | The distance between the outside of the outermost casing and natural ground, or the distance between multiple casings in which the sealant is installed. Measured in inches, e.g., 2. |
| SURFACE_SEAL_METHOD | string | Method of how the surface seal was installed around the well casing, i.e., pumped, poured, other. |
| SCREEN_INTAKE_METHOD | string | Main entry for water into the well, i.e., open bottom, uncased hole, and screen. |
| WATER_SUPPLY_SYSTEM_NAME | string | Owner of the water supply system using the well, e.g., Township of Langley, Cedar Lake Water System, Copperside Estates. |
| WATER_SUPPLY_SYSTEM_WELL_NAME | string | Well name or identifier used by the water supply system, e.g., Well#5, north well, pine street well. |
| CONSTRUCTION_START_DATE | timestamp[ms] | The date that the well construction was started. |
| CONSTRUCTION_END_DATE | timestamp[ms] | The date that the well construction was completed. |
| ALTERATION_START_DATE | timestamp[ms] | The date that alteration works, such as increasing the well depth or diameter, were started. |
| ALTERATION_END_DATE | timestamp[ms] | The date that alteration works, such as increasing the well depth or diameter, were completed. |
| DECOMMISSION_START_DATE | timestamp[ms] | The date that closure works were started in order to take a well permanently out of service. |
| DECOMMISSION_END_DATE | timestamp[ms] | The date that closure works were completed in order to take a well permanently out of service. |
| DECOMMISSION_REASON | string | Description or rationale for why well was closed permanently, e.g., dry hole, no longer in use, contamination risk. |
| OBSERVATION_WELL_NUMBER | string | The number assigned to a well within the Provincial Groundwater Observation Well Network, e.g., 552. |
| OBSERVATION_WELL_STATUS | string | The current status of a well within the Provincial Groundwater Observation Well Network, e.g., Active, Inactive. |
| EMS_ID | string | A unique identifier from the provincial Environmental Monitoring System (EMS), to be used for connecting to any well monitoring data, e.g., E218071, 1401072. |
| AQUIFER_MATERIAL | string | A high-level description of the aquifer material type the well is located within, i.e., bedrock, unconsolidated, or unknown. |
| OBJECTID | int32 | A column required by spatial layers that interact with ESRI ArcSDE. It is populated with unique values automatically by SDE. |
| SE_ANNO_CAD_DATA | string | A binary column used by spatial tools to store annotation, curve features and CAD data when using the SDO_GEOMETRY storage data type. |
| geometry | binary |  |
| geometry_bbox | struct<xmin: float not null, ymin: float not null, xmax: float not null, ymax: float not null> |  |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./water-wells.parquet | 10.6 MB | 12201964617b... |
| ./README.md | 12.1 KB | 122005d253e4... |
| ./water-wells.thumb.jpg | 23.3 KB | 1220ab5f8d71... |
| ./water-wells.pmtiles | 69.6 MB | 12203e7a1913... |
| ./styles/default.json | 1.0 KB | 1220c89cddb8... |
| ./styles/well-class.json | 1010 B | 12202052440f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./water-wells.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://catalogue.data.gov.bc.ca/dataset/groundwater-wells](https://catalogue.data.gov.bc.ca/dataset/groundwater-wells)

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13). BCGW table: GW_WATER_WELLS_WRBC_SVW.

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

## Known Issues

STREET_ADDRESS and PERSON_RESPONSIBLE can identify private individuals; they are kept as the Province publishes them.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
