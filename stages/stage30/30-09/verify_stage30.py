#!/usr/bin/env python3
"""Independent final verifier for Stage30 MODULAR-S4-ACTION.

This checker deliberately does not import or execute any earlier Stage30 verifier.
It rechecks immutable Git-blob pins, reconstructs PSL2(Z/4), re-derives the
K8 -> endpoint sign formula on all eight elements, and cross-checks the frozen
common-model/cocycle/physical-scope certificates.
"""

from __future__ import annotations

from itertools import product
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def git_blob_sha(rel):
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def neg_mod4(m):
    return tuple(tuple((-x) % 4 for x in row) for row in m)


def canon_mod4(m):
    return min(m, neg_mod4(m))


def reconstruct_psl2_z4():
    sl2 = []
    for a,b,c,d in product(range(4), repeat=4):
        if (a*d-b*c) % 4 == 1:
            sl2.append(((a,b),(c,d)))
    psl2 = sorted({canon_mod4(m) for m in sl2})
    require(len(sl2) == 48, "SL2(Z/4) order != 48")
    require(len(psl2) == 24, "PSL2(Z/4) order != 24")
    return psl2


def endpoint_image_from_A(A):
    a = A[0][0] % 2
    b = A[0][1] % 2
    c = A[1][0] % 2
    require(A[1][1] % 2 == a, "A is not in sl2(F2) trace-zero form")
    bits = ((a+b)%2, (a+c)%2, a)
    names = [name for bit,name in zip(bits,("b1","b2","b3")) if bit]
    if not names:
        return "identity", bits
    return "delta_{" + ",".join(names) + "}", bits


def kappa_from_A(A):
    return [
        [(1 + 4*A[0][0]) % 8, (4*A[0][1]) % 8],
        [(4*A[1][0]) % 8, (1 + 4*A[1][1]) % 8],
    ]


def main():
    manifest = json.loads((HERE / "input-manifest.json").read_text(encoding="utf-8"))
    action_ref = json.loads((HERE / "action-tables.json").read_text(encoding="utf-8"))
    eqmap = json.loads((HERE / "equivariant-map.json").read_text(encoding="utf-8"))
    gcoc = json.loads((HERE / "galois-cocycle.json").read_text(encoding="utf-8"))
    defect_ref = json.loads((HERE / "defect-classification.json").read_text(encoding="utf-8"))
    final = json.loads((HERE / "final-certificate.json").read_text(encoding="utf-8"))

    # Immutable source pins. Mutable controller state is intentionally excluded.
    for item in manifest["inputs"]:
        require(git_blob_sha(item["path"]) == item["blob_sha"],
                f"Git blob SHA mismatch: {item['path']}")
    require(manifest["mutable_controller_hash_pinned"] is False,
            "mutable controller must not be a permanent mathematical input pin")

    actions = load("stages/stage30/30-02C/action-tables.json")
    common = load("stages/stage30/30-05/common-anchor.json")
    spec = load("stages/stage30/30-06/semilinear-spec.json")
    semcert = load("stages/stage30/30-06C/semilinear-certificate.json")
    defects = load("stages/stage30/30-07/defect-classification.json")
    physical = load("stages/stage30/30-08/physical-adapter.json")
    audit08 = load("stages/stage30/30-08/audit-state.json")

    # Concrete finite groups, reconstructed rather than imported from an abstract S4.
    psl2 = reconstruct_psl2_z4()
    require(len(actions["arrangement"]["elements"]) == 24, "arrangement action order != 24")
    require(len(actions["modular"]["elements"]) == 24, "modular action row count != 24")
    source_mats = {
        tuple(tuple(x for x in row) for row in rec["matrix"])
        for rec in actions["modular"]["elements"]
    }
    require(source_mats == set(psl2), "Task-A modular matrices != reconstructed PSL2(Z/4)")
    v_ids = []
    for rec in actions["modular"]["elements"]:
        m = rec["matrix"]
        if [[x % 2 for x in row] for row in m] == [[1,0],[0,1]]:
            v_ids.append(rec["id"])
    require(sorted(v_ids) == ["g04","g06","g12","g14"], "V_mod reconstruction mismatch")
    require(action_ref["expected"]["v_mod_ids"] == sorted(v_ids), "final action wrapper V_mod mismatch")

    # Common geometric anchor: the actual branch action has V4 kernel and S3 image.
    branch = common["branch_squareclass_action"]
    require(branch["kernel_ids"] == ["g04","g06","g12","g14"], "common-anchor kernel mismatch")
    require(branch["kernel_order"] == 4 and branch["image_order"] == 6 and branch["image_is_S3"],
            "common-anchor branch projection mismatch")
    require(eqmap["branch_projection"]["kernel_order"] == 4, "final equivariant-map kernel mismatch")
    require(eqmap["branch_projection"]["image_order"] == 6, "final equivariant-map image mismatch")

    # Galois/cocycle certificate. 30-06C already reconstructed the 24 projective lifts;
    # here we independently bind that certificate to the frozen source spec and final wrapper.
    require(spec["common_model_descent_cocycle"]["c_sigma"] == "delta_a3", "spec c_sigma mismatch")
    require(spec["residual_group"]["theta_fixes_V_mod_pointwise"] is True, "theta does not fix V_mod")
    require(semcert["coordinate_cocycle"]["name"] == "delta_a3", "certificate c_sigma mismatch")
    require(semcert["coordinate_cocycle"]["quadratic_cocycle_identity_verified"] is True,
            "cocycle identity not verified")
    require(semcert["endpoint_projective_group"]["order"] == 24, "endpoint projective order mismatch")
    require(semcert["endpoint_projective_group"]["multiplication_all_576_verified"] is True,
            "576 multiplication checks not certified")
    sem_rows = semcert["modular_group"]["elements"]
    require(len(sem_rows) == 24, "semilinear certificate does not cover 24 elements")
    require(all(row["semilinear_pass"] for row in sem_rows), "a semilinear row failed")
    require(gcoc["c_sigma"] == "delta_a3" and gcoc["semilinear_all24_verified"] is True,
            "final Galois wrapper mismatch")

    # Re-derive all eight K8 elements and endpoint sign images from A in sl2(F2).
    require(len(defects["rows"]) == 8, "K8 row count != 8")
    ids = set()
    qclasses = set()
    weight_counts = [0,0,0,0]
    for row in defects["rows"]:
        did = row["defect_id"]
        require(did not in ids, f"duplicate defect id {did}")
        ids.add(did)
        expected_image, bits = endpoint_image_from_A(row["A_f2"])
        require(row["endpoint_adapter_image"] == expected_image, f"endpoint image mismatch {did}")
        require(row["kappa_mod8"] == kappa_from_A(row["A_f2"]), f"kappa mismatch {did}")
        require(row["sigma_image"] == did, f"sigma is not trivial on {did}")
        require(row["eliminated"] is False, f"unexpected elimination {did}")
        qclasses.add(row["q_descent_class"])
        weight_counts[sum(bits)] += 1
        require(defect_ref["endpoint_images"][did] == expected_image, f"final defect wrapper mismatch {did}")
    require(weight_counts == [1,3,3,1], "ordinary Hamming-weight orbit multiplicities mismatch")
    require(len(qclasses) == 8, "marked Q-descent classes are not eight singletons")
    require(defects["defect_elimination_count"] == 0, "source defect elimination count changed")
    require(defect_ref["defect_elimination_count"] == 0, "final defect elimination count changed")

    # Physical-open scope and audited receiver closure.
    require(physical["source_scope"]["physical_open_non_cusp"] is True, "physical open cusp firewall failed")
    require(physical["source_scope"]["physical_open_g0_stabilizer_free"] is True,
            "physical open stabilizer firewall failed")
    require(physical["source_scope"]["compactified_boundary_extension_required_for_physical_open"] is False,
            "unexpected compactified boundary requirement")
    require(audit08["audit_verdict"] == "PASS_R29_KUM5_NONOBSTRUCTIVE_ADAPTER_CLOSURE",
            "30-08 hostile audit not materialized as PASS")
    require(audit08["r29_kum5_discharged"] is True and audit08["kernel_closed"] is True,
            "receiver/kernel closure not audited")

    # Final closure and firewalls.
    require(final["closure"]["r29_kum5_discharged"] is True, "final receiver closure mismatch")
    require(final["closure"]["kernel_closed"] is True, "final kernel closure mismatch")
    require(final["closure"]["defect_elimination_count"] == 0, "final elimination count mismatch")
    require(final["route_consequence"]["q11_modular_color_after"] == "AMBER", "route color drift")
    require(final["route_consequence"]["route_color_changed"] is False, "route color changed unexpectedly")
    require(final["firewalls"]["perfect_cuboid_existence_claim"] is False, "forbidden existence claim")
    require(final["firewalls"]["perfect_cuboid_nonexistence_claim"] is False, "forbidden nonexistence claim")
    require(final["stage30_closed"] is False and final["final_audit_required"] is True,
            "30-09 must not pre-grant final Stage30 closure")

    print("STAGE30_FINAL_CERTIFICATE=PASS")
    print("PSL2_Z4_ORDER=24")
    print("V_MOD_ORDER=4")
    print("SEMI_LINEAR_24_OF_24=PASS")
    print("K8_DEFECT_ROWS=8")
    print("MARKED_Q_DESCENT_CLASSES=8")
    print("DEFECT_ELIMINATION_COUNT=0")
    print("R29_KUM5=DISCHARGED_NONOBSTRUCTIVE")
    print("K16_C2_MODULAR_S4_ACTION=CLOSED_PENDING_STAGE30_FINAL_AUDIT")
    print("Q11_MODULAR=AMBER")


if __name__ == "__main__":
    main()
