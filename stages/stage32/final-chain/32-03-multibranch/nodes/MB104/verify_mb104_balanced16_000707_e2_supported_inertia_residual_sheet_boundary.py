#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-SUPPORTED-INERTIA-RESIDUAL-SHEET-BOUNDARY-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SUPPORTED-INERTIA-RESIDUAL-SHEET-BOUNDARY.md",
        "5e3b070959078f5f73ed93c84d071c15d50b0c27",
    ),
    "NODE_TYPE_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md",
        "a29161602c0b38f0607794e56e61068b8cb9735d",
    ),
    "RESIDUAL_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md",
        "bf5f1fe82db9c1bfd1a5465ddf4e7015a3d2bb72",
    ),
    "LOCAL_THETA_LIFT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-LOCAL-THETA-PRODUCT-LIFT.md",
        "9490f2b765351f779eac90febb9a56c2965f3e8d",
    ),
    "INVARIANT_NORMALIZATION": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION.md",
        "7b749f361535031164904bd479fddd69ccc12929",
    ),
    "SQRT_BASECHANGE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SQRT-FACTOR-BASECHANGE-SEMANTICS.md",
        "9d688ee48fd0df8d7ad4e2c6abc146fa2728ba7e",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def generated_subgroup(*gens):
    out = {0}
    changed = True
    while changed:
        changed = False
        for x in list(out):
            for g in gens:
                y = x ^ g
                if y not in out:
                    out.add(y)
                    changed = True
    return out


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_SUPPORTED_INERTIA_RESIDUAL_SHEET_BOUNDARY_V1", "schema")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob(p) == expected, f"source lock {key}")

    recorded = cert["canonical_sha256_without_this_field"]
    canonical_obj = dict(cert)
    del canonical_obj["canonical_sha256_without_this_field"]
    canonical = json.dumps(canonical_obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    req(hashlib.sha256(canonical).hexdigest() == recorded, "canonical sha256")

    support = cert["support"]
    req(support["mask"] == "000707000f0f", "support mask")
    req(support["node_type_counts"] == [7, 7, 0], "node type counts")
    req(support["used_singular_types"] == ["s1", "s2"], "used singular types")
    req(support["absent_singular_type"] == "s3", "absent singular type")

    # Same finite F2^3 model used by the retained residual-sheet verifier.
    G = set(range(8))
    s1, s2, s3 = 4, 5, 6
    H = generated_subgroup(s1, s2)
    req(len(G) == 8 and len(H) == 4, "G/H orders")
    req(s1 in H and s2 in H, "supported inertias lie in H")
    req(s3 not in H, "absent inertia outside H")
    req(len(G - H) == 4 and {s3 ^ h for h in H} == G - H, "s3H is nontrivial residual coset")

    gm = cert["group_model"]
    req(gm["G_order"] == 8 and gm["H_order"] == 4 and gm["residual_order"] == 2, "certificate group orders")
    req(gm["s1_in_H"] is True and gm["s2_in_H"] is True and gm["s3_in_H"] is False, "certificate membership")
    req(gm["residual_nontrivial_coset"] == "s3 H", "certificate residual coset")

    sem = cert["semantic_boundary"]
    req(sem["supported_node_involution_belongs_to_H"] is True, "supported involution belongs H")
    req(sem["supported_node_involution_survives_in_R_equals_C8_over_H"] is False, "supported involution dies in H quotient")
    req(sem["supported_node_plus_minus_exchanges_residual_G_over_H_sheets"] is False, "local plus/minus is not residual sheet")
    req(sem["exact_local_A1_jet_alone_determines_residual_sheet"] is False, "local A1 jet insufficiency")

    routing = cert["routing"]
    req(routing["active_leaf"] == "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP", "active leaf")
    req("H-orbit coordinate" in routing["active_semantics"], "H-orbit routing")
    req("s3H" in routing["active_semantics"], "residual-coset routing")

    fw = cert["credit_firewall"]
    req(fw["conductor_sign_computed"] is False and fw["cross_sheet_upper_bound_proved"] is False, "no sign/bound credit")
    req(fw["e2_closed"] is False and fw["e4_closed"] is False and fw["orbit_000707_closed"] is False, "open cases")
    req(fw["geometric_uniform_ray_support_population"] == 864, "geometric core")
    req(fw["mb104_equality_packet_support_population"] == 768, "packet core")
    req(fw["finite_degree_window_proved"] is False and fw["MB104_complete"] is False, "MB104 firewall")
    req(fw["receiver_credit"] is False and fw["effectivity_credit"] is False, "receiver/effectivity firewall")
    req(fw["theorem_credit"] is False and fw["endpoint_credit"] is False, "theorem/endpoint firewall")
    req(fw["perfect_cuboid_existence_claim"] is False and fw["perfect_cuboid_nonexistence_claim"] is False, "perfect cuboid firewall")
    req(fw["heavy_compute_authorized"] is False and fw["merge_authorized"] is False, "heavy/merge firewall")

    print("PASS STAGE32_MB104_000707_E2_SUPPORTED_INERTIA_RESIDUAL_SHEET_BOUNDARY_V1")
    print("supported s1/s2 node involutions lie in H and die in C8/H")
    print("residual sheet is the nontrivial G/H coset s3H; local supported-node +/- cannot determine it")
    print("firewall: e=2,e=4,000707 remain open; no MB104/receiver/theorem/endpoint credit")


if __name__ == "__main__":
    main()
