#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"
STATE = HERE / "MAIN-STATE.json"
VERIFY_MAIN = HERE / "verify_main_state.py"
V2_HELPER = HERE / "apply_ex2_03d_claim_sync_v2.py"

OLD_EX2_CLAIM_HEAD = "25cf939cdc2696f57c263e1c1b6ecfc5a6e79b03"
CURRENT_MAIN = "226a8aa11ac61293a7e4b7f9611177f68af94ff4"
ANCESTRY_SYNC = "5cba8da8f10d5580b087604d2c394aafdc3eae08"
OLD_MAIN = "f2a89e613cdf91191a0aada9e90c9fc93373a6c6"

SELECTED_OLD_CLAIMS = [
    "S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3",
    "S32.EX2.LANE_CONTRACT.V3",
    "S32.EX2.SECTION_SOURCE_INVENTORY.V1",
    "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1",
    "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1",
]
EX2_REF_ORDER = [
    "S32.EX2.LANE_CONTRACT.V3",
    "S32.EX2.SECTION_SOURCE_INVENTORY.V1",
    "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1",
    "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1",
    "S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3",
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def dump(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def old_json(path: str) -> dict:
    return json.loads(git("show", f"{OLD_EX2_CLAIM_HEAD}:{path}"))


# Recover only the immutable EX2/V3 claim cores that existed on the pre-freshness
# branch.  Current-main claims remain authoritative and are never replaced.
old_registry = old_json("stages/stage32/proof/CLAIM-REGISTRY.json")
old_claims = {c["claim_id"]: c for c in old_registry["claims"]}
r = json.loads(REGISTRY.read_text())
current = {c["claim_id"]: c for c in r["claims"]}
for cid in SELECTED_OLD_CLAIMS:
    assert cid in old_claims, cid
    if cid in current:
        assert current[cid]["claim_core_sha256"] == old_claims[cid]["claim_core_sha256"], cid
    else:
        r["claims"].append(old_claims[cid])
dump(REGISTRY, r)

# Extend only EX2 lane references.  Preserve every current-main lane and ref,
# including hostile-audited EX4 material.
l = json.loads(LANES.read_text())
ex2 = next(x for x in l["lanes"] if x["lane"] == "EX2")
refs = ex2["claim_refs"]
for cid in EX2_REF_ORDER:
    if cid not in refs:
        refs.append(cid)
dump(LANES, l)

# Preserve immutable EX2-01 V1, create the semantic-replay V2, then register
# the already source-locked EX2-03D five-conic reduction.
runpy.run_path(str(V2_HELPER), run_name="__main__")

# The older deterministic helper was authored before the current-main sync.
# Update only freshness/provenance fields and the generated verifier's exact
# expected main SHA; mathematical claim cores and credit remain unchanged.
s = json.loads(STATE.read_text())
s["freshness"].update({
    "last_reconciled_current_main_sha": CURRENT_MAIN,
    "current_main_observed_sha": CURRENT_MAIN,
    "ancestry_sync_commit": ANCESTRY_SYNC,
    "unreconciled_main_commit_count": 0,
    "freshness_sync_deferred_until_retained_promotion_checkpoint": False,
    "stage32ex2_source_drift_in_intervening_main_commit": False,
    "promotion_requires_recheck_current_main": True,
})
s["claim_sync"].update({
    "reconciled_current_main_sha": CURRENT_MAIN,
    "current_main_reconciliation_required": False,
    "shared_claim_files_written_from_stale_branch": False,
    "stage32_main_authority_changed": False,
    "promotion_attempted": False,
    "status": "COMPLETE_CURRENT_MAIN_RECONCILED_LOCAL_DAG_VERIFIERS_PASS_EXACT_HEAD_CI_REQUIRED_BEFORE_AUDIT",
})
dump(STATE, s)

text = VERIFY_MAIN.read_text()
assert OLD_MAIN in text
text = text.replace(OLD_MAIN, CURRENT_MAIN)
VERIFY_MAIN.write_text(text)

# Fail closed before the workflow is allowed to commit the four synchronized files.
checks = [
    ["python", "-B", "stages/stage32/proof/verify_stage32_claim_dag.py", "--integrity"],
    ["python", "-B", "stages/stage32/proof/verify_stage32_active_frontier.py"],
    ["python", "-B", "stages/stage32-ex2/verify_ex2_03d_five_conic_restriction.py"],
    ["python", "-B", "stages/stage32-ex2/verify_main_state.py"],
]
for cmd in checks:
    subprocess.check_call(cmd, cwd=ROOT)

print("PASS current-main-safe EX2 V3 coexistence + EX2-01 V2 replay + EX2-03D claim sync")
