"""Refresh file:size / file:checksum on every collection asset after `portolan readme`.

ponytail: workaround. `portolan readme` (portolan-cli 0.8.0) rewrites README.md without
re-stamping the `documentation` asset, so `portolan check` reports PTL-DAT-001/002.
Delete this once the CLI stamps it. Run with the CLI's interpreter:
  ~/.local/share/uv/tools/portolan-cli/bin/python -I scripts/restamp.py
"""
import json, pathlib
from portolan_cli.stac_parquet import stamp_file_fields

for cj in sorted((pathlib.Path(__file__).resolve().parent.parent / "catalog").glob("*/collection.json")):
    c = json.loads(cj.read_text())
    if any([stamp_file_fields(a, cj.parent) for a in c.get("assets", {}).values()]):
        cj.write_text(json.dumps(c, indent=2) + "\n")
        print("restamped", cj.parent.name)
