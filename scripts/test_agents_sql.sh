#!/usr/bin/env bash
# Run every ```sql block in catalog/**/AGENTS.md with DuckDB, so no documented
# query ships broken. Blocks reference the published URLs; by default they are
# rewritten to the local catalog. Pass --live to run them against the host.
# Usage: scripts/test_agents_sql.sh [--live]
set -uo pipefail
cd "$(dirname "$0")/.."
BASE="https://data.source.coop/alukach/bc-open-data/"
fail=0 n=0
for md in catalog/AGENTS.md catalog/*/AGENTS.md; do
  # one block per record, separated by NUL
  while IFS= read -r -d '' sql; do
    n=$((n + 1))
    [ "${1:-}" = --live ] || sql=${sql//$BASE/catalog\/}
    if out=$(duckdb -c "INSTALL spatial; LOAD spatial; $sql" 2>&1) && ! grep -q 'Error' <<<"$out"; then
      echo "ok   $md #$n"
    else
      echo "FAIL $md #$n"; echo "$out" | head -5; fail=1
    fi
  done < <(awk '/^```sql/{f=1; b=""; next} /^```/{if(f){printf "%s%c", b, 0}; f=0; next} f{b=b $0 "\n"}' "$md")
done
echo "$n queries"; exit $fail
