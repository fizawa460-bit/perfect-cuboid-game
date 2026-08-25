#!/usr/bin/env python3
"""Exact 2Q quadratic-value profile filter on all k=1,2 full-Q4 skeleton orbits.

The certified full-Q4/Burnside predecessor leaves 3,187 k=1 and 294 k=2
surviving skeleton orbits, carrying 380,572 full integral-symmetry orbits.
For H[2]=2W, the parity image of K=H^perp is V=W^perp.  Multiplication by 2
maps every class in K/H to 2Q, and the quadratic numerator over 8 of 2x depends
only on v=x mod 2:

    q_2Q(v) = 4*wt_X(v) + 2*wt_Y(v)  (mod 16).

Each v in W^perp occurs with constant multiplicity |W|=2^(9-k), so this gives
the complete 16,384-element 2Q value profile, not merely its support.  Because
the formula depends only on W, it is constant across every affine lift fibre
over a skeleton and is preserved by the locked order-288 source symmetry.

The endpoint profile is independently recomputed from the locked mixed-modulus
Picard discriminant matrix.  This leaf filters complete skeleton fibres and
therefore can reconstruct exact surviving H counts and exact full-symmetry
orbit counts directly from the certified Burnside records.  It does not claim
full finite-q isometry, endpoint action conjugacy, actual glue, or HS closure.
"""

import hashlib
import json
import runpy
from collections import Counter
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
BURNSIDE_SCRIPT_BLOB_SHA1 = "9f3c2a0dd2da436643bc5a5b647f5384b2c68f02"
WITNESS_SCRIPT_BLOB_SHA1 = "906daecc168a576c368431623c0b92f745462f53"
TARGET_Q_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
TARGET_MODS = [2] * 4 + [4] * 6 + [8] * 4
X_MASK = (1 << 10) - 1

# These W bases are independently extracted from the two explicit exact-Smith
# witnesses locked by WITNESS_SCRIPT_BLOB_SHA1.  They are used only to regress
# the closed-form 2Q profiler against the already-certified witness profiles.
WITNESS_W = {
    1: (8192, 4096, 2048, 1024, 340, 141, 60, 3),
    2: (8192, 4096, 2048, 1024, 48, 12, 3),
}
WITNESS_EXPECTED_2Q = {
    1: {0: 4096, 4: 4096, 8: 4096, 12: 4096},
    2: {0: 4096, 4: 4096, 8: 4096, 12: 4096},
}


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(data)).encode() + b"\0" + data
    ).hexdigest()


if git_blob_sha1(HERE / "profile_nonelementary_k12_q4_affine_burnside.py") != BURNSIDE_SCRIPT_BLOB_SHA1:
    raise SystemExit("Q4 Burnside source script moved")
if git_blob_sha1(HERE / "certify_nonelementary_exact_quotient_action_witnesses.py") != WITNESS_SCRIPT_BLOB_SHA1:
    raise SystemExit("exact-Smith witness source script moved")

# Rebuild the exact full-Q4/Burnside predecessor.  This source already locks the
# exhaustive Q4 certificate and exact F2 Burnside fixed-set computation.
burn_ns = runpy.run_path(str(HERE / "profile_nonelementary_k12_q4_affine_burnside.py"))
burn = json.loads((HERE / "nonelementary-k12-q4-affine-burnside-certified.json").read_text())
if burn.get("combined_exact_full_symmetry_orbits_after_Q4") != 380572:
    raise SystemExit("Q4 Burnside predecessor orbit count moved")
if burn.get("combined_Q4_surviving_H") != 10880256:
    raise SystemExit("Q4 Burnside predecessor H count moved")
if not burn.get("burnside_exact") or not burn.get("burnside_certified"):
    raise SystemExit("Q4 Burnside predecessor is not exact-certified")

target = json.loads((HERE / "picard-discriminant-compact.json").read_text())
if target.get("canonical_sha256") != TARGET_Q_LOCK:
    raise SystemExit("endpoint finite-q source moved")
target_B8 = [
    [-int(x) % (16 if i == j else 8) for j, x in enumerate(row)]
    for i, row in enumerate(target["discriminant_bilinear_numerator_over_8_reduced"])
]


def target_2q_profile():
    counts = Counter()
    values = [list(range(0, modulus, 2)) for modulus in TARGET_MODS]
    for vector in product(*values):
        value = sum(
            vector[i] * target_B8[i][j] * vector[j]
            for i in range(14)
            for j in range(14)
        ) % 16
        counts[value] += 1
    return dict(sorted(counts.items()))


ENDPOINT_PROFILE = target_2q_profile()
if ENDPOINT_PROFILE != {0: 8192, 8: 8192}:
    raise SystemExit(f"endpoint 2Q profile regression: {ENDPOINT_PROFILE}")


def canonical_basis(rows):
    pivots = {}
    for raw in rows:
        value = int(raw)
        for pivot in sorted(pivots, reverse=True):
            if (value >> pivot) & 1:
                value ^= pivots[pivot]
        if not value:
            continue
        pivot = value.bit_length() - 1
        for old in list(pivots):
            if (pivots[old] >> pivot) & 1:
                pivots[old] ^= value
        pivots[pivot] = value
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def nullspace_basis(rows, n=14):
    matrix = [int(x) for x in rows if int(x)]
    rank = 0
    pivot_columns = []
    for column in range(n):
        pivot = next(
            (i for i in range(rank, len(matrix)) if (matrix[i] >> column) & 1),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for i in range(len(matrix)):
            if i != rank and ((matrix[i] >> column) & 1):
                matrix[i] ^= matrix[rank]
        pivot_columns.append(column)
        rank += 1
        if rank == len(matrix):
            break

    free_columns = [c for c in range(n) if c not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = 1 << free
        for row, pivot in zip(matrix[:rank], pivot_columns):
            if (row >> free) & 1:
                vector |= 1 << pivot
        basis.append(vector)

    out = canonical_basis(basis)
    if len(out) != n - len(canonical_basis(rows)):
        raise SystemExit("F2 nullspace dimension regression")
    if any(((w & v).bit_count() & 1) for w in rows for v in out):
        raise SystemExit("F2 nullspace orthogonality regression")
    return out


def span(basis):
    values = [0]
    for row in basis:
        values += [x ^ int(row) for x in values]
    return values


def exact_2q_profile(w_basis):
    w_basis = canonical_basis(w_basis)
    v_basis = nullspace_basis(w_basis)
    parity_counts = Counter()
    for vector in span(v_basis):
        value = (4 * (vector & X_MASK).bit_count() + 2 * (vector >> 10).bit_count()) % 16
        parity_counts[value] += 1

    multiplicity = 1 << len(w_basis)
    profile = {value: count * multiplicity for value, count in sorted(parity_counts.items())}
    if sum(profile.values()) != 16384:
        raise SystemExit("2Q profile cardinality regression")
    return profile


for kind, w_basis in WITNESS_W.items():
    got = exact_2q_profile(w_basis)
    if got != WITNESS_EXPECTED_2Q[kind]:
        raise SystemExit(f"k={kind} exact-Smith witness 2Q formula regression: {got}")

ns = burn_ns["ns"]


def process(label, kind, source, burn_part):
    records = burn_part["records"]
    if len(records) != burn_part["Q4_surviving_skeleton_orbits"]:
        raise SystemExit(f"{label} Burnside record count regression")

    surviving_indices = []
    profile_histogram = Counter()
    h_before = h_after = orbit_before = orbit_after = 0

    for record in records:
        skeleton_index = int(record["skeleton_orbit_index"])
        representative = source["orbit_representatives"][skeleton_index]
        p_basis = tuple(map(int, representative["P_basis_bits"]))
        w_basis = tuple(map(int, representative["W_basis_bits"]))
        if len(p_basis) != kind or len(w_basis) != 9 - kind:
            raise SystemExit(f"{label} skeleton type regression")

        profile = exact_2q_profile(w_basis)
        signature = ",".join(f"{value}:{count}" for value, count in sorted(profile.items()))
        profile_histogram[signature] += 1

        skeleton_orbit_size = int(record["skeleton_orbit_size"])
        affine_count = int(record["Q4_surviving_affine_section_count"])
        fibre_orbits = int(record["exact_stabilizer_fibre_orbits"])
        local_h = skeleton_orbit_size * affine_count
        h_before += local_h
        orbit_before += fibre_orbits

        if set(profile) - {0, 8}:
            raise SystemExit(f"{label} Q4 survivor violated certified 2Q-support predecessor")

        if profile == ENDPOINT_PROFILE:
            surviving_indices.append(skeleton_index)
            h_after += local_h
            orbit_after += fibre_orbits

    if h_before != int(burn_part["Q4_surviving_H_reconstructed"]):
        raise SystemExit(f"{label} Q4 H reconstruction regression")
    if orbit_before != int(burn_part["exact_full_symmetry_orbits_after_Q4"]):
        raise SystemExit(f"{label} Q4 orbit reconstruction regression")

    return {
        "Q4_surviving_skeleton_orbits_before_exact_2Q_profile": len(records),
        "Q4_surviving_H_before_exact_2Q_profile": h_before,
        "full_symmetry_orbits_before_exact_2Q_profile": orbit_before,
        "skeleton_orbits_after_exact_2Q_profile": len(surviving_indices),
        "H_after_exact_2Q_profile": h_after,
        "full_symmetry_orbits_after_exact_2Q_profile": orbit_after,
        "rejected_skeleton_orbits": len(records) - len(surviving_indices),
        "rejected_H": h_before - h_after,
        "rejected_full_symmetry_orbits": orbit_before - orbit_after,
        "profile_histogram_over_Q4_surviving_skeleton_orbits": dict(sorted(profile_histogram.items())),
        "surviving_skeleton_orbit_indices": surviving_indices,
    }


out1 = process("k1", 1, ns["k1"], burn["k1"])
out2 = process("k2", 2, ns["k2"], burn["k2"])
combined_before_H = out1["Q4_surviving_H_before_exact_2Q_profile"] + out2["Q4_surviving_H_before_exact_2Q_profile"]
combined_after_H = out1["H_after_exact_2Q_profile"] + out2["H_after_exact_2Q_profile"]
combined_before_orbits = out1["full_symmetry_orbits_before_exact_2Q_profile"] + out2["full_symmetry_orbits_before_exact_2Q_profile"]
combined_after_orbits = out1["full_symmetry_orbits_after_exact_2Q_profile"] + out2["full_symmetry_orbits_after_exact_2Q_profile"]
if combined_before_H != 10880256 or combined_before_orbits != 380572:
    raise SystemExit("combined Q4 predecessor reconstruction regression")

certificate = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_EXACT_2Q_PROFILE_FILTER_V1",
    "source_Q4_burnside_script_git_blob_sha1": BURNSIDE_SCRIPT_BLOB_SHA1,
    "source_exact_Smith_witness_script_git_blob_sha1": WITNESS_SCRIPT_BLOB_SHA1,
    "source_endpoint_picard_discriminant_sha256": TARGET_Q_LOCK,
    "endpoint_exact_2Q_quadratic_value_profile_numerator_over_8": {str(k): v for k, v in ENDPOINT_PROFILE.items()},
    "source_profile_formula": "q(2x)=4*wt_X(v)+2*wt_Y(v) mod16 for v=x mod2 in W^perp",
    "source_profile_multiplicity": "|W|=2^(9-k) for every v in W^perp",
    "formula_regressed_against_two_exact_Smith_witnesses": True,
    "profile_depends_only_on_W": True,
    "complete_affine_fibres_filtered": True,
    "k1": out1,
    "k2": out2,
    "combined_Q4_surviving_H_before_exact_2Q_profile": combined_before_H,
    "combined_H_after_exact_2Q_profile": combined_after_H,
    "combined_full_symmetry_orbits_before_exact_2Q_profile": combined_before_orbits,
    "combined_full_symmetry_orbits_after_exact_2Q_profile": combined_after_orbits,
    "exact_2Q_quadratic_profile_certified": True,
    "full_finite_q_isometry_certified": False,
    "endpoint_finite_q_certified": False,
    "endpoint_full_action_certified": False,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": ("L33-07-IMPOSE-EXACT-Q2-PROFILE-ON-2Q-PROFILE-SURVIVING-K1K2-AFFINE-ORBITS" if combined_after_orbits else "L33-07-RETURN-TO-K3-AND-ELEMENTARY-RESIDUAL-AFTER-K1K2-TYPE-ELIMINATION"),
    "unit_status": "RUNNING_REPAIR",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
raw = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(HERE / "nonelementary-k12-exact-2q-profile-filter.json").write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "k1_skeletons_after": out1["skeleton_orbits_after_exact_2Q_profile"],
    "k1_orbits_after": out1["full_symmetry_orbits_after_exact_2Q_profile"],
    "k2_skeletons_after": out2["skeleton_orbits_after_exact_2Q_profile"],
    "k2_orbits_after": out2["full_symmetry_orbits_after_exact_2Q_profile"],
    "combined_H_after": combined_after_H,
    "combined_orbits_after": combined_after_orbits,
    "certificate_sha256": certificate["canonical_sha256"],
    "next": certificate["next_exact_leaf"],
}, indent=2, sort_keys=True))
