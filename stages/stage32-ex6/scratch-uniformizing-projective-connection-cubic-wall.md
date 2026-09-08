# Stage32EX6 — uniformizing projective-connection cubic wall

Status: `SCRATCH_EXACT_BOUNDED_PROJECTIVE_CONNECTION_CUBIC_WALL_NO_ENDPOINT_CREDIT`.

This is the tenth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6.

The previous scratch leaf proved that at every FSM-minimal product-cover lift one may choose the source-locked X(8) cusp parameters so that

`q(p)=eps*(lambda*p + mu*p^3 + O(p^5))`,

with `eps in {+1,-1}`, `lambda != 0`, and locally free cubic coefficient `mu`. In particular the graph is odd and the quadratic coefficient vanishes.

The bounded question here is whether the canonical uniformizing projective structure on the modular curve globalizes that quadratic-coefficient vanishing into a zero of an intrinsic bounded-degree section.

## Source locks

Retained Stage32 modular geometry:

- Freitag--Salvati Manni identifies the relevant factor as `X(8)=H/Gamma[8]` and uses the cusp parameter
  `p=exp(2*pi*i*z/8)`;
- the second factor has the analogous parameter `q=exp(2*pi*i*w/8)`;
- the exact product-cover component `D` maps to the two X(8) factors with degrees `105` and `81`.

Standard projective-structure input:

- for a locally univalent function `f`, the Schwarzian derivative is
  `S(f)=f'''/f'-(3/2)(f''/f')^2`;
- under change of projective coordinate it gives the standard projective-connection transformation law;
- the difference of two projective connections on a Riemann surface is a quadratic differential.

This is the standard complex-projective-structure formalism; no claim is made that the retained Stage32 sources already contained this adapter.

## Canonical cusp projective connection

The Fuchsian/uniformizing projective coordinate at an X(8) cusp is `z`, with

`p=exp(2*pi*i*z/8)`.

Up to an irrelevant nonzero affine scalar,

`z = log p`.

Therefore the uniformizing projective connection in the compactifying cusp coordinate `p` is

`P(p)=S(log p,p)=1/(2*p^2)`.

The same formula holds in the second factor with cusp coordinate `q`.

Let the first projection provide the local coordinate `p` on `D` at a minimal lift. Pull the second X(8) projective connection back through `q=q(p)`. The difference

`Theta := ( P(q)*(q')^2 + S(q,p) - P(p) )*(dp)^2`

is the local expression of the difference between the two pulled-back uniformizing projective connections. Thus `Theta` is the intrinsic projective-connection replacement for the coordinate-dependent second derivative.

## Exact minimal-lift expansion

Write

`q(p)=eps*(lambda*p + mu*p^3 + O(p^5))`.

The sign `eps` and a constant rescaling of the target cusp coordinate do not affect the ratio `mu/lambda` entering the quadratic differential.

Direct expansion gives

`q'/q = 1/p + 2*(mu/lambda)*p + O(p^3)`,

so

`P(q)*(q')^2`
`= (1/2)*(q'/q)^2`
`= 1/(2*p^2) + 2*(mu/lambda) + O(p^2)`.

Also

`S(q,p)=6*(mu/lambda)+O(p^2)`.

Hence the universal cusp poles cancel and

`Theta = ( 8*(mu/lambda) + O(p^2) )*(dp)^2`.

Therefore the canonical projective globalization is regular at every FSM-minimal lift, but its value is controlled by the cubic coefficient:

`Theta(P_min)=8*(mu/lambda)*(dp)^2`.

In particular the locally forced equation `q''(0)=0` does **not** imply `Theta(P_min)=0`.

## Why the projective globalization does not create a 744-point zero count

The retained A1/FSM local model leaves `mu` free branch-by-branch. Thus `mu/lambda` is not forced to vanish or lie in a finite set.

AR gives at least `186` FSM-minimal branches downstairs and hence at least `744` product-cover minimal lifts upstairs. At all of them:

- both factor projections are unramified;
- the odd graph parity is exact;
- the pulled-back projective-connection difference `Theta` is regular;
- but its value is an unconstrained finite cubic-jet value `8*mu/lambda` rather than a forced zero.

Consequently one cannot count the 744 minimal lifts as zeros of `Theta` or of any section obtained merely by passing from the coordinate second derivative to the canonical Schwarzian/projective-connection formalism.

This is stronger than the previous globalization wall: a canonical intrinsic globalization exists, but it converts the apparently rigid quadratic-jet vanishing into the **free cubic jet**.

## Coordinate-scale check

If the source cusp coordinate is rescaled `p_tilde=a*p` and the target cusp coordinate is rescaled `q_tilde=b*q`, then

`lambda_tilde=(b/a)*lambda`,

`mu_tilde=(b/a^3)*mu`,

hence

`mu_tilde/lambda_tilde=(mu/lambda)/a^2`.

Since `(dp_tilde)^2=a^2*(dp)^2`, the tensor

`(mu/lambda)*(dp)^2`

is invariant. Thus the local value of `Theta` above is compatible with the allowed cusp-parameter rescaling and is not an artifact of a chosen scalar normalization.

## What remains genuinely untested

A useful higher-jet continuation now needs information beyond the canonical projective connection itself, for example:

1. a fixed-V6 member equation forcing `mu=0` or restricting `mu/lambda`;
2. a modular/deck identity coupling the cubic coefficients across different minimal lifts of the same member;
3. a global differential equation satisfied by the pair map whose projective-connection difference has prescribed zeros/values;
4. a higher Schwarzian / Wilczynski-type invariant whose local value is forced by the odd graph rather than by the free cubic coefficient;
5. or an independent member-level jet-separation theorem for the V6 linear system.

No such member-level cubic coupling is claimed here.

## Decision

Canonical scratch decisions:

- `UNIFORMIZING_X8_CUSP_PROJECTIVE_CONNECTION = 1_OVER_2P2`;
- `PULLEDBACK_PROJECTIVE_CONNECTION_DIFFERENCE_IS_INTRINSIC = true`;
- `UNIVERSAL_CUSP_DOUBLE_POLES_CANCEL_AT_MINIMAL_LIFT = true`;
- `PROJECTIVE_CONNECTION_DIFFERENCE_MINIMAL_VALUE = 8_MU_OVER_LAMBDA`;
- `ODD_GRAPH_QUADRATIC_VANISHING_FORCES_PROJECTIVE_ZERO = false`;
- `PROJECTIVE_CONNECTION_GLOBALIZES_SECOND_JET_BUT_EXPOSES_FREE_CUBIC = true`;
- `MINIMAL_LIFT_COUNT_UPSTAIRS >= 744`;
- `PROJECTIVE_CONNECTION_744_ZERO_COUNT = false`;
- `MEMBER_LEVEL_CUBIC_COUPLING = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The standard Schwarzian/projective-connection formalism is used only to globalize the already-retained local cusp map; it does not enlarge Stage32 authority.
- The formula `Theta(P_min)=8*mu/lambda` is a local exact expansion in the source-locked cusp chart and is not promoted to a global zero theorem.
- The 744 minimal lifts are not counted as zeros of `Theta`.
- Local freedom of `mu` is not a global realization theorem.
- No RH, delta, conductor, cusp-grid, Picard, Abel, first-order Jacobian, deck symmetry, or previous jet count is double-charged as a new `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
