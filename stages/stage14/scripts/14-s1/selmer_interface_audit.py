#!/usr/bin/env python3
"""Stage14-s1 exact full-2-torsion descent interface and deterministic PARI audit.

The Stage14 fiber attached to a primitive oriented Pythagorean face F=(S,X,H) is

    E_F: y^2 = x(x-S^2)(x+X^2).

This is the integral scaling of E_t: y^2=x(x-1)(x+t^2), t=X/S.
The script records the exact Kummer 2-descent interface, then uses PARI/GP
ellrank with effort=0 on a deterministic active/inactive sample. PARI returns
unconditional Mordell-Weil rank bounds [r1,r2] and Cassels-pairing information s.
For full rational 2-torsion, dim_F2 E[2](Q)=2 and PARI's documented relation gives

    dim Sel_2(E) = r2 + 2 + s.

No equality between Selmer rank and Mordell-Weil rank is assumed.
"""

from collections import defaultdict
from math import gcd
from pathlib import Path
import json
import shutil
import subprocess
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH_SCRIPT = ROOT / "stages/stage14/scripts/14-4/rank_jump_graph_audit.py"
OUTPUT = ROOT / "stages/stage14/data/14-s1/selmer_interface_audit.json"
MAX_B = 2_000_000
SAMPLE_EACH = 96
HEIGHT_BINS = (0, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000,
               500_000, 1_000_000, 2_000_000)


def primitive_faces(max_h):
    out = set()
    m = 2
    while m * m + 1 <= max_h:
        for n in range(1, m):
            if ((m - n) & 1) == 0 or gcd(m, n) != 1:
                continue
            u = m * m - n * n
            v = 2 * m * n
            h = m * m + n * n
            if h > max_h:
                continue
            out.add((u, v, h))
            out.add((v, u, h))
        m += 1
    return sorted(out, key=lambda f: (f[2], f[0], f[1]))


def active_first_hits():
    mod = runpy.run_path(str(GRAPH_SCRIPT))
    keep, _ = mod["enumerate_multi"](MAX_B)
    object_edges = mod["object_edges"]
    first = {}
    for (a, b, c, d), (mask, ds) in keep.items():
        if d > MAX_B or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            first[f1] = min(first.get(f1, d), d)
            first[f2] = min(first.get(f2, d), d)
    assert len(first) == 490
    return first


def hbin(h):
    for lo, hi in zip(HEIGHT_BINS, HEIGHT_BINS[1:]):
        if lo < h <= hi:
            return (lo, hi)
    raise ValueError(h)


def even_sample(rows, n):
    if len(rows) <= n:
        return list(rows)
    if n == 1:
        return [rows[len(rows)//2]]
    idx = [round(i * (len(rows) - 1) / (n - 1)) for i in range(n)]
    return [rows[i] for i in idx]


def balanced_samples(active_map, all_faces):
    active = sorted(active_map, key=lambda f: (f[2], f[0], f[1]))
    inactive = [f for f in all_faces if f not in active_map]
    inactive_bins = defaultdict(list)
    for f in inactive:
        inactive_bins[hbin(f[2])].append(f)

    active_sample = even_sample(active, SAMPLE_EACH)
    quota = defaultdict(int)
    for f in active_sample:
        quota[hbin(f[2])] += 1

    inactive_sample = []
    for b in sorted(quota):
        pool = inactive_bins[b]
        need = quota[b]
        assert len(pool) >= need
        inactive_sample.extend(even_sample(pool, need))
    assert len(active_sample) == len(inactive_sample) == SAMPLE_EACH
    return active_sample, sorted(inactive_sample, key=lambda f: (f[2], f[0], f[1]))


def curve_coefficients(face):
    S, X, H = face
    assert gcd(S, X) == 1 and S*S + X*X == H*H
    return (X*X - S*S, -(S*S)*(X*X))


def discriminant_formula(face):
    S, X, _ = face
    return 16 * (S**4) * (X**4) * ((S*S + X*X)**2)


def gp_audit(rows):
    gp = shutil.which("gp")
    if gp is None:
        raise SystemExit("PARI/GP executable 'gp' is required (Ubuntu package: pari-gp)")
    lines = ["default(parisizemax, 4G);"]
    for rec in rows:
        i = rec["id"]
        a2, a4 = curve_coefficients(tuple(rec["face"]))
        lines.append(
            f'E=ellinit([0,{a2},0,{a4},0]);'
            f'R=ellrank(E,0);'
            f'print("{i}|",R[1],"|",R[2],"|",R[3],"|",ellrootno(E));'
        )
    lines.append("quit;")
    proc = subprocess.run(
        [gp, "-q"],
        input="\n".join(lines) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )
    got = {}
    for line in proc.stdout.splitlines():
        if "|" not in line:
            continue
        p = line.strip().split("|")
        if len(p) != 5:
            continue
        got[p[0]] = {
            "rank_lower": int(p[1]),
            "rank_upper": int(p[2]),
            "sha_2_mod_4_rank_s": int(p[3]),
            "root_number": int(p[4]),
        }
    assert len(got) == len(rows), (len(got), len(rows), proc.stderr[-2000:])
    return got


def descent_interface():
    return {
        "rational_model": "E_t: y^2=x(x-1)(x+t^2), t=X/S",
        "integral_model": "E_F: Y^2=Z(Z-S^2)(Z+X^2)",
        "integral_coefficients": "[a1,a2,a3,a4,a6]=[0,X^2-S^2,0,-S^2 X^2,0]",
        "rational_2_torsion_x": ["0", "S^2", "-X^2"],
        "E2_dimension_over_F2": 2,
        "kummer_map": "[P] -> (Z, Z-S^2, Z+X^2) in (Q*/Q*^2)^3, with product a square",
        "covering_equations": [
            "d1*u1^2 - d2*u2^2 = S^2",
            "d3*u3^2 - d1*u1^2 = X^2",
            "d1*d2*d3 is a square class"
        ],
        "bad_prime_support": "only infinity and primes dividing 2*S*X*H need local attention for the 2-coverings",
        "discriminant": "Delta=16*S^4*X^4*H^4",
        "pari_contract": (
            "ellrank(E,0) returns unconditional [r1,r2,s,L]; for full rational 2-torsion "
            "dim Sel_2(E)=r2+2+s. Rank is certified only when r1=r2."
        ),
    }


def summarize(rows):
    def one(group):
        xs = [r for r in rows if r["status"] == group]
        exact = [r for r in xs if r["rank_lower"] == r["rank_upper"]]
        positive_cert = [r for r in xs if r["rank_lower"] > 0]
        rank0_cert = [r for r in xs if r["rank_upper"] == 0]
        selmer_nontrivial_beyond_torsion = [r for r in xs if r["selmer_2_rank"] > 2]
        odd_root = [r for r in xs if r["root_number"] == -1]
        return {
            "sample_size": len(xs),
            "exact_rank_certified": len(exact),
            "positive_rank_certified": len(positive_cert),
            "rank_zero_certified": len(rank0_cert),
            "selmer_rank_gt_torsion": len(selmer_nontrivial_beyond_torsion),
            "root_number_minus_one": len(odd_root),
            "mean_selmer_2_rank": sum(r["selmer_2_rank"] for r in xs) / len(xs),
            "mean_rank_upper": sum(r["rank_upper"] for r in xs) / len(xs),
        }
    return {"active": one("active"), "inactive_control": one("inactive_control")}


def main():
    active_map = active_first_hits()
    all_faces = primitive_faces(MAX_B)
    active_sample, inactive_sample = balanced_samples(active_map, all_faces)

    rows = []
    for j, face in enumerate(active_sample):
        rows.append({
            "id": f"A{j:03d}", "status": "active", "face": list(face),
            "first_physical_height_mu": active_map[face],
        })
    for j, face in enumerate(inactive_sample):
        rows.append({
            "id": f"I{j:03d}", "status": "inactive_control", "face": list(face),
            "first_physical_height_mu": None,
        })

    gp = gp_audit(rows)
    for rec in rows:
        face = tuple(rec["face"])
        rec.update(gp[rec["id"]])
        rec["selmer_2_rank"] = rec["rank_upper"] + 2 + rec["sha_2_mod_4_rank_s"]
        rec["rank_certified"] = rec["rank_lower"] == rec["rank_upper"]
        rec["curve_a2_a4"] = list(curve_coefficients(face))
        rec["discriminant"] = discriminant_formula(face)
        S, X, H = face
        assert rec["discriminant"] == 16*(S**4)*(X**4)*(H**4)

    assert all(r["rank_upper"] >= 1 for r in rows if r["status"] == "active")

    summary = summarize(rows)
    report = {
        "metadata": {
            "stage": "14-s1",
            "title": "Exact full-2-torsion descent interface and deterministic PARI Selmer/rank-bound audit",
            "max_stage14_B": MAX_B,
            "global_active_vertices_at_ceiling": len(active_map),
            "sample_each": SAMPLE_EACH,
            "pari_effort": 0,
        },
        "descent_interface": descent_interface(),
        "finite_audit": {
            "sampling": (
                "96 active fibers evenly sampled from all 490 active vertices through B=2m; "
                "96 inactive primitive Pythagorean controls selected in the same face-hypotenuse strata."
            ),
            "summary": summary,
            "rows": rows,
        },
        "theorem_boundary": {
            "active_implies_positive_rank": "imported merged Stage14-4af theorem",
            "selmer_rank_equals_mw_rank_assumed": False,
            "root_number_parity_used_to_change_rank_bounds": False,
            "bsd_used": False,
            "parity_conjecture_used": False,
            "average_selmer_theorem_imported": False,
            "inactive_control_means_rank_zero": False,
            "interpretation": (
                "s1 measures an unconditional 2-Selmer/rank-bound envelope on a deterministic finite sample. "
                "Inactive means no Stage14 physical partner through B=2m, not Mordell-Weil rank zero."
            ),
        },
        "decision": {
            "STAGE14_S1": "COMPLETE_EXACT_DESCENT_INTERFACE_AND_FINITE_PARIRANK_AUDIT",
            "EXACT_FULL_2_TORSION_DESCENT_INTERFACE_LOCKED": True,
            "PARI_UNCONDITIONAL_RANK_BOUNDS_AUDITED": True,
            "FINITE_ACTIVE_INACTIVE_SELMER_AUDIT_COMPLETE": True,
            "SELMER_RANK_USED_AS_MW_RANK_EQUALITY": False,
            "ROOT_NUMBER_PARITY_USED_AS_RANK_EQUALITY": False,
            "POSITIVE_RANK_DENSITY_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s2 Pythagorean-base Selmer/local-density sieve",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["finite_audit"]["summary"], indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
