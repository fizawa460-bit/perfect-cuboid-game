# Stage32EX6 — projective-connection zero-capacity wall

Status: `SCRATCH_EXACT_BOUNDED_PROJECTIVE_ZERO_CAPACITY_WALL_NO_ENDPOINT_CREDIT`.

This is the eleventh isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6, and let `D` be the exact `q'=4` normalized product-cover component.

Retained inputs:

- `g(D)=533`;
- at least `186` FSM-minimal branches downstairs;
- hence at least `744` corresponding product-cover lift points;
- at each minimal lift the source-locked cusp graph is odd,
  `q(p)=eps*(lambda*p + mu1*p^3 + mu2*p^5 + mu3*p^7 + ...)`,
  with `lambda != 0`;
- the previous scratch leaf constructs the intrinsic difference `Theta` of the two pulled-back uniformizing projective connections and gives
  `Theta(P_min)=8*(mu1/lambda)*(dp)^2`.

The bounded question here is not whether `mu1` is actually forced to vanish. It is stronger and counterfactual:

> Even if a future member-level equation forced `mu1=0` at every minimal lift, would the resulting projective-connection zero count already contradict the genus-533 global degree?

## Exact local expansion one order deeper

Using

`Theta = ( P(q)*(q')^2 + S(q,p) - P(p) )*(dp)^2`,

with the cusp projective connection `P(r)=1/(2r^2)`, direct expansion for

`q(p)=eps*(lambda*p + mu1*p^3 + mu2*p^5 + mu3*p^7 + O(p^9))`

gives

`Theta/(dp)^2`
`= 8*mu1/lambda`
`  + 8*(-9*mu1^2 + 8*mu2*lambda)/lambda^2 * p^2`
`  + 8*(47*mu1^3 - 71*mu1*mu2*lambda + 27*mu3*lambda^2)/lambda^3 * p^4`
`  + O(p^6)`.

Consequences:

1. if `mu1` is arbitrary, the value is the already-retained `8*mu1/lambda`;
2. if `mu1=0`, then
   `Theta = (64*mu2/lambda)*p^2*(dp)^2 + O(p^4)`,
   so every such point is forced to be a zero of order at least two, but not higher when `mu2 != 0`;
3. if `mu1=mu2=0`, then
   `Theta = (216*mu3/lambda)*p^4*(dp)^2 + O(p^6)`,
   so every such point is forced to be a zero of order at least four.

Thus odd parity makes the projective-connection zero orders jump in even steps.

## Best-case holomorphic global capacity

For the exact product-cover genus

`g(D)=533`,

the canonical bundle has degree

`deg K_D = 2g(D)-2 = 1064`,

so

`deg K_D^2 = 4g(D)-4 = 2128`.

Therefore any nonzero **holomorphic** quadratic differential on `D` has total zero degree exactly `2128`.

This holomorphic model is deliberately optimistic for contradiction. The actual modular uniformizing projective-connection difference may be meromorphic on the compactification because cusp/ramification pullbacks can contribute poles; allowing poles only increases the available zero degree. Hence failure already in the holomorphic best case is a rigorous dominance wall for the naive zero-count route.

## Cubic vanishing alone is quantitatively insufficient

There are at least `744` minimal lifts.

Counterfactually force

`mu1=0`

at every one of them. The guaranteed projective-connection zero multiplicity is then only two per point, so the forced zero count is

`2*744 = 1488`.

But

`1488 < 2128`.

Therefore even in the strongest favorable setting where `Theta` is holomorphic and nonzero, forcing the cubic correction `mu1` to vanish at every minimal lift does **not** exceed the global quadratic-differential zero capacity.

Hence a future fixed-V6 member equation whose sole new consequence is

`mu1=0 at all minimal lifts`

cannot close O266 via this projective-connection divisor count.

## What strength would first become interesting

If one could instead force

`mu1=mu2=0`

at every minimal lift, then each point would contribute at least four zeros and

`4*744 = 2976 > 2128`.

Thus in the idealized holomorphic/nonzero model this would force `Theta` to vanish identically.

However this is **not** yet an O266 contradiction for two reasons:

1. the actual compactified modular `Theta` may be meromorphic, so its pole divisor must first be source-locked before using the `2128` holomorphic threshold;
2. even `Theta identically 0` would require a separate theorem translating equality of the two pulled-back projective structures into an impossibility for the fixed V6 pair map.

Accordingly `mu1=mu2=0` is only the first jet-strength level that could become globally competitive after a genuine pole/control adapter.

## Standard projective-connection input

The only external standard fact used beyond the previous scratch leaf is that the difference of two projective connections is a quadratic differential. The genus-degree calculation then uses `deg K_D=2g-2`.

No external theorem is promoted into retained Stage32 authority here.

## Decision

Canonical scratch decisions:

- `PRODUCT_COVER_GENUS_D = 533`;
- `HOLOMORPHIC_QUADRATIC_ZERO_CAPACITY = 2128`;
- `MINIMAL_LIFT_COUNT_UPSTAIRS >= 744`;
- `MU1_ZERO_FORCES_THETA_ZERO_ORDER_AT_LEAST = 2`;
- `MU1_ZERO_ALL_MINIMAL_FORCED_ZERO_COUNT >= 1488`;
- `1488_LT_2128 = true`;
- `CUBIC_COEFFICIENT_VANISHING_ALONE_CLOSES_PROJECTIVE_ROUTE = false`;
- `MU1_MU2_ZERO_FORCES_THETA_ZERO_ORDER_AT_LEAST = 4`;
- `MU1_MU2_ZERO_ALL_MINIMAL_IDEALIZED_ZERO_COUNT >= 2976`;
- `2976_GT_2128 = true`;
- `ACTUAL_PROJECTIVE_CONNECTION_POLE_DIVISOR_SOURCE_LOCKED = false`;
- `THETA_IDENTICALLY_ZERO_IMPLIES_V6_IMPOSSIBLE = UNTESTED`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The assumptions `mu1=0` and `mu1=mu2=0` are counterfactual strength tests, not new constraints actually proved for V6.
- The `2128` threshold is used only as an optimistic holomorphic benchmark; the actual compactified modular projective-connection difference is not claimed holomorphic.
- No meromorphic pole degree is invented or silently ignored in a positive exclusion claim.
- `2976>2128` is not promoted to an endpoint contradiction because neither `mu1=mu2=0` nor holomorphicity/nonzero `Theta` is source-locked.
- No RH, delta, conductor, cusp-grid, Picard, Abel, first-order Jacobian, deck symmetry, or previous jet count is double-charged as a new `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
