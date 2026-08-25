#!/usr/bin/env python3
"""Materialize every k=1,2 full-Q[4] symmetry-orbit representative exactly.

The preceding certified leaf proves that the surviving full-Q[4] sections are
whole affine fibres over 3,187 k=1 and 294 k=2 skeleton orbits.  The Burnside
leaf counts 77,076 and 303,496 full integral-symmetry orbits respectively, but
does not materialize representatives.

This leaf rebuilds the exact full-Q[4] predecessor, enumerates every surviving
affine section over each skeleton representative, applies the complete
stabilizer inside the proved order-288 integral symmetry, and writes one
canonical representative per exact orbit.  No sampling, heuristic traversal,
or finite-q filtering is used.

The binary artifact is intentionally compact.  Each record is
    <BHI = (k, skeleton_orbit_index, affine_solution_mask)
in little-endian order.  The deterministic complement/affine-coordinate
conventions are inherited from the locked predecessor scripts.
"""
import hashlib
import json
import runpy
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q4_CERT_LOCK = "cc7350ecd3a5f7d1c3eca0b96649df0fb1219283190f806ec1e537d28cbd4b19"
BURNSIDE_SCRIPT_BLOB_SHA1 = "9f3c2a0dd2da436643bc5a5b647f5384b2c68f02"
TARGET_Q_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
EXPECTED = {
    "k1": {"skeleton_orbits": 3187, "full_symmetry_orbits": 77076},
    "k2": {"skeleton_orbits": 294, "full_symmetry_orbits": 303496},
}
RECORD_STRUCT = struct.Struct("<BHI")
OUT_BIN = HERE / "nonelementary-k12-q4-symmetry-orbit-representatives.bin"
OUT_JSON = HERE / "nonelementary-k12-q4-symmetry-orbit-materialization.json"


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(data)).encode() + b"\0" + data
    ).hexdigest()


burnside_script = HERE / "profile_nonelementary_k12_q4_affine_burnside.py"
if git_blob_sha1(burnside_script) != BURNSIDE_SCRIPT_BLOB_SHA1:
    raise SystemExit("Q4 Burnside source script moved")

runpy.run_path(str(HERE / "certify_nonelementary_k12_full_q4.py"))
q4 = json.loads((HERE / "nonelementary-k12-full-q4-certified.json").read_text())
if q4.get("canonical_sha256") != Q4_CERT_LOCK:
    raise SystemExit("full-Q4 certificate moved")
if not q4.get("full_Q4_condition_certified"):
    raise SystemExit("full-Q4 predecessor is not certified")
if q4.get("combined_full_Q4_surviving_H") != 10880256:
    raise SystemExit("full-Q4 survivor total moved")

target = json.loads((HERE / "picard-discriminant-compact.json").read_text())
if target.get("canonical_sha256") != TARGET_Q_LOCK:
    raise SystemExit("endpoint finite-q source moved")

ns = runpy.run_path(str(HERE / "profile_nonelementary_k12_integral_cc_ct.py"))
canon = ns["canon"]
rank = ns["rank"]
complement = ns["complement"]
span_coordinate_map = ns["span_coordinate_map"]
section_equations = ns["section_equations"]
affine_rref = ns["affine_rref"]
stability_equations = ns["stability_equations"]
CC = ns["cc"][0]


def free_variables(reduced, nvar):
    pivots = set()
    mask_all = (1 << nvar) - 1
    for value in reduced:
        coefficient = int(value) & mask_all
        if not coefficient:
            raise SystemExit("reduced affine row lost coefficient")
        pivots.add(coefficient.bit_length() - 1)
    return tuple(i for i in range(nvar) if i not in pivots)


def solution_from_free(reduced, nvar, free_mask):
    free = free_variables(reduced, nvar)
    solution = 0
    for j, variable in enumerate(free):
        if (int(free_mask) >> j) & 1:
            solution |= 1 << variable
    mask_all = (1 << nvar) - 1
    for value in reversed(reduced):
        coefficient = int(value) & mask_all
        pivot = coefficient.bit_length() - 1
        rhs = ((int(value) >> nvar) & 1) ^ (
            (coefficient & solution).bit_count() & 1
        )
        if rhs:
            solution |= 1 << pivot
    return solution


def is_solution(reduced, nvar, solution):
    mask_all = (1 << nvar) - 1
    for value in reduced:
        coefficient = int(value) & mask_all
        rhs = (int(value) >> nvar) & 1
        if ((coefficient & int(solution)).bit_count() & 1) != rhs:
            return False
    return True


def affine_action(p_basis, w_basis, quotient_basis, quotient_coordinates,
                  permutation, transport):
    k = len(p_basis)
    wdim = len(w_basis)
    q = len(quotient_basis)
    nvar = k * q
    transported_p = tuple(transport(v, permutation) for v in p_basis)
    transported_coordinates = span_coordinate_map(transported_p)
    linear_rows = [0] * nvar
    constant_mask = 0

    for output_generator, target_p in enumerate(p_basis):
        combination = transported_coordinates.get(target_p)
        if combination is None:
            raise SystemExit("stabilizer does not preserve P")
        selected = [j for j in range(k) if (combination >> j) & 1]

        carry = 0
        for coordinate in range(14):
            total = sum(
                (transported_p[j] >> coordinate) & 1 for j in selected
            )
            target_bit = (target_p >> coordinate) & 1
            if (total - target_bit) % 2:
                raise SystemExit("binary carry parity regression")
            if ((total - target_bit) // 2) & 1:
                carry |= 1 << coordinate
        carry_q = quotient_coordinates[carry] >> wdim

        for output_bit in range(q):
            if (carry_q >> output_bit) & 1:
                constant_mask |= 1 << (q * output_generator + output_bit)

        for input_generator in selected:
            for input_bit, vector in enumerate(quotient_basis):
                transported = transport(vector, permutation)
                output_q = quotient_coordinates[transported] >> wdim
                input_variable = q * input_generator + input_bit
                for output_bit in range(q):
                    if (output_q >> output_bit) & 1:
                        linear_rows[
                            q * output_generator + output_bit
                        ] ^= 1 << input_variable

    if rank(linear_rows) != nvar:
        raise SystemExit("stabilizer affine linear part is singular")
    return tuple(linear_rows), constant_mask


def apply_affine(solution, action):
    rows, constant = action
    out = 0
    for output_bit, row in enumerate(rows):
        bit = ((int(row) & int(solution)).bit_count() & 1) ^ (
            (int(constant) >> output_bit) & 1
        )
        if bit:
            out |= 1 << output_bit
    return out


def process(label, source, source_ns, q4_part, kind):
    keep = {
        int(record["orbit_index"]): record
        for record in q4_part["surviving_orbit_records"]
    }
    if len(keep) != EXPECTED[label]["skeleton_orbits"]:
        raise SystemExit(f"{label} surviving skeleton-orbit count moved")

    symmetry = tuple(source_ns["sym"])
    transport = source_ns["transport"]
    move = source_ns["move"]
    if len(symmetry) != 288 or len(set(symmetry)) != 288:
        raise SystemExit("source symmetry order regression")

    records = []
    explicit_orbit_count = 0
    affine_sections_enumerated = 0
    stabilizer_actions_built = 0
    local_orbit_size_histogram = {}

    for skeleton_index in sorted(keep):
        representative = source["orbit_representatives"][skeleton_index]
        p_basis = tuple(map(int, representative["P_basis_bits"]))
        w_basis = tuple(map(int, representative["W_basis_bits"]))
        skeleton = (p_basis, w_basis)
        skeleton_orbit_size = int(representative["orbit_size"])
        k = len(p_basis)
        if k != kind:
            raise SystemExit("type/skeleton rank regression")

        quotient_basis = complement(
            w_basis, canon(1 << j for j in range(14))
        )
        q = len(quotient_basis)
        nvar = k * q
        reduced = affine_rref(
            section_equations(p_basis, quotient_basis)
            + stability_equations(
                p_basis, w_basis, quotient_basis, CC
            ),
            nvar,
        )
        if reduced is None:
            raise SystemExit("surviving integral affine fibre became inconsistent")
        dimension = nvar - len(reduced)
        q4_record = keep[skeleton_index]
        if dimension != int(q4_record["dimension"]):
            raise SystemExit("full-Q4 affine dimension moved")
        if int(q4_record["representative_section_survivors"]) != (1 << dimension):
            raise SystemExit("Q4 survivor is not the entire affine fibre")

        quotient_coordinates = span_coordinate_map(w_basis + quotient_basis)
        if len(quotient_coordinates) != (1 << 14):
            raise SystemExit("ambient coordinate map incomplete")
        stabilizer = [
            g for g in symmetry if move(skeleton, g) == skeleton
        ]
        if len(stabilizer) * skeleton_orbit_size != 288:
            raise SystemExit("skeleton orbit-stabilizer regression")

        actions = tuple(
            affine_action(
                p_basis, w_basis, quotient_basis, quotient_coordinates,
                g, transport,
            )
            for g in stabilizer
        )
        stabilizer_actions_built += len(actions)

        solutions = {
            solution_from_free(reduced, nvar, free)
            for free in range(1 << dimension)
        }
        if len(solutions) != (1 << dimension):
            raise SystemExit("affine solution enumeration collision")
        if any(not is_solution(reduced, nvar, x) for x in solutions):
            raise SystemExit("affine solution reconstruction failed")
        affine_sections_enumerated += len(solutions)

        unseen = set(solutions)
        local_count = 0
        while unseen:
            seed = min(unseen)
            orbit = {apply_affine(seed, action) for action in actions}
            if not orbit or not orbit <= solutions:
                raise SystemExit("stabilizer affine action left survivor fibre")
            if seed not in orbit:
                raise SystemExit("stabilizer orbit lost identity image")
            if len(stabilizer) % len(orbit):
                raise SystemExit("affine orbit size does not divide stabilizer")
            canonical = min(orbit)
            records.append((kind, skeleton_index, canonical))
            unseen.difference_update(orbit)
            local_count += 1
            local_orbit_size_histogram[len(orbit)] = (
                local_orbit_size_histogram.get(len(orbit), 0) + 1
            )

        explicit_orbit_count += local_count

    if explicit_orbit_count != EXPECTED[label]["full_symmetry_orbits"]:
        raise SystemExit(
            f"{label} explicit orbit census {explicit_orbit_count} "
            f"!= locked Burnside {EXPECTED[label]['full_symmetry_orbits']}"
        )
    return {
        "Q4_surviving_skeleton_orbits": len(keep),
        "affine_sections_enumerated_over_skeleton_representatives":
            affine_sections_enumerated,
        "stabilizer_actions_built": stabilizer_actions_built,
        "exact_full_symmetry_orbits_materialized": explicit_orbit_count,
        "local_affine_orbit_size_histogram": {
            str(k): v for k, v in sorted(local_orbit_size_histogram.items())
        },
        "records": records,
    }


out1 = process("k1", ns["k1"], ns["k1ns"], q4["k1"], 1)
out2 = process("k2", ns["k2"], ns["k2ns"], q4["k2"], 2)
all_records = out1.pop("records") + out2.pop("records")
if len(all_records) != 380572:
    raise SystemExit("combined exact orbit count regression")
if all_records != sorted(all_records):
    raise SystemExit("binary representative record order is not canonical")

with OUT_BIN.open("wb") as handle:
    for kind, skeleton_index, solution in all_records:
        handle.write(RECORD_STRUCT.pack(kind, skeleton_index, solution))
binary = OUT_BIN.read_bytes()
if len(binary) != RECORD_STRUCT.size * len(all_records):
    raise SystemExit("binary record length regression")
binary_sha256 = hashlib.sha256(binary).hexdigest()

certificate = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_Q4_SYMMETRY_ORBIT_MATERIALIZATION_V1",
    "source_full_Q4_certificate_sha256": Q4_CERT_LOCK,
    "source_Q4_burnside_script_git_blob_sha1": BURNSIDE_SCRIPT_BLOB_SHA1,
    "source_endpoint_picard_discriminant_sha256": TARGET_Q_LOCK,
    "source_integral_symmetry_order": 288,
    "k1": out1,
    "k2": out2,
    "combined_exact_full_symmetry_orbits_materialized": len(all_records),
    "locked_Burnside_combined_orbit_count": 380572,
    "explicit_orbit_materialization_matches_locked_Burnside_count": True,
    "binary_record_struct": "<BHI",
    "binary_record_fields": [
        "number_of_Z4_factors_k",
        "skeleton_orbit_index",
        "affine_solution_mask",
    ],
    "binary_record_size_bytes": RECORD_STRUCT.size,
    "binary_record_count": len(all_records),
    "binary_size_bytes": len(binary),
    "binary_sha256": binary_sha256,
    "all_surviving_affine_sections_enumerated_over_skeleton_representatives": True,
    "all_stabilizer_elements_applied": True,
    "fast_or_heuristic_traversal_used": False,
    "endpoint_finite_q_certified": False,
    "endpoint_full_action_certified": False,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf":
        "L33-07-SHARD-EXACT-ENDPOINT-FINITE-Q-PROFILES-OVER-380572-MATERIALIZED-K12-Q4-ORBITS",
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
OUT_JSON.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "k1_orbits": out1["exact_full_symmetry_orbits_materialized"],
    "k2_orbits": out2["exact_full_symmetry_orbits_materialized"],
    "combined_orbits": len(all_records),
    "binary_sha256": binary_sha256,
    "certificate_sha256": certificate["canonical_sha256"],
    "next": certificate["next_exact_leaf"],
}, indent=2, sort_keys=True))
