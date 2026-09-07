#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage32-ex1" / "ex1-03-smooth-ambient-singularity-ledger.json"

def canonical_sha256(obj):
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def req(cond, msg):
    if not cond:
        raise AssertionError(msg)

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    c = load_json(CERT)
    req(canonical_sha256(c) == c["canonical_sha256_without_this_field"], "canonical hash mismatch")
    req(c["canonical_sha256_without_this_field"] == "4324234386213810a6de8f7ef2e32712006e628d80291dad4f9d74e6c1e03ac5", "unexpected certificate hash")

    deps = c["source_locks"]
    for key in ("ex1_00_candidate", "ex1_01_candidate", "ex1_02_candidate"):
        p = ROOT / deps[key]["path"]
        req(p.is_file(), f"missing dependency {key}")
        d = load_json(p)
        req(canonical_sha256(d) == deps[key]["canonical_sha256"], f"dependency hash mismatch {key}")

    sp = ROOT / deps["surface_invariants"]["path"]
    req(sp.is_file(), "missing surface source lock")
    req(git_blob_sha1(sp) == deps["surface_invariants"]["blob_sha1"], "surface source blob mismatch")

    ex0 = load_json(ROOT / deps["ex1_00_candidate"]["path"])
    req(ex0["v6_target"]["K_dot_D"] == 186, "K.D mismatch")
    req(ex0["v6_target"]["D_square"] == 758, "D^2 mismatch")
    req(ex0["v6_target"]["required_total_normalization_genus_defect"] == 472, "global delta mismatch")

    env = c["global_numerical_envelope"]
    req(env["total_delta_all_locations"] == 472, "wrong total delta")
    req(env["delta_U_min"] == 0 and env["delta_U_max"] == 472, "wrong delta_U range")
    req(env["smooth_locus_singular_point_count_upper_bound"] == 472, "wrong singular point upper bound")
    req(env["total_smooth_locus_branch_excess_upper_bound"] == 472, "wrong branch excess upper bound")
    req(sum(d + 1 for d in range(1, 473)) == 112100, "local pair envelope count arithmetic")
    req(sum(d for d in range(1, 473)) == 111628, "multibranch pair envelope count arithmetic")
    req(env["local_delta_branch_pair_over_envelope_count"] == 112100, "stored local pair count mismatch")
    req(env["local_multibranch_pair_over_envelope_count"] == 111628, "stored multibranch count mismatch")
    req(env["local_unibranch_delta_pair_count"] == 472, "stored unibranch count mismatch")

    hyp = c["canonical_hyperplane_multiplicity_lemma"]
    req(hyp["canonical_degree"] == 186, "hyperplane canonical degree mismatch")
    req(hyp["self_intersection"] == 758, "hyperplane self intersection mismatch")
    req(hyp["canonical_model_dimension"] == 6, "canonical ambient dimension mismatch")
    req(186 - 758 == -572, "residual intersection arithmetic mismatch")

    src = c["external_source_locks"]
    req(src["delta_definition"]["tag"] == "0C3Q", "wrong delta source tag")
    req(src["branch_lower_bound"]["tag"] == "0C43", "wrong branch source tag")
    req("delta invariant >= number of geometric branches - 1" in src["branch_lower_bound"]["statement"], "branch inequality source wording missing")

    status = c["branch_status"]
    req(status["smooth_ambient_branch_excluded"] is False, "forbidden smooth branch exclusion")
    req(status["smooth_ambient_branch_exactly_accounted_at_coarse_numerical_layer"] is True, "coarse ledger missing")
    req(status["next_leaf"] == "EX1-04_GLOBAL_DELTA_CONTACT_INTERSECTION_COUPLING", "wrong next leaf")

    out = c["exit"]
    req(out["smooth_ambient_curve_singularity_branch_closed"] is False, "smooth branch falsely closed")
    req(out["smooth_locus_numerical_residual_ledger_complete"] is True, "numerical ledger not complete")
    req(out["branch_exclusion_credit"] is False, "forbidden branch exclusion credit")
    req(out["full_target_closure"] is False, "forbidden full closure")

    f = c["firewalls"]
    for key in (
        "branch_excess_identified_with_delta",
        "coarse_delta_branch_pair_promoted_to_analytic_realization",
        "canonical_multiplicity_budget_promoted_to_delta_bound",
        "smooth_ambient_branch_claimed_excluded",
        "local_plane_singularity_constructed_as_v6_member",
        "stage32_main_credit", "receiver_credit", "theorem_credit", "endpoint_credit",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"
    ):
        req(f[key] is False, f"firewall violated: {key}")

    print("PASS_STAGE32EX1_EX1_03_SMOOTH_AMBIENT_SINGULARITY_LEDGER")

if __name__ == "__main__":
    main()
