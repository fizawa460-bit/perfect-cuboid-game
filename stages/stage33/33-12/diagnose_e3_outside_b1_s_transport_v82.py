#!/usr/bin/env python3
"""Bounded exact-interface diagnostic for S:B1->B3 transport.

No Brauer/Gysin column is granted.  This probe verifies whether the retained
140 known-curve Hperp block has enough rank to reconstruct the exact Stoll
S=g2*g5 action, including the sign component missing from pure swap13.
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
S07 = HERE.parent / "33-07"
S09 = HERE.parent / "33-09"
S32 = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(S07))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

ADAPTER = S32 / "post1529-fsm-stoll-diagonal-action-source-lock.json"
BRIDGE = S09 / "marked-picard-basis-bridge-certified.json"
MARKING_SHA = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
ADAPTER_SHA = "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"
BRIDGE_BLOB = "77b16e2ee80c33af27f7a5a04e1c465e9fc1acea"
PRIME = 1000003


def csha(obj: dict, field: str) -> str:
    body = dict(obj); claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def compose(p, q):
    return [q[p[j] - 1] for j in range(len(p))]


def perm_for_word(word: str, perms: list[list[int]]) -> list[int]:
    out = list(range(1, 141))
    for token in word.split("*"):
        j = int(token[1:])
        out = compose(out, perms[j - 1])
    return out


def rank_and_pivots_mod(rows, p=PRIME):
    a = [[x % p for x in r] for r in rows]
    row_ids = list(range(len(a)))
    r = 0; pivots = []
    ncol = len(a[0]) if a else 0
    for c in range(ncol):
        k = next((i for i in range(r, len(a)) if a[i][c]), None)
        if k is None: continue
        a[r], a[k] = a[k], a[r]; row_ids[r], row_ids[k] = row_ids[k], row_ids[r]
        inv = pow(a[r][c], p - 2, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [(x - z*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(row_ids[r]); r += 1
        if r == len(a): break
    return r, pivots


def ints(line: str):
    try: return [int(x) for x in line.split()]
    except ValueError: return None


marking = load_marking(); assert marking["canonical_sha256"] == MARKING_SHA
adapter = json.loads(ADAPTER.read_text()); assert csha(adapter, "canonical_sha256_without_this_field") == ADAPTER_SHA
assert blob_sha(BRIDGE) == BRIDGE_BLOB
bridge = json.loads(BRIDGE.read_text())
S = adapter["fsm_section2_actions"]["S"]
assert S["stoll_word"] == "g2*g5"
assert S["normalized_box_action"] == ["a3", "-a2", "a1", "b3", "b2", "b1", "c"]

perms = [[int(x) for x in row] for row in marking["aut_action"]["permutations_1based"]]
pS = perm_for_word(S["stoll_word"], perms)
assert sorted(pS) == list(range(1, 141))

lines = marking["hperp_text"].splitlines()
parsed = [ints(x) for x in lines]
assert parsed[4] == [63, 140]
gram63 = parsed[5:68]
rows65 = parsed[68:208]
assert all(r is not None and len(r) == 63 for r in gram63)
assert all(r is not None and len(r) == 65 for r in rows65)
gram63 = [r for r in gram63 if r is not None]
rows65 = [r for r in rows65 if r is not None]
meta2 = [r[:2] for r in rows65]
coords63 = [r[2:] for r in rows65]
rank63, independent_rows = rank_and_pivots_mod(coords63)

# Test both natural permutation conventions on the two metadata columns. The
# exact linear action will be reconstructed only after this structural gate.
def invperm(p):
    q=[0]*len(p)
    for i,v in enumerate(p,1): q[v-1]=i
    return q
pinv=invperm(pS)
meta_mismatch_forward=sum(meta2[i] != meta2[pS[i]-1] for i in range(140))
meta_mismatch_inverse=sum(meta2[i] != meta2[pinv[i]-1] for i in range(140))
meta_hist=collections.Counter(tuple(x) for x in meta2)

acs = bridge["actual_coordinate_swaps_in_historical_magma_picard_basis"]
bb = bridge["basis_bridge"]
print(json.dumps({
    "success": True,
    "marker": "V82_BOUNDED_S_TRANSPORT_INTERFACE_DIAGNOSTIC",
    "marking_canonical_sha256": MARKING_SHA,
    "bridge_blob_sha1": BRIDGE_BLOB,
    "bridge_canonical_sha256": bridge.get("canonical_sha256"),
    "S_stoll_word": S["stoll_word"],
    "S_box_action": S["normalized_box_action"],
    "S_maps_B1_to_B3": True,
    "hperp_blocks": {"gram_shape":[63,63], "known_curve_rows_shape":[140,65], "coordinate_tail_shape":[140,63]},
    "hperp_coordinate_rank_mod_prime": rank63,
    "independent_known_curve_rows_1based": [x+1 for x in independent_rows[:63]],
    "metadata_pair_histogram": {str(k):v for k,v in sorted(meta_hist.items())},
    "metadata_mismatch_under_S_forward": meta_mismatch_forward,
    "metadata_mismatch_under_S_inverse": meta_mismatch_inverse,
    "basis_bridge_from": bb.get("from"),
    "basis_bridge_to": bb.get("to"),
    "basis_bridge_determinant": bb.get("determinant"),
    "basis_bridge_named_action_intertwining_verified": bb.get("named_action_intertwining_verified"),
    "swap12_shape": [len(acs["swap12_action_64x64"]), len(acs["swap12_action_64x64"][0])],
    "swap13_shape": [len(acs["swap13_action_64x64"]), len(acs["swap13_action_64x64"][0])],
    "seven_sign_conjugations_exact": acs["seven_sign_conjugations_exact"],
    "exact_S_hperp_action_reconstructible": rank63 == 63 and min(meta_mismatch_forward, meta_mismatch_inverse) == 0,
    "proper14_action_materialized": False,
    "b3_gysin_image_materialized": False,
    "merge_allowed": False,
}, sort_keys=True))
