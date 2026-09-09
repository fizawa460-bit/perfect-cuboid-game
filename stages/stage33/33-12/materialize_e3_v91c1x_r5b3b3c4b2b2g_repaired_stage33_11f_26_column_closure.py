#!/usr/bin/env python3
"""Rebuild historical Stage33-11f 26-column closure on the repaired 47-prime inventory."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
SOURCE = STAGE33 / "33-11f" / "stage33-11f-source-lock.json"
HIST11F = STAGE33 / "33-11f" / "stage33-11f-26-column-exact-closure-certificate.json"
REPAIRED = HERE / "e3-v91c1x-r5b3b3c4b2b2f-stage33-11e-actual-direct-prime-transport-replay.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2g-repaired-stage33-11f-26-column-closure.json"

SOURCE_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"
HIST11F_SHA = "c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4"
REPAIRED_SHA = "b4e384e4f88fcb690193c8cfef8dbabf995c400696fe2ba73679fbc657d98480"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
AUDIT_REVIEW = 5150130766
AUDITED_REPAIR_HEAD = "e4a861a13819e60e9e7d7eece8e5c1d90748b68d"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical certificate mismatch: {path}")
    return obj


def rowmul(v, matrix):
    return tuple(sum(v[i] * matrix[i][j] for i in range(26)) & 1 for j in range(26))


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


def recursive_values(obj, key):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                out.append(v)
            out.extend(recursive_values(v, key))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(recursive_values(v, key))
    return out


def unique_recursive_value(obj, key):
    vals = recursive_values(obj, key)
    if not vals:
        raise SystemExit(f"missing recursive key: {key}")
    first = vals[0]
    if any(v != first for v in vals[1:]):
        raise SystemExit(f"non-unique recursive value for key: {key}")
    return first


def build_certificate():
    source = load_checked(SOURCE, SOURCE_SHA)
    hist = load_checked(HIST11F, HIST11F_SHA)
    repaired = load_checked(REPAIRED, REPAIRED_SHA)

    if repaired["entry"] != {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722}:
        raise SystemExit("C4B2B2F authority/progress/PR entry moved")
    xc = repaired["exact_consequence"]
    if not xc["historical_stage33_11e_prime_level_transport_replay_succeeded"]:
        raise SystemExit("C4B2B2F repaired 33-11e replay is not exact")
    if not xc["historical_stage33_11e_nonprime_direct_support_defect_repaired"]:
        raise SystemExit("C4B2B2F prime-type repair is not complete")
    for key, expected in {
        "historical_prime_inventory_count": 44,
        "historical_nonprime_direct_support_ids_removed": 9,
        "retained_historical_exact_prime_count": 35,
        "repaired_actual_direct_prime_count": 24,
        "new_actual_direct_prime_ids_not_previously_in_inventory": 12,
        "replayed_prime_inventory_count": 47,
    }.items():
        if unique_recursive_value(repaired, key) != expected:
            raise SystemExit(f"C4B2B2F inventory count moved: {key}")
    if unique_recursive_value(repaired, "historical_stage33_11f_26_column_closure_reuse_allowed") is not False:
        raise SystemExit("historical 33-11f reuse firewall unexpectedly moved")

    prime_actions = repaired["prime_actions"]
    if prime_actions["actions_total_on_replayed_prime_inventory"] is not True:
        raise SystemExit("C4B2B2F prime actions are not total")
    inventory = set(prime_actions["cc"])
    if len(inventory) != 47 or set(prime_actions["ct"]) != inventory:
        raise SystemExit("C4B2B2F cc/ct prime-action inventory mismatch")
    if set(prime_actions["cc"].values()) != inventory or set(prime_actions["ct"].values()) != inventory:
        raise SystemExit("C4B2B2F prime actions are not permutations of the 47-prime inventory")

    replacement = unique_recursive_value(repaired, "old_to_actual_prime_replacement")
    old_pseudo_ids = set(replacement)
    if len(old_pseudo_ids) != 9 or old_pseudo_ids & inventory:
        raise SystemExit("historical pseudo-prime IDs leaked into repaired inventory")

    expected_generators = [2, 3, 24, 25, 26, 4, 1, 7, 5, 10, 8, 9, 16, 15]
    generator_records = {}
    used_prime_ids = set()
    for record in repaired["generator_records"]:
        direction = int(record["source_direction"].split("_")[1])
        if direction in generator_records:
            raise SystemExit("duplicate repaired generator direction")
        generator_records[direction] = record
        if record["exact_consequence"] != "ZERO_EXACT_REPAIRED_PRIME_LEVEL_CC_CT":
            raise SystemExit("repaired generator consequence moved")
        for action in ("cc", "ct"):
            if record["prime_level_galois_differences"][action] != {"nonzero_prime_coefficients": 0, "status": "ZERO_EXACT_REPAIRED_PRIME_LEVEL"}:
                raise SystemExit("repaired generator Galois difference moved")
        for vec in record["component_signed_prime_vectors"].values():
            used_prime_ids.update(vec)
            if not set(vec) <= inventory:
                raise SystemExit("generator vector uses a prime outside repaired 47-prime inventory")
            if set(vec) & old_pseudo_ids:
                raise SystemExit("generator vector still uses a historical pseudo-prime ID")
    if list(generator_records) != expected_generators or len(generator_records) != 14:
        raise SystemExit("repaired generator order/set moved")

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
            raise SystemExit("cyclic representative lacks repaired generator proof")
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
                "selected_orbit_terms": [{"orbit_index": i, "action_word": words[i], "source_vector_f2": list(orbit[i])} for i in selected],
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
    if orbit_proofs != hist["orbit_span_proofs"]:
        raise SystemExit("recomputed source orbit-span proofs differ from historical 33-11f")

    owner = {i: i for i in direct}
    for block in blocks:
        rep = block["representative_direction_1based"]
        for member in block["named_source_directions_1based"]:
            owner[member] = rep

    hist_columns = {c["column_1based"]: c for c in hist["columns"]}
    columns = []
    changed_prime_vector_columns = 0
    for i in range(1, 27):
        rep = owner[i]
        record = generator_records[rep]
        if i in direct:
            transport = {"kind": "DIRECT_EXACT_GENERATOR", "representative": f"A2_{rep:02d}"}
        else:
            transport = {"kind": "CERTIFIED_F2_ORBIT_SPAN", "representative": f"A2_{rep:02d}", "witness": orbit_proofs[str(rep)]["named_member_witnesses"][str(i)]}
        old_col = hist_columns[i]
        if old_col["source_transport"] != transport:
            raise SystemExit(f"historical source transport changed at column {i}")
        new_hash = record["package_prime_vector_sha256"]
        old_hash = old_col["generator_package_prime_vector_sha256"]
        changed = new_hash != old_hash
        changed_prime_vector_columns += int(changed)
        columns.append({
            "column_1based": i,
            "source_basis_name": f"A2_{i:02d}",
            "source_basis_vector_f2": [int(j == i - 1) for j in range(26)],
            "exact_zero_generator": f"A2_{rep:02d}",
            "historical_generator_package_prime_vector_sha256": old_hash,
            "repaired_generator_package_prime_vector_sha256": new_hash,
            "prime_vector_changed_by_actual_prime_repair": changed,
            "prime_level_galois_difference_cc": "ZERO_EXACT_REPAIRED_PRIME_LEVEL",
            "prime_level_galois_difference_ct": "ZERO_EXACT_REPAIRED_PRIME_LEVEL",
            "source_transport": transport,
            "historical_source_transport_identical": True,
            "absolute_receiver_value": {"X_Q_power_5": "ZERO", "X_Q_i_power_3": "ZERO", "E_L": "ZERO_CLASS", "E_L_filtration_subobject": "ZERO", "E_L_filtration_quotient": "ZERO", "E_L_splitting_used": False},
            "status": "ZERO_EXACT_REPAIRED_11F_MAIN",
            "unresolved": False,
        })

    if hist["absolute_receiver"] != source["stage33_10_absolute_receiver"]["exact_receiver"]:
        raise SystemExit("historical 33-11f absolute receiver differs from locked source handoff")

    cert = {
        "schema": "stage33.e3.v91c1x.r5b3b3c4b2b2g.repaired_stage33_11f_26_column_closure.v1",
        "candidate": "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE",
        "role": "EXACT_NONCREDIT_RECONSTRUCTION_OF_STAGE33_11F_ON_C4B2B2F_REPAIRED_47_PRIME_CANONICAL_INVENTORY",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "stage33_11f_source_lock_sha256": SOURCE_SHA,
            "historical_stage33_11f_26_column_closure_sha256": HIST11F_SHA,
            "c4b2b2f_repaired_stage33_11e_transport_sha256": REPAIRED_SHA,
            "c4b2b2f_hostile_reaudit_review": AUDIT_REVIEW,
            "c4b2b2f_hostile_reaudit_exact_head": AUDITED_REPAIR_HEAD,
            "stage33_10_absolute_receiver_handoff_sha256": source["stage33_10_absolute_receiver"]["handoff_sha256"],
        },
        "repair_inventory": {
            "historical_prime_inventory_count": 44,
            "historical_nonprime_direct_support_ids_removed": 9,
            "retained_historical_exact_prime_count": 35,
            "repaired_actual_direct_prime_count": 24,
            "actual_direct_primes_new_relative_to_retained_inventory": 12,
            "repaired_distinct_prime_inventory_count": 47,
            "cc_ct_actions_total_on_repaired_inventory": True,
            "historical_pseudo_prime_ids_absent_from_repaired_inventory": True,
            "generator_component_prime_ids_used_count": len(used_prime_ids),
            "all_generator_component_prime_ids_inside_repaired_inventory": True,
        },
        "exact_adapter": {
            "statement": "The 26-dimensional F2 source action and cyclic-span witnesses are unchanged. C4B2B2F replaces the defective nine pseudo-prime targets at the generator layer by exact vectors on the canonical 47-prime inventory and proves cc(D)-D=ct(D)-D=0 there for all fourteen generator packages. F2-linearity and equivariance therefore transport those repaired exact zero differences through the same certified cyclic source spans to all 26 source columns.",
            "historical_44_slot_prime_inventory_reused_as_is": False,
            "historical_source_orbit_spans_recomputed": True,
            "historical_source_orbit_spans_match_exactly": True,
            "repaired_generator_prime_vectors_consumed": True,
            "no_receiver_splitting_used": True,
            "finite_v4_shortcut_used": False,
            "quotient_or_extension_field_promotion_used": False,
        },
        "source_action_checks": {"action_count": 9, "all_generators_involutive": True, "swap_pair_s3_relation_exact": True, "matrices_sha256": source["exact_source_actions"]["matrices_sha256"]},
        "orbit_span_proofs": orbit_proofs,
        "absolute_receiver": source["stage33_10_absolute_receiver"]["exact_receiver"],
        "columns": columns,
        "summary": {
            "repaired_exact_generator_inputs": "14/14",
            "named_source_directions": 26,
            "repaired_exact_main_connecting_columns": "26/26",
            "repaired_exact_audited_connecting_columns": "0/26",
            "unresolved_connecting_columns": 0,
            "connecting_map_repaired_main_value": "ZERO_EXACT_ALL_26_COLUMNS_ON_REPAIRED_47_PRIME_INVENTORY",
            "columns_whose_generator_prime_vector_changed": changed_prime_vector_columns,
            "repaired_stage33_11f_main_exit_condition_satisfied": True,
            "repaired_stage33_11f_status": "MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
            "stage33_11_closed_exact": False,
            "next_exact_leaf": "V91C1X_R5_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE_HOSTILE_AUDIT",
        },
        "exact_consequence": {
            "c4b2b2f_hostile_reaudit_consumed": True,
            "repaired_stage33_11f_26_column_closure_reconstructed": True,
            "historical_stage33_11f_44_slot_closure_reused_as_is": False,
            "source_span_geometry_unchanged": True,
            "prime_level_repair_propagated_to_all_26_columns": True,
            "authority_unchanged": True,
            "stage33_progress_unchanged": True,
            "stage33_11_closed_exact": False,
            "unramifiedness_verified": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
        },
        "audit_debt": [
            "Fresh hostile audit must verify the repaired 47-prime generator inputs, the unchanged source-span adapter, and all 26 reconstructed column witnesses.",
            "Repaired MAIN 26/26 is not audited 26/26 until that hostile audit passes.",
            "The non-split E_L filtration is retained; no decomposition or finite-V4 replacement is claimed.",
        ],
        "credit_firewall": {
            "authority_promotion": False,
            "stage33_11_close_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "unramifiedness_credit": False,
            "offboundary_cancellation_credit": False,
            "marked_brauer_image_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
            "perfect_cuboid_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    elif not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("recorded C4B2B2G certificate differs; regenerate and review")
    print("STAGE33_C4B2B2G_REPAIRED_11F_26_COLUMN_CLOSURE=PASS")
    print("REPAIRED_EXACT_MAIN_CONNECTING_COLUMNS=" + cert["summary"]["repaired_exact_main_connecting_columns"])
    print("REPAIRED_EXACT_AUDITED_CONNECTING_COLUMNS=" + cert["summary"]["repaired_exact_audited_connecting_columns"])
    print("UNRESOLVED_CONNECTING_COLUMNS=0")
    print("STAGE33_11_CLOSED_EXACT=false")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
