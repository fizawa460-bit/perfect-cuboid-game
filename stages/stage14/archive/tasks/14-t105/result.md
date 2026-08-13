# Stage14-t105 — background Gaussian fiber density no-go and outer-Q support reduction

## Status

`COMPLETE_BACKGROUND_GAUSSIAN_FIBER_DENSITY_NOGO_AND_OUTER_Q_SUPPORT_REDUCTION`

Consumes only merged Stage14 sources on latest main: Stage14-t104, Stage14-t91/t89, Stage14-Work-bkX23, and the completed frozen Stage14-tH27 audit. No H snapshot is reopened or refined. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Reinsert the scalar cofactor coordinate

Fix the outer fixed-U data

```text
(U,epsilon,k,h,kappa,beta,eta),
k0=eta*k,
```

and the reciprocal/inversion orientation. Merged t89 gives the one-dimensional canonical-LPF scalar kernel

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
d=B^o(1).
```

For each admissible `Q`, let `Omega_Q` be the complete background Gaussian representation fiber after the fixed packet labels and representation-local masks are imposed, but before the one frozen t104 full elementary Boolean boundary is evaluated.

Merged t89 proves that the full fixed-Q Gaussian representation/completion fiber is `B^o(1)`. Merged t91 gives the exact orientation-cube realization and the exceptional/generic split. Therefore, uniformly on every live `Q`,

```text
1 <= M_Q := |Omega_Q| <= B^o(1).
```

The lower bound is only asserted on live fibers; empty scalar fibers are omitted from the conditional density.

```text
FIXED_Q_BACKGROUND_GAUSSIAN_FIBER_SIZE=Bo1
OUTER_SCALAR_COFACTOR_COORDINATE_RESTORED=true
```

## 2. Fiberwise Boolean principal density is quantized

After the local `B^o(1)` selector/action labels are frozen as in t104, write the resulting Boolean event on one fixed-Q background fiber as

```text
b_Q : Omega_Q -> {0,1}.
```

Define

```text
N_Q   := sum_{x in Omega_Q} b_Q(x),
rho_Q := N_Q/M_Q.
```

Hence `rho_Q` belongs to the finite grid

```text
{0,1/M_Q,2/M_Q,...,1}.
```

In particular, if the principal event is nonempty,

```text
N_Q>0
=>
rho_Q >= 1/M_Q = B^(-o(1)).
```

If the boundary is nonconstant,

```text
0<N_Q<M_Q,
```

then also

```text
1-rho_Q >= 1/M_Q = B^(-o(1)).
```

Thus exponent-zero principal density inside one fixed-Q background fiber is not a new analytic density phenomenon. It is automatic from subpolynomial fiber cardinality as soon as one accepted background label exists.

```text
FIBER_PRINCIPAL_DENSITY_QUANTIZED=true
NONEMPTY_FIBER_ACCEPTANCE_IMPLIES_EXPONENT_ZERO_DENSITY=true
NONCONSTANT_FIBER_BOUNDARY_IMPLIES_TWO_SIDED_EXPONENT_ZERO_DENSITY=true
LOCAL_FIBER_EXPONENT_ZERO_DENSITY_IS_AUTOMATIC=true
```

## 3. Exact centered identity and the complement correction

For every fixed Q,

```text
b_Q = rho_Q + b_Q^circ,
E_Q b_Q^circ = 0,
E_Q |b_Q^circ|^2 = rho_Q(1-rho_Q).
```

The centered variance is small when the complement is thin. But the positive principal contribution `rho_Q` is not removed by that fact.

For example, if `rho_Q=1`, then

```text
b_Q^circ == 0
```

while the principal term equals one. More generally, `1-rho_Q` fixed-power small controls only the centered fluctuation; it does not by itself give a fixed-power upper bound for the positive principal acceptance mass.

Therefore the t104 statement

```text
FIXED_FULL_BOUNDARY_EXPONENT_ZERO_INTERMEDIATE_DENSITY_IS_MINIMAL_SURVIVOR=true
```

is too strong when interpreted as a statement about the unresolved positive principal mass. The legal principal-density survivor requires only

```text
rho_Q>0,
```

which already implies `rho_Q=B^(-o(1))` on a live subpolynomial fiber. Two-sided intermediate density remains correct only for a genuinely nonconstant boundary when one is specifically studying its centered variance.

```text
COMPLEMENT_DEFICIT_ONLY_CONTROLS_CENTERED_TERM=true
COMPLEMENT_DEFICIT_ELIMINATES_POSITIVE_PRINCIPAL_MASS=false
T104_TWO_SIDED_MINIMAL_PRINCIPAL_SURVIVOR_LOCK_SUPERSEDED=true
FIXED_U_PRINCIPAL_SURVIVOR_REQUIRES_ONLY_NONEMPTY_FIBER_ACCEPTANCE=true
```

This correction aligns the fixed-U bookkeeping with merged Work-bkX23, which explicitly distinguishes principal density from centered Bernoulli fluctuation.

## 4. Fiber density cannot supply a fixed-power saving

Because

```text
M_Q=B^o(1),
```

there is no room for a fixed exponent density deficit between one accepted label and the whole fixed-Q fiber. A local statement of the form

```text
rho_Q <= B^(-delta+o(1)), delta>0,
```

would force `N_Q=0` for all sufficiently large B on that fiber.

Hence the only possible fixed-power gain from the positive principal term is not a fractional density estimate inside `Omega_Q`; it must come from showing that accepted/nonempty fibers themselves occupy a fixed-power sparse subset of the outer scalar canonical-LPF family.

```text
LOCAL_BACKGROUND_FIBER_DENSITY_FIXED_POWER_SAVING_AVAILABLE=false
FIXED_POWER_LOCAL_DENSITY_DEFICIT_COLLAPSES_TO_EMPTY_FIBER=true
OUTER_Q_SUPPORT_IS_FIRST_REMAINING_POLYNOMIAL_LENGTH=true
```

## 5. Boundary-bearing outer-Q weight

Define the positive integer weight

```text
omega_B(Q) := N_Q
            = # {x in Omega_Q : b_Q(x)=1}.
```

If several local selector/action cells are needed before applying t104 on a given Q, sum them charged-once into `omega_B(Q)`. Their number and each fixed-Q Gaussian fiber multiplicity are `B^o(1)`, so uniformly

```text
0 <= omega_B(Q) <= B^o(1).
```

The positive principal contribution is therefore reduced to the one-dimensional scalar kernel

```text
sum_Q omega_B(Q)
```

over the merged t89 canonical-LPF conditions.

Equivalently, if

```text
S_B := {Q : omega_B(Q)>0},
```

then

```text
sum_Q omega_B(Q) <= |S_B| B^o(1).
```

Thus a fixed-power saving on the positive principal branch would follow from a fixed-power support deficit for `S_B`; no such deficit is proved here.

```text
BOUNDARY_BEARING_Q_WEIGHT_SUP_NORM=Bo1
POSITIVE_PRINCIPAL_MASS_REDUCED_TO_OUTER_Q_SUPPORT_WEIGHT=true
FIXED_U_OUTER_Q_SUPPORT_FIXED_POWER_SAVING_PROVED=false
```

This is a refinement of t89's bounded physical weight: t89 bounded all representation-local physical completions over Q, while t105 identifies the t104 principal-boundary obstruction as another bounded representation-local weight and proves that its inner-fiber density is not an independent analytic length.

## 6. Tower decomposition over Q and background labels

Let the outer Q measure be weighted by the ambient fiber size `M_Q`. For any finite scalar block `I`, set

```text
M(I) = sum_{Q in I} M_Q,
rho_I = (1/M(I)) sum_{Q in I} N_Q.
```

Then exactly

```text
rho_I = E_Q^M rho_Q,
```

where `E_Q^M` denotes the `M_Q`-weighted outer average.

For the full Bernoulli selector on the disjoint union of fibers, total variance decomposes as

```text
rho_I(1-rho_I)
 = Var_Q^M(rho_Q)
 + E_Q^M[rho_Q(1-rho_Q)].
```

The second term is purely within-fiber variance. Since each fiber is subpolynomial, it cannot provide a fixed-power principal-density loss. Any remaining polynomial-scale structure lies in the first level: which Q fibers are occupied and how their bounded weights vary.

```text
FIXED_U_Q_FIBER_TOWER_DECOMPOSITION_EXACT=true
WITHIN_FIBER_VARIANCE_IS_NOT_INDEPENDENT_POLYNOMIAL_LENGTH=true
OUTER_Q_OCCUPANCY_IS_REMAINING_PRINCIPAL_SCALE=true
```

No cancellation is claimed for the positive weight `omega_B(Q)`.

## 7. Relation to Work-bkX23

Merged Work-bkX23 asks for

```text
BackgroundFiberPrincipalDensityAdapterOrNoGo.
```

Stage14-t105 supplies the fixed-U **no-go half**:

```text
fixed-Q Gaussian background fibers are only B^o(1),
so nonempty principal density is automatically B^(-o(1));
no fixed-power density theorem can live solely inside those fibers.
```

The global primitive-slope background from Work-bkX23 is genuinely polynomial (`B^(1/2+o(1))` on the relevant scale), so the two background measures are not arithmetically identified by this result.

```text
WORK_BKX23_FIXED_U_BACKGROUND_FIBER_NOGO_PROVED=true
GLOBAL_FIXED_U_BACKGROUND_SPACES_IDENTIFIED=false
COMMON_ARITHMETIC_ACCEPTANCE_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## 8. H decision

No new tH is opened.

The gain is internal and exact: the local background Gaussian fiber has been shown too short to host a fixed-power density theorem, and the obstruction has been pushed back to a positive bounded weight on the canonical-LPF Q family. No explicit multiplicative, bilinear, trace-function, congruence, or polynomial-equation description of the support of `omega_B(Q)` is yet proved.

Frozen tH26 already warned that a generic bounded canonical-LPF cofactor weight is not theorem-ready, while frozen tH27 audited the one-boundary principal-mass obstruction. Reopening either theorem class would add no new information.

```text
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
```

## 9. New minimal receiver

The fixed-U obstruction is now

```text
SharedUStrongGapCanonicalLPF
BoundaryBearingGaussianCofactorQSupportWeight.
```

with

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
0<=omega_B(Q)<=B^o(1).
```

The next internal task is to open `omega_B(Q)` across Q and determine whether boundary-bearing support can be expressed through one common arithmetic condition rather than a Q-dependent `B^o(1)` representation-label choice.

```text
NEXT_INTERNAL_TARGET=BoundaryBearingCanonicalLPFQSupportArithmeticDecomposition
```

## 10. Frozen boundary

```text
STAGE14_T105=COMPLETE_BACKGROUND_GAUSSIAN_FIBER_DENSITY_NOGO_AND_OUTER_Q_SUPPORT_REDUCTION
MERGED_T104_CONSUMED=true
MERGED_WORK_BKX23_CONSUMED=true
FIXED_Q_BACKGROUND_GAUSSIAN_FIBER_SIZE=Bo1
OUTER_SCALAR_COFACTOR_COORDINATE_RESTORED=true
FIBER_PRINCIPAL_DENSITY_QUANTIZED=true
NONEMPTY_FIBER_ACCEPTANCE_IMPLIES_EXPONENT_ZERO_DENSITY=true
NONCONSTANT_FIBER_BOUNDARY_IMPLIES_TWO_SIDED_EXPONENT_ZERO_DENSITY=true
LOCAL_FIBER_EXPONENT_ZERO_DENSITY_IS_AUTOMATIC=true
COMPLEMENT_DEFICIT_ONLY_CONTROLS_CENTERED_TERM=true
COMPLEMENT_DEFICIT_ELIMINATES_POSITIVE_PRINCIPAL_MASS=false
T104_TWO_SIDED_MINIMAL_PRINCIPAL_SURVIVOR_LOCK_SUPERSEDED=true
FIXED_U_PRINCIPAL_SURVIVOR_REQUIRES_ONLY_NONEMPTY_FIBER_ACCEPTANCE=true
LOCAL_BACKGROUND_FIBER_DENSITY_FIXED_POWER_SAVING_AVAILABLE=false
FIXED_POWER_LOCAL_DENSITY_DEFICIT_COLLAPSES_TO_EMPTY_FIBER=true
OUTER_Q_SUPPORT_IS_FIRST_REMAINING_POLYNOMIAL_LENGTH=true
BOUNDARY_BEARING_Q_WEIGHT_SUP_NORM=Bo1
POSITIVE_PRINCIPAL_MASS_REDUCED_TO_OUTER_Q_SUPPORT_WEIGHT=true
FIXED_U_OUTER_Q_SUPPORT_FIXED_POWER_SAVING_PROVED=false
FIXED_U_Q_FIBER_TOWER_DECOMPOSITION_EXACT=true
WITHIN_FIBER_VARIANCE_IS_NOT_INDEPENDENT_POLYNOMIAL_LENGTH=true
OUTER_Q_OCCUPANCY_IS_REMAINING_PRINCIPAL_SCALE=true
WORK_BKX23_FIXED_U_BACKGROUND_FIBER_NOGO_PROVED=true
GLOBAL_FIXED_U_BACKGROUND_SPACES_IDENTIFIED=false
COMMON_ARITHMETIC_ACCEPTANCE_ADAPTER_PROVED=false
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUStrongGapCanonicalLPFBoundaryBearingGaussianCofactorQSupportWeight
NEXT_INTERNAL_TARGET=BoundaryBearingCanonicalLPFQSupportArithmeticDecomposition
NEXT=Stage14-t106
```
