#!/usr/bin/env python3
"""Goal4AF generation7: close the last Picard ambiguity with source C1 #25.

Generation6 proved that the sign+Galois system has rank 63 and that its unique
null direction is detected exactly by retained C1 curves 25..32.  This leaf
adds one *source-computed* intersection, not a guessed lattice invariant.

For the seed C5 pair (e1,e2,e3)=(1,1,1), C1 #25 is the c=0 conic
  c=0, i*a1+b1=0, i*a2+b2=0, i*a3+b3=0.
On this conic each e4=+/- C5 restricts to the same line
  a1+a2+a3=0.
The C5 quadratic equation becomes -i(a1*a2+a1*a3+a2*a3)=0, which follows
from the line and the conic a1^2+a2^2+a3^2=0.  The line cuts the conic in two
distinct points: a1 cannot vanish, and with a1=1, a2=r,
a3=-1-r the conic is 2(r^2+r+1), whose discriminant is -3.  The exact
48-node model verifies that neither point is singular.  Hence each C5 has
intersection 2 with C1 #25 and the strict pair has intersection 4.  No C5
node of the seed lies on C1 #25, so the contracted-exceptional correction
from strict pair to the total pullback pair contributes zero there.  Thus the
rank-63 total-pair class satisfies D.C25=4.

No C5 square, antipodal 2H relation, target-span result, or theorem credit is
used to determine the row.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_galois_stabilizer.py"
BASE_BLOB = "59859e620f65555234fdc5176338281a191dac17"
raw = BASE.read_bytes()
got = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
if got != BASE_BLOB:
    raise SystemExit(f"Goal4AF generation6 diagnostic blob moved: {got}")
text = raw.decode()

old = '''galois_augmented_rank = len(gal_basis)\ngalois_augmented_nullity = 64 - galois_augmented_rank\nseed_basis = gal_basis\n\n# Locate an exact retained curve receiver for the remaining ambiguity.'''
new = r'''galois_augmented_rank = len(gal_basis)
galois_augmented_nullity = 64 - galois_augmented_rank
if galois_augmented_rank != 63 or galois_augmented_nullity != 1:
    raise SystemExit("Goal4AF generation6 rank/nullity regression before C25 receiver")

# Source C1 #25 is the first c=0 conic in the pinned list-comprehension order.
a1,a2,a3,b1,b2,b3,c = (BASE[x] for x in ("a1","a2","a3","b1","b2","b3","c"))
c25_forms = source_curves[24]
c25_expected = (
    c,
    ladd(lscale(II,a1), b1),
    ladd(lscale(II,a2), b2),
    ladd(lscale(II,a3), b3),
)
if c25_forms != c25_expected:
    raise SystemExit("source C1 #25 c=0 conic locator regression")

# Exact projective line/conic calculation.  If a1=0 and L=0, then a3=-a2
# and the conic is 2*a2^2, so no projective point occurs at a1=0.  On a1=1
# the conic is 2*(r^2+r+1), with nonzero discriminant -3.
receiver_each_c5_intersection = 2
receiver_strict_pair_intersection = 4
if (1*1 - 4*1*1) != -3:
    raise SystemExit("C25 line/conic discriminant arithmetic regression")

seed = (1,1,1)
# The explicit 48-node model is complete and was source-aligned to the retained
# exceptional packet.  Check directly that C25 and either seed C5 have no
# common singular point, and therefore no blow-up subtraction at the two
# line/conic intersection points.
c25_seed_singular_hits = []
for p in nodes:
    if all(leval(f,p)==ZERO for f in c25_forms):
        for e4 in (1,-1):
            L,Q = c5_values(seed+(e4,),p)
            if L==ZERO and Q==ZERO:
                c25_seed_singular_hits.append((node_to_exc[node_key(p)],e4))
if c25_seed_singular_hits:
    raise SystemExit(f"seed C5/C25 intersection unexpectedly singular: {c25_seed_singular_hits}")

# Since no seed C5 singular node lies on C25, the exceptional correction used
# to pass from strict pair to total pullback pair has zero C25 pairing.
receiver_total_pair_intersection = receiver_strict_pair_intersection
receiver_row = pairing_column(known[24])
receiver_basis = reduce_system(seed_rows + gal_rows + [receiver_row],
                               seed_rhs + [0]*len(gal_rows) + [receiver_total_pair_intersection])
receiver_augmented_rank = len(receiver_basis)
receiver_augmented_nullity = 64 - receiver_augmented_rank
if receiver_augmented_rank != 64 or receiver_augmented_nullity != 0:
    raise SystemExit(f"C25 source receiver did not close final ambiguity: rank={receiver_augmented_rank}")
seed_basis = receiver_basis

# Locate an exact retained curve receiver for the remaining ambiguity.'''
if text.count(old) != 1:
    raise SystemExit("Goal4AF generation6 C25 receiver injection target regression")
text = text.replace(old,new)

old_summary = '''    "known_curve_receiver_count_detecting_null": len(null_receiver_rows),\n'''
new_summary = '''    "known_curve_receiver_count_detecting_null": len(null_receiver_rows),\n    "source_receiver_known_curve_index_1based": 25,\n    "source_receiver_each_c5_intersection": receiver_each_c5_intersection,\n    "source_receiver_strict_pair_intersection": receiver_strict_pair_intersection,\n    "source_receiver_total_pair_intersection": receiver_total_pair_intersection,\n    "source_receiver_seed_singular_hit_count": len(c25_seed_singular_hits),\n    "source_receiver_augmented_rank": receiver_augmented_rank,\n    "source_receiver_augmented_nullity": receiver_augmented_nullity,\n'''
if text.count(old_summary) != 1:
    raise SystemExit("Goal4AF generation6 summary receiver injection target regression")
text = text.replace(old_summary,new_summary)

# Generation6 already demoted the provisional antipodal 2H relation to an
# observation.  Keep that no-credit behavior unchanged.
exec(compile(text, str(BASE), "exec"), globals())

if not summary.get("pair_rows_materialized") or summary.get("pair_count") != 8:
    raise SystemExit("C25 receiver closed rank but did not materialize eight C5 pair rows")
if summary.get("goal4ac_residual_pair_count") != 4:
    raise SystemExit("C25 receiver did not materialize four Goal4AC residual pair rows")

# Independent equivariant receiver replay.  Transporting seed C25 by the same
# sign transversal must produce exactly the eight c=0 C1 conics #25..#32, and
equiv_receiver_indices = {}
for tr in triples:
    moved = row_times_matrix(known[24], trans[tr])
    idx = known_index.get(tuple(moved))
    if idx is None:
        raise SystemExit(f"transported C25 receiver missing from known packet at {tr}")
    if not (24 <= idx < 32):
        raise SystemExit(f"transported C25 receiver left c=0 conic packet at {tr}: {idx+1}")
    if pairing(total_by_triple[tr], known[idx], gram) != 4:
        raise SystemExit(f"transported C5 pair/branch-conic intersection regression at {tr}")
    equiv_receiver_indices[str(tr)] = idx+1
if set(equiv_receiver_indices.values()) != set(range(25,33)):
    raise SystemExit("C5 pair labels do not exhaust the eight c=0 branch conic receivers")

out = {
    "schema":"STAGE35_EX_GOAL4AF_C5_BRANCH_CONIC_RECEIVER_DIAGNOSTIC_V1",
    "generation6_diagnostic_blob_sha1":BASE_BLOB,
    "upstream_git_blob_sha1":UPSTREAM_BLOB,
    "galois_rank_before_receiver":galois_augmented_rank,
    "galois_nullity_before_receiver":galois_augmented_nullity,
    "receiver_known_curve_index_1based":25,
    "receiver_source_description":"C1 c=0, i*a1+b1=i*a2+b2=i*a3+b3=0",
    "receiver_each_c5_intersection":2,
    "receiver_total_pair_intersection":4,
    "receiver_augmented_rank":receiver_augmented_rank,
    "receiver_augmented_nullity":receiver_augmented_nullity,
    "equivariant_receiver_indices_1based":equiv_receiver_indices,
    "pair_rows_materialized":True,
    "pair_count":8,
    "goal4ac_residual_pair_count":4,
    "target_span_computed":False,
    "theorem_credit":False,
    "endpoint_credit":False,
}
print("GOAL4AF_BRANCH_CONIC_RECEIVER_JSON="+json.dumps(out,sort_keys=True,separators=(",",":")))
