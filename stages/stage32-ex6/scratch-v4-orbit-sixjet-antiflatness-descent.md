# Stage32EX6 — V4-orbit descent of projective six-jet anti-flatness

Status: `SCRATCH_EXACT_BOUNDED_V4_ORBIT_PROJECTIVE_ANTIFLATNESS_NO_ENDPOINT_CREDIT`.

This is the fourteenth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` and exact `q'=4` normalized product-cover component `D` used throughout EX6.

The previous scratch leaf proved:

- the meromorphic quadratic differential `Theta` (difference of the two pulled-back X(8) uniformizing projective connections) is nonzero;
- `deg Zero(Theta) <= 5520 + 32*Rrho`, where `Rrho=rho81+rho105` and `0<=Rrho<=80`;
- therefore `deg Zero(Theta) <=8080` uniformly;
- at an FSM-minimal product-cover lift, if the first six higher odd graph coefficients vanish, then `ord_P(Theta)>=12`.

That leaf deliberately did not divide the resulting upstairs anti-flatness count by four because deck-equivariance had not yet been source-locked.

This leaf resolves exactly that firewall.

## Source-locked V4 cover

Retained Stage32 source `post1473-specific-class-multibranch-beauville-odd-branch-wall.md` records from Freitag--Salvati Manni that

- `P=X(8) x X(8)` admits a free action of
  `G=Gamma'[4]/Gamma[8] ~= (Z/2)^2`;
- the quotient is the Beauville surface `X`;
- hence `P -> X` is an unramified degree-4 Galois cover.

For the hypothetical carrier, let `Y` be the connected normalized Beauville pullback and let `D` be a connected component of the normalized pullback through `P->X`.

Retained Stage32 proves that the exact V6 factor degrees force

`q' = deg(D->Y)=4`.

Standard finite-etale Galois pullback theory then gives:

- the pullback of the G-torsor `P->X` to `Y` is a G-torsor;
- because the chosen component `D` is connected and has full degree `|G|=4`, it is the whole connected pullback;
- therefore `D->Y` itself is a free Galois `V4` cover with deck group `G`.

No stronger group identification is invented: this is exactly the full-degree connected pullback of the retained free `V4` quotient.

## Four lifts of every O266 node branch form one V4 orbit

At O266 every node contact on the normalization `N` is odd, so the connected Beauville double cover `Y->N` is ramified there. Consequently each O266 node branch has exactly one point on `Y` above it.

The cover `D->Y` is unramified degree four and a free V4 torsor. Hence the four product-cover lifts above each O266 node branch form one free V4 orbit.

In particular every FSM-minimal downstairs node branch `(A,B)=(1,1)` gives exactly one four-point minimal-lift orbit on `D`.

Since retained AR gives at least `186` FSM-minimal node branches, there are at least `186` such V4 orbits, i.e. at least `744` minimal lifts.

## Theta is V4-invariant

The V4 action on `P=X(8)xX(8)` is induced by modular automorphisms and acts diagonally on the two factors.

Let `P_X8` denote the uniformizing projective connection on `X(8)`. A modular automorphism is induced by a fractional-linear transformation of the uniformizing upper-half-plane coordinate, hence preserves the uniformizing projective structure and therefore

`alpha^* P_X8 = P_X8`

for every relevant factor automorphism `alpha`.

Write the two projections as `pi105, pi81:D->X(8)` and

`Theta = pi81^*P_X8 - pi105^*P_X8`

in invariant projective-connection notation.

For any deck element `g in V4`, the diagonal action gives

`pi_i o g = alpha_g o pi_i`.

Therefore

`g^*Theta = Theta`.

Thus the divisor of `Theta`, and in particular `ord_P(Theta)`, is constant on every four-point V4 orbit.

This invariant order, rather than the coordinate tuple `(mu1,...,mu6)` itself, is the correct object for downstairs descent.

## Projectively six-flat orbits

Call a minimal lift **projectively 6-flat** when

`ord_P(Theta)>=12`.

This condition is V4-invariant, so projectively 6-flat minimal lifts occur in complete four-point orbits.

Let `H12` be their total number among all minimal lifts. Since `Theta` is nonzero,

`12*H12 <= deg Zero(Theta) <= 5520+32*Rrho`.

Because `H12` is divisible by four, the number of projectively 6-flat minimal **branch orbits** satisfies

`B12 <= floor((5520+32*Rrho)/48)`.

Using only `Rrho<=80`,

`B12 <= floor(8080/48)=168`.

But there are at least `186` minimal branch orbits. Hence at least

`186-168 = 18`

FSM-minimal downstairs node branches have

`ord_P(Theta)<12`

at all four of their product-cover lifts.

Equivalently, the previous upstairs anti-flatness bound descends exactly to a branch-level statement:

`PROJECTIVELY_NON_6_FLAT_MINIMAL_BRANCHES >=18`.

The parameter-dependent sharpened form is

`PROJECTIVELY_NON_6_FLAT_MINIMAL_BRANCHES`
`>= 186 - floor((5520+32*Rrho)/48)`.

For example, at `Rrho=0` this gives at least

`186-floor(5520/48)=186-115=71`

downstairs minimal branches.

## Relation to coefficient six-flatness

The previous local jet calculation proves at each minimal lift

`mu1=...=mu6=0  => ord_P(Theta)>=12`.

Therefore every lift with `ord_P(Theta)<12` is certainly not coefficient-six-flat.

Hence the at least 18 branch orbits above have the stronger property that **none of their four product-cover lifts can satisfy**

`mu1=...=mu6=0`.

This does not assert that the raw coefficient tuple is itself deck-invariant; that stronger coordinate statement is unnecessary.

## Conditional closure criterion, now downstairs

Any future source-locked member theorem that forces projective six-flatness (`ord Theta>=12`), or the sufficient coefficient condition `mu1=...=mu6=0`, on all retained `>=186` FSM-minimal downstairs branches would contradict the branch-orbit capacity above.

More generally, if such a theorem forced six-flatness on more than

`floor((5520+32*Rrho)/48)`

minimal branches, O266 would be excluded within this adapter chain.

No such member-level forcing theorem is currently obtained.

## Decision

Canonical scratch decisions:

- `PRODUCT_COVER_D_TO_Y_FULL_DEGREE4_CONNECTED_PULLBACK_IS_V4_TORSOR = true`;
- `O266_NODE_BRANCH_PRODUCT_LIFTS_FORM_V4_ORBIT_OF_SIZE4 = true`;
- `THETA_V4_INVARIANT = true`;
- `THETA_ORDER_CONSTANT_ON_FOUR_LIFT_ORBIT = true`;
- `PROJECTIVE_6_FLAT_BRANCH_ORBIT_CAP = floor((5520+32*Rrho)/48)`;
- `PROJECTIVE_6_FLAT_BRANCH_ORBIT_UNIFORM_MAX = 168`;
- `FSM_MINIMAL_DOWNSTAIRS_BRANCH_COUNT_MIN = 186`;
- `PROJECTIVELY_NON_6_FLAT_MINIMAL_BRANCHES_UNIFORM_MIN = 18`;
- `COEFFICIENT_SIX_FLAT_LIFT_ABSENT_ON_AT_LEAST_18_MINIMAL_BRANCH_ORBITS = true`;
- `UNIFORM_SIX_JET_FLATNESS_ON_ALL_MINIMAL_BRANCHES_WOULD_EXCLUDE_O266 = true`;
- `UNIFORM_SIX_JET_FLATNESS_ACTUALLY_PROVED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The V4 torsor statement is conditional on the same hypothetical carrier and follows from full-degree connected pullback of the retained free V4 quotient.
- The deck-invariant object is `ord(Theta)`, not the raw chosen cusp-coordinate coefficient tuple.
- The downstairs count is not obtained by naively dividing 71 by four; it is recomputed using V4 invariance and the divisor budget, giving the exact uniform minimum 18 branch orbits.
- No member equation forcing six-flatness is claimed.
- No prior RH, delta, conductor, cusp-grid, Picard, Abel, or jet budget is double-charged as a new eta/rho cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until retained consolidation and hostile audit.
