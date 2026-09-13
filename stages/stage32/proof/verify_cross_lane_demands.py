#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
REPO = STAGE.parents[1]
MAIN_STATE = STAGE / "MAIN-STATE.json"
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
EX5_STATE = REPO / "stages/stage32-ex5/CROSS-LANE-STATE.json"
V13_SNAPSHOT = STAGE / "management/MAIN-STATE-V13-N357-PRECONSUMPTION.json"
V13_REGISTRY_SNAPSHOT = STAGE / "management/CROSS-LANE-DEMANDS-V13-N357-PRECONSUMPTION.json"
V13_EX5_SNAPSHOT = STAGE / "management/EX5-CROSS-LANE-STATE-V13-N357-PRECONSUMPTION.json"
V13_VERIFIER = HERE / "verify_cross_lane_demands_v13.py"
N357_RECEIPT = STAGE / "management/post-n357-composition-pass-consumption-20260912.json"
CUT195_RECEIPT = STAGE / "management/post-cut195-current-v14-composition-consumption-20260912.json"
HPADJ_RECEIPT = HERE / "HPADJ-EX5-FULL178-PICARD64-HANDOFF-SATISFIED.json"

V13_STATE_BLOB = "0f281111572572a8068cc38bb77f5f1c869b98ad"
V13_STATE_CANONICAL = "7c39d7935c36066cf2ec4a549eadc45e821fbf818490e6bfd10126f32bdf8a6d"
V13_REGISTRY_SNAPSHOT_BLOB = "006b4fbb66c83955dbda9e0e40bf5acf402ada8b"
V13_REGISTRY_CANONICAL = "ae916d01b2690b2f86f06c754c83d396f947d4d2ed5df0b3adbdc42d10c2e62a"
V13_EX5_SNAPSHOT_BLOB = "95328732bf98a2b2b693b82b78e701e3e3b6d7ee"
V13_EX5_CANONICAL = "7d3e06425e8672cb31a1c39c871b2e11964a662cffa29d0157623b8808710a9a"
V13_VERIFIER_BLOB = "4ce5d9ffe53aa25a00af054e35d5419d35b05355"
V15_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
CURRENT_REGISTRY_BLOB = "776495776423a8682b4baca5a444d4b8a0345628"
CURRENT_REGISTRY_CANONICAL = "79a29c2bdbae0852c7932b9ddc573f9d3b79da0d2a427b482639551c92e581f0"
CURRENT_EX5_STATE_BLOB = "fca87e4e5daca77df9fe641b83a9f718ab8a71c6"
CURRENT_EX5_STATE_CANONICAL = "b3bbf910f23cf57ff0380121fddee0e1ba0b02b6b95d90769c5f48a14079473b"
HPADJ_RECEIPT_BLOB = "724d9b0d625a4035b43e28a61ad5579ab68c6b57"
HPADJ_RECEIPT_CANONICAL = "2cacd0b104ccd12f5aac46963db01e890685c99c29903e2c1a2c91604dd4f0b8"
HPADJ_DEMAND = "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
N357_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
N357_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
CUT195_RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
CUT195_RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"
CUT194_INCREMENT = 26442
N357_INCREMENT = 17797986705435299826016
CUT195_INCREMENT = 26216
POST_CUT191 = 65396964990500233636101
POST_CUT194 = 65396964990500233609659
POST_N357 = 47598978285064933783643
POST_CUT195 = 47598978285064933757427

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def lock_json(path: Path, blob: str, canon: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(REPO)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(REPO)}")
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == canon, f"stored canonical drift {path.relative_to(REPO)}")
    req(canonical(obj) == canon, f"recomputed canonical drift {path.relative_to(REPO)}")
    return obj

def replay_v13_contract() -> None:
    req(git_blob(V13_SNAPSHOT) == V13_STATE_BLOB, "V13 snapshot blob drift")
    old = load(V13_SNAPSHOT)
    req(old["canonical_sha256_without_this_field"] == V13_STATE_CANONICAL, "V13 snapshot stored canonical drift")
    req(canonical(old) == V13_STATE_CANONICAL, "V13 snapshot canonical drift")
    lock_json(V13_REGISTRY_SNAPSHOT, V13_REGISTRY_SNAPSHOT_BLOB, V13_REGISTRY_CANONICAL)
    lock_json(V13_EX5_SNAPSHOT, V13_EX5_SNAPSHOT_BLOB, V13_EX5_CANONICAL)
    req(git_blob(V13_VERIFIER) == V13_VERIFIER_BLOB, "V13 cross-lane verifier blob drift")

    live = {
        MAIN_STATE: MAIN_STATE.read_bytes(),
        REGISTRY: REGISTRY.read_bytes(),
        EX5_STATE: EX5_STATE.read_bytes(),
    }
    try:
        MAIN_STATE.write_bytes(V13_SNAPSHOT.read_bytes())
        REGISTRY.write_bytes(V13_REGISTRY_SNAPSHOT.read_bytes())
        EX5_STATE.write_bytes(V13_EX5_SNAPSHOT.read_bytes())
        proc = subprocess.run([sys.executable, str(V13_VERIFIER)], cwd=REPO)
        req(proc.returncode == 0, "historical V13 cross-lane contract replay failed")
    finally:
        for path, raw in live.items():
            path.write_bytes(raw)
    req(git_blob(MAIN_STATE) == V15_STATE_BLOB, "V15 MAIN state was not restored after historical replay")
    req(git_blob(REGISTRY) == CURRENT_REGISTRY_BLOB, "current cross-lane registry was not restored")
    req(git_blob(EX5_STATE) == CURRENT_EX5_STATE_BLOB, "current EX5 coordination state was not restored")

def verify_current_hpadj_coordination() -> None:
    reg = lock_json(REGISTRY, CURRENT_REGISTRY_BLOB, CURRENT_REGISTRY_CANONICAL)
    req(reg["contract"]["claim_dag_separation"] is True and reg["contract"]["satisfaction_does_not_grant_credit"] is True, "current demand/claim separation drift")
    ids = [d["demand_id"] for d in reg["demands"]]
    req(len(ids) == len(set(ids)), "duplicate current demand id")
    open_ex5 = [d for d in reg["demands"] if d.get("producer_lane") == "EX5" and d.get("status") == "OPEN"]
    req(open_ex5 == [], "current EX5 producer demand still OPEN")
    hp = [d for d in reg["demands"] if d.get("demand_id") == HPADJ_DEMAND]
    req(len(hp) == 1, "HPADJ demand identity drift")
    hp = hp[0]
    req(hp["producer_lane"] == "EX5" and hp["consumer_lane"] == "MAIN" and hp["priority"] == "P0_BLOCKING_DOWNSTREAM" and hp["status"] == "SATISFIED", "HPADJ routing/status drift")
    sat = hp["satisfying_artifact"]
    req(sat["path"] == "stages/stage32/proof/HPADJ-EX5-FULL178-PICARD64-HANDOFF-SATISFIED.json" and sat["blob_sha1"] == HPADJ_RECEIPT_BLOB and sat["canonical_sha256"] == HPADJ_RECEIPT_CANONICAL, "HPADJ satisfying receipt identity drift")
    req(sat["interface_blob_sha1"] == "8a30e3aa30777460f344eb19836dc725dd442329" and sat["interface_canonical_sha256"] == "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6", "HPADJ interface identity drift")
    req(sat["audited_exact_head"] is None and sat["audit_review_id"] is None, "HPADJ operational satisfaction masquerades as hostile audit")
    pop = hp["source_population_semantics"]
    req(pop["affected_rows"] == 178 and pop["charged_terminal_lower_bound"] == 27104321327305699275487 and pop["hpadj01_main_pruning_credit"] is False and pop["population_drift_forbidden"] is True, "HPADJ source population drift")
    receipt = lock_json(HPADJ_RECEIPT, HPADJ_RECEIPT_BLOB, HPADJ_RECEIPT_CANONICAL)
    req(receipt["status"] == "SATISFIED_OPERATIONAL_ARTIFACT_NO_MATH_CREDIT", "HPADJ receipt status drift")
    req(receipt["bc2_38_quarantine"]["p0_preemption_violation_not_retroactively_erased"] is True and receipt["bc2_38_quarantine"]["bc2_38_main_credit"] is False, "BC2-38 quarantine drift")
    req(all(v is False for v in receipt["credit_firewall"].values()), "HPADJ receipt credit firewall opened")
    ex5 = lock_json(EX5_STATE, CURRENT_EX5_STATE_BLOB, CURRENT_EX5_STATE_CANONICAL)
    req(ex5["open_producer_demands"] == [] and ex5["producer_acknowledged"] is True and ex5["producer_sync_required"] is False and ex5["coordination_repair_complete"] is True, "EX5 current coordination state drift")
    req(ex5["next_gate"]["next_command"] == "stage32ex5-audit" and ex5["next_gate"]["bc2_38_hostile_audit_required"] is True and ex5["next_gate"]["bc2_39_blocked_until_bc2_38_hostile_audit_pass"] is True, "EX5 post-HPADJ gate drift")

def main() -> None:
    replay_v13_contract()
    verify_current_hpadj_coordination()

    state = load(MAIN_STATE)
    frontier = state["current_exact_frontier"]
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 lost MAIN credit")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 lost MAIN credit")
    req(frontier["n357_main_pruning_credit"] is True, "N357 not consumed into MAIN")
    req(frontier["cut195_main_pruning_credit"] is True, "CUT195 not consumed into MAIN")
    req(frontier["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized MAIN credit")
    req(frontier["cut191_remaining_terminals"] == POST_CUT191, "post-CUT191 historical count drift")
    req(frontier["cut194_remaining_terminals"] == POST_CUT194, "post-CUT194 historical count drift")
    req(frontier["n357_incremental_rejected_terminals"] == N357_INCREMENT, "N357 increment drift")
    req(frontier["n357_remaining_terminals"] == POST_N357, "post-N357 count drift")
    req(frontier["cut195_incremental_rejected_terminals"] == CUT195_INCREMENT, "CUT195 increment drift")
    req(frontier["cut195_remaining_terminals"] == POST_CUT195, "post-CUT195 count drift")
    req(frontier["authoritative_remaining_terminals"] == POST_CUT195, "live authority is not post-CUT195")
    req(frontier["authoritative_remaining_strata"] == 17128, "live strata drift")
    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_N357 - CUT195_INCREMENT == POST_CUT195, "CUT195 arithmetic drift")
    req(POST_CUT191 - POST_CUT195 == CUT194_INCREMENT + N357_INCREMENT + CUT195_INCREMENT,
        "live MAIN delta double-charge or gap")

    auth = state["authority_sync"]
    req(auth["n357_current_v13_composition_hostile_audit_status"] == "PASS", "N357 current-authority composition lacks audit PASS")
    req(auth["n357_current_v13_composition_hostile_audit_review_id"] == 5184369560, "N357 composition audit review drift")
    req(auth["n357_current_v13_composition_audited_exact_head"] == "0bdc3b952b35ea3201d8619f21a3df7a3015ff85", "N357 composition audited head drift")
    req(auth["n357_main_pruning_credit_consumed"] is True, "N357 consumption flag false")
    req(auth["n357_post_sync_reaudit_status"] == "PASS", "N357 replacement-head re-audit not consumed")
    req(auth["n357_synchronized_head_hostile_audited"] is True, "N357 synchronized head not audited")
    req(auth["cut195_candidate_hostile_audit_status"] == "PASS", "CUT195 candidate lacks audit PASS")
    req(auth["cut195_current_v14_composition_replayed"] is True, "CUT195 current-V14 composition not replayed")
    req(auth["cut195_current_v14_overlap_n357_terminals"] == 0, "CUT195 overlaps N357")
    req(auth["cut195_main_pruning_credit_consumed"] is True, "CUT195 consumption flag false")
    req(auth["cut195_post_sync_reaudit_required"] is True, "CUT195 replacement-head audit gate missing")
    req(auth["cut195_post_sync_reaudit_status"] == "PENDING", "CUT195 replacement-head audit status drift")
    req(frontier["cut195_synchronized_head_hostile_audited"] is False, "CUT195 replacement head self-awarded audit")

    req(git_blob(N357_RECEIPT) == N357_RECEIPT_BLOB, "N357 consumption receipt blob drift")
    n357_receipt = load(N357_RECEIPT)
    req(n357_receipt["canonical_sha256_without_this_field"] == N357_RECEIPT_CANONICAL and canonical(n357_receipt) == N357_RECEIPT_CANONICAL, "N357 consumption receipt canonical drift")
    x = n357_receipt["overlap_and_cross_lane_replay"]
    req(x["cut191_overlap_terminals"] == 0 and x["cut194_overlap_terminals"] == 0, "N357 overlaps previously consumed cuts")
    req(x["double_charge"] is False, "N357 double-charge flag set")
    req(x["g1_d008_e8_current_prefix_survivor_block_count"] == 7596, "CUT192 source prefix block count drift")
    req(x["g1_d008_e8_current_prefix_survivor_block_stream_sha256"] == "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3", "CUT192 source prefix stream drift")
    req(x["cut192_preferred_wave_survivor_offset_range"] == [1, 255], "CUT192 preferred wave identity drift")
    req(x["n357_rejecting_current_prefix_blocks"] == 0, "N357 invalidates e=8 current prefix")
    req(x["n357_rejecting_cut192_preferred_wave_blocks"] == 0 and x["n357_rejecting_cut192_preferred_wave_terminals"] == 0, "N357 invalidates CUT192 preferred wave")
    req(x["cut192_satisfied_handoff_remains_current_main_surviving"] is True, "CUT192 satisfied handoff no longer current-MAIN surviving")

    req(git_blob(CUT195_RECEIPT) == CUT195_RECEIPT_BLOB, "CUT195 consumption receipt blob drift")
    cut195_receipt = load(CUT195_RECEIPT)
    req(cut195_receipt["canonical_sha256_without_this_field"] == CUT195_RECEIPT_CANONICAL and canonical(cut195_receipt) == CUT195_RECEIPT_CANONICAL, "CUT195 consumption receipt canonical drift")
    y = cut195_receipt["current_v14_composition_replay"]
    req(y["cut195_target_equals_current_prefix_offsets_511_765"] is True, "CUT195 current-prefix population identity drift")
    req(y["n357_rejecting_cut195_target_blocks"] == 0 and y["n357_rejecting_cut195_target_terminals"] == 0, "CUT195 overlaps N357 in retained receipt")
    req(y["cut191_disjoint"] is True and y["cut194_disjoint"] is True, "CUT195 overlaps consumed CUT191/CUT194")
    req(y["double_charge"] is False, "CUT195 double-charge flag set")

    req(state["firewalls"]["merge_authorized"] is False, "merge authorized")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(frontier["stage32_closed"] is False, "Stage32 incorrectly closed")

    print(json.dumps({
        "verdict": "PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V15_PLUS_HPADJ",
        "historical_v13_contract_replayed": True,
        "hpadj_p0_satisfied_operationally": True,
        "hpadj_main_credit": False,
        "bc2_38_quarantine_preserved": True,
        "cut191_main_consumed": True,
        "cut194_main_consumed": True,
        "n357_main_consumed": True,
        "cut195_main_consumed": True,
        "authoritative_remaining_terminals": POST_CUT195,
        "full178_complete": False,
        "replacement_head_hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
