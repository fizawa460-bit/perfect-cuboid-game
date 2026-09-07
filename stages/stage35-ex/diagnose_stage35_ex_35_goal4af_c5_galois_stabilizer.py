#!/usr/bin/env python3
"""Generation4: add source-literal Galois stabilizers to the C5 pair solve.

This replays the pinned generation2 sign-stabilizer diagnostic with the illegal
node-union locator gate removed, then adds only symmetries whose action on the
C5 equations is literal: ct fixes every C5 equation (no sqrt(2) occurs), while
cc flips (e1,e4); composing cc with sign(b2) flips e4 only and hence stabilizes
the unordered e4=+/- C5 pair.  No C5 self-intersection or antipodal 2H relation
is assumed.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_sign_stabilizer.py"
BASE_BLOB = "732332e94f1346b03d91425bb664905d3f440c44"
raw = BASE.read_bytes()
got = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
if got != BASE_BLOB:
    raise SystemExit(f"Goal4AF sign-stabilizer generation2 blob moved: {got}")
text = raw.decode()

old_node = '''if len(set(pair_union.values())) != 8:\n    raise SystemExit("C5 pair exceptional-node unions are not label-distinct")\n'''
new_node = '''pair_union_distinct_count = len(set(pair_union.values()))\n'''
if text.count(old_node) != 1:
    raise SystemExit("Goal4AF node-union gate patch target regression")
text = text.replace(old_node, new_node)

old_rank = '''seed_basis = reduce_system(seed_rows, seed_rhs)\naugmented_rank = len(seed_basis)\nnullity = 64 - augmented_rank\n'''
new_rank = r'''seed_basis = reduce_system(seed_rows, seed_rhs)
augmented_rank = len(seed_basis)
nullity = 64 - augmented_rank

# Exact retained Galois permutations, sourced from the same pinned Stoll blob.
GALOIS = ROOT / "stages/stage33/33-07/galois-known-class-permutations.json"
GALOIS_BLOB = "f277939b7f258928f484d2b970d4dfb2ec6133a8"
graw = GALOIS.read_bytes()
gblob = hashlib.sha1(b"blob " + str(len(graw)).encode() + b"\0" + graw).hexdigest()
if gblob != GALOIS_BLOB:
    raise SystemExit(f"Stage33 Galois permutation blob moved: {gblob}")
gal = json.loads(graw)
if gal.get("canonical_sha256") != "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30":
    raise SystemExit("Stage33 Galois permutation canonical hash moved")
if gal.get("source", {}).get("git_blob_sha1") != UPSTREAM_BLOB:
    raise SystemExit("Stage33 Galois source blob moved")
cc_perm = [int(x) for x in gal["cc_permutation_1based"]]
ct_perm = [int(x) for x in gal["ct_permutation_1based"]]
if len(cc_perm) != 140 or len(ct_perm) != 140:
    raise SystemExit("Galois known-class permutation width regression")
cc_action = action_from_perm(cc_perm)
ct_action = action_from_perm(ct_perm)
for name, perm, A in (("cc", cc_perm, cc_action), ("ct", ct_perm, ct_action)):
    if mm(A, A) != I64:
        raise SystemExit(f"{name} Picard action not involutive")
    if row_times_matrix(hyperplane, A) != hyperplane:
        raise SystemExit(f"{name} does not fix hyperplane")
    if mm(mm(A, gram), transpose(A)) != gram:
        raise SystemExit(f"{name} does not preserve Picard Gram")
    for j in range(140):
        if row_times_matrix(known[j], A) != known[perm[j]-1]:
            raise SystemExit(f"{name} all-known-class transport regression at {j+1}")

# Bind the literal C5 Galois action to retained exceptional transport.
# ct fixes i and the C5 equations contain no sqrt(2), so it fixes each label.
# cc sends (e1,e2,e3,e4)->(-e1,e2,e3,-e4).  Source generator g8=sign(b2)
# flips e1, so cc followed by g8 sends only e4 -> -e4 and stabilizes the pair.
g8_perm = perms[7]
def exc_move_from_perm(perm):
    out = {}
    for k in range(48):
        z = int(perm[92+k]) - 1
        if not (92 <= z < 140):
            raise SystemExit("Galois/sign exceptional transport left packet")
        out[k] = z - 92
    return out
ct_exc = exc_move_from_perm(ct_perm)
cc_exc = exc_move_from_perm(cc_perm)
g8_exc = exc_move_from_perm(g8_perm)
for t in labels:
    if {ct_exc[k] for k in c5_nodes[t]} != set(c5_nodes[t]):
        raise SystemExit(f"ct C5-node transport regression at {t}")
    e1,e2,e3,e4 = t
    want = (e1,e2,e3,-e4)
    moved = {g8_exc[cc_exc[k]] for k in c5_nodes[t]}
    if moved != set(c5_nodes[want]):
        raise SystemExit(f"cc*g8 C5-node transport regression at {t}")

cc_g8 = mm(cc_action, actions[7])
galois_stabilizers = [ct_action, cc_g8]
gal_rows = []
for Sg in galois_stabilizers:
    gal_rows.extend(transpose(submat(Sg, I64)))
gal_basis = reduce_system(seed_rows + gal_rows, seed_rhs + [0] * len(gal_rows))
galois_augmented_rank = len(gal_basis)
galois_augmented_nullity = 64 - galois_augmented_rank
seed_basis = gal_basis
'''
if text.count(old_rank) != 1:
    raise SystemExit("Goal4AF stabilizer rank injection target regression")
text = text.replace(old_rank, new_rank)

old_summary = '''        "sign_stabilizer_augmented_rank": augmented_rank,\n        "sign_stabilizer_augmented_nullity": nullity,\n'''
new_summary = '''        "sign_stabilizer_augmented_rank": augmented_rank,\n        "sign_stabilizer_augmented_nullity": nullity,\n        "galois_stabilizer_augmented_rank": galois_augmented_rank,\n        "galois_stabilizer_augmented_nullity": galois_augmented_nullity,\n        "galois_stabilizers": ["ct", "cc_then_g8_sign_b2"],\n'''
if text.count(old_summary) != 1:
    raise SystemExit("Goal4AF summary injection target regression")
text = text.replace(old_summary, new_summary)

# The old exploratory script used antipodal total-pair sum=2H only as a final
# consistency assertion.  That exceptional correction has not been source-
# established for Goal4AC, so generation4 records it if observed but never uses
# it to determine the rows and never fails on it.
old_anti_fail = '''if not all(anti_checks.values()):\n    raise SystemExit("unique sign-stabilized rows fail Goal4AC antipodal 2H relation")\n'''
new_anti_fail = '''antipodal_total_pair_sum_equals_2H_observed = all(anti_checks.values())\n'''
if text.count(old_anti_fail) != 1:
    raise SystemExit("Goal4AF antipodal assertion patch target regression")
text = text.replace(old_anti_fail, new_anti_fail)
old_anti_summary = '''    "antipodal_total_pair_sum_equals_2H": True,\n'''
new_anti_summary = '''    "antipodal_total_pair_sum_equals_2H": antipodal_total_pair_sum_equals_2H_observed,\n'''
if text.count(old_anti_summary) != 1:
    raise SystemExit("Goal4AF antipodal summary patch target regression")
text = text.replace(old_anti_summary, new_anti_summary)

exec(compile(text, str(BASE), "exec"), globals())
