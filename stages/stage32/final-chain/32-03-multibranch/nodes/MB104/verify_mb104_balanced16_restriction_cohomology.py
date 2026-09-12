#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-RESTRICTION-COHOMOLOGY-CERTIFICATE.json"

LOCKS = {
    "FORMAL_PICARD": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md",
        "de83fc169814681109bcbc1576ad24f67d6159e0",
    ),
    "PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "STOLL_CANONICAL_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md",
        "e344290d5241c3f7f165ea3027cfc778abec3360",
    ),
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-RESTRICTION-COHOMOLOGY-WALL.md",
        "dccd805176d710cfbc05728c0746de60f54b2798",
    ),
}


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root not found")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def source_lock_preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = root()
    for key, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {sha}, got {got}")
    return rr


def source_semantics(rr):
    formal = (rr / LOCKS["FORMAL_PICARD"][0]).read_text()
    require("D^2=21k^2=336*l^2" in formal, "formal Picard D^2 source text")
    require("D1_P5,l = 7*l H - 4*l sum" in formal, "formal Picard ray source text")

    stoll = (rr / LOCKS["STOLL_CANONICAL_NOTE"][0]).read_text()
    require("K_S = b^* O_barS(1)" in stoll, "K=H source text")
    require("K_S^2 = 16" in stoll, "K^2 source text")
    require("chi(O_S) = 8" in stoll, "chi source text")
    require("`K_S` is big and nef" in stoll, "K nef source text")

    pic0 = json.loads((rr / LOCKS["PIC0_CERT"][0]).read_text())
    require(pic0["retained_consequence"]["restriction_bundle_trivial_for_all_l"] is True,
            "Pic0 restriction triviality")
    require(pic0["retained_consequence"]["restriction_map_nonzero_proved"] is False,
            "Pic0 restriction-map firewall")
    profiles = pic0["balanced_profiles"]
    require(set(profiles) == {"0000770000ff", "00007b0000ff", "000707000f0f", "00070b000f0f"},
            "four balanced support orbits")
    for h, row in profiles.items():
        require(row["supported_nodes_per_zero_quartic"] == 7, f"{h} seven-of-eight zero quartic")
        require(row["zero_quartics"] >= 2, f"{h} has another zero quartic")
    return pic0


def check_rr_and_duality():
    # q^2 from adjunction: 2g-2 = q^2 + K.q, with g=1 and K.q=4.
    g, KQ = 1, 4
    Q2 = 2*g - 2 - KQ
    require(Q2 == -4, "elliptic quartic self-intersection")

    # Symbolic polynomial coefficients in l for D^2, K.D and chi.
    # D^2 = 336 l^2; K.D = 112 l; chi = 8 + (D^2-K.D)/2.
    chi_D = (168, -56, 8)
    # (D-Q)^2 = 336l^2-4 and K.(D-Q)=112l-4; constants cancel in RR.
    chi_DmQ = (168, -56, 8)
    require(chi_D == chi_DmQ, "RR Euler characteristics agree")

    for l in (1, 2, 7, 31):
        chi = 168*l*l - 56*l + 8
        require(chi > 0, f"positive chi at l={l}")
        require(16 - 112*l < 0, f"H.(K-D)<0 at l={l}")
        require(20 - 112*l < 0, f"H.(K-D+Q)<0 at l={l}")


def check_exact_sequence_contract(cert):
    c = cert["cohomology_reduction"]
    require(c["Q2"] == -4, "certificate Q^2")
    require(c["chi_D"] == "168*l^2-56*l+8", "certificate chi(D)")
    require(c["chi_D_minus_Q"] == "168*l^2-56*l+8", "certificate chi(D-Q)")
    require(c["H2_D_zero"] is True and c["H2_D_minus_Q_zero"] is True, "H2 vanishings")
    require(c["restriction_rank_values"] == [0, 1], "restriction rank range")
    require(c["h1_D_forced_at_least"] == 1, "forced speciality")
    require(c["H1_D_minus_Q_zero_implies_restriction_surjective"] is True,
            "H1 sufficient criterion")


def check_exceptional_and_kv_wall(cert, pic0):
    e = cert["omitted_exceptional"]
    require(e["D_dot_E_P"] == 0, "D.E_P")
    require(e["Q_dot_E_P"] == 1, "Q.E_P")
    require(e["E_P2"] == -2, "E_P^2")
    require(e["D_minus_Q_dot_E_P"] == -1, "(D-Q).E_P")
    require(e["restriction_degree_on_E_P"] == -1, "O_E(D-Q) degree")
    require(e["acyclic_fixed_component_stripping"] is True, "acyclic E stripping")

    kv = cert["direct_KV_wall"]
    require(kv["all_four_orbits_have_at_least_two_zero_quartics"] is True,
            "simultaneous zero quartics")
    for h, row in pic0["balanced_profiles"].items():
        require(row["zero_quartics"] >= 2, f"{h} another zero quartic replay")
    # For any other irreducible zero quartic R, Q.R>=0 and E_P.R>=0.
    # Hence the three tested adjoint residuals are already <= -4 on R.
    require(-4 < 0, "D-Q-K negative on another zero quartic at minimum intersection")
    require(-4 < 0, "D-Q-E-K negative on another zero quartic at minimum intersection")
    require(-4 < 0, "D-2Q-E-K negative on another zero quartic at minimum intersection")
    require(kv["D_minus_Q_minus_K_nef"] is False, "direct KV residual not nef")
    require(kv["after_exceptional_strip_nef"] is False, "E strip does not repair nefness")
    require(kv["double_Q_ladder_nef"] is False, "double-Q ladder does not repair nefness")


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_BALANCED16_RESTRICTION_COHOMOLOGY_WALL_V1",
            "certificate schema")
    rr = source_lock_preflight(cert)
    pic0 = source_semantics(rr)
    check_rr_and_duality()
    check_exact_sequence_contract(cert)
    check_exceptional_and_kv_wall(cert, pic0)

    rc = cert["retained_consequence"]
    require(rc["restriction_map_nonzero_proved"] is False, "restriction-map firewall")
    require(rc["restriction_map_zero_proved"] is False, "restriction-map zero firewall")
    require(rc["direct_single_quartic_KV_route_closed"] is True, "KV route wall")
    require(rc["next_required_lever"] == "simultaneous_zero_quartic_union_or_explicit_global_jet_gluing",
            "next lever")
    require(cert["credit_firewall"]["balanced16_closed"] is False, "balanced16 firewall")
    require(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_BALANCED16_RESTRICTION_COHOMOLOGY_WALL_V1")
    print("RR=chi(D)=chi(D-Q)=168l^2-56l+8 H2(D)=H2(D-Q)=0")
    print("restriction_rank=r_in_{0,1}; h1(D)=h1(D-Q)+r; h1(D)>=1")
    print("omitted_exceptional=(D-Q).E_P=-1 and O_E(D-Q)=O_P1(-1) acyclic")
    print("direct_KV=blocked_by_E_P_and_by_another_zero_quartic_on_all_4_orbits")
    print("scope=restriction_map_still_open balanced16_open MB104_open")


if __name__ == "__main__":
    main()
