#!/usr/bin/env python3
"""Re-refine stored slack-0 maps (state.jsonl with critical points 0, oo, 1, lam...) to high precision.

Newton in mpmath (dps 110) on the same system as build_maps.mp_refine, but started from the
stored mp values (not from doubles) and with the normalisation ell = e_k (largest coefficient).
Usage: python -I refine5.py N IN_STATE OUT_STATE
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mpmath as mp
import build_maps as bm
import build_maps5 as b5

mp.mp.dps = 110


def refine(n, rec):
    P, Q, cps, vals = rec
    assert cps[0] == 0 and cps[1] == mp.inf and cps[2] == 1
    x = list(P) + list(Q); lam = list(cps[3:])
    kmax = max(range(len(x)), key=lambda k: abs(x[k]))
    s = x[kmax]; x = [t / s for t in x]
    zz = x + lam; m = len(zz)
    def FJ(zz):
        lam = zz[2 * n + 2:]; x = zz[:2 * n + 2]
        cl = [mp.mpf(0), "oo", mp.mpf(1)] + list(lam)
        F = []; J = mp.matrix(m, m); r = 0
        for i, (c, y) in enumerate(zip(cl, vals)):
            yv = (mp.mpc(bm.BH[y][0]), mp.mpc(bm.BH[y][1]))
            for d in (0, 1):
                row = bm.cond_rows(n, c, yv, d)
                F.append(mp.fsum(a * b for a, b in zip(row, x)))
                for k in range(2 * n + 2): J[r, k] = row[k]
                if i >= 3: J[r, 2 * n + 2 + i - 3] = mp.fsum(a * b for a, b in zip(bm.drow(n, c, yv, d), x))
                r += 1
        F.append(x[kmax] - 1); J[r, kmax] = 1
        return F, J
    step = None
    for _ in range(25):
        F, J = FJ(zz)
        dz = mp.lu_solve(J, mp.matrix([-f for f in F]))
        zz = [a + dz[k] for k, a in enumerate(zz)]
        step = mp.norm(dz)
        if step < mp.mpf(10) ** -100: break
    F, _ = FJ(zz)
    res = mp.norm(mp.matrix(F))
    cond = mp.mnorm(J, 1) * mp.mnorm(mp.inverse(J), 1)
    return (zz[:n + 1], zz[n + 1:2 * n + 2], [mp.mpf(0), mp.inf, mp.mpf(1)] + zz[2 * n + 2:], vals), res, step, cond


def main():
    n = int(sys.argv[1]); src, dst = sys.argv[2], sys.argv[3]
    rows = []; worst = 0; worst_cond = 0
    with open(src, encoding="utf-8") as f:
        lines = [json.loads(l) for l in f if l.strip()]
    for i, r in enumerate(lines):
        rec = b5.parse_state_map(r)
        new, res, step, cond = refine(n, rec)
        assert res < mp.mpf(10) ** -95, (i, r["datum"], mp.nstr(res, 5))
        worst = max(worst, res); worst_cond = max(worst_cond, cond)
        P, Q, cps, vals = new
        rows.append({"datum": r["datum"], "target": r["target"],
                     "P": [mp.nstr(c, 100) for c in P], "Q": [mp.nstr(c, 100) for c in Q],
                     "critical_points": [b5.cstr(c) if c in (0, 1) or c == mp.inf else mp.nstr(c, 100) for c in cps],
                     "critical_values": list(vals),
                     "max_verified_residual": mp.nstr(res, 8), "jacobian_cond": mp.nstr(cond, 5)})
    tmp = dst + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    os.replace(tmp, dst)
    print(f"refined {len(rows)} maps; worst residual {mp.nstr(worst, 5)}; worst Jacobian cond {mp.nstr(worst_cond, 5)}")


if __name__ == "__main__":
    main()
