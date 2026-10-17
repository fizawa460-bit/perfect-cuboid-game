#!/usr/bin/env python3
"""Stage32 FIXED-DIRECTION-CERTIFICATES: exact count of unibranch-census terminals surviving the exact Hodge bound and
24 fixed-direction certificates (see CONTRACT.md for the proof).

Steps (fail-closed):
  1. exact rational forms from the retained Picard data:  Q = (A G^-1 A^T)^-1,  LIN = P G^-1 A^T Q,
     BMB = P N M^-1 N^T P^T  (N integral kernel of A, M = -N^T G N > 0 checked);  per direction lam (DIRECTIONS.json,
     all entries >= 0):  lin_D = lam.LIN,  c_D = lam^T BMB lam  -> integer-scaled forms file;
  2. the 530 UNIBRANCH-NODE-HURWITZ strata with their exact prefix counts (N220 symbolic counter, required support
     max(K, ceil((d+e)/2) - 2g + 2));
  3. compile and run the C counter (gcc -O2 -fopenmp; __int128 with overflow checks); every stratum's enumerated
     prefix count must equal step 2;
  4. INDEPENDENT Python re-implementation (itertools enumeration + Fraction arithmetic) on the 40 smallest strata must
     reproduce the C per-stratum (prefixes, Hodge survivors, final survivors);
  5. per-stratum results and totals must equal RESULT.json; per-row MIN with HPADJ22-UNIBRANCH (V51) recomputed.
usage: python verify_fixed_direction_certificates.py [--threads N] [--skip-full]   (full run about 14 min on 12 threads)
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import os
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

from flint import fmpq_mat, fmpz_mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESULT = HERE / "RESULT.json"
DIRECTIONS = HERE / "DIRECTIONS.json"
C_SRC = HERE / "count_fixed_direction_certificates.c"
V51_RESULT = ROOT / "stages/stage32/management/hpadj22-unibranch/RESULT.json"
ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def exact_forms(directions: list[dict]):
    sys.path.insert(0, str(ROOT / "stages/stage32/residual-32-01-production"))
    from hperp_integral_adapter import HperpIntegralPairingAdapter
    bundle = load_retained(ROOT / "stages/stage33/33-07/picard_base_rows_retained.py", "fdc_bundle")
    marking = load_retained(ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py", "fdc_marking")
    ad = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    Gi = [[int(v) for v in r] for r in bundle["picard_gram_64x64"]]
    Pi = [[int(v) for v in r] for r in ad.pairing_matrix.tolist()]
    exc = [sum(Pi[k][j] for k in range(92, 140)) for j in range(64)]
    deg19 = [sum(Pi[k][j] for k in range(92)) + 5 * exc[j] for j in range(64)]
    req(all(v % 19 == 0 for v in deg19), "degree row integrality")
    Ai = [Pi[l - 1] for l in ORDER] + [[v // 19 for v in deg19], exc]
    G, A, P = fmpq_mat(Gi), fmpq_mat(Ai), fmpq_mat(Pi)
    req(A.rank() == 13, "fixed map rank")
    Q = (A * G.inv() * A.transpose()).inv()
    LIN = P * G.inv() * A.transpose() * Q
    H, U = fmpz_mat([[Ai[j][i] for j in range(13)] for i in range(64)]).hnf(transform=True)
    req(all(int(H[i, j]) == 0 for i in range(13, 64) for j in range(13)), "HNF kernel shape")
    N = fmpq_mat([[int(U[r, c]) for r in range(13, 64)] for c in range(64)])
    req(all(v == 0 for v in (A * N).entries()), "kernel")
    M = -(N.transpose() * G * N)
    # M positive definite: exact LDL pivots
    Mf = [[Fraction(int(M[i, j].p), int(M[i, j].q)) for j in range(51)] for i in range(51)]
    for i in range(51):
        req(Mf[i][i] > 0, "kernel not negative definite")
        for r in range(i + 1, 51):
            f = Mf[r][i] / Mf[i][i]
            if f:
                for c in range(i, 51):
                    Mf[r][c] -= f * Mf[i][c]
    BMB = P * N * M.inv() * N.transpose() * P.transpose()
    fr = lambda x: Fraction(int(x.p), int(x.q))
    Qf = [[fr(Q[i, j]) for j in range(13)] for i in range(13)]
    LINf = [[fr(LIN[k, j]) for j in range(13)] for k in range(140)]
    dirs = []
    for dd in directions:
        lam = [Fraction(v, dd["lambda_den"]) for v in dd["lambda_num"]]
        req(len(lam) == 140 and all(v >= 0 for v in lam), "direction must be a nonnegative 140-vector")
        lrow = [sum(lam[k] * LINf[k][j] for k in range(140) if lam[k]) for j in range(13)]
        nz = [k for k in range(140) if lam[k]]
        cD = sum(lam[i] * fr(BMB[i, j]) * lam[j] for i in nz for j in nz)
        req(cD > 0, "c_D must be positive")
        dirs.append((lrow, cD))
    return Qf, dirs


def forms_text(Qf, dirs) -> str:
    qden = math.lcm(*[q.denominator for r in Qf for q in r])
    out = [str(qden)] + [" ".join(str(int(q * qden)) for q in r) for r in Qf] + [str(len(dirs))]
    for lrow, cD in dirs:
        lden = math.lcm(*[v.denominator for v in lrow])
        out.append(f"{lden} {cD.numerator} {cD.denominator}")
        out.append(" ".join(str(int(v * lden)) for v in lrow))
    return "\n".join(out) + "\n"


def strata():
    sys.path.insert(0, str(ROOT / "stages/stage32/32-01-178/nodes/N220"))
    import verify_n220_exact_symbolic_count as base
    import verify_n220_exact_symbolic_count_fast as fast
    man = base.load_canonical(ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json", base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(man["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    ex = base.build_exceptional_exact_mass_support()
    lt = fast.build_support_lt(ex)
    cum, run = [], 0
    for e in range(base.MAX_E + 1):
        run += sum(ex[e]); cum.append(run)
    cd = lambda a, b: -((-a) // b)
    out = []
    for rid in rows:
        g, d = base.parse_row_id(rid)
        K = cd(d - 16 * g + 16, 4)
        for e in range(max(8 if g == 0 else 4, K), (19 * d) // 5 + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * cd(e, 6):
                continue
            r = max(K, cd(d + e, 2) - 2 * g + 2)
            s = cum[e] - fast.rejected_fast(ex, lt, e=e, required=r)
            if s:
                out.append((g, d, e, r, s))
    out.sort(key=lambda x: (x[4], x[0], x[1], x[2]))
    return out


def python_reference(stratum, Qf, dirs):
    """Independent enumeration (recursive Python generator, its own pruning) + exact integer arithmetic."""
    g, d, e, r, _ = stratum
    L = 2 * g - 2 - d
    X = 19 * d - 5 * e
    qden = math.lcm(*[q.denominator for row in Qf for q in row])
    Qi = [[int(q * qden) for q in row] for row in Qf]
    dl = []
    for lrow, cD in dirs:
        lden = math.lcm(*[v.denominator for v in lrow])
        dl.append(([int(v * lden) for v in lrow], lden, cD.numerator, cD.denominator))

    def gen(i, left, acc):
        # 10 exceptional coordinates with total mass <= e.  Necessary for the census predicate
        # S10 + min(38, e - M10) >= r:  (e - m) >= r - s  (each later positive coordinate adds 1 to s and >= 1 to m, so
        # this slack never increases; it fails for all larger v once it fails) and  s + (#remaining) + 38 >= r.
        if i == 10:
            yield tuple(acc)
            return
        for v in range(left + 1):
            acc.append(v)
            m = e - left + v
            s = sum(1 for w in acc if w)
            if (e - m) < r - s:
                acc.pop()
                break
            if s + (9 - i) + 38 >= r:
                yield from gen(i + 1, left - v, acc)
            acc.pop()

    pref = hs = fs = 0
    for comp in gen(0, e, []):
        x = list(comp[:4]) + [0] + list(comp[4:])
        m = sum(comp)
        s = sum(1 for v in comp if v)
        if s + min(38, e - m) < r:
            continue
        if x[0] > x[1] or (x[1] + x[8] + x[9] + x[10]) % 2:
            continue
        if x[0] == x[1] and (x[5], x[6]) > (x[8], x[9]):
            continue
        pref += 1
        for x4 in range(X + 1):
            t = x[:4] + [x4] + x[5:] + [d, e]
            H = sum(Qi[i][j] * t[i] * t[j] for i in range(13) for j in range(13))   # = qden * h0
            if H < L * qden:
                continue
            hs += 1
            killed = False
            for lnum, lden, cn, cdn in dl:
                l = sum(lnum[j] * t[j] for j in range(13))                       # = lden * lin_D
                # lin_D^2 > (h0 - L) c_D  <=>  l^2 * qden * cdn > (H - L*qden) * cn * lden^2
                if l < 0 and l * l * qden * cdn > (H - L * qden) * cn * lden * lden:
                    killed = True
                    break
            fs += not killed
    return pref, hs, fs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threads", type=int, default=os.cpu_count() or 1)
    ap.add_argument("--skip-full", action="store_true", help="only forms, strata and the independent small-strata check")
    a = ap.parse_args()

    res = json.loads(RESULT.read_text(encoding="utf-8"))
    req(res.get("canonical_sha256_without_this_field") == canon(res), "RESULT.json canonical drift")
    req(not any(res["credit"].values()), "credit firewall")
    dj = json.loads(DIRECTIONS.read_text(encoding="utf-8"))
    req(len(dj["directions"]) == res["directions_count"], "direction count")
    Qf, dirs = exact_forms(dj["directions"])
    ftxt = forms_text(Qf, dirs)
    req(hashlib.sha256(ftxt.encode()).hexdigest() == res["forms_sha256"], "exact forms drift")
    st = strata()
    req(len(st) == 530 and sum(s[4] for s in st) == 3736306749, "strata/prefix totals")
    print("PASS: exact forms (Q, 24 directions) rebuilt; 530 strata, 3736306749 census prefixes", flush=True)

    per = {f"g{s[0]}-d{s[1]:03d}-e{s[2]:03d}": s for s in st}
    for s in st[:40]:
        key = f"g{s[0]}-d{s[1]:03d}-e{s[2]:03d}"
        ref = python_reference(s, Qf, dirs)
        req(list(ref) == res["per_stratum"][key], f"independent Python reference mismatch at {key}: {ref}")
    print("PASS: independent Python enumeration reproduces the 40 smallest strata", flush=True)
    if a.skip_full:
        print("SKIPPED: full C run (--skip-full)")
        return

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "forms.txt").write_text(ftxt, newline="\n")
        (tdp / "strata.txt").write_text(f"{len(st)}\n" + "".join(f"{g} {d} {e} {r} {s}\n" for g, d, e, r, s in st), newline="\n")
        exe = tdp / "count"
        subprocess.run(["gcc", "-O2", "-fopenmp", "-o", str(exe), str(C_SRC)], check=True)
        env = dict(os.environ, OMP_NUM_THREADS=str(a.threads))
        out = subprocess.run([str(exe), str(tdp / "forms.txt"), str(tdp / "strata.txt")], check=True, text=True,
                             stdout=subprocess.PIPE, env=env).stdout
    got = {}
    for line in out.split("\n"):
        if line.strip():
            g, d, e, p, h, f = map(int, line.split())
            got[f"g{g}-d{d:03d}-e{e:03d}"] = [p, h, f]
    req(set(got) == set(per), "stratum set")
    for k, s in per.items():
        req(got[k][0] == s[4], f"C prefix count mismatch at {k}")
    req(got == res["per_stratum"], "per-stratum regression against RESULT.json")
    rows: dict[str, int] = {}
    for k, v in got.items():
        rows[k[:7]] = rows.get(k[:7], 0) + v[2]
    v51 = json.loads(V51_RESULT.read_text(encoding="utf-8"))["per_row"]
    per_row_min = {k: min(rows.get(k, 0), int(v["hpadj22_unibranch"])) for k, v in v51.items()}
    req({k: str(v) for k, v in per_row_min.items() if v} == res["per_row_min_with_v51"], "per-row MIN regression")
    tot = sum(per_row_min.values())
    req(str(sum(v[2] for v in got.values())) == res["totals"]["final_survivors"] and str(tot) == res["totals"]["per_row_min_with_v51"], "totals")
    print(f"PASS: C counter reproduces all 530 strata; final survivors {res['totals']['final_survivors']}; "
          f"per-row MIN with V51 = {tot} compressed terminals (not Picard classes)")
    print("PASS: zero credit; MAIN authority unchanged")


if __name__ == "__main__":
    main()
