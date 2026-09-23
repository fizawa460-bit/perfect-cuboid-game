#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFLIGHT = HERE / "V47-SUPPORT-QBC-INTERSECTION-PREFLIGHT.json"
MANIFEST = HERE / "local-support-qbc/GENERATION4-COMPLETE.json"
WORKER = HERE / "run_hpadj22_support_qbc_local_row_b.py"
RECEIPT_VERIFIER = HERE / "verify_local_support_qbc_receipt.py"

V47_SYNC = ROOT / "stages/stage32/management/grf04-hpadj22-joint/GRF04-HPADJ22-V47-FULL178-AUTHORITY-SYNC.json"
V47_ROW = ROOT / "stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent_cshard.py"
V47_AGG = ROOT / "stages/stage32/management/grf04-hpadj22-joint/aggregate_grf04_hpadj22_full178_windowed.py"
V47_HELPER = ROOT / "stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"

def req(v, m):
    if not v:
        raise SystemExit("FAIL: " + m)

def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main():
    p = json.loads(PREFLIGHT.read_text())
    v = p["v47_authority"]
    s = p["support_qbc_producer"]
    c = p["intersection_contract"]

    req(blob(V47_SYNC) == v["retained_sync_blob_sha1"], "V47 retained sync blob drift")
    vo = json.loads(V47_SYNC.read_text())
    req(canon(vo) == v["retained_sync_canonical_sha256"] == vo["canonical_sha256_without_this_field"], "V47 retained sync canonical drift")
    req(vo["execution"]["exact_head"] == v["source_exact_head"], "V47 exact-head drift")
    req(vo["authority"]["same_population_joint_upper_bound"] == v["same_population_joint_upper_bound"], "V47 upper-bound drift")
    req(vo["execution"]["aggregate_canonical_sha256"] == v["aggregate_canonical_sha256"], "V47 aggregate canonical drift")
    req(blob(V47_ROW) == v["row_compute_worker_blob_sha1"], "V47 row worker drift")
    req(blob(V47_AGG) == v["aggregate_worker_blob_sha1"], "V47 aggregate worker drift")
    req(blob(V47_HELPER) == v["helper_blob_sha1"], "V47 helper drift")
    req(vo["source_locks"]["hpadj22_source_head"] == v["hpadj22_source_head"], "V47 HPADJ22 source-head drift")

    req(blob(MANIFEST) == s["manifest_blob_sha1"], "support-qBC manifest blob drift")
    mo = json.loads(MANIFEST.read_text())
    req(canon(mo) == s["manifest_canonical_sha256"] == mo["canonical_sha256_without_this_field"], "support-qBC manifest canonical drift")
    req(len(mo["receipts"]) == s["receipt_count"] == 384, "support-qBC receipt count drift")
    coords = [(int(x["verified"]["row_index"]), int(x["verified"]["b"])) for x in mo["receipts"]]
    req(len(set(coords)) == len(coords), "duplicate support-qBC row,b coordinate")
    req(sum(int(x["verified"]["saving"]) for x in mo["receipts"]) == int(s["raw_hpadj22_support_qbc_saving"]), "support-qBC raw saving drift")
    req(blob(WORKER) == s["worker_blob_sha1"], "support-qBC worker drift")
    req(blob(RECEIPT_VERIFIER) == s["receipt_verifier_blob_sha1"], "support-qBC receipt verifier drift")
    req(all(x["verified"]["status"] == "PASS" for x in mo["receipts"]), "non-PASS support-qBC receipt")
    req(s["hpadj22_source_head"] == v["hpadj22_source_head"], "cross-producer HPADJ22 source-head mismatch")

    req(c["composition_rule"] == "SAME_POPULATION_EXACT_INTERSECTION_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION", "composition rule drift")
    req(c["raw_saving_may_be_added_to_v47"] is False, "raw saving must not be added/subtracted against V47")
    req(c["statistical_independence"] is False and c["min_of_counts"] is False, "forbidden composition shortcut")
    req(p["execution"]["exact_intersection_run_complete"] is False, "preflight must not claim execution")
    req(p["execution"]["candidate_global_upper_bound"] is None and p["execution"]["exact_incremental_saving_vs_v47"] is None, "preflight must not invent intersection result")
    req(p["promotion_packet"]["ready"] is False, "promotion packet cannot be ready before exact execution/audit")
    req(all(x is False for x in p["firewalls"].values()), "credit/merge firewall drift")

    print("PASS: V47 hostile-audited authority/source locks frozen")
    print("PASS: Generation4 384-coordinate support-qBC producer frozen and unique")
    print("PASS: common HPADJ22 source head bound across V47 and support-qBC")
    print("PASS: exact intersection/replacement contract prepared; raw producer saving is not double-charged")
    print("PASS: zero MAIN/theorem/endpoint credit; exact intersection execution and hostile audit remain required")

if __name__ == "__main__":
    main()
