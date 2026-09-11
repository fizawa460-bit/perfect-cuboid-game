#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N220 = HERE.parent / "N220"
sys.path.insert(0, str(N220))
import verify_n220_exact_symbolic_count as base
import verify_n220_exact_symbolic_count_fast as fast

MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
N355_RECEIPT = HERE / "HOSTILE-AUDIT-PASS.json"
N355_X1 = HERE / "verify_n355_x1_diagonal_lower_bound.py"

EXPECTED_N220_BLOB = "5855ae0835a828ab56b7a6e93a42f6788b6f676a"
EXPECTED_N355_RECEIPT_BLOB = "2f89b467d5dab8865b4ac52b0c03333f2a903b8f"
EXPECTED_N355_REVIEW = 5165493296
EXPECTED_N355_HEAD = "a13a39ba5ec0a281fcd65601f9f75d41405b1da1"
EXPECTED_N355_X1_BLOB = "ac281268032d06ab4687922395bb16543552beaf"
N354_STRATA = 17128
N354_TERMINALS = 38560956534397137634780102
AUDITED_X1_REJECT = 8211103970847375998477971
AUDITED_X1_REMAIN = 30349852563549761636302131


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def add_state(dst, mass: int, support: int, value: int) -> None:
    if value:
        dst[mass][support] += value


def pair2_distribution(H: int):
    # x5 + x9 = g2; parity is x9 mod 2.
    out = [[[0, 0] for _ in range(3)] for __ in range(H + 1)]
    for g in range(H + 1):
        for x9 in range(g + 1):
            x5 = g - x9
            s = int(x5 > 0) + int(x9 > 0)
            out[g][s][x9 & 1] += 1
    return out


def triple3_distribution(H: int):
    # x6 + x8 + x10 = g3; parity is x8+x10 mod 2.
    out = [[[0, 0] for _ in range(4)] for __ in range(H + 1)]
    for g in range(H + 1):
        for x8 in range(g + 1):
            for x10 in range(g - x8 + 1):
                x6 = g - x8 - x10
                s = int(x6 > 0) + int(x8 > 0) + int(x10 > 0)
                out[g][s][(x8 + x10) & 1] += 1
    return out


def build_bc_prefix(H: int):
    """Prefix in g2 along each fixed r=g2+g3 for the unequal branch."""
    B = pair2_distribution(H)
    C = triple3_distribution(H)
    pref = []
    for r in range(2 * H + 1):
        row = []
        running = [[0, 0] for _ in range(6)]
        for b in range(H + 1):
            c = r - b
            if 0 <= c <= H:
                for sb in range(3):
                    for pb in (0, 1):
                        vb = B[b][sb][pb]
                        if not vb:
                            continue
                        for sc in range(4):
                            for pc in (0, 1):
                                vc = C[c][sc][pc]
                                if vc:
                                    running[sb + sc][pb ^ pc] += vb * vc
            row.append(tuple((v[0], v[1]) for v in running))
        pref.append(row)
    return pref


def pair_x6_x10_exact(q: int):
    out = [[0, 0] for _ in range(3)]
    for x10 in range(q + 1):
        x6 = q - x10
        s = int(x6 > 0) + int(x10 > 0)
        out[s][x10 & 1] += 1
    return out


def build_lex_prefix(H: int):
    """Exact/prefix distribution for lex (x5,x6)<=(x8,x9).

    Coordinates are indexed by g2=x5+x9 and g3=x6+x8+x10.  Parity is
    x8+x9+x10 mod 2.  A rectangular cap g2,g3<=c can therefore be queried
    along each r=g2+g3 by one interval subtraction.
    """
    exact = [[[[0, 0] for _ in range(6)] for __ in range(H + 1)] for ___ in range(H + 1)]
    pair_cache = [pair_x6_x10_exact(q) for q in range(H + 1)]

    # Strict first-coordinate lex branch: x5 < x8; x6,x9 are then unrestricted.
    for x5 in range(H + 1):
        s5 = int(x5 > 0)
        for x8 in range(x5 + 1, H + 1):
            base_support = s5 + 1
            for x9 in range(H - x5 + 1):
                g2 = x5 + x9
                s0 = base_support + int(x9 > 0)
                p0 = (x8 + x9) & 1
                for q in range(H - x8 + 1):
                    g3 = x8 + q
                    pq = pair_cache[q]
                    for sq in range(3):
                        v0, v1 = pq[sq]
                        if v0:
                            exact[g2][g3][s0 + sq][p0] += v0
                        if v1:
                            exact[g2][g3][s0 + sq][p0 ^ 1] += v1

    # Equal first coordinate: x5=x8=t, so lex reduces to x6<=x9.
    for t in range(H + 1):
        st = 2 * int(t > 0)
        L = H - t
        for x6 in range(L + 1):
            for x9 in range(x6, L + 1):
                g2 = t + x9
                base_support = st + int(x6 > 0) + int(x9 > 0)
                p0 = (t + x9) & 1
                for x10 in range(L - x6 + 1):
                    g3 = t + x6 + x10
                    exact[g2][g3][base_support + int(x10 > 0)][p0 ^ (x10 & 1)] += 1

    pref = []
    for r in range(2 * H + 1):
        row = []
        running = [[0, 0] for _ in range(6)]
        for g2 in range(H + 1):
            g3 = r - g2
            if 0 <= g3 <= H:
                cell = exact[g2][g3]
                for s in range(6):
                    running[s][0] += cell[s][0]
                    running[s][1] += cell[s][1]
            row.append(tuple((v[0], v[1]) for v in running))
        pref.append(row)
    return pref


def interval_query(pref, r: int, lo: int, hi: int, support: int, parity: int) -> int:
    if lo > hi:
        return 0
    v = pref[r][hi][support][parity]
    if lo:
        v -= pref[r][lo - 1][support][parity]
    return v


def triple_free_count(mass: int, support: int) -> int:
    if mass == 0:
        return int(support == 0)
    if support <= 0 or support > 3 or support > mass:
        return 0
    return math.comb(3, support) * math.comb(mass - 1, support - 1)


def build_capped_exact(h: int, bc_pref, lex_pref):
    """Count base terminal exceptional prefixes by exact mass/support under full N355 block caps."""
    h = int(h)
    mid = [[0] * 8 for _ in range(2 * h + 1)]

    # x0<x1.  g2 residual cap is h-x1; g3 residual cap is h-x0.
    for x0 in range(h + 1):
        for x1 in range(x0 + 1, h + 1):
            c2 = h - x1
            c3 = h - x0
            m0 = x0 + x1
            s0 = 1 + int(x0 > 0)
            parity = x1 & 1
            for r in range(c2 + c3 + 1):
                lo = max(0, r - c3)
                hi = min(c2, r)
                for s in range(6):
                    v = interval_query(bc_pref, r, lo, hi, s, parity)
                    if v:
                        mid[m0 + r][s0 + s] += v

    # x0=x1=a.  Both residual block caps are c=h-a and lex is active.
    for a in range(h + 1):
        c = h - a
        m0 = 2 * a
        s0 = 0 if a == 0 else 2
        parity = a & 1
        for r in range(2 * c + 1):
            lo = max(0, r - c)
            hi = min(c, r)
            for s in range(6):
                v = interval_query(lex_pref, r, lo, hi, s, parity)
                if v:
                    mid[m0 + r][s0 + s] += v

    # Independent known block {101,102,103} = (x7,x3,x2), exact sum <=h.
    out = [[0] * 11 for _ in range(3 * h + 1)]
    for m0, row in enumerate(mid):
        for s0, left in enumerate(row):
            if not left:
                continue
            for q in range(h + 1):
                for sq in range(4):
                    right = triple_free_count(q, sq)
                    if right:
                        out[m0 + q][s0 + sq] += left * right
    return out


def brute_small(h: int):
    out = [[0] * 11 for _ in range(3 * h + 1)]
    # exceptional tuple order x0,x1,x2,x3,x5,x6,x7,x8,x9,x10
    for v in itertools.product(range(h + 1), repeat=10):
        x0,x1,x2,x3,x5,x6,x7,x8,x9,x10 = v
        if x0 > x1:
            continue
        if x0 == x1 and (x5,x6) > (x8,x9):
            continue
        if (x1+x8+x9+x10) & 1:
            continue
        if x2+x3+x7 > h:
            continue
        if x1+x5+x9 > h:
            continue
        if x0+x6+x8+x10 > h:
            continue
        m = sum(v)
        s = sum(int(x > 0) for x in v)
        out[m][s] += 1
    return out


def n220_accept_from_exact(exact, *, e: int, required: int) -> int:
    total = 0
    for mass, row in enumerate(exact):
        if mass > e:
            break
        extra = min(38, e - mass)
        for support, count in enumerate(row):
            if count and support + extra >= required:
                total += count
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    if git_blob_sha1(Path(base.__file__)) != EXPECTED_N220_BLOB:
        raise ValueError("N220 verifier source-lock regression")
    if git_blob_sha1(N355_RECEIPT) != EXPECTED_N355_RECEIPT_BLOB:
        raise ValueError("N355 audit receipt source-lock regression")
    if git_blob_sha1(N355_X1) != EXPECTED_N355_X1_BLOB:
        raise ValueError("N355 x1 verifier source-lock regression")

    receipt = json.loads(N355_RECEIPT.read_text())
    if receipt["status"] != "PASS" or receipt["review_id"] != EXPECTED_N355_REVIEW:
        raise ValueError("N355 audit PASS regression")
    if receipt["audited_exact_head"] != EXPECTED_N355_HEAD:
        raise ValueError("N355 audited exact-head regression")
    if receipt["consumed_counts"]["remaining_terminals"] != AUDITED_X1_REMAIN:
        raise ValueError("N355 audited residual regression")

    manifest = base.load_canonical(MANIFEST, base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")
    parsed = [base.parse_row_id(row_id) for row_id in rows]
    H = max(d // 2 for _, d in parsed)

    bc_pref = build_bc_prefix(H)
    lex_pref = build_lex_prefix(H)

    # Independent small-domain hostile check of the full DP construction.
    for h in (0, 1, 2):
        if build_capped_exact(h, bc_pref, lex_pref) != brute_small(h):
            raise ValueError(f"full-prefix capped DP brute regression h={h}")

    total_exact = base.build_exceptional_exact_mass_support()
    support_lt = fast.build_support_lt(total_exact)
    cumulative = []
    running = 0
    for e in range(base.MAX_E + 1):
        running += sum(total_exact[e])
        cumulative.append(running)

    x1mod = load_module(N355_X1, "s32_n355_x1_reuse")
    x1_table = x1mod.build_suffix_capacity_table()
    capped_cache = {}
    records = []
    full_reject_terminals = 0
    incremental_reject_terminals = 0
    remaining_terminals = 0
    remaining_strata = 0
    n354_terminals_replayed = 0
    x1_terminals_replayed = 0
    full_affected_strata = 0
    incremental_affected_strata = 0

    for row_id in rows:
        g, d = base.parse_row_id(row_id)
        h = d // 2
        if h not in capped_cache:
            capped_cache[h] = build_capped_exact(h, bc_pref, lex_pref)
        capped = capped_cache[h]
        legacy_emin = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * ceil_div(e, 6):
                continue

            n220_exceptional = cumulative[e] - fast.rejected_fast(total_exact, support_lt, e=e, required=K)
            valid_exceptional = n220_accept_from_exact(capped, e=e, required=K)
            if not 0 <= valid_exceptional <= n220_exceptional:
                raise ValueError(f"capped count outside N220 population {(g,d,e)}")
            full_reject_exceptional = n220_exceptional - valid_exceptional

            x1_exceptional = x1mod.unequal_x1_gt_half_count(genus=g, degree=d, e=e, table=x1_table)
            if not 0 <= x1_exceptional <= full_reject_exceptional:
                raise ValueError(f"audited x1 subset not contained in full cut {(g,d,e)}")
            incremental_exceptional = full_reject_exceptional - x1_exceptional

            normal_block = 19 * d - 5 * e + 1
            n354_t = n220_exceptional * normal_block
            x1_t = x1_exceptional * normal_block
            full_reject_t = full_reject_exceptional * normal_block
            incremental_t = incremental_exceptional * normal_block
            remain_t = valid_exceptional * normal_block

            n354_terminals_replayed += n354_t
            x1_terminals_replayed += x1_t
            full_reject_terminals += full_reject_t
            incremental_reject_terminals += incremental_t
            remaining_terminals += remain_t
            if full_reject_t:
                full_affected_strata += 1
            if incremental_t:
                incremental_affected_strata += 1
            if remain_t:
                remaining_strata += 1

            records.append({
                "g": g, "d": d, "e": e, "h": h,
                "n354_terminals": n354_t,
                "audited_x1_reject_terminals": x1_t,
                "full_prefix_reject_terminals": full_reject_t,
                "incremental_after_audited_x1_terminals": incremental_t,
                "full_prefix_remaining_terminals": remain_t,
            })

    if len(records) != N354_STRATA:
        raise ValueError(f"N354 survivor strata regression {len(records)}")
    if n354_terminals_replayed != N354_TERMINALS:
        raise ValueError("N354 terminal replay regression")
    if x1_terminals_replayed != AUDITED_X1_REJECT:
        raise ValueError("audited N355 x1 subset replay regression")
    if N354_TERMINALS - full_reject_terminals != remaining_terminals:
        raise ValueError("full-cut partition identity regression")
    if AUDITED_X1_REMAIN - incremental_reject_terminals != remaining_terminals:
        raise ValueError("sequential N355 partition identity regression")
    if incremental_reject_terminals <= 0:
        raise ValueError("full block-sum cut did not strengthen audited x1 subset")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r:(r["g"],r["d"],r["e"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode()+b"\n")

    result = {
        "schema":"STAGE32_32_01_178_N355_FULL_PREFIX_BLOCK_SUM_CENSUS_V1",
        "node_id":"N355",
        "status":"AUDIT_CANDIDATE_FULL_PREFIX_CENSUS_NO_NEW_AUTHORITY_CREDIT",
        "audited_input":{
            "review_id":EXPECTED_N355_REVIEW,
            "audited_exact_head":EXPECTED_N355_HEAD,
            "audited_subset_remaining_strata":N354_STRATA,
            "audited_subset_remaining_terminals":AUDITED_X1_REMAIN,
        },
        "full_prefix_cut":{
            "known_groups":[[101,102,103],[97,98,99],[93,94,95,96]],
            "factor1_and_factor2_known_group_partition_identical":True,
            "equivalent_cut":"max(group1_sum,group2_sum,group3_sum)<=floor(d/2)",
            "source_geometry":"externally hostile-audited N355 special-fibre prefix max cut",
        },
        "aggregate":{
            "n354_survivor_strata_replayed":len(records),
            "n354_terminals_replayed":n354_terminals_replayed,
            "audited_x1_subset_rejected_terminals_replayed":x1_terminals_replayed,
            "full_prefix_affected_strata":full_affected_strata,
            "full_prefix_rejected_terminals_from_n354":full_reject_terminals,
            "incremental_affected_strata_after_audited_x1":incremental_affected_strata,
            "candidate_incremental_rejected_terminals_after_audited_x1":incremental_reject_terminals,
            "candidate_remaining_strata":remaining_strata,
            "candidate_remaining_terminals":remaining_terminals,
            "per_stratum_stream_sha256":stream.hexdigest(),
        },
        "verification":{
            "small_brute_h_0_1_2":True,
            "audited_x1_subset_contained_recordwise":True,
            "n354_partition_identity":True,
            "sequential_partition_identity":True,
            "max_h":H,
        },
        "semantics":{
            "main_incremental_pruning_credit":False,
            "external_hostile_audit_required_for_full_census":True,
            "current_authority_remains_audited_x1_subset":True,
            "n350_producer_registered":False,
            "full178_complete":False,
            "heavy_compute_authorized":False,
            "theorem_credit":False,
            "receiver_credit":False,
            "endpoint_credit":False,
            "stage32_closed":False,
            "perfect_cuboid_existence_claim":False,
            "perfect_cuboid_nonexistence_claim":False,
            "merge_authorized":False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    if args.output:
        args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "verdict":"PASS_N355_FULL_PREFIX_BLOCK_SUM_CENSUS",
        "incremental_rejected_terminals":incremental_reject_terminals,
        "remaining_strata":remaining_strata,
        "remaining_terminals":remaining_terminals,
        "stream":stream.hexdigest(),
        "canonical":result["canonical_sha256_without_this_field"],
        "main_credit":False,
    },sort_keys=True))


if __name__ == "__main__":
    main()
