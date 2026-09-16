#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HANDOFF = HERE / "MAIN-HANDOFF.json"

HANDOFF_BLOB = "52ca73eeb52b7d930f905c42a85b62f044bda269"
HANDOFF_CANON = "826966a95f22c2235258c6499c9bc9c03b2521687d71dbf99d9728eaaaa6d3f5"
AUDITED_HEAD = "4140e5eb2ebee0c32b22ec78fd531ab35fb7c3ff"
AUDIT_REVIEW = 5228477451
HEAVY_RUN = 35077283028
UNION_CANON = "801999649a71700c369f0c2a32da9f7603b86e077212d3a4865ffbf1773822e7"
MANIFEST_CANON = "b619d5c31115f5783b58b91978e33f5aa410470601e228aa72d1c6f337275e1e"
RECOVERY_CANON = "e30c782edd67ac9057dc290f6d539d6bac3ddbd4370b741a934148e0c3915dec"
MAIN_PREFLIGHT_CANON = "0191c14b3fc072a762d1b702408746691cd5fe315ce9f4a0a040b75183bd13a8"
MAIN_PREFLIGHT_BLOB = "0eb5672dea0712cbf5044d5376e60fe233e767c3"
HPADJ20 = 179119009547804181594
HPADJ19 = 179245728231734014087
OBSERVED_MAIN = 195414091250828468192


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def git_blob(path: Path) -> str:
    return git_blob_bytes(path.read_bytes())


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_local_locked_json(path: Path, blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    raw = path.read_bytes()
    req(git_blob_bytes(raw) == blob, f"{label} blob drift")
    obj = json.loads(raw.decode())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--artifact-dir",
        type=Path,
        help="Directory containing hpadj20-parallel-union.json and hpadj20-heavy-execution-manifest.json",
    )
    ap.add_argument(
        "--main-root",
        type=Path,
        help="Optional checkout of the observed Stage32 MAIN PR head for preflight binding",
    )
    args = ap.parse_args()

    handoff = load_local_locked_json(
        HANDOFF, HANDOFF_BLOB, HANDOFF_CANON, "HPADJ20 MAIN handoff"
    )
    req(handoff["schema"] == "STAGE32EX5_HPADJ20_FULL178_MAIN_HANDOFF_V1",
        "handoff schema")
    req(handoff["status"] ==
        "HOSTILE_AUDITED_HEAVY_RESULT_READY_FOR_MAIN_NUMERICAL_PREFLIGHT__ZERO_MAIN_CREDIT",
        "handoff status")
    p = handoff["producer"]
    req(p["audited_exact_head"] == AUDITED_HEAD, "audited head")
    req(p["hostile_audit_review_id"] == AUDIT_REVIEW and
        p["hostile_audit_verdict"] == "PASS", "hostile-audit receipt")
    hr = p["heavy_run"]
    req(hr["run_id"] == HEAVY_RUN and hr["conclusion"] == "success", "heavy run")
    req(hr["union_canonical_sha256"] == UNION_CANON, "union canonical receipt")
    req(hr["execution_manifest_canonical_sha256"] == MANIFEST_CANON,
        "manifest canonical receipt")
    req(hr["recovery_snapshot_canonical_sha256"] == RECOVERY_CANON,
        "recovery canonical receipt")
    req(hr["full178_rows"] == 178 and hr["row_gap_count"] == 0 and
        hr["row_overlap_count"] == 0, "FULL178 partition receipt")
    req(hr["carried_units"] == 3 and hr["computed_units"] == 175,
        "resume accounting receipt")

    # Fail closed on every local producer source lock before using the transition.
    for label, lock in p["source_locks"].items():
        path = ROOT / lock["path"]
        req(path.is_file(), f"missing producer source {label}")
        req(git_blob(path) == lock["blob_sha1"], f"producer source blob drift: {label}")

    c = handoff["candidate_transition"]
    req(c["hpadj20_candidate_upper_bound"] == HPADJ20, "HPADJ20 bound")
    req(c["replayed_hpadj19_candidate_upper_bound"] == HPADJ19, "HPADJ19 replay bound")
    req(c["strict_improvement_vs_hpadj19"] == HPADJ19 - HPADJ20,
        "HPADJ19 improvement arithmetic")
    req(c["observed_current_main_upper_bound"] == OBSERVED_MAIN, "observed MAIN bound")
    req(c["strict_improvement_vs_observed_current_main"] == OBSERVED_MAIN - HPADJ20,
        "observed MAIN improvement arithmetic")
    req(c["remaining_strata_if_consumed_as_valid_replacement"] == 17128,
        "strata preservation")
    req(c["composition_rule"] ==
        "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        "composition rule")
    req(c["same_hpadj08_td01_x4_complete_population"] is True and
        c["ordered_triple_population_preserved_exactly"] is True,
        "population preservation")
    req(c["exact_incremental_rejected_identity_set_available"] is False and
        c["additive_subtraction_authorized"] is False and
        c["ex5_main_authority_mutation_performed"] is False,
        "no-additive/no-authority firewalls")

    fw = handoff["firewalls"]
    req(all(v is False for v in fw.values()), "handoff credit firewall raised")

    if args.artifact_dir is not None:
        d = args.artifact_dir.resolve()
        union_path = d / "hpadj20-parallel-union.json"
        manifest_path = d / "hpadj20-heavy-execution-manifest.json"
        req(union_path.is_file() and manifest_path.is_file(), "missing heavy artifact files")
        union = json.loads(union_path.read_text())
        manifest = json.loads(manifest_path.read_text())
        req(union.get("canonical_sha256_without_this_field") == UNION_CANON and
            canon(union) == UNION_CANON, "heavy union canonical")
        req(manifest.get("canonical_sha256_without_this_field") == MANIFEST_CANON and
            canon(manifest) == MANIFEST_CANON, "heavy manifest canonical")
        req(manifest["exact_head"] == AUDITED_HEAD, "manifest exact head")
        req(manifest["union_canonical"] == UNION_CANON, "manifest->union binding")
        req(manifest["recovery_snapshot_canonical"] == RECOVERY_CANON,
            "manifest recovery binding")
        req(manifest["carried_units"] == 3 and manifest["computed_units"] == 175,
            "manifest resume accounting")
        req(manifest["concurrency"]["stage_heavy_cap"] == 18 and
            manifest["concurrency"]["planned_effective_heavy_concurrency"] == 15 and
            manifest["concurrency"]["reserved_stage_headroom"] == 3,
            "manifest concurrency contract")
        req(all(v is False for v in manifest["credit"].values()),
            "manifest credit firewall raised")
        req(union["partition"]["exact_disjoint_union_verified"] is True and
            union["partition"]["full178_rows"] == 178 and
            union["partition"]["row_gap_count"] == 0 and
            union["partition"]["row_overlap_count"] == 0, "union partition")
        req(union["candidate_bound"]["hpadj20_candidate_upper_bound"] == HPADJ20,
            "artifact HPADJ20 bound")
        req(union["candidate_bound"]["replayed_hpadj19_candidate_upper_bound"] == HPADJ19,
            "artifact HPADJ19 replay bound")
        req(union["candidate_bound"]["strict_improvement_vs_hpadj19_replay"] is True,
            "artifact strict HPADJ19 improvement")
        req(union["candidate_bound"]["structurally_no_weaker_than_hpadj19"] is True,
            "artifact structural dominance")
        req(union["exact_population_adapter"]["A_ordered_triple_population_preserved_exactly"]
            is True, "artifact ordered-triple population")
        req(union["semantics"]["same_hpadj08_td01_x4_complete_population"] is True and
            union["semantics"]["additive_subtraction_used"] is False and
            union["semantics"]["statistical_independence_assumed"] is False and
            union["semantics"]["main_consumption_performed"] is False,
            "artifact semantic firewalls")
        req(all(v is False for v in union["firewalls"].values()),
            "artifact credit firewall raised")

    if args.main_root is not None:
        main_root = args.main_root.resolve()
        rel = handoff["target_main"]["parallel_preflight"]["path"]
        preflight = load_local_locked_json(
            main_root / rel, MAIN_PREFLIGHT_BLOB, MAIN_PREFLIGHT_CANON,
            "MAIN HPADJ20 full-qA preflight"
        )
        req(preflight["schema"] ==
            "STAGE32_MAIN_PARALLEL_HPADJ20_FULL_QA_HISTOGRAM_PREFLIGHT_V1",
            "MAIN preflight schema")
        req(preflight["next_exact_gate"]["requires_hpadj20_exact_numeric_output"] is True and
            preflight["next_exact_gate"]["requires_full_histogram_numeric_replay"] is True,
            "MAIN preflight next gate")
        req(preflight["structural_dominance"]["population_preserved_exactly"] is True and
            preflight["structural_dominance"]["same_pre_domain_terminal_mass"] is True and
            preflight["structural_dominance"]["same_post_mass_constraint"] is True,
            "MAIN preflight population semantics")
        req(preflight["structural_dominance"]["full_histogram_cell_objective_no_larger_than_hpadj20"]
            is True, "MAIN full-histogram dominance")
        req(all(v is False for v in preflight["firewalls"].values()),
            "MAIN preflight credit firewall raised")

    print(json.dumps({
        "verdict": "PASS_HPADJ20_FULL178_MAIN_HANDOFF",
        "audited_producer_head": AUDITED_HEAD,
        "hostile_audit_review_id": AUDIT_REVIEW,
        "heavy_run_id": HEAVY_RUN,
        "hpadj20_upper_bound": HPADJ20,
        "observed_current_main_upper_bound": OBSERVED_MAIN,
        "strict_improvement_vs_observed_current_main": OBSERVED_MAIN - HPADJ20,
        "main_credit_granted_by_ex5": False,
        "main_consumption_performed": False,
        "artifact_replayed": args.artifact_dir is not None,
        "main_preflight_bound": args.main_root is not None,
        "handoff_canonical": HANDOFF_CANON,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
