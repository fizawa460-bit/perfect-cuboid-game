# Stage14-Work-bfX18 receiver / supersession matrix

| Track | Previous integrated boundary | Current merged boundary | Current receiver | New contraction | Cross-promotable? |
|---|---|---|---|---|---|
| Mainline | 4dl | 4dm | principal + positive dense pair covariance + positive connected third cumulant | negative covariance removed; pair covariance split into zero-mode cofactor and masked centered inverse-fraction pieces | no |
| s route | s7-53 at beX17 publication, later s7-55 | s7-56 | dense representative pair joint occupancy + principal defect / centered error | every fixed-power sparse pair-joint layer removed | no |
| fixed U | t94 at beX17 publication | t96 / frozen tH26 | intermediate antipodal occupancy + one non-negligible generic split-prime influence | variance converted into orientation-edge influence localization | no |
| q radar | q10 carry-forward | q11 | multiplicative/Hecke transfer test + retained inverse-fraction shelf | Azevedo--Moreira architecture classified NEAR, not theorem source | no |
| integrated X | X17 | X18 | ExponentZeroConditionalSensitivityTemplate | exact global covariance-as-conditional-response identity; influence-to-response implication refuted | no |

## Global pairwise exact views

The following are alternative views of the same charged-once representative pair covariance and must not be multiplied:

```text
Gamma_ij
= Var(W_i) * Resp_{i->j}
= Z_pair + E_pair.
```

Here

```text
Resp_{i->j}=E[W_j|W_i=1]-E[W_j|W_i=0],
Z_pair=(1/C_*)Cov(A_+,B_-),
E_pair=Cov(A_+K_rho,B_-).
```

```text
GLOBAL_PAIRWISE_COVARIANCE_AS_CONDITIONAL_RESPONSE_PROVED=true
PAIRWISE_ZERO_CENTERED_SPLIT_RETAINED=true
ALTERNATIVE_PAIRWISE_VIEWS_MULTIPLICABLE=false
```

## X18 no-cross-promotion witness

On the fixed-U Boolean side the antipodally even function

```text
f(x)=1_{x_1 x_2=1}
```

has unit edge influence in `x_1,x_2` but zero first-order conditional mean contrast in either coordinate. Therefore t96's influential-bit conclusion can live entirely in even degree-two Walsh structure and does not imply the global pairwise conditional-response receiver.

```text
COMMON_CONDITIONAL_SENSITIVITY_LANGUAGE_PROVED=true
T96_INFLUENCE_IMPLIES_FIRST_ORDER_CONDITIONAL_BIAS=false
GLOBAL_FIXED_U_SENSITIVITY_SPACES_IDENTIFIED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## H gate

```text
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH27_NEEDED=false
```

Reason: main/s still have deterministic dense-pair normalization/factorization work, while t96 has not converted the influential-bit event into a fixed-power arithmetic theorem target.

## Whole-family ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

## Revisit

Normal next integrated revisit after `4do + s7-58 + t98`, or earlier on a material positive-delta, arithmetic influence localization, multiplicative-phase adapter, or global/fixed-U sensitivity map.
