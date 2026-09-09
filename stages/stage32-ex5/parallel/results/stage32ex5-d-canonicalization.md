# Stage32EX5-D canonicalization hostile check

Scope: scratch-only validation of the canonicalization component of `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`. This lane does not construct the runtime exceptional-index -> node table and grants no Stage32/receiver/FULL178 credit.

## Exact source lock

The load-bearing runtime convention is Michael Stoll's `Verification/Cuboids/cuboids.magma` at commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd` (blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`). It fixes projective coordinate order `[a1,a2,a3,b1,b2,b3,c]`, defines the four surface quadrics, computes `pts := Points(SingularSubscheme(S))`, asserts `#pts eq 48`, and defines nine exact coordinate substitutions used to permute the known curves and singular points.

The inherited EX5 checkpoint is `bc2-01a-exceptional-pairing-bridge.json` at scaffold commit `d12bde289f471a53fd149381089847b00f92d6e0`, where BC2-01B requires a 48/48 runtime-index-to-projective-node bijection plus permutation-invariant exact canonicalization.

## Canonicalization

For any nonzero projective representative

`v = [a1,a2,a3,b1,b2,b3,c]`

over the runtime field, scan the fixed named coordinate order from left to right. Let `v_j` be the first nonzero coordinate and define

`K(v) = (v_1/v_j, ..., v_7/v_j)`.

This is exact and field-independent. For every nonzero scalar `lambda`,

`K(lambda v) = K(v)`,

because the first nonzero position is unchanged and the common scalar cancels.

The named coordinate order is part of the contract. A different coordinate convention must first be transported back by an explicit coordinate adapter. Arbitrary coordinate permutations are not silently quotiented.

## Independent 48-node reconstruction/check

The verifier reconstructs six 8-point families over `Q(i)`:

- `[1,0,0,0,a,b,c]`;
- `[0,1,0,a,0,b,c]`;
- `[0,0,1,a,b,0,c]`;
- `[0,1,s*i,0,a*i,b,0]`;
- `[1,0,s*i,a*i,0,b,0]`;
- `[1,s*i,0,a*i,b,0,0]`;

with independent signs in `{+1,-1}`.

It checks all 48 satisfy the four defining quadrics and have Jacobian rank exactly 3. Together with Stoll's exact `#pts eq 48` source assertion, these are the full singular-node target set. Canonical keys are collision-free: `48 -> 48`.

Zero-coordinate edge cases are explicit: first-nonzero pivots occur `24` times at `a1`, `16` at `a2`, and `8` at `a3`; no node needs a `b` or `c` pivot.

## Hostile symmetry test

The tempting stronger interpretation of “permutation-invariant” is wrong.

Using Stoll's nine exact coordinate-substitution generators, each generator permutes the 48 canonical keys bijectively. The generated action has one orbit of size `48`. Therefore any canonicalizer made invariant under the full geometric node-permutation action would identify all 48 nodes and produce only one orbit key. That directly contradicts BC2-01B's required 48/48 node identity.

Independent coordinate sign changes are also not projective equivalences. The six sign generators move respectively `24,24,24,32,32,32` of the 48 canonical keys. Complex conjugation likewise permutes the node set rather than fixing every node.

Hence geometric automorphisms and Galois act **equivariantly**, not invariantly, on the canonical node identities.

## Maximal justified invariance

For BC2-01B, the exact justified contract is:

1. invariant under common nonzero projective scaling;
2. invariant under permutation/reordering of the 48-element runtime list once each point is expressed in the fixed named coordinate convention;
3. collision-free on the 48 nodes;
4. equivariant, not invariant, under geometric/Galois permutations of distinct nodes.

If a runtime reorders `pts`, the numeric index necessarily follows that reordering. The stable identity is the canonical coordinate key. Therefore lanes B/C must export/recover `runtime index -> exact point -> canonical key`; lane D cannot and should not try to make the raw numeric index invariant.

## Result

`PASS` for the canonicalization component only.

The over-strong full-symmetry invariant is rejected by an exact 48-to-1 collapse counterexample. The fixed-coordinate first-nonzero projective key satisfies the required scale/list-order invariance with no collisions.

BC2-01B itself remains pending until mainbatch has an independently validated 48/48 runtime exceptional-index -> exact point -> canonical-key table. FULL178 span replay remains forbidden before that bridge is complete.

Replay:

`python stages/stage32-ex5/parallel/results/verify_stage32ex5_d_canonicalization.py`
