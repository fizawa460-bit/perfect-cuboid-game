#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DATA = HERE / "V48-EXACT-TSET-HIGHVALUE-PANEL-RETAINED.json"


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def main() -> None:
    o = json.loads(DATA.read_text())
    req(canon(o) == o["canonical_sha256_without_this_field"], "retained canonical drift")
    req(o["status"].startswith("EXACT_BOUNDED_3CELL_STRICT_V48_REFINEMENT_RETAINED"), "status drift")

    ex = o["execution"]
    probe_rel = ex["probe"]
    historical_blob = git("rev-parse", ex["execution_head"] + ":" + probe_rel)
    req(historical_blob == ex["probe_blob_sha1"], "historical execution probe blob drift")
    req(ex["conclusion"] == "SUCCESS", "execution conclusion drift")

    cells = o["cells"]
    req([int(x["c"]) for x in cells] == [83, 85, 89], "cell domain drift")
    req(all(int(x["incremental_tightening_vs_v48"]) > 0 for x in cells), "non-strict retained cell")

    v47 = sum(int(x["v47_joint_survivors"]) for x in cells)
    v48 = sum(int(x["v48_hull_survivors"]) for x in cells)
    exact = sum(int(x["exact_tset_survivors"]) for x in cells)
    inc = sum(int(x["incremental_tightening_vs_v48"]) for x in cells)
    a = o["aggregate"]

    req(v47 == int(a["covered_v47_joint_survivors"]), "V47 aggregate drift")
    req(v48 == int(a["covered_v48_hull_survivors"]), "V48 aggregate drift")
    req(exact == int(a["covered_exact_tset_survivors"]), "exact-tset aggregate drift")
    req(inc == int(a["v48_incremental_tightening"]) == v48 - exact, "incremental arithmetic drift")
    req(int(a["v47_to_exact_tset_tightening"]) == v47 - exact, "V47-to-exact arithmetic drift")
    req(int(a["v47_to_v48_hull_tightening"]) == v47 - v48, "V47-to-V48 arithmetic drift")

    req(o["authority_context"]["main_consumption_performed"] is False, "unexpected MAIN consumption")
    req(o["semantics"]["production_scaleout_authorized"] is False, "unexpected scaleout authorization")
    req(all(v is False for v in o["firewalls"].values()), "credit/merge firewall drift")

    print("PASS: retained exact-tset three-cell panel canonical and arithmetic")
    print("PASS: historical execution probe blob bound to exact run head")
    print("PASS: all three retained cells strictly tighten V48")
    print("PASS: zero MAIN/theorem/effectivity/endpoint/merge credit")


if __name__ == "__main__":
    main()
