# Stage14-Work-bfX18 — integrated toolbox-bf and X18 conditional-sensitivity audit

## Status

`COMPLETE_POST_BEX17_DENSE_PAIR_CONDITIONAL_RESPONSE_AND_FIXED_U_INFLUENCE_INTERFACE`

This integrated Work stage consumes only merged sources on latest main through

```text
Stage14-Work-beX17,
Stage14-4dm,
Stage14-s7-56,
Stage14-t96,
Stage14-q11,
Stage14-tH26,
Stage14-X15.
```

Source main SHA:

```text
b17c238576376e14e3b19fa2da81e862d7bf7488
```

No open/draft/unmerged descendant is imported as a theorem source.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here.

---

## 1. Work gate and numbering

The previous integrated stage `Stage14-Work-beX17` requested a normal revisit after merged `4dm + s7-55 + t95`, or an earlier material trigger.

Current merged main has advanced beyond that boundary:

```text
mainline: Stage14-4dm,
s route : Stage14-s7-56,
fixed U : Stage14-t96,
literature radar: Stage14-q11.
```

Therefore

```text
STAGE14_WORK_TOOLBOX_X_GATE=RUN
PREVIOUS_INTEGRATED_STAGE=Stage14-Work-beX17
CURRENT_INTEGRATED_STAGE=Stage14-Work-bfX18
```

The integrated ledgers advance

```text
toolbox-be -> toolbox-bf,
X17 -> X18.
```

---

## 2. Toolbox-bf — current global receiver

Merged `s7-56` removes every fixed-power sparse representative pair-joint-occupancy layer. On a possible pairwise square-root sequence,

```text
mu_+   = B^(-o(1)),
mu_-   = B^(-o(1)),
mu_+-  = B^(-o(1)),
1-mu_+ = B^(-o(1)),
1-mu_- = B^(-o(1)).
```

Merged `4dm` makes the upper-bound sign reduction and exact recentering

```text
Gamma_+- = Z_pair + E_pair,
```

where

```text
Z_pair = (1/C_*) Cov(A_+,B_-),
E_pair = Cov(A_+ K_rho,B_-).
```

Only the positive parts are upper-bound obstructions. Negative pairwise covariance is helpful and need not be counted as an exceptional positive family.

The representative pairwise square-root mechanism is therefore confined to dense joint occupancy and one of

```text
positive zero-mode cofactor covariance,
positive masked full-conductor inverse-fraction covariance.
```

The three pairwise coordinate realizations remain fixed-power finite-fiber equivalent and count once.

Together with the already-separated principal and connected branches, the current global obstruction is

```text
A. positive near-maximal principal occupancy;
B. positive dense pairwise covariance, internally
   B1. zero-mode cofactor covariance, or
   B2. masked full-conductor inverse-fraction covariance;
C. positive connected third cumulant.
```

Thus the toolbox-bf global receiver is

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagorean
PrincipalOrPositiveDensePairConditionalCorrelationOrPositiveConnectedThirdCumulant
```

with the pairwise branch retaining the exact 4dm zero/centered split.

No new exponent improvement follows from this contraction.

---

## 3. Toolbox-bf — current fixed-U receiver

Merged `t95` identifies the antipodal quotient occupancy variance exactly:

```text
Var(f)=mu(1-mu).
```

Merged `t96` then applies the discrete Poincare/Efron-Stein inequality on a Boolean chart of the quotient:

```text
sum_p Inf_p(f) >= 4 mu(1-mu).
```

On a square-root-saturating fixed-U sequence,

```text
mu=B^(-o(1)),
1-mu=B^(-o(1)),
```

so at least one generic split-prime orientation bit has

```text
Inf_p(f) >= B^(-o(1)).
```

No fixed-power influence lower bound follows because the moving Boolean rank is only controlled by `B^o(1)`. Hence no packet power saving follows.

The current fixed-U receiver is

```text
SharedUCanonicalLPFExponentZeroIntermediateAntipodalPairOccupancy
SingleGenericSplitPrimeInfluenceBoundary
```

with all t90--t96 physical masks retained.

---

## 4. X18 exact global conditional-response identity

Let `W_i,W_j in {0,1}` on one surviving global conditioning cell and put

```text
mu_i = E W_i,
nu_1  = E[W_j | W_i=1],
nu_0  = E[W_j | W_i=0].
```

On the interior cells retained by merged s7-52/4dk, `0<mu_i<1` at fixed-power scale. Then

```text
E(W_i W_j)=mu_i nu_1,
mu_j=mu_i nu_1+(1-mu_i)nu_0.
```

Therefore exactly

```text
Gamma_ij
 = E(W_iW_j)-mu_i mu_j
 = mu_i(1-mu_i)(nu_1-nu_0).                 (4.1)
```

Define the directional conditional response

```text
Resp_{i->j}:=nu_1-nu_0.
```

Then

```text
Gamma_ij = Var(W_i) Resp_{i->j}.             (4.2)
```

This is an exact finite-cell identity before any Fourier/root-line expansion.

Since every surviving marginal variance is `B^(-o(1))`, a positive pairwise square-root obstruction requires

```text
Resp_{i->j}^+ = B^(-o(1))
```

for at least one ordered representative pair. Conversely a fixed-power conditional-response deficit gives the same fixed-power loss after multiplication by the charged-once ambient mass.

```text
GLOBAL_PAIRWISE_COVARIANCE_AS_CONDITIONAL_RESPONSE_PROVED=true
GLOBAL_PAIRWISE_SQRT_OBSTRUCTION_REQUIRES_RESPONSE=Bo0=true
```

Equation (4.1) does not replace the 4dm zero/centered decomposition. It gives a second exact view of the same charged-once pairwise covariance and therefore may not be multiplied with `Z_pair/E_pair` as an independent saving.

---

## 5. X18 comparison with t96 influence

There is now a genuine common functional-analytic vocabulary:

```text
global:  change one physical selector state and measure conditional response of another selector;
fixed U: flip one generic split-prime orientation bit and measure change of physical acceptance.
```

Thus

```text
COMMON_CONDITIONAL_SENSITIVITY_LANGUAGE_PROVED=true
```

but this is still not an arithmetic adapter.

The two notions are mathematically different:

```text
Resp_{i->j}
  = difference of conditional means,

Inf_p(f)
  = probability that an edge flip changes the Boolean value.
```

A large edge influence does not force a nonzero first-order conditional mean contrast.

An exact stress witness is the antipodally even Boolean function

```text
f(x)=1_{x_1 x_2=1}
```

on `{+-1}^r` for `r>=2`. It descends to the antipodal quotient, satisfies

```text
Inf_1(f)=Inf_2(f)=1,
```

but

```text
E[f | x_1=1]=E[f | x_1=-1]=1/2,
```

so the first-order conditional contrast in coordinate `x_1` is zero.

Therefore the t96 influential-bit conclusion can be supported purely by an even degree-two Walsh mode and does not imply the global pairwise conditional-response receiver.

```text
T96_INFLUENCE_IMPLIES_FIRST_ORDER_CONDITIONAL_BIAS=false
T96_INFLUENCE_IMPLIES_GLOBAL_PAIRWISE_RESPONSE=false
GLOBAL_PAIRWISE_RESPONSE_IMPLIES_T96_ARITHMETIC_INFLUENCE=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

---

## 6. q11 compatibility

Merged `q11` identifies the Azevedo--Moreira Pythagorean multiplicative-function structure as `NEAR_STRUCTURE_HIGH_PRIORITY`, not a direct theorem source. It also keeps the q10 inverse-fraction shelf active for the masked centered pairwise branch.

The X18 conditional-response identity sharpens the q11 internal transfer test:

```text
GLOBAL_INTERNAL_TEST:
  factor either
  (a) Resp_{i->j},
  (b) Z_pair,
  (c) E_pair,
  or the connected kappa_3 coefficient
  into B^o(1)-complexity multiplicative/Hecke phases
  before absolute values.
```

No such factorization is proved here. In particular a formal sensitivity decomposition does not make the physical selectors multiplicative.

```text
Q11_DIRECT_THEOREM_IMPORTED=false
Q11_MULTIPLICATIVE_PHASE_ADAPTER_PROVED=false
Q10_INVERSE_FRACTION_BRANCH_RETAINED=true
```

---

## 7. Supersession and charged-once audit

The following remain charged exactly once:

```text
X15 primitive Pythagorean cone and its finite-fiber coordinate systems;
4dj/4dk principal/interior localization;
s7-54 pairwise coordinate equivalence;
s7-56 sparse joint-occupancy peel;
4dm zero-mode / centered pairwise recentering;
t93/t94 antipodal quotient reduction;
t95 variance identity;
t96 influence localization.
```

X18 does not multiply

```text
conditional response x zero/centered covariance split,
three pairwise coordinate realizations,
global sensitivity x fixed-U influence.
```

They are alternative descriptions or different quantifier spaces, not independent savings.

---

## 8. H decisions

### Mainline

No new H is requested. The newly isolated zero-mode cofactor covariance and conditional-response formulation are still internal density/factorization objects. Merged q11 found no direct theorem, and 4dm explicitly directs the next work internally.

```text
MAINLINE_H_NEEDED=false
MAINLINE_H_TARGET=NONE_INTERNAL_DENSE_PAIR_RESPONSE_FACTORIZATION_PENDING
```

### s route

No new s-route H is requested. `s7-56` sends the dense pair receiver to deterministic normalization in `s7-57`; the masked centered inverse-fraction family already has the completed negative applicability audits sH50/4diH.

```text
S_ROUTE_H_NEEDED=false
S_ROUTE_H_TARGET=NONE_S7_57_DENSE_PAIR_NORMALIZATION_PENDING
```

### fixed U

No new fixed-U H is requested. t96 has only an exponent-zero influential-bit conclusion, not a fixed-power influence theorem or theorem-compatible arithmetic edge event.

```text
FIXED_U_H_NEEDED=false
FIXED_U_H_TARGET=NONE_T96_INFLUENTIAL_BIT_NOT_YET_ARITHMETICALLY_LOCALIZED
TH27_NEEDED=false
```

---

## 9. Current receivers

Global:

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagorean
PrincipalOrPositiveDensePairConditionalCorrelationOrPositiveConnectedThirdCumulant
```

Pairwise internal split:

```text
PositiveZeroModeCofactorCovariance
or
PositiveMaskedFullConductorInverseFractionCovariance
```

Fixed U:

```text
SharedUCanonicalLPFExponentZeroIntermediateAntipodalPairOccupancy
SingleGenericSplitPrimeInfluenceBoundary
```

Common formal interface:

```text
ExponentZeroConditionalSensitivityTemplate
```

The global and fixed-U receivers are not equivalent.

---

## 10. Whole-family ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

Progress is a receiver contraction and an exact sensitivity/no-cross-promotion theorem, not an exponent improvement.

---

## 11. Next revisit condition

Do not rerun the permanent Work task after only one immediate successor. Normal revisit after material accumulation, provisionally:

```text
mainline merged through at least Stage14-4do,
s route merged through at least Stage14-s7-58,
fixed-U merged through at least Stage14-t98,
```

or earlier if one of the following occurs:

```text
1. a strict whole-family exponent improvement;
2. a new H/tH audit with nonzero certified delta;
3. a proof that dense pair conditional response has a fixed-power deficit;
4. a multiplicative/Hecke phase factorization of the physical pair or connected coefficient;
5. a fixed-power arithmetic localization of the t96 influential orientation bit;
6. an explicit global/fixed-U arithmetic sensitivity map preserving quantifier order.
```

---

## Locked boundary

```text
STAGE14_WORK_BFX18=COMPLETE_POST_BEX17_DENSE_PAIR_CONDITIONAL_RESPONSE_AND_FIXED_U_INFLUENCE_INTERFACE
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
TOOLBOX_BF_COMPONENT_COMPLETE=true
X18_COMPONENT_COMPLETE=true
AUDITED_THROUGH_MAINLINE=Stage14-4dm
AUDITED_THROUGH_S_ROUTE=Stage14-s7-56
AUDITED_THROUGH_FIXED_U=Stage14-t96_and_tH26
AUDITED_THROUGH_Q=Stage14-q11
PREVIOUS_INTEGRATED_STAGE=Stage14-Work-beX17
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_GLOBAL_RECEIVER=FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagoreanPrincipalOrPositiveDensePairConditionalCorrelationOrPositiveConnectedThirdCumulant
CURRENT_FIXED_U_RECEIVER=SharedUCanonicalLPFExponentZeroIntermediateAntipodalPairOccupancySingleGenericSplitPrimeInfluenceBoundary
GLOBAL_PAIRWISE_COVARIANCE_AS_CONDITIONAL_RESPONSE_PROVED=true
COMMON_CONDITIONAL_SENSITIVITY_LANGUAGE_PROVED=true
T96_INFLUENCE_IMPLIES_FIRST_ORDER_CONDITIONAL_BIAS=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH27_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=4do_and_s7-58_and_t98_or_material_early_trigger
```
