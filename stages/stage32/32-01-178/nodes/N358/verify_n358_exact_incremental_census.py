#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

LOCKS = {
    ROOT / "stages/stage32/32-01-178/nodes/N358/JOINT_TRANSPORT_SUPPORT_SATURATION_CONTRACT.md": "a9a6836dc201feefd37bebb2f6c0ef42e8faaee4",
    ROOT / "stages/stage32/32-01-178/nodes/N358/verify_n358_joint_transport_support_saturation.py": "63666cdb0f3d14676f0ab5dac561501279e8c2a0",
    ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json": "50014d453266ad79101910a943d14388bd3ef6ec",
    ROOT / "stages/stage32/32-01-178/nodes/N357/HOSTILE-AUDIT-PASS.json": "e9f93fb1b2bfeb68b72598632522d164fee715c6",
    ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json": "0a46b34e278688240656b4977e9cb7f589e90e06",
}

EXPECTED_N357_REVIEW = 5183069892
EXPECTED_N357_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
EXPECTED_N357_REMAIN = 47_598_978_285_064_933_810_198
EXPECTED_STRUCTURAL_STRATA = 17_128
EXPECTED_AFFECTED_STRATA = 2_540
EXPECTED_AFFECTED_ROWS = 76
EXPECTED_REJECTED_EXCEPTIONAL = 11_344_256_366_314_850
EXPECTED_REJECTED_TERMINALS = 9_274_971_107_798_843_958
EXPECTED_REMAINING = 47_589_703_313_957_134_966_240
EXPECTED_STREAM = "206538209460c6b7b9cb3cc33e601a2cbf75fa084f9693af379e660ed6cf9625"
EXPECTED_N357_WITNESS = 49_030_556_814_634
HMAX = 96


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def triple_free_count(mass: int, support: int) -> int:
    if mass == 0:
        return int(support == 0)
    if support <= 0 or support > 3 or support > mass:
        return 0
    return math.comb(3, support) * math.comb(mass - 1, support - 1)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def build_pair_triple(H: int):
    B = [[[0, 0] for _ in range(3)] for __ in range(H + 1)]
    C = [[[0, 0] for _ in range(4)] for __ in range(H + 1)]
    for g in range(H + 1):
        for x9 in range(g + 1):
            x5 = g - x9
            B[g][int(x5 > 0) + int(x9 > 0)][x9 & 1] += 1
        for x8 in range(g + 1):
            for x10 in range(g - x8 + 1):
                x6 = g - x8 - x10
                C[g][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1] += 1
    D = [[[[0] * 6 for _ in range(H + 1)] for __ in range(H + 1)] for ___ in range(2)]
    for req in (0, 1):
        for g2 in range(H + 1):
            for g3 in range(H + 1):
                dst = D[req][g2][g3]
                for sb in range(3):
                    for pb in (0, 1):
                        bv = B[g2][sb][pb]
                        if not bv:
                            continue
                        for sc in range(4):
                            cv = C[g3][sc][pb ^ req]
                            if cv:
                                dst[sb + sc] += bv * cv
    return D


def build_lex_exact(H: int):
    L = [[[[0, 0] for _ in range(6)] for __ in range(H + 1)] for ___ in range(H + 1)]
    P = [[[0, 0] for _ in range(3)] for __ in range(H + 1)]
    for q in range(H + 1):
        for x10 in range(q + 1):
            x6 = q - x10
            P[q][int(x6 > 0) + int(x10 > 0)][x10 & 1] += 1
    for x5 in range(H + 1):
        s5 = int(x5 > 0)
        for x8 in range(x5 + 1, H + 1):
            for x9 in range(H - x5 + 1):
                g2 = x5 + x9
                s0 = s5 + 1 + int(x9 > 0)
                p0 = (x8 + x9) & 1
                for q in range(H - x8 + 1):
                    g3 = x8 + q
                    for sq in range(3):
                        v0, v1 = P[q][sq]
                        if v0:
                            L[g2][g3][s0 + sq][p0] += v0
                        if v1:
                            L[g2][g3][s0 + sq][p0 ^ 1] += v1
    for t in range(H + 1):
        st = 2 * int(t > 0)
        cap = H - t
        for x6 in range(cap + 1):
            for x9 in range(x6, cap + 1):
                g2 = t + x9
                base = st + int(x6 > 0) + int(x9 > 0)
                p0 = (t + x9) & 1
                for x10 in range(cap - x6 + 1):
                    g3 = t + x6 + x10
                    L[g2][g3][base + int(x10 > 0)][p0 ^ (x10 & 1)] += 1
    return L


def build_bc_exact(H: int):
    D = build_pair_triple(H)
    L = build_lex_exact(H)
    BC = [[[0] * 8 for _ in range(H + 1)] for __ in range(H + 1)]
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            req = x1 & 1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    src = D[req][g2][g3]
                    dst = BC[b][c]
                    for s, value in enumerate(src):
                        if value:
                            dst[s + extra] += value
    for t in range(H + 1):
        extra = 2 * int(t > 0)
        parity = t & 1
        cap = H - t
        for g2 in range(cap + 1):
            b = t + g2
            for g3 in range(cap + 1):
                c = t + g3
                dst = BC[b][c]
                src = L[g2][g3]
                for s in range(6):
                    value = src[s][parity]
                    if value:
                        dst[s + extra] += value
    return BC


def n357_count_witness(BC) -> int:
    g, d, e = 0, 100, 200
    h = d // 2
    K = ceil_div(d - 16 * g + 16, 4)
    T = 3 * d - e
    total = 0
    for b in range(h + 1):
        for c in range(h + 1):
            if b - c > T:
                continue
            for a in range(h + 1):
                srem = min(16, d) + component_a(d, a) + component3(d, b, c)
                omitted = e - a - b - c
                if omitted < 0:
                    continue
                for sbc, bc_count in enumerate(BC[b][c]):
                    if not bc_count:
                        continue
                    for sa in range(4):
                        ac = triple_free_count(a, sa)
                        if ac and sbc + sa + min(srem, omitted) >= K:
                            total += bc_count * ac
    return total


def n358_incremental_exceptional(BC, g: int, d: int, e: int) -> int:
    h = d // 2
    T = 3 * d - e
    if T < 0 or T > h - 5:
        return 0
    K = ceil_div(d - 16 * g + 16, 4)
    S0 = min(16, d)
    total = 0
    for b in range(T, h - 4):
        c = b - T
        for a in range(h + 1):
            srem = S0 + component_a(d, a) + 9
            required_stored_support = K - srem
            if required_stored_support < 0 or required_stored_support > 10:
                continue
            if a + b + c > e - srem:
                continue
            for sa in range(4):
                sbc = required_stored_support - sa
                if 0 <= sbc < 8:
                    ac = triple_free_count(a, sa)
                    if ac:
                        total += BC[b][c][sbc] * ac
    return total


def main() -> None:
    for path, expected in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual} != {expected}")
    receipt = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N357/HOSTILE-AUDIT-PASS.json").read_text())
    result357 = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json").read_text())
    if receipt.get("status") != "PASS" or receipt.get("review_id") != EXPECTED_N357_REVIEW:
        raise ValueError("N357 hostile-audit authority regression")
    if receipt["consumed_counts"]["remaining_terminals"] != EXPECTED_N357_REMAIN:
        raise ValueError("N357 retained frontier regression")
    if result357.get("canonical_sha256_without_this_field") != EXPECTED_N357_CANONICAL:
        raise ValueError("N357 RESULT canonical regression")

    manifest = json.loads((ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json").read_text())
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 population regression")
    parsed = []
    for row_id in rows:
        g = int(row_id[1])
        d = int(row_id.split("-d", 1)[1])
        parsed.append((g, d))
    if max(d // 2 for _, d in parsed) != HMAX or not all(d % 2 == 0 for _, d in parsed):
        raise ValueError("FULL178 degree domain regression")

    BC = build_bc_exact(HMAX)
    witness = n357_count_witness(BC)
    if witness != EXPECTED_N357_WITNESS:
        raise ValueError(f"N357 witness semantic replay regression: {witness}")

    records = []
    structural = 0
    affected_rows = set()
    total_exc = 0
    total_term = 0
    for g, d in parsed:
        h = d // 2
        legacy_emin = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        for e in range(max(legacy_emin, K), (19 * d) // 5 + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * ceil_div(e, 6):
                continue
            structural += 1
            exc = n358_incremental_exceptional(BC, g, d, e)
            if not exc:
                continue
            normal = 19 * d - 5 * e + 1
            term = exc * normal
            records.append({
                "g": g, "d": d, "e": e,
                "n358_incremental_rejected_exceptional_prefixes": exc,
                "normal_block": normal,
                "n358_incremental_rejected_terminals": term,
            })
            affected_rows.add((g, d))
            total_exc += exc
            total_term += term

    if structural != EXPECTED_STRUCTURAL_STRATA:
        raise ValueError(f"structural stratum regression: {structural}")
    if len(records) != EXPECTED_AFFECTED_STRATA or len(affected_rows) != EXPECTED_AFFECTED_ROWS:
        raise ValueError("N358 affected-domain regression")
    if total_exc != EXPECTED_REJECTED_EXCEPTIONAL or total_term != EXPECTED_REJECTED_TERMINALS:
        raise ValueError("N358 exact incremental count regression")
    if EXPECTED_N357_REMAIN - total_term != EXPECTED_REMAINING:
        raise ValueError("N358 partition identity regression")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    if stream.hexdigest() != EXPECTED_STREAM:
        raise ValueError("N358 affected-record stream regression")

    # Every affected stratum keeps an explicit N357 survivor outside N358 scope:
    # all ten stored coordinates equal 1 -> (a,b,c)=(3,3,4), M=s=10 and b<c.
    for rec in records:
        g, d, e = rec["g"], rec["d"], rec["e"]
        K = ceil_div(d - 16 * g + 16, 4)
        T = 3 * d - e
        a, b, c, M, s = 3, 3, 4, 10, 10
        srem = min(16, d) + component_a(d, a) + component3(d, b, c)
        if not (b < c and b - c <= T and max(a, b, c) <= d // 2 and s + min(e - M, srem) >= K):
            raise ValueError(f"retained-stratum witness regression {(g,d,e)}")

    print(json.dumps({
        "verdict": "PASS_N358_EXACT_INCREMENTAL_CENSUS_AUDIT_CANDIDATE",
        "structural_strata": structural,
        "affected_strata": len(records),
        "affected_rows": len(affected_rows),
        "incremental_rejected_exceptional_prefixes": total_exc,
        "incremental_rejected_terminals": total_term,
        "candidate_remaining_strata": EXPECTED_STRUCTURAL_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING,
        "affected_record_stream_sha256": stream.hexdigest(),
        "n357_witness_semantic_replay": witness,
        "n358_main_pruning_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
