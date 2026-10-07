# British Columbia Open Data

Build code for [source.coop/alukach/bc-open-data](https://source.coop/alukach/bc-open-data): province-wide
mirrors of openly licensed [BC Data Catalogue](https://catalogue.data.gov.bc.ca/) datasets as GeoParquet and
PMTiles, published as a [Portolan](https://github.com/portolan-sdi/portolan-spec) catalog. Data is under the
[Open Government Licence – British Columbia](https://www2.gov.bc.ca/gov/content/data/policy-standards/open-data/open-government-licence-bc).

`catalog/` holds the STAC metadata, styles and agent guides; the data files are not tracked. To rebuild:

```bash
scripts/extract.sh            # province-wide WFS extraction -> catalog/<collection>/<collection>.parquet
scripts/tile.sh               # PMTiles, zooms 0-13
scripts/register.sh <collections...>   # portolan add, working around portolan-cli#929
python3 scripts/describe.py --fetch && python3 scripts/describe.py   # column descriptions
python3 scripts/styles.py     # MapLibre styles from measured values
scripts/test_agents_sql.sh    # run every query in the AGENTS.md files
```

Remaining work is tracked in [#1](https://github.com/alukach/bc-open-data/issues/1).
