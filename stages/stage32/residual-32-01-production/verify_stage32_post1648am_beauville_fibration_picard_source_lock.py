#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
CERT = HERE / "post1648am-beauville-fibration-picard-source-lock.json"
NOTE = HERE / "post1648am-beauville-fibration-picard-source-note.md"
DIAG_SCRIPT = HERE / "diagnose_stage32_post1648am_beauville_fibration_picard_recovery.py"
DIAG_OUT = HERE / "post1648am-beauville-fibration-picard-recovery-diagnostic.json"
AL = HERE / "post1648al-beauville-cover-projection-genus-bound.json"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
    _parse_hperp,
)
from pairing_prefix_engine import close_permutation_group  # noqa: E402


def canonical_sha(payload: dict) -> str:
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    # Permanent context-heavy payloads are consumed runner-side only.
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def orbit_partition(indices: set[int], group: list[tuple[int, ...]]) -> list[list[int]]:
    out, unseen = [], set(indices)
    while unseen:
        seed = min(unseen)
        orb = {g[seed] for g in group}
        if not orb <= indices:
            raise ValueError("orbit leaves requested population")
        out.append(sorted(orb))
        unseen -= orb
    return sorted(out, key=lambda x: (len(x), x))


def key(v: Matrix) -> tuple[int, ...]:
    return tuple(int(v[0, j]) for j in range(v.cols))


def main() -> None:
    cert = json.loads(CERT.read_text())
    got = canonical_sha(cert)
    if got != cert["canonical_sha256_without_this_field"]:
        raise SystemExit(f"certificate canonical mismatch: {got}")

    locks = cert["source_locks"]
    if hashlib.sha256(NOTE.read_bytes()).hexdigest() != locks["source_note_sha256"]:
        raise SystemExit("AM source note hash moved")
    if git_blob_sha1(DIAG_SCRIPT.read_bytes()) != locks["am_diagnostic_script_blob_sha1"]:
        raise SystemExit("AM diagnostic script blob moved")
    if git_blob_sha1(DIAG_OUT.read_bytes()) != locks["am_diagnostic_output_blob_sha1"]:
        raise SystemExit("AM diagnostic output blob moved")

    al = json.loads(AL.read_text())
    if al["canonical_sha256_without_this_field"] != cert["parent"]["al_canonical_sha256"]:
        raise SystemExit("AL canonical moved")
    if int(al["exact_results"]["minimum_ramification_points"]) != 186:
        raise SystemExit("AL baseline ramification bound moved")

    v6 = json.loads(V6.read_text())
    if v6["canonical_sha256_without_this_field"] != locks["v6_witness_canonical_sha256"]:
        raise SystemExit("V6 witness canonical moved")
    if str(v6["target"]["row_id"]) != "g1-d186" or int(v6["target"]["d"]) != 186:
        raise SystemExit("V6 target moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(pairings) != 140:
        raise SystemExit("V6 all140 width moved")
    masses = pairings[92:]
    if masses != [int(x) for x in cert["v6_exact_inputs"]["exceptional_pairings"]]:
        raise SystemExit("V6 exceptional vector moved")
    if sum(masses) != 266 or sum(m > 0 for m in masses) != 47:
        raise SystemExit("V6 exceptional mass/support moved")

    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_am_final_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_am_final_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise SystemExit("retained Picard shapes moved")
    full = coords * gram * coords.T
    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]

    retained_idx = [i - 1 for i in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    kq = Matrix([[degrees[i] for i in retained_idx]]) * gram.inv()
    if any(x.q != 1 for x in kq):
        raise SystemExit("canonical class became nonintegral")
    K = Matrix([[int(x) for x in kq]])
    if int((K * gram * K.T)[0, 0]) != 16:
        raise SystemExit("K^2 moved")

    C = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    if int((C * gram * K.T)[0, 0]) != 186:
        raise SystemExit("K.C moved")

    group = close_permutation_group(marking["aut_action"]["permutations_1based"])
    normal_orbits = orbit_partition(set(range(92)), group)
    orbit_signature = sorted(
        (len(o), tuple(sorted({degrees[i] for i in o})), tuple(i + 1 for i in o))
        for o in normal_orbits
    )
    expected_signature = sorted([
        (32, (2,), tuple(range(1, 33))),
        (12, (4,), tuple(range(33, 45))),
        (48, (4,), tuple(range(45, 93))),
    ])
    if orbit_signature != expected_signature:
        raise SystemExit("normal-curve Aut orbit decomposition moved")

    boundary = list(range(32, 44))
    fibre_classes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    class_meta: dict[tuple[int, ...], tuple[int, int, int]] = {}
    for i in boundary:
        E = coords.row(i)
        inc = [int(full[i, j]) for j in range(92, 140)]
        if any(x < 0 for x in inc) or sum(inc) != 8 or sum(x > 0 for x in inc) != 8:
            raise SystemExit(f"boundary exceptional incidence moved at label {i+1}")
        S = Matrix([[0] * 64])
        for off, mult in enumerate(inc):
            if mult:
                S += mult * coords.row(92 + off)
        B = 2 * E + S
        kB = key(B)
        b_sq = int((B * gram * B.T)[0, 0])
        k_dot = int((B * gram * K.T)[0, 0])
        c_dot = int((C * gram * B.T)[0, 0])
        if b_sq != 0 or k_dot != 8:
            raise SystemExit(f"boundary fibre numerical type moved at label {i+1}")
        fibre_classes[kB].append(i + 1)
        class_meta[kB] = (b_sq, k_dot, c_dot)

    if len(fibre_classes) != 2:
        raise SystemExit("boundary fibres no longer collapse to two classes")
    rows = []
    for kB, labels in fibre_classes.items():
        b_sq, k_dot, c_dot = class_meta[kB]
        rows.append((c_dot, tuple(labels), b_sq, k_dot, kB))
    rows.sort()
    expected_rows = [
        (81, (33, 36, 37, 40, 41, 44), 0, 8),
        (105, (34, 35, 38, 39, 42, 43), 0, 8),
    ]
    if [(x[0], x[1], x[2], x[3]) for x in rows] != expected_rows:
        raise SystemExit("retained 6+6 fibre partition/intersections moved")

    B81 = Matrix([list(rows[0][4])])
    B105 = Matrix([list(rows[1][4])])
    if B81 + B105 != K:
        raise SystemExit("B81+B105 != K")
    if int((B81 * gram * B105.T)[0, 0]) != 8:
        raise SystemExit("B81.B105 moved")

    diag = json.loads(DIAG_OUT.read_text())
    relation = diag["beauville_two_fibre_relation"]
    if not relation["B1_plus_B2_equals_K"] or int(relation["B1_dot_B2"]) != 8:
        raise SystemExit("locked AM diagnostic relation moved")
    if sorted([int(relation["n1"]), int(relation["n2"])]) != [81, 105]:
        raise SystemExit("locked AM diagnostic candidate degrees moved")
    if not bool(diag["source_geometry_relation_required_for_n_identification"]):
        raise SystemExit("AM diagnostic firewall moved")

    semantic = cert["source_geometry_adapter"]
    if (
        semantic["factor_directions"] != 2
        or semantic["satake_boundary_elliptic_count"] != 12
        or semantic["boundary_elliptics_per_direction"] != 6
        or semantic["singular_cusps_per_boundary_elliptic"] != 8
        or semantic["special_fibre_class_formula"] != "F_E=2*E+sum(8 incident exceptional curves)"
        or semantic["projection_formula"] != "n_i=C.F_i"
    ):
        raise SystemExit("source-geometry adapter contract moved")

    nvals = sorted([rows[0][0], rows[1][0]])
    if nvals != [81, 105] or sum(nvals) != 186:
        raise SystemExit("semantic projection degrees moved")
    if cert["retained_picard_replay"]["projection_degrees_unordered"] != nvals:
        raise SystemExit("certificate projection degrees stale")

    min_r = 2 * max(nvals)
    max_r = sum(masses)
    min_genus = 1 + min_r // 2
    baseline_odd = sum(m & 1 for m in masses)
    increments = sorted((m - (m & 1) for m in masses if m > 1), reverse=True)

    cumulative = baseline_odd
    min_multibranch = 0
    for inc in increments:
        if cumulative >= min_r:
            break
        cumulative += inc
        min_multibranch += 1
    if cumulative < min_r:
        raise SystemExit("exceptional capacity cannot attain AM lower bound")

    top18 = sum(increments[:18])
    top19 = sum(increments[:19])
    cap18 = baseline_odd + top18
    cap19 = baseline_odd + top19
    expected_results = {
        "minimum_ramification_points": min_r,
        "maximum_ramification_points_from_exceptional_mass": max_r,
        "minimum_lift_genus": min_genus,
        "minimum_total_normalization_preimages_over_met_surface_nodes": min_r,
        "minimum_normalization_branch_excess_over_47_met_nodes": min_r - 47,
        "odd_mass_unibranch_ramification_capacity": baseline_odd,
        "largest_18_multibranch_capacity_increment_sum": top18,
        "ramification_capacity_with_at_most_18_multibranch_nodes": cap18,
        "largest_19_multibranch_capacity_increment_sum": top19,
        "ramification_capacity_with_19_multibranch_nodes": cap19,
        "minimum_distinct_multibranch_surface_nodes": min_multibranch,
    }
    for k, v in expected_results.items():
        if cert["exact_results"][k] != v:
            raise SystemExit(f"{k} moved: cert={cert['exact_results'][k]} replay={v}")
    if not (cap18 < min_r <= cap19 and min_multibranch == 19):
        raise SystemExit("AM multibranch threshold moved")
    if min_r <= int(al["exact_results"]["minimum_ramification_points"]):
        raise SystemExit("AM failed to strengthen AL ramification bound")

    if any(cert["firewalls"].values()):
        raise SystemExit("AM credit firewall moved")
    guards = cert["guardrails"]
    if not all(guards.values()):
        raise SystemExit("AM guardrail moved")
    if cert["decision"]["v6_carrier_excluded"]:
        raise SystemExit("AM must remain a necessary-condition leaf")

    print("PASS_STAGE32_POST1648AM_BEAUVILLE_FIBRATION_PICARD_SOURCE_LOCK")
    print(cert["canonical_sha256_without_this_field"])
    print(json.dumps({
        "projection_degrees_unordered": nvals,
        "minimum_ramification_points": min_r,
        "minimum_distinct_multibranch_surface_nodes": min_multibranch,
        "minimum_total_node_preimages": min_r,
        "minimum_branch_excess": min_r - 47,
        "minimum_lift_genus": min_genus,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
