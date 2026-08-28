#!/usr/bin/env python3
"""Verify the Stage33-11f exact MAIN closure of all 26 connecting columns."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stage33-11f-source-lock.json"
E_CERT_PATH = HERE.parent / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
OUT = HERE / "stage33-11f-26-column-exact-closure-certificate.json"
SOURCE_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"
E_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical certificate mismatch: {path}")
    return obj


def rowmul(v, matrix):
    return tuple(
        sum(v[i] * matrix[i][j] for i in range(26)) & 1 for j in range(26)
    )


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(26)) & 1 for j in range(26)] for i in range(26)]


def identity():
    return [[int(i == j) for j in range(26)] for i in range(26)]


def bits(v):
    return sum((x & 1) << i for i, x in enumerate(v))


def vector(n):
    return [(n >> i) & 1 for i in range(26)]


def orbit_with_words(start, actions, names):
    start = tuple(start)
    words = {start: []}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for name, action in zip(names, actions):
            w = rowmul(v, action)
            if w not in words:
                words[w] = words[v] + [name]
                queue.append(w)
    ordered = sorted(words, key=bits)
    return ordered, [words[v] for v in ordered]


def span_basis_with_combinations(vectors):
    """Return pivots carrying an XOR mask of the original vector list."""
    pivots = {}
    for i, v in enumerate(vectors):
        x, combo = bits(v), 1 << i
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = (x, combo)
                break
            y, ycombo = pivots[p]
            x ^= y
            combo ^= ycombo
    return pivots


def solve_in_span(target, pivots):
    x, combo = bits(target), 0
    while x:
        p = x.bit_length() - 1
        if p not in pivots:
            return None
        y, ycombo = pivots[p]
        x ^= y
        combo ^= ycombo
    return combo


def xor_selected(vectors, indices):
    ans = 0
    for i in indices:
        ans ^= bits(vectors[i])
    return vector(ans)


def build_certificate():
    source = load_checked(SOURCE, SOURCE_SHA)
    e_cert = load_checked(E_CERT_PATH, E_SHA)
    action_names = source["exact_source_actions"]["action_names"]
    actions = source["exact_source_actions"]["matrices"]
    if len(action_names) != 9 or len(actions) != 9:
        raise SystemExit("exact source action count moved")
    if any(len(a) != 26 or any(len(r) != 26 for r in a) for a in actions):
        raise SystemExit("exact source action shape moved")
    if any(matmul(a, a) != identity() for a in actions):
        raise SystemExit("a source generator is not an involution")
    if matmul(matmul(actions[7], actions[8]), matmul(actions[7], actions[8])) == identity():
        raise SystemExit("swap pair unexpectedly has order at most two")
    s3 = matmul(actions[7], actions[8])
    if matmul(matmul(s3, s3), s3) != identity():
        raise SystemExit("swap pair fails the exact S3 relation")

    expected_generators = [2, 3, 24, 25, 26, 4, 1, 7, 5, 10, 8, 9, 16, 15]
    generator_records = {int(r["source_direction"].split("_")[1]): r for r in e_cert["generator_records"]}
    if list(generator_records) != expected_generators:
        raise SystemExit("33-11e exact generator order/set moved")
    for record in generator_records.values():
        if record["exact_consequence"] != "ZERO_EXACT_PRIME_LEVEL_CC_CT":
            raise SystemExit("non-exact generator consequence")
        for action in ("cc", "ct"):
            difference = record["prime_level_galois_differences"][action]
            if difference != {"nonzero_prime_coefficients": 0, "status": "ZERO_EXACT_PRIME_LEVEL"}:
                raise SystemExit("prime-level Galois difference moved")

    direct = source["frozen_cyclic_partition"]["smallest_exact_directions_1based"]
    if direct != [2, 3, 24, 25, 26]:
        raise SystemExit("direct source directions moved")
    blocks = source["frozen_cyclic_partition"]["remaining_block_records"]
    if len(blocks) != 9:
        raise SystemExit("cyclic block count moved")

    coverage = list(direct)
    orbit_proofs = {}
    for block in blocks:
        representative = block["representative_direction_1based"]
        if representative not in generator_records:
            raise SystemExit("cyclic representative lacks 33-11e exact proof")
        e = [int(i == representative - 1) for i in range(26)]
        orbit, words = orbit_with_words(e, actions, action_names)
        pivots = span_basis_with_combinations(orbit)
        rank = len(pivots)
        if rank != block["cyclic_submodule_dimension_f2"]:
            raise SystemExit(f"cyclic dimension mismatch at A2_{representative:02d}")
        member_proofs = {}
        for member in block["named_source_directions_1based"]:
            target = [int(i == member - 1) for i in range(26)]
            combo = solve_in_span(target, pivots)
            if combo is None:
                raise SystemExit(f"A2_{member:02d} is not in certified representative span")
            selected = [i for i in range(len(orbit)) if (combo >> i) & 1]
            if xor_selected(orbit, selected) != target:
                raise SystemExit("recorded orbit-span witness does not reconstruct target")
            member_proofs[str(member)] = {
                "target_basis_name": f"A2_{member:02d}",
                "selected_orbit_terms": [
                    {"orbit_index": i, "action_word": words[i], "source_vector_f2": list(orbit[i])}
                    for i in selected
                ],
                "xor_equals_target_exactly": True,
            }
        orbit_proofs[str(representative)] = {
            "representative_basis_name": f"A2_{representative:02d}",
            "orbit_size": len(orbit),
            "orbit_span_dimension_f2": rank,
            "expected_cyclic_submodule_dimension_f2": block["cyclic_submodule_dimension_f2"],
            "named_member_witnesses": member_proofs,
        }
        coverage.extend(block["named_source_directions_1based"])
    if sorted(coverage) != list(range(1, 27)) or len(coverage) != 26:
        raise SystemExit("direct/cyclic partition is not exactly 1..26")

    owner = {i: i for i in direct}
    for block in blocks:
        rep = block["representative_direction_1based"]
        for member in block["named_source_directions_1based"]:
            owner[member] = rep

    columns = []
    for i in range(1, 27):
        rep = owner[i]
        record = generator_records[rep]
        if i in direct:
            transport = {"kind": "DIRECT_EXACT_GENERATOR", "representative": f"A2_{rep:02d}"}
        else:
            transport = {
                "kind": "CERTIFIED_F2_ORBIT_SPAN",
                "representative": f"A2_{rep:02d}",
                "witness": orbit_proofs[str(rep)]["named_member_witnesses"][str(i)],
            }
        columns.append({
            "column_1based": i,
            "source_basis_name": f"A2_{i:02d}",
            "source_basis_vector_f2": [int(j == i - 1) for j in range(26)],
            "exact_zero_generator": f"A2_{rep:02d}",
            "generator_package_prime_vector_sha256": record["package_prime_vector_sha256"],
            "prime_level_galois_difference_cc": "ZERO_EXACT_PRIME_LEVEL",
            "prime_level_galois_difference_ct": "ZERO_EXACT_PRIME_LEVEL",
            "source_transport": transport,
            "absolute_receiver_value": {
                "X_Q_power_5": "ZERO",
                "X_Q_i_power_3": "ZERO",
                "E_L": "ZERO_CLASS",
                "E_L_filtration_subobject": "ZERO",
                "E_L_filtration_quotient": "ZERO",
                "E_L_splitting_used": False,
            },
            "status": "ZERO_EXACT_MAIN",
            "unresolved": False,
        })

    cert = {
        "schema": "STAGE33_11F_26_COLUMN_EXACT_CLOSURE_V1",
        "stage": "33-11f",
        "branch": "CARRIER-PRIME-REFINEMENT-CONTINUATION/26-COLUMN-EXACT-CLOSURE",
        "source_locks": {
            "stage33_11f_source_lock_sha256": SOURCE_SHA,
            "audited_stage33_11e_certificate_sha256": E_SHA,
            "audited_stage33_11e_pr": 1457,
            "audited_stage33_11e_head": "433dc8f644ed173555c261fe1742e32851611ea9",
            "stage33_10_absolute_receiver_handoff_sha256": source["stage33_10_absolute_receiver"]["handoff_sha256"],
        },
        "exact_adapter": {
            "statement": "The connecting construction is F2-linear and equivariant for the nine certified source actions. Exact prime-level equality g(D)-D=0 for each of the 14 generators therefore gives the zero absolute connecting class for every vector in its certified cyclic source submodule.",
            "no_receiver_splitting_used": True,
            "finite_v4_shortcut_used": False,
            "quotient_or_extension_field_promotion_used": False,
        },
        "source_action_checks": {
            "action_count": 9,
            "all_generators_involutive": True,
            "swap_pair_s3_relation_exact": True,
            "matrices_sha256": source["exact_source_actions"]["matrices_sha256"],
        },
        "orbit_span_proofs": orbit_proofs,
        "absolute_receiver": source["stage33_10_absolute_receiver"]["exact_receiver"],
        "columns": columns,
        "summary": {
            "exact_generator_inputs": "14/14",
            "named_source_directions": 26,
            "exact_main_connecting_columns": "26/26",
            "exact_audited_connecting_columns": "0/26",
            "unresolved_connecting_columns": 0,
            "connecting_map_main_value": "ZERO_EXACT_ALL_26_COLUMNS",
            "stage33_11f_main_exit_condition_satisfied": True,
            "stage33_11f_status": "MAIN_COMPLETE_PENDING_AUDIT",
            "stage33_11_closed_exact": False,
            "next": "33-11g HOSTILE-AUDIT-AND-STAGE33-11-EXACT-EXIT",
        },
        "actions_safety": {
            "artifact_uploads": 0,
            "projected_peak_artifact_storage_mb": 0,
            "heavy_compute_runners": 0,
            "remote_cas_used": False,
            "smith_form_used_for_target": False,
        },
        "audit_debt": [
            "Hostile audit must independently verify all 26 orbit-span witnesses and the exact adapter.",
            "MAIN 26/26 is not audited 26/26 until 33-11g closes.",
            "The non-split E_L filtration is retained; no decomposition or finite-V4 replacement is claimed.",
        ],
        "firewalls": {
            "exact_connecting_columns_promoted_beyond_main": False,
            "stage33_11_closed_exact": False,
            "stage33_12_released": False,
            "stage33_08_released": False,
            "stage33_07_closed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-certificate", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write_certificate:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    elif not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("recorded 33-11f certificate differs; regenerate and review")
    print("STAGE33_11F_26_COLUMN_EXACT_CLOSURE=PASS")
    print("EXACT_MAIN_CONNECTING_COLUMNS=" + cert["summary"]["exact_main_connecting_columns"])
    print("EXACT_AUDITED_CONNECTING_COLUMNS=" + cert["summary"]["exact_audited_connecting_columns"])
    print("UNRESOLVED_CONNECTING_COLUMNS=0")
    print("STAGE33_11_CLOSED_EXACT=false")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
