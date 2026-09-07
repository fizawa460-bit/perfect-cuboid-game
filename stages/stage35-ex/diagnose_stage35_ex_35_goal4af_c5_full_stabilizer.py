#!/usr/bin/env python3
"""Goal4AF generation4: add the two source coordinate swaps to the exact C5-pair
stabilizer calculation.

Generation3 source-locked the six sign changes and showed that they raise the
rank-57 C5-pair system only to rank 60.  Here the remaining source generators
swap12 and swap13 are added from their literal substitutions in the pinned
Stoll `cuboids.magma` blob.  Their C5 label formulas are derived from the
source equations, not inferred from exceptional-node unions.  The explicit
48-node model is used only as an independent transport check.

For swap12, after multiplying the transformed linear equation by e2,
  (e1,e2,e3,e4) -> (e1*e2, e2, e2*e3, e2*e4).
For swap13, after multiplying it by e3,
  (e1,e2,e3,e4) -> (e1*e3, e2*e3, e3, e3*e4).
The quadratic equation transforms compatibly because on the corresponding
linear section
  X^2+Y^2+Z^2+XY+XZ+YZ = 0,
and
  (Y+Z)(Y^2+Z^2) - (X+Z)(X^2+Z^2)
    = (Y-X)(X^2+Y^2+Z^2+XY+XZ+YZ),
with the analogous X<->Z identity for swap13.  Thus the displayed label maps
are source-derived; the node check below is deliberately only corroboration.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_sign_stabilizer_v2.py"
BASE_BLOB = "122731f6c9cb63471ab584eb6d25aecb33d4481f"
raw = BASE.read_bytes()
got = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
if got != BASE_BLOB:
    raise SystemExit(f"Goal4AF generation3 diagnostic blob moved: {got}")
# Generation3 is no-credit and leaves the exact source-node/Picard structures
# in globals.  Its own summary line is harmless; this file emits a distinct
# generation4 marker below.
exec(compile(raw.decode(), str(BASE), "exec"), globals())


def swap_full_label(g1, t):
    e1, e2, e3, e4 = t
    if g1 == 1:
        return (e1 * e2, e2, e2 * e3, e2 * e4)
    if g1 == 2:
        return (e1 * e3, e2 * e3, e3, e3 * e4)
    raise ValueError(g1)


def swap_pair_label(g1, tr):
    e1, e2, e3 = tr
    if g1 == 1:
        return (e1 * e2, e2, e2 * e3)
    if g1 == 2:
        return (e1 * e3, e2 * e3, e3)
    raise ValueError(g1)


full_labels = list(itertools.product((1, -1), repeat=4))
for g1 in (1, 2):
    if {swap_full_label(g1, t) for t in full_labels} != set(full_labels):
        raise SystemExit(f"source swap g{g1} is not a permutation of C5 labels")
    if any(swap_full_label(g1, swap_full_label(g1, t)) != t for t in full_labels):
        raise SystemExit(f"source swap g{g1} label action not involutive")

# Independent exact common-anchor check: transport every explicit source node
# through the retained exceptional permutation and compare the ordered
# individual C5 incidence set with the source-derived expected full label.
# No uniqueness of incidence signatures is used to *derive* a label.
swap_ordered_node_transport_exact = {}
individual_incidence_distinct_count = len({frozenset(c5_nodes[t]) for t in full_labels})
ordered_pair_incidence_distinct_count = len({
    (frozenset(c5_nodes[tr + (1,)]), frozenset(c5_nodes[tr + (-1,)]))
    for tr in triples
})
for g1 in (1, 2):
    A = actions[g1 - 1]
    exc_move = {}
    for k in range(48):
        moved = row_times_matrix(known[92 + k], A)
        idx = known_index.get(tuple(moved))
        if idx is None or not (92 <= idx < 140):
            raise SystemExit(f"source swap g{g1} lost exceptional packet")
        exc_move[k] = idx - 92
    ok = True
    for t in full_labels:
        want = swap_full_label(g1, t)
        got_nodes = frozenset(exc_move[k] for k in c5_nodes[t])
        want_nodes = frozenset(c5_nodes[want])
        if got_nodes != want_nodes:
            ok = False
            raise SystemExit(f"source swap/C5 ordered-node transport mismatch g{g1}: {t} -> {want}")
    swap_ordered_node_transport_exact[str(g1)] = ok

# S3 sanity check in both source-label and retained Picard actions.
def compose_label_map(f, g, t):
    return f(g(t))
for t in full_labels:
    u = t
    for _ in range(3):
        u = swap_full_label(1, swap_full_label(2, u))
    if u != t:
        raise SystemExit("source swap label braid/order-3 regression")
A12 = mm(actions[0], actions[1])
if mm(mm(A12, A12), A12) != I64:
    raise SystemExit("retained swap12*swap13 order-3 regression")

# Extend the already source-locked sign label action by the two coordinate
# swaps.  The sign subgroup alone is transitive, so Schreier with all eight
# generators gives the full stabilizer constraints visible from this source
# action without introducing any geometric locator assumption.
full_generators_1based = [1, 2, 4, 5, 6, 7, 8, 9]
full_generator_indices = [g - 1 for g in full_generators_1based]
full_label_permutations = {}
for g1 in full_generators_1based:
    mp = {}
    for tr in triples:
        if g1 in (1, 2):
            mp[tr] = swap_pair_label(g1, tr)
        else:
            mp[tr] = label_permutations[g1][tr]
    if set(mp.values()) != set(triples):
        raise SystemExit(f"full source generator g{g1} not a C5-pair label permutation")
    full_label_permutations[g1] = mp

seed = (1, 1, 1)
full_trans = {seed: I64}
full_words = {seed: ()}
queue = [seed]
while queue:
    x = queue.pop(0)
    for g1, gi in zip(full_generators_1based, full_generator_indices):
        y = full_label_permutations[g1][x]
        if y not in full_trans:
            full_trans[y] = mm(full_trans[x], actions[gi])
            full_words[y] = full_words[x] + (gi,)
            queue.append(y)
if set(full_trans) != set(triples):
    raise SystemExit(f"full source subgroup not transitive on C5 pair labels: {sorted(full_trans)}")


def inverse_word_matrix_local(word):
    out = I64
    for gi in reversed(word):
        out = mm(out, actions[gi])
    return out

full_invtrans = {}
for tr in triples:
    inv = inverse_word_matrix_local(full_words[tr])
    if mm(full_trans[tr], inv) != I64 or mm(inv, full_trans[tr]) != I64:
        raise SystemExit(f"full C5 label transversal inverse regression at {tr}")
    full_invtrans[tr] = inv

full_stabilizers = []
seen = set()
for x in triples:
    for g1, gi in zip(full_generators_1based, full_generator_indices):
        y = full_label_permutations[g1][x]
        S = mm(mm(full_trans[x], actions[gi]), full_invtrans[y])
        key = tuple(tuple(r) for r in S)
        if S != I64 and key not in seen:
            seen.add(key)
            full_stabilizers.append(S)

full_stab_rows = []
for S in full_stabilizers:
    full_stab_rows.extend(transpose(submat(S, I64)))
full_seed_rows = baseA + full_stab_rows
full_seed_rhs = rhs_for(seed) + [0] * len(full_stab_rows)
full_seed_basis = reduce_system(full_seed_rows, full_seed_rhs)
full_rank = len(full_seed_basis)
full_nullity = 64 - full_rank

out = {
    "schema": "STAGE35_EX_GOAL4AF_C5_FULL_SOURCE_STABILIZER_DIAGNOSTIC_V1",
    "upstream_git_blob_sha1": UPSTREAM_BLOB,
    "generation3_diagnostic_blob_sha1": BASE_BLOB,
    "source_tuple_order_convention": convention,
    "base_pair_characterization_rank": base_rank,
    "base_pair_characterization_nullity": 64 - base_rank,
    "sign_stabilizer_augmented_rank": augmented_rank,
    "sign_stabilizer_augmented_nullity": nullity,
    "full_generators_1based": full_generators_1based,
    "source_swap_full_label_formulas": {
        "g1_swap12": "(e1*e2,e2,e2*e3,e2*e4)",
        "g2_swap13": "(e1*e3,e2*e3,e3,e3*e4)"
    },
    "swap_ordered_node_transport_exact": swap_ordered_node_transport_exact,
    "individual_c5_node_incidence_distinct_count": individual_incidence_distinct_count,
    "ordered_pair_node_incidence_distinct_count": ordered_pair_incidence_distinct_count,
    "full_label_orbit_size": len(full_trans),
    "full_schreier_nonidentity_stabilizer_matrix_count": len(full_stabilizers),
    "full_stabilizer_augmented_rank": full_rank,
    "full_stabilizer_augmented_nullity": full_nullity,
    "pair_rows_materialized": False,
    "pair_count": 0,
    "goal4ac_residual_pair_count": 0,
    "remote_cas_used": False,
    "target_span_computed": False,
    "theorem_credit": False,
    "endpoint_credit": False
}

seed_total = solve_unique(full_seed_basis)
if seed_total is None:
    print("GOAL4AF_FULL_STABILIZER_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
    raise SystemExit(0)

# Unique case: transport and independently recheck every row against its own
# source-node/degree/sigma_c constraints before exposing any numeric row.
total_by_triple = {}
for tr in triples:
    total = row_times_matrix(seed_total, full_trans[tr])
    rhs = rhs_for(tr)
    for r, b in zip(baseA, rhs):
        if sum(r[j] * total[j] for j in range(64)) != b:
            raise SystemExit(f"full-stabilizer transported C5 pair failed base constraints at {tr}")
    total_by_triple[tr] = total

pair_rows = []
for tr in triples:
    total = total_by_triple[tr]
    plus_nodes = set(c5_nodes[tr + (1,)])
    minus_nodes = set(c5_nodes[tr + (-1,)])
    correction = [0] * 64
    corr_coeff = []
    for local_k, E in enumerate(contracted, 24):
        m = int(local_k in plus_nodes)
        corr_coeff.append(m)
        if m:
            correction = addi(correction, E)
    strict = subi(total, correction)
    if row_times_matrix(total, c_action) != total or row_times_matrix(strict, c_action) != strict:
        raise SystemExit(f"full-stabilizer C5 pair sigma_c invariance regression at {tr}")
    if any(pairing(total, E, gram) != 0 for E in contracted):
        raise SystemExit(f"full-stabilizer C5 total pair not orthogonal to contracted packet at {tr}")
    if pairing(total, hyperplane, gram) != 16 or pairing(strict, hyperplane, gram) != 16:
        raise SystemExit(f"full-stabilizer C5 pair degree regression at {tr}")
    for k, E in enumerate(known[92:140]):
        expected = int(k in plus_nodes) + int(k in minus_nodes)
        if pairing(strict, E, gram) != expected:
            raise SystemExit(f"full-stabilizer C5 strict pair exceptional incidence regression at {tr}, E{k}")
    pair_rows.append({
        "sign_triple": list(tr),
        "c5_plus_exceptional_indices_0based": sorted(plus_nodes),
        "c5_minus_exceptional_indices_0based": sorted(minus_nodes),
        "strict_pair_INDLIST64": strict,
        "total_pullback_pair_INDLIST64": total,
        "strict_pair_square": psq(strict),
        "total_pullback_pair_square": psq(total)
    })

anti_checks = {}
for tr in triples:
    anti = tuple(-x for x in tr)
    anti_checks[str(tr)] = addi(total_by_triple[tr], total_by_triple[anti]) == scalei(2, hyperplane)
if not all(anti_checks.values()):
    raise SystemExit("full-stabilizer rows fail Goal4AC antipodal 2H relation")

residual = []
for e2, e3 in itertools.product((1, -1), repeat=2):
    chosen = (1, e2, e3)
    anti = (-1, -e2, -e3)
    row = next(r for r in pair_rows if tuple(r["sign_triple"]) == anti)
    residual.append({
        "chosen_section_representative": list(chosen),
        "residual_antipodal_pair": list(anti),
        "strict_pair_INDLIST64": row["strict_pair_INDLIST64"],
        "total_pullback_pair_INDLIST64": row["total_pullback_pair_INDLIST64"]
    })

out.update({
    "pair_rows_materialized": True,
    "pair_count": 8,
    "pair_rows": pair_rows,
    "antipodal_total_pair_sum_equals_2H": True,
    "antipodal_checks": anti_checks,
    "goal4ac_residual_pair_count": 4,
    "goal4ac_residual_pairs": residual
})
print("GOAL4AF_FULL_STABILIZER_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
