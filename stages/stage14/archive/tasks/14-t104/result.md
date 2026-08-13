# Stage14-t104 — full prime-action freeze and prime-average discharge

## Status

`COMPLETE_FULL_PRIME_ACTION_FREEZE_AND_PRIME_AVERAGE_DISCHARGE`

Consumes only merged Stage14 sources on latest main: Stage14-t103, Stage14-t101/t100/t98, Stage14-Work-bjX22, and the completed frozen Stage14-tH27 audit. No H snapshot is reopened or refined. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering common-skeleton receiver

Fix one live square-root-saturating fixed-U packet. Merged t103 gives one packet-wide elementary selector skeleton `e_*` such that, for the generic split-prime orientation bits

```text
P_G,
r = |P_G| = omega(delta_G)=B^o(1),
```

and elementary boundary densities

```text
rho_p := J_{p,e_*} in [0,1],
```

one has

```text
rho_bar := (1/r) sum_{p in P_G} rho_p = B^(-o(1))
```

in the lower-bound/exponent-zero sense.

The skeleton is fixed across primes, but t103 leaves one prime-dependent action parameter.

## 2. Exact action label

For the fixed skeleton define an **exact action label** `a_p` that is sufficient to determine the Boolean boundary function on the packet state variable `x`.

### SIGN

The fixed forms `S,D` are inherited from t103/t100. One may take

```text
a_p = |B_p/A_p|
```

with the packet's exact tie convention included in the label. Equivalently one may use the canonical projective square ratio `[A_p^2:B_p^2]`. Once this label is fixed, the event

```text
A_p^2 S(x)^2 - B_p^2 D(x)^2 < 0
```

is the same Boolean function of `x` for every prime with that action label.

### DIV

For fixed `q,S,D`, take the exact residue pair

```text
a_p = (A_p mod q, B_p mod q).
```

Then

```text
1_{q | A_p S(x)+B_p D(x)} xor
1_{q | A_p S(x)-B_p D(x)}
```

is identical for primes with the same action label. No projective quotient is needed for the argument and no smallness of `q` is asserted.

### PROJ

For fixed `d,C_d`, take

```text
a_p = tau_p,
```

the exact finite projective orientation-switch action. Then

```text
1_{z in C_d} xor 1_{tau_p z in C_d}
```

is identical for equal action labels.

Thus in every branch

```text
SAME_SKELETON_PLUS_SAME_ACTION_IMPLIES_SAME_BOUNDARY_FUNCTION=true.
```

## 3. The action image is automatically subpolynomial

Let

```text
A_* = {a_p : p in P_G},
K = |A_*|.
```

No arithmetic theorem is needed to bound this image: there are only `r` generic prime bits, hence exactly

```text
K <= r = B^o(1).
```

This is an image-size statement inside one fixed packet. It does not assert that the ambient SIGN slope space or a residue/projective action space is itself small.

```text
PRIME_ACTION_IMAGE_SIZE=Bo1
AMBIENT_ACTION_SPACE_FORCED_SUBPOLYNOMIAL=false
```

## 4. Freeze one exact full action without fixed-power loss

For `a in A_*`, define its normalized incidence mass

```text
W(a) := (1/r) sum_{p:a_p=a} rho_p.
```

Then exactly

```text
sum_{a in A_*} W(a) = rho_bar.
```

Since `K=B^o(1)`, there exists `a_*` with

```text
W(a_*) >= rho_bar/K = B^(-o(1)).
```

Let

```text
P_* = {p in P_G : a_p=a_*},
n_* = |P_*|.
```

Because `e_*` and `a_*` together determine one exact Boolean boundary function, write it as

```text
b_*(x),
rho_* := E_x b_*(x).
```

For every `p in P_*`,

```text
rho_p = rho_*.
```

Therefore the selected action-cell mass factors **exactly** as

```text
W(a_*) = (n_*/r) rho_*.
```

Both factors lie in `[0,1]`. Hence

```text
n_*/r >= W(a_*) = B^(-o(1)),
rho_* >= W(a_*) = B^(-o(1)).
```

Thus one may simultaneously freeze

```text
one elementary selector skeleton e_*,
one exact prime action a_*,
one full-coefficient Boolean boundary b_*(x),
```

while retaining an exponent-zero fraction of generic prime bits and exponent-zero state density.

```text
FULL_PRIME_ACTION_FREEZE_PROVED=true
+COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ON_EXPONENT_ZERO_PRIME_SUBFAMILY_PROVED=true
FIXED_ACTION_PRIME_FRACTION_EXPONENT_ZERO=true
FIXED_FULL_BOUNDARY_STATE_DENSITY_EXPONENT_ZERO=true
```

The leading `+` in the displayed lock above is punctuation only; the canonical lock is repeated without punctuation in the frozen boundary below.

A singleton prime action class is allowed. Since `r=B^o(1)`, even `1/r=B^(-o(1))`; no positive constant prime density is claimed.

## 5. Prime averaging is a localization device, not a new analytic length

On `P_*`, the state boundary function is literally the same `b_*(x)`. The prime coordinate contributes only the multiplicity `n_*`:

```text
(1/r) sum_{p in P_*} E_x b_{p,e_*}(x)
 = (n_*/r) E_x b_*(x)
 = (n_*/r) rho_*.
```

There is therefore no residual oscillatory prime family in this selected action cell. In particular the t102/t103 prime-average energy cannot be multiplied by a separate fixed-boundary saving.

The legal interpretation is

```text
prime mover density / energy
-> common skeleton localization
-> exact action localization
-> one fixed boundary principal/centered problem.
```

```text
PRIME_ACTION_VARIATION_DISCHARGED_AS_LOCALIZATION=true
PRIME_AVERAGE_ANALYTIC_LENGTH_REMAINS_POLYNOMIAL=false
PRIME_ENERGY_AND_ACTION_FREEZE_DOUBLE_CHARGE_FORBIDDEN=true
```

## 6. Re-enter the t101 principal/centered boundary with stronger localization

For the frozen full boundary define

```text
b_*^circ(x) = b_*(x)-rho_*.
```

Exactly

```text
E_x b_*^circ = 0,
E_x |b_*^circ|^2 = rho_*(1-rho_*).
```

The low-density alternative `rho_*=B^(-delta+o(1))` for fixed `delta>0` is incompatible with the selected saturating action cell because t104 already gives `rho_*=B^(-o(1))` in the lower-bound sense.

If instead

```text
1-rho_* = B^(-delta+o(1))
```

for fixed `delta>0`, then the centered `L^2` energy has the same fixed-power deficit and the existing t101 Cauchy ledger gives a discrepancy gain.

Hence the genuinely unsaved fixed-action survivor can be restricted to

```text
rho_*   = B^(-o(1)),
1-rho_* = B^(-o(1)).
```

This is an exponent-scale statement. It does not mean `rho_*` tends to a fixed constant.

```text
FIXED_FULL_BOUNDARY_EXPONENT_ZERO_INTERMEDIATE_DENSITY_IS_MINIMAL_SURVIVOR=true
```

## 7. Relation to tH27

This contraction does **not** create a new external theorem question. Frozen tH27 already audited the one-elementary-boundary setting and certified that SIGN, DIV, and PROJ principal mass need not have uniform fixed-power codimension under the canonical-LPF physical masks.

Stage14-t104 shows that the later t102/t103 prime averaging does not escape that obstruction: because its action image inside the packet is only `B^o(1)`, it can be frozen without fixed-power loss and returns to one exact full boundary.

Therefore

```text
TH27_NEGATIVE_PRINCIPAL_MASS_OBSTRUCTION_REACHED_AGAIN=true
PRIME_AVERAGING_ESCAPE_FROM_TH27_OBSTRUCTION_PROVED=false
```

and a new H audit would repeat the same theorem class.

```text
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
```

## 8. Relation to merged Work-bjX22

Merged Work-bjX22 records the common finite-label freezing principle between the global and fixed-U routes. Stage14-t104 realizes that principle one step further on the fixed-U side: not only the selector skeleton but the complete prime action may be frozen inside the subpolynomial generic-prime support.

The arithmetic receivers nevertheless remain different. The global branch has a fixed subpolynomial Gaussian mover prime/root and square-root-many primitive divisor directions; the fixed-U branch now has one fixed full elementary boundary under the canonical-LPF background cofactor measure.

```text
COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_CONSUMED=true
GLOBAL_FIXED_U_ARITHMETIC_MASK_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## 9. New minimal receiver

The prime coordinate has been exhausted as an independent source of saving. The fixed-U obstruction is now

```text
SharedUCanonicalLPF
FixedFullElementaryBoundary
ExponentZeroIntermediatePrincipalDensity
UnderBackgroundGaussianCofactorMeasure.
```

The next internal step should decompose the fixed boundary density `rho_*` over the remaining background Gaussian cofactor fibers, retaining canonical largest-prime, primitive cover, endpoint, and physical reconstruction masks exactly. The objective is to determine whether the principal mass can be concentrated into `B^o(1)` background labels again or whether a genuinely polynomial cofactor family finally appears.

```text
NEXT_INTERNAL_TARGET=FixedFullBoundaryBackgroundGaussianCofactorDensityDecomposition
```

## 10. Frozen boundary

```text
STAGE14_T104=COMPLETE_FULL_PRIME_ACTION_FREEZE_AND_PRIME_AVERAGE_DISCHARGE
MERGED_T103_CONSUMED=true
MERGED_WORK_BJX22_CONSUMED=true
SAME_SKELETON_PLUS_SAME_ACTION_IMPLIES_SAME_BOUNDARY_FUNCTION=true
PRIME_ACTION_IMAGE_SIZE=Bo1
AMBIENT_ACTION_SPACE_FORCED_SUBPOLYNOMIAL=false
FULL_PRIME_ACTION_FREEZE_PROVED=true
COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ON_EXPONENT_ZERO_PRIME_SUBFAMILY_PROVED=true
FIXED_ACTION_PRIME_FRACTION_EXPONENT_ZERO=true
FIXED_FULL_BOUNDARY_STATE_DENSITY_EXPONENT_ZERO=true
PRIME_ACTION_VARIATION_DISCHARGED_AS_LOCALIZATION=true
PRIME_AVERAGE_ANALYTIC_LENGTH_REMAINS_POLYNOMIAL=false
PRIME_ENERGY_AND_ACTION_FREEZE_DOUBLE_CHARGE_FORBIDDEN=true
FIXED_FULL_BOUNDARY_EXPONENT_ZERO_INTERMEDIATE_DENSITY_IS_MINIMAL_SURVIVOR=true
TH27_NEGATIVE_PRINCIPAL_MASS_OBSTRUCTION_REACHED_AGAIN=true
PRIME_AVERAGING_ESCAPE_FROM_TH27_OBSTRUCTION_PROVED=false
COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_CONSUMED=true
GLOBAL_FIXED_U_ARITHMETIC_MASK_ADAPTER_PROVED=false
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFFixedFullElementaryBoundaryExponentZeroIntermediatePrincipalDensityUnderBackgroundGaussianCofactorMeasure
NEXT_INTERNAL_TARGET=FixedFullBoundaryBackgroundGaussianCofactorDensityDecomposition
NEXT=Stage14-t105
```
