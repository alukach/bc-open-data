"""Write MapLibre styles to catalog/<collection>/styles/<name>.json (BC catalog).

Every `match` branch is built from the values actually present in the GeoParquet,
largest first, so a legend can never list a category the map does not draw; the
counts are printed as the check. The data browser builds legends only from
fill-color / circle-color `match` or `step` expressions; line styles get none.
Run from the repo root, then `portolan add` to register new style files. Stdlib only.
"""
import json, pathlib, subprocess

CAT = pathlib.Path(__file__).resolve().parent.parent / "catalog"
OTHER = "#b0b0b0"
PALETTES = {  # varied across sibling collections so cards don't read as one dataset
    "bold": ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666"],
    "warm": ["#b2182b", "#ef8a62", "#fddbc7", "#67a9cf", "#2166ac", "#762a83", "#5aae61", "#1b7837"],
    "earth": ["#8c510a", "#d8b365", "#5ab4ac", "#01665e", "#c51b7d", "#4d9221", "#f1b6da", "#35978f"],
    "set": ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#a65628", "#f781bf", "#999999"],
}
RAMPS = {
    "green": ["#edf8e9", "#c7e9c0", "#a1d99b", "#74c476", "#41ab5d", "#238b45", "#006d2c", "#00441b", "#002a10"],
    "orange": ["#feedde", "#fdbe85", "#fd8d3c", "#e6550d", "#a63603"],
    "purple": ["#f2f0f7", "#cbc9e2", "#9e9ac8", "#756bb1", "#54278f"],
}


def values(coll, item, col, limit=8):
    sql = (f"SELECT {col}::VARCHAR v, count(*) n FROM read_parquet('{CAT / coll / item}.parquet') "
           f"WHERE {col} IS NOT NULL GROUP BY 1 ORDER BY 2 DESC LIMIT {limit}")
    return [(r["v"], r["n"]) for r in json.loads(subprocess.run(
        ["duckdb", "-json", "-c", sql], capture_output=True, text=True, check=True).stdout or "[]")]


def match(coll, item, col, palette, numeric=False):
    vals = values(coll, item, col)
    print(f"  {coll}/{item}.{col}: " + ", ".join(f"{v}={n}" for v, n in vals))
    expr = ["match", ["get", col]]
    for (v, _), color in zip(vals, PALETTES[palette]):
        expr += [int(v) if numeric else v, color]
    return expr + [OTHER]


def step(col, stops, ramp):
    colors = RAMPS[ramp]
    expr = ["step", ["get", col], colors[0]]
    for s, c in zip(stops, colors[1:]):
        expr += [s, c]
    return expr


def src(item):
    return {"type": "vector", "url": f"pmtiles://../{item}.pmtiles", "minzoom": 0, "maxzoom": 13}


def fill(item, color, opacity=0.7, outline="#ffffff"):
    return {"id": f"{item}-fill", "type": "fill", "source": item, "source-layer": item,
            "paint": {"fill-color": color, "fill-opacity": opacity, "fill-outline-color": outline}}


def line(item, color, width=1.5, **paint):
    return {"id": f"{item}-line", "type": "line", "source": item, "source-layer": item,
            "paint": {"line-color": color, "line-width": width, **paint}}


def circle(item, color, radius=6):
    return {"id": f"{item}-circle", "type": "circle", "source": item, "source-layer": item,
            "paint": {"circle-color": color, "circle-radius": radius,
                      "circle-stroke-color": "#ffffff", "circle-stroke-width": 1.5}}


def write(coll, name, title, layers):
    items = sorted({l["source"] for l in layers})
    style = {"version": 8, "name": title, "sources": {i: src(i) for i in items}, "layers": layers}
    d = CAT / coll / "styles"
    d.mkdir(exist_ok=True)
    (d / f"{name}.json").write_text(json.dumps(style, indent=2) + "\n")


def main():
    for d in CAT.glob("*/styles"):  # regenerate from scratch; drops stale auto-generated styles
        for f in d.glob("*.json"):
            f.unlink()

    c = "municipalities"
    write(c, "default", "Municipal boundaries", [fill(c, "#f4a261", 0.35, "#e76f51"), line(c, "#e76f51", 1)])

    write("fwa-lakes", "default", "Lakes", [fill("fwa-lakes", "#3a86c8", 0.85, "#2b6aa0")])
    write("fwa-rivers", "default", "Double-line rivers", [fill("fwa-rivers", "#1f78b4", 0.9, "#1f78b4")])
    write("fwa-wetlands", "default", "Wetlands", [fill("fwa-wetlands", "#6aa84f", 0.75, "#4e8a3a")])

    c = "aquifers"
    write(c, "default", "Vulnerability to contamination", [fill(c, match(c, c, "VULNERABILITY", "warm"), 0.6)])
    write(c, "material", "Aquifer material", [fill(c, match(c, c, "MATERIAL", "earth"), 0.6)])
    write(c, "productivity", "Productivity", [fill(c, match(c, c, "PRODUCTIVITY", "bold"), 0.6)])

    c = "water-wells"
    write(c, "default", "Intended water use", [circle(c, match(c, c, "INTENDED_WATER_USE", "set"), 3)])
    write(c, "well-class", "Well class", [circle(c, match(c, c, "WELL_CLASS", "earth"), 3)])

    c = "wildfire-incidents"
    write(c, "default", "Cause", [circle(c, match(c, c, "FIRE_CAUSE", "warm"), 2.5)])
    write(c, "fire-year", "Fire year", [circle(c, step("FIRE_YEAR", [1960, 1980, 2000, 2020], "orange"), 2.5)])

    c = "wildfire-perimeters"
    write(c, "default", "Fire year", [fill(c, step("FIRE_YEAR", [1960, 1980, 2000, 2020], "orange"), 0.7)])
    write(c, "cause", "Cause", [fill(c, match(c, c, "FIRE_CAUSE", "warm"), 0.7)])

    c = "schools"
    write(c, "default", "School category", [circle(c, match(c, c, "SCHOOL_CATEGORY", "bold"), 4)])
    write(c, "education-level", "Grade levels", [circle(c, match(c, c, "SCHOOL_EDUCATION_LEVEL", "set"), 4)])

    write("hospitals", "default", "Hospitals", [circle("hospitals", "#c0392b", 6)])

    c = "recreation-trails"
    write(c, "default", "Feature type", [line(c, match(c, c, "PROJECT_TYPE", "set"), 1.5)])

    c = "culverts"
    write(c, "default", "Culvert material", [circle(c, match(c, c, "CULVERT_MATERIAL", "earth"), 2.5)])

    c = "hydrometric-stations"
    write(c, "default", "Operating status", [circle(c, match(c, c, "STATION_OPERATING_STATUS", "warm"), 4)])

    c = "parks"
    write(c, "default", "Designation", [fill(c, match(c, c, "PROTECTED_LANDS_DESIGNATION", "bold"), 0.6), line(c, "#1b5e20", 0.75)])
    write(c, "park-class", "Park class", [fill(c, match(c, c, "PARK_CLASS", "earth"), 0.6)])


if __name__ == "__main__":
    main()
