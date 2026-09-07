#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_SCRIPT = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_local_node_lattice.py"
BASE_BLOB = "aa43bc38d799ab78cf0252830718979b15fa54fc"
MARKER = "# Build the common linear system characterizing a total pullback pair y:"

raw = BASE_SCRIPT.read_bytes()
blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
if blob != BASE_BLOB:
    raise SystemExit(f"Goal4AF generation1 node diagnostic blob moved: {blob}")
text = raw.decode()
if text.count(MARKER) != 1:
    raise SystemExit("Goal4AF generation1 prefix marker regression")
prefix = text.split(MARKER, 1)[0]
# Reuse only the exact source-node alignment, C5 node incidence, sigma_c action,
# and retained Picard reconstruction from generation1.  The old rank-57 solve
# and everything after it are intentionally not executed.
exec(compile(prefix, str(BASE_SCRIPT), "exec"), globals())


def submat(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def pairing_column(e):
    return [sum(gram[i][j] * e[j] for j in range(64)) for i in range(64)]


def addi(a, b):
    return [x + y for x, y in zip(a, b)]


def subi(a, b):
    return [x - y for x, y in zip(a, b)]


def scalei(k, a):
    return [k * x for x in a]


def psq(v):
    return int(pairing(v, v, gram))


# Generation1 established that the source-node incidence alignment is exact but
# sigma_c + all exceptional pairings + degree have rank only 57.  Rebuild that
# common system without assuming any C5 self-intersection.
fixed = transpose(submat(c_action, I64))
contracted = [known[116 + k] for k in range(24)]
uncontracted = [known[92 + k] for k in range(24)]
baseA = [list(map(int, r)) for r in fixed]
baseA += [pairing_column(E) for E in contracted]
baseA += [pairing_column(E) for E in uncontracted]
baseA += [pairing_column(hyperplane)]
if len(baseA) != 113 or any(len(r) != 64 for r in baseA):
    raise SystemExit("Goal4AF base pair system shape regression")

triples = list(itertools.product((1, -1), repeat=3))

def rhs_for(tr):
    plus = set(c5_nodes[tr + (1,)])
    minus = set(c5_nodes[tr + (-1,)])
    p_un = [int(k in plus) + int(k in minus) for k in range(24)]
    return [0] * 64 + [0] * 24 + p_un + [16]


def reduce_system(rows, rhs):
    if len(rows) != len(rhs):
        raise SystemExit("constraint/RHS height mismatch")
    basis = {}
    for rawrow, rawb in zip(rows, rhs):
        v = [Fraction(x) for x in rawrow]
        b = Fraction(rawb)
        for p in sorted(basis):
            brow, bb = basis[p]
            f = v[p]
            if f:
                v = [x - f * y for x, y in zip(v, brow)]
                b -= f * bb
        p = next((j for j, x in enumerate(v) if x), None)
        if p is None:
            if b:
                raise SystemExit("exact C5 pair linear system inconsistent")
            continue
        d = v[p]
        v = [x / d for x in v]
        b /= d
        basis[p] = (v, b)
    return basis


def solve_unique(basis):
    if len(basis) != 64:
        return None
    x = [Fraction(0) for _ in range(64)]
    for p in sorted(basis, reverse=True):
        row, b = basis[p]
        x[p] = b - sum(row[j] * x[j] for j in range(p + 1, 64))
    if any(v.denominator != 1 for v in x):
        raise SystemExit("unique sign-stabilized C5 pair row is nonintegral")
    return [int(v) for v in x]

base_rank = len(reduce_system(baseA, [0] * len(baseA)))
if base_rank != 57:
    raise SystemExit(f"Goal4AF generation1 rank regression: {base_rank} != 57")

# Use only the six source sign-change generators 4..9.  Their action on the
# C5 equations is literal and needs no name/curve locator:
#   g4: (e1,e2,e3,e4) -> (-e1,-e2,-e3,-e4)
#   g5: (e1,e2,e3,e4) -> ( e1,-e2, e3, e4)
#   g6: (e1,e2,e3,e4) -> ( e1, e2,-e3, e4)
#   g7,g8,g9 flip e1 (Q may be rescaled by -1 for g7).
# After forgetting e4 inside a C5 pair, these induce the maps below.
def expected_label_map(g1, tr):
    e1, e2, e3 = tr
    if g1 == 4:
        return (-e1, -e2, -e3)
    if g1 == 5:
        return (e1, -e2, e3)
    if g1 == 6:
        return (e1, e2, -e3)
    if g1 in (7, 8, 9):
        return (-e1, e2, e3)
    raise ValueError(g1)

sign_generators_1based = [4, 5, 6, 7, 8, 9]
sign_generator_indices = [g - 1 for g in sign_generators_1based]
for gi in sign_generator_indices:
    if mm(actions[gi], actions[gi]) != I64:
        raise SystemExit(f"source sign generator {gi+1} not involutive on Picard")

pair_union = {
    tr: frozenset(set(c5_nodes[tr + (1,)]) | set(c5_nodes[tr + (-1,)]))
    for tr in triples
}
if len(set(pair_union.values())) != 8:
    raise SystemExit("C5 pair exceptional-node unions are not label-distinct")

# Cross-check the literal source sign-label formula against the independently
# retained Picard/ex\-ceptional action.  This binds the equation semantics to the
# historical INDLIST64 action before any stabilizer constraint is used.
label_permutations = {}
for g1, gi in zip(sign_generators_1based, sign_generator_indices):
    A = actions[gi]
    exc_move = {}
    for k in range(48):
        moved = row_times_matrix(known[92 + k], A)
        idx = known_index.get(tuple(moved))
        if idx is None or not (92 <= idx < 140):
            raise SystemExit(f"sign generator {g1} lost exceptional packet")
        exc_move[k] = idx - 92
    mp = {}
    for tr in triples:
        want = expected_label_map(g1, tr)
        got_nodes = frozenset(exc_move[k] for k in pair_union[tr])
        if got_nodes != pair_union[want]:
            raise SystemExit(f"source sign-label/Picard-node transport mismatch g{g1} {tr} -> {want}")
        mp[tr] = want
    label_permutations[g1] = mp

# The six sign generators act transitively on the eight C5-pair labels.  Build
# a Schreier transversal from the seed.  Because every selected generator is an
# involution, the inverse of a transversal word is its reversed word.
seed = (1, 1, 1)
trans = {seed: I64}
words = {seed: ()}
queue = [seed]
while queue:
    x = queue.pop(0)
    for g1, gi in zip(sign_generators_1based, sign_generator_indices):
        y = label_permutations[g1][x]
        if y not in trans:
            trans[y] = mm(trans[x], actions[gi])
            words[y] = words[x] + (gi,)
            queue.append(y)
if set(trans) != set(triples):
    raise SystemExit(f"source sign subgroup not transitive on C5 pair labels: {sorted(trans)}")


def inverse_word_matrix(word):
    out = I64
    for gi in reversed(word):
        out = mm(out, actions[gi])
    return out

invtrans = {}
for tr in triples:
    inv = inverse_word_matrix(words[tr])
    if mm(trans[tr], inv) != I64 or mm(inv, trans[tr]) != I64:
        raise SystemExit(f"C5 label transversal inverse regression at {tr}")
    invtrans[tr] = inv

# Schreier lemma: T_x g T_{xg}^{-1} generates the stabilizer of the seed in the
# sign subgroup.  A genuine seed pair class must be fixed by each such Picard
# action.  Collect only distinct nonidentity stabilizer matrices.
stabilizers = []
seen_stab = set()
for x in triples:
    for g1, gi in zip(sign_generators_1based, sign_generator_indices):
        y = label_permutations[g1][x]
        S = mm(mm(trans[x], actions[gi]), invtrans[y])
        key = tuple(tuple(r) for r in S)
        if S != I64 and key not in seen_stab:
            seen_stab.add(key)
            stabilizers.append(S)

stab_rows = []
for S in stabilizers:
    stab_rows.extend(transpose(submat(S, I64)))

seed_rows = baseA + stab_rows
seed_rhs = rhs_for(seed) + [0] * len(stab_rows)
seed_basis = reduce_system(seed_rows, seed_rhs)
augmented_rank = len(seed_basis)
nullity = 64 - augmented_rank

summary = {
    "schema": "STAGE35_EX_GOAL4AF_C5_SIGN_STABILIZER_DIAGNOSTIC_V1",
    "upstream_git_blob_sha1": UPSTREAM_BLOB,
    "generation1_node_diagnostic_blob_sha1": BASE_BLOB,
    "source_tuple_order_convention": convention,
    "base_pair_characterization_rank": base_rank,
    "base_pair_characterization_nullity": 64 - base_rank,
    "sign_generators_1based": sign_generators_1based,
    "sign_subgroup_label_orbit_size": len(trans),
    "schreier_nonidentity_stabilizer_matrix_count": len(stabilizers),
    "sign_stabilizer_augmented_rank": augmented_rank,
    "sign_stabilizer_augmented_nullity": nullity,
    "pair_rows_materialized": False,
    "pair_count": 0,
    "goal4ac_residual_pair_count": 0,
    "remote_cas_used": False,
    "target_span_computed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}

seed_total = solve_unique(seed_basis)
if seed_total is None:
    print("GOAL4AF_SIGN_STABILIZER_JSON=" + json.dumps(summary, sort_keys=True, separators=(",", ":")))
    raise SystemExit(0)

# Transport the unique seed class to all eight source labels, and independently
# recheck every transported row against its own sigma_c/exceptional/degree RHS.
total_by_triple = {}
for tr in triples:
    total = row_times_matrix(seed_total, trans[tr])
    rhs = rhs_for(tr)
    for r, b in zip(baseA, rhs):
        if sum(r[j] * total[j] for j in range(64)) != b:
            raise SystemExit(f"transported C5 pair failed base constraints at {tr}")
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
        raise SystemExit(f"C5 pair sigma_c invariance regression at {tr}")
    if any(pairing(total, E, gram) != 0 for E in contracted):
        raise SystemExit(f"C5 total pair not orthogonal to contracted packet at {tr}")
    if pairing(total, hyperplane, gram) != 16 or pairing(strict, hyperplane, gram) != 16:
        raise SystemExit(f"C5 pair degree regression at {tr}")
    for k, E in enumerate(known[92:140]):
        strict_expected = int(k in plus_nodes) + int(k in minus_nodes)
        if pairing(strict, E, gram) != strict_expected:
            raise SystemExit(f"C5 strict pair exceptional incidence regression at {tr}, E{k}")
    pair_rows.append({
        "sign_triple": list(tr),
        "c5_plus_exceptional_indices_0based": sorted(plus_nodes),
        "c5_minus_exceptional_indices_0based": sorted(minus_nodes),
        "contracted_correction_coefficients_24": corr_coeff,
        "strict_pair_INDLIST64": strict,
        "total_pullback_pair_INDLIST64": total,
        "strict_pair_square": psq(strict),
        "total_pullback_pair_square": psq(total),
    })

anti_checks = {}
for tr in triples:
    anti = tuple(-x for x in tr)
    anti_checks[str(tr)] = addi(total_by_triple[tr], total_by_triple[anti]) == scalei(2, hyperplane)
if not all(anti_checks.values()):
    raise SystemExit("unique sign-stabilized rows fail Goal4AC antipodal 2H relation")

residual = []
for e2, e3 in itertools.product((1, -1), repeat=2):
    chosen = (1, e2, e3)
    anti = (-1, -e2, -e3)
    row = next(r for r in pair_rows if tuple(r["sign_triple"]) == anti)
    residual.append({
        "chosen_section_representative": list(chosen),
        "residual_antipodal_pair": list(anti),
        "strict_pair_INDLIST64": row["strict_pair_INDLIST64"],
        "total_pullback_pair_INDLIST64": row["total_pullback_pair_INDLIST64"],
    })

summary.update({
    "pair_rows_materialized": True,
    "pair_count": 8,
    "pair_rows": pair_rows,
    "antipodal_total_pair_sum_equals_2H": True,
    "antipodal_checks": anti_checks,
    "goal4ac_residual_pair_count": 4,
    "goal4ac_residual_pairs": residual,
})
print("GOAL4AF_SIGN_STABILIZER_JSON=" + json.dumps(summary, sort_keys=True, separators=(",", ":")))
