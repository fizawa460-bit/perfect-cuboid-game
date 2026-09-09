#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
E11 = HERE.parent / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
S11 = HERE.parent / "33-11e" / "stage33-11e-source-lock.json"
C2 = HERE / "e3-v91c1x-r5b3b3c4b2b2c2-lin024-actual-four-component-prime-incidence.json"
E = HERE / "e3-v91c1x-r5b3b3c4b2b2e-remaining-seven-direct-support-actual-prime-refinement.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2f-stage33-11e-actual-direct-prime-transport-replay.json"

LOCKS = {
    E11: "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426",
    S11: "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2",
    C2: "68d1be09543e79e210dc3e1e13d9f3e9cee3eb08d1b576238b5889e2a995e59f",
    E: "0b1d89e97153bacbde35865f06dda08ebdc6cbdb570719ca750ee10e2968defe",
}
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
LIN024 = "437ad2bc8c4c25e8a2078e663cbca3d5523efbdec3e06be6f2c1b8555c6c58f7"
DIRECT_KIND = "AUDITED_33_11D_DIRECT_PRIME_SUPPORT"
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    expected = LOCKS[path]
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved: {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def parse_poly(text: str, local: dict[str, sp.Expr]) -> sp.Expr:
    return sp.expand(sp.sympify(text.replace("^", "**"), locals=local))


def canonical_ideal(generators: list[sp.Expr], variables: tuple[sp.Symbol, ...]) -> tuple[str, list[str]]:
    gb = sp.groebner(generators, *variables, order="grevlex", extension=I)
    basis = [sp.srepr(sp.expand(poly.as_expr())) for poly in gb.polys]
    return csha(basis), basis


def cc_expr(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.xreplace({I: -I}))


def add_vector(out: dict[str, int], key: str, value: int) -> None:
    out[key] = out.get(key, 0) + int(value)
    if out[key] == 0:
        del out[key]


def build() -> dict:
    e11 = load(E11)
    s11 = load(S11)
    c2 = load(C2)
    e = load(E)

    if e["next_exact_leaf"] != "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_REPLAY_STAGE33_11E_GALOIS_TRANSPORT_ON_THE_24_ACTUAL_DIRECT_COMPONENT_PRIMES":
        raise SystemExit("C4B2B2E replay gate moved")
    if e["historical_direct_support_repair"]["repaired_nine_label_actual_prime_slot_count"] != 24:
        raise SystemExit("C4B2B2E 24-prime repair count moved")
    if e11["prime_inventory"]["distinct_prime_ids"] != 44:
        raise SystemExit("historical 33-11e prime inventory count moved")
    if e11["summary"]["working_generator_coverage"] != "14/14":
        raise SystemExit("historical 33-11e generator coverage moved")

    a1, a2, a3, b1, b2, b3, cv = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    local = {str(v): v for v in variables} | {"i": I}

    replacement: dict[str, list[str]] = {}
    actual_meta: dict[str, dict] = {}
    ideal_generators: dict[str, list[sp.Expr]] = {}

    def add_actual(old_id: str, carrier_id: str, direct_type: str, component: dict) -> None:
        pid = str(component["actual_prime_id"])
        gens = [parse_poly(text, local) for text in component["actual_prime_generators"]]
        rebuilt, basis = canonical_ideal(gens, variables)
        if rebuilt != pid or component["canonical_groebner_basis_sha256"] != pid:
            raise SystemExit(f"actual-prime canonical ideal moved: {pid}")
        replacement.setdefault(old_id, []).append(pid)
        if pid in actual_meta:
            raise SystemExit(f"duplicate repaired actual prime id: {pid}")
        actual_meta[pid] = {
            "prime_id": pid,
            "kind": "ACTUAL_HEIGHT_ONE_REPAIRED_DIRECT_PRIME",
            "replaces_old_pseudo_prime_id": old_id,
            "carrier_id": carrier_id,
            "direct_type": direct_type,
            "canonical_groebner_basis": basis,
        }
        ideal_generators[pid] = gens

    for row in c2["component_refinement"]["rows"]:
        add_actual(str(row["old_support_id"]), LIN024, "AXIS_B2_ZERO", row)

    for row in e["historical_direct_support_repair"]["rows"]:
        for component in row["actual_components"]:
            add_actual(str(row["old_support_id"]), str(row["carrier_id"]), str(row["direct_type"]), component)

    if len(replacement) != 9 or len(actual_meta) != 24:
        raise SystemExit(f"repaired direct replacement inventory moved: labels={len(replacement)} primes={len(actual_meta)}")
    if any(len(v) not in (2, 4) for v in replacement.values()):
        raise SystemExit("unexpected repaired component multiplicity per old support label")

    historical_records = {r["prime_id"]: r for r in e11["prime_inventory"]["records"]}
    historical_direct_ids = {pid for pid, r in historical_records.items() if r["kind"] == DIRECT_KIND}
    if historical_direct_ids != set(replacement):
        raise SystemExit("historical nine pseudo-prime ids do not match repaired replacement keys")
    retained_ids = set(historical_records) - historical_direct_ids
    if len(retained_ids) != 35:
        raise SystemExit(f"retained non-direct prime count moved: {len(retained_ids)}")
    overlap_ids = retained_ids & set(actual_meta)
    actual_only_ids = set(actual_meta) - retained_ids

    actual_cc: dict[str, str] = {}
    for pid, gens in ideal_generators.items():
        image_id, _ = canonical_ideal([cc_expr(g) for g in gens], variables)
        if image_id not in ideal_generators:
            raise SystemExit(f"cc image of repaired direct prime absent: {pid} -> {image_id}")
        actual_cc[pid] = image_id
    if any(actual_cc[actual_cc[p]] != p for p in actual_cc):
        raise SystemExit("repaired direct-prime cc action lost involutivity")

    old_cc = e11["prime_actions"]["cc"]
    old_ct = e11["prime_actions"]["ct"]
    retained_cc = {}
    retained_ct = {}
    for pid in retained_ids:
        q = old_cc[pid]
        t = old_ct[pid]
        if q not in retained_ids or t not in retained_ids:
            raise SystemExit("historical retained prime action crosses repaired direct boundary")
        retained_cc[pid] = q
        retained_ct[pid] = t

    for pid in overlap_ids:
        if actual_cc[pid] != retained_cc[pid]:
            raise SystemExit(f"cross-carrier overlap cc action mismatch: {pid}: actual={actual_cc[pid]} retained={retained_cc[pid]}")
        if retained_ct[pid] != pid:
            raise SystemExit(f"cross-carrier overlap ct action mismatch: {pid}")

    prime_cc = dict(retained_cc)
    for pid in actual_only_ids:
        prime_cc[pid] = actual_cc[pid]
    prime_ct = dict(retained_ct)
    prime_ct.update({pid: pid for pid in actual_only_ids})
    new_prime_ids = retained_ids | set(actual_meta)
    replayed_prime_count = len(new_prime_ids)
    if set(prime_cc) != new_prime_ids or set(prime_ct) != new_prime_ids:
        raise SystemExit("replayed prime action inventory incomplete")
    if any(prime_cc[prime_cc[p]] != p for p in prime_cc):
        raise SystemExit("replayed prime cc action lost involutivity")

    def replace_vector(vector: dict[str, int]) -> dict[str, int]:
        out: dict[str, int] = {}
        for pid, coeff in vector.items():
            if pid in replacement:
                for q in replacement[pid]:
                    add_vector(out, q, coeff)
            else:
                if pid not in retained_ids:
                    raise SystemExit(f"unexpected historical prime id in vector: {pid}")
                add_vector(out, pid, coeff)
        return dict(sorted(out.items()))

    def act_vector(vector: dict[str, int], action: dict[str, str]) -> dict[str, int]:
        out: dict[str, int] = {}
        for pid, coeff in vector.items():
            add_vector(out, action[pid], coeff)
        return dict(sorted(out.items()))

    old_refinements = e11["prime_inventory"]["carrier_refinements"]
    new_refinements: dict[str, list[dict]] = {}
    for carrier_id, pieces in old_refinements.items():
        out = []
        for piece in pieces:
            pid = piece["prime_id"]
            mult = int(piece["multiplicity"])
            if pid in replacement:
                out.extend({"prime_id": q, "multiplicity": mult} for q in replacement[pid])
            else:
                out.append({"prime_id": pid, "multiplicity": mult})
        new_refinements[carrier_id] = sorted(out, key=lambda r: (r["prime_id"], r["multiplicity"]))
    if len(new_refinements) != 30:
        raise SystemExit("carrier refinement coverage moved")

    target_map = {(r["action"], r["carrier_id"]): r["target_carrier_id"] for r in e11["prime_inventory"]["carrier_refinement_equivariance_checks"]}
    carrier_checks = []
    for action_name, action in (("cc", prime_cc), ("ct", prime_ct)):
        for carrier_id, pieces in sorted(new_refinements.items()):
            target_id = target_map[(action_name, carrier_id)]
            image = sorted((action[p["prime_id"]], int(p["multiplicity"])) for p in pieces)
            target = sorted((p["prime_id"], int(p["multiplicity"])) for p in new_refinements[target_id])
            if image != target:
                raise SystemExit(f"repaired {action_name} carrier refinement mismatch: {carrier_id} -> {target_id}")
            carrier_checks.append({
                "action": action_name,
                "carrier_id": carrier_id,
                "target_carrier_id": target_id,
                "prime_multiset_matches_exactly": True,
            })

    source_by_direction = {r["source_direction"]: r for r in s11["generator_records"]}
    generator_rows = []
    direct_prime_usage = set()
    for old_row in e11["generator_records"]:
        direction = old_row["source_direction"]
        source = source_by_direction[direction]
        vectors = {component: replace_vector(vector) for component, vector in old_row["component_signed_prime_vectors"].items()}
        action_checks = []
        package: dict[str, int] = {}
        for vector in vectors.values():
            for pid, coeff in vector.items():
                add_vector(package, pid, coeff)
                if pid in actual_meta:
                    direct_prime_usage.add(pid)
        package = dict(sorted(package.items()))
        differences = {}
        for action_name, action in (("cc", prime_cc), ("ct", prime_ct)):
            for component, vector in vectors.items():
                acted = act_vector(vector, action)
                candidates = source["component_galois_target_candidates"][action_name][component]
                matches = sorted(target for target in candidates if vectors[target] == acted)
                if not matches:
                    raise SystemExit(f"{direction}/{component}: no repaired prime-level {action_name} target")
                action_checks.append({
                    "action": action_name,
                    "source_component": component,
                    "matching_target_components": matches,
                    "signed_prime_vector_matches_exactly": True,
                    "source_prime_vector_sha256": csha(vector),
                    "acted_prime_vector_sha256": csha(acted),
                })
            acted_package = act_vector(package, action)
            diff = dict(acted_package)
            for pid, coeff in package.items():
                add_vector(diff, pid, -coeff)
            if diff:
                raise SystemExit(f"{direction}: repaired package {action_name}(D)-D nonzero")
            differences[action_name] = {
                "status": "ZERO_EXACT_REPAIRED_PRIME_LEVEL",
                "nonzero_prime_coefficients": 0,
            }
        generator_rows.append({
            "source_direction": direction,
            "component_count": len(vectors),
            "distinct_primes_in_package": len(package),
            "component_signed_prime_vectors": vectors,
            "action_checks": action_checks,
            "package_prime_vector_sha256": csha(package),
            "prime_level_galois_differences": differences,
            "exact_consequence": "ZERO_EXACT_REPAIRED_PRIME_LEVEL_CC_CT",
        })

    if len(generator_rows) != 14:
        raise SystemExit("repaired generator coverage moved")
    if direct_prime_usage != set(actual_meta):
        raise SystemExit(f"not all 24 repaired direct primes are consumed by 14 packages: {len(direct_prime_usage)}/24")

    records = []
    for pid in sorted(retained_ids):
        row = dict(historical_records[pid])
        if pid in overlap_ids:
            row["repair_status"] = "RETAINED_HISTORICAL_EXACT_PRIME_ALSO_REPAIRED_DIRECT_COMPONENT"
            row["repaired_direct_component_provenance"] = actual_meta[pid]
        else:
            row["repair_status"] = "RETAINED_HISTORICAL_EXACT_PRIME_UNCHANGED"
        records.append(row)
    for pid in sorted(actual_only_ids):
        records.append(actual_meta[pid])

    cert = {
        "schema": "stage33.e3.v91c1x.r5b3b3c4b2b2f.stage33_11e_actual_direct_prime_transport_replay.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2F_STAGE33_11E_ACTUAL_DIRECT_PRIME_TRANSPORT_REPLAY",
        "role": "EXACT_NONCREDIT_REPLAY_OF_HISTORICAL_STAGE33_11E_CC_CT_GALOIS_TRANSPORT_AFTER_REPLACING_NINE_NONPRIME_DIRECT_SUPPORT_LABELS_BY_TWENTY_FOUR_ACTUAL_HEIGHT_ONE_PRIMES",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "historical_stage33_11e_certificate_sha256": LOCKS[E11],
            "stage33_11e_source_lock_sha256": LOCKS[S11],
            "c4b2b2c2_lin024_actual_prime_refinement_sha256": LOCKS[C2],
            "c4b2b2e_remaining_seven_actual_prime_refinement_sha256": LOCKS[E],
        },
        "repair_inventory": {
            "historical_prime_inventory_count": 44,
            "historical_nonprime_direct_support_ids_removed": 9,
            "retained_historical_exact_prime_count": 35,
            "repaired_actual_direct_prime_count": 24,
            "direct_actual_prime_overlap_with_retained_exact_count": len(overlap_ids),
            "direct_actual_prime_overlap_with_retained_exact_ids": sorted(overlap_ids),
            "new_actual_direct_prime_ids_not_previously_in_inventory": len(actual_only_ids),
            "replayed_prime_inventory_count": replayed_prime_count,
            "all_24_actual_direct_prime_ideals_rebuilt_exactly": True,
            "all_24_actual_direct_prime_ids_pairwise_distinct": True,
            "cross_carrier_overlap_is_canonical_prime_id_equality": True,
            "cross_carrier_overlap_cc_ct_actions_agree": True,
            "old_to_actual_prime_replacement": {k: sorted(v) for k, v in sorted(replacement.items())},
            "all_24_actual_direct_primes_consumed_by_generator_packages": True,
        },
        "prime_inventory": {
            "distinct_prime_ids": replayed_prime_count,
            "records": records,
            "carrier_refinements": new_refinements,
            "carrier_refinement_equivariance_checks": carrier_checks,
        },
        "prime_actions": {
            "cc": dict(sorted(prime_cc.items())),
            "ct": dict(sorted(prime_ct.items())),
            "cc_involutive": True,
            "ct_identity_on_repaired_Qi_direct_prime_data": True,
            "actions_total_on_replayed_prime_inventory": True,
        },
        "generator_records": generator_rows,
        "summary": {
            "working_generator_coverage": "14/14",
            "carrier_prime_refinement_coverage": "30/30",
            "repaired_direct_prime_coverage": "24/24",
            "prime_level_cc_transport": "PASS_ALL_COMPONENTS_AFTER_DIRECT_PRIME_REPAIR",
            "prime_level_ct_transport": "PASS_ALL_COMPONENTS_AFTER_DIRECT_PRIME_REPAIR",
            "generator_prime_level_galois_difference": "ZERO_EXACT_ALL_14_AFTER_DIRECT_PRIME_REPAIR",
            "unresolved_prime_transports": 0,
            "historical_stage33_11e_prime_type_debt_repaired": True,
            "cross_carrier_actual_prime_incidence_reconciled": True,
            "stage33_11e_replay_status": "EXACT_REPLAY_COMPLETE_PENDING_HOSTILE_AUDIT",
            "historical_stage33_11f_26_column_closure_reuse_allowed": False,
        },
        "exact_consequence": {
            "historical_stage33_11e_prime_level_transport_replay_succeeded": True,
            "historical_stage33_11e_nonprime_direct_support_defect_repaired": True,
            "fresh_hostile_audit_required_before_reusing_stage33_11f": True,
            "authority_unchanged": True,
            "stage33_progress_unchanged": True,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_HOSTILE_AUDIT_CHECKPOINT_BEFORE_REUSING_STAGE33_11F_26_COLUMN_CLOSURE",
        "credit_firewall": {
            "authority_promotion": False,
            "authority_demotion_claim": False,
            "hostile_audit_credit": False,
            "marked_brauer_image_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_11f_reuse_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "replayed_prime_inventory_count": cert["repair_inventory"]["replayed_prime_inventory_count"],
            "repaired_direct_prime_coverage": cert["summary"]["repaired_direct_prime_coverage"],
            "generator_coverage": cert["summary"]["working_generator_coverage"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2F certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
