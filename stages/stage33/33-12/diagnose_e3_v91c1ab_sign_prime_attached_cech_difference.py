#!/usr/bin/env python3
"""V91C1AB NONCREDIT actual-prime/exceptional differences for sign_a2/sign_b1.

Reuse the exact V91C1S prime namespace, literal A2_02 package source, canonical
ideal machinery, and 48 frozen exceptional nodes.  For each V91C1Z reducer
word, act the actual strict-transform primes directly and evaluate the acted
literal factors on all exceptional nodes.  This materializes the complete
codimension-one acted-minus-original divisor difference only; no Pic/2 or H2
fixedness is inferred.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = HERE / "diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py"
AA = HERE / "diagnose_e3_v91c1aa_sign_reducer_package_transport.py"
S_BLOB = "5dbe9fdc61a2663da3a2fd39e20bab130ae163b5"
AA_BLOB = "f1549d36afde2f04e6ec53b225ce5f8eb574f47c"
ACTIONS = {
    "sign_a2": ["sign_a2"],
    "sign_b1": ["sign_b1"],
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


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


assert gitblob(S.read_bytes()) == S_BLOB
assert gitblob(AA.read_bytes()) == AA_BLOB
sns = runpy.run_path(str(S))
assert sns["result"]["success"] is True
ens = sns["ens"]
variables = sns["variables"]
canonical_generators = sns["canonical_generators"]
retained_canonical_primes = sns["retained_canonical_primes"]
strict_original = sns["strict_original"]
packages = sns["packages"]
node_points = sns["node_points"]
qi = sns["qi"]
qmul = sns["qmul"]
zero = sns["zero"]
qadd = sns["qadd"]
EXPECTED_COMPONENTS = sns["EXPECTED_COMPONENTS"]


def dot(form, point):
    out = zero
    for x, y in zip(form, point):
        out = qadd(out, qmul(x, y))
    return out


def acted_atoms(package, word):
    out = []
    for factor in package["numerator_factors"]:
        sig = ens["apply_word_signature"](factor["coefficients_Qi"], word)
        out.append((sig, int(factor["exponent"])))
    den = package["denominator"]
    sig = ens["apply_word_signature"](den["coefficients_Qi"], word)
    out.append((sig, -int(den["exponent"])))
    return out


def exceptional_vector(package, word=None):
    out = {eid: 0 for eid in node_points}
    atoms = []
    if word is None:
        for factor in package["numerator_factors"]:
            atoms.append((factor["coefficients_Qi"], int(factor["exponent"])))
        den = package["denominator"]
        atoms.append((den["coefficients_Qi"], -int(den["exponent"])))
    else:
        atoms = acted_atoms(package, word)
    for sig, exponent in atoms:
        form = [qi(z) for z in sig]
        for eid, point in node_points.items():
            if dot(form, point) == zero:
                out[eid] += exponent
    return {eid: v for eid, v in sorted(out.items()) if v}


exceptional_original = {cid: exceptional_vector(pkg) for cid, pkg in packages.items()}
records = {}
for action, word in ACTIONS.items():
    prime_action = {}
    for canonical_id, generators in canonical_generators.items():
        acted_generators = [ens["apply_word_expr"](poly, word, variables) for poly in generators]
        image_id, _basis = ens["canonical_ideal"](acted_generators, variables)
        twice_generators = [ens["apply_word_expr"](poly, word, variables) for poly in acted_generators]
        twice_id, _basis2 = ens["canonical_ideal"](twice_generators, variables)
        if twice_id != canonical_id:
            raise SystemExit(f"{action} actual-prime involution failed: {canonical_id}")
        prime_action[canonical_id] = image_id

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

    exceptional_acted = {cid: exceptional_vector(pkg, word) for cid, pkg in packages.items()}
    exceptional_difference = {
        cid: subtract(exceptional_acted[cid], exceptional_original[cid])
        for cid in EXPECTED_COMPONENTS
    }
    exceptional_package_original = sum_vectors(exceptional_original.values())
    exceptional_package_acted = sum_vectors(exceptional_acted.values())
    exceptional_package_difference = subtract(exceptional_package_acted, exceptional_package_original)

    needed_strict_primes = sorted(strict_package_difference)
    acted_outside = sorted(set(prime_action.values()) - retained_canonical_primes)
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
    records[action] = {
        "word": word,
        "swap_involution_verified_on_retained_actual_primes": True,
        "acted_actual_primes_outside_retained_inventory_count": len(acted_outside),
        "acted_actual_primes_outside_retained_inventory_sha256": csha(acted_outside),
        "components_with_zero_full_attached_divisor_difference": sum(
            int(row["full_attached_divisor_difference_zero"])
            for row in component_summary.values()
        ),
        "component_differences": component_summary,
        "strict_package_difference_nonzero_coefficients": len(strict_package_difference),
        "strict_package_difference_sha256": csha(strict_package_difference),
        "exceptional_package_difference_nonzero_coefficients": len(exceptional_package_difference),
        "exceptional_package_difference_sha256": csha(exceptional_package_difference),
        "full_codim1_package_difference_zero": not strict_package_difference and not exceptional_package_difference,
        "needed_strict_prime_class_count": len(needed_strict_primes),
        "needed_strict_prime_ids": needed_strict_primes,
        "needed_strict_prime_ids_sha256": csha(needed_strict_primes),
        "pic2_difference_computed": False,
        "literal_h2_seed_fixedness_materialized": False,
    }

result = {
    "success": True,
    "marker": "V91C1AB_SIGN_PRIME_ATTACHED_CECH_DIFFERENCES",
    "actions": records,
    "component_count": len(EXPECTED_COMPONENTS),
    "exceptional_prime_count": len(node_points),
    "actual_marked_brauer_image_computed": False,
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1ab_sign_prime_attached_cech_difference.py,"
    "title=V91C1AB_SIGN_PRIME_DIFFERENCE::"
    + json.dumps(result, sort_keys=True, separators=(",", ":"))
)
