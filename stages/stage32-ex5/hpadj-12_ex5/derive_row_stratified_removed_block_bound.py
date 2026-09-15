#!/usr/bin/env python3
import base64
import hashlib
import json
import zlib
from pathlib import Path

CERT_CANONICAL = "9dc6d1976b171dc1b71df1e767200a62cba9683ebc2d722819b92f8cd1e617c3"
CERT_BLOB_SHA1 = "29ef2acf15e6649f5db90935f53b65a9388f7db4"
CERT_ROW_STREAM_SHA256 = "eb5716aad8931012fabc2183e3ef5957b0951606970eb89067a6bdbfb66f3f2f"
HPADJ11_REFINER_BLOB_SHA1 = "bda314b4ebbca59a209e2f4fd4d17dfc826cd17a"
HPADJ11_RESULT_CANONICAL = "c25501d53f424a6ddcaa68d54ec671545563d6b663cf9a192b118389fb974546"
EXPECTED_HPADJ08_REMOVED_TERMINALS = 40886299509963924857401
EXPECTED_PREBLOCKS = 33358843813855035700
EXPECTED_SURVIVOR_TERMINALS = 6703403803993209250491
EXPECTED_HPADJ11_UPPER = 3360778813767800658369
EXPECTED_TD01_UPPER = 3453268626299532038131
EXPECTED_OLD_REMOVED_BLOCK_LB = 15205020271462969453
EXPECTED_NEW_REMOVED_BLOCK_LB = 17071409609395633850
EXPECTED_NEW_SURVIVOR_BLOCK_UPPER = 16287434204459401850
EXPECTED_NEW_SURVIVOR_UPPER = 3359845619098834326170
EXPECTED_IMPROVEMENT_VS_HPADJ11 = 933194668966332199
EXPECTED_IMPROVEMENT_VS_TD01 = 93423007200697711961
EXPECTED_RESULT_CANONICAL = "2b710888bd332e4c402f086ae0e5177acfd96a003a6bb30991b2f67e131b2e74"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT_PATH = HERE / "HPADJ08-ROW-REJECT-CERTIFICATE.json"
HPADJ11_REFINER = ROOT / "stages/stage32-ex5/hpadj-11_ex5/refine_with_hpadj08_removed_blocks.py"

def canonical_sha256(obj):
    payload = {k: v for k, v in obj.items() if k != "canonical_sha256_without_this_field"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def git_blob_sha1(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def row_stream_sha256(rows):
    raw = "\n".join(
        json.dumps(
            {
                "d": int(r["d"]),
                "g": int(r["g"]),
                "stored_exact_square_candidate_rejected_terminals":
                    int(r["stored_exact_square_candidate_rejected_terminals"]),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        for r in rows
    ).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    cert = json.loads(CERT_PATH.read_text())
    assert canonical_sha256(cert) == CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == CERT_CANONICAL
    assert git_blob_sha1(CERT_PATH) == CERT_BLOB_SHA1

    # Fail closed on the exact hostile-audited HPADJ11 refiner before consuming
    # any retained constants from its mathematical boundary.
    assert git_blob_sha1(HPADJ11_REFINER) == HPADJ11_REFINER_BLOB_SHA1

    rows_raw = zlib.decompress(base64.b64decode(cert["rows_zlib_base64"]))
    assert hashlib.sha256(rows_raw).hexdigest() == cert["aggregate"]["rows_json_sha256"]
    rows = json.loads(rows_raw)
    assert len(rows) == 178
    keys = [(int(r["g"]), int(r["d"])) for r in rows]
    assert len(set(keys)) == 178
    assert keys == sorted(keys)
    assert sum(1 for g, _ in keys if g == 0) == 85
    assert sum(1 for g, _ in keys if g == 1) == 93
    assert row_stream_sha256(rows) == CERT_ROW_STREAM_SHA256

    removed_total = sum(int(r["stored_exact_square_candidate_rejected_terminals"]) for r in rows)
    assert removed_total == EXPECTED_HPADJ08_REMOVED_TERMINALS
    assert removed_total == cert["aggregate"]["stored_exact_square_candidate_rejected_terminals"]

    derived_rows = []
    removed_blocks_lb = 0
    for r in rows:
        g = int(r["g"])
        d = int(r["d"])
        rejected = int(r["stored_exact_square_candidate_rejected_terminals"])
        # On the source-locked enumerated domain, e>=d. Therefore
        # B=19d-5e+1 <= 14d+1. Each fully removed x4 block contains at most
        # this many rejected terminals, so ceil(rejected/Bmax) is a valid
        # per-row lower bound on the number of removed complete blocks.
        bmax = 14 * d + 1
        block_lb = (rejected + bmax - 1) // bmax
        removed_blocks_lb += block_lb
        derived_rows.append({
            "g": g,
            "d": d,
            "stored_exact_square_candidate_rejected_terminals": rejected,
            "row_max_block_size": bmax,
            "removed_complete_block_lower_bound": block_lb,
        })

    assert removed_blocks_lb == EXPECTED_NEW_REMOVED_BLOCK_LB
    assert removed_blocks_lb > EXPECTED_OLD_REMOVED_BLOCK_LB

    survivor_blocks = EXPECTED_PREBLOCKS - removed_blocks_lb
    assert survivor_blocks == EXPECTED_NEW_SURVIVOR_BLOCK_UPPER

    # For each surviving odd x4-complete block, one parity character keeps at
    # most ceil(B/2). Summed over the envelope this is
    # floor((surviving terminals + surviving block count)/2).
    new_upper = (EXPECTED_SURVIVOR_TERMINALS + survivor_blocks) // 2
    assert new_upper == EXPECTED_NEW_SURVIVOR_UPPER
    assert EXPECTED_HPADJ11_UPPER - new_upper == EXPECTED_IMPROVEMENT_VS_HPADJ11
    assert EXPECTED_TD01_UPPER - new_upper == EXPECTED_IMPROVEMENT_VS_TD01

    result = {
        "schema": "STAGE32EX5_HPADJ12_ROW_STRATIFIED_REMOVED_BLOCK_REFINEMENT_V1",
        "status": "STRICTER_ROW_STRATIFIED_TD01_SAME_CHARACTER_UPPER_BOUND_AUDIT_REQUIRED",
        "route_id": "HPADJ-12_ex5",
        "block_geometry": {
            "full178_rows": 178,
            "enumerated_domain_lower_bound_on_e":
                "e>=d, inherited from the source-locked HPADJ11/FULL178 terminal-family domain",
            "normal_block_size": "B=19*d-5*e+1",
            "rowwise_maximum_block_size": "B<=14*d+1",
            "hpadj08_removed_terminals": EXPECTED_HPADJ08_REMOVED_TERMINALS,
            "previous_global_maximum_block_size": 2689,
            "previous_global_removed_complete_block_lower_bound": EXPECTED_OLD_REMOVED_BLOCK_LB,
            "row_stratified_removed_complete_block_lower_bound": removed_blocks_lb,
            "removed_block_lower_bound_improvement":
                removed_blocks_lb - EXPECTED_OLD_REMOVED_BLOCK_LB,
            "pre_hpadj08_x4_complete_blocks": EXPECTED_PREBLOCKS,
            "hpadj08_survivor_complete_block_upper_bound": survivor_blocks,
            "derived_row_stream_sha256": "2e3400c68c90020377fd3cb6d26be67988b822b5f7de20b3f1dfd9577854cfc4",
        },
        "candidate_bound": {
            "hpadj08_survivor_envelope_terminals": EXPECTED_SURVIVOR_TERMINALS,
            "hpadj11_previous_removed_block_refined_survivor_upper_bound": EXPECTED_HPADJ11_UPPER,
            "td01_previous_17_over_33_upper_bound": EXPECTED_TD01_UPPER,
            "row_stratified_refined_survivor_upper_bound": new_upper,
            "improvement_vs_hpadj11_upper_bound": EXPECTED_HPADJ11_UPPER - new_upper,
            "improvement_vs_td01_upper_bound": EXPECTED_TD01_UPPER - new_upper,
            "strict_improvement_over_hpadj11": True,
            "strict_improvement_over_td01": True,
        },
        "sources": {
            "hpadj08_row_reject_certificate_blob_sha1": CERT_BLOB_SHA1,
            "hpadj08_row_reject_certificate_canonical_sha256": CERT_CANONICAL,
            "hpadj08_audited_exact_head": "36eab50192cf80ec5ed48aba40f4a56076759fea",
            "hpadj08_hostile_audit_review_id": 5205760920,
            "hpadj08_workflow_run_id": 34935380596,
            "hpadj11_refiner_blob_sha1": HPADJ11_REFINER_BLOB_SHA1,
            "hpadj11_removed_block_result_canonical_sha256": HPADJ11_RESULT_CANONICAL,
            "hpadj11_audited_exact_head": "1c694f6650125a8fb0121925beff7f800b5d6283",
            "hpadj11_hostile_audit_review_id": 5216133884,
            "td01_exact_bound_packet_blob_sha1": "51271c11078459ad9171138c4fb6121d7a665c39",
            "td01_exact_bound_packet_canonical_sha256":
                "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
            "td01_hostile_audit_review_id": 5214778974,
        },
        "semantics": {
            "candidate_is_refinement_not_additive_subtraction": True,
            "same_picard64_character_as_td01_hpadj10_hpadj11": True,
            "uses_hpadj08_exact_archived_shard_rows": True,
            "heavy_run_required": False,
            "new_heavy_run_used": False,
            "main_consumption_performed": False,
            "v31_main_upper_bound_used_as_exact_identity_set": False,
            "hostile_audit_required_before_main_handoff_or_consumption": True,
            "next_exact_unit":
                "Hostile-audit this HPADJ12 row-stratified replacement bound; only after PASS may EX5 build a new MAIN replacement handoff.",
        },
        "firewalls": {
            "current_main_incremental_credit": False,
            "effectivity_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
            "perfect_cuboid_credit": False,
            "receiver_credit": False,
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
        },
    }
    result["canonical_sha256_without_this_field"] = canonical_sha256(result)
    assert result["canonical_sha256_without_this_field"] == EXPECTED_RESULT_CANONICAL
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False))

if __name__ == "__main__":
    main()
