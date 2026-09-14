#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESULT = HERE / "RESULT.json"

RESULT_BLOB = "2f7b016c9030bdb86071f5b0b4803b4bde210584"
RESULT_CANON = "d7e653f7e693776730121769c86fc3fa11af0b6a5755dc392d40837c1eb05986"

LOCKS = {
    "hpadj01": (
        "stages/stage32/management/hpadj-01/RESULT.json",
        "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b",
        "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506",
    ),
    "rr_checkpoint": (
        "stages/stage32/final-chain/32-02-effectivity/RR-EFFECTIVITY-SUFFICIENT-CHECKPOINT.json",
        "f6fd9935865542d7d05a9ce83df0263f0f051bc2",
        "ff9ca45aef3f81835609588c2a189ebd26baedd7f4f69b0cba9339a5101f22bc",
    ),
    "degree_gate": (
        "stages/stage32/final-chain/32-02-effectivity/FULL178-RR-DEGREE-GATE.json",
        "6ee0887d6f37ae9f4971b5d48df9edc8c2b99010",
        "f936aa647922268a0000315701a297d1fc31fa8d25e4ffd099b335f35872e5f3",
    ),
    "gap": (
        "stages/stage32/32-21/post-21bl-effectivity-gap-separation.json",
        "8b46b85a7fe7d1b366d0ada0a7db852f123e77e1",
        "4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc",
    ),
    "genus_defect": (
        "stages/stage32/32-21/post-21bl-genus-defect-preflight.json",
        "ecf4e9d20eddcaef9375f4c6b21ecf9bf6b0cd8c",
        "e59e23b2aefb1a3b622f3f3ed4eb0f83fd7bb335125fa3254c7e4e737caaa96c",
    ),
}
RR_LEMMA = (
    "stages/stage32/final-chain/32-02-effectivity/RR-EFFECTIVITY-SUFFICIENT-LEMMA.md",
    "07b3fbb969457a29b0a92f8fbc0d3e81bc7138e2",
)


def req(ok: bool, msg: str) -> None:
    if not ok:
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


def lock_json(rel: str, blob: str, expected_canon: str) -> dict:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    req(git_blob(path) == blob, f"source blob drift {rel}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        f"stored canonical drift {rel}")
    req(canon(obj) == expected_canon, f"canonical drift {rel}")
    return obj


def main() -> None:
    req(RESULT.is_file(), "missing retained RESULT.json")
    req(git_blob(RESULT) == RESULT_BLOB, "RESULT blob drift")
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    req(result.get("canonical_sha256_without_this_field") == RESULT_CANON,
        "RESULT stored canonical drift")
    req(canon(result) == RESULT_CANON, "RESULT canonical drift")

    hpadj = lock_json(*LOCKS["hpadj01"])
    rr = lock_json(*LOCKS["rr_checkpoint"])
    gate = lock_json(*LOCKS["degree_gate"])
    gap = lock_json(*LOCKS["gap"])
    defect = lock_json(*LOCKS["genus_defect"])

    lemma_path = ROOT / RR_LEMMA[0]
    req(lemma_path.is_file(), "missing RR lemma")
    req(git_blob(lemma_path) == RR_LEMMA[1], "RR lemma blob drift")
    lemma = lemma_path.read_text(encoding="utf-8")

    req(hpadj["status"] == "RETAINED_CURRENT_V22_ENDPOINT_NECESSARY_FILTER_CANDIDATE_NO_MAIN_CREDIT",
        "HPADJ-01 status drift")
    req(hpadj["current_v22_intersection_lower_bound"]["affected_rows"] == 178,
        "HPADJ-01 affected-row count drift")
    req(hpadj["current_v22_intersection_lower_bound"]["candidate_endpoint_rejected_terminals_lower_bound"]
        == 27104321327305699275487, "HPADJ-01 lower-bound drift")
    req(hpadj["necessary_condition"]["exact_hodge_bound"]
        == "C^2 <= d^2/16 - (1/2)*sum_{i=1}^{10} y_i^2",
        "HPADJ Hodge formula drift")
    req(hpadj["necessary_condition"]["exact_terminal_necessary_condition"]
        == "8*sum(y_i^2) <= d^2 + 32",
        "HPADJ terminal inequality drift")
    req(hpadj["necessary_condition"]["irreducible_k3_adjunction"] == "C^2 >= -2",
        "HPADJ irreducible K3 adjunction drift")

    classifier = rr["classifier"]
    req(classifier["sufficient_gate"] == "d > 16 and C2 >= d - 14",
        "RR sufficient gate drift")
    req("integral irreducible representative" in classifier["does_not_conclude"],
        "RR irreducibility firewall missing")
    req("not an irreducibility theorem" in lemma,
        "RR lemma irreducibility disclaimer missing")
    req("An effective divisor is not automatically an integral irreducible representative" in lemma,
        "RR lemma credit ceiling drift")

    rg = gate["rr_degree_gate"]
    req(rg["degree_gt_16_row_count"] == 168, "RR high-degree row count drift")
    req(rg["degree_le_16_row_count"] == 10, "RR low-degree row count drift")
    req(rg["all_178_rows_partitioned_exactly_once"] is True,
        "RR degree partition no longer exact")
    req(rg["degree_gt_16_row_count"] + rg["degree_le_16_row_count"] == 178,
        "RR degree partition count drift")
    for row in rg["degree_le_16_rows"]:
        d = int(row.split("-d", 1)[1])
        req(d <= 16, f"low-degree row escaped d<=16 gate: {row}")

    req(17 - 14 == 3 and 3 > -2, "integer threshold sanity drift")
    sep = result["exact_predicate_separation"]
    req(sep["hpadj01_rejection_implies"] == "C2 < -2",
        "retained HPADJ strict consequence drift")
    req(sep["rr_sufficient_gate"] == classifier["sufficient_gate"],
        "retained RR gate drift")
    req(sep["rr_certified_overlap_with_hpadj01_rejection_population"] == "EMPTY_BY_PREDICATE",
        "RR/HPADJ overlap verdict drift")
    req(sep["rr_classifier_can_promote_hpadj01"] is False,
        "RR promotion firewall opened")

    exact_gap = gap["exact_gap_result"]
    req(exact_gap["actual_effective_curve_certificate_present"] is False,
        "historical effective-curve gap unexpectedly closed")
    req(exact_gap["integral_irreducible_curve_certificate_present"] is False,
        "historical irreducible-curve gap unexpectedly closed")
    req(exact_gap["geometric_genus1_normalization_certificate_present"] is False,
        "historical normalization gap unexpectedly closed")
    req(gap["firewalls"]["effectivity_is_not_low_genus_irreducible_carrier_without_adapter"] is True,
        "historical effectivity/carrier firewall drift")

    interp = defect["interpretation"]
    req(interp["actual_effective_integral_curve_certificate_present"] is False,
        "genus-defect effective integral curve unexpectedly certified")
    req(interp["normalization_genus1_certificate_present"] is False,
        "genus-defect normalization unexpectedly certified")
    req(defect["exact_numerical_data"]["required_total_normalization_genus_defect"] == 522,
        "historical genus-defect burden drift")

    req(result["semantic_gap"]["therefore_existing_rr_material_does_not_supply_irreducible_carrier_adapter"] is True,
        "semantic no-go verdict drift")
    req(result["next_exact_datum"]["rr_effectivity_route_for_hpadj_promotion"]
        == "DOMINATED_NO_OVERLAP", "next-route separation drift")
    req(result["next_exact_datum"]["genus_defect_route"] == "LIVE_GEOMETRIC_ALTERNATIVE",
        "geometric alternative route drift")

    for key, value in result["firewalls"].items():
        req(value is False, f"credit firewall opened: {key}")

    print(json.dumps({
        "verdict": "PASS_HPADJ02_RR_PROMOTION_NOGO",
        "hpadj01_affected_rows": 178,
        "rr_degree_gt_16_rows": 168,
        "rr_degree_le_16_rows": 10,
        "rr_certified_overlap_with_hpadj01_rejection_population": 0,
        "current_rr_can_promote_hpadj01": False,
        "next_route": "GEOMETRIC_IRREDUCIBLE_CARRIER_OR_NORMALIZATION_DEFECT_ADAPTER",
        "main_pruning_credit": False,
        "endpoint_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
