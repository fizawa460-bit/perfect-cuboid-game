#!/usr/bin/env python3
"""Verify V91C1X: zero complete swap23 Pic/2 difference fixes the literal A2_02
H2(mu2) seed, and naturality excludes proper14 mask20.

This is a branch-candidate verifier. It does not compute the actual marked
Brauer image and grants no authority/theorem/receiver/endpoint credit.
"""
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
W = HERE / "e3-v91c1w-a2-02-all8-picard64-reduction.json"
X = HERE / "e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json"
Q = HERE / "diagnose_e3_v91c1q_shortest_mask20_moving_stabilizer_word.py"
S = HERE / "diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py"
NOTE = HERE / "e3-v91c1x-kummer-action-difference-source-lock.md"

D_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
W_SHA = "e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7"
X_SHA = "aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f"
Q_BLOB = "1b83812cec6473f04de0e3cf7e2b70bfb47de409"
S_BLOB = "5dbe9fdc61a2663da3a2fd39e20bab130ae163b5"
NOTE_BLOB = "759882263013eb1967945d1c1128747848a6ec9d"
WORD = ["swap12", "swap13", "swap12"]

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

d = load(D, D_SHA)
w = load(W, W_SHA)
x = load(X, X_SHA)
assert gitblob(Q.read_bytes()) == Q_BLOB
assert gitblob(S.read_bytes()) == S_BLOB
assert gitblob(NOTE.read_bytes()) == NOTE_BLOB

note = NOTE.read_text(encoding="utf-8")
assert "Stacks Project, Tag 03PL, Lemma 59.28.1" in note
assert "Stacks Project, Tag 0117, Lemma 12.13.12" in note
assert "g(seed) - seed = delta([L_g])" in note
assert "[L_g]=0" in note

assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert d["exact_consequence"]["a2_02_cartier_transition_binding_materialized"] is True
assert w["exact_result"]["pic2_cech_difference_class_computed"] is True
assert w["exact_result"]["complete_swap23_difference_zero_mod2"] is True
assert w["exact_result"]["complete_swap23_difference_mod2_support_one_based"] == []
assert w["anti_inference"]["zero_pic2_divisor_difference_promoted_to_h2_seed_fixedness"] is False

q = runpy.run_path(str(Q))["result"]
assert q["word"] == WORD and q["word_length"] == 3
assert q["source_a2_02_residue_fixed"] is True
assert q["mask20_moved"] is True
assert q["mask20_target_image_decimal"] == 22
assert q["mask20_target_image_support_one_based"] == [2, 3, 5]

si = x["semantic_bridge"]
assert si["kummer_n"] == 2
assert si["two_invertible_on_geometric_surface"] is True
assert si["connecting_map_functorial_under_surface_automorphisms"] is True
assert si["literal_seed_action_difference_is_kummer_image_of_complete_cartier_pic2_difference"] is True
assert si["zero_pic2_difference_implies_literal_h2_seed_fixedness"] is True
assert si["quotient_map_natural_under_swap23"] is True

ec = x["exact_consequence"]
assert ec["a2_02_swap23_seed_fixed_mod_pic2"] is True
assert ec["a2_02_marked_brauer_image_must_be_swap23_fixed"] is True
assert ec["a2_02_marked_brauer_image_excluded_from_mask20"] is True
assert ec["a2_02_marked_brauer_image_computed"] is False
assert ec["a2_02_claimed_mask20_image"] is False
assert ec["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False
assert ec["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert ec["e3_kummer_column_materialized"] is False

assert x["branch_parent_candidate"]["hostile_audited"] is False
assert x["branch_parent_candidate"]["same_pr"] == 1671
assert x["credit_firewall"]["stage33_progress"] == "6/11"
assert x["credit_firewall"]["merge_allowed"] is False
assert x["credit_firewall"]["theorem_credit"] is False

print(json.dumps({
    "success": True,
    "marker": "V91C1X_KUMMER_NATURALITY_MASK20_EXCLUSION_PASS",
    "canonical_sha256": X_SHA,
    "swap23_word": WORD,
    "mask20_target_image_decimal": 22,
    "seed_fixed_mod_pic2": True,
    "mask20_excluded": True,
    "actual_marked_brauer_image_computed": False,
    "stage33_progress": "6/11",
    "credit": False
}, sort_keys=True))
