#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md",
        "bf5f1fe82db9c1bfd1a5465ddf4e7015a3d2bb72",
    ),
    "HURWITZ_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY-CERTIFICATE.json",
        "76b458d2f21af7113764447e1a8064e957b025e7",
    ),
    "JOINT_PAIR_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY-CERTIFICATE.json",
        "8fb4578029037c088c17b6cfb219955c9d0dc4d6",
    ),
    "BOUNDARY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION-CERTIFICATE.json",
        "1f51cf157b3de6db393049af41fda0843e0f2068",
    ),
    "NODE_TYPE_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md",
        "a29161602c0b38f0607794e56e61068b8cb9735d",
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


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL missing {key}: {rel}")
        got = blob(p)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL {key}: expected {expected}, got {got}")


def load(key):
    return json.loads((root() / LOCKS[key][0]).read_text())


def subgroup_generated(*gens):
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
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_000707_RESIDUAL_SHEET_CHARACTER_V1", "schema")
    preflight(cert)

    hz = load("HURWITZ_CERT")
    jp = load("JOINT_PAIR_CERT")
    bd = load("BOUNDARY_CERT")

    # Exact upstream scope.
    req(hz["support"]["mask"] == "000707000f0f", "support mask")
    req(hz["support"]["node_type_counts"] == [7, 7, 0], "two used and one absent type")
    req(hz["scope_firewall"]["e2_closed"] is False and hz["scope_firewall"]["e4_closed"] is False, "upstream e cases open")
    req(jp["scope"]["allowed_e"] == [2, 4], "joint-pair e cases")
    req(jp["joint_quotient"]["H_order"] == 4 and jp["joint_quotient"]["R_genus"] == 0, "H and R")
    req(bd["rank_two_subgroup"]["order"] == 4, "boundary H order")

    # Finite F2^3 model. G0 is the plane with high bit zero.
    G = set(range(8))
    G0 = {0, 1, 2, 3}
    s1, s2, s3 = 4, 5, 6
    H = subgroup_generated(s1, s2)
    req(len(G) == 8 and len(G0) == 4 and len(H) == 4, "group orders")
    req(s1 not in G0 and s2 not in G0 and s3 not in G0, "singular types outside G0")
    req((s1 ^ s2) in G0, "product of used outside types lies in G0")
    req(H & G0 == {0, s1 ^ s2}, "H cap G0 order two")
    req(s3 not in H, "absent singular type outside H")
    residual_coset = {s3 ^ h for h in H}
    req(len(residual_coset) == 4 and residual_coset == (G - H), "nontrivial G/H coset")
    req(len(G) // len(H) == 2, "residual quotient order two")

    gq = cert["group_quotients"]
    req(gq["G_order"] == 8 and gq["G0_order"] == 4 and gq["H_order"] == 4, "certificate group orders")
    req(gq["H_intersection_G0_order"] == 2, "certificate H cap G0")
    req(gq["residual_group"] == "G/H ~= Z/2", "residual group")
    req(gq["residual_branch_points"] == 2, "two residual branch points")
    req(gq["residual_branch_type"] == "third/absent singular stabilizer type", "absent branch type")

    # Degree arithmetic unifies e=2 and e=4 downstairs.
    cm = cert["common_downstairs_map"]
    req(cm["e2"]["psi_degree"] == "28*l" and cm["e2"]["phi_degree"] == "56*l", "e2 degree chain")
    req(2 * 28 == 56, "e2 q degree arithmetic")
    req(cm["e4"]["Q_to_E_degree"] == 2 and cm["e4"]["Q_to_E_etale"] is True, "e4 residual cover")
    req(cm["e4"]["psi_degree"] == "56*l" and cm["e4"]["phi_degree"] == "56*l", "e4 degree chain")
    req(2 * 56 == 2 * 56, "e4 descent degree arithmetic")

    # Half-fiber arithmetic: both doubled half-fibers have total degree 56*l.
    hf = cert["half_fiber"]
    req(hf["absent_value_1_fiber"] == "phi^*(a)=2*A", "first half-fiber")
    req(hf["absent_value_2_fiber"] == "phi^*(b)=2*B", "second half-fiber")
    req(hf["deg_A"] == "28*l" and hf["deg_B"] == "28*l", "half-fiber degrees")
    req(2 * 28 == 56, "doubled half-fiber degree")
    req(hf["eta"] == "O_E(A-B)" and hf["eta_in"] == "Pic^0(E)[2]", "eta definition")

    fp = cert["fiber_product"]
    req(fp["T_to_E_etale_degree"] == 2, "residual pullback degree")
    req(fp["classifying_line_bundle"] == "eta", "residual class")
    req(fp["eta_zero_iff_split"] is True and fp["eta_nonzero_iff_connected"] is True, "split/connected criterion")

    cc = cert["case_classification"]
    req(cc["e2_eta_zero"] is True and cc["e4_eta_nonzero"] is True, "case eta values")
    req(cc["e2_iff_eta_zero"] is True and cc["e4_iff_eta_nonzero"] is True, "case iff classification")

    jc = cert["joint_factor_constraint"]
    req(jc["two_factor_maps"] is True and jc["eta_1_equals_eta_2"] is True, "same residual character from both factors")

    fw = cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False, "e cases remain open")
    req(fw["orbit_000707_closed"] is False, "orbit remains open")
    req(fw["geometric_uniform_ray_support_population"] == 864, "geometric frontier")
    req(fw["mb104_equality_packet_support_population"] == 768, "packet frontier")
    req(fw["MB104_complete"] is False and fw["span5_closed"] is False, "MB104/span5 firewall")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False, "credit firewall")
    req(fw["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_RESIDUAL_SHEET_CHARACTER_V1")
    print("residual G/H double cover classified by eta=O_E(A-B) in Pic0(E)[2]")
    print("e=2 iff eta=0; e=4 iff eta!=0; both factor maps must recover the same eta")
    print("firewall: eta not yet computed from exact factor-grid/theta data; e=2,e=4 remain open")


if __name__ == "__main__":
    main()
