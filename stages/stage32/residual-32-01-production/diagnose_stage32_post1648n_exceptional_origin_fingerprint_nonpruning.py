#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
L_PATH = HERE / "diagnose_stage32_post1648l_trace_oriented_h_coset.py"
NODE_ACTION = HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json"
INCIDENCE = HERE / "post1473-x8-marked-exceptional-incidence.json"
CZERO = HERE / "post1473-x8-marked-node-czero-partition.json"

EXPECTED_L_BLOB = "50bcc889e2edc2a3f87dfa94f877fe0a4a13f21e"
EXPECTED_NODE_ACTION = "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"
EXPECTED_INCIDENCE = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_CZERO = "96e9d9b78201e99d98b31b8ece51c3e6227a2637c35356f012d0049d589a0f42"
EXCEPTIONAL = list(range(93, 141))


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != got:
        raise SystemExit(f"canonical mismatch: {claimed} != {got}")
    return got


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


if git_blob_sha1(L_PATH) != EXPECTED_L_BLOB:
    raise SystemExit("post1648L diagnostic blob moved")
L = load_module(L_PATH, "stage32_post1648n_l")

node_action = json.loads(NODE_ACTION.read_text())
incidence = json.loads(INCIDENCE.read_text())
czero = json.loads(CZERO.read_text())
if canonical(node_action) != EXPECTED_NODE_ACTION:
    raise SystemExit("relative-H marked-node action moved")
if canonical(incidence) != EXPECTED_INCIDENCE:
    raise SystemExit("marked exceptional incidence moved")
if canonical(czero) != EXPECTED_CZERO:
    raise SystemExit("marked-node c-zero partition moved")

# Recheck that the H used by the four post1648L candidates is exactly the
# source-locked relative-H action on the 48 exceptional labels.
locked = node_action["marked_node_action"]["nonidentity_permutations_images_of_93_to_140"]
for hname in ("u", "v", "uv"):
    got = [L.H[hname][x - 1] for x in EXCEPTIONAL]
    if got != [int(x) for x in locked[hname]]:
        raise SystemExit(f"post1648L H action disagrees with marked-node source lock for {hname}")

rows = incidence["rows"]
if [int(r["exceptional_label"]) for r in rows] != EXCEPTIONAL:
    raise SystemExit("exceptional incidence row order/coverage moved")
zero_labels = {int(x) for x in czero["structure"]["c_zero_exceptional_labels"]}
nonzero_labels = {int(x) for x in czero["structure"]["c_nonzero_exceptional_labels"]}
if zero_labels | nonzero_labels != set(EXCEPTIONAL) or zero_labels & nonzero_labels:
    raise SystemExit("c-zero partition ceased to partition the 48 exceptional labels")

fingerprint = {}
pair_fibers = defaultdict(list)
for r in rows:
    x = int(r["exceptional_label"])
    pair = (int(r["first_factor_boundary_label"]), int(r["second_factor_boundary_label"]))
    pair_fibers[pair].append(x)
    fingerprint[x] = (pair[0], pair[1], x in zero_labels)
if len(pair_fibers) != 12 or any(len(v) != 4 for v in pair_fibers.values()):
    raise SystemExit("expected twelve four-node marked boundary-pair fibers")

# The source-locked H action is regular on each four-node boundary-pair fiber.
h_orbits = []
seen = set()
for x in EXCEPTIONAL:
    if x in seen:
        continue
    orbit = sorted({L.H[h][x - 1] for h in ("id", "u", "v", "uv")})
    if len(orbit) != 4:
        raise SystemExit(f"H orbit on exceptional label {x} is not regular")
    h_orbits.append(orbit)
    seen.update(orbit)
pair_fiber_sets = {tuple(sorted(v)) for v in pair_fibers.values()}
if {tuple(o) for o in h_orbits} != pair_fiber_sets:
    raise SystemExit("H-orbit partition differs from marked boundary-pair fibers")
for orbit in h_orbits:
    if len({fingerprint[x] for x in orbit}) != 1:
        raise SystemExit(f"boundary/c-zero fingerprint varies inside H orbit {orbit}")

# post1648L proved that the four trace-oriented principal-b3 lifts are one
# left and right H-coset. Check pointwise that, for every marked exceptional
# label, their four candidate images are exactly one target H orbit. Hence the
# retained boundary-pair + c-zero fingerprint is identical for all candidates.
base_name = "label18"
base = L.candidates[base_name]
point_rows = []
for x in EXCEPTIONAL:
    images = {name: p[x - 1] for name, p in L.candidates.items()}
    image_set = sorted(set(images.values()))
    base_image = base[x - 1]
    target_h_orbit = sorted({L.H[h][base_image - 1] for h in ("id", "u", "v", "uv")})
    if image_set != target_h_orbit or len(image_set) != 4:
        raise SystemExit(f"candidate image set at exceptional label {x} is not one H orbit")
    image_fingerprints = {fingerprint[y] for y in image_set}
    if len(image_fingerprints) != 1:
        raise SystemExit(f"candidate images at exceptional label {x} have distinguishable retained fingerprints")
    point_rows.append({
        "source_exceptional_label": x,
        "candidate_image_set": image_set,
        "common_target_fingerprint": list(next(iter(image_fingerprints))),
    })

result = {
    "schema": "STAGE32_POST1648N_EXCEPTIONAL_ORIGIN_FINGERPRINT_NONPRUNING_DIAGNOSTIC_V1",
    "source_locks": {
        "post1648L_git_blob_sha1": EXPECTED_L_BLOB,
        "relative_H_marked_node_action_canonical_sha256": EXPECTED_NODE_ACTION,
        "marked_exceptional_incidence_canonical_sha256": EXPECTED_INCIDENCE,
        "marked_node_czero_partition_canonical_sha256": EXPECTED_CZERO,
    },
    "exact_counts": {
        "exceptional_label_count": len(EXCEPTIONAL),
        "boundary_pair_fiber_count": len(pair_fibers),
        "nodes_per_boundary_pair_fiber": sorted({len(v) for v in pair_fibers.values()}),
        "H_orbit_count_on_exceptionals": len(h_orbits),
        "H_orbit_sizes": sorted({len(v) for v in h_orbits}),
        "trace_oriented_candidate_count": len(L.candidates),
        "exceptional_labels_checked_pointwise": len(point_rows),
    },
    "exact_nonpruning": {
        "H_orbits_equal_marked_boundary_pair_fibers": True,
        "c_zero_status_constant_on_each_H_orbit": True,
        "for_every_exceptional_label_four_candidate_images_equal_one_H_orbit": True,
        "boundary_pair_plus_czero_fingerprint_identical_across_four_candidates_for_every_exceptional_label": True,
        "retained_exceptional_incidence_breaks_H_coset_ambiguity": False,
        "retained_czero_partition_breaks_H_coset_ambiguity": False,
        "retained_incidence_plus_czero_selects_origin_section": False,
    },
    "sample_point_rows": point_rows[:6],
    "decision_boundary": {
        "principal_b3_lift_identified": False,
        "absolute_delta0inf_retained_W_line_identified": False,
        "survivors_current_credit": [73, 97, 235],
        "Q602_excluded": False,
        "O210_excluded": False,
        "O212_plus_advance_allowed": False,
        "next_exact_route": "SOURCE_BIND_AN_ABSOLUTE_EXCEPTIONAL_NODE_IMAGE_OR_OTHER_H_NONINVARIANT_ORIGIN_SECTION_UNDER_CECOTTI_B7_B8, OR MATERIALIZE_THE_DISTINGUISHED_INNER_CONJUGATING_ELEMENT / MARKED_PPAV_BASIS_CHANGE; BOUNDARY_PAIR_AND_CZERO_FINGERPRINTS_ARE_EXACTLY_H_INVARIANT",
    },
    "firewalls": {
        "all_origin_section_routes_declared_exhausted": False,
        "unregistered_node_invariant_assumed": False,
        "conditional_residue_promoted": False,
        "controller_change_authorized": False,
        "receiver_credit": False,
        "route_credit": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_credit": False,
    },
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
