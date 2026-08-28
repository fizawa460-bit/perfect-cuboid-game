#!/usr/bin/env python3
"""Materialize the exact A2_26 ambient-function Galois-difference preimage.

This is the first hostile-audit repair leaf below the already certified visible
boundary V4-fixity. It deliberately stops one layer before a Gersten class:
for the four A2_26 boundary components it reconstructs the ambient rational
function as a multiset of linear numerator/denominator factors, applies the
actual cc/ct field action used by Stage33-07, and records the exact factor
orbits. The remaining datum needed for g(L)-L is then explicit: attach every
ambient hyperplane factor to its height-one prime valuation vector on the
resolved surface and solve the resulting off-boundary purity correction.

No Q-defined/V4-fixed correction is assumed. In particular this certificate
MUST NOT emit five cc/ct bits or a connecting column unless that valuation
attachment exists and is checked separately.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
SIDE = S07 / "mixed-order-side-ambient-function-lifts.json"
EXC = S07 / "mixed-order-exceptional-ambient-tangent-function-lifts.json"
DECODER = HERE / "stage33-11-a2-26-restriction-decoder.json"
BOUNDARY = HERE / "stage33-11-a2-26-ambient-boundary-galois.json"
OUT = HERE / "stage33-11-a2-26-explicit-gersten-difference-preimage.json"

LOCKS = {
    SIDE.name: "2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d",
    EXC.name: "a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397",
}
SOURCE = "A2_26"
SUPPORT = ["SIDE_021", "SIDE_022", "EXC_046", "EXC_047"]
CC_TARGET = {
    "SIDE_021": "SIDE_021",
    "SIDE_022": "SIDE_022",
    "EXC_046": "EXC_047",
    "EXC_047": "EXC_046",
}
CT_TARGET = {x: x for x in SUPPORT}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    expected = LOCKS[path.name]
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"source lock moved for {path.name}: {claimed}")
    return obj


def load_self_checked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


def qi(z):
    """Decode [real_num, real_den, imag_num, imag_den] into Q(i)."""
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qmul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c


def qinv(x):
    a, b = x
    den = a * a + b * b
    if den == 0:
        raise SystemExit("cannot invert zero Gaussian rational")
    return a / den, -b / den


def qconj(x):
    return x[0], -x[1]


def qenc(x):
    return [x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator]


def normalize_form(raw):
    vals = [qi(z) for z in raw]
    pivot = next((x for x in vals if x != (0, 0)), None)
    if pivot is None:
        raise SystemExit("zero ambient linear form")
    inv = qinv(pivot)
    return tuple(tuple(qenc(qmul(x, inv))) for x in vals)


def act_form(sig, generator):
    vals = [(Fraction(z[0], z[1]), Fraction(z[2], z[3])) for z in sig]
    if generator == "cc":
        vals = [qconj(x) for x in vals]
    elif generator != "ct":
        raise SystemExit(f"unknown generator {generator}")
    return normalize_form([qenc(x) for x in vals])


def sig_json(sig):
    return [list(z) for z in sig]


def atom(component, role, exponent, raw, source_label):
    sig = normalize_form(raw)
    return {
        "component_id": component,
        "role": role,
        "divisor_exponent": int(exponent),
        "source_label": source_label,
        "normalized_linear_form_Qi": sig_json(sig),
        "linear_form_sha256": csha(sig_json(sig)),
    }


def package_atoms(component, row, kind):
    out = []
    if kind == "side":
        for j, f in enumerate(row["numerator_factors"]):
            out.append(
                atom(
                    component,
                    "numerator",
                    int(f.get("exponent", 1)),
                    f["ambient_linear_factor_coefficients_L_basis"],
                    f"numerator_factors[{j}]/{f['edge_id']}",
                )
            )
        d = int(row["denominator"]["exponent"])
        out.append(atom(component, "denominator", -d, row["D_coefficients_L_basis"], "D"))
    elif kind == "exceptional":
        for j, f in enumerate(row["numerator_factors"]):
            out.append(
                atom(
                    component,
                    "numerator",
                    int(f.get("exponent", 1)),
                    f["ambient_tangent_linear_factor_coefficients_L_basis"],
                    f"numerator_factors[{j}]/{f['edge_id']}",
                )
            )
        d = int(row["denominator"]["exponent"])
        out.append(
            atom(
                component,
                "denominator",
                -d,
                row["ambient_projection_R0_R1_coefficients_L_basis"][1],
                "R1",
            )
        )
    else:
        raise SystemExit(f"bad package kind {kind}")
    return out


def multiset(atoms):
    counts = {}
    for a in atoms:
        key = (
            tuple(tuple(z) for z in a["normalized_linear_form_Qi"]),
            int(a["divisor_exponent"]),
        )
        counts[key] = counts.get(key, 0) + 1
    return counts


def acted_multiset(atoms, generator):
    counts = {}
    for a in atoms:
        sig = tuple(tuple(z) for z in a["normalized_linear_form_Qi"])
        gs = act_form(sig, generator)
        key = (gs, int(a["divisor_exponent"]))
        counts[key] = counts.get(key, 0) + 1
    return counts


side = load_locked(SIDE)
exc = load_locked(EXC)
decoder = load_self_checked(DECODER)
boundary = load_self_checked(BOUNDARY)
if decoder["source_direction"]["name"] != SOURCE:
    raise SystemExit("decoder source moved")
obs = decoder["decoder"]["canonical_observation_coordinates"]
if decoder["decoder"]["canonical_observation_count"] != 5 or len(obs) != 5:
    raise SystemExit("A2_26 decoder is no longer five-bit")
if boundary["source_direction"] != SOURCE or boundary["support"] != SUPPORT:
    raise SystemExit("visible boundary certificate support moved")
if not boundary["exact_checks"]["explicit_ambient_boundary_package_v4_fixed"]:
    raise SystemExit("visible boundary V4 certificate moved")

srow = next(r for r in side["source_ambient_side_lifts"] if r["source_basis_name"] == SOURCE)
erow = next(r for r in exc["source_ambient_exceptional_lifts"] if r["source_basis_name"] == SOURCE)
if int(srow["raw_order"]) != 2 or int(erow["raw_order"]) != 2:
    raise SystemExit("A2_26 raw-order2 status moved")
side_rows = {r["component_id"]: r for r in srow["side_ambient_function_lifts"]}
exc_rows = {r["component_id"]: r for r in erow["exceptional_ambient_tangent_function_lifts"]}
if sorted(side_rows) != ["SIDE_021", "SIDE_022"] or sorted(exc_rows) != ["EXC_046", "EXC_047"]:
    raise SystemExit("A2_26 four-component support moved")

atoms_by_component = {}
for cid, row in side_rows.items():
    atoms_by_component[cid] = package_atoms(cid, row, "side")
for cid, row in exc_rows.items():
    atoms_by_component[cid] = package_atoms(cid, row, "exceptional")

orbit_checks = []
for generator, target_map in (("cc", CC_TARGET), ("ct", CT_TARGET)):
    for cid in SUPPORT:
        target = target_map[cid]
        got = acted_multiset(atoms_by_component[cid], generator)
        want = multiset(atoms_by_component[target])
        if got != want:
            raise SystemExit(f"{generator}: ambient rational function mismatch {cid}->{target}")
        orbit_checks.append(
            {
                "generator": generator,
                "source_component": cid,
                "target_component": target,
                "rational_function_divisor_factor_multiset_matches": True,
            }
        )

# Inventory unique ambient hyperplane factors. These are NOT yet height-one
# primes on the resolved surface: a hyperplane section may split, acquire
# exceptional valuation, or share a component with another factor. That exact
# valuation attachment is precisely the missing hostile-audit repair datum.
unique = {}
for cid in SUPPORT:
    for a in atoms_by_component[cid]:
        h = a["linear_form_sha256"]
        rec = unique.setdefault(
            h,
            {
                "linear_form_sha256": h,
                "normalized_linear_form_Qi": a["normalized_linear_form_Qi"],
                "occurrences": [],
            },
        )
        rec["occurrences"].append(
            {
                "component_id": cid,
                "role": a["role"],
                "divisor_exponent": a["divisor_exponent"],
                "source_label": a["source_label"],
            }
        )

# Record the field-action orbit on the unique hyperplane forms themselves.
form_index = {
    tuple(tuple(z) for z in r["normalized_linear_form_Qi"]): h for h, r in unique.items()
}
form_orbits = []
for h, rec in sorted(unique.items()):
    sig = tuple(tuple(z) for z in rec["normalized_linear_form_Qi"])
    row = {"linear_form_sha256": h}
    for generator in ("cc", "ct"):
        gs = act_form(sig, generator)
        gh = form_index.get(gs)
        row[f"{generator}_image_linear_form_sha256_in_A2_26_inventory"] = gh
        row[f"{generator}_image_present_in_inventory"] = gh is not None
    form_orbits.append(row)

cert = {
    "schema": "STAGE33_11_A2_26_EXPLICIT_GERSTEN_DIFFERENCE_PREIMAGE_V1",
    "stage": "33-11",
    "branch": "33-11c_A2_26_EXPLICIT_CC_CT_GERSTEN_GALOIS_DIFFERENCE_BITS",
    "source_direction": SOURCE,
    "source_locks": {
        "mixed_order_side_ambient_function_lifts_sha256": LOCKS[SIDE.name],
        "mixed_order_exceptional_ambient_tangent_function_lifts_sha256": LOCKS[EXC.name],
        "restriction_decoder_sha256": decoder["canonical_sha256"],
        "visible_boundary_galois_sha256": boundary["canonical_sha256"],
    },
    "support": SUPPORT,
    "generator_component_action": {"cc": CC_TARGET, "ct": CT_TARGET},
    "ambient_rational_function_atoms": {cid: atoms_by_component[cid] for cid in SUPPORT},
    "ambient_rational_function_galois_checks": orbit_checks,
    "offboundary_hyperplane_factor_inventory": [unique[h] for h in sorted(unique)],
    "offboundary_hyperplane_factor_galois_orbits": form_orbits,
    "decoder_target": {
        "canonical_observation_count": 5,
        "canonical_observation_coordinates": obs,
    },
    "exact_checks": {
        "a2_26_raw_order_is_2": True,
        "four_component_support_exact": True,
        "cc_side_packages_fixed_as_rational_functions": True,
        "cc_exchanges_exceptional_046_047_as_rational_functions": True,
        "ct_fixes_all_four_ambient_rational_functions": True,
        "ambient_function_factor_divisors_compared_with_multiplicity": True,
        "no_q_defined_or_v4_fixed_offboundary_correction_assumed": True,
    },
    "repair_frontier": {
        "ambient_function_package_difference_before_purity_correction_is_zero": True,
        "height_one_prime_valuation_attachment_materialized": False,
        "offboundary_purity_correction_cochain_materialized": False,
        "actual_gersten_galois_difference_materialized": False,
        "cc_ct_five_bit_vector_materialized": False,
        "connecting_column_materialized": False,
        "exact_progress": "0/26",
        "blocker_code": "MISSING_RESOLVED_HEIGHT_ONE_VALUATION_ATTACHMENT_FOR_AMBIENT_HYPERPLANE_FACTORS",
        "why_bits_cannot_be_inferred": (
            "The ambient factor multiset is V4-stable, but Gersten residues are indexed by "
            "height-one primes of the resolved surface. The retained Stage33-07 artifacts do "
            "not decompose these ambient hyperplane factors into those primes or record their "
            "exceptional valuations. Without that map, the off-boundary purity correction "
            "torsor and g(L)-L are not defined machine-exactly; setting the five decoder bits "
            "to zero would repeat the hostile-audit error."
        ),
        "next_exact_leaf": "A2_26_ATTACH_AMBIENT_FACTORS_TO_RESOLVED_HEIGHT_ONE_VALUATIONS_AND_SOLVE_CORRECTION_TORSOR",
    },
    "firewalls": {
        "stage33_11_closed_exact": False,
        "stage33_12_released": False,
        "stage33_08_released": False,
        "stage33_07_closed": False,
        "stage33_40_plus_released": False,
        "merge_allowed": False,
        "advance_allowed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "brauer_manin_empty_claim": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "success": True,
            "source": SOURCE,
            "support": SUPPORT,
            "unique_ambient_hyperplane_factors": len(unique),
            "ambient_function_package_difference_before_purity_correction": "ZERO_EXACT",
            "actual_gersten_difference_bits": "BLOCKED_NOT_INFERRED",
            "blocker": cert["repair_frontier"]["blocker_code"],
            "exact_progress": "0/26",
            "certificate_sha256": cert["canonical_sha256"],
        },
        indent=2,
        sort_keys=True,
    )
)
