#!/usr/bin/env python3
"""Cheap exact gap test before any 58D enumeration.

On each fixed (d,e,base4) affine Picard fiber, certify an inequality

    pairing_energy <= lambda * Q + mu(base4),

where Q=d^2/16-C^2 and pairing_energy is the sum of squares of all 140
pairings.  Nonnegative integral pairings with the fixed normal/exceptional
masses have an independent discrete lower bound.  If the upper bound on the
bad shell lies below that lower bound, bad-shell UNSAT follows without
Fincke--Pohst enumeration.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"

SAMPLE_BASE4 = (
    (0, 1, 1, 1),
    (0, 4, 4, 8),
    (0, 6, 2, 6),
    (1, 2, 2, 2),
    (1, 3, 3, 3),
)


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "module spec")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def pd(m: Matrix) -> bool:
    if m != m.T:
        return False
    try:
        l, d = m.LDLdecomposition(hermitian=False)
    except Exception:
        return False
    return m == l * d * l.T and all(d[i, i] > 0 for i in range(d.rows))


def min_square_sum(total: int, count: int) -> int:
    q, r = divmod(total, count)
    return (count - r) * q * q + r * (q + 1) * (q + 1)


def main() -> None:
    # Fail closed before executing the research engine.
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine05_engine")

    F, A, I, RK, R, _L, _diag, _coeff, _dual, P, gram = eng.build()
    req(R.shape == (eng.N, eng.N) and pd(R), "kernel Q form")

    pair_form = RK.T * P.T * P * RK
    req(pair_form == pair_form.T and pd(pair_form), "kernel pairing-energy form")

    # Smallest integer lambda making lambda*Q_kernel - pairing_energy_kernel PD.
    hi = 1
    while not pd(hi * R - pair_form):
        hi *= 2
        req(hi <= (1 << 20), "lambda search cap")
    lo = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pd(mid * R - pair_form):
            hi = mid
        else:
            lo = mid
    lam = hi
    dom = lam * R - pair_form
    ldl_l, ldl_d = dom.LDLdecomposition(hermitian=False)
    req(dom == ldl_l * ldl_d * ldl_l.T, "domination LDL replay")
    req(all(ldl_d[i, i] > 0 for i in range(ldl_d.rows)), "domination LDL")

    def inverse_quadratic(b: Matrix):
        # Exact b^T dom^-1 b via dom=L D L^T, without forming dom^-1.
        y = []
        for i in range(ldl_l.rows):
            v = b[i, 0]
            for j in range(i):
                v -= ldl_l[i, j] * y[j]
            v /= ldl_l[i, i]
            y.append(v)
        return sum(y[i] * y[i] / ldl_d[i, i] for i in range(len(y)))

    normal_lb = min_square_sum(eng.NORMAL_MASS, 92)
    exceptional_lb = min_square_sum(eng.E, 48)
    energy_lb = normal_lb + exceptional_lb
    q_bad_upper = Rational(eng.D * eng.D, 16) - eng.LOW
    req(q_bad_upper == Rational(161, 4), "bad-shell Q upper drift")

    rows = []
    for base4 in SAMPLE_BASE4:
        target = Matrix([eng.D, eng.E, *base4])
        ic = I.inv() * target
        integral_image = all(getattr(x, "q", 1) == 1 for x in ic)
        row = {"base4": list(base4), "hnf_image_integral": integral_image}
        if not integral_image:
            row.update({
                "classification": "HNF_IMAGE_UNSAT",
                "bad_shell_unsat_by_energy_gap": True,
            })
            rows.append(row)
            continue

        bp = A * ic
        req(all(getattr(x, "q", 1) == 1 for x in bp), "integral affine base point")
        p0 = P * bp
        q0 = (bp.T * gram * bp)[0]
        cross = RK.T * gram * bp
        s = RK.T * P.T * p0
        e0 = (p0.T * p0)[0]

        # lambda*Q(C)-E(C) = z^T dom z + 2 b^T z + c.
        b = -lam * cross - s
        c = lam * (Rational(eng.D * eng.D, 16) - q0) - e0
        min_gap = c - inverse_quadratic(b)
        mu = -min_gap
        bad_energy_upper = lam * q_bad_upper + mu
        gap = Rational(energy_lb) - bad_energy_upper
        proved = bool(gap > 0)

        row.update({
            "lambda": lam,
            "mu": str(mu),
            "bad_shell_Q_upper": str(q_bad_upper),
            "bad_shell_pairing_energy_upper": str(bad_energy_upper),
            "nonnegative_integral_mass_energy_lower": energy_lb,
            "strict_gap": str(gap),
            "bad_shell_unsat_by_energy_gap": proved,
            "classification": (
                "BAD_SHELL_UNSAT_EXACT_ENERGY_GAP"
                if proved else
                "ENERGY_GAP_INCONCLUSIVE"
            ),
        })
        rows.append(row)

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE05_ENERGY_NORM_GAP_PROBE_V1",
        "status": "PASS_EXACT_FIVE_KEY_ENERGY_GAP_PROBE",
        "kernel_domination": {
            "lambda_min_integer_pd": lam,
            "statement": "pairing_energy_kernel < lambda * Q_kernel for every nonzero kernel vector",
        },
        "mass_energy_lower_bound": {
            "normal_mass": eng.NORMAL_MASS,
            "normal_count": 92,
            "normal_min_square_sum": normal_lb,
            "exceptional_mass": eng.E,
            "exceptional_count": 48,
            "exceptional_min_square_sum": exceptional_lb,
            "total_min_square_sum": energy_lb,
        },
        "bad_shell": {
            "C2": [eng.LOW, eng.HIGH],
            "Q_upper": str(q_bad_upper),
        },
        "rows": rows,
        "summary": {
            "sample_count": len(rows),
            "exact_bad_shell_unsat_count": sum(bool(r["bad_shell_unsat_by_energy_gap"]) for r in rows),
            "inconclusive_count": sum(r["classification"] == "ENERGY_GAP_INCONCLUSIVE" for r in rows),
        },
        "credit": {
            "effectivity": False,
            "main": False,
            "receiver": False,
            "theorem": False,
            "endpoint": False,
            "merge": False,
        },
        "next": (
            "If all five keys close, extend the same cheap exact calculation to the 343-key d18/e8 base4 census before any FP58 heavy run. "
            "If not, use the exact gaps to prioritize only the inconclusive keys for FP58."
        ),
    }
    print("EFF_AFFINE05_ENERGY_GAP=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
