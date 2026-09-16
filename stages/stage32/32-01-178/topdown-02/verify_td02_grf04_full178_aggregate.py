#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "compressed_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "prefix_checkpoint": (
        "stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json",
        "eb823cc2f99d74456d5701b4673f848f18ba3151",
    ),
    "full178_manifest": (
        "stages/stage32/residual-32-01-production/full178-manifest.json",
        "0a46b34e278688240656b4977e9cb7f589e90e06",
    ),
    "corrected_adjunction": (
        "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
    ),
    "grf04": (
        "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json",
        "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    ),
    "full178_contract": (
        "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json",
        "ca1b195a3ee8e786707e1ef50b404ee8c19f1429",
    ),
    "hperp_probe": (
        "stages/stage32/32-01-178/topdown-02/TD02-GRF04-HPERP-PROBE.json",
        "08528d746df7730f247fb461d034ee787ea86e08",
    ),
    "bounded_bc_verifier": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bc_envelope_bounded.py",
        "3ce709a2afe9d1acb573cb7c4c1b2e7bff4b53ae",
    ),
    "bounded_canonical_verifier": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_canonical_interval_bounded.py",
        "17ca036da982583a0495220dc1ab9e23452f5506",
    ),
    "hpadj08_v29": (
        "stages/stage32/management/hpadj08-main-disposition/HPADJ08-V29-MAIN-BOUND-REPLACEMENT.json",
        "68a01142d0af4285d2a7801bf0e6808321ee689c",
    ),
}

HMAX = 96
INF = 10**30
EXPECTED_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_ROWS = 178
EXPECTED_RELAXED_PANEL = 71_384_787_021_929_133_241_956
EXPECTED_SURVIVOR_UPPER = 1_666_897_772_020_475_143_768
EXPECTED_ROW_STREAM_SHA256 = "bf091551094c774df62983d55916d2337fd7d4008188fc81baa8628a5c95eec6"
EXPECTED_BOUNDED_RELAXED_PANEL = 38_076_510_118_826
EXPECTED_BOUNDED_SURVIVOR_UPPER = 2_080_529_210_067
PRIOR_BOUNDED_CANONICAL_SURVIVORS = 611_555_346_552
REFERENCE_HPADJ08_UPPER = 6_703_403_803_993_210_101_494


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def verified_sources() -> dict[str, bytes]:
    out = {}
    for name, (rel, expected) in LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), f"missing source {name}")
        raw = path.read_bytes()
        req(git_blob(raw) == expected, f"source drift {name}")
        out[name] = raw
    return out


def load_module(name: str, path: Path, raw: bytes):
    old = sys.modules.get(name)
    try:
        mod = types.ModuleType(name)
        mod.__file__ = str(path)
        sys.modules[name] = mod
        exec(compile(raw, str(path), "exec"), mod.__dict__)
        return mod
    finally:
        if old is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = old


def qmin3(s: int) -> int:
    # Exact integer minimum of u^2+v^2+w^2 for u+v+w=s, u,v,w>=0.
    q, r = divmod(s, 3)
    return r * (q + 1) ** 2 + (3 - r) * q * q


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def canonical_t_bounds(b: int, c: int) -> tuple[int, int]:
    # Source-locked TD02 canonical envelope:
    # t=x0+x1+x6+x9, t==c mod2.
    lo = c & 1
    if (c & 1) == 0 and b > c:
        lo = 2
    if b == 0:
        hi = 0 if c == 0 else c - 2
    else:
        hi = c + 2 * (b // 2)
    return lo, hi


def even_interval_count_sum(lower: int, upper: int) -> tuple[int, int, int, int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0, lo, hi
    n = (hi - lo) // 2 + 1
    return n, n * (lo + hi) // 2, lo, hi


def build_bc_count_minq(H: int):
    # At fixed b=x1+x5+x9 and c=x0+x6+x8+x10 retain only:
    #  (i) exact number of canonical/parity exceptional assignments, and
    # (ii) exact minimum of their square sum.
    # This is enough for a safe GRF04 survivor upper bound.
    B = [[(0, INF) for _ in range(2)] for __ in range(H + 1)]
    C = [[(0, INF) for _ in range(2)] for __ in range(H + 1)]
    D = [[(0, INF) for _ in range(2)] for __ in range(H + 1)]

    for m in range(H + 1):
        acc = [[0, INF], [0, INF]]
        for x9 in range(m + 1):
            x5 = m - x9
            p = x9 & 1
            q = x5*x5 + x9*x9
            acc[p][0] += 1
            acc[p][1] = min(acc[p][1], q)
        B[m] = [tuple(acc[0]), tuple(acc[1])]

        acc = [[0, INF], [0, INF]]
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                p = (x8 + x10) & 1
                q = x6*x6 + x8*x8 + x10*x10
                acc[p][0] += 1
                acc[p][1] = min(acc[p][1], q)
        C[m] = [tuple(acc[0]), tuple(acc[1])]

        acc = [[0, INF], [0, INF]]
        for x10 in range(m + 1):
            x6 = m - x10
            p = x10 & 1
            q = x6*x6 + x10*x10
            acc[p][0] += 1
            acc[p][1] = min(acc[p][1], q)
        D[m] = [tuple(acc[0]), tuple(acc[1])]

    # Unequal branch x0<x1. R[p][gb][gc] aggregates the residual
    # (x5,x9) and (x6,x8,x10) pieces with total parity p.
    R = [[[[0, INF] for _ in range(H + 1)] for __ in range(H + 1)] for ___ in range(2)]
    for gb in range(H + 1):
        for gc in range(H + 1):
            for pb in (0, 1):
                cb, qb = B[gb][pb]
                if not cb:
                    continue
                for pc in (0, 1):
                    cc, qc = C[gc][pc]
                    if not cc:
                        continue
                    dst = R[pb ^ pc][gb][gc]
                    dst[0] += cb * cc
                    dst[1] = min(dst[1], qb + qc)

    count = [[0] * (H + 1) for _ in range(H + 1)]
    minq = [[INF] * (H + 1) for _ in range(H + 1)]

    for b in range(H + 1):
        for c in range(H + 1):
            ct = 0
            qm = INF
            for x1 in range(1, b + 1):
                gb = b - x1
                for x0 in range(min(c, x1 - 1) + 1):
                    rc, rq = R[x1 & 1][gb][c - x0]
                    if not rc:
                        continue
                    ct += rc
                    qm = min(qm, x0*x0 + x1*x1 + rq)
            count[b][c] += ct
            minq[b][c] = min(minq[b][c], qm)

    # Equal branch x0=x1=t. Dcap handles the diagonal lex condition x6<=x9.
    Dcap = [[[[0, INF] for _ in range(2)] for __ in range(H + 1)] for ___ in range(H + 1)]
    for r in range(H + 1):
        acc = [[0, INF], [0, INF]]
        for cap in range(H + 1):
            if cap <= r:
                x6 = cap
                x10 = r - cap
                p = x10 & 1
                q = x6*x6 + x10*x10
                acc[p][0] += 1
                acc[p][1] = min(acc[p][1], q)
            Dcap[r][cap][0] = list(acc[0])
            Dcap[r][cap][1] = list(acc[1])

    # E[p][bs][cs] aggregates x5,x9,x8,x6,x10 subject to
    # (x5,x6)<=lex(x8,x9), with p=x8+x9+x10 mod2.
    E = [[[[0, INF] for _ in range(H + 1)] for __ in range(H + 1)] for ___ in range(2)]

    # Strict first-coordinate branch x5<x8.
    for x5 in range(H + 1):
        for x8 in range(x5 + 1, H + 1):
            for x9 in range(H - x5 + 1):
                bs = x5 + x9
                for r in range(H - x8 + 1):
                    cs = x8 + r
                    for p10 in (0, 1):
                        dc, dq = D[r][p10]
                        if not dc:
                            continue
                        p = (x8 + x9 + p10) & 1
                        dst = E[p][bs][cs]
                        dst[0] += dc
                        dst[1] = min(dst[1], x5*x5 + x8*x8 + x9*x9 + dq)

    # Diagonal first-coordinate branch x5=x8=u, then x6<=x9.
    for u in range(H + 1):
        for x9 in range(H - u + 1):
            bs = u + x9
            for r in range(H - u + 1):
                cs = u + r
                for p10 in (0, 1):
                    dc, dq = Dcap[r][x9][p10]
                    if not dc:
                        continue
                    p = (u + x9 + p10) & 1
                    dst = E[p][bs][cs]
                    dst[0] += dc
                    dst[1] = min(dst[1], 2*u*u + x9*x9 + dq)

    for b in range(H + 1):
        for c in range(H + 1):
            for t in range(min(b, c) + 1):
                ec, eq = E[t & 1][b - t][c - t]
                if not ec:
                    continue
                count[b][c] += ec
                minq[b][c] = min(minq[b][c], 2*t*t + eq)

    return count, minq


def crosscheck_h16_exact(sources: dict[str, bytes], count, minq) -> None:
    path = ROOT / LOCKS["bounded_bc_verifier"][0]
    base = load_module("td02_bc_exact_crosscheck", path, sources["bounded_bc_verifier"])
    exact = base.build_bc_q()
    for b in range(17):
        for c in range(17):
            ec = 0
            eq = INF
            for support_hist in exact[b][c]:
                ec += sum(support_hist.values())
                if support_hist:
                    eq = min(eq, min(support_hist))
            req(count[b][c] == ec, f"H16 BC count mismatch {(b,c,count[b][c],ec)}")
            if ec:
                req(minq[b][c] == eq, f"H16 BC qmin mismatch {(b,c,minq[b][c],eq)}")
            else:
                req(minq[b][c] == INF, f"H16 empty BC qmin mismatch {(b,c)}")


def crosscheck_compressed_family(sources: dict[str, bytes], count) -> None:
    path = ROOT / LOCKS["compressed_family"][0]
    fam = load_module("td02_compressed_family", path, sources["compressed_family"])
    table = fam.build_exceptional_count_table(HMAX)

    mass = [0] * (HMAX + 1)
    for a in range(HMAX + 1):
        ac = math.comb(a + 2, 2)
        for b in range(HMAX - a + 1):
            for c in range(HMAX - a - b + 1):
                mass[a + b + c] += ac * count[b][c]

    cumulative = 0
    for e in range(HMAX + 1):
        cumulative += mass[e]
        req(cumulative == table.count(e), f"compressed-family count mismatch e={e}")


def td02_x4_survivors(*, d: int, g: int, b: int, c: int, qmin: int) -> tuple[int, int]:
    # Any actual cell member has q>=qmin and t in the source-locked canonical
    # parity interval. Enlarging to q=qmin and every t in that parity interval
    # can only enlarge the GRF04 survivor set, hence yields an upper bound.
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*qmin
    if rem < 0:
        return 0, -1
    r = math.isqrt(rem // 4)
    tlo, thi = canonical_t_bounds(b, c)
    if thi < tlo:
        return 0, -1
    delta = (d//2 - c) & 1
    r_eff = r if (r & 1) == delta else r - 1
    if r_eff < 0:
        return 0, -1
    D0 = d // 2
    lo = max(0, ceil_div(D0 - thi - r_eff, 2))
    raw_hi = (D0 - tlo + r_eff) // 2
    return max(0, raw_hi - lo + 1), raw_hi


def row_census(*, g: int, d: int, count, minq) -> tuple[int, int]:
    h = d // 2
    legacy = 8 if g == 0 else 4
    K = ceil_div(d - 16*g + 16, 4)
    panel = survivor = 0

    for b in range(h + 1):
        for c in range(h + 1):
            bcc = count[b][c]
            if not bcc or component3(d, b, c) < 0:
                continue
            for a in range(h + 1):
                if component_a(d, a) < 0:
                    continue
                M = a + b + c

                # Actual support is bounded above by this cellwise maximum.
                # Replacing actual support by smax in the HPADJ08 e-lower
                # condition lowers/equalizes the lower endpoint. Dropping the
                # qneed/srem feasibility test and exact singleton exclusions
                # further enlarges the panel. Thus this is a superset count.
                smax = min(3, a) + min(3, b) + min(4, c)
                lower = max(
                    legacy,
                    K,
                    d - 4*g + 4,
                    M,
                    M + max(0, K - smax),
                )
                upper = min((19*d)//5, 3*d, 3*d - (b-c))
                ne, se, _elo, ehi = even_interval_count_sum(lower, upper)
                if ne == 0:
                    continue

                normal_sum = ne * (19*d + 1) - 5 * se
                configs = math.comb(a + 2, 2) * bcc
                panel += configs * normal_sum

                q = qmin3(a) + minq[b][c]
                sx4, raw_hi = td02_x4_survivors(d=d, g=g, b=b, c=c, qmin=q)
                if raw_hi >= 0:
                    # Since upper<=3d, every retained normal budget n=19d-5e
                    # is >=4d. Also the GRF04 radius is <=2d for d>=8, so the
                    # raw x4 upper endpoint is <=5d/4<4d: n clipping is inactive.
                    req(ehi <= 3*d, f"e upper regression {(g,d,a,b,c,ehi)}")
                    min_n = 19*d - 5*ehi
                    req(min_n >= 4*d, f"normal lower regression {(g,d,a,b,c,min_n)}")
                    req(raw_hi <= min_n, f"x4 clipping regression {(g,d,a,b,c,raw_hi,min_n)}")
                survivor += configs * ne * sx4

    return panel, survivor


def run_domain(rows: list[tuple[int, int]], count, minq):
    out = []
    panel = survivor = 0
    for g, d in rows:
        rp, rs = row_census(g=g, d=d, count=count, minq=minq)
        out.append({
            "row_id": f"g{g}-d{d:03d}",
            "g": g,
            "d": d,
            "relaxed_panel_terminals": rp,
            "td02_survivor_upper_bound": rs,
        })
        panel += rp
        survivor += rs
    stream = hashlib.sha256()
    for row in out:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return out, panel, survivor, stream.hexdigest()


def main() -> None:
    sources = verified_sources()

    prefix = json.loads(sources["prefix_checkpoint"])
    req(prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] == EXPECTED_LABELS,
        "FULL178 assignment order")

    contract = json.loads(sources["full178_contract"])
    cov = contract["coverage"]
    req(cov["rows_total"] == EXPECTED_ROWS and cov["hmax"] == HMAX, "FULL178 contract coverage")
    req(contract["mathematical_refinement"]["e_interval_and_exclusions_unchanged"] is True,
        "HPADJ08 e-semantics contract")
    req(contract["source_locks"]["hpadj08_worker_blob_sha1"] ==
        "c5fc340ea734dfc54436f124bb302c1ec6c5677c",
        "HPADJ08 FULL178 worker lock")

    probe = json.loads(sources["hperp_probe"])
    req(probe["labels_1based"] == EXPECTED_LABELS, "Hperp probe labels")
    req(probe["a_rank"] == 11 and probe["s_positive_definite"] is True and probe["s_determinant"] == "3072",
        "concrete GRF04 Schur probe")

    correction = json.loads(sources["corrected_adjunction"])["corrected_general_type_adjunction"]
    req(correction["g0_exact_exceptional_square_necessary_condition"] ==
        "8*sum(y_i^2)<=d^2+16*d+32", "g0 adjunction")
    req(correction["g1_exact_exceptional_square_necessary_condition"] ==
        "8*sum(y_i^2)<=d^2+16*d", "g1 adjunction")

    hpadj = json.loads(sources["hpadj08_v29"])
    href = hpadj["accounting"]["post_transition_certified_remaining_terminals_upper_bound"]
    req(href == REFERENCE_HPADJ08_UPPER, "HPADJ08 V29 reference bound")
    req(hpadj["accounting"]["composition_rule"] ==
        "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "HPADJ08 composition semantics")

    manifest = json.loads(sources["full178_manifest"])
    manifest_ids = {row_id for group in manifest["m_class_rows"].values() for row_id in group}
    expected_rows = [(0, d) for d in range(8, 177, 2)] + [(1, d) for d in range(8, 193, 2)]
    expected_ids = {f"g{g}-d{d:03d}" for g, d in expected_rows}
    req(manifest["residual_row_count"] == EXPECTED_ROWS and manifest_ids == expected_ids,
        "FULL178 manifest row domain")

    count, minq = build_bc_count_minq(HMAX)
    # Rebuild H=16 independently and compare every (b,c) cell with the exact
    # support/q histogram used by the bounded TD02 verifier.
    count16, minq16 = build_bc_count_minq(16)
    crosscheck_h16_exact(sources, count16, minq16)
    # Exact combinatorial identity against the production symbolic counter for
    # every exceptional cap e<=96.
    crosscheck_compressed_family(sources, count)

    bounded_rows = [(0, d) for d in range(8, 33, 2)] + [(1, d) for d in range(8, 33, 2)]
    _brows, bpanel, bsurvivor, _bsha = run_domain(bounded_rows, count, minq)
    req(bpanel == EXPECTED_BOUNDED_RELAXED_PANEL, f"bounded relaxed panel drift {bpanel}")
    req(bsurvivor == EXPECTED_BOUNDED_SURVIVOR_UPPER, f"bounded survivor drift {bsurvivor}")
    req(bsurvivor >= PRIOR_BOUNDED_CANONICAL_SURVIVORS,
        "relaxed bounded upper fell below exact canonical bounded survivors")

    rows, panel, survivor, row_sha = run_domain(expected_rows, count, minq)
    req(len(rows) == EXPECTED_ROWS, "row count")
    req(panel == EXPECTED_RELAXED_PANEL, f"FULL178 relaxed panel drift {panel}")
    req(survivor == EXPECTED_SURVIVOR_UPPER, f"FULL178 survivor upper drift {survivor}")
    req(row_sha == EXPECTED_ROW_STREAM_SHA256, f"row stream drift {row_sha}")
    req(survivor < href, "TD02 does not strictly tighten HPADJ08 reference upper bound")

    result = {
        "schema": "STAGE32_32_01_178_TD02_GRF04_FULL178_AGGREGATE_UPPER_V1",
        "domain": {
            "rows": EXPECTED_ROWS,
            "g0_d_even": [8, 176],
            "g1_d_even": [8, 192],
            "hmax": HMAX,
        },
        "semantics": {
            "bound_type": "INDEPENDENT_CERTIFIED_SURVIVOR_UPPER_BOUND_CANDIDATE",
            "panel": "SAFE_SUPERSET_OF_FULL178_HPADJ08_COUNTING_DOMAIN",
            "aggregation": "EXACT_CELL_COUNT_PLUS_EXACT_CELL_QMIN__NO_TERMINAL_ENUMERATION",
            "t": "SOURCE_LOCKED_CANONICAL_PARITY_INTERVAL_ENVELOPE",
            "support_relaxation":
                "replace actual support by cellwise support upper bound; drop support-cap infeasibility and exact e exclusions",
            "composition": "MIN_ONLY__NO_ADDITIVE_STACKING__NO_EXACT_RESIDUAL_SET_CLAIM",
        },
        "relaxed_panel_terminals": panel,
        "td02_independent_survivor_upper_bound": survivor,
        "reference_hpadj08_v29_upper_bound": href,
        "numeric_upper_bound_tightening_vs_hpadj08_reference": href - survivor,
        "bounded_regression": {
            "relaxed_panel_terminals": bpanel,
            "relaxed_survivor_upper_bound": bsurvivor,
            "prior_exact_canonical_survivors": PRIOR_BOUNDED_CANONICAL_SURVIVORS,
        },
        "crosschecks": {
            "h16_exact_bc_count_and_qmin_all_cells": True,
            "production_compressed_exceptional_counts_e_0_through_96": True,
            "concrete_schur_rank": 11,
            "concrete_schur_determinant": "3072",
        },
        "external_hpadj08_source_lock": {
            "producer_pr": 1812,
            "audited_exact_head": "36eab50192cf80ec5ed48aba40f4a56076759fea",
            "full178_result_blob_sha1": "f9a01c3e673dc630a3446ac4560c72c4f76db812",
            "full178_worker_blob_sha1": "c5fc340ea734dfc54436f124bb302c1ec6c5677c",
        },
        "row_stream_sha256": row_sha,
        "rows": rows,
        "source_blobs": {name: sha for name, (_rel, sha) in LOCKS.items()},
        "credit": {
            "main": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "stage32_closed": False,
            "perfect_cuboid_existence": False,
            "perfect_cuboid_nonexistence": False,
            "merge": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    out = HERE / "TD02-GRF04-FULL178-AGGREGATE-RESULT.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "relaxed_panel_terminals": panel,
        "td02_independent_survivor_upper_bound": survivor,
        "reference_hpadj08_v29_upper_bound": href,
        "numeric_upper_bound_tightening_vs_hpadj08_reference": href - survivor,
        "row_stream_sha256": row_sha,
        "canonical_sha256_without_this_field": result["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
