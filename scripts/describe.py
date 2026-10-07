"""Fill table:columns descriptions in catalog/*/collection.json from the BC Data Catalogue.

Column comments (attested) are fetched per table by `python3 scripts/describe.py --fetch`
into .work/dict/<TABLE>.json. Also drops table:columns entries no file in the collection
has (portolan-cli 0.8.0 keeps stale ones, portolan-cli#931). Run from the repo root after
`portolan add`. Stdlib only.
"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT, DICT = ROOT / "catalog", ROOT / ".work" / "dict"
CKAN = "https://catalogue.data.gov.bc.ca/api/3/action/package_show?id="

# collection -> [(BCGW table, BC Data Catalogue dataset slug)]
BC = {
    "municipalities": [("ABMS_MUNICIPALITIES_SP", "municipalities-legally-defined-administrative-areas-of-bc")],
    "fwa-lakes": [("FWA_LAKES_POLY", "freshwater-atlas-lakes")],
    "fwa-rivers": [("FWA_RIVERS_POLY", "freshwater-atlas-rivers")],
    "fwa-wetlands": [("FWA_WETLANDS_POLY", "freshwater-atlas-wetlands")],
    "water-wells": [("GW_WATER_WELLS_WRBC_SVW", "groundwater-wells")],
    "aquifers": [("GW_AQUIFERS_CLASSIFICATION_SVW", "ground-water-aquifers")],
    "wildfire-incidents": [("PROT_HISTORICAL_INCIDENTS_SP", "bc-wildfire-fire-incident-locations-historical")],
    "wildfire-perimeters": [("PROT_HISTORICAL_FIRE_POLYS_SP", "bc-wildfire-fire-perimeters-historical")],
    "schools": [("GSR_SCHOOLS_K_TO_12_SVW", "bc-schools-k-12-with-francophone-indicators")],
    "hospitals": [("GSR_HOSPITALS_SVW", "hospitals-in-bc")],
    "recreation-trails": [("FTEN_RECREATION_LINES_SVW", "recreation-line")],
    "culverts": [("MOT_CULVERTS_SP", "ministry-of-transportation-mot-culverts")],
    "hydrometric-stations": [("ENVCAN_HYDROMETRIC_STN_SP", "hydrometric-stations-active-and-discontinued")],
    "parks": [("TA_PARK_ECORES_PA_SVW", "bc-parks-ecological-reserves-and-protected-areas")],
}


def fetch():
    DICT.mkdir(parents=True, exist_ok=True)
    for tables in BC.values():
        for table, slug in tables:
            res = json.load(__import__("urllib.request").request.urlopen(CKAN + slug))["result"]["resources"]
            cols = {}
            for r in res:
                if (r.get("object_name") or "").endswith("." + table) and r.get("details"):
                    d = r["details"]
                    for c in json.loads(d) if isinstance(d, str) else d:
                        cols[c["column_name"]] = c.get("column_comments") or ""
            (DICT / f"{table}.json").write_text(json.dumps(cols, indent=1))
            print(table, len(cols))


def file_columns(coll):
    names = set()
    for pq in coll.glob("*.parquet"):
        out = subprocess.run(["duckdb", "-json", "-c", f"DESCRIBE SELECT * FROM read_parquet('{pq}')"],
                             capture_output=True, text=True, check=True).stdout
        names |= {r["column_name"] for r in json.loads(out)}
    return names


def describe():
    for cj in sorted(CAT.glob("*/collection.json")):
        coll, c = cj.parent, json.loads(cj.read_text())
        known = {}
        for table, _ in BC.get(coll.name, []):
            known.update(json.loads((DICT / f"{table}.json").read_text()))
        have = file_columns(coll)
        cols = [col for col in c.get("table:columns", []) if col["name"] in have]
        stale = {col["name"] for col in c.get("table:columns", [])} - have
        missing = []
        for col in cols:
            text = known.get(col["name"], "")
            if text.strip():
                col["description"] = " ".join(text.split())
            elif col["name"] not in ("geometry", "geometry_bbox"):
                missing.append(col["name"])
        c["table:columns"] = cols
        cj.write_text(json.dumps(c, indent=2) + "\n")
        print(f"{coll.name}: {len(cols)} cols, dropped stale {sorted(stale) or '-'}, undescribed {missing or '-'}")


if __name__ == "__main__":
    fetch() if "--fetch" in sys.argv else describe()
