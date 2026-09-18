# Stage32 MB104 — H5 exact etale-correspondence quotient-rigidity shallow gate — 2026-09-18

Status: **H5 SHALLOW GATE FAIL / PARKED / H6 NEXT / NO MATHEMATICAL CREDIT**

## Gate tested

H5 asks whether every exact active MB104 carrier can be converted into a source-complete equivariant finite etale self-correspondence of the fixed genus-five factor `C8`, and whether the allowed correspondence classes are finite or effectively bounded strongly enough to close all `l` or leave an explicit finite backend.

The gate is deliberately stronger than the already-retained equality-rigidity statement.

## Forward adapter to a bare correspondence passes

For an actual balanced equality carrier,

```
d=r_odd=112l,
```

the retained Beauville equality argument gives a connected component `Z` in `C8 x C8` whose two projections are finite etale of equal degree

```
n=14 e l.
```

On the current active support `000707000f0f`, the retained frontier has

```
e in {2,4},
n=28l or 56l.
```

So

```
actual carrier -> bare equal-degree etale correspondence
```

is not the missing step.

## Ambient C8 does not provide finiteness

The external-source adapter `MB104-H5-ARITHMETIC-SELF-CORRESPONDENCE-SOURCE-NOTE-20260918.md` records:

1. `C8=X(8)` is the Wiman genus-five curve;
2. the full automorphism quotient has signature `(2,3,8)`;
3. `Delta(2,3,8)` is arithmetic;
4. hence the compact surface group uniformizing `C8` is arithmetic;
5. its commensurator is dense, and commensurator elements give finite holomorphic self-correspondences.

Therefore there is no finite ambient list, nor an ambient degree cutoff, for finite etale self-correspondences of `C8`.

H5 can succeed only if the exact MB104 quotient/passport data cut this infinite universe down to a finite or effectively bounded subset.

## The exact packet-to-correspondence adapter fails

That load-bearing reduction is not currently source-complete.

### Historical finite split was retracted

The repaired six-branch passport explicitly withdraws

```
u_q=8l*m_q.
```

The invalid step was concentration: all `8l` normalization branches through one box node were assumed to descend to one fixed quotient branch value. The retained data do not prove this. Different normalization branches can lift to different fixed points in the product-cover fibre.

Therefore the old finite six-integer/Nielsen reduction cannot be reused.

### Current 000707 e=2 passport is stronger, but still aggregate

For the active `000707` support, the exact e=2 base-change passport proves that the `112l` supported branches exhaust all unramified points over the eight `H`-branch values. It also gives exact totals and parity constraints.

But it does not attach each normalization branch source-completely to one product-cover fixed lift. Its own firewalls state that determinant/sign monodromy does not recover the pointwise conductor/gluing character.

The current residual-deck note makes the remaining datum explicit:

```
M_(u,v) in G=Gamma[4]/Gamma[8]
```

for each conductor identification, or equivalently the two limiting residual lift values. This transition is still missing.

Thus the current data determine

```
aggregate branch-value capacity / parity
```

but not

```
exact branch -> fixed product lift -> quotient/Nielsen datum.
```

## Reverse adapter fails with the same loss

Suppose one classifies a finite set of quotient passports using only the retained aggregate totals. Different unresolved branch-to-fixed-lift assignments map to the same reduced passport.

Therefore a vanishing or impossibility statement for one artificially concentrated finite passport is not reversible to the original carrier. Conversely, admitting all unresolved allocations restores a family whose combinatorics grows with `l`; no finite H5 classification has been obtained.

This is exactly an F/R failure under the Class-3 roadmap.

## Decision

```
carrier -> bare etale correspondence: PASS
ambient fixed-C8 correspondence finiteness: FAIL
packet -> exact finite quotient/passport object: FAIL
reverse adapter: FAIL
H5 shallow gate: FAIL
H5: PARKED
finite-degree window: NOT PROVED
next: H6 finite monodromy / Nielsen-passport shallow gate
```

H5 may be reopened only with either:

1. a source-complete normalization-branch to product-cover fixed-lift adapter; or
2. a new theorem proving finiteness directly from the current aggregate `000707` data without the retracted concentration assumption.

No conductor signs are guessed, no heavy computation is released, and no MB104, receiver, effectivity, theorem, endpoint, Perfect-Cuboid, or merge credit changes.
