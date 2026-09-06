#!/usr/bin/env python3
"""V91C1S NONCREDIT diagnostic for the V91C1Q/R swap23 word.

Materialize acted-minus-original divisor vectors on actual strict-transform
height-one primes and all 48 resolution exceptional primes.  The acted primes
are canonicalized as ideals even when swap23 leaves the retained 30-carrier
inventory.  This deliberately does not identify the resulting Cech/Cartier
difference with zero in Pic/2 without an explicit class reduction.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
R_PATH = HERE / "diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py"
E11_PATH = S33 / "33-11e" / "verify_stage33_11e_prime_galois_transport.py"
E11_CERT = S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
E11_SOURCE = S33 / "33-11e" / "stage33-11e-source-lock.json"
D11_SOURCE = S33 / "33-11d" / "stage33-11d-source-lock.json"
NODES = S33 / "33-07" / "exceptional-p1-tangent-coordinates.json"
D_CERT = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"

E11_CERT_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
E11_SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
D11_SOURCE_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
D_CERT_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
EXPECTED_COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
WORD = ["swap12", "swap13", "swap12"]
PERM23 = [0, 2, 1, 3, 5, 4, 6]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path: Path, expected: str | None = None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert csha(body) == claimed, path
    if expected is not None:
        assert claimed == expected, path
    return obj


def add(out, key, value):
    out[key] = out.get(key, 0) + int(value)
    if out[key] == 0:
        del out[key]


def subtract(left, right):
    out = dict(left)
    for key, value in right.items():
        add(out, key, -int(value))
    return dict(sorted(out.items()))


def sum_vectors(vectors):
    out = {}
    for vector in vectors:
        for key, value in vector.items():
            add(out, key, value)
    return dict(sorted(out.items()))


# Exact coordinate word and literal package source from V91C1R.
rns = runpy.run_path(str(R_PATH))
assert rns["result"]["success"] is True
assert rns["result"]["composed_coordinate_permutation"] == PERM23
assert rns["WORD"] == WORD
packages = rns["packages"]
assert sorted(packages) == sorted(EXPECTED_COMPONENTS)

# Audited 33-11d / exact 33-11e actual-prime data.
ens = runpy.run_path(str(E11_PATH))
e11 = load_checked(E11_CERT, E11_CERT_SHA)
e11_source = load_checked(E11_SOURCE, E11_SOURCE_SHA)
d11_source = load_checked(D11_SOURCE, D11_SOURCE_SHA)
dcert = load_checked(D_CERT, D_CERT_SHA)
assert dcert["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert e11["summary"]["carrier_prime_refinement_coverage"] == "30/30"
assert e11["summary"]["unresolved_prime_transports"] == 0

inventory = {
    h: tuple(tuple(z) for z in sig)
    for h, sig in e11_source["carrier_inventory"].items()
}
by_sig = {sig: h for h, sig in inventory.items()}
assert len(inventory) == len(by_sig) == 30
perms = d11_source["certified_actions"]
assert perms["swap12"] == [1, 0, 2, 4, 3, 5, 6]
assert perms["swap13"] == [2, 1, 0, 5, 4, 3, 6]
carrier_images = {
    h: by_sig.get(ens["apply_word_signature"](sig, WORD))
    for h, sig in inventory.items()
}
missing_carrier_images = sorted(h for h, image in carrier_images.items() if image is None)

prime_records = {
    row["prime_id"]: row for row in e11["prime_inventory"]["records"]
}
variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
a1, a2v, a3, b1, b2, b3, c = variables
local = {str(x): x for x in variables} | {"i": sp.I}
Q = [
    a1**2 + a2v**2 - b3**2,
    a2v**2 + a3**2 - b1**2,
    a1**2 + a3**2 - b2**2,
    a1**2 + a2v**2 + a3**2 - c**2,
]

# Put every retained actual prime into one canonical-ideal namespace.  The
# direct-support records need their carrier equation restored first.
old_to_canonical = {}
canonical_generators = {}
for old_id, row in prime_records.items():
    if row["kind"] == "EXACT_REDUCED_PRIME_IDEAL":
        generators = [sp.sympify(text, locals=local) for text in row["canonical_groebner_basis"]]
    elif row["kind"] == "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
        carrier_sig = inventory[row["carrier_id"]]
        carrier = ens["linear_from_signature"](carrier_sig, variables)
        support = ens["parse_poly"](row["reduced_support"], local)
        generators = Q + [carrier, support]
    else:
        raise SystemExit(f"unknown prime kind: {row['kind']}")
    canonical_id, _basis = ens["canonical_ideal"](generators, variables)
    old_to_canonical[old_id] = canonical_id
    canonical_generators.setdefault(canonical_id, generators)

retained_canonical_primes = set(canonical_generators)
assert set(old_to_canonical) == set(prime_records)

# Act on each actual prime ideal directly.  Images need not belong to the old
# 30-carrier universe; they remain exact height-one primes by surface automorphism.
prime_action = {}
for canonical_id, generators in canonical_generators.items():
    acted_generators = [
        ens["apply_word_expr"](poly, WORD, variables) for poly in generators
    ]
    image_id, _basis = ens["canonical_ideal"](acted_generators, variables)
    twice = [
        ens["apply_word_expr"](poly, WORD, variables) for poly in acted_generators
    ]
    twice_id, _basis2 = ens["canonical_ideal"](twice, variables)
    if twice_id != canonical_id:
        raise SystemExit(f"swap23 actual-prime involution failed: {canonical_id}")
    prime_action[canonical_id] = image_id
acted_prime_ids = set(prime_action.values())
acted_outside_retained = sorted(acted_prime_ids - retained_canonical_primes)

# Convert A2_02's checked-in prime vectors to the canonical-ideal namespace.
a2row = next(row for row in e11["generator_records"] if row["source_direction"] == "A2_02")
raw_strict = a2row["component_signed_prime_vectors"]
assert sorted(raw_strict) == sorted(EXPECTED_COMPONENTS)
strict_original = {}
for cid, vector in raw_strict.items():
    out = {}
    for old_id, coeff in vector.items():
        add(out, old_to_canonical[old_id], coeff)
    strict_original[cid] = dict(sorted(out.items()))
strict_acted = {}
strict_difference = {}
for cid, vector in strict_original.items():
    acted = {}
    for prime_id, coeff in vector.items():
        add(acted, prime_action[prime_id], coeff)
    strict_acted[cid] = dict(sorted(acted.items()))
    strict_difference[cid] = subtract(strict_acted[cid], vector)
strict_package_original = sum_vectors(strict_original.values())
strict_package_acted = sum_vectors(strict_acted.values())
strict_package_difference = subtract(strict_package_acted, strict_package_original)

# Resolution exceptional primes: compute the swap23 permutation of all 48
# frozen node centers, then evaluate each acted literal Q(i)-linear factor.
nodes = json.loads(NODES.read_text(encoding="utf-8"))
if "canonical_sha256" in nodes:
    body = dict(nodes); claimed = body.pop("canonical_sha256")
    assert claimed == csha(body)
models = nodes["exceptional_models"]
assert len(models) == 48
qi = rns["qi"]
qmul = rns["qmul"]
zero = (Fraction(0), Fraction(0))

def qadd(x, y): return x[0] + y[0], x[1] + y[1]
def point_signature(raw):
    norm, _pivot = rns["normalize_signature"](raw)
    return tuple(tuple(z) for z in norm)

node_by_sig = {}
node_points = {}
for row in models:
    eid = row["exceptional_id"]
    raw = row["node_point_ambient_P6_L_basis"]
    sig = point_signature(raw)
    assert sig not in node_by_sig
    node_by_sig[sig] = eid
    node_points[eid] = [qi(z) for z in raw]
node_action = {}
for sig, eid in node_by_sig.items():
    acted = [list(sig[j]) for j in PERM23]
    norm, _pivot = rns["normalize_signature"](acted)
    image = node_by_sig.get(tuple(tuple(z) for z in norm))
    if image is None:
        raise SystemExit(f"swap23 exceptional node image absent: {eid}")
    node_action[eid] = image
assert all(node_action[node_action[eid]] == eid for eid in node_action)

def dot(form, point):
    out = zero
    for x, y in zip(form, point): out = qadd(out, qmul(x, y))
    return out

def atoms(package, acted=False):
    out = []
    for factor in package["numerator_factors"]:
        sig = factor["coefficients_Qi"]
        if acted: sig = [sig[j] for j in PERM23]
        out.append((sig, int(factor["exponent"])))
    den = package["denominator"]
    sig = den["coefficients_Qi"]
    if acted: sig = [sig[j] for j in PERM23]
    out.append((sig, -int(den["exponent"])))
    return out

def exceptional_vector(package, acted=False):
    out = {eid: 0 for eid in node_points}
    for sig, exponent in atoms(package, acted):
        form = [qi(z) for z in sig]
        for eid, point in node_points.items():
            if dot(form, point) == zero: out[eid] += exponent
    return {eid: v for eid, v in sorted(out.items()) if v}

exceptional_original = {cid: exceptional_vector(pkg) for cid, pkg in packages.items()}
exceptional_acted = {cid: exceptional_vector(pkg, True) for cid, pkg in packages.items()}
for cid, vector in exceptional_original.items():
    transported = {}
    for eid, coeff in vector.items(): add(transported, node_action[eid], coeff)
    if dict(sorted(transported.items())) != exceptional_acted[cid]:
        raise SystemExit(f"swap23 exceptional valuation covariance failed: {cid}")
exceptional_difference = {
    cid: subtract(exceptional_acted[cid], exceptional_original[cid])
    for cid in EXPECTED_COMPONENTS
}
exceptional_package_original = sum_vectors(exceptional_original.values())
exceptional_package_acted = sum_vectors(exceptional_acted.values())
exceptional_package_difference = subtract(exceptional_package_acted, exceptional_package_original)

component_summary = {
    cid: {
        "strict_prime_difference_nonzero_coefficients": len(strict_difference[cid]),
        "exceptional_prime_difference_nonzero_coefficients": len(exceptional_difference[cid]),
        "full_attached_divisor_difference_zero": not strict_difference[cid] and not exceptional_difference[cid],
        "strict_prime_difference_sha256": csha(strict_difference[cid]),
        "exceptional_prime_difference_sha256": csha(exceptional_difference[cid]),
    }
    for cid in EXPECTED_COMPONENTS
}
strict_package_zero = not strict_package_difference
exceptional_package_zero = not exceptional_package_difference
full_package_zero = strict_package_zero and exceptional_package_zero
full_component_zero_count = sum(
    int(row["full_attached_divisor_difference_zero"])
    for row in component_summary.values()
)
result = {
    "success": True,
    "marker": "V91C1S_SWAP23_PRIME_ATTACHED_CECH_DIFFERENCE_DIAGNOSTIC",
    "role": "EXACT_NONCREDIT_SWAP23_FULL_CODIM1_ATTACHMENT_DIAGNOSTIC",
    "q_word": WORD,
    "coordinate_permutation": PERM23,
    "retained_carrier_count": len(inventory),
    "retained_carrier_inventory_closed_under_swap23": not missing_carrier_images,
    "retained_carrier_images_missing_count": len(missing_carrier_images),
    "retained_carrier_images_missing_sha256": csha(missing_carrier_images),
    "retained_actual_prime_record_count": len(prime_records),
    "canonical_retained_actual_prime_count": len(retained_canonical_primes),
    "swap23_actual_prime_transport_materialized": True,
    "acted_actual_primes_outside_retained_inventory_count": len(acted_outside_retained),
    "acted_actual_primes_outside_retained_inventory_sha256": csha(acted_outside_retained),
    "swap23_actual_prime_involution_verified": True,
    "exceptional_node_inventory_closed_under_swap23": True,
    "exceptional_prime_count": len(node_points),
    "component_differences": component_summary,
    "components_with_zero_full_attached_divisor_difference": full_component_zero_count,
    "component_count": len(EXPECTED_COMPONENTS),
    "strict_transform_package_difference_zero": strict_package_zero,
    "exceptional_package_difference_zero": exceptional_package_zero,
    "full_codim1_package_difference_zero": full_package_zero,
    "strict_package_difference_nonzero_coefficients": len(strict_package_difference),
    "exceptional_package_difference_nonzero_coefficients": len(exceptional_package_difference),
    "strict_package_difference_sha256": csha(strict_package_difference),
    "exceptional_package_difference_sha256": csha(exceptional_package_difference),
    "prime_attached_component_difference_materialized": True,
    "pic2_cech_difference_class_computed": False,
    "a2_02_swap23_seed_fixed_mod_pic2": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
    "remaining_blocker_code": "EXPLICIT_SWAP23_CECH_CARTIER_DIFFERENCE_REDUCTION_INTO_RETAINED_PIC_OVER_2",
    "anti_inference": {
        "retained_carrier_inventory_miss_used_as_absence_proof": False,
        "zero_total_divisor_promoted_to_h2_seed_fixedness": False,
        "principal_divisor_promoted_to_cech_pic2_zero": False,
        "target_mask20_used_as_source_data": False,
        "repository_wide_absence_claim": False,
    },
    "stage33_progress": "6/11",
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py,"
    "title=V91C1S_SWAP23_PRIME_ATTACHED_CECH_DIFFERENCE::"
    + f"carrier_misses={len(missing_carrier_images)};"
    + f"new_prime_images={len(acted_outside_retained)};"
    + f"full_package_zero={str(full_package_zero).lower()};"
    + f"component_zero={full_component_zero_count}/{len(EXPECTED_COMPONENTS)};pic2=false"
)
