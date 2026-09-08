# Stage32EX6 — projective-connection nonzero and six-jet anti-flatness bound

Status: `SCRATCH_EXACT_BOUNDED_PROJECTIVE_NONZERO_ANTIFLATNESS_NO_ENDPOINT_CREDIT`.

This is the thirteenth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` and the same exact `q'=4` normalized product-cover component `D` used throughout EX6.

This leaf uses the immediately previous scratch projective-connection pole-budget calculation only as scratch-local input. In particular it uses:

- `g(D)=533`;
- at least `186` FSM-minimal node branches downstairs, hence at least `744` minimal product-cover lifts;
- the intrinsic meromorphic quadratic differential `Theta`, defined as the difference of the two pulled-back uniformizing projective connections from the two `X(8)` factors;
- at every minimal lift, in source-locked modular cusp coordinates,
  `q(p)=eps*(lambda*p+mu1*p^3+mu2*p^5+...)`;
- if `mu1=...=mur=0`, then `ord_P(Theta)>=2r`;
- writing `Rrho=rho81+rho105`, the previous scratch leaf gives
  `0<=Rrho<=80`,
  `deg Pole(Theta)<=3392+32*Rrho<=5952`,
  and hence for nonzero `Theta`,
  `deg Zero(Theta)<=5520+32*Rrho<=8080`.

The bounded question here is whether the remaining firewall

`Theta identically 0 implies V6 impossibility = UNTESTED`

can already be discharged from the same pole calculation, and what unconditional member-level jet restriction then follows.

## Theta is forced nonzero

The previous scratch pole-budget leaf gives the exact smooth-boundary normalization-point counts

- degree-81 direction: `s81=58+rho81`;
- degree-105 direction: `s105=154+rho105`.

The two boundary families meet only at node geometry, so these smooth supports are disjoint. Every such normalization point has eight lifts to `D`, and exactly one of the two projections lands at an `X(8)` cusp.

Therefore the number of one-cusp smooth lifts is exactly

`8*(s81+s105)`
`=8*(212+Rrho)`
`=1696+8*Rrho`.

In particular this number is always at least `1696`.

At each such point the previous local projective-connection calculation gives an **exact double pole** of `Theta`: the cusp-side pulled-back connection has universal double-pole coefficient `1/2`, while the interior-side pullback has coefficient `(1-e^2)/2`; their difference has nonzero double-pole coefficient `e^2/2` up to sign.

Hence `Theta` has at least one pole, indeed at least `1696` distinct double-pole points. Consequently

`Theta != 0`

as a meromorphic quadratic differential on `D`.

Thus the previous firewall is discharged at scratch level:

`THETA_IDENTICALLY_ZERO_COMPATIBLE_WITH_O266 = false`.

No global monodromy or commensurator theorem is needed for this conclusion; the one-cusp local pole already forbids identical vanishing.

## Six-jet flatness cannot hold at all guaranteed minimal lifts

Because `Theta` is now known nonzero in this scratch model, the divisor upper bound applies without a conditional nonzero branch:

`deg Zero(Theta)<=5520+32*Rrho<=8080`.

Call a minimal lift **6-flat** if

`mu1=mu2=mu3=mu4=mu5=mu6=0`.

At every 6-flat minimal lift,

`ord_P(Theta)>=12`.

Let `F6` be the number of 6-flat minimal lifts. Distinct minimal lift points contribute disjoint zero multiplicities, so

`12*F6 <= deg Zero(Theta)`.

Hence the exact parameter-dependent bound is

`F6 <= floor((5520+32*Rrho)/12)`.

Using only the endpoint-uniform `Rrho<=80`,

`F6 <= floor(8080/12)=673`.

But the retained AR bound gives at least `744` minimal lifts. Therefore at least

`744-673 = 71`

of the guaranteed minimal lifts are **not** 6-flat.

Equivalently, at least 71 guaranteed minimal lifts satisfy

`(mu1,mu2,mu3,mu4,mu5,mu6) != (0,0,0,0,0,0)`.

This is an actual scratch-level necessary member condition, not a counterfactual threshold test.

## Conditional closure theorem for any future six-jet forcing input

Suppose a future source-locked fixed-V6 theorem forced

`mu1=...=mu6=0`

at every guaranteed minimal lift. Then all at least `744` minimal lifts would be 6-flat and would force zero multiplicity at least

`12*744=8928`.

Since `Theta` is forced nonzero and its total zero degree is at most `8080`, this is impossible.

Therefore, within the exact scratch adapter chain,

`UNIFORM_SIX_HIGHER_ODD_JET_VANISHING_ON_ALL_GUARANTEED_MINIMAL_LIFTS`

would directly exclude the O266 hypothetical carrier; no additional `Theta identically 0 -> impossibility` theorem is needed.

This is only a conditional closure criterion because no such six-jet forcing theorem has been obtained.

## What remains genuinely missing

The projective-connection route has now been reduced to a concrete member-level target rather than a global projective-correspondence target:

1. prove enough fixed-V6 local equations / modular differential identities to force six-jet flatness on all guaranteed minimal lifts; or
2. obtain a stronger partial flatness count exceeding the parameter-dependent capacity
   `floor((5520+32*Rrho)/(2r))` for some `r`; or
3. independently reduce `Rrho`, which lowers the zero-capacity and correspondingly lowers the required jet strength.

The existing retained/scratch local A1 model leaves higher coefficients free and does not provide any of these inputs.

## Decision

Canonical scratch decisions:

- `ONE_CUSP_SMOOTH_LIFT_COUNT = 1696+8*(rho81+rho105)`;
- `ONE_CUSP_SMOOTH_LIFT_COUNT_MIN = 1696`;
- `ONE_CUSP_SMOOTH_LIFTS_FORCE_THETA_NONZERO = true`;
- `THETA_IDENTICALLY_ZERO_COMPATIBLE_WITH_O266 = false`;
- `THETA_ZERO_DEGREE_UNIFORM_UPPER = 8080`;
- `SIX_FLAT_MINIMAL_LIFT_ZERO_ORDER_MIN = 12`;
- `SIX_FLAT_MINIMAL_LIFT_COUNT_UNIFORM_MAX = 673`;
- `GUARANTEED_MINIMAL_LIFT_COUNT_MIN = 744`;
- `GUARANTEED_MINIMAL_LIFTS_NOT_SIX_FLAT_MIN = 71`;
- `UNIFORM_SIX_JET_FLATNESS_WOULD_EXCLUDE_O266 = true`;
- `UNIFORM_SIX_JET_FLATNESS_ACTUALLY_PROVED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- This leaf depends on prior scratch projective-connection local/pole adapters; it is not independent retained authority.
- The 71-point anti-flatness statement is upstairs on `D`; it is not silently divided by four into a downstairs branch count without an additional deck-equivariance adapter.
- No six-jet vanishing theorem is claimed.
- The conditional statement `uniform six-jet flatness would exclude O266` is not promoted to actual endpoint exclusion.
- No RH, delta, conductor, cusp-grid, Picard, Abel, deck symmetry, or previous jet count is recharged as a new `eta/rho` cap.
- No Stage32 MAIN, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
