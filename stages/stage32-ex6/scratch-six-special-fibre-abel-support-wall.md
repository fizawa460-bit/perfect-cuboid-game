# Stage32EX6 — six-special-fibre Abel/support wall

Status: `SCRATCH_EXACT_BOUNDED_MARKED_ABEL_SUPPORT_WALL_NO_ENDPOINT_CREDIT`.

This is the sixth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `N` be its normalization and fix one retained factor map

`f : N -> P1`

of degree `n in {81,105}`.

The retained modular-factor source lock gives exactly six special factor-cusp fibres in each direction. The retained AR decomposition defines `rho` as ramification away from those six special fibres.

The previous scratch leaf showed

`O_N(R_off) ~= O_N(2F - R_special)`

and that positive degree alone never obstructs effectivity on genus one. The bounded question here is whether the six actual marked fibres give a stronger Abel/support condition.

## Exact six-fibre divisor identity

Let the six special values be `c_1,...,c_6`. Write the fibre divisors

`F_j = f^*(c_j) = sum_P e_{j,P} P`,

so each `F_j` has degree `n` and `F_j ~ F` for the common fibre class `F`.

Let

`S_j := (F_j)_red = sum_{P in supp(F_j)} P`

be the reduced support divisor of the `j`-th special fibre.

The ramification contribution over that fibre is exactly

`F_j - S_j = sum_P (e_{j,P}-1)P`.

Therefore

`R_special = sum_{j=1}^6 (F_j-S_j)`.

Since `N` has genus one, Riemann--Hurwitz gives `R_total ~ 2F`. Hence

`R_off`
`~ 2F - R_special`
`~ 2F - sum_j F_j + sum_j S_j`
`~ sum_j S_j - 4F`.

Thus the six marked special supports determine the exact residual Abel/Picard class

`[R_off] = [sum_j S_j - 4F]`.

Taking degrees gives the exact support-count identity

`rho = sum_j deg(S_j) - 4n`.

This is the six-fibre form of the retained scalar ramification ledger. It is structural but not an independent numerical bound.

## Group-law / Abel interpretation

Choose an origin on the elliptic curve `N`. Linear equivalence of divisors of the same degree is equivalent to equality of their Abel sums in `Pic^0(N) ~= N`.

Therefore the actual off-special ramification divisor must satisfy the marked-point Abel equality corresponding to

`R_off + 4F ~ sum_j S_j`.

However, the retained source locks do not supply source-identified group-law coordinates for the points in the reduced special supports `S_j`, nor a torsion identity for their sum. The exact retained data provide fibre classes, multiplicities, boundary labels, node incidence and local landing semantics, but not a member-level Abel-sum value on the hypothetical normalization.

A bounded Stage-local/Arsenal lookup also did not surface an applicable pre-existing fixed-V6 marked-Abel/torsion adapter. This is only a bounded discovery result, not a repository-wide mathematical nonexistence claim.

## Support-disjointness does not obstruct rho >= 2

The off-special divisor must not meet the finite union

`U := union_j supp(S_j)`.

Set

`L_off := O_N(sum_j S_j - 4F)`,

so `deg L_off = rho`.

If `rho >= 2`, then on a smooth genus-one curve `L_off` is globally generated. Indeed for every point `P`,

`h0(L_off)=rho`,

`h0(L_off(-P))=rho-1`,

so evaluation at `P` is not identically zero.

Over the retained complex geometry, for each `P in U` the sections vanishing at `P` form a proper hyperplane in `H0(N,L_off)`. A finite union of proper hyperplanes cannot cover the vector space. Hence there exists a section nonzero at every point of `U`.

Its zero divisor is an effective representative of `L_off` disjoint from all six special-fibre supports.

Therefore for

`rho >= 2`

the exact Abel class plus the requirement “off-special support” does not create a generic existence obstruction.

## The only potentially rigid low-rho corners

The marked Abel class can become rigid only at very small residual degree:

- `rho=0`: one needs `L_off ~= O_N`, equivalently the degree-zero Abel class must vanish;
- `rho=1`: `h0(L_off)=1`, so there is a unique effective point representing the class; the actual marked Abel sum could test whether that point lies outside `U`;
- `rho>=2`: the linear system has enough freedom to choose an effective divisor avoiding the finite special set.

Thus class/support information alone can at most test the `rho=0` or `rho=1` corners unless additional symmetry or member-level point data are supplied.

## Consequence at O266

The retained O266 scalar system permits the explicit nonnegative corner

- `q81_node=0, eta81=0, rho81=52`;
- `q105_node=0, eta105=0, rho105=28`.

Both residual degrees are far above the rigid range. Consequently neither the six-fibre Abel relation nor off-special support-disjointness contradicts this scalar corner.

This does not construct global factor maps realizing the corner. It only proves that the generic genus-one Abel/support mechanism itself cannot eliminate it.

## Decision

Canonical scratch decisions:

- `SIX_SPECIAL_FIBRE_RESIDUAL_CLASS = SUM_REDUCED_SPECIAL_SUPPORT_MINUS_4F`;
- `RHO_EQUALS_TOTAL_REDUCED_SPECIAL_SUPPORT_MINUS_4N = true`;
- `MARKED_ABEL_RELATION_IS_EXACT = true`;
- `SOURCE_LOCKED_SPECIAL_SUPPORT_TORSION_IDENTITY_AVAILABLE = false`;
- `RHO_GE_2_OFFSPECIAL_SUPPORT_EFFECTIVITY_OBSTRUCTION = false`;
- `RHO_ZERO_OR_ONE_REMAINS_MEMBER_LEVEL_ABEL_TESTABLE = true`;
- `CURRENT_O266_FEASIBLE_CORNER_LIES_IN_RHO_GE_2 = true`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier or global factor map is constructed.
- The group-law statement is conditional on the hypothetical genus-one normalization and uses only divisor-class consequences of an actual map.
- A bounded repository/Arsenal search miss is not a repository-wide absence theorem.
- The existence of some off-special effective representative for `rho>=2` does not prescribe the actual ramification support of a global map.
- No torsion identity for the reduced special support is invented.
- No total RH, delta, conductor, cusp-grid, tangent, Jacobian or previous Picard datum is double-charged as a new `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
