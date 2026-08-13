# Stage14-4dd — full-residual saturation and balanced Gaussian zero-frequency reduction

## Status

`COMPLETE_FIRST_RESIDUAL_DEFICIT_SAVING_AND_BALANCED_GAUSSIAN_SATURATION_REDUCTION`

Stage14-4dd consumes merged `Stage14-4dH`, merged `Stage14-4dc`, merged `Stage14-X13`, and the exact signed-quotient / primitive-root-line identities of merged `s7-27`, `s7-29`, and `s7-42`.

The entering whole-family theorem is

```text
V(B) << B^(1/2+o(1)).
```

Stage14-4dH completed the requested external applicability audit with

```text
CERTIFIED_MAINLINE_H_DELTA=0,
MAINLINE_BLOCKED_BY_H=false,
ADDITIONAL_MAINLINE_H_NEEDED=false.
```

The remaining obstruction is therefore an exact zero-frequency density problem, not a pending H theorem.

Stage14-4dd proves no strict sub-square-root whole-family theorem. Its new contribution is to stratify the first signed residual inside the 4dc Gaussian product coordinates and show that every fixed-power residual deficit is already strict sub-square-root. Consequently any square-root-saturating sequence has a full first residual and a fully balanced real Gaussian product pair.

---

## 1. Imported square-root band

Every possible square-root equality sequence already satisfies

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).
```

Put

```text
A_phi:=1/2-2phi=1/4-chi.
```

Across the band

```text
0<=A_phi<=1/12.
```

Merged s7-42 gives the first residual cap

```text
u_res<=B^(A_phi+o(1)).                              (1.1)
```

Merged 4dc uses

```text
a=g*a0,
b=g*b0,
g=B^o(1),
P=a0*U,
Q=b0*V,
```

with

```text
U*V=B^(2phi+o(1)),                                 (1.2)
oddpart(a*b)=oddpart(u_res).                       (1.3)
```

The finite 2-primary and `g=B^o(1)` decorations have zero fixed-power cost.

The good common core is

```text
C0=C/B^o(1)=B^(chi+o(1))
```

and

```text
C0 | P^2+Q^2,
gcd(C0,PQ)=1.                                     (1.4)
```

After the endpoint-small primitive peel,

```text
gcd(P,Q)=1
```

at fixed-power scale.

---

## 2. Dyadic first-residual stratification

Dyadically localize

```text
u_res=B^(mu+o(1)),
0<=mu<=A_phi.                                      (2.1)
```

By (1.2)-(1.3),

```text
boxed:
P*Q=B^(2phi+mu+o(1)).                              (2.2)
```

This is an equality of fixed-power scales on a fixed dyadic residual stratum; endpoint-small odd and 2-primary factors are absorbed into `B^o(1)`.

For fixed `C0` and a fixed CRT root

```text
rho^2=-1 mod C0,
P==rho*Q mod C0,
```

the merged primitive determinant-spacing lemma gives in dyadic boxes

```text
#(P,Q)
 << B^o(1)*(1+P0*Q0/C0).                           (2.3)
```

Here

```text
P0*Q0=B^(2phi+mu+o(1)).
```

Since

```text
2phi-chi=1/4,
```

we have uniformly

```text
2phi+mu-chi=1/4+mu>0.                              (2.4)
```

Therefore the `1` term in (2.3) is lower order and

```text
boxed:
fixed C => #(P,Q)
 <=B^(1/4+mu+o(1)).                                (2.5)
```

The number of admissible `C~B^chi` is at most `B^(chi+o(1))`; the local root assignments cost only `B^o(1)`.

Merged 4dc/X13 gives only divisor-many physical reconstruction after `(C,P,Q)` and a divisor split are fixed. Thus the complete fixed-`mu` physical count satisfies

```text
E_4dd(mu)
 <=chi+(1/4+mu)
 =2phi+mu.                                         (2.6)
```

Using `A_phi=1/2-2phi`,

```text
boxed:
E_4dd(mu)
 <=1/2-(A_phi-mu).                                 (2.7)
```

This is the main new 4dd estimate.

---

## 3. Every fixed-power residual deficit is strict sub-square-root

Define the first-residual deficit

```text
delta_res:=A_phi-mu>=0.                            (3.1)
```

Then (2.7) is exactly

```text
boxed:
E_4dd<=1/2-delta_res.                              (3.2)
```

Hence for every fixed `epsilon>0`, the region

```text
mu<=A_phi-epsilon
```

satisfies

```text
boxed:
E_4dd<=1/2-epsilon.                                (3.3)
```

Therefore any sequence capable of saturating the global square-root theorem must satisfy

```text
boxed:
mu=A_phi+o(1),                                     (3.4)

boxed:
u_res=B^(1/2-2phi+o(1)).                    (3.5)
```

In particular the first residual is not merely bounded by the s7-42 cap: it must saturate that cap at fixed-power scale.

```text
FIRST_RESIDUAL_FIXED_POWER_DEFICIT_SAVING_PROVED=true.
```

---

## 4. Saturation forces the Gaussian product to full half scale

Substitute (3.4) into (2.2):

```text
2phi+mu
 =2phi+(1/2-2phi)
 =1/2.
```

Thus every possible square-root equality sequence satisfies

```text
boxed:
P*Q=B^(1/2+o(1)).                                  (4.1)
```

This removes all fixed-power short-product strata from the 4dH zero-frequency receiver.

At this point the norm relation also lives at its full natural scale. In the exact s7-29/4dc notation,

```text
D=delta*s,
A_k=alpha*r,
D>A_k>0,
```

and

```text
D+A_k=aU=gP,
D-A_k=bV=gQ.                                       (4.2)
```

Therefore

```text
boxed:
P+Q=2D/g,
P-Q=2A_k/g.                                        (4.3)
```

On `theta=1/4`,

```text
alpha,delta=B^(1/4+o(1)),
r,s,g=B^o(1),                                      (4.4)
```

so

```text
boxed:
P+Q=B^(1/4+o(1)),
P-Q=B^(1/4+o(1)).                                  (4.5)
```

Moreover (4.2)-(4.4) imply individually

```text
P,Q<=B^(1/4+o(1)).                                 (4.6)
```

Combining (4.1) and (4.6), both coordinates must attain the quarter scale:

```text
boxed:
P=B^(1/4+o(1)),
Q=B^(1/4+o(1)).                                    (4.7)
```

Thus all four real linear forms satisfy

```text
boxed:
P,Q,P+Q,P-Q=B^(1/4+o(1)).                          (4.8)
```

Possible square-root saturation is therefore confined to a genuinely balanced Gaussian box. Fixed-power coordinate-axis degeneration and fixed-power real-diagonal degeneration are absent.

```text
SQRT_SATURATION_GAUSSIAN_PAIR_BALANCED=true.
```

---

## 5. Full norm quotient scale

From (4.7),

```text
P^2+Q^2=B^(1/2+o(1)).                              (5.1)
```

Since `C0=B^(chi+o(1))` and `C0|P^2+Q^2`, define

```text
R_G:=(P^2+Q^2)/C0.                                 (5.2)
```

Then on every possible square-root equality sequence

```text
boxed:
R_G=B^(1/2-chi+o(1)).                              (5.3)
```

Using `chi=2phi-1/4`,

```text
1/2-chi=3/4-2phi.                                  (5.4)
```

This is exactly the exponent of the xi-switch product `S*T` in the merged common-core parameterization. Thus the Gaussian norm quotient is also forced to its full physical scale; no fixed-power short norm quotient can occur at square-root equality.

The alternative norm-divisor quantifier order

```text
C0,
R_G,
P^2+Q^2=C0*R_G
```

does not by itself improve the exponent. The fixed-power support is

```text
chi+(1/2-chi)=1/2,                                 (5.5)
```

and for fixed norm the number of primitive sum-of-two-squares representations is divisor-bounded. Hence changing from the root-line view to the norm-divisor view merely reparameterizes the same zero-frequency mass.

```text
NORM_DIVISOR_REPARAMETERIZATION_GIVES_EXTRA_FIXED_POWER_SAVING=false.
```

The two views must not be multiplied as independent savings.

---

## 6. What 4dd removes from the zero-frequency receiver

Stage14-4dH left the set

```text
A_C={
 primitive (P,Q):
 C0|P^2+Q^2,
 P*Q<=B^(1/2+o(1)),
 some divisor split admits the physical completion
}.
```

Stage14-4dd shows that only the top product stratum can participate in square-root equality. Any equality sequence must now satisfy simultaneously

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/2-2phi,
u_res=B^(A_phi+o(1)),
P*Q=B^(1/2+o(1)),
P,Q,P+Q,P-Q=B^(1/4+o(1)),
(P^2+Q^2)/C0=B^(1/2-chi+o(1)),
H=K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).
```

The old zero-frequency receiver included fixed-power-short residual/product strata. Those strata are now closed with an explicit saving equal to their residual deficit.

---

## 7. Why this does not yet prove a strict whole-family saving

The stratum

```text
mu=A_phi
```

is not empty by any merged theorem. On that stratum the charged-once determinant ledger is still

```text
C choice                 : chi
balanced product rootline: 1/2-chi
post-(C,P,Q) completion  : 0
--------------------------------
total                    : 1/2.                    (7.1)
```

Squarefree-cell, interval, sign/orientation and divisor-split conditions are retained as filters, but no theorem in the merged chain proves that their support inside this balanced top-product root line has fixed-power density loss.

Therefore

```text
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.          (7.2)
```

The new obstruction is no longer generic Gaussian norm density. It is the physical reciprocal selector restricted to the full-residual balanced Gaussian packet.

---

## 8. New minimal receiver

Define

```text
SquareRootThetaQuarterFullResidualBalancedGaussianPhysicalReciprocalSelectorDensity
```

as the physical packets satisfying

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
u_res=B^(1/2-2phi+o(1)),
C0=B^(chi+o(1)),
P,Q,P+Q,P-Q=B^(1/4+o(1)),
C0|P^2+Q^2,
(P^2+Q^2)/C0=B^(1/2-chi+o(1)),
P=a0U,
Q=b0V,
all global odd-primitivity and squarefree-cell masks,
all exact reciprocal equations,
all Cayley row/column orientation masks,
X13 post-column reconstruction.
```

A strict sub-square-root theorem must prove power sparsity of the remaining exact reciprocal-completion selector on this balanced top-product family.

The next deterministic target is to substitute

```text
P=(D+A_k)/g,
Q=(D-A_k)/g
```

into the two reciprocal difference-of-squares equations and classify the resulting balanced physical eliminant before considering another analytic theorem.

---

## 9. H / tH decision

The mainline H request emitted by 4dc has already been completed by merged 4dH. Its negative applicability verdict is not a blocker.

Stage14-4dd has produced a strict downstream exact reduction and there remains unexhausted deterministic reciprocal algebra. Therefore no new auxiliary H is requested here.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false.
```

The contemporaneous fixed-U `t/tH` coefficient space is not cross-promoted.

---

## 10. Whole-family ledger

No new global exponent is claimed:

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The new local fixed-deficit theorem is

```text
boxed:
FIRST_RESIDUAL_DEFICIT_delta
=> E<=1/2-delta.
```

---

## Stage boundary

```text
STAGE14_4DD=COMPLETE_FIRST_RESIDUAL_DEFICIT_SAVING_AND_BALANCED_GAUSSIAN_SATURATION_REDUCTION
MERGED_4DH_IMPORTED=true
MERGED_4DC_IMPORTED=true
MERGED_X13_IMPORTED=true
MERGED_S7_42_FIRST_RESIDUAL_CAP_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
SQRT_SATURATION_COMMON_CORE_EXPONENT=chi=2phi-1/4
FIRST_RESIDUAL_CAP_EXPONENT=A_phi=1/2-2phi=1/4-chi
FIRST_RESIDUAL_DYADIC_EXPONENT=mu
FIRST_RESIDUAL_DEFICIT=A_phi-mu
FIXED_MU_COMPLETE_COUNT_EXPONENT=2phi+mu
FIXED_FIRST_RESIDUAL_DEFICIT_SAVING=A_phi-mu
FIRST_RESIDUAL_FIXED_POWER_DEFICIT_SAVING_PROVED=true
SQRT_SATURATION_REQUIRES_FIRST_RESIDUAL_AT_CAP=true
SQRT_SATURATION_FIRST_RESIDUAL_EXPONENT=1/2-2phi
SQRT_SATURATION_GAUSSIAN_PRODUCT_EXPONENT=1/2
SQRT_SATURATION_GAUSSIAN_PAIR_BALANCED=true
SQRT_SATURATION_P_EXPONENT=1/4
SQRT_SATURATION_Q_EXPONENT=1/4
SQRT_SATURATION_P_PLUS_Q_EXPONENT=1/4
SQRT_SATURATION_P_MINUS_Q_EXPONENT=1/4
SQRT_SATURATION_GAUSSIAN_NORM_EXPONENT=1/2
SQRT_SATURATION_NORM_QUOTIENT_EXPONENT=1/2-chi
NORM_DIVISOR_REPARAMETERIZATION_GIVES_EXTRA_FIXED_POWER_SAVING=false
ROOT_LINE_AND_NORM_DIVISOR_VIEWS_MAY_BE_DOUBLE_CHARGED=false
REMAINING_RECEIVER=SquareRootThetaQuarterFullResidualBalancedGaussianPhysicalReciprocalSelectorDensity
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false
NEXT=Stage14-4de
```
