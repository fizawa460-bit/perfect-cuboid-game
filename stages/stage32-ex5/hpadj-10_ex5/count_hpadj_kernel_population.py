#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
FAMILY = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
HPADJ_SOURCE = ROOT / "stages/stage32/management/hpadj-01/RESULT.json"
KERNEL_RESULT = HERE / "KERNEL-RESULT.json"

LOCKS = {
    "manifest_blob": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "hpadj_source_blob": "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b",
    "hpadj_source_canonical": "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506",
    "kernel_result_blob": "0a073dc9e01e037fa02fdbca5a482ee1ce6ab002",
    "kernel_result_canonical": "c678a84a8bb8aa44db0063ca797dec0e174ff021893ae5e9631ac607f43f1598",
}

EXPECTED = {
    "affected_rows": 178,
    "exceptional_prefix_stratum_instances": 19700993066083231249,
    "charged_terminal_lower_bound": 27104321327305699275487,
    "genus0_terminal_lower_bound": 6263333577918328238904,
    "genus1_terminal_lower_bound": 20840987749387371036583,
    "per_row_stream_sha256": "5852e58fdd570e05c057d5fcaf426f6b25fefb1eaf83ae1329657b42289775ae",
}


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_locked_json(path: Path, blob_sha: str, canonical_sha: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob_sha, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical_sha, f"{label} stored canonical drift")
    req(canon(value) == canonical_sha, f"{label} canonical drift")
    return value


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def triple_free_count(mass: int, support: int) -> int:
    if mass == 0:
        return int(support == 0)
    if support <= 0 or support > 3 or support > mass:
        return 0
    return math.comb(3, support) * math.comb(mass - 1, support - 1)


def component_a(d: int, a: int) -> int:
    return min(13, d - a, d - 2 * a + 4, d // 2 + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def manifest_rows(manifest: dict) -> list[tuple[str, int, int]]:
    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    req(len(rows) == 178 and len(set(rows)) == 178, "FULL178 row partition drift")
    out = []
    for row_id in rows:
        g = int(row_id[1])
        d = int(row_id.split("-d", 1)[1])
        req(g in (0, 1) and d >= 8 and d % 2 == 0, f"row parse drift {row_id}")
        out.append((row_id, g, d))
    return out


def build_pair_triple_parity(H: int):
    # Unequal x0<x1 branch. Preserve x9 parity in addition to the historical
    # (b,c,support) census; under the terminal-family parity relation,
    # r=x0+x8+x10 = x0+x1+x9 (mod 2).
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

    D = [[[[[0, 0] for _ in range(6)] for __ in range(H + 1)] for ___ in range(H + 1)] for ____ in range(2)]
    for x1par in (0, 1):
        for g2 in range(H + 1):
            for g3 in range(H + 1):
                dst = D[x1par][g2][g3]
                for sb in range(3):
                    for x9par in (0, 1):
                        bv = B[g2][sb][x9par]
                        if not bv:
                            continue
                        required_cpar = x9par ^ x1par
                        for sc in range(4):
                            cv = C[g3][sc][required_cpar]
                            if cv:
                                dst[sb + sc][x9par] += bv * cv
    return D


def build_lex_exact_parity(H: int):
    # Equal x0=x1 branch. Preserve terminal parity and r. Under the exact
    # terminal-family parity relation, r=x0+x8+x10 = x9 (mod 2).
    L = [[[[[0, 0] for _ in range(2)] for __ in range(6)] for ___ in range(H + 1)] for ____ in range(H + 1)]
    P = [[[0, 0] for _ in range(3)] for __ in range(H + 1)]
    for q in range(H + 1):
        for x10 in range(q + 1):
            x6 = q - x10
            P[q][int(x6 > 0) + int(x10 > 0)][x10 & 1] += 1

    # Lex-strict first coordinate x5<x8.
    for x5 in range(H + 1):
        s5 = int(x5 > 0)
        for x8 in range(x5 + 1, H + 1):
            for x9 in range(H - x5 + 1):
                g2 = x5 + x9
                s0 = s5 + 1 + int(x9 > 0)
                p0 = (x8 + x9) & 1
                r = x9 & 1
                for q in range(H - x8 + 1):
                    g3 = x8 + q
                    for sq in range(3):
                        v0, v1 = P[q][sq]
                        if v0:
                            L[g2][g3][s0 + sq][p0][r] += v0
                        if v1:
                            L[g2][g3][s0 + sq][p0 ^ 1][r] += v1

    # First coordinates equal x5=x8=t; enforce x6<=x9.
    for t in range(H + 1):
        st = 2 * int(t > 0)
        cap = H - t
        for x6 in range(cap + 1):
            for x9 in range(x6, cap + 1):
                g2 = t + x9
                base = st + int(x6 > 0) + int(x9 > 0)
                p0 = (t + x9) & 1
                r = x9 & 1
                for x10 in range(cap - x6 + 1):
                    g3 = t + x6 + x10
                    L[g2][g3][base + int(x10 > 0)][p0 ^ (x10 & 1)][r] += 1
    return L


def build_bc_exact_parity(H: int):
    D = build_pair_triple_parity(H)
    L = build_lex_exact_parity(H)
    # BC[b][c][support][r], r=(x0+x8+x10) mod2.
    BC = [[[[0, 0] for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]

    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            x1par = x1 & 1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    src = D[x1par][g2][g3]
                    dst = BC[b][c]
                    for s in range(6):
                        for x9par in (0, 1):
                            value = src[s][x9par]
                            if value:
                                r = (x0 & 1) ^ x1par ^ x9par
                                dst[s + extra][r] += value

    for t in range(H + 1):
        extra = 2 * int(t > 0)
        terminal_parity = t & 1
        cap = H - t
        for g2 in range(cap + 1):
            b = t + g2
            for g3 in range(cap + 1):
                c = t + g3
                dst = BC[b][c]
                src = L[g2][g3]
                for s in range(6):
                    for r in (0, 1):
                        value = src[s][terminal_parity][r]
                        if value:
                            dst[s + extra][r] += value
    return BC


def even_interval_normal_sum(d: int, lower: int, upper: int, excluded: set[int]) -> tuple[int, int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0
    n = (hi - lo) // 2 + 1
    total_e = n * (lo + hi) // 2
    total = n * (19 * d + 1) - 5 * total_e
    count = n
    for e in sorted(excluded):
        if lo <= e <= hi and e % 2 == 0:
            total -= 19 * d - 5 * e + 1
            count -= 1
    return count, total


def census(rows: list[tuple[str, int, int]]) -> dict:
    H = max(d // 2 for _, _, d in rows)
    BC = build_bc_exact_parity(H)
    total_prefix_by_r = [0, 0]
    total_accepted = 0
    total_rejected = 0
    total_terms = 0
    by_g_terms = {0: 0, 1: 0}
    by_g_rejected = {0: 0, 1: 0}
    per_row = []

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        row_prefix_by_r = [0, 0]
        row_accepted = 0
        row_rejected = 0
        row_terms = 0
        A = [[triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]

        for b in range(h + 1):
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = component3(d, b, c)
                if c3 < 0:
                    continue
                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    if 8 * a * a + 8 * b * b + 6 * c * c <= 3 * d * d + 96:
                        continue
                    M = a + b + c
                    ca = component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    scount = [[[0 for _ in range(11)] for __ in range(2)]][0]
                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left = pair[r]
                            if not left:
                                continue
                            for sa, right in enumerate(avec):
                                if right:
                                    scount[r][sbc + sa] += left * right

                    for support in range(11):
                        qneed = K - support
                        if qneed > 0 and srem < qneed:
                            continue
                        lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                        upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                        if lower > upper:
                            continue
                        excluded: set[int] = set()
                        e_n358 = 3 * d - (b - c)
                        if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                            excluded.add(e_n358)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        ne, normal_sum = even_interval_normal_sum(d, lower, upper, excluded)
                        if ne <= 0:
                            continue
                        req((normal_sum - ne) % 2 == 0, "odd normal half-sum regression")
                        half_sum = (normal_sum - ne) // 2
                        for r in (0, 1):
                            count = scount[r][support]
                            if not count:
                                continue
                            row_prefix_by_r[r] += count * ne
                            # N=19d-5e is even. If required parity r=0, accepted
                            # x4 count is k+1 and rejected k; for r=1 vice versa.
                            row_accepted += count * (half_sum + (1 - r) * ne)
                            row_rejected += count * (half_sum + r * ne)
                            row_terms += count * normal_sum

        req(row_terms > 0, f"HPADJ row unexpectedly empty {row_id}")
        req(row_accepted + row_rejected == row_terms, f"row partition mismatch {row_id}")
        total_prefix_by_r[0] += row_prefix_by_r[0]
        total_prefix_by_r[1] += row_prefix_by_r[1]
        total_accepted += row_accepted
        total_rejected += row_rejected
        total_terms += row_terms
        by_g_terms[g] += row_terms
        by_g_rejected[g] += row_rejected
        per_row.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "prefix_parity0": row_prefix_by_r[0],
            "prefix_parity1": row_prefix_by_r[1],
            "exceptional_prefix_stratum_instances": sum(row_prefix_by_r),
            "kernel_accepted_terminals": row_accepted,
            "kernel_rejected_terminals": row_rejected,
            "candidate_hodge_endpoint_terms": row_terms,
        })

    # Reproduce the retained HPADJ population before trusting the new split.
    req(len(per_row) == EXPECTED["affected_rows"], "HPADJ affected-row count drift")
    req(sum(total_prefix_by_r) == EXPECTED["exceptional_prefix_stratum_instances"], "HPADJ prefix-instance count drift")
    req(total_terms == EXPECTED["charged_terminal_lower_bound"], "HPADJ terminal lower-bound drift")
    req(by_g_terms[0] == EXPECTED["genus0_terminal_lower_bound"], "HPADJ genus0 subtotal drift")
    req(by_g_terms[1] == EXPECTED["genus1_terminal_lower_bound"], "HPADJ genus1 subtotal drift")

    legacy_stream = hashlib.sha256()
    parity_stream = hashlib.sha256()
    for rec in sorted(per_row, key=lambda r: (r["g"], r["d"])):
        legacy_stream.update(json.dumps({
            "g": rec["g"],
            "d": rec["d"],
            "candidate_hodge_endpoint_terms": rec["candidate_hodge_endpoint_terms"],
        }, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parity_stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(legacy_stream.hexdigest() == EXPECTED["per_row_stream_sha256"], "HPADJ legacy per-row stream drift")

    return {
        "row_count": len(per_row),
        "prefix_parity0": total_prefix_by_r[0],
        "prefix_parity1": total_prefix_by_r[1],
        "exceptional_prefix_stratum_instances": sum(total_prefix_by_r),
        "kernel_accepted_terminals": total_accepted,
        "kernel_rejected_terminals": total_rejected,
        "charged_terminal_lower_bound": total_terms,
        "genus0_kernel_rejected_terminals": by_g_rejected[0],
        "genus1_kernel_rejected_terminals": by_g_rejected[1],
        "legacy_per_row_stream_sha256": legacy_stream.hexdigest(),
        "parity_per_row_stream_sha256": parity_stream.hexdigest(),
        "rows": per_row,
    }


def main() -> None:
    manifest = load_locked_json(MANIFEST, LOCKS["manifest_blob"], LOCKS["manifest_canonical"], "FULL178 manifest")
    req(FAMILY.is_file() and git_blob(FAMILY) == LOCKS["family_blob"], "compressed terminal family blob drift")
    hpadj = load_locked_json(HPADJ_SOURCE, LOCKS["hpadj_source_blob"], LOCKS["hpadj_source_canonical"], "HPADJ01 source")
    kernel = load_locked_json(KERNEL_RESULT, LOCKS["kernel_result_blob"], LOCKS["kernel_result_canonical"], "HPADJ10 kernel result")
    req(kernel.get("kernel", {}).get("accepted_terminal_condition") == "x4 ≡ x0 + x8 + x10 (mod 2)", "kernel parity identity drift")
    req(hpadj.get("current_v22_intersection_lower_bound", {}).get("candidate_endpoint_rejected_terminals_lower_bound") == EXPECTED["charged_terminal_lower_bound"], "HPADJ source population drift")

    result = census(manifest_rows(manifest))
    req(result["kernel_accepted_terminals"] + result["kernel_rejected_terminals"] == result["charged_terminal_lower_bound"], "global kernel partition mismatch")

    out = {
        "schema": "STAGE32EX5_HPADJ10_POPULATION_KERNEL_COUNT_V1",
        "status": "EXACT_POPULATION_WIDE_COUNT_ON_RETAINED_HPADJ01_CANDIDATE_POPULATION_AUDIT_REQUIRED",
        "route_id": "HPADJ-10_ex5",
        "population_scope": {
            "name": "HPADJ01_CURRENT_V22_CHARGED_LOWER_BOUND_POPULATION",
            "affected_rows": result["row_count"],
            "source_blob_sha1": LOCKS["hpadj_source_blob"],
            "source_canonical_sha256": LOCKS["hpadj_source_canonical"],
            "population_is_full_current_stage32_residual": False,
            "population_is_exact_retained_hpadj01_subset": True,
        },
        "kernel": {
            "source_blob_sha1": LOCKS["kernel_result_blob"],
            "source_canonical_sha256": LOCKS["kernel_result_canonical"],
            "accepted_terminal_condition": "x4 ≡ x0 + x8 + x10 (mod 2)",
            "equivalent_exceptional_only_parity_under_terminal_family": "x0 + x1 + x9 (mod 2)",
        },
        "exact_count": {
            "exceptional_prefix_stratum_instances": result["exceptional_prefix_stratum_instances"],
            "prefix_required_x4_parity0": result["prefix_parity0"],
            "prefix_required_x4_parity1": result["prefix_parity1"],
            "charged_terminal_lower_bound": result["charged_terminal_lower_bound"],
            "kernel_accepted_terminals": result["kernel_accepted_terminals"],
            "kernel_rejected_terminals": result["kernel_rejected_terminals"],
            "rejected_fraction_numerator": result["kernel_rejected_terminals"],
            "rejected_fraction_denominator": result["charged_terminal_lower_bound"],
            "genus0_kernel_rejected_terminals": result["genus0_kernel_rejected_terminals"],
            "genus1_kernel_rejected_terminals": result["genus1_kernel_rejected_terminals"],
            "legacy_per_row_stream_sha256": result["legacy_per_row_stream_sha256"],
            "parity_per_row_stream_sha256": result["parity_per_row_stream_sha256"],
        },
        "method": {
            "terminal_enumeration_used": False,
            "symbolic_prefix_census": True,
            "normal_x4_count_closed_form": True,
            "all_178_rows_replayed": True,
            "legacy_hpadj_population_totals_exactly_reproduced": True,
            "per_prefix_rule": "For N=19*d-5*e=2k, r=0 gives accepted k+1/rejected k; r=1 gives accepted k/rejected k+1.",
        },
        "semantics": {
            "population_wide_count_completed_within_retained_hpadj01_scope": True,
            "global_50_percent_claimed": False,
            "full_stage32_residual_fraction_claimed": False,
            "main_pruning_credit_claimed": False,
            "accepted_terminals_assert_geometric_realization": False,
            "rejected_terminals_fail_integral_selected64_picard_completion_necessary_condition": True,
            "hostile_audit_required_before_consumption": True,
            "next_exact_unit": "Hostile-audit this exact population count; only after PASS may MAIN evaluate a population-preserving consumption adapter and overlap accounting.",
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "rows": result["rows"],
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
