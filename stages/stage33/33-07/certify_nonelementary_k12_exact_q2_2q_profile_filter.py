#!/usr/bin/env python3
"""Exact endpoint-Q[2] profile filter on k1/k2 full-Q4 symmetry representatives.

Input:
* a retained exact 2Q-profile certificate, which filters whole skeleton fibres;
* the exact v1 full-Q4 materialization binary (<BHI), one representative per
  full order-288 source-symmetry orbit.

For H <= (Z/4)^14, write a normalized H element as y=low+2*high.  For one
chosen half in A0=(Z/8)^10+(Z/16)^4 the quotient quadratic numerator over 8 is

    sum_X y_i^2 + 2*sum_Y y_i^2  (mod 16).

All 2^14 halves differ by ambient two-torsion.  If low_X != 0, half of those
choices add 8; if low_X=0, all have the same numerator.  Enumerating the <=4
P parity cosets and the complete W high-bit plane therefore gives the complete
16,384-element Q[2] value profile exactly.

This is still only a necessary finite-q invariant.  Matching Q[2] and 2Q
profiles does not certify finite quadratic-module isometry, endpoint action
conjugacy, actual glue, Hochschild-Serre closure, or any theorem endpoint.
"""
import hashlib
import itertools
import json
import runpy
import struct
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

TARGET_Q_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
Q4_MATERIALIZATION_BINARY_SHA256 = "15b21b405da16908ec1cc2daa275cb1016b35c1618975a1bf450e6f78469eccd"
Q4_MATERIALIZATION_RECORD_COUNT = 380572
Q4_MATERIALIZATION_CERT_SHA256 = "65fd651b785099892548bc1f43a6bf08c523a749ff7f78f19cbd0de0434ffd84"
TWOQ_CERT_SHA256 = "00385fb56ae07a8ce8ce20f374297a88fa98257bb13dd9e6d80ccc6aca4f8f5f"
K1_SCRIPT_BLOB_SHA1 = "21ea4897bbec5d6fef8c7615edf90d23ee786949"
K2_SCRIPT_BLOB_SHA1 = "09f46fe93fb5cafbd8ec769bac6cb3af9ebe23f4"

RECORD = struct.Struct("<BHI")
IN_TWOQ = HERE / "nonelementary-k12-exact-2q-profile-filter.json"
IN_BIN = HERE / "nonelementary-k12-q4-symmetry-orbit-representatives.bin"
OUT_JSON = HERE / "nonelementary-k12-exact-q2-2q-profile-filter.json"
OUT_BIN = HERE / "nonelementary-k12-exact-q2-2q-profile-surviving-orbits.bin"
X_MASK = (1 << 10) - 1
Y_MASK = ((1 << 14) - 1) ^ X_MASK


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


if git_blob_sha1(HERE / "certify_nonelementary_k1_q2_2q_cc_orbits.py") != K1_SCRIPT_BLOB_SHA1:
    raise SystemExit("k1 skeleton source script moved")
if git_blob_sha1(HERE / "certify_nonelementary_k2_q2_2q_skeleton_orbits.py") != K2_SCRIPT_BLOB_SHA1:
    raise SystemExit("k2 skeleton source script moved")

twoq = json.loads(IN_TWOQ.read_text())
stored = twoq.get("canonical_sha256")
unsigned = dict(twoq)
unsigned.pop("canonical_sha256", None)
rehash = hashlib.sha256(
    json.dumps(unsigned, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
if stored != rehash or stored != TWOQ_CERT_SHA256:
    raise SystemExit("2Q-profile retained certificate hash regression")
if not twoq.get("exact_2Q_quadratic_profile_certified"):
    raise SystemExit("2Q-profile predecessor is not exact-certified")
if twoq.get("endpoint_finite_q_certified"):
    raise SystemExit("2Q predecessor crossed finite-q firewall")

binary = IN_BIN.read_bytes()
if hashlib.sha256(binary).hexdigest() != Q4_MATERIALIZATION_BINARY_SHA256:
    raise SystemExit("Q4 materialization binary moved")
if len(binary) != Q4_MATERIALIZATION_RECORD_COUNT * RECORD.size:
    raise SystemExit("Q4 materialization record-count regression")

# Rebuild only the cheap skeleton sources.  This avoids rebuilding the
# 28-minute full-Q4/Burnside predecessor.
runpy.run_path(str(HERE / "certify_nonelementary_k1_q2_2q_cc_orbits.py"))
runpy.run_path(str(HERE / "certify_nonelementary_k2_q2_2q_skeleton_orbits.py"))
sources = {
    "k1": json.loads((HERE / "nonelementary-k1-q2-2q-cc-orbits.json").read_text()),
    "k2": json.loads((HERE / "nonelementary-k2-q2-2q-skeleton-orbits.json").read_text()),
}

target = json.loads((HERE / "picard-discriminant-compact.json").read_text())
if target.get("canonical_sha256") != TARGET_Q_LOCK:
    raise SystemExit("endpoint finite-q source moved")
mods = list(map(int, target["discriminant_moduli"]))
raw_b = target["discriminant_bilinear_numerator_over_8_reduced"]
target_b = [
    [-int(x) % (16 if i == j else 8) for j, x in enumerate(row)]
    for i, row in enumerate(raw_b)
]


def target_q2_profile():
    profile = Counter()
    for vector in itertools.product(*[[0, modulus // 2] for modulus in mods]):
        value = sum(
            vector[i] * target_b[i][j] * vector[j]
            for i in range(14)
            for j in range(14)
        ) % 16
        profile[value] += 1
    return dict(sorted(profile.items()))


TARGET_PROFILE = target_q2_profile()
if TARGET_PROFILE != {0: 8192, 8: 8192}:
    raise SystemExit(f"endpoint Q2 profile regression: {TARGET_PROFILE}")


def canon(rows):
    pivots = {}
    for raw in rows:
        row = int(raw)
        for pivot in sorted(pivots, reverse=True):
            if (row >> pivot) & 1:
                row ^= pivots[pivot]
        if not row:
            continue
        pivot = row.bit_length() - 1
        for old in list(pivots):
            if (pivots[old] >> pivot) & 1:
                pivots[old] ^= row
        pivots[pivot] = row
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def complement(base, whole):
    current = list(canon(base))
    out = []
    for vector in canon(whole):
        after = canon(current + [vector])
        if len(after) > len(canon(current)):
            current.append(vector)
            out.append(vector)
    return tuple(out)


def span(basis):
    out = [0]
    for row in basis:
        out += [x ^ int(row) for x in out]
    return tuple(out)


def qnum_half(low, high):
    lx = int(low) & X_MASK
    ly = (int(low) & Y_MASK) >> 10
    hx = int(high) & X_MASK
    hy = (int(high) & Y_MASK) >> 10
    return (
        lx.bit_count()
        + 4 * hx.bit_count()
        + 4 * (lx & hx).bit_count()
        + 2 * ly.bit_count()
        + 8 * hy.bit_count()
        + 8 * (ly & hy).bit_count()
    ) % 16


def order4_corrections(p_basis, quotient_basis, solution):
    q = len(quotient_basis)
    out = []
    for generator in range(len(p_basis)):
        correction = 0
        for bit, vector in enumerate(quotient_basis):
            if (int(solution) >> (q * generator + bit)) & 1:
                correction ^= int(vector)
        out.append(correction)
    return tuple(out)


def selected_bitplanes(p_basis, corrections, selection):
    low = 0
    high = 0
    for i, p in enumerate(p_basis):
        if (int(selection) >> i) & 1:
            high ^= int(corrections[i]) ^ (low & int(p))
            low ^= int(p)
    return low, high


structure_cache = {}
coset_profile_cache = {}


def structure(label, skeleton_index):
    key = (label, int(skeleton_index))
    if key in structure_cache:
        return structure_cache[key]
    rep = sources[label]["orbit_representatives"][int(skeleton_index)]
    p_basis = tuple(map(int, rep["P_basis_bits"]))
    w_basis = tuple(map(int, rep["W_basis_bits"]))
    quotient_basis = complement(w_basis, canon(1 << j for j in range(14)))
    w_elements = span(w_basis)
    kind = int(label[-1])
    if len(p_basis) != kind or len(w_basis) != 9 - kind:
        raise SystemExit("skeleton type regression")
    item = (p_basis, w_basis, quotient_basis, w_elements)
    structure_cache[key] = item
    return item


def coset_units(label, skeleton_index, low, high0, w_elements):
    key = (label, int(skeleton_index), int(low), int(high0))
    if key in coset_profile_cache:
        return coset_profile_cache[key]
    units = Counter()
    odd_x = bool(int(low) & X_MASK)
    for w in w_elements:
        value = qnum_half(low, int(high0) ^ int(w))
        if odd_x:
            units[value] += 1
            units[(value + 8) % 16] += 1
        else:
            units[value] += 2
    coset_profile_cache[key] = units
    return units


def source_q2_profile(label, skeleton_index, solution):
    p_basis, _, quotient_basis, w_elements = structure(label, skeleton_index)
    corrections = order4_corrections(p_basis, quotient_basis, solution)
    units = Counter()
    for selection in range(1 << len(p_basis)):
        low, high0 = selected_bitplanes(p_basis, corrections, selection)
        units.update(coset_units(label, skeleton_index, low, high0, w_elements))
    if sum(units.values()) != 1024:
        raise SystemExit("Q2 half-count unit regression")
    profile = {value: 16 * count for value, count in sorted(units.items())}
    if sum(profile.values()) != 16384:
        raise SystemExit("Q2 profile cardinality regression")
    return profile


keep = {
    1: set(map(int, twoq["k1"]["surviving_skeleton_orbit_indices"])),
    2: set(map(int, twoq["k2"]["surviving_skeleton_orbit_indices"])),
}
expected_input_orbits = {
    1: int(twoq["k1"]["full_symmetry_orbits_after_exact_2Q_profile"]),
    2: int(twoq["k2"]["full_symmetry_orbits_after_exact_2Q_profile"]),
}

records_seen = Counter()
passing = Counter()
profile_hist = {"k1": Counter(), "k2": Counter()}
with OUT_BIN.open("wb") as handle:
    for offset in range(0, len(binary), RECORD.size):
        kind, skeleton_index, solution = RECORD.unpack_from(binary, offset)
        if skeleton_index not in keep.get(kind, set()):
            continue
        label = f"k{kind}"
        records_seen[kind] += 1
        profile = source_q2_profile(label, skeleton_index, solution)
        signature = ",".join(f"{k}:{v}" for k, v in sorted(profile.items()))
        profile_hist[label][signature] += 1
        if profile == TARGET_PROFILE:
            handle.write(RECORD.pack(kind, skeleton_index, solution))
            passing[kind] += 1

for kind in (1, 2):
    if records_seen[kind] != expected_input_orbits[kind]:
        raise SystemExit(
            f"k{kind} 2Q-survivor materialization coverage regression: "
            f"{records_seen[kind]} != {expected_input_orbits[kind]}"
        )

filtered = OUT_BIN.read_bytes()
filtered_sha256 = hashlib.sha256(filtered).hexdigest()
if len(filtered) != RECORD.size * sum(passing.values()):
    raise SystemExit("Q2 filtered binary framing regression")

certificate = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_EXACT_Q2_2Q_PROFILE_FILTER_V1",
    "source_2Q_profile_certificate_sha256": TWOQ_CERT_SHA256,
    "source_Q4_materialization_certificate_sha256": Q4_MATERIALIZATION_CERT_SHA256,
    "source_Q4_materialization_binary_sha256": Q4_MATERIALIZATION_BINARY_SHA256,
    "source_Q4_materialization_record_count": Q4_MATERIALIZATION_RECORD_COUNT,
    "source_k1_skeleton_script_git_blob_sha1": K1_SCRIPT_BLOB_SHA1,
    "source_k2_skeleton_script_git_blob_sha1": K2_SCRIPT_BLOB_SHA1,
    "source_k1_skeleton_certificate_sha256": sources["k1"]["canonical_sha256"],
    "source_k2_skeleton_certificate_sha256": sources["k2"]["canonical_sha256"],
    "source_endpoint_picard_discriminant_sha256": TARGET_Q_LOCK,
    "endpoint_Q2_quadratic_value_profile_numerator_over_8": {
        str(k): v for k, v in TARGET_PROFILE.items()
    },
    "k1": {
        "2Q_surviving_skeleton_orbits": len(keep[1]),
        "exact_full_symmetry_orbits_before_Q2_profile": records_seen[1],
        "exact_full_symmetry_orbits_matching_endpoint_Q2_and_2Q_profiles": passing[1],
        "Q2_profile_histogram_by_full_symmetry_orbit": dict(sorted(profile_hist["k1"].items())),
    },
    "k2": {
        "2Q_surviving_skeleton_orbits": len(keep[2]),
        "exact_full_symmetry_orbits_before_Q2_profile": records_seen[2],
        "exact_full_symmetry_orbits_matching_endpoint_Q2_and_2Q_profiles": passing[2],
        "Q2_profile_histogram_by_full_symmetry_orbit": dict(sorted(profile_hist["k2"].items())),
    },
    "combined_exact_full_symmetry_orbits_matching_endpoint_Q2_and_2Q_profiles":
        passing[1] + passing[2],
    "filtered_binary_record_struct": "<BHI",
    "filtered_binary_record_count": passing[1] + passing[2],
    "filtered_binary_size_bytes": len(filtered),
    "filtered_binary_sha256": filtered_sha256,
    "exact_Q2_quadratic_profile_certified": True,
    "exact_2Q_quadratic_profile_inherited_certified": True,
    "weighted_H_after_Q2_profile_certified": False,
    "endpoint_finite_q_certified": False,
    "endpoint_full_action_certified": False,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf":
        "L33-07-CLASSIFY-FULL-FINITE-Q-ISOMETRY-ON-Q2-2Q-PROFILE-SURVIVORS",
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
    "k1_input_orbits": records_seen[1],
    "k2_input_orbits": records_seen[2],
    "k1_passing_orbits": passing[1],
    "k2_passing_orbits": passing[2],
    "combined_passing_orbits": passing[1] + passing[2],
    "filtered_binary_sha256": filtered_sha256,
    "certificate_sha256": certificate["canonical_sha256"],
    "next": certificate["next_exact_leaf"],
}, indent=2, sort_keys=True))
