#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648av-canonical-coordinate-hyperplane-recovery.json"
NOTE = HERE / "post1648av-canonical-coordinate-hyperplane-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"
SUMMARY = HERE / "summarize_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"

EXPECTED_CANONICAL = "af05c0189270cefdac55daf1a4c80b3afe9766637db6fc4b2492042db2dd2fb4"
EXPECTED_NOTE_SHA256 = "4012cff211320d2b73f0a8d4ade0640b9898c837e78cae1b035a6e7caf1a050c"
EXPECTED_DIAG_BLOB = "de405c842745f07f1e84ff0379605a8d0b9eef23"
EXPECTED_SUMMARY_BLOB = "4c7b0002a1a9f2ca004acfd7d65c026dc9c01320"
EXPECTED_PROFILE_DIGEST = "072ba137f1d15285901ae150c96c694093768b036852cd7c46c1ca440a3f2096"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def replay_box_nodes(cert: dict) -> None:
    data = cert["box_node_coordinate_replay"]
    A = Matrix(data["defining_quadrics_square_coefficient_matrix"])
    if A.shape != (4, 7):
        raise ValueError("defining quadric matrix shape regression")
    names = data["coordinate_order"]
    if names != ["Z1", "Z2", "Z3", "W1", "W2", "W3", "C"]:
        raise ValueError("coordinate order regression")

    support_types = []
    zero_pairs = []
    total_points = 0
    for bits in itertools.product([0, 1], repeat=7):
        if not any(bits):
            continue
        support = [i for i, b in enumerate(bits) if b]
        As = A[:, support]
        if As.rank() >= 4:
            continue
        ns = As.nullspace()
        # Over an infinite field there is an all-nonzero vector in the nullspace
        # iff no support coordinate vanishes identically on the whole nullspace.
        has_all_nonzero = bool(ns) and all(any(v[j] != 0 for v in ns) for j in range(len(support)))
        if not has_all_nonzero:
            continue
        if len(ns) != 1 or len(support) != 4 or any(v == 0 for v in ns[0]):
            raise ValueError(f"unexpected positive-dimensional or degenerate singular support: {support}")
        support_types.append(support)
        zero = [names[j] for j in (3, 4, 5, 6) if j not in support]
        if len(zero) != 2:
            raise ValueError(f"unexpected W/C zero count: {support}, {zero}")
        zero_pairs.append(zero)
        total_points += 2 ** (len(support) - 1)

    expected_pairs = {frozenset(x) for x in data["W1_W2_W3_C_zero_pairs"]}
    if len(support_types) != 6 or {frozenset(x) for x in zero_pairs} != expected_pairs:
        raise ValueError(f"box-node zero-pair regression: {zero_pairs}")
    if total_points != 48:
        raise ValueError(f"box-node count regression: {total_points}")
    if data["singular_support_type_count"] != 6 or data["points_per_support_type"] != 8:
        raise ValueError("stored node support count regression")
    if data["total_singular_points"] != 48:
        raise ValueError("stored node total regression")
    if data["zero_coordinate_hyperplanes_per_node"] != 2 or data["nodes_per_coordinate_hyperplane"] != 24:
        raise ValueError("stored coordinate-hyperplane incidence regression")


def replay_picard_summary(cert: dict) -> None:
    p = subprocess.run([sys.executable, "-B", str(SUMMARY)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(p.stdout)
    r = cert["retained_picard_recovery"]
    if x["single_hyperplane_candidate_count"] != r["single_hyperplane_candidate_count"] != 28:
        raise ValueError("single hyperplane candidate count regression")
    if x["exact_cover_count"] != r["global_four_hyperplane_exact_cover_count"] != 25:
        raise ValueError("four-hyperplane exact cover count regression")
    if x["distinct_mass_profile_count"] != r["distinct_mass_profile_count"] != 18:
        raise ValueError("mass profile count regression")
    if x["per_hyperplane_exceptional_mass_min"] != r["per_hyperplane_exceptional_mass_min"] != 110:
        raise ValueError("minimum mass regression")
    if x["per_hyperplane_exceptional_mass_max"] != r["per_hyperplane_exceptional_mass_max"] != 168:
        raise ValueError("maximum mass regression")
    if x["all_per_hyperplane_masses_lt_186"] is not True or not r["all_per_hyperplane_exceptional_masses_strictly_below_186"]:
        raise ValueError("coordinate hyperplane mass bound regression")
    if x["every_cover_mass_sum"] != [532] or r["every_cover_exceptional_mass_sum"] != 532:
        raise ValueError("cover exceptional mass sum regression")
    if x["every_cover_normal_sum"] != [212] or r["every_cover_rational_contribution_sum"] != 212:
        raise ValueError("cover rational contribution sum regression")
    profile_digest = csha(x["mass_profiles"])
    if profile_digest != EXPECTED_PROFILE_DIGEST or r["mass_profiles_sha256"] != EXPECTED_PROFILE_DIGEST:
        raise ValueError(f"mass profile digest regression: {profile_digest}")


def main() -> None:
    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field")
    if stored != EXPECTED_CANONICAL or csha(cert) != EXPECTED_CANONICAL:
        raise ValueError("AV certificate canonical regression")
    cert["canonical_sha256_without_this_field"] = stored

    if sha256_bytes(NOTE.read_bytes()) != EXPECTED_NOTE_SHA256:
        raise ValueError("AV source note hash regression")
    if git_blob_sha1(DIAG.read_bytes()) != EXPECTED_DIAG_BLOB:
        raise ValueError("AV diagnostic blob regression")
    if git_blob_sha1(SUMMARY.read_bytes()) != EXPECTED_SUMMARY_BLOB:
        raise ValueError("AV summary blob regression")
    locks = cert["source_locks"]
    if locks["source_note_sha256"] != EXPECTED_NOTE_SHA256:
        raise ValueError("certificate source-note lock regression")
    if locks["diagnostic_blob_sha1"] != EXPECTED_DIAG_BLOB or locks["summary_blob_sha1"] != EXPECTED_SUMMARY_BLOB:
        raise ValueError("certificate replay-script lock regression")
    if locks["V6_canonical_sha256"] != "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8":
        raise ValueError("V6 source lock regression")
    if locks["AO_canonical_sha256"] != "39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378":
        raise ValueError("AO source lock regression")

    replay_box_nodes(cert)
    replay_picard_summary(cert)

    if cert["decision"]["v6_genus1_carrier_excluded"] is not False:
        raise ValueError("AV must not exclude V6")
    fw = cert["firewalls"]
    for key in ("Q602_excluded", "O210_excluded", "O212_plus_advance_allowed", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit"):
        if fw[key] is not False:
            raise ValueError(f"firewall regression: {key}")
    if fw["scratch_only"] is not True or fw["shared_MAIN_authority_changed"] is not False:
        raise ValueError("scratch/shared authority firewall regression")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AV_CANONICAL_COORDINATE_HYPERPLANE_RECOVERY",
        "canonical_sha256": EXPECTED_CANONICAL,
        "box_nodes": 48,
        "single_hyperplane_candidates": 28,
        "exact_four_hyperplane_covers": 25,
        "mass_range": [110, 168],
        "v6_carrier_excluded": False,
        "next_exact_route": cert["decision"]["next_exact_route"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
