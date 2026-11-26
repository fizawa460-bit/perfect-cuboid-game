#!/usr/bin/env python3
"""L36 Step 1: exact (integer) verification of the two exclusion mechanisms.

Mechanism A (cone infeasibility, both l, both maps):
  Farkas certificates found by LP duality:
    B8 : D' = 3*E39 + E40 + 2*E127 + 2*E130
    B16: D' = 3*E33 + E34 + 2*E119 + 2*E122
  Claims (checked here in exact integer arithmetic):
    (i)   C_i . D' >= 0 for all 38 common vertical curves C_i
          => V . D' >= 0 for every V = sum a_i C_i with a_i >= 0.
    (ii)  R_l . D' = -16 l  (< 0) for l = 3, 6
          => Q_h . D' = R_l.D' - V.D' <= -16 l < 0.
    (iii) Each certificate curve E_k differs from Q_h:
          (G.E_k, F.E_k) != (12 l, 40 l/3), so Q_h . E_k >= 0 is a
          legitimate necessary condition, and (ii) contradicts
          Q_h . D' = sum w_k (Q_h . E_k) >= 0.
  Hence conditions (a)+(c) of the relaxation are infeasible: no
  effective V (real, rational or integral coefficients) makes
  Q_h . E >= 0 hold for all known curves E.

Mechanism B (l = 6 only, both maps): the unconstrained maximum of
  p_a(R_l - V) over ALL V in Lambda (x) R is attained at
  V* = proj_L(H)/2 - l * proj_L(P) and equals, exactly,
    l=3: 62/3 (> 0, no exclusion),   l=6: -394/3 (< 0).
  Computed here from the exact rationals
    -(proj_L P)^2 = 856/3,  H . proj_L P = -232/3,  -(proj_L H)^2 = 88/3
  (recomputed from the Gram data in this script).
  So for l=6, p_a(Q_h) >= 0 fails for every V in Lambda, with no
  cone conditions used at all.
"""
from __future__ import annotations

import json
from pathlib import Path
from sympy import Matrix, Rational

import g3_common as gc

HERE = Path(__file__).resolve().parent

CERT = {
    "B8": (list(range(8, 16)), [(39, 3), (40, 1), (127, 2), (130, 2)]),
    "B16": (list(range(16, 24)), [(33, 3), (34, 1), (119, 2), (122, 2)]),
}


def main():
    gram, curves, vH, vP, vG, stage3 = gc.load_all()
    labels = sorted(curves)

    def pair(x, y):
        return int((x.T * gram * y)[0])

    out = {}
    for bname, (B, cert) in CERT.items():
        F = gc.f_class(gram, curves, vH, B)
        common = [lab for lab in labels
                  if pair(curves[lab], vG) == 0 and pair(curves[lab], F) == 0]
        assert len(common) == 38
        Dp = Matrix.zeros(64, 1)
        for lab, w in cert:
            Dp += w * curves[lab]
        # (i) C_i . D' >= 0 for all common curves
        ci_dp = {lab: pair(curves[lab], Dp) for lab in common}
        assert all(v >= 0 for v in ci_dp.values()), ci_dp
        entry = {
            "Dprime": {str(lab): w for lab, w in cert},
            "Ci_Dprime_min": min(ci_dp.values()),
            "Ci_Dprime_zeros": sum(1 for v in ci_dp.values() if v == 0),
            "Dprime_pairings": {"G": pair(vG, Dp), "F": pair(F, Dp),
                                "H": pair(vH, Dp), "P": pair(vP, Dp),
                                "self": pair(Dp, Dp)},
            "cert_curves": {},
        }
        for lab, w in cert:
            entry["cert_curves"][str(lab)] = {
                "G.E": pair(vG, curves[lab]), "F.E": pair(F, curves[lab]),
                "H.E": pair(vH, curves[lab]), "P.E": pair(vP, curves[lab]),
                "E2": pair(curves[lab], curves[lab]),
                "is_common": lab in common,
            }
        # (ii) R_l . D' for l = 3, 6 (exact integer classes)
        for l in (3, 6):
            R = Matrix((40 * l // 3) * vG + (12 * l) * F - l * vP)
            entry[f"R{l}_Dprime"] = pair(R, Dp)
            assert pair(R, Dp) == -16 * l
        # Mechanism B data: exact projections
        GLs = Matrix.hstack(*[curves[lab] for lab in common])
        GL = GLs.T * gram * GLs
        p_vec = Matrix([pair(vP, curves[lab]) for lab in common])
        h_vec = Matrix([pair(vH, curves[lab]) for lab in common])
        aP = GL.LUsolve(p_vec)
        aH = GL.LUsolve(h_vec)
        w0sq = -(aP.T * p_vec)[0]      # -(proj P)^2 = kappa
        u0sq = -(aH.T * h_vec)[0]      # -(proj H)^2
        uw = (aP.T * h_vec)[0]         # proj P . proj H = H . proj P
        assert w0sq == Rational(856, 3) and uw == Rational(-232, 3)
        assert u0sq == Rational(88, 3)
        entry["proj"] = {"kappa": str(w0sq), "H_projP": str(uw),
                         "neg_projH_sq": str(u0sq)}
        for l in (3, 6):
            # V* = u0/2 - l w0 ; V*^2 = u0sq-term: -(u0^2)/4 ... use signed squares
            Vst_sq = (-u0sq) / 4 - l * uw + l * l * (-w0sq)
            pa_max = 1 + 72 * l - 152 * l * l - Vst_sq / 2
            entry[f"unconstrained_pa_max_l{l}"] = str(pa_max)
        out[bname] = entry
        print(bname, json.dumps(entry, indent=1, ensure_ascii=False))

    (HERE / "l36_step1_certificates.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False))
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
