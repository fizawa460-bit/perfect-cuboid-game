# Stage32EX6 — genus-one off-special ramification Picard/effectivity wall

Status: `SCRATCH_EXACT_BOUNDED_RHO_PICARD_EFFECTIVITY_WALL_NO_ENDPOINT_CREDIT`.

This is the fifth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `N` be its normalization. For either retained factor direction, write

`f_i : N -> P1`

for the degree `n_i` map, with `n_81=81` and `n_105=105`.

The retained AR source lock defines the factor ramification split into special-fibre and off-special pieces. At O266 (`t=0`) the scalar identities are

`52 = q81_node + eta81 + rho81`,

`28 = q105_node + eta105 + rho105`,

where `rho_i` is exactly the total ramification away from the six special fibres in that factor direction.

The bounded question here is whether the genus-one Picard/Abel class of the off-special ramification divisor itself can impose a new numerical upper bound on `rho_i`.

## Exact residual ramification line bundle

Let `R_i` be the full ramification divisor of `f_i`, and let `R_i,special` be its effective special-fibre part in the exact AR decomposition. Then

`R_i = R_i,special + R_i,off`,

with

`deg R_i,off = rho_i`.

Riemann-Hurwitz gives

`K_N = f_i^* K_P1 + R_i`.

Since `N` has genus one, `K_N` has degree zero and is trivial after choosing the standard elliptic canonical trivialization. Therefore, if `F_i` denotes the fibre divisor class of `f_i`,

`O_N(R_i) ~= O_N(2F_i)`,

and hence

`O_N(R_i,off) ~= O_N(2F_i - R_i,special)`.

Thus the off-special ramification is not arbitrary support: its Picard class is fixed once the actual member-level special ramification divisor is fixed.

## Positive degree is automatically effective on genus one

For a line bundle `L` of positive degree `r` on a smooth projective genus-one curve, Riemann-Roch and Serre duality give

`h0(L)-h0(L^(-1)) = r`.

Because `deg L^(-1)=-r<0`, one has `h0(L^(-1))=0`, so

`h0(L)=r>0`.

Therefore every positive-degree line-bundle class on `N` has an effective divisor representative.

Applied to

`L_i,off := O_N(2F_i - R_i,special)`,

this means:

- if `rho_i>0`, the Picard class of the residual divisor alone cannot obstruct effectivity;
- in fact `h0(L_i,off)=rho_i`;
- no class-only upper bound on positive `rho_i` follows.

This is the genus-one reason a direct Picard/effectivity attack on `rho` does not improve the retained scalar slack.

For a standard source reference, this is the genus-one specialization of Riemann-Roch; see the Stacks Project, Tag `0BS6`.

## The degree-zero corner is different

If `rho_i=0`, then `L_i,off` has degree zero. An effective divisor of degree zero must be zero, so the actual residual ramification vanishes only if

`O_N(2F_i - R_i,special) ~= O_N`.

Equivalently, the corresponding degree-zero Abel/Picard class must vanish.

Thus member-level Abel data could test a **zero-rho corner**. But this is not an upper bound on general positive `rho_i`, and the current O266 scalar system does not force either `rho_i` to be zero.

Indeed the already-retained feasible scalar residual choice

`q81_node=0, eta81=0, rho81=52`,

`q105_node=0, eta105=0, rho105=28`

has both residual degrees positive. Picard effectivity supplies no contradiction to that scalar corner.

This statement does not construct global factor maps realizing that corner; it only shows that positive residual degree has no generic genus-one line-bundle effectivity obstruction.

## Consequence for route selection

The direct genus-one Picard route produces a structural constraint but no closing inequality:

1. `R_i,off` has the exact member-level class `2F_i-R_i,special`;
2. if `rho_i>0`, every such degree-`rho_i` class is automatically effective;
3. only `rho_i=0` exposes a degree-zero Abel-class equality;
4. current O266 slack allows positive `rho81` and positive `rho105` simultaneously.

Therefore a useful `rho` continuation must use more than line-bundle degree/effectivity. It would need actual marked-point Abel sums, torsion/symmetry restrictions on the special fibres, a branch-value relation, higher jets, or another member-level condition that restricts the **specific** effective divisor rather than merely its Picard class.

The argument is downstairs on the genus-one normalization `N`. It does not claim that every analogous positive-degree line bundle on the genus-533 product-cover component `D` is automatically effective.

## Decision

Canonical scratch decisions:

- `RHO_OFFSPECIAL_LINE_BUNDLE_CLASS = 2F_MINUS_R_SPECIAL`;
- `GENUS1_POSITIVE_DEGREE_LINE_BUNDLE_EFFECTIVE = true`;
- `POSITIVE_RHO_PICARD_EFFECTIVITY_OBSTRUCTION = false`;
- `RHO_ZERO_REQUIRES_TRIVIAL_RESIDUAL_PICARD_CLASS = true`;
- `CURRENT_O266_SLACK_FORCES_RHO_ZERO = false`;
- `DIRECT_GENUS1_PICARD_ROUTE_BOUNDS_RHO = false`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier or global factor map is constructed.
- Automatic positive-degree effectivity is used only on the genus-one normalization `N`.
- The result does not say every prescribed support realizes the line bundle; only some effective representative exists.
- A zero-rho Abel-class test is not silently promoted to a positive-rho bound.
- No total RH, delta, conductor, cusp-grid, tangent, or first-order Jacobian datum is recharged as an `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
