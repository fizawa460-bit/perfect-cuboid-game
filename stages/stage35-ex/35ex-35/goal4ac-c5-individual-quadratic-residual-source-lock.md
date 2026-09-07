# Stage35-EX Goal4AC source lock — individual C5 quadratic-section residual geometry

Scope: continue only the Goal4AB class-B `Q(i)/Q` cyclic principalization route. Goal4AC resolves the remaining *strict geometric support* question for the individual retained Stoll C5 quadratic sections. It does not compute the marked Picard classes of the C5 pairs, does not construct `F_B`, and does not promote any Brauer–Manin or E1 credit.

## Exact parent and freshness lock

- parent live Stage35-EX head before Goal4AC: `e08f399034dc2743de8bc2b2b88ebca52d3686db`;
- current main incorporated by that merge: `f8522bd1a38fa551186ad370f51d17c73c7927e2`;
- exact-head freshness replay: workflow run `34029652526`, job `101476730031`, SUCCESS;
- immutable V65 snapshot: `stages/stage35-ex/snapshots/MAIN-STATE-V65-e08f399034dc.json`, exact blob `1479da3b0dbb1ce3b60941375261e2660d7847b6`, snapshot correction commit `2901109d925442f8143b56510bcd352a0ee7e448`;
- Goal4AB artifact: `stages/stage35-ex/35ex-35/goal4ab-second-class-qi-cyclic-low-degree-rr-blocker.json`, blob `62ad3a99036bce4bd12cc11c72a48bbf2fd6d0a0`;
- Goal4AB source lock: `stages/stage35-ex/35ex-35/goal4ab-second-class-qi-cyclic-low-degree-rr-blocker-source-lock.md`, blob `e0492a5319d8a966c41992b65c7c099927a29445`;
- Goal4AB verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4ab.py`, blob `347cc43a60f7772d6c8b3f4145839cf9978b4114`.

Pinned external source remains:

- repository `MichaelStollBayreuth/Verification`;
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- path `Cuboids/cuboids.magma`;
- git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

The pinned source defines the 16 C5 curves as genus-3 nonhyperelliptic curves of degree 8 by

`L(e2,e3,e4) = a1 + e2*a2 + e3*a3 + e4*i*c = 0`,

`Q(e1,e2,e3) = (e2*a2 + e3*a3)*b1 + e1*i*b2*b3 = 0`,

with `e1,e2,e3,e4 in {+1,-1}`.

The Stage35 coordinate adapter remains

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`.

## Scalar-equivalent quadratic sections

There are eight sign triples `(e1,e2,e3)`, but

`Q(-e1,-e2,-e3) = -Q(e1,e2,e3)`.

Hence they define exactly four distinct projective quadratic sections.

For a fixed representative `(e1,e2,e3)`, the same quadratic section contains the four C5 curves

- `C(e1,e2,e3,+1)`,
- `C(e1,e2,e3,-1)`,
- `C(-e1,-e2,-e3,+1)`,
- `C(-e1,-e2,-e3,-1)`.

The first pair is the pair visible from the chosen sign triple. The second pair is exactly the antipodal pair that Goal4AB had left as a possible degree-16 residual.

## Exact support exhaustion

Goal4AB already verified, modulo the four defining quadrics of the cuboid surface, the four identities

`prod_{e4=±1} L(e2,e3,e4) * prod_{e4=±1} L(-e2,-e3,e4)`

`= 4 * Q(+1,e2,e3) * Q(-1,e2,e3)`.

Restricting to one of the two quadratic factors forces the product of the four corresponding linear factors to vanish. Thus the reduced support of that quadratic section is contained in the four C5 intersections listed above.

The projective cuboid surface is a complete intersection of four quadrics in `P^6`, so `deg(S)=16`; a proper quadratic section has degree 32. The four retained C5 curves are distinct and each has degree 8, so their total degree is exactly 32. Therefore there is no room for any further one-dimensional component or higher generic multiplicity: the individual quadratic section is exhausted by those four C5 curves.

Equivalently, after removing the two C5 curves attached to a chosen sign triple, the strict degree-16 residual is exactly the antipodal C5 pair. Across the four scalar-equivalence classes, the 16 retained C5 curves are partitioned exactly once.

## Firewall

Goal4AC proves only this strict-support decomposition. It does **not** prove that the antipodal C5-pair class lies in the old rank-31 linear-section span, nor does it compute its exact marked Picard-64 coordinates or its exceptional total-transform correction. Consequently it does not yet decide whether adjoining these four pair classes helps synthesize the fixed 69-support target `V_B`.

Still unproved/uncomputed:

- exact marked Picard classes of the four C5 residual pairs;
- target-span test after adjoining those classes;
- general graded-coordinate-ring/Riemann–Roch principal-function synthesis;
- explicit `F_B`;
- full `Br_a(U)`, local evaluations, verticality, Brauer–Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.

The next smallest exact leaf is therefore a marked-Picard adapter for these four now-explicit C5 pair divisors, before broadening to the general graded-coordinate-ring synthesis.
