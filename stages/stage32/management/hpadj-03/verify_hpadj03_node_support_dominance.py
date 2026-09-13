#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

AUDITED_N358_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
AUDITED_N358_REVIEW = 5184322011
AUDITED_N357_REVIEW = 5183069892

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

RESULT = HERE / "RESULT.json"
RESULT_BLOB = "6f5985f2c2e0995628653a6bc73b9bf6c7256a7c"
RESULT_CANON = "0840d9ec07f6380e4fdad97ab2d6e32c69d25e7539837fa65bd0c34ca3cb8b49"

HPADJ01_RESULT = ROOT / "stages/stage32/management/hpadj-01/RESULT.json"
HPADJ01_RESULT_BLOB = "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b"
HPADJ01_RESULT_CANON = "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506"

HPADJ01_VERIFIER = ROOT / "stages/stage32/management/hpadj-01/verify_hpadj01_current_v22_lower_bound.py"
HPADJ01_VERIFIER_BLOB = "b0253975ddf28c99b9d9898f54ada9a6842b2386"

HPADJ02_RESULT = ROOT / "stages/stage32/management/hpadj-02/RESULT.json"
HPADJ02_RESULT_BLOB = "2f7b016c9030bdb86071f5b0b4803b4bde210584"
HPADJ02_RESULT_CANON = "d7e653f7e693776730121769c86fc3fa11af0b6a5755dc392d40837c1eb05986"

NODE_RESULT = ROOT / "stages/stage32/32-21/post-21bl-node-support-refinement.json"
NODE_RESULT_BLOB = "e0d66b5317034bed5ce0384ca4e126a921d5d87e"
NODE_RESULT_CANON = "d1b446dd8fa32db16a3ec4f2eb8a4db06b2cc65b80a0ef7580cec1437b4ff5ad"

NODE_AUDIT = ROOT / "stages/stage32/32-21/post-21bl-node-support-refinement-audit.json"
NODE_AUDIT_BLOB = "f95cb5a5585b39374887e75ca803d4e8f2bdba2d"
NODE_AUDIT_CANON = "29312a61c79fc2d0d7525142be54677119c5006d900126c769c8bcb7fb711f7c"

N357_RESULT_REL = Path("stages/stage32/32-01-178/nodes/N357/RESULT.json")
N357_RESULT_BLOB = "50014d453266ad79101910a943d14388bd3ef6ec"
N357_RESULT_CANON = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
N357_RECEIPT_REL = Path("stages/stage32/32-01-178/nodes/N357/HOSTILE-AUDIT-PASS.json")
N357_RECEIPT_BLOB = "e9f93fb1b2bfeb68b72598632522d164fee715c6"

N358_RESULT_REL = Path("stages/stage32/32-01-178/nodes/N358/RESULT.json")
N358_RESULT_BLOB = "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"
N358_RESULT_CANON = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
N358_VERIFIER_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")
N358_VERIFIER_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
N358_RECEIPT_REL = Path("stages/stage32/32-01-178/nodes/N358/HOSTILE-AUDIT-PASS.json")

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def lock_json(path: Path, blob: str, canonical: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == canonical,
        f"stored canonical drift {path}")
    req(canon(obj) == canonical, f"canonical drift {path}")
    return obj

def head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()

def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n358-root", type=Path, required=True)
    args = ap.parse_args()
    audited = args.audited_n358_root.resolve()

    req(head(audited) == AUDITED_N358_HEAD, "audited N358 exact head drift")

    result = lock_json(RESULT, RESULT_BLOB, RESULT_CANON)
    hp1 = lock_json(HPADJ01_RESULT, HPADJ01_RESULT_BLOB, HPADJ01_RESULT_CANON)
    hp2 = lock_json(HPADJ02_RESULT, HPADJ02_RESULT_BLOB, HPADJ02_RESULT_CANON)
    node = lock_json(NODE_RESULT, NODE_RESULT_BLOB, NODE_RESULT_CANON)
    node_audit = lock_json(NODE_AUDIT, NODE_AUDIT_BLOB, NODE_AUDIT_CANON)

    req(HPADJ01_VERIFIER.is_file(), "missing HPADJ-01 verifier")
    req(git_blob(HPADJ01_VERIFIER) == HPADJ01_VERIFIER_BLOB,
        "HPADJ-01 verifier blob drift")

    n357 = lock_json(
        audited / N357_RESULT_REL, N357_RESULT_BLOB, N357_RESULT_CANON
    )
    n358 = lock_json(
        audited / N358_RESULT_REL, N358_RESULT_BLOB, N358_RESULT_CANON
    )
    req((audited / N358_VERIFIER_REL).is_file(), "missing N358 verifier")
    req(git_blob(audited / N358_VERIFIER_REL) == N358_VERIFIER_BLOB,
        "N358 verifier blob drift")

    req((audited / N357_RECEIPT_REL).is_file(), "missing N357 audit receipt")
    req(git_blob(audited / N357_RECEIPT_REL) == N357_RECEIPT_BLOB,
        "N357 audit receipt blob drift")
    receipt357 = json.loads((audited / N357_RECEIPT_REL).read_text(encoding="utf-8"))
    req(receipt357.get("status") == "PASS", "N357 audit status drift")
    req(receipt357.get("review_id") == AUDITED_N357_REVIEW, "N357 review drift")

    req((audited / N358_RECEIPT_REL).is_file(), "missing materialized N358 audit receipt")
    receipt358 = json.loads((audited / N358_RECEIPT_REL).read_text(encoding="utf-8"))
    req(receipt358.get("status") == "PASS", "N358 audit status drift")
    req(receipt358.get("review_id") == AUDITED_N358_REVIEW, "N358 review drift")
    req(receipt358.get("audited_exact_head") == AUDITED_N358_HEAD,
        "N358 audited head drift")

    req(node["status"] == "PROVISIONAL_PASS_PENDING_FRESH_AUDIT",
        "historical node-support result status drift")
    req(node["refinement"]["derivation"] ==
        "16(2g-2)k >= 2kd-8kn, hence d <= 16g-16+4n",
        "historical refined degree bound drift")
    req(node_audit["status"] == "PASS_STAGE32_POST21BL_FRESH_NODE_SUPPORT_REFINEMENT_AUDIT",
        "historical node-support fresh audit drift")
    req(node_audit["independent_replay"]["refined_bound"] == "d <= 16g-16+4n",
        "fresh audit refined bound drift")

    rows = 0
    for g, dmax in ((0, 176), (1, 192)):
        for d in range(8, dmax + 1, 2):
            rows += 1
            K = ceil_div(d - 16 * g + 16, 4)
            for n in range(49):
                theorem_ok = d <= 16 * g - 16 + 4 * n
                threshold_ok = n >= K
                req(theorem_ok == threshold_ok,
                    f"Freitag/K equivalence drift g={g} d={d} n={n}")
    req(rows == 178, "FULL178 row-domain drift")

    req(n357["necessary_condition"] == "s + min(e-M,Srem) >= K",
        "N357 support condition drift")
    req(n357["aggregate"]["source_terminals_replayed"] == 65396964990500233636214,
        "N357 source authority drift")
    req(n358["necessary_cut"]["condition"] == "s + min(e-M,Srem-1) >= K",
        "N358 support condition drift")
    req(n358["audited_input"]["review_id"] == AUDITED_N357_REVIEW,
        "N358 predecessor audit drift")
    req(n358["aggregate"]["source_terminals"] ==
        n357["aggregate"]["candidate_remaining_terminals"],
        "N357/N358 chain identity drift")

    firewall = hp1["composition_firewall"]
    req(firewall["n357_semantics_replayed"] is True,
        "HPADJ-01 no longer replays N357 semantics")
    req(firewall["n358_incremental_slice_excluded"] is True,
        "HPADJ-01 no longer excludes N358 incremental slice")
    hp1_method = hp1["current_v22_intersection_lower_bound"]["method"]
    req("count only N357 survivors" in hp1_method,
        "HPADJ-01 method lost N357 survivor restriction")
    req("exclude exact N358 incremental slice" in hp1_method,
        "HPADJ-01 method lost N358 exclusion")
    req(hp1["current_v22_intersection_lower_bound"]["affected_rows"] == 178,
        "HPADJ-01 row coverage drift")

    req(hp2["next_exact_datum"]["genus_defect_route"] == "LIVE_GEOMETRIC_ALTERNATIVE",
        "HPADJ-02 next geometry route drift")

    sem = result["exact_semantic_identity"]
    req(sem["same_threshold_exactly"] is True, "retained threshold identity drift")
    dom = result["dominance_replay"]
    req(dom["hpadj01_replays_audited_n358_combinatorics"] is True,
        "retained N358 replay claim drift")
    req(dom["hpadj01_counts_only_n357_support_survivors"] is True,
        "retained N357 survivor claim drift")
    req(dom["hpadj01_excludes_exact_n358_incremental_slice"] is True,
        "retained N358 exclusion claim drift")
    req(dom["reapplying_freitag_node_support_to_hpadj01_is_new_mathematics"] is False,
        "node-support route incorrectly marked new")
    req(dom["freitag_node_support_can_supply_new_hpadj01_promotion_credit"] is False,
        "node-support route incorrectly grants promotion credit")

    own = result["ownership_and_next_datum"]
    req(own["multibranch_local_delta_genus_ledger_owner"] == "stage32mb-mainbatch",
        "multibranch ownership drift")
    req(own["main_must_not_identify_exceptional_contact_mass_with_delta"] is True,
        "delta firewall missing")
    req(own["population_wide_interface_present"] is False,
        "population-wide adapter unexpectedly present")

    for key in (
        "main_authority_mutated", "main_pruning_credit", "full178_complete",
        "effectivity_final_credit", "receiver_credit", "theorem_credit",
        "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ):
        req(result["firewalls"][key] is False, f"firewall opened {key}")

    print(json.dumps({
        "verdict": "PASS_HPADJ03_NODE_SUPPORT_DOMINANCE_NO_NEW_PROMOTION",
        "full178_rows_checked": rows,
        "n357_support_threshold_is_freitag_K": True,
        "n358_incremental_support_slice_already_excluded": True,
        "hpadj01_candidate_terms": hp1["current_v22_intersection_lower_bound"][
            "candidate_endpoint_rejected_terminals_lower_bound"
        ],
        "new_main_credit": False,
        "next_required_adapter": own["required_unibranch_adapter"],
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
