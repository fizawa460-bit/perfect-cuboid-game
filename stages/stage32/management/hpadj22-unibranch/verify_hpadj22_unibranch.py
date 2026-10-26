#!/usr/bin/env python3
"""Stage32 HPADJ22-UNIBRANCH: HPADJ22 direct count composed with the UNIBRANCH-NODE-HURWITZ support requirement.

Reuses, unchanged and blob-locked:
  * the HPADJ22 direct counter  stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py
    (consumed by V44..V47 as "MIN of current authority and exact HPADJ22 direct count"), and
  * its source chain at HPADJ22 head 4bd68ded (pass a checkout of that commit as --source-root).

Only change: in the e-eligibility test `eligible_e(counter,d,g,h,a,b,c,support,srem,K)` an e that passes the original
test is kept only if, with req(e) = max(K, ceil((d+e)/2) - 2g + 2) (UNIBRANCH-NODE-HURWITZ, #1838) and
need = req(e) - support,
    need <= 0, or (srem >= need and e - M >= need),   M = a + b + c,
which is the original test's own capacity semantics (visible support `support`, hidden support capacity `srem`,
hidden mass e - M) with K replaced by req(e).

Checks, fail-closed:
  1. every selected row's UNMODIFIED direct count passes the counter's own retained-HPADJ08-rejected-mass check;
  2. modified <= unmodified on every row;
  3. per-row modified counts equal RESULT.json, and are <= the UNIBRANCH-NODE-HURWITZ per-row counts;
  4. totals equal RESULT.json; zero credit.
Counts are compressed terminals (prefixes) surviving necessary conditions, NOT Picard classes or curves.
usage: python verify_hpadj22_unibranch.py --source-root <checkout of 4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2>
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import inspect
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESULT = HERE / "RESULT.json"
UNH_RESULT = ROOT / "stages/stage32/management/unibranch-node-hurwitz/RESULT.json"
DIRECT_REL = Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB = "e965ab0a6ea51938006882ca2110016f48b3768e"
HPADJ22_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
MAX_D = 48
CHECK_LINE = '    req(reject==retained,f"retained HPADJ08 reject mismatch {reject}!={retained}")\n'


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, required=True)
    a = ap.parse_args()
    src = a.source_root.resolve()
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=src, check=True, text=True, stdout=subprocess.PIPE).stdout.strip()
    req(head == HPADJ22_HEAD, "source root is not the HPADJ22 head")

    res = json.loads(RESULT.read_text(encoding="utf-8"))
    req(res.get("canonical_sha256_without_this_field") == canon(res), "RESULT.json canonical drift")
    req(not any(res["credit"].values()), "credit firewall")
    unh = json.loads(UNH_RESULT.read_text())["census"]["per_row"]

    p = ROOT / DIRECT_REL
    req(blob(p) == DIRECT_BLOB, "direct-count source drift")
    spec = importlib.util.spec_from_file_location("hpadj22_direct_locked_for_unibranch", p)
    direct = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = direct
    spec.loader.exec_module(direct)
    s = inspect.getsource(direct.direct_count)
    req(s.count(CHECK_LINE) == 1, "direct_count source shape drift")
    exec(compile(s.replace(CHECK_LINE, "").replace("def direct_count(", "def direct_count_modified_eligibility("),
                 "direct_count_modified_eligibility", "exec"), direct.__dict__)

    old = direct.load_old(src)
    ctx = old.source_context()
    bc, bnd = ctx[0], ctx[1]
    rows = ctx[8]
    orig = bnd.eligible_e

    def unibranch_eligible_e(counter, d, g, h, aa, b, c, support, srem, K):
        out = []
        M = aa + b + c
        for e in orig(counter, d, g, h, aa, b, c, support, srem, K):
            need = max(K, ceil_div(d + e, 2) - 2 * g + 2) - support
            if need > 0 and (srem < need or e - M < need):
                continue
            out.append(e)
        return out

    per_row: dict[str, dict] = {}
    for band in range(len(old.PLANNED)):
        b0, b1 = old.PLANNED[band]
        sel = [i for i in range(178) if int(rows[i][2]) <= MAX_D and b0 <= int(rows[i][2]) // 2]
        if not sel:
            continue
        joint = bc.build_joint_bc_shard(old.HMAX, b0, b1)
        for idx in sel:
            bnd.eligible_e = orig
            g0 = direct.direct_count(old, ctx, joint, band, idx)
            bnd.eligible_e = unibranch_eligible_e
            g1 = direct.direct_count_modified_eligibility(old, ctx, joint, band, idx)
            bnd.eligible_e = orig
            u, m = int(g0["hpadj22_exact_survivors"]), int(g1["hpadj22_exact_survivors"])
            req(m <= u, f"modified exceeds unmodified at row {idx}")
            r = per_row.setdefault(g0["row"]["row_id"], {"hpadj22": 0, "hpadj22_unibranch": 0})
            r["hpadj22"] += u
            r["hpadj22_unibranch"] += m
        print(f"band {band} done ({len(sel)} rows)", flush=True)

    got = {k: {"hpadj22": str(v["hpadj22"]), "hpadj22_unibranch": str(v["hpadj22_unibranch"])}
           for k, v in sorted(per_row.items())}
    req(got == res["per_row"], "per-row regression against RESULT.json")
    for k, v in per_row.items():
        if v["hpadj22_unibranch"]:
            req(k in unh and v["hpadj22_unibranch"] <= unh[k]["terminals"], f"row {k} not below UNIBRANCH-NODE-HURWITZ")
    total = sum(v["hpadj22_unibranch"] for v in per_row.values())
    nz = sum(1 for v in per_row.values() if v["hpadj22_unibranch"])
    req(str(total) == res["totals"]["hpadj22_unibranch"] and nz == res["totals"]["rows_nonzero"], "totals regression")
    print(f"PASS: unmodified HPADJ22 direct counts replay with the retained HPADJ08 check on {len(per_row)} rows (d<={MAX_D})")
    print(f"PASS: HPADJ22 x UNIBRANCH-NODE-HURWITZ = {total} compressed terminals in {nz} rows (not Picard classes); "
          "per-row data equal RESULT.json and are <= the UNIBRANCH-NODE-HURWITZ rows")
    print("PASS: zero credit; MAIN authority unchanged")


if __name__ == "__main__":
    main()
