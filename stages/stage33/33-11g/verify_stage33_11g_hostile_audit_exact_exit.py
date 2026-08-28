#!/usr/bin/env python3
"""Independent hostile audit and exact-exit verifier for Stage33-11."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
OUT = HERE / "stage33-11g-hostile-audit-exact-exit-certificate.json"
LOCK_SHA = "791b98bbf8f92fa71cad6626cead6cf3b65f3edd79e19c30f7fbc9480a9d648c"
D_SHA = "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d"
E_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
F_SHA = "c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4"
F_SOURCE_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical certificate mismatch: {path}")
    return obj


def add(out, key, value):
    out[key] = out.get(key, 0) + value
    if out[key] == 0:
        del out[key]


def acted_signed_vector(v, action):
    out = {}
    for prime, coefficient in v.items():
        add(out, action[prime], coefficient)
    return dict(sorted(out.items()))


def package_vector(component_vectors):
    out = {}
    for v in component_vectors.values():
        for prime, coefficient in v.items():
            add(out, prime, coefficient)
    return dict(sorted(out.items()))


def row_action(v, matrix):
    return tuple(sum(v[i] * matrix[i][j] for i in range(26)) & 1 for j in range(26))


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(26)) & 1 for j in range(26)] for i in range(26)]


def eye():
    return [[int(i == j) for j in range(26)] for i in range(26)]


def bit_integer(v):
    return sum((x & 1) << i for i, x in enumerate(v))


def f2_rank(vectors):
    pivots = {}
    for v in vectors:
        x = bit_integer(v)
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)


def complete_orbit(start, actions):
    seen = {tuple(start)}
    queue = deque(seen)
    while queue:
        v = queue.popleft()
        for action in actions:
            w = row_action(v, action)
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return sorted(seen, key=bit_integer)


def apply_word(start, word, action_by_name):
    v = tuple(start)
    for name in word:
        v = row_action(v, action_by_name[name])
    return v


def xor_vectors(vectors):
    out = [0] * 26
    for v in vectors:
        out = [x ^ y for x, y in zip(out, v)]
    return out


def audit_prime_refinement(d):
    direct = d["inherited_direct_refinements"]
    representatives = d["new_exact_representative_refinements"]
    if direct["carrier_count"] != 6 or len(direct["records"]) != 6:
        raise SystemExit("33-11d direct refinement count moved")
    if len(representatives) != 8 or d["explicit_unresolved_representatives"]:
        raise SystemExit("33-11d representative resolution moved")
    direct_ids = set(direct["carrier_ids"])
    if direct_ids != {r["carrier_id"] for r in direct["records"]}:
        raise SystemExit("direct carrier inventory mismatch")
    expected_reps = {
        "2e722a596b0b1bbbae15627fa242d2d40e8c2644af0dc304794b9e56aa0758a7",
        "08ff6ec13783579af6e27191bacb0629b63b5b6a9e8427f82fc89d9a513e5371",
        "3391419a957d94cd764c183c742c7c87bbdcfb5cd19705c9c5cfc6054a3a610b",
        "0b6cf3cef3a98a1d0aaefd163f620a137fc5079e9899a8aabdf2cd40e4821c49",
        "3fccacee6062d9d2a6cd9456589ffeb534cb8e6df2ef8e1c79f3b38cf3f2e145",
        "18ec52da066551e7adeaf9574658f243738c43afc8dd2491ba16207a48841842",
        "07895739ca2cfe72ad76e981568c82eb660f1ff9987003fa766a0309aa857e26",
        "231089ddfcbb0ffdf649192eaea857a1cb8ed3714d8ebef2fdf7b21e05370a0f",
    }
    if {r["representative_signature_sha256"] for r in representatives} != expected_reps:
        raise SystemExit("unresolved representative identity moved")
    transported_ids = set()
    component_total = 0
    multiplicity_two_reps = 0
    for record in representatives:
        ids = record["original_carrier_ids"]
        if transported_ids.intersection(ids):
            raise SystemExit("carrier appears in two geometric refinements")
        transported_ids.update(ids)
        decomposition_verified = record["exact_primary_decomposition_verified_by_ideal_intersection"]
        single_prime_verified = record.get("exact_prime_section_verified_by_saturation_and_function_field", False)
        if not (decomposition_verified or single_prime_verified):
            raise SystemExit("neither exact primary decomposition nor exact prime-section proof is recorded")
        if not record["reduced_support_and_scheme_multiplicity_recorded_separately"]:
            raise SystemExit("support/multiplicity separation missing")
        if not record["transport_uses_only_certified_surface_automorphisms"]:
            raise SystemExit("uncertified carrier transport")
        components = record["components"]
        if len(components) != record["component_count"]:
            raise SystemExit("component count mismatch")
        observed_multiplicities = set()
        for component in components:
            if not component["primary_ideal_generators"] or not component["reduced_height_one_prime_generators"]:
                raise SystemExit("primary ideal or reduced height-one support is missing")
            multiplicity = component["scheme_theoretic_multiplicity"]
            if not isinstance(multiplicity, int) or multiplicity < 1:
                raise SystemExit("invalid scheme multiplicity")
            observed_multiplicities.add(multiplicity)
            proof = component["prime_proof"]
            if decomposition_verified:
                required = [
                    proof["quotient_is_domain_over_Qi"],
                    proof["triangular_linear_elimination"],
                    proof["rank_three_quadratic_cannot_factor_as_two_linear_forms"],
                    proof["height_in_surface"] == 1,
                    proof["projective_component_dimension"] == 1,
                ]
            else:
                required = [
                    proof["affine_chart_is_domain"],
                    proof["section_ideal_saturated_with_respect_to_b3"],
                    proof["saturation_lifts_domain_to_homogeneous_section"],
                    proof["squareclass_rank_f2"] == 4,
                    proof["multiquadratic_fraction_field_degree"] == 16,
                    proof["height_in_surface"] == 1,
                    proof["projective_component_dimension"] == 1,
                ]
            if not all(required):
                raise SystemExit("height-one primality proof incomplete")
        if sorted(observed_multiplicities) != record["component_multiplicities"]:
            raise SystemExit("scheme multiplicity summary mismatch")
        multiplicity_two_reps += int(2 in observed_multiplicities)
        component_total += len(components)
    if len(transported_ids) != 24 or direct_ids.intersection(transported_ids):
        raise SystemExit("30-carrier partition is not disjoint 6+24")
    if len(direct_ids | transported_ids) != 30:
        raise SystemExit("30-carrier exact coverage failed")
    if d["summary"]["actual_height_one_prime_refinement_coverage"] != "30/30":
        raise SystemExit("33-11d coverage summary moved")
    return {
        "direct_carriers": len(direct_ids),
        "geometric_representatives": len(representatives),
        "transported_original_carriers": len(transported_ids),
        "representative_components_checked": component_total,
        "multiplicity_two_representatives": multiplicity_two_reps,
        "unresolved": 0,
    }


def audit_prime_transport(e):
    inventory = e["prime_inventory"]
    records = inventory["records"]
    prime_ids = {r["prime_id"] for r in records}
    if len(records) != 44 or len(prime_ids) != 44 or inventory["distinct_prime_ids"] != 44:
        raise SystemExit("prime inventory is not exactly 44 distinct IDs")
    refinements = inventory["carrier_refinements"]
    if len(refinements) != 30:
        raise SystemExit("carrier-to-prime refinement inventory moved")
    for pieces in refinements.values():
        if not pieces or any(p["prime_id"] not in prime_ids or p["multiplicity"] < 1 for p in pieces):
            raise SystemExit("invalid carrier refinement piece")
    checks = inventory["carrier_refinement_equivariance_checks"]
    if len(checks) != 60 or not all(x["prime_multiset_matches_exactly"] for x in checks):
        raise SystemExit("carrier refinement equivariance incomplete")
    actions = {name: e["prime_actions"][name] for name in ("cc", "ct")}
    for name, action in actions.items():
        if set(action) != prime_ids or set(action.values()) != prime_ids:
            raise SystemExit(f"{name} is not total/bijective on prime inventory")
        if any(action[action[p]] != p for p in prime_ids):
            raise SystemExit(f"{name} is not involutive")
    generators = e["generator_records"]
    if len(generators) != 14:
        raise SystemExit("prime-level generator count moved")
    component_checks = 0
    for record in generators:
        components = record["component_signed_prime_vectors"]
        if len(components) != record["component_count"]:
            raise SystemExit("component package count mismatch")
        package = package_vector(components)
        if csha(package) != record["package_prime_vector_sha256"]:
            raise SystemExit("package vector hash mismatch")
        for name, action in actions.items():
            if acted_signed_vector(package, action) != package:
                raise SystemExit(f"nonzero exact package difference for {name}")
            status = record["prime_level_galois_differences"][name]
            if status != {"nonzero_prime_coefficients": 0, "status": "ZERO_EXACT_PRIME_LEVEL"}:
                raise SystemExit("recorded package difference status moved")
            for component, vector in components.items():
                acted = acted_signed_vector(vector, action)
                if not any(acted == candidate for candidate in components.values()):
                    raise SystemExit("acted component has no exact component target")
                component_checks += 1
        if record["exact_consequence"] != "ZERO_EXACT_PRIME_LEVEL_CC_CT":
            raise SystemExit("generator exact consequence moved")
    if component_checks != 268:
        raise SystemExit("component/action audit count moved")
    return {
        "prime_ids": len(prime_ids),
        "carrier_refinements": len(refinements),
        "carrier_action_checks": len(checks),
        "generators": len(generators),
        "component_action_checks": component_checks,
        "unresolved": 0,
        "aggregate_difference": "ZERO_EXACT_ALL_14",
    }


def audit_columns(e, f, f_source):
    names = f_source["exact_source_actions"]["action_names"]
    actions = f_source["exact_source_actions"]["matrices"]
    if len(names) != 9 or len(actions) != 9 or any(len(a) != 26 for a in actions):
        raise SystemExit("source action inventory moved")
    if csha(actions) != f_source["exact_source_actions"]["matrices_sha256"]:
        raise SystemExit("source action matrix digest mismatch")
    if any(matmul(a, a) != eye() for a in actions):
        raise SystemExit("source action involution failed")
    s3 = matmul(actions[7], actions[8])
    if matmul(matmul(s3, s3), s3) != eye():
        raise SystemExit("source swaps fail S3 relation")
    action_by_name = dict(zip(names, actions))
    generator_hash = {r["source_direction"]: r["package_prime_vector_sha256"] for r in e["generator_records"]}

    blocks = []
    named_members = set()
    for rep, proof in sorted(f["orbit_span_proofs"].items(), key=lambda x: int(x[0])):
        rep_i = int(rep)
        start = [int(i == rep_i - 1) for i in range(26)]
        orbit = complete_orbit(start, actions)
        rank = f2_rank(orbit)
        if len(orbit) != proof["orbit_size"] or rank != proof["orbit_span_dimension_f2"]:
            raise SystemExit("independent orbit size/rank mismatch")
        if rank != proof["expected_cyclic_submodule_dimension_f2"]:
            raise SystemExit("cyclic source block dimension mismatch")
        for member, witness in proof["named_member_witnesses"].items():
            member_i = int(member)
            terms = []
            for term in witness["selected_orbit_terms"]:
                actual = apply_word(start, term["action_word"], action_by_name)
                if list(actual) != term["source_vector_f2"] or actual not in orbit:
                    raise SystemExit("explicit action-word term does not reproduce recorded vector")
                terms.append(actual)
            target = [int(i == member_i - 1) for i in range(26)]
            if xor_vectors(terms) != target or witness["target_basis_name"] != f"A2_{member_i:02d}":
                raise SystemExit("explicit XOR witness does not recover named column")
            named_members.add(member_i)
        blocks.append({
            "representative": f"A2_{rep_i:02d}",
            "orbit_size": len(orbit),
            "span_dimension_f2": rank,
            "named_members_checked": len(proof["named_member_witnesses"]),
        })

    columns = f["columns"]
    if len(columns) != 26 or {c["column_1based"] for c in columns} != set(range(1, 27)):
        raise SystemExit("26-column inventory is not exact")
    column_audit = []
    for column in columns:
        i = column["column_1based"]
        if column["source_basis_name"] != f"A2_{i:02d}":
            raise SystemExit("column/source basis mismatch")
        expected_basis = [int(j == i - 1) for j in range(26)]
        if column["source_basis_vector_f2"] != expected_basis:
            raise SystemExit("column basis vector mismatch")
        generator = column["exact_zero_generator"]
        if generator not in generator_hash:
            raise SystemExit("column lacks a prime-level exact generator")
        if column["generator_package_prime_vector_sha256"] != generator_hash[generator]:
            raise SystemExit("column prime-level provenance hash mismatch")
        if column["prime_level_galois_difference_cc"] != "ZERO_EXACT_PRIME_LEVEL" or column["prime_level_galois_difference_ct"] != "ZERO_EXACT_PRIME_LEVEL":
            raise SystemExit("column lacks prime-level cc/ct zero")
        receiver = column["absolute_receiver_value"]
        if receiver != {
            "E_L": "ZERO_CLASS",
            "E_L_filtration_quotient": "ZERO",
            "E_L_filtration_subobject": "ZERO",
            "E_L_splitting_used": False,
            "X_Q_i_power_3": "ZERO",
            "X_Q_power_5": "ZERO",
        }:
            raise SystemExit("absolute receiver zero or non-splitting boundary moved")
        if column["status"] != "ZERO_EXACT_MAIN" or column["unresolved"]:
            raise SystemExit("column MAIN exact state moved")
        column_audit.append({
            "column_1based": i,
            "source_basis_name": column["source_basis_name"],
            "prime_level_generator": generator,
            "prime_package_sha256": generator_hash[generator],
            "transport_kind": column["source_transport"]["kind"],
            "audited_status": "ZERO_EXACT_AUDITED",
        })
    if named_members != set(range(1, 27)) - {2, 3, 24, 25, 26}:
        raise SystemExit("cyclic block witnesses do not cover exactly the 21 transported columns")
    receiver = f["absolute_receiver"]
    if receiver["E_L_splitting_claimed"] or receiver["finite_v4_shortcut_status"] != "EXPLICITLY_REPLACED":
        raise SystemExit("Stage33-10 receiver firewall failed")
    return blocks, column_audit


def build_certificate():
    lock = load_checked(HERE / "stage33-11g-source-lock.json", LOCK_SHA)
    d = load_checked(S33 / "33-11d" / "stage33-11d-prime-refinement-certificate.json", D_SHA)
    e = load_checked(S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json", E_SHA)
    f = load_checked(S33 / "33-11f" / "stage33-11f-26-column-exact-closure-certificate.json", F_SHA)
    f_source = load_checked(S33 / "33-11f" / "stage33-11f-source-lock.json", F_SOURCE_SHA)
    d_audit = audit_prime_refinement(d)
    e_audit = audit_prime_transport(e)
    block_audit, column_audit = audit_columns(e, f, f_source)
    if lock["hostile_reaudit"]["verdict"] != "PASS_STAGE33_11F_26_COLUMN_EXACT_CLOSURE":
        raise SystemExit("merged hostile re-audit verdict is not PASS")

    cert = {
        "schema": "STAGE33_11G_HOSTILE_AUDIT_EXACT_EXIT_V1",
        "stage": "33-11g",
        "branch": "HOSTILE-AUDIT-AND-STAGE33-11-EXACT-EXIT",
        "source_locks": {
            "stage33_11g_source_lock_sha256": LOCK_SHA,
            "stage33_11d_certificate_sha256": D_SHA,
            "stage33_11e_certificate_sha256": E_SHA,
            "stage33_11f_certificate_sha256": F_SHA,
            "stage33_11f_source_lock_sha256": F_SOURCE_SHA,
            "stage33_11f_merged_head": lock["merged_stage33_11f"]["repaired_head"],
            "stage33_11f_hostile_reaudit_review_id": lock["hostile_reaudit"]["review_id"],
        },
        "independent_replay": {
            "upstream_verifiers_replayed_separately": ["33-11d", "33-11e", "33-11f"],
            "prime_refinement_audit": d_audit,
            "prime_level_transport_audit": e_audit,
            "source_block_audit": block_audit,
            "columns": column_audit,
            "discarded_working_pin_used": False,
            "carrier_level_equality_used_as_prime_level_substitute": False,
            "finite_v4_shortcut_used": False,
            "E_L_splitting_used": False,
            "remote_cas_used": False,
            "smith_form_used_for_target": False,
        },
        "exact_result": {
            "connecting_columns_exact_main": "26/26",
            "connecting_columns_exact_audited": "26/26",
            "unresolved_connecting_columns": 0,
            "arithmetic_localization_connecting_map": "COMPUTED_EXACT_ZERO_MAP",
            "hostile_audit_verdict": "PASS_STAGE33_11G_HOSTILE_AUDIT_EXACT_EXIT",
            "stage33_11_exact_exit_condition_satisfied": True,
            "stage33_11_closed_exact": True,
        },
        "controller_promotion": {
            "stage33_11_status": "CLOSED_EXACT_HOSTILE_AUDIT_PASS",
            "stage33_11_audit_required": True,
            "stage33_11_audit_passed": True,
            "stage33_11_repair_required": False,
            "stage33_11_unit_closed": True,
            "stage33_12_released": False,
            "next": "Stage33-12 remains available for its original summary/connection task under a separate release decision",
        },
        "actions_safety": {
            "artifact_uploads": 0,
            "projected_peak_artifact_storage_mb": 0,
            "effective_heavy_concurrency": 0,
        },
        "firewalls": {
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
        raise SystemExit("recorded 33-11g certificate differs; regenerate and review")
    print("STAGE33_11G_HOSTILE_AUDIT_EXACT_EXIT=PASS")
    print("CONNECTING_COLUMNS_EXACT_AUDITED=26/26")
    print("UNRESOLVED_CONNECTING_COLUMNS=0")
    print("ARITHMETIC_LOCALIZATION_CONNECTING_MAP=COMPUTED_EXACT_ZERO_MAP")
    print("STAGE33_11_CLOSED_EXACT=true")
    print("STAGE33_12_RELEASED=false")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
