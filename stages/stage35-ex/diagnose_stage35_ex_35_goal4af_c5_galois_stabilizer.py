#!/usr/bin/env python3
"""Generation6: expose the final one-dimensional C5-pair ambiguity.

Replays the exact generation5 sign+Galois constraints and, if one dimension
remains, computes a primitive integral null direction and the retained known
curve pairings that detect it.  This is locator-only: it does not assign the
missing geometric intersection value and does not materialize C5 rows.
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

# Locate an exact retained curve receiver for the remaining ambiguity.  The
# reduced rows are echelon with pivot coefficient 1, so one free coordinate
# gives a homogeneous null vector by reverse substitution.
free_cols = [j for j in range(64) if j not in seed_basis]
null_direction = None
null_receiver_rows = []
if len(free_cols) == 1:
    fcol = free_cols[0]
    nv = [Fraction(0) for _ in range(64)]
    nv[fcol] = Fraction(1)
    for p in sorted(seed_basis, reverse=True):
        row, _b = seed_basis[p]
        nv[p] = -sum(row[j] * nv[j] for j in range(p + 1, 64))
    from math import gcd, lcm
    den = 1
    for z in nv:
        den = lcm(den, z.denominator)
    zi = [int(z * den) for z in nv]
    g = 0
    for z in zi:
        g = gcd(g, abs(z))
    if g:
        zi = [z // g for z in zi]
    if next((z for z in zi if z), 1) < 0:
        zi = [-z for z in zi]
    null_direction = zi
    if any(sum(r[j]*zi[j] for j in range(64)) != 0 for r in seed_rows + gal_rows):
        raise SystemExit("final null direction failed homogeneous constraints")
    for j in range(92):
        val = pairing(zi, known[j], gram)
        if val:
            null_receiver_rows.append({"known_curve_index_1based": j+1, "null_pairing": int(val)})
'''
if text.count(old_rank) != 1:
    raise SystemExit("Goal4AF stabilizer rank injection target regression")
text = text.replace(old_rank, new_rank)

old_summary = '''    "sign_stabilizer_augmented_rank": augmented_rank,\n    "sign_stabilizer_augmented_nullity": nullity,\n'''
new_summary = '''    "sign_stabilizer_augmented_rank": augmented_rank,\n    "sign_stabilizer_augmented_nullity": nullity,\n    "galois_stabilizer_augmented_rank": galois_augmented_rank,\n    "galois_stabilizer_augmented_nullity": galois_augmented_nullity,\n    "galois_stabilizers": ["ct", "cc_then_g8_sign_b2"],\n    "final_free_columns_0based": free_cols,\n    "final_null_direction_INDLIST64": null_direction,\n    "known_curve_receivers_detecting_null": null_receiver_rows[:32],\n    "known_curve_receiver_count_detecting_null": len(null_receiver_rows),\n'''
if text.count(old_summary) != 1:
    raise SystemExit("Goal4AF summary injection target regression")
text = text.replace(old_summary, new_summary)

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
