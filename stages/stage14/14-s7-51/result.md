# Stage14-s7-51 — dense principal-cell reduction and signed-covariance saturation dichotomy

## Status

`COMPLETE_DENSE_PRINCIPAL_CELL_REDUCTION_AND_SIGNED_COVARIANCE_SATURATION_DICHOTOMY`

Stage14-s7-51 consumes merged `Stage14-s7-50`, merged `Stage14-sH50`, merged `Stage14-X15`, and the latest merged roadmap release through `#632`.

The entering whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The sH50 receiver is

```text
FullConductorPrimitiveQuarterPythagoreanThreeProjectionConditionalPrincipalDensityAndSignedCovarianceCorrelation.
```

The purpose of s7-51 is to remove all polynomially sparse conditioning cells from that receiver before any further analytic theorem search.

---

## 1. Full-conductor physical conditioning cells

At possible square-root saturation we may assume, by s7-50,

```text
q=C_* B^o(1),
gcd(h0,q)=1,
C_*=B^(chi+o(1)),
1/6<=chi<=1/4.
```

Retain the primitive quarter pair `(m,n)` and the three X15 physical weights

```text
W_+(m,n), W_-(m,n), W_k(m,n),
```

all bounded by `B^o(1)`.

Partition the quarter-pair family into admissible conditioning cells `Omega` which freeze only data already known to have subpolynomial multiplicity once the charged source coordinate is fixed:

```text
C_* dyadic scale and squarefree/2-primary decoration,
Gaussian root label rho,
endpoint-small orientation data,
fixed-power gcd-free allocation pattern,
full-conductor class q=C_* B^o(1).
```

No new polynomial support is introduced by the cell label beyond the already charged `C_*` choice.

For a nonempty cell define

```text
P_Omega = #Omega,
mu_i(Omega) = P_Omega^(-1) sum_Omega W_i,
W_i^0 = W_i-mu_i(Omega).
```

The exact X15 triple-centering identity holds cellwise.

---

## 2. Cellwise exact decomposition

For every `Omega`,

```text
I_Omega := sum_Omega W_+ W_- W_k
```

satisfies exactly

```text
I_Omega
 = P_Omega mu_+ mu_- mu_k
 + mu_+ sum W_-^0 W_k^0
 + mu_- sum W_+^0 W_k^0
 + mu_k sum W_+^0 W_-^0
 + sum W_+^0 W_-^0 W_k^0.                 (2.1)
```

Call the first term `M_Omega` and the remaining signed sum `C_Omega`:

```text
M_Omega=P_Omega mu_+mu_-mu_k,
C_Omega=I_Omega-M_Omega.
```

Thus

```text
I(B)=sum_Omega M_Omega + sum_Omega C_Omega.        (2.2)
```

up to the already frozen `B^o(1)` reconstruction factor.

---

## 3. Polynomially sparse principal cells are automatically harmless

Fix any `delta>0`.  Split cells into

```text
D_delta = {Omega : mu_+mu_-mu_k >= B^(-delta)},
S_delta = {Omega : mu_+mu_-mu_k <  B^(-delta)}.
```

The total primitive quarter-pair ambient mass is at most `B^(1/2+o(1))`, while each physical weight is `B^o(1)`. Hence

```text
sum_{Omega in S_delta} M_Omega
 <= B^(1/2-delta+o(1)).                            (3.1)
```

This is deterministic and uses no distribution theorem.

Therefore a square-root-saturating principal contribution can only come from cells satisfying, for every fixed `delta>0`,

```text
mu_+(Omega) mu_-(Omega) mu_k(Omega) >= B^(-delta).
```

Equivalently along a saturation sequence,

```text
mu_+ mu_- mu_k = B^(-o(1)).                        (3.2)
```

Because each `mu_i<=B^o(1)` and is nonnegative, no one of the three marginals may have a fixed-power deficit on the cells carrying square-root principal mass.

```text
DENSE_PRINCIPAL_CELL_REDUCTION_PROVED=true
ANY_FIXED_POWER_MARGINAL_DEFICIT_IS_SUBSQRT=true
SQRT_PRINCIPAL_SATURATION_FORCES_PRODUCT_MEAN=Bo1
```

---

## 4. Signed covariance saturation dichotomy

Let

```text
M(B)=sum_Omega M_Omega,
C(B)=sum_Omega C_Omega.
```

Then exactly

```text
I(B)=M(B)+C(B).                                    (4.1)
```

Suppose one seeks a strict saving `I(B)<<B^(1/2-delta)`.

There are only two possible mechanisms after s7-51:

1. **principal-density deficit**: `M(B)<<B^(1/2-delta)`;
2. **main-term-scale signed anti-correlation**: `M(B)` may be square-root size, but `C(B)` cancels it to power precision.

If neither occurs, no strict saving follows from the current exact decomposition.

Conversely, if a sequence saturates `I(B)=B^(1/2-o(1))` while the sparse cells are removed by (3.1), then some dense-cell subfamily carries `B^(1/2-o(1))` total physical mass. On that subfamily either the principal term itself is `B^(1/2-o(1))`, or the signed covariance sum is of main-term scale. Thus future work may discard all cells with any fixed-power marginal deficit and work only on dense cells.

```text
SQRT_SATURATION_DICHOTOMY_PROVED=true
SPARSE_CELLS_REMOVED_BEFORE_ANALYTIC_THEOREM=true
REMAINING_PRINCIPAL_MECHANISM=dense_joint_marginals
REMAINING_SIGNED_MECHANISM=main_term_scale_joint_covariance
```

---

## 5. Why this is a genuine receiver contraction

sH50 had to ask for a theorem uniform over the full physical family. s7-51 shows that such uniformity is stronger than necessary.

A future theorem only needs to address cells satisfying the saturation condition

```text
mu_+mu_-mu_k=B^(-o(1)),
q=C_* B^o(1),
```

with the eight X15 atomic blocks pairwise separated at fixed-power scale.

All cells with

```text
mu_+mu_-mu_k <= B^(-delta)
```

for some fixed `delta>0` already contribute strictly below square root and need no Kloosterman/dispersion theorem.

This is not a new whole-family exponent, because the dense-cell regime may still exist.

---

## 6. Relation to parallel mainline and fixed-U work

Parallel `Stage14-4di/4diH` reaches the same full-conductor principal/covariance obstruction. It is compatible with this reduction but is not required as a theorem source.

Merged `Stage14-t91` is fixed-`U` and concerns a primitive Gaussian orientation hypercube. No charged-once bridge from that fixed-packet Boolean coefficient to the whole-family dense principal cells is proved here.

```text
T91_CROSS_PROMOTED_TO_S7_51=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
```

---

## 7. H decision

The receiver has changed, but the change is an internal restriction to dense saturation cells. It does not yet expose a new theorem class beyond the one already audited by sH50.

Therefore:

```text
S7_51_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH50_REOPENED=false
NEXT_H_NEEDED=false
```

A new H should be requested only after a later s-stage derives a concrete coefficient factorization, character expansion, or signed kernel on the dense cells that materially changes theorem applicability.

---

## 8. Whole-family boundary and next receiver

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

New receiver:

```text
FullConductorDensePrimitiveQuarterPythagoreanThreeProjectionJointMarginalDensityOrMainTermScaleSignedCovariance.
```

Boundary:

```text
STAGE14_S7_51=COMPLETE_DENSE_PRINCIPAL_CELL_REDUCTION_AND_SIGNED_COVARIANCE_SATURATION_DICHOTOMY
DENSE_PRINCIPAL_CELL_REDUCTION_PROVED=true
ANY_FIXED_POWER_MARGINAL_DEFICIT_IS_SUBSQRT=true
SQRT_PRINCIPAL_SATURATION_FORCES_PRODUCT_MEAN=Bo1
SQRT_SATURATION_DICHOTOMY_PROVED=true
SPARSE_CELLS_REMOVED_BEFORE_ANALYTIC_THEOREM=true
S7_51_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-52
```
