#!/usr/bin/env python3
"""Stage32 MAIN V52: verify the authority sync that consumes FIXED-DIRECTION-CERTIFICATES.

MAIN takes the per-row minimum (with V51) of certified upper bounds on the same unibranch g<=1 FULL178 population:
V51 5369214401 -> V52 726240487 compressed terminals.  Strata are kept at 530 as an upper bound.  Counts are compressed
terminals surviving necessary conditions, not Picard classes or curves.
The full recount is `verify_fixed_direction_certificates.py` (about 15 minutes with gcc/OpenMP, local).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

RECEIPT = HERE / "V52-MAIN-AUTHORITY-SYNC.json"
RECEIPT_BLOB = "38117791d498242374b62b36cd433bdab5259188"
RECEIPT_CANON = "a73de3b3ae6b80db0fcee42dc1a9da5ccc02ff9ddbcb604bb4ab2b9242d314ab"
SNAPSHOT = HERE / "MAIN-STATE-V51-PRE-V52.json"
SNAPSHOT_BLOB = "d13c7e312e1c58ea7c269920aa306d2af5973aa2"
RESULT = HERE / "RESULT.json"
LEAF_VERIFIER = HERE / "verify_fixed_direction_certificates.py"
C_COUNTER = HERE / "count_fixed_direction_certificates.c"
UNH_RESULT = ROOT / "stages/stage32/management/hpadj22-unibranch/RESULT.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CURRENT = ROOT / "stages/stage32/CURRENT.json"

SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V52_FIXED_DIRECTION_CERTIFICATES_SYNCED"
V50_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V51_HPADJ22_UNIBRANCH_SYNCED"
V50_BOUND = 5369214401
V50_STRATA = 530
NEW_BOUND = 726240487
MAIN_HEAD = "8f44a901fca92a6373ed7a4f281f6b3ebcf33542"
AUDITED_HEAD = "6173ea54fbdcbfa6fa33e74cc66166c22839736d"
RULE = "PER_ROW_MIN_WITH_V51__SAME_UNIBRANCH_G_LE_1_POPULATION__NO_ADDITIVE_STACKING"
SEMANTICS = "COMPRESSED_TERMINALS_SURVIVING_NECESSARY_CONDITIONS__NOT_PICARD_CLASSES_OR_CURVES"
FIREWALLS = ("effectivity_released", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit",
             "stage32_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized",
             "full178_complete")


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    req(blob(RECEIPT) == RECEIPT_BLOB, "V51 receipt blob drift")
    rec = load(RECEIPT)
    req(rec.get("canonical_sha256_without_this_field") == RECEIPT_CANON == canon(rec), "V51 receipt canonical drift")
    src, a = rec["source"], rec["authority"]
    req(src["hostile_audit_status"] == "PASS" and src["hostile_audited_exact_head"] == AUDITED_HEAD, "audit binding")
    req(src["pr"] == 1841, "leaf PR binding")
    req(blob(C_COUNTER) == src["c_counter_blob_sha1"], "C counter blob drift")
    req(blob(RESULT) == src["result_blob_sha1"], "leaf RESULT blob drift")
    req(blob(LEAF_VERIFIER) == src["leaf_verifier_blob_sha1"], "leaf verifier blob drift")
    req((ROOT / src["audit_receipt_path"]).is_file(), "audit receipt missing")
    res = load(RESULT)
    req(res["canonical_sha256_without_this_field"] == src["result_canonical_sha256"] == canon(res), "leaf RESULT canonical")
    v51 = load(UNH_RESULT)["per_row"]
    rows = res["per_row_final"]
    per_row_min = sum(min(int(rows.get(k, 0)), int(u["hpadj22_unibranch"])) for k, u in v51.items())
    req(per_row_min == NEW_BOUND == int(res["totals"]["per_row_min_with_v51"]), "per-row MIN with V51")
    req(sum(int(u["hpadj22_unibranch"]) for u in v51.values()) == V50_BOUND, "V51 per-row data")
    req(not any(res["credit"].values()), "leaf credit firewall")

    req(blob(SNAPSHOT) == SNAPSHOT_BLOB == a["predecessor_main_state_blob_sha1"], "V51 snapshot drift")
    old = load(SNAPSHOT)
    req(old["schema"] == V50_SCHEMA and old.get("canonical_sha256_without_this_field") == canon(old), "V51 snapshot schema/canonical")
    of = old["current_exact_frontier"]
    req(of["authoritative_remaining_terminals"] == V50_BOUND and of["authoritative_remaining_strata"] == V50_STRATA, "V51 snapshot authority")
    req(int(a["predecessor_v51_upper_bound"]) == V50_BOUND and a["predecessor_v51_remaining_strata"] == V50_STRATA, "receipt predecessor")
    req(int(a["v52_upper_bound"]) == NEW_BOUND == min(V50_BOUND, NEW_BOUND), "MIN composition")
    req(int(a["v52_exact_tightening_vs_v51"]) == V50_BOUND - NEW_BOUND, "tightening")
    req(a["v52_remaining_strata_upper_bound"] == V50_STRATA, "strata kept")
    req(a["composition_rule"] == RULE and a["count_semantics"] == SEMANTICS, "composition/semantics")
    req(a["additive_subtraction"] is False and a["exact_rejected_identity_set_claimed"] is False, "accounting firewall")
    req(a["upper_bound_is_exact_residual_identity_set"] is False, "identity-set firewall")
    cs = rec["claim_sync"]
    req(not (cs["claim_registry_mutation_required"] or cs["active_frontier_mutation_required"] or cs["lane_adapter_mutation_required"]), "claim-sync firewall")
    req(not any(rec["credit"].values()), "receipt credit firewall")

    st = load(STATE)
    live = st.get("schema") == SCHEMA
    req(live, "MAIN schema is not V52")
    req(st.get("canonical_sha256_without_this_field") == canon(st), "MAIN state canonical; expected=" + canon(st))
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == NEW_BOUND and f["authoritative_remaining_strata"] == V50_STRATA, "MAIN V52 authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["v52_predecessor_upper_bound"] == V50_BOUND and f["v52_exact_tightening_vs_v51"] == V50_BOUND - NEW_BOUND, "V52 predecessor")
    req(f["v52_fixed_direction_certificates_main_numeric_bound_consumed"] is True and f["v52_composition_rule"] == RULE, "V52 consumption")
    req(f["v52_additive_subtraction_performed"] is False and f["v52_exact_incremental_rejected_identity_set_claimed"] is False, "V52 accounting firewall")
    req(f["full178_numerical_census_complete"] is True, "FULL178 census flag")
    for k, v in of.items():
        if k.startswith(("v4", "v50", "v51", "predecessor_")):
            req(f.get(k) == v, "V51 history field drift: " + k)
    req(st["current"]["latest_main_native_research"] == "V52_FIXED_DIRECTION_CERTIFICATES_AUTHORITY_SYNC", "latest MAIN research")
    req(st["current"]["next_exact_route"] == "ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS", "next route")
    req(st["authority_sync"]["current_repository_main"] == MAIN_HEAD, "current repository-main identity")
    locks = st["source_locks"]["v52_fixed_direction_certificates_authority_sync"]
    req(locks["receipt_blob_sha1"] == RECEIPT_BLOB and locks["receipt_canonical_sha256"] == RECEIPT_CANON, "state receipt lock")
    req(locks["predecessor_main_state_blob_sha1"] == SNAPSHOT_BLOB and locks["hostile_audited_exact_head"] == AUDITED_HEAD, "state predecessor lock")
    req(locks["verifier_path"] == "stages/stage32/management/fixed-direction-certificates/verify_v52_main_authority_sync.py", "state verifier pointer")
    for k in FIREWALLS:
        req(st["firewalls"][k] is False, "firewall " + k)

    cur = load(CURRENT)["current_frontier"]
    req(cur["certified_upper_bound"] == str(NEW_BOUND) and cur["remaining_strata"] == V50_STRATA, "CURRENT frontier")
    req(cur["upper_bound_is_exact_residual_identity_set"] is False, "CURRENT semantics")

    print("PASS: Stage32 MAIN V52 consumes hostile-audited FIXED-DIRECTION-CERTIFICATES as the per-row minimum with V51 on the same population")
    print("V51_UPPER_BOUND=" + str(V50_BOUND) + " V52_UPPER_BOUND=" + str(NEW_BOUND) + " STRATA_UPPER_BOUND=" + str(V50_STRATA))
    print("SEMANTICS=" + SEMANTICS)


if __name__ == "__main__":
    main()
