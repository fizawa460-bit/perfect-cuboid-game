# Stage32 scratch — B.7/B.8 unbound ordered-pair orbit on retained J[2]

Status: scratch exact finite diagnostic only. No MAIN authority, claim-DAG, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Input

This leaf starts from `b7-b8-j2-retained-w-intertwiner-20260908.json`, which already derived the Cecotti B.7/B.8 branch-marked `J[2]` action and showed:

- if the literal ordered identification `B.7 -> S`, `B.8 -> T` is supplied, exactly two `GL4(F2)` intertwiners exist;
- both send `delta_0inf=Z3` to retained `L3`, hence conditionally to Q602 residue `235`;
- the missing semantic datum is precisely the source-bound ordered generator marking.

The present diagnostic asks whether that missing marking is merely cosmetic. It drops the literal `S,T` choice and allows every retained ordered generator pair compatible with the same exact `J[2]` module action.

## Exact exhaustion

Let `G=<S,T>` in the retained mod-2 representation. Exact enumeration gives `|G|=24` and `|GL4(F2)|=20160`.

For every `P in GL4(F2)`, form

`(s,t)=(P B7 P^-1, P B8 P^-1)`.

Retain exactly those `P` for which `s,t in G` and `<s,t>=G`.

Result:

- admissible intertwiners: `48`;
- distinct ordered pairs `(s,t)`: `24`;
- every ordered pair occurs with multiplicity `2`;
- these 24 pairs are exactly the full inner-conjugacy orbit of the literal pair `(S,T)`;
- `P(delta_0inf)` lands on `L1/L2/L3` with counts `16/16/16`.

Restricting back to the literal pair `(S,T)` leaves exactly the previous two intertwiners, both with `delta_0inf -> L3`.

## Decision

The ordered-generator source binding is load-bearing, not cosmetic. Exact simultaneous `J[2]` action matching plus abstract identification with the retained mod-2 G12 image still leaves the full three-line ambiguity once the literal ordered marking is forgotten.

Thus this leaf gives the bounded obstruction

`UNBOUND_ORDERED_GENERATOR_ORBIT_DOES_NOT_SELECT_ABSOLUTE_W_LINE`.

It does **not** identify an absolute residue and does not exclude Q602 or O210.

The next exact re-entry datum remains a source-bound ordered identification of the curve automorphisms with the retained principal generators, or an equivalent marked-Jacobian adapter.

Replay:

`python3 stages/stage32/scratch/diagnose_stage32_b7_b8_unbound_pair_orbit.py`
