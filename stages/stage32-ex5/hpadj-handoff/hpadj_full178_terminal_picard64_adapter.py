#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
MANIFEST = RESIDUAL / "full178-manifest.json"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
PREFIX = RESIDUAL / "pairing_prefix_engine.py"
HPERP = RESIDUAL / "hperp_integral_adapter.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))
from compressed_terminal_family import terminal_predicate
from compressed_terminal_indexer import CompressedTerminalIndexer
from pairing_prefix_engine import RetainedBasisPairingTransform
import picard_base_rows_retained as retained_bundle

SCHEMA = "STAGE32EX5_HPADJ_FULL178_TERMINAL_TO_PICARD64_INTERFACE_V1"
DEMAND_ID = "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXCEPTIONAL_LABELS = [95, 99, 103, 102, 97, 94, 101, 93, 98, 96]
GROUPS = {
    "a": [103, 102, 101],
    "b": [99, 97, 98],
    "c": [95, 94, 93, 96],
}
SOURCE_LOCKS = {
    "full178_manifest_blob_sha1": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "full178_manifest_canonical_sha256": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
    "compressed_terminal_family_blob_sha1": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "compressed_terminal_indexer_blob_sha1": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "pairing_prefix_engine_blob_sha1": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "hperp_integral_adapter_blob_sha1": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    "picard_bundle_source_blob_sha1": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "picard_bundle_canonical_sha256": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
}
HPADJ_SOURCE = {
    "path": "stages/stage32/management/hpadj-01/RESULT.json",
    "authority_exact_head": "f8039b4ce479a4b91f2f0547e7049f629e9be5f5",
    "authority_hostile_audit_review_id": 5188224290,
    "blob_sha1": "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b",
    "canonical_sha256": "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506",
    "affected_rows": 178,
    "exceptional_prefix_stratum_instances": 19700993066083231249,
    "charged_terminal_lower_bound": 27104321327305699275487,
    "genus0_terminal_lower_bound": 6263333577918328238904,
    "genus1_terminal_lower_bound": 20840987749387371036583,
    "per_row_stream_sha256": "5852e58fdd570e05c057d5fcaf426f6b25fefb1eaf83ae1329657b42289775ae",
}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def req(v: bool, msg: str) -> None:
    if not v:
        raise ValueError(msg)


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def verify_source_locks() -> dict:
    checks = [
        (MANIFEST, SOURCE_LOCKS["full178_manifest_blob_sha1"]),
        (FAMILY, SOURCE_LOCKS["compressed_terminal_family_blob_sha1"]),
        (INDEXER, SOURCE_LOCKS["compressed_terminal_indexer_blob_sha1"]),
        (PREFIX, SOURCE_LOCKS["pairing_prefix_engine_blob_sha1"]),
        (HPERP, SOURCE_LOCKS["hperp_integral_adapter_blob_sha1"]),
        (BUNDLE_SOURCE, SOURCE_LOCKS["picard_bundle_source_blob_sha1"]),
    ]
    for path, expected in checks:
        req(path.is_file(), f"missing source lock {path.relative_to(ROOT)}")
        req(git_blob(path) == expected, f"source-lock drift {path.relative_to(ROOT)}")
    manifest = json.loads(MANIFEST.read_text())
    body = dict(manifest)
    stored = body.pop("canonical_sha256_without_this_field", None)
    req(stored == SOURCE_LOCKS["full178_manifest_canonical_sha256"], "manifest stored canonical drift")
    req(csha(body) == stored, "manifest canonical drift")
    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == SOURCE_LOCKS["picard_bundle_canonical_sha256"], "Picard bundle canonical drift")
    return manifest


def manifest_rows(manifest: dict) -> list[tuple[str, int, int]]:
    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    req(len(rows) == 178 and len(set(rows)) == 178, "FULL178 row partition drift")
    out = []
    for row_id in rows:
        g = int(row_id[1])
        d = int(row_id.split("-d", 1)[1])
        req(g in (0, 1) and d % 2 == 0 and d >= 8, f"row parse drift {row_id}")
        out.append((row_id, g, d))
    return out


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
    for parity in (0, 1):
        for g2 in range(H + 1):
            for g3 in range(H + 1):
                dst = D[parity][g2][g3]
                for sb in range(3):
                    for pb in (0, 1):
                        bv = B[g2][sb][pb]
                        if not bv:
                            continue
                        for sc in range(4):
                            cv = C[g3][sc][pb ^ parity]
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


def build_bc_exact(H: int = 96):
    D = build_pair_triple(H)
    L = build_lex_exact(H)
    BC = [[[0] * 8 for _ in range(H + 1)] for __ in range(H + 1)]
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            parity = x1 & 1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    src = D[parity][g2][g3]
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


def hpadj_census(rows: list[tuple[str, int, int]]) -> dict:
    BC = build_bc_exact(96)
    total_prefix = 0
    total_terms = 0
    by_g = {0: 0, 1: 0}
    per_row = []
    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        row_prefix = 0
        row_terms = 0
        A = [[triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        for b in range(h + 1):
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(bcv):
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
                    scount = [0] * 11
                    for sbc, left in enumerate(bcv):
                        if not left:
                            continue
                        for sa, right in enumerate(avec):
                            if right:
                                scount[sbc + sa] += left * right
                    for support, count in enumerate(scount):
                        if not count:
                            continue
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
                        row_prefix += count * ne
                        row_terms += count * normal_sum
        req(row_terms > 0, f"HPADJ row unexpectedly empty {row_id}")
        total_prefix += row_prefix
        total_terms += row_terms
        by_g[g] += row_terms
        per_row.append({"row_id": row_id, "g": g, "d": d, "exceptional_prefix_stratum_instances": row_prefix, "candidate_hodge_endpoint_terms": row_terms})
    stream = hashlib.sha256()
    for rec in sorted(per_row, key=lambda r: (r["g"], r["d"])):
        stream.update(json.dumps({"g": rec["g"], "d": rec["d"], "candidate_hodge_endpoint_terms": rec["candidate_hodge_endpoint_terms"]}, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(len(per_row) == HPADJ_SOURCE["affected_rows"], "HPADJ affected row count drift")
    req(total_prefix == HPADJ_SOURCE["exceptional_prefix_stratum_instances"], "HPADJ prefix-instance count drift")
    req(total_terms == HPADJ_SOURCE["charged_terminal_lower_bound"], "HPADJ terminal lower-bound drift")
    req(by_g[0] == HPADJ_SOURCE["genus0_terminal_lower_bound"] and by_g[1] == HPADJ_SOURCE["genus1_terminal_lower_bound"], "HPADJ genus subtotal drift")
    req(stream.hexdigest() == HPADJ_SOURCE["per_row_stream_sha256"], "HPADJ per-row stream drift")
    return {"row_count": len(per_row), "exceptional_prefix_stratum_instances": total_prefix, "charged_terminal_lower_bound": total_terms, "genus0_terminal_lower_bound": by_g[0], "genus1_terminal_lower_bound": by_g[1], "per_row_stream_sha256": stream.hexdigest(), "rows": per_row}


def hpadj_member(*, g: int, d: int, e: int, values: tuple[int, ...]) -> bool:
    if not terminal_predicate(values, e=e, d=d):
        return False
    if g not in (0, 1) or d < 8 or d % 2 or e % 2:
        return False
    x = tuple(int(v) for v in values)
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    if 8 * a * a + 8 * b * b + 6 * c * c <= 3 * d * d + 96:
        return False
    support = sum(int(x[i] > 0) for i in range(11) if i != 4)
    M = a + b + c
    K = ceil_div(d - 16 * g + 16, 4)
    ca = component_a(d, a)
    c3 = component3(d, b, c)
    if ca < 0 or c3 < 0:
        return False
    srem = min(16, d) + ca + c3
    qneed = K - support
    if qneed > 0 and srem < qneed:
        return False
    lower = max(8 if g == 0 else 4, K, d - 4 * g + 4, M, M + max(0, qneed))
    upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
    if not lower <= e <= upper:
        return False
    e_n358 = 3 * d - (b - c)
    if b <= d // 2 - 5 and support + srem == K and e_n358 - M >= srem and e == e_n358:
        return False
    if g == 1 and d == 8 and e == 8:
        return False
    return True


def completion_contract() -> dict:
    bundle = retained_bundle.load()
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(len(labels) == 64 and len(set(labels)) == 64, "selected64 label identity drift")
    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    req(len(fixed_positions) == 11 and len(free_positions) == 53, "fixed/free selected64 partition drift")
    B = transform.inverse_integer
    fixed = B.extract(list(range(64)), fixed_positions)
    free = B.extract(list(range(64)), free_positions)
    req(transform.den == 8, "selected64 inverse denominator drift")
    return {
        "selected_pairing_coordinate_order_1based": labels,
        "terminal_assignment_labels_1based": ASSIGNMENT_LABELS,
        "terminal_fixed_selected_positions_0based": fixed_positions,
        "free_selected_positions_0based": free_positions,
        "free_selected_labels_1based": [labels[i] for i in free_positions],
        "inverse_denominator": int(transform.den),
        "inverse_integer_matrix_sha256": csha(matrix_list(B)),
        "terminal_fixed_coefficient_matrix_sha256": csha(matrix_list(fixed)),
        "free_completion_coefficient_matrix_sha256": csha(matrix_list(free)),
        "coordinate_formula": "retained_picard64 = (B_fixed*x11 + B_free*z53)/8, defined exactly when every numerator coordinate is divisible by 8",
        "fiber_parameter_semantics": "z53 is the ordered integer vector of the 53 unassigned selected-pairing coordinates; every integral Picard64 completion of the terminal is represented exactly once",
        "integrality_congruence": "B_fixed*x11 + B_free*z53 == 0 (mod 8) coordinatewise",
        "full_picard64_coordinate_count": 64,
        "free_pairing_parameter_count": 53,
        "terminal_pairing_count": 11,
    }


def terminal_identity(*, g: int, d: int, e: int, values: tuple[int, ...], allowed_rows: set[tuple[int, int]]) -> dict:
    req((g, d) in allowed_rows, "terminal row is not in FULL178")
    idx = CompressedTerminalIndexer(e, d)
    rank = idx.rank(values)
    req(idx.unrank(rank) == tuple(values), "terminal rank/unrank regression")
    req(hpadj_member(g=g, d=d, e=e, values=tuple(values)), "terminal is not in retained HPADJ population")
    return {"row_id": f"g{g}-d{d:03d}", "g": g, "d": d, "e": e, "compressed_terminal_rank": rank, "pairings_x0_to_x10": list(values)}


def describe() -> dict:
    manifest = verify_source_locks()
    rows = manifest_rows(manifest)
    census = hpadj_census(rows)
    completion = completion_contract()
    row_stream = hashlib.sha256()
    for rec in sorted(census["rows"], key=lambda r: (r["g"], r["d"])):
        row_stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    body = {
        "schema": SCHEMA,
        "stage": 32,
        "producer_lane": "EX5",
        "consumer_lane": "MAIN",
        "demand_id": DEMAND_ID,
        "status": "PRODUCED_SOURCE_LOCKED_EXACT_INTERFACE_NO_MATH_CREDIT",
        "hpadj01_population_identity": dict(HPADJ_SOURCE),
        "all_178_rows_partition": {
            "manifest_path": "stages/stage32/residual-32-01-production/full178-manifest.json",
            "manifest_blob_sha1": SOURCE_LOCKS["full178_manifest_blob_sha1"],
            "manifest_canonical_sha256": SOURCE_LOCKS["full178_manifest_canonical_sha256"],
            "row_count": census["row_count"],
            "row_id_semantics": "g{genus}-d{degree:03d}",
            "population_count_by_row_replay_stream_sha256": census["per_row_stream_sha256"],
            "extended_row_partition_stream_sha256": row_stream.hexdigest(),
            "full_materialization_required": False,
        },
        "terminal_identity_or_exact_rank_unrank_contract": {
            "identity_tuple": ["row_id", "e", "compressed_terminal_rank"],
            "indexer_path": "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py",
            "indexer_blob_sha1": SOURCE_LOCKS["compressed_terminal_indexer_blob_sha1"],
            "canonical_index_order": "EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST",
            "rank_unrank_roundtrip_exact": True,
            "hpadj_membership_predicate": "terminal_predicate AND Cauchy violation AND current-V22/N357 survivor interval AND exact N358-slice exclusion AND conservative g1-d008/e8 exclusion",
            "x4_normal_budget": "0 <= x4 <= 19*d-5*e",
            "full_population_materialization_required": False,
        },
        "terminal_to_picard64_map": completion,
        "stored_10_exceptional_coordinate_identity": {
            "terminal_assignment_order_1based": ASSIGNMENT_LABELS,
            "normal_x4_label_1based": 49,
            "exceptional_labels_1based": EXCEPTIONAL_LABELS,
            "groups": GROUPS,
            "all_exceptional_labels_in_selected64": True,
            "stored_exceptional_coordinate_count": 10,
        },
        "reconstructed_picard64_coordinate_identity": {
            "model": "EXACT_SELECTED64_PAIRING_FIBER_TO_RETAINED_PRIMITIVE_PICARD64",
            "retained_picard64_coordinate_count": 64,
            "picard_bundle_canonical_sha256": SOURCE_LOCKS["picard_bundle_canonical_sha256"],
            "selected64_inverse_denominator": completion["inverse_denominator"],
            "selected64_inverse_integer_matrix_sha256": completion["inverse_integer_matrix_sha256"],
            "fixed_plus_free_affine_fiber_exact": True,
            "unique_coordinate_vector_for_each_integral_selected64_completion": True,
            "terminal_alone_asserts_completion_exists": False,
        },
        "population_cardinality_replay": {
            "affected_rows": census["row_count"],
            "exceptional_prefix_stratum_instances": census["exceptional_prefix_stratum_instances"],
            "charged_terminal_lower_bound": census["charged_terminal_lower_bound"],
            "genus0_terminal_lower_bound": census["genus0_terminal_lower_bound"],
            "genus1_terminal_lower_bound": census["genus1_terminal_lower_bound"],
            "per_row_stream_sha256": census["per_row_stream_sha256"],
            "replay_algorithm": "exact symbolic BC support/group convolution; exact even-e interval normal-block sum; exact N358 and g1-d008/e8 exclusions",
            "matches_hpadj01_source_lock": True,
        },
        "dependency_source_locks": dict(SOURCE_LOCKS),
        "replay_verifier": {
            "producer": "stages/stage32-ex5/hpadj-handoff/hpadj_full178_terminal_picard64_adapter.py",
            "verifier": "stages/stage32-ex5/hpadj-handoff/verify_hpadj_full178_terminal_picard64_interface.py",
            "deterministic_replay": True,
        },
        "credit_firewall": {
            "demand_satisfaction_grants_math_credit": False,
            "hpadj_main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "integrality_or_irreducibility_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "bc2_38_main_credit": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    return body


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--sample", nargs=4, metavar=("G", "D", "E", "RANK"))
    args = ap.parse_args()
    if args.sample:
        manifest = verify_source_locks()
        rows = manifest_rows(manifest)
        allowed = {(g, d) for _, g, d in rows}
        g, d, e, rank = map(int, args.sample)
        idx = CompressedTerminalIndexer(e, d)
        values = idx.unrank(rank)
        out = terminal_identity(g=g, d=d, e=e, values=values, allowed_rows=allowed)
    else:
        out = describe()
    text = json.dumps(out, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
