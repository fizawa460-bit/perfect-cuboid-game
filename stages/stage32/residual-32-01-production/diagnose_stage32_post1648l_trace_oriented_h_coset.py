#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
E_PATH = HERE / "diagnose_stage32_post1648e_b3_boundary_weierstrass_filter.py"
MARKING_FILE = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


E = load_module(E_PATH, "stage32_post1648l_e")
marking_mod = load_module(MARKING_FILE, "stage32_post1648l_marking")
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

base_name = "label18"
base = candidates[base_name]
base_inv = E.inverse(base)
right_quotients = {}
left_quotients = {}
for name, p in candidates.items():
    # compose(a,b)=b o a.  Thus compose(base_inv,p)=p o base^-1.
    rq = E.compose(base_inv, p)
    lq = E.compose(p, base_inv)
    right_quotients[name] = h_lookup.get(tuple(rq))
    left_quotients[name] = h_lookup.get(tuple(lq))

assert set(right_quotients.values()) == {"id", "u", "v", "uv"}
assert set(left_quotients.values()) == {"id", "u", "v", "uv"}
assert all(x is not None for x in right_quotients.values())
assert all(x is not None for x in left_quotients.values())

# Check the common conjugation action on H; H-adjustment cannot distinguish it.
conjugations = {}
for cname, p in candidates.items():
    pinv = E.inverse(p)
    action = {}
    for hname, h in H.items():
        conj = E.compose(E.compose(pinv, h), p)
        action[hname] = h_lookup[tuple(conj)]
    conjugations[cname] = action
assert len({tuple(sorted(v.items())) for v in conjugations.values()}) == 1

print("POST1648L_TRACE_ORIENTED_FOUR_LIFTS_H_COSET_DIAGNOSTIC_COMPLETE")
print("candidate_words=label18:g2*g4*g3*g6,label21:g2*g3*g4*g5*g7,label19:g2*g3*g4*g5*g8,label24:g2*g3*g4*g5*g9")
print("right_H_quotients=" + ",".join(f"{k}:{v}" for k, v in sorted(right_quotients.items())))
print("left_H_quotients=" + ",".join(f"{k}:{v}" for k, v in sorted(left_quotients.items())))
print("four_candidates_form_single_left_and_right_H_coset=true")
print("common_H_conjugation=" + repr(next(iter(conjugations.values()))))
print("principal_b3_lift_still_H_ambiguous=true")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
