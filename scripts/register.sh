#!/usr/bin/env bash
# Register collections with Portolan without tripping portolan-cli#929: an existing
# sibling .pmtiles gets registered as a *data* asset. So the tiles are moved aside while
# the GeoParquet is added, then registered as the `-tiles` visual derivative through the
# CLI's own helper. Re-stamps file fields afterwards (portolan-cli#930).
# Usage: scripts/register.sh <collection>...   (run after extract.sh and tile.sh)
set -euo pipefail
cd "$(dirname "$0")/../catalog"
PY=~/.local/share/uv/tools/portolan-cli/bin/python
HOLD=../.work/pmtiles-hold

for c in "$@"; do mkdir -p "${HOLD:?}/${c:?}"; mv "${c:?}"/*.pmtiles "${HOLD:?}/${c:?}/"; done
portolan add "$@" --no-thumbnails --datetime 2026-10-07
for c in "$@"; do mv "${HOLD:?}/${c:?}/"*.pmtiles "${c:?}/" && rmdir "${HOLD:?}/${c:?}"; done

"$PY" -I - "$@" <<'EOF'
import json, sys
from pathlib import Path
from portolan_cli.viz.pmtiles import add_pmtiles_asset_to_collection
for c in sys.argv[1:]:
    d = Path(c).resolve()
    for pm in sorted(d.glob("*.pmtiles")):
        add_pmtiles_asset_to_collection(d, pm.stem, f"./{pm.name}")
    cj = d / "collection.json"; col = json.loads(cj.read_text())
    for a in col["assets"].values():  # belt and braces: tiles are always visual
        if a["href"].endswith(".pmtiles"):
            a["roles"] = ["visual"]
    cj.write_text(json.dumps(col, indent=2) + "\n")
    print("registered", c)
EOF
portolan check --fix >/dev/null  # adds rel:pmtiles links
"$PY" -I ../scripts/restamp.py
