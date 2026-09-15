#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HPADJ10 = ROOT / "stages/stage32-ex5/hpadj-10_ex5/KERNEL-RESULT.json"
GRF04_REL = Path("stages/stage32/management/grf04-uniform-bound/GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json")

LOCKS = {
    "hpadj10_blob": "0a073dc9e01e037fa02fdbca5a482ee1ce6ab002",
    "hpadj10_canonical": "c678a84a8bb8aa44db0063ca797dec0e174ff021893ae5e9631ac607f43f1598",
    "grf04_blob": "f2a50838e9a443d70a13957c2f65626c7af5d4cc",
    "grf04_canonical": "aa60c5710f86891628420389b0aa5a7f12675264287bd18742e7e9255b2841e6",
}
EXPECTED_ENVELOPE = 6703403803993209250491
EXPECTED_MAIN_AUDITED = 3360778813767800658369
EXPECTED_HPADJ12 = 3359845619098834326170
EXPECTED_GRF04 = 2640734831876112735041
EXPECTED_JOINT = 1421934140240983780407
EXPECTED_CANONICAL = "58039b1e73a288389a6b2899d22e2902e2dc291b6f4f7482b6685c69d1ab7b3a"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked(path: Path, blob: str, canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")
    data = json.loads(path.read_text())
    req(data.get("canonical_sha256_without_this_field") == canon, f"{label} stored canonical drift")
    req(canonical(data) == canon, f"{label} canonical drift")
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grf-root", required=True, help="checkout root containing exact GRF04 V35 candidate head")
    args = ap.parse_args()

    hp = load_locked(HPADJ10, LOCKS["hpadj10_blob"], LOCKS["hpadj10_canonical"], "HPADJ10 kernel")
    grf_path = Path(args.grf_root) / GRF04_REL
    grf = load_locked(grf_path, LOCKS["grf04_blob"], LOCKS["grf04_canonical"], "GRF04 V35 candidate")

    req(hp["kernel"]["accepted_terminal_condition"] == "x4 ≡ x0 + x8 + x10 (mod 2)", "HPADJ10 parity drift")
    req(hp["kernel"]["normal_coordinate_index"] == 4, "HPADJ10 normal-coordinate drift")
    req(hp["kernel"]["reduced_modulus"] == 2, "HPADJ10 modulus drift")

    req(grf["exact_input_envelope"]["full178_rows"] == 178, "GRF04 row coverage drift")
    req(grf["exact_input_envelope"]["x4_complete_after_hpadj08"] is True, "GRF04 x4-complete contract drift")
    req(grf["exact_input_envelope"]["e_even"] is True, "GRF04 e-even contract drift")
    req(grf["exact_input_envelope"]["e_upper_bound"] == "e<=3*d", "GRF04 e upper-bound drift")
    req(grf["exact_input_envelope"]["hpadj08_survivor_x4_complete_envelope_terminals"] == EXPECTED_ENVELOPE, "GRF04 envelope drift")
    req(grf["candidate_bound"]["candidate_upper_bound"] == EXPECTED_GRF04, "GRF04 candidate upper-bound drift")
    req(grf["candidate_bound"]["predecessor_v34_authoritative_upper_bound"] == EXPECTED_MAIN_AUDITED, "V34 authority drift")
    req(grf["grf04_exact_necessary_condition"]["formula"] == "24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2 + 48*d + 96 - 96*g", "GRF04 formula drift")
    req(grf["grf04_exact_necessary_condition"]["q_nonnegative"] is True, "GRF04 q nonnegative drift")

    # Direct intersection, not an independence assumption:
    # y=D-2*x4. GRF04 gives |y|<=r. HPADJ10 fixes x4 mod 2, hence y mod 4.
    # One residue class mod 4 inside [-r,r] has at most floor(r/2)+1 elements.
    worst_num = -1
    worst_den = 1
    worst = None
    for g in (0, 1):
        for d in range(8, 193, 2):
            R = 3*d*d + 48*d + 96 - 96*g
            req(R >= 0 and R % 4 == 0, f"R divisibility drift {(g,d,R)}")
            r = math.isqrt(R // 4)
            joint = r // 2 + 1
            min_block = 4*d + 1
            req(33*joint <= 7*min_block, f"7/33 block inequality failed {(g,d,r,joint,min_block)}")
            if joint * worst_den > worst_num * min_block:
                worst_num, worst_den, worst = joint, min_block, (g, d, R, r, joint, min_block)

    req(worst == (0, 8, 672, 12, 7, 33), f"unexpected worst block {worst}")

    # Closed proof used by the retained certificate for every even d>=10:
    # sqrt(R0(d)) <= (112*d-104)/33 follows after squaring from Q(d)>=0.
    def Q(d: int) -> int:
        return 9277*d*d - 75568*d - 93728

    req(Q(10) == 78292, "Q(10) drift")
    for d in range(10, 193, 2):
        req(Q(d) >= 0, f"Q(d) negative at d={d}")
        if d + 2 <= 192:
            req(Q(d+2) - Q(d) == 37108*d - 114028, f"Q step identity drift at d={d}")
            req(Q(d+2) - Q(d) > 0, f"Q step not positive at d={d}")

    joint_upper = (7 * EXPECTED_ENVELOPE) // 33
    req(joint_upper == EXPECTED_JOINT, "joint upper-bound drift")
    req((13 * EXPECTED_ENVELOPE) // 33 == EXPECTED_GRF04, "GRF04 13/33 arithmetic drift")

    out = {
        "schema": "STAGE32EX5_HPADJ13_GRF04_PICARD_PARITY_UNIFORM_BOUND_V1",
        "status": "STRICTER_JOINT_GRF04_PICARD_PARITY_7_OVER_33_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id": "HPADJ-13_ex5",
        "sources": {
            "hpadj10_kernel_blob_sha1": LOCKS["hpadj10_blob"],
            "hpadj10_kernel_canonical_sha256": LOCKS["hpadj10_canonical"],
            "hpadj10_hostile_audit_reconfirmed_review_id": 5214966911,
            "grf04_v35_candidate_exact_head": "9cc20024e7842918a45210d8a7d5e2428f5f85f3",
            "grf04_v35_candidate_blob_sha1": LOCKS["grf04_blob"],
            "grf04_v35_candidate_canonical_sha256": LOCKS["grf04_canonical"],
            "grf04_v35_candidate_hostile_audited": False,
            "audited_grf04_symbolic_kernel_exact_head": "d534e107bfcf68ab1d687366afd3671a152f6e2b",
            "audited_grf04_symbolic_kernel_review_id": 5194832346,
            "audited_td01_envelope_exact_head": "54945927416a94a67533c7b06c59c5a24e50c4f1",
            "audited_td01_envelope_review_id": 5214778974,
            "audited_td01_envelope_packet_blob_sha1": "51271c11078459ad9171138c4fb6121d7a665c39",
            "audited_td01_envelope_packet_canonical_sha256": "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
        },
        "joint_block_proof": {
            "grf04_weakened_condition": "|D-2*x4| <= r_g(d), r_g(d)=floor(sqrt((3*d^2+48*d+96-96*g)/4))",
            "picard_condition": "x4 ≡ x0+x8+x10 (mod 2)",
            "mod4_intersection": "After fixing x4 mod 2, y=D-2*x4 lies in one residue class mod 4.",
            "survivors_per_block_upper": "floor(r_g(d)/2)+1",
            "genus_monotonicity": "g=0 is worst because R_1(d)=R_0(d)-96.",
            "block_size_lower": "B=N+1>=4*d+1 because e<=3*d and N=19*d-5*e.",
            "d8_check": {"R0": 672, "r0": 12, "joint_survivors_upper": 7, "minimum_block_size": 33, "ratio": "7/33"},
            "d_ge_10_proof": {
                "target": "sqrt(R_0(d)) <= (112*d-104)/33",
                "squared_difference_polynomial": "Q(d)=9277*d^2-75568*d-93728",
                "Q_10": 78292,
                "even_step_difference": "Q(d+2)-Q(d)=37108*d-114028",
                "even_step_positive_from_d10": True,
                "conclusion": "floor(r_0(d)/2)+1 <= 7*(4*d+1)/33 for every even d>=10",
            },
            "uniform_retained_fraction": "7/33",
            "applies_to_all_178_rows": True,
        },
        "candidate_bound": {
            "hpadj08_survivor_x4_complete_envelope": EXPECTED_ENVELOPE,
            "joint_uniform_fraction_numerator": 7,
            "joint_uniform_fraction_denominator": 33,
            "joint_survivor_upper_bound": joint_upper,
            "current_audited_main_upper_bound": EXPECTED_MAIN_AUDITED,
            "improvement_vs_current_audited_main": EXPECTED_MAIN_AUDITED - joint_upper,
            "hpadj12_candidate_upper_bound": EXPECTED_HPADJ12,
            "improvement_vs_hpadj12_candidate": EXPECTED_HPADJ12 - joint_upper,
            "grf04_v35_candidate_upper_bound": EXPECTED_GRF04,
            "improvement_vs_grf04_v35_candidate": EXPECTED_GRF04 - joint_upper,
            "composition_if_consumed": "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_SUBTRACTION",
            "strict_improvement": True,
        },
        "semantics": {
            "same_x4_direct_intersection_not_independence_assumption": True,
            "grf04_v35_source_candidate_is_audit_pending": True,
            "candidate_requires_independent_hostile_audit": True,
            "main_consumption_performed": False,
            "main_authority_mutated": False,
            "heavy_run_required": False,
            "new_heavy_run_used": False,
            "exact_incremental_rejected_identity_set_claimed": False,
            "current_main_upper_bound_used_as_exact_identity_set": False,
            "next_exact_unit": "Hostile-audit HPADJ13 including the audit-pending GRF04 concrete formula/domain dependency; only after PASS may a MAIN replacement handoff be built.",
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
    out["canonical_sha256_without_this_field"] = canonical(out)
    req(out["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL, "result canonical drift")
    print(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
