#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md",
        "ce9554bc047159baf7640db50aa5daf1f0c67f74",
    ),
    "FSM_COORD_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md",
        "a49f5b28b456dd88436c030e857cf771e5a1ba2f",
    ),
    "NODE_TYPE_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md",
        "a29161602c0b38f0607794e56e61068b8cb9735d",
    ),
    "BOUNDARY_SATURATION": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md",
        "aa9a7215467428b55b18ef296ced91b63ec4bf07",
    ),
    "RESIDUAL_SHEET": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md",
        "bf5f1fe82db9c1bfd1a5465ddf4e7015a3d2bb72",
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

def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def mm(A, B):
    return (
        (
            (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % 8,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % 8,
        ),
        (
            (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % 8,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % 8,
        ),
    )

I = ((1,0),(0,1))
T = ((1,4),(0,1))
TP = ((1,0),(4,1))
R = ((5,0),(0,5))

def pw2(M, e):
    return M if e else I

def cls(tau, upsilon, rho):
    return mm(mm(pw2(T,tau), pw2(TP,upsilon)), pw2(R,rho))

def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_MODULAR_CONDUCTOR_RESIDUAL_DECK_CHARACTER_V2", "schema")

    declared = {x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob_sha1(p) == expected, f"source lock {key}")

    TTpR = mm(mm(T,TP),R)
    TR = mm(T,R)
    TTp = mm(T,TP)
    TpR = mm(TP,R)
    H = {I, TP, TR, TTpR}
    G0 = {I, TTp, TR, TpR}
    req(len(H) == 4 and len(G0) == 4, "subgroup orders")
    req(H != G0, "support H differs from Beauville G0")
    req(TP in H and TP not in G0, "Tprime witness")

    seen = set()
    for tau in (0,1):
        for upsilon in (0,1):
            for rho in (0,1):
                M = cls(tau,upsilon,rho)
                seen.add(M)
                A,B = M[0]
                C,D = M[1]
                req(D % 8 == A % 8, "Gamma[4] determinant diagonal form")
                chi_res = (rho + tau) % 2
                chi_B = (rho + tau + upsilon) % 2
                req((M in H) == (chi_res == 0), "residual kernel H")
                req((A+B) % 8 == (1 if chi_res == 0 else 5), "A+B residual congruence")
                req((M in G0) == (chi_B == 0), "Beauville kernel G0")
                req((A+B+C) % 8 == (1 if chi_B == 0 else 5), "A+B+C Beauville congruence")
                r_sign = -1 if chi_res else 1
                req(r_sign == (-1 if (tau+rho)%2 else 1), "r sign character")
    req(len(seen) == 8, "eight deck classes")

    grp = cert["support_specific_group"]
    req(grp["H_equals_G0"] is False and grp["witness_Tprime_in_H_not_G0"] is True, "certificate subgroup correction")

    mc = cert["mod8_class"]
    req(mc["residual_character"] == "rho+tau mod 2", "certificate residual character")
    req(mc["residual_kernel_test"] == "A+B == 1 mod 8", "certificate residual congruence")
    req(mc["beauville_kernel_test"] == "A+B+C == 1 mod 8", "certificate Beauville congruence")
    req(mc["Tprime_residual_bit"] == 0 and mc["Tprime_beauville_bit"] == 1, "Tprime character split")

    qc = cert["quotient_coordinate"]
    req(qc["r"] == "e/d" and qc["x"] == "c/d", "quotient coordinates")
    req(qc["relation"] == "r^2=2*x", "theta quotient relation")
    req(qc["H_fixes_r"] is True and qc["fixed_field"] == "C(r)", "H-invariant coordinate")
    req(qc["residual_action"] == "T:r->-r", "residual action")
    req(qc["q"] == "s=r^2", "residual quotient map")
    req(qc["square_root"] == "sqrt(h)=r=e/d", "explicit residual square root")

    ce = cert["conductor_evaluator"]
    req(ce["transition_elements_materialized"] is False, "pair transitions remain missing")
    req(ce["individual_signs_assigned"] is False, "no conductor signs")
    req(ce["weighted_cut_bound_proved"] is False, "no weighted-cut bound")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/closure/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_MODULAR_CONDUCTOR_RESIDUAL_DECK_CHARACTER_V2")
    print("corrected: residual G/H character is A+B mod 8, not Beauville A+B+C mod 8")
    print("explicit: R=C8/H has coordinate r=theta10(z)/theta10(2z), residual T acts r->-r")
    print("firewall: transition M_(u,v) still missing; e=2,e=4,000707 open; credit 0")

if __name__ == "__main__":
    main()
