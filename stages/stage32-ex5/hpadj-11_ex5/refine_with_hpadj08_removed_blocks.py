#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "CHECKPOINT.json"
PRODUCER = HERE / "count_td01_envelope_block_upper_bound.py"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"

LOCKS = {
    "checkpoint_blob": "e1cc971a7505a28eb62401869c2754793ab57c91",
    "checkpoint_canonical": "1f5095cf4a26a09f9d756f629789255170841ad4911a9d3a579512667955d5db",
    "producer_blob": "4afe018e1108c89d419f85c5aa1219e42e292a96",
    "manifest_blob": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
}

TD01_EXACT_PACKET = {
    "blob_sha1": "51271c11078459ad9171138c4fb6121d7a665c39",
    "canonical_sha256": "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
    "hpadj08_replay_domain_exact_cardinality": 47589703313957134107892,
    "hpadj08_exact_square_rejected": 40886299509963924857401,
    "hpadj08_exact_square_survivor_envelope": 6703403803993209250491,
    "x4_complete_after_hpadj08": True,
    "reason": "HPADJ08 exact-square rejection depends only on the ten stored exceptional coordinates, not x4.",
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_locked_json(path: Path, blob: str, canonical: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical drift")
    req(canon(value) == canonical, f"{label} canonical drift")
    return value


def main() -> None:
    cp = load_locked_json(
        CHECKPOINT,
        LOCKS["checkpoint_blob"],
        LOCKS["checkpoint_canonical"],
        "HPADJ11 pre-block checkpoint",
    )
    req(PRODUCER.is_file() and git_blob(PRODUCER) == LOCKS["producer_blob"], "HPADJ11 producer blob drift")
    manifest = load_locked_json(
        MANIFEST,
        LOCKS["manifest_blob"],
        LOCKS["manifest_canonical"],
        "FULL178 manifest",
    )

    # The source-locked HPADJ11 producer enumerates exactly the TD01 replay
    # domain with lower=max(legacy,K,d-4*g+4,...).  Since g in {0,1}, every
    # enumerated degree e satisfies e>=d.  Therefore each complete x4 block
    # B=19*d-5*e+1 satisfies B<=14*d+1.  The manifest fixes max d=192.
    row_ids = set()
    max_d = 0
    for ids in manifest["m_class_rows"].values():
        for row_id in ids:
            s = str(row_id)
            row_ids.add(s)
            max_d = max(max_d, int(s.split("-d", 1)[1]))
    req(len(row_ids) == 178, "FULL178 row-set drift")
    req(max_d == 192, f"FULL178 max degree drift: {max_d}")
    max_block_size = 14 * max_d + 1
    req(max_block_size == 2689, "derived maximum x4 block size drift")

    pre_terms = int(cp["td01_scope"]["replay_domain_exact_terminals"])
    survivor_terms = int(cp["td01_scope"]["hpadj08_survivor_x4_complete_envelope_terminals"])
    pre_blocks = int(cp["exact_block_census"]["pre_hpadj08_x4_complete_blocks"])
    td01_bound = int(cp["candidate_bound"]["td01_previous_17_over_33_upper_bound"])
    prior_refined = int(cp["candidate_bound"]["block_count_refined_survivor_upper_bound"])

    removed_terms = pre_terms - survivor_terms
    req(pre_terms == TD01_EXACT_PACKET["hpadj08_replay_domain_exact_cardinality"], "TD01 replay-domain drift")
    req(survivor_terms == TD01_EXACT_PACKET["hpadj08_exact_square_survivor_envelope"], "TD01 survivor-envelope drift")
    req(removed_terms == TD01_EXACT_PACKET["hpadj08_exact_square_rejected"], "TD01 HPADJ08 rejected total drift")
    req(TD01_EXACT_PACKET["x4_complete_after_hpadj08"] is True, "TD01 x4-complete contract drift")

    # Every HPADJ08-rejected terminal belongs to a whole rejected x4 block,
    # and every such block has at most max_block_size terminals.  Thus at
    # least ceil(removed_terms/max_block_size) complete blocks were removed.
    rejected_block_lower_bound = (removed_terms + max_block_size - 1) // max_block_size
    survivor_block_upper_bound = pre_blocks - rejected_block_lower_bound
    req(0 <= survivor_block_upper_bound <= pre_blocks, "survivor block upper bound invalid")

    # For one parity character an odd complete block of size B retains at most
    # (B+1)/2 terminals.  Summed over the survivor envelope this is
    # (S + number_of_survivor_blocks)/2, rounded down after using an upper
    # bound on the survivor-block count.
    strengthened_upper = (survivor_terms + survivor_block_upper_bound) // 2
    strengthened_rejection_lower = survivor_terms - strengthened_upper
    improvement_vs_td01 = td01_bound - strengthened_upper
    improvement_vs_preblock = prior_refined - strengthened_upper

    req(strengthened_upper < prior_refined, "retained HPADJ08 removal did not strengthen pre-block bound")
    req(strengthened_upper < td01_bound, "strengthened bound did not improve TD01")
    req(strengthened_upper + strengthened_rejection_lower == survivor_terms, "envelope partition arithmetic drift")

    out = {
        "schema": "STAGE32EX5_HPADJ11_RETAINED_HPADJ08_REMOVED_BLOCK_REFINEMENT_V1",
        "status": "STRICTER_TD01_SAME_CHARACTER_UPPER_BOUND_AUDIT_REQUIRED",
        "route_id": "HPADJ-11_ex5",
        "sources": {
            "preblock_checkpoint_blob_sha1": LOCKS["checkpoint_blob"],
            "preblock_checkpoint_canonical_sha256": LOCKS["checkpoint_canonical"],
            "preblock_producer_blob_sha1": LOCKS["producer_blob"],
            "full178_manifest_blob_sha1": LOCKS["manifest_blob"],
            "full178_manifest_canonical_sha256": LOCKS["manifest_canonical"],
            "td01_exact_packet": TD01_EXACT_PACKET,
            "td01_hostile_audit_review_id": 5214778974,
            "hpadj10_hostile_audit_reconfirmed_review_id": 5214966911,
        },
        "block_geometry": {
            "full178_rows": len(row_ids),
            "max_degree_d": max_d,
            "enumerated_domain_lower_bound_on_e": "e>=d, from source-locked lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed)) with g in {0,1}",
            "normal_block_size": "B=19*d-5*e+1",
            "maximum_possible_block_size": max_block_size,
            "pre_hpadj08_x4_complete_blocks": pre_blocks,
            "hpadj08_removed_terminals": removed_terms,
            "hpadj08_rejected_complete_block_lower_bound": rejected_block_lower_bound,
            "hpadj08_survivor_complete_block_upper_bound": survivor_block_upper_bound,
        },
        "candidate_bound": {
            "hpadj08_survivor_envelope_terminals": survivor_terms,
            "td01_previous_17_over_33_upper_bound": td01_bound,
            "preblock_refined_upper_bound": prior_refined,
            "removed_block_refined_survivor_upper_bound": strengthened_upper,
            "removed_block_refined_rejection_lower_bound_inside_td01_envelope": strengthened_rejection_lower,
            "improvement_vs_td01_upper_bound": improvement_vs_td01,
            "additional_improvement_vs_preblock_refinement": improvement_vs_preblock,
            "strict_improvement": True,
        },
        "semantics": {
            "same_picard64_character_as_td01_and_hpadj10": True,
            "candidate_is_refinement_not_additive_subtraction": True,
            "v30_main_upper_bound_used_as_exact_identity_set": False,
            "old_hpadj01_population_reused_as_current_main_population": False,
            "artifact_download_required_for_replay": False,
            "heavy_run_required": False,
            "main_consumption_performed": False,
            "hostile_audit_required_before_main_consumption": True,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
