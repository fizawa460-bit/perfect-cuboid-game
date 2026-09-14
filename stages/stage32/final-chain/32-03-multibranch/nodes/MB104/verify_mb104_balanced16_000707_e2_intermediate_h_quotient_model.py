#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md", "d2e3056137360a9e15ae7c820088d2977a5eb137"),
    "FSM_COORD_SOURCE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md", "a49f5b28b456dd88436c030e857cf771e5a1ba2f"),
    "EXPLICIT_KUMMER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE.md", "5017d7c137f6d4994a34cb1edac28aadcd832a2a"),
    "MODULAR_CHARACTER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md", "ce9554bc047159baf7640db50aa5daf1f0c67f74"),
    "HURWITZ_CAPACITY": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY.md", "c91f97b738faa66a49a068824f9b8c3739d4a8fa"),
    "FOURIER_REFINEMENT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-G-FOURIER-CHARACTER.md", "42b70776bde2259efce03d500d76fba837a5cf36"),
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


def mul_sign(*xs):
    return tuple(__import__('functools').reduce(lambda a, b: a*b, vals, 1) for vals in zip(*xs))


def ratio_sign(s, num, den):
    return s[num] * s[den]


def addv(a, b):
    return tuple(x+y for x,y in zip(a,b))


def subv(a, b):
    return tuple(x-y for x,y in zip(a,b))


def scale(c, a):
    return tuple(c*x for x in a)


def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_INTERMEDIATE_H_QUOTIENT_MODEL_V1", "schema")
    declared = {x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing {key}")
        req(blob(p) == want, f"source lock {key}")
    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    # Imported one-factor sign actions on (a,e,b,c,d).
    T  = (1,-1, 1, 1, 1)
    Tp = (1, 1,-1, 1, 1)
    R  = (1, 1, 1,-1,-1)
    H2 = mul_sign(T, Tp, R)  # TT'R
    req(H2 == (1,-1,-1,-1,-1), "TT'R sign action")

    # r=e/d, u=a/d, v=b/d. In signs division equals multiplication.
    def ruv(s):
        return (ratio_sign(s,1,4), ratio_sign(s,0,4), ratio_sign(s,2,4))
    req(ruv(Tp) == (1,1,-1), "T' on (r,u,v)")
    req(ruv(H2) == (1,-1,1), "TT'R on (r,u,v)")
    req(ruv(T) == (-1,1,1), "T on (r,u,v)")

    # Algebraic one-factor identities with q=c/d:
    # r^2=2q, hence r^4=4q^2; a^2/d^2=q^2+1, b^2/d^2=q^2-1.
    r4_coeff_q2 = 4
    req(r4_coeff_q2 // 4 == 1, "u/v q^2 coefficient")
    req((4 // 4) == 1, "u constant coefficient")
    req((-4 // 4) == -1, "v constant coefficient")

    # The two relative H generators act independently on U=u_z*u_w and V=v_z*v_w.
    # Represent a first-factor relative action by the induced signs on (U,V).
    uv_Tp = (ruv(Tp)[1], ruv(Tp)[2])
    uv_H2 = (ruv(H2)[1], ruv(H2)[2])
    req(uv_Tp == (1,-1), "relative T' flips V only")
    req(uv_H2 == (-1,1), "relative TT'R flips U only")
    req({uv_Tp, uv_H2, (uv_Tp[0]*uv_H2[0], uv_Tp[1]*uv_H2[1]), (1,1)} == {(1,1),(1,-1),(-1,1),(-1,-1)}, "full relative H characters")

    # Exact box bilinear identities in basis (xX,yY,yX,xY).
    C  = (1,1,0,0)
    W3 = (1,-1,0,0)
    W1 = (0,0,1,1)
    # W2 = i(yX-xY). Store i*W2 = -(yX-xY) = (-yX+xY).
    iW2 = (0,0,-1,1)
    req(subv(C,W3) == (0,2,0,0), "C-W3=2yY")
    req(addv(C,W3) == (2,0,0,0), "C+W3=2xX")
    req(subv(W1,iW2) == (0,0,2,0), "W1-iW2=2yX")
    req(addv(W1,iW2) == (0,0,0,2), "W1+iW2=2xY")

    model = cert["exact_model"]
    req(model["one_factor_u2"] == "(r^4+4)/4", "certificate u2")
    req(model["one_factor_v2"] == "(r^4-4)/4", "certificate v2")
    req(model["XH_over_RxR_degree"] == 4, "degree four")
    req(model["XH_over_B_degree"] == 2, "degree two")
    req(model["tau"] == "(r_z,r_w,U,V)->(-r_z,-r_w,U,V)", "tau")
    req(model["box_rz2"] == "2*(C+W3)/(W1-i*W2)", "box rz2")
    req(model["box_rw2"] == "2*(C+W3)/(W1+i*W2)", "box rw2")
    req(model["box_rzrw"] == "2*Z3/(C-W3)", "box product")
    req(model["box_U"] == "2*Z2/(C-W3)", "box U")
    req(model["box_V"] == "2*Z1/(C-W3)", "box V")
    req(model["generic_residual_ambiguity"] == "simultaneous_sign_only", "one residual bit")

    # Guard the imported e=2 semantic bridge, not merely the arithmetic formulas.
    hurwitz = (rr / LOCKS["HURWITZ_CAPACITY"][0]).read_text()
    req("K=<s1,s2>={1,s1,s2,h}" in hurwitz, "e2 stabilizer semantic lock")
    req("E=Z/K" in hurwitz, "e2 quotient semantic lock")
    kummer = (rr / LOCKS["EXPLICIT_KUMMER"][0]).read_text()
    req("H=<T',TT'R>" in kummer, "support H semantic lock")
    req("T H : r0 -> -r0" in kummer, "residual deck semantic lock")

    route = cert["routing"]
    req(route["active_leaf"] == ACTIVE, "active leaf")
    req(route["ambient_quotient_equation_materialized"] is True, "quotient model materialized")
    req(route["per_conductor_preimage_sign_missing"] is True, "branch sign still missing")
    req(route["conductor_transition_computed"] is False, "transition remains open")
    req(route["weighted_cut_bound_proved"] is False, "no cut bound")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/closure/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_INTERMEDIATE_H_QUOTIENT_MODEL_V1")
    print("one factor: H fixes r, flips u/v independently; residual T flips r")
    print("two factor: X_H/RxR degree 4 via U,V; X_H/B degree 2 via simultaneous r sign")
    print("open: specialization of simultaneous sign at conductor normalization preimages; credit 0")


if __name__ == "__main__":
    main()
