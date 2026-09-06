#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
E_PATH = HERE / "diagnose_stage32_post1648e_b3_boundary_weierstrass_filter.py"
L_PATH = HERE / "diagnose_stage32_post1648l_trace_oriented_h_coset.py"
POST1623 = HERE / "post1623-hperp-v6-hdeck-character-preflight.json"
MARKING_FILE = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"

EXPECTED_L_GIT_BLOB_SHA1 = "50bcc889e2edc2a3f87dfa94f877fe0a4a13f21e"
EXPECTED_POST1623_CANONICAL = "00843ec64f7ecd522614f750c9f84d3a746ce664064d1c4413784cab9d26791c"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


assert git_blob_sha1(L_PATH.read_bytes()) == EXPECTED_L_GIT_BLOB_SHA1
post1623 = json.loads(POST1623.read_text())
assert canonical(post1623) == EXPECTED_POST1623_CANONICAL
probe = post1623["exact_hdeck_probe"]["source_bound_nontrivial_character"]
assert probe["normal_curve_label_1based"] == 9
assert probe["character_name"] == "chi_u"
assert probe["profile"] == [0, 1, 0, 1]

E = load_module(E_PATH, "stage32_post1648m_e")
marking_mod = load_module(MARKING_FILE, "stage32_post1648m_marking")
marking = marking_mod.load()
perms = [[int(x) for x in p] for p in marking["aut_action"]["permutations_1based"]]
assert len(perms) == 9 and all(len(p) == 140 for p in perms)
identity = list(range(1, 141))


def word(indices):
    out = identity
    for i in indices:
        out = E.compose(out, perms[i - 1])
    return out


H = {
    "id": identity,
    "u": word((7, 9)),
    "v": word((7, 8)),
    "uv": word((8, 9)),
}
h_lookup = {tuple(v): k for k, v in H.items()}
assert len(h_lookup) == 4

candidates = {
    "label18": word((2, 4, 3, 6)),
    "label21": word((2, 3, 4, 5, 7)),
    "label19": word((2, 3, 4, 5, 8)),
    "label24": word((2, 3, 4, 5, 9)),
}
assert {p[0] for p in candidates.values()} == {18, 19, 21, 24}
assert all(E.power(p, 3) == identity for p in candidates.values())

# Recheck L's exact H-coset statement locally.
base = candidates["label18"]
base_inv = E.inverse(base)
right_q = {}
left_q = {}
for name, p in candidates.items():
    right_q[name] = h_lookup.get(tuple(E.compose(base_inv, p)))
    left_q[name] = h_lookup.get(tuple(E.compose(p, base_inv)))
assert set(right_q.values()) == {"id", "u", "v", "uv"}
assert set(left_q.values()) == {"id", "u", "v", "uv"}

source_label = 9
source_h_orbit = sorted({h[source_label - 1] for h in H.values()})
assert len(source_h_orbit) == 4

images = {name: p[source_label - 1] for name, p in candidates.items()}
assert len(set(images.values())) == 4
base_image_h_orbit = sorted({h[images["label18"] - 1] for h in H.values()})
assert sorted(images.values()) == base_image_h_orbit

# Because every candidate normalizes H with the same conjugation, the image of
# the entire distinguished source H-orbit is the same target H-orbit.
image_orbits = {}
conjugations = {}
for cname, p in candidates.items():
    pinv = E.inverse(p)
    image_orbits[cname] = sorted({p[x - 1] for x in source_h_orbit})
    action = {}
    for hname, h in H.items():
        conj = E.compose(E.compose(pinv, h), p)
        action[hname] = h_lookup[tuple(conj)]
    conjugations[cname] = action
assert len({tuple(v) for v in image_orbits.values()}) == 1
assert len({tuple(sorted(v.items())) for v in conjugations.values()}) == 1

# The source-bound post1623 datum is only the H-character direction / profile,
# not an absolute target label under the Cecotti/Bolza order-3 automorphism.
assert post1623["abstract_character_to_w_binding"]["retained_F2_4_coordinate_line_identified"] is False
assert post1623["bounded_conclusion"]["absolute_delta_0inf_retained_W_line_still_unidentified"] is True

result = {
    "schema": "STAGE32_POST1648M_LABEL9_H_COSET_NONPRUNING_DIAGNOSTIC_V1",
    "source_locks": {
        "post1648L_git_blob_sha1": EXPECTED_L_GIT_BLOB_SHA1,
        "post1623_canonical_sha256": EXPECTED_POST1623_CANONICAL,
    },
    "source_bound_probe": {
        "label": source_label,
        "character": "chi_u",
        "profile": [0, 1, 0, 1],
        "H_orbit": source_h_orbit,
    },
    "trace_oriented_candidates": {
        "candidate_label9_images": images,
        "candidate_image_set": sorted(images.values()),
        "base_image_H_orbit": base_image_h_orbit,
        "all_candidate_image_H_orbits": image_orbits,
        "common_H_conjugation": next(iter(conjugations.values())),
        "four_images_are_exactly_one_H_orbit": True,
        "all_four_transport_the_distinguished_H_orbit_to_the_same_H_orbit": True,
    },
    "decision_boundary": {
        "label9_character_probe_breaks_H_coset_ambiguity": False,
        "absolute_image_of_label9_under_named_curve_generator_source_bound": False,
        "principal_b3_member_identified": False,
        "absolute_delta0inf_retained_W_line_identified": False,
        "survivors_current_credit": [73, 97, 235],
        "Q602_excluded": False,
        "O210_excluded": False,
        "next_exact_route": "SOURCE_BIND_AN_ABSOLUTE_IMAGE_OF_A_DISTINGUISHED_LABEL_OR_ORIGIN_SECTION_UNDER_THE_CECOTTI_B7_B8_ACTION; H_CHARACTER_ORBIT_DATA_ALONE_CANNOT_SELECT_ONE_OF_THE_FOUR_H_COSET_LIFTS",
    },
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
