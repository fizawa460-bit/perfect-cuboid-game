#!/usr/bin/env python3
"""Stage32 MAIN V50: verify the authority sync that consumes UNIBRANCH-NODE-HURWITZ.

MAIN takes the minimum of certified upper bounds on the same unibranch g<=1 FULL178 population:
V49 128443221087959579960 (17128 strata) -> V50 511353002049 compressed N220 terminals (530 strata, 40 rows).
The count is of compressed terminals surviving necessary conditions, not Picard classes or curves.

--replay-leaf additionally reruns the leaf verifier (known curves + full census replay).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

RECEIPT = HERE / "V50-MAIN-AUTHORITY-SYNC.json"
RECEIPT_BLOB = "59545e5dcc3ee2f03fc6e3d2c6035e3c907275ec"
RECEIPT_CANON = "ba2bfd26b0203a1d79beb0409263372f22a83c4da35953f3f58d3a15c1b5b2d6"
SNAPSHOT = HERE / "MAIN-STATE-V49-PRE-V50.json"
SNAPSHOT_BLOB = "9eef41db0645300398d8187297f489472fcfbf1c"
RESULT = HERE / "RESULT.json"
LEAF_VERIFIER = HERE / "verify_unibranch_node_hurwitz.py"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CURRENT = ROOT / "stages/stage32/CURRENT.json"
# After the V51 sync the live MAIN-STATE is V51; the V50 state is then replayed from its blob-locked snapshot.
V51_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V51_HPADJ22_UNIBRANCH_SYNCED"
V50_STATE_SNAPSHOT = ROOT / "stages/stage32/management/hpadj22-unibranch/MAIN-STATE-V50-PRE-V51.json"
V50_STATE_SNAPSHOT_BLOB = "14dc10f96d8f63cfc566f4e2228dd68ec5bd5a07"

SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V50_UNIBRANCH_NODE_HURWITZ_SYNCED"
V49_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V49_POST_V48_178_FULLSUPPORT_384_AUDIT_SYNCED"
V49_BOUND = 128443221087959579960
V49_STRATA = 17128
N354 = [17128, 38560956534397137634780102]
NEW_STRATA = 530
NEW_BOUND = 511353002049
MAIN_HEAD = "5fd74ee8d9f1129fea7fbb5bf1c647e120817860"
LEAF_MERGE = "6b7fefa4256399ed8b448b9c3349e724b2728920"
RULE = "MIN_OF_CERTIFIED_UPPER_BOUNDS__SAME_UNIBRANCH_G_LE_1_POPULATION__NO_ADDITIVE_STACKING"
SEMANTICS = "COMPRESSED_N220_TERMINALS_SURVIVING_NECESSARY_CONDITIONS__NOT_PICARD_CLASSES_OR_CURVES"
FIREWALLS = ("effectivity_released", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit",
             "stage32_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized")


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--replay-leaf", action="store_true")
    args = ap.parse_args()

    req(blob(RECEIPT) == RECEIPT_BLOB, "V50 receipt blob drift")
    rec = load(RECEIPT)
    req(rec.get("canonical_sha256_without_this_field") == RECEIPT_CANON == canon(rec), "V50 receipt canonical drift")
    src, a = rec["source"], rec["authority"]
    req(src["leaf_merge_commit"] == LEAF_MERGE and src["leaf_merge_pr"] == 1838, "leaf merge binding")
    req(src["external_bundle_hostile_audit_status"] == "PASS", "leaf audit status")
    req(src["repo_exact_head_audit"].startswith("WAIVED_BY_REPOSITORY_OWNER"), "exact-head audit disposition")
    req(blob(RESULT) == src["result_blob_sha1"], "leaf RESULT blob drift")
    req(blob(LEAF_VERIFIER) == src["leaf_verifier_blob_sha1"], "leaf verifier blob drift")
    req(blob(HERE / "CONTRACT.md") == src["contract_blob_sha1"], "leaf contract blob drift")
    res = load(RESULT)
    req(res["canonical_sha256_without_this_field"] == src["result_canonical_sha256"], "leaf RESULT canonical binding")
    req(res["census"]["unibranch_node_hurwitz_remaining"] == [NEW_STRATA, NEW_BOUND], "leaf headline")
    req(len(res["census"]["per_row"]) == 40, "leaf row count")
    req(sum(r["strata"] for r in res["census"]["per_row"].values()) == NEW_STRATA, "leaf per-row strata sum")
    req(sum(r["terminals"] for r in res["census"]["per_row"].values()) == NEW_BOUND, "leaf per-row terminal sum")
    req(not any(res["credit"].values()), "leaf credit firewall")

    req(blob(SNAPSHOT) == SNAPSHOT_BLOB == a["predecessor_main_state_blob_sha1"], "V49 snapshot drift")
    old = load(SNAPSHOT)
    req(old["schema"] == V49_SCHEMA and old.get("canonical_sha256_without_this_field") == canon(old), "V49 snapshot schema/canonical")
    of = old["current_exact_frontier"]
    req(of["authoritative_remaining_terminals"] == V49_BOUND and of["authoritative_remaining_strata"] == V49_STRATA, "V49 snapshot authority")
    req(int(a["predecessor_v49_upper_bound"]) == V49_BOUND and a["predecessor_v49_remaining_strata"] == V49_STRATA, "receipt predecessor")
    req([a["n354_baseline_remaining"][0], int(a["n354_baseline_remaining"][1])] == N354, "receipt N354 baseline")
    req([a["unibranch_node_hurwitz_remaining"][0], int(a["unibranch_node_hurwitz_remaining"][1])] == [NEW_STRATA, NEW_BOUND], "receipt filter count")
    req(int(a["v50_upper_bound"]) == NEW_BOUND == min(V49_BOUND, NEW_BOUND) and a["v50_remaining_strata"] == NEW_STRATA <= V49_STRATA, "MIN composition")
    req(int(a["v50_exact_tightening_vs_v49"]) == V49_BOUND - NEW_BOUND, "tightening")
    req(a["composition_rule"] == RULE and a["count_semantics"] == SEMANTICS, "composition/semantics")
    req(a["additive_subtraction"] is False and a["exact_rejected_identity_set_claimed"] is False, "accounting firewall")
    req(a["upper_bound_is_exact_residual_identity_set"] is False, "identity-set firewall")
    cs = rec["claim_sync"]
    req(cs["transition_class"] == "AUTHORITY_METADATA_ONLY__EXISTING_NUMERICAL_CENSUS_CLAIM_CORE_UNCHANGED", "claim-sync class")
    req(not (cs["claim_registry_mutation_required"] or cs["active_frontier_mutation_required"] or cs["lane_adapter_mutation_required"]), "claim-sync firewall")
    req(not any(rec["credit"].values()), "receipt credit firewall")

    st = load(STATE)
    superseded = st.get("schema") == V51_SCHEMA
    if superseded:
        req(blob(V50_STATE_SNAPSHOT) == V50_STATE_SNAPSHOT_BLOB, "V50 state snapshot drift")
        st = load(V50_STATE_SNAPSHOT)
    req(st.get("canonical_sha256_without_this_field") == canon(st), "MAIN state canonical; expected=" + canon(st))
    req(st["schema"] == SCHEMA, "MAIN schema")
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == NEW_STRATA and f["authoritative_remaining_terminals"] == NEW_BOUND, "MAIN V50 authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["v50_predecessor_upper_bound"] == V49_BOUND and f["v50_predecessor_remaining_strata"] == V49_STRATA, "V50 predecessor")
    req(f["v50_exact_tightening_vs_v49"] == V49_BOUND - NEW_BOUND, "V50 tightening")
    req(f["v50_unibranch_node_hurwitz_main_numeric_bound_consumed"] is True, "V50 consumption")
    req(f["v50_composition_rule"] == RULE and f["v50_count_semantics"] == SEMANTICS, "V50 rule/semantics")
    req(f["v50_additive_subtraction_performed"] is False and f["v50_exact_incremental_rejected_identity_set_claimed"] is False, "V50 accounting firewall")
    req(f["full178_numerical_census_complete"] is True, "FULL178 census flag")
    for k, v in of.items():
        if k.startswith(("v4", "predecessor_")):
            req(f.get(k) == v, "V49 history field drift: " + k)
    req(st["current"]["latest_main_native_research"] == "V50_UNIBRANCH_NODE_HURWITZ_AUTHORITY_SYNC", "latest MAIN research")
    req(st["current"]["next_exact_route"] == "ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS", "next route")
    req(st["authority_sync"]["current_repository_main"] == MAIN_HEAD, "current repository-main identity")
    locks = st["source_locks"]["v50_unibranch_node_hurwitz_authority_sync"]
    req(locks["receipt_blob_sha1"] == RECEIPT_BLOB and locks["receipt_canonical_sha256"] == RECEIPT_CANON, "state receipt lock")
    req(locks["predecessor_main_state_blob_sha1"] == SNAPSHOT_BLOB and locks["leaf_merge_commit"] == LEAF_MERGE, "state predecessor lock")
    req(locks["verifier_path"] == "stages/stage32/management/unibranch-node-hurwitz/verify_v50_main_authority_sync.py", "state verifier pointer")
    for k in FIREWALLS:
        req(st["firewalls"][k] is False, "firewall " + k)
    req(st["firewalls"]["full178_complete"] is False, "firewall full178_complete")

    if not superseded:
        cur = load(CURRENT)["current_frontier"]
        req(cur["certified_upper_bound"] == str(NEW_BOUND) and cur["remaining_strata"] == NEW_STRATA, "CURRENT frontier")
        req(cur["upper_bound_is_exact_residual_identity_set"] is False, "CURRENT semantics")

    if args.replay_leaf:
        subprocess.run([sys.executable, str(LEAF_VERIFIER)], check=True)

    print("PASS: Stage32 MAIN V50 consumes hostile-audited UNIBRANCH-NODE-HURWITZ as the minimum of same-population certified upper bounds")
    print("V49_UPPER_BOUND=" + str(V49_BOUND) + " STRATA=" + str(V49_STRATA))
    print("V50_UPPER_BOUND=" + str(NEW_BOUND) + " STRATA=" + str(NEW_STRATA))
    print("SEMANTICS=" + SEMANTICS)


if __name__ == "__main__":
    main()
