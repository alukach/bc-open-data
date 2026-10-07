# British Columbia Open Data

![British Columbia](https://img.shields.io/badge/British_Columbia-blue) ![BC](https://img.shields.io/badge/BC-blue) ![Canada](https://img.shields.io/badge/Canada-blue) ![open data](https://img.shields.io/badge/open_data-blue) ![BC Data Catalogue](https://img.shields.io/badge/BC_Data_Catalogue-blue) ![DataBC](https://img.shields.io/badge/DataBC-blue)

Province-wide mirrors of openly licensed datasets from the [BC Data Catalogue](https://catalogue.data.gov.bc.ca/), converted from the Province's web services to GeoParquet (query directly with DuckDB over HTTPS) and PMTiles. Independent mirror, not a Province of British Columbia publication; every collection is under the [Open Government Licence – British Columbia](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc). Start with [AGENTS.md](AGENTS.md) for query recipes. Build code and issues: [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data).

## Collections

<details>
<summary>📁 14 collections (click to expand)</summary>

### [Ground Water Aquifers](catalog/aquifers/)

1,166 mapped and classified aquifers, with material, productivity, vulnerability and demand ratings. Published by Watershed Stewardship and Security (Province of British Columbia) as [Ground Water ...

### [Ministry of Transportation (MOT) Culverts](catalog/culverts/)

186,427 culverts on Ministry of Transportation roads, with material, size, installation date and fish-passage attributes. Published by Construction and Maintenance (Province of British Columbia) as...

### [Freshwater Atlas - Lakes](catalog/fwa-lakes/)

386,025 lake polygons from the Freshwater Atlas, BC's 1:20,000 corporate watershed base. Published by GeoBC Branch (Province of British Columbia) as [Freshwater Atlas - Lakes](https://catalogue.dat...

### [Freshwater Atlas - Rivers](catalog/fwa-rivers/)

37,083 double-line river polygons from the Freshwater Atlas: the wide rivers mapped as areas rather than lines. Published by GeoBC Branch (Province of British Columbia) as [Freshwater Atlas - River...

### [Freshwater Atlas - Wetlands](catalog/fwa-wetlands/)

375,178 wetland polygons from the Freshwater Atlas. Published by GeoBC Branch (Province of British Columbia) as [Freshwater Atlas - Wetlands](https://catalogue.data.gov.bc.ca/dataset/freshwater-atl...

### [Hospitals in BC](catalog/hospitals/)

91 hospitals listed by HealthLinkBC, with address, hours and services. Published by HealthLinkBC (Province of British Columbia) as [Hospitals in BC](https://catalogue.data.gov.bc.ca/dataset/hospita...

### [Hydrometric Stations - Active and Discontinued](catalog/hydrometric-stations/)

2,317 active and discontinued Water Survey of Canada water level and streamflow stations in BC. Published by Environmental Monitoring and Analysis Branch (Province of British Columbia) as [Hydromet...

### [Municipalities - Legally Defined Administrative Areas of BC](catalog/municipalities/)

The legally defined boundaries of BC's 160 municipalities (cities, districts, towns, villages and other local governments). Published by Governance and Structure (Province of British Columbia) as [...

### [BC Parks, Ecological Reserves, and Protected Areas](catalog/parks/)

930 BC Parks, ecological reserves and protected areas. Published by BC Parks (Province of British Columbia) as [BC Parks, Ecological Reserves, and Protected Areas](https://catalogue.data.gov.bc.ca/...

### [Recreation Line](catalog/recreation-trails/)

19,936 recreation trail and feature lines managed by Recreation Sites and Trails BC. Published by Recreation Sites and Trails BC (Province of British Columbia) as [Recreation Line](https://catalogu...

### [BC Schools - K-12 with Francophone Indicators](catalog/schools/)

1,914 K-12 schools with category, grade level, district and French-language program indicators. Published by Education Analytics Office (Province of British Columbia) as [BC Schools - K-12 with Fra...

### [Groundwater Wells](catalog/water-wells/)

130,946 groundwater wells registered in the provincial GWELLS registry, with construction, depth, yield and aquifer. Published by Watershed Stewardship and Security (Province of British Columbia) a...

### [BC Wildfire Fire Incident Locations - Historical](catalog/wildfire-incidents/)

200,479 historical wildfire incident locations recorded by the BC Wildfire Service, with cause, year, size and response. Published by BC Wildfire Service (Province of British Columbia) as [BC Wildf...

### [BC Wildfire Fire Perimeters - Historical](catalog/wildfire-perimeters/)

24,751 mapped historical wildfire perimeters from the BC Wildfire Service. Published by BC Wildfire Service (Province of British Columbia) as [BC Wildfire Fire Perimeters - Historical](https://cata...

</details>

## Coverage

**Spatial Extent**

- West: -139.5190, South: 45.1788, East: -112.2320, North: 60.7189

## Processing Notes

Extracted province-wide on 2026-10-07 from the [BC Geographic Warehouse WFS](https://openmaps.gov.bc.ca/geo/pub/wfs) by scripts/extract.sh in [github.com/alukach/bc-open-data](https://github.com/alukach/bc-open-data): pages of 10,000 features sorted by OBJECTID, row count checked against the server's numberMatched. Geometry is kept in the source CRS, EPSG:3005 (BC Albers); the file is spatially sorted with a bbox covering column. Dropped: GeoServer's synthetic `id`, and LATITUDE/LONGITUDE where the geometry carries them. PMTiles by scripts/tile.sh (tippecanoe, zooms 0-13).

## Attribution

Contains information licensed under the Open Government Licence – British Columbia.

## License

[other](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc)

## Contact

Anthony Lukach <anthonylukach@gmail.com>

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
