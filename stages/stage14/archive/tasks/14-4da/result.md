# Stage14-4da — square-root root-gcd excess peel and matched lost-core saturation

## Status

`COMPLETE_SQRT_ROOT_GCD_EXCESS_PEEL_AND_MATCHED_LOST_CORE_SATURATION_REFINEMENT`

Stage14-4da consumes merged `Stage14-X13`, merged `Stage14-4cz`, merged `Stage14-4cx`, merged `Stage14-s7-41`, and the earlier exact root-gcd / column infrastructure.

The entering canonical theorem is the merged X13 square-root bound

```text
V(B) << B^(1/2+o(1)).
```

Stage14-4da does not claim a new whole-family exponent. It proves that every square-root-saturating packet must have:

1. no fixed-power same-side root gcd;
2. no fixed-power cross-root square in excess of the already-forced lost core;
3. the cross-root square and the lost core matched at exponent scale.

The new receiver is

```text
SquareRootThetaQuarterCrossRootSquareMatchedLostCorePrimitiveSingleColumnIncidence.
```

No external theorem is used.

---

## 1. Imported square-root saturation band

Merged X13 proves

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Its possible equality band is

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
0<=s<=phi-5/24.                                   (1.1)
```

Here

```text
H=oddpart(gcd(X,Y))=H_S*H_T
```

is the cross-root gcd from the four root-gcd cells.

At `theta=1/4`, the merged X13 fixed-power count is

```text
common-core + primitive-pair base = 2phi,
residual single-column support     = 1/4-chi,
post-column reciprocal completion  = B^o(1).
```

Set

```text
a_col:=1/4-chi=1/2-2phi.                           (1.2)
```

Then

```text
2phi+a_col=1/2.                                    (1.3)
```

The goal of 4da is to refine the single column support `a_col` using exact gcd divisibility.

---

## 2. Lost core and cross-root square

Use the merged 4cx notation

```text
J=B^(j+o(1)),
D=C/J,
D0=D/gcd(D,Omega_0),
Omega_0=B^o(1).                                    (2.1)
```

Merged 4cx proves exactly

```text
D0 | H^2,                                           (2.2)

gcd(J,H)=1,                                        (2.3)

H|h_-,
H|h_+,
H^2|h_-h_+,                                        (2.4)

D0|h_-h_+.                                         (2.5)
```

At exponent scale

```text
D0=B^(d+o(1)),
d=chi-j.                                           (2.6)
```

Because of (2.2),

```text
d<=2s.                                             (2.7)
```

Merged 4cx removes `D0` before counting the residual column. Since

```text
|h_-h_+|<=B^(1/4-j+o(1)),
```

the quotient after removing `D0` has size

```text
boxed:
R_col:=(h_-h_+)/D0,
|R_col|<=B^(a_col+o(1)).                            (2.8)
```

This is the exact single-column support retained by merged X13.

---

## 3. Cross-root excess is a fixed squareclass

Define the exact cross-root excess

```text
boxed:
G:=H^2/D0.                                         (3.1)
```

This is an integer by (2.2). Moreover (2.4)-(2.5) imply

```text
boxed:
G | R_col.                                         (3.2)
```

Fix `D0`. Let

```text
r0:=sqf(D0)
```

be its squarefree kernel. Since

```text
D0*G=H^2
```

is a perfect square, prime valuations give

```text
v_p(G) == v_p(D0) (mod 2).
```

Therefore

```text
boxed:
G=r0*t^2                                           (3.3)
```

for some positive integer `t`.

This is an exact squareclass statement, not an asymptotic approximation.

Write

```text
G=B^(e+o(1)).                                      (3.4)
```

For fixed `D0`, the squarefree kernel `r0` is already fixed. Hence the number of possible `G` values in this dyadic range is bounded by the number of possible `t`, namely

```text
boxed:
#G <= B^(e/2+o(1)).                                (3.5)
```

The bound is deliberately conservative: any fixed-power contribution of `r0` only makes `t` shorter.

At exponent scale

```text
e=2s-d=2s-(chi-j)=j+2s-chi.                       (3.6)
```

Thus

```text
e>=0                                               (3.7)
```

by (2.7).

---

## 4. Same-side root gcd survives the lost-core division

Define the same-side odd root gcd

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
K=K_x*K_y.                                         (4.1)
```

Merged 4cz proves the primewise support facts

```text
gcd(K,C)=1,                                        (4.2)
K|L_-,
K|L_+,
K^2|h_-h_+.                                        (4.3)
```

Because `D0|C`, (4.2) gives

```text
gcd(K,D0)=1.                                       (4.4)
```

Therefore the square divisor in (4.3) survives the lost-core division:

```text
boxed:
K^2 | R_col.                                       (4.5)
```

The four root-gcd cells are pairwise coprime, hence

```text
gcd(K,H)=1.                                        (4.6)
```

Using (3.1),

```text
gcd(K,G)=1.                                        (4.7)
```

Combining (3.2), (4.5), and (4.7),

```text
boxed:
K^2*G | R_col.                                     (4.8)
```

Write

```text
K=B^(kappa+o(1)).                                  (4.9)
```

---

## 5. Forced-divisor feasibility

From (2.8) and (4.8), every physical square-root-band packet satisfies

```text
2kappa+e <= a_col+o(1).                            (5.1)
```

Thus if a fixed-power stratum has

```text
2kappa+e>a_col,
```

it is empty.

This is already a strict contraction near the right endpoint `phi=1/4`, where `a_col=0` and therefore

```text
kappa=e=0                                          (5.2)
```

at fixed-power scale.

---

## 6. Charged-once root-gcd excess count

Fix the once-charged common-core / primitive-pair base, hence fixed `C`, `J`, and `D0` up to divisor-many choices. The base cost remains

```text
2phi.                                              (6.1)
```

Now stratify by

```text
K=B^(kappa+o(1)),
G=B^(e+o(1)).
```

The costs are:

```text
choice of K:                 kappa,
choice of G in fixed class:  <=e/2,
remaining column quotient:   <=a_col-2kappa-e,
```

on every nonempty fixed-power stratum by (5.1).

Therefore

```text
E_4da(kappa,e)
 <=2phi
   +kappa
   +e/2
   +(a_col-2kappa-e).                              (6.2)
```

Using (1.3),

```text
boxed:
E_4da(kappa,e)
 <=1/2-kappa-e/2.                                  (6.3)
```

This is a complete count of the same physical square-root-band packet: after the reduced column fixes `M`, merged X13 gives only `B^o(1)` post-column reciprocal completion.

No row lift is reintroduced.

---

## 7. Consequence for square-root saturation

Equation (6.3) immediately gives:

```text
kappa>0 fixed power
=> E<1/2,                                          (7.1)

e>0 fixed power
=> E<1/2.                                          (7.2)
```

Hence every sequence that can still saturate the square-root envelope must satisfy

```text
boxed:
kappa=0,                                           (7.3)

boxed:
e=0.                                               (7.4)
```

Equivalently,

```text
boxed:
K=B^o(1),                                          (7.5)

boxed:
H^2/D0=B^o(1).                                     (7.6)
```

At exponent scale, (7.4) and (3.6) give

```text
boxed:
chi-j=2s,                                          (7.7)

boxed:
j=chi-2s.                                         (7.8)
```

Thus the entire fixed-power cross-root square is consumed by the lost core:

```text
boxed:
D0=H^2*B^o(1)                                     (7.9)
```

in exponent/valuation-scale notation.

This does not mean literal equality at endpoint-small primes; it means the quotient `H^2/D0` has no fixed-power size.

---

## 8. Refined square-root band

Combine merged X13

```text
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4                                       (8.1)
```

with (7.8):

```text
j=2phi-1/4-2s.                                     (8.2)
```

Since

```text
s<=phi-5/24,
```

we get

```text
j>=2phi-1/4-2(phi-5/24)=1/6.                       (8.3)
```

Also `s>=0` gives

```text
j<=chi.                                            (8.4)
```

Therefore every possible square-root saturation packet now satisfies

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4,
1/6<=j<=chi,
j=chi-2s,
K=B^o(1),
H^2/D0=B^o(1).                                    (8.5)
```

The remaining residual column exponent is still

```text
a_col=1/2-2phi.                                    (8.6)
```

but it no longer carries any fixed-power same-side gcd or any fixed-power cross-root-square excess beyond `D0`.

---

## 9. New minimal receiver

Merged X13 leaves

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence.
```

Stage14-4da narrows it to

```text
boxed:
SquareRootThetaQuarterCrossRootSquareMatchedLostCorePrimitiveSingleColumnIncidence.
```

Its mandatory fixed-power data are

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
0<=s<=phi-5/24,
J=B^(j+o(1)),
j=chi-2s,
1/6<=j<=chi,
K=B^o(1),
D0=H^2*B^o(1),
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal completion=B^o(1).
```

The next deterministic question is prime-power allocation: how the matched `H^2` valuation is distributed through the Cayley-bad/lost-core component and the two endpoint-linear signs before the residual column is counted.

---

## 10. Whole-family exponent

The current whole-family theorem remains the merged X13 result

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2.         (10.1)
```

Stage14-4da proves strict sub-square-root bounds only on fixed-power root-gcd-excess strata; it does not produce a uniform positive `delta` on the remaining matched stratum.

Therefore

```text
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false,
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false,
SQRT_B_UPPER_BOUND_PROVED=true.                    (10.2)
```

---

## 11. Relation to merged s7-41 and the H gate

Merged s7-41 opened an H gate for the old `23/44` twin-short receiver. Merged X13 superseded that gate for square-root closure using reverse reciprocal reconstruction.

Stage14-4da works strictly after merged X13 and never reopens the eliminated row-lift/twin-short problem.

The remaining square-root receiver still has unused exact prime-power structure, namely

```text
D0=H^2*B^o(1)
```

and the sign allocation of the matched lost core.

Therefore no new mainline H theorem is requested at 4da:

```text
MAINLINE_H_NEEDED=false,
MAINLINE_BLOCKED_BY_H=false,
S7_41_MAINLINE_H_GATE_SUPERSEDED=true,
GENERIC_GENUS_ONE_H_REOPENED=false.                (11.1)
```

If exact prime-power allocation is exhausted and a stable average remains, any future H target must be stated on the new matched-lost-core **single-column** receiver, not on the old twin-short incidence.

---

## 12. t/tH route compatibility

Merged tH22 and the t79/t80 fixed-U projective-ray route remain a different coefficient space. They are not used to prove (6.3) or the saturation contraction.

```text
TH22_CROSS_PROMOTED_TO_MAINLINE=false,
T79_CROSS_PROMOTED_TO_MAINLINE=false,
T80_CROSS_PROMOTED_TO_MAINLINE=false.              (12.1)
```

---

## 13. Validation contract

The dedicated 4da audit must verify:

1. `D0|H^2` squareclass identity;
2. fixed-`D0` representation `G=sqf(D0)*t^2`;
3. pairwise coprimality of same-side and cross-root cells;
4. divisibility `K^2*G|R_col` in synthetic prime-power models;
5. exact exponent identity `E_4da=1/2-kappa-e/2`;
6. feasibility constraint `2kappa+e<=a_col`;
7. square-root saturation requires `kappa=e=0`;
8. `j=chi-2s` and `j>=1/6` on the refined band;
9. merged X13 regression;
10. merged 4cz / 4cx regressions;
11. theorem-boundary locks.

---

## Stage boundary

```text
STAGE14_4DA=COMPLETE_SQRT_ROOT_GCD_EXCESS_PEEL_AND_MATCHED_LOST_CORE_SATURATION_REFINEMENT
MERGED_X13_SQRT_IMPORTED=true
MERGED_4CZ_IMPORTED=true
MERGED_4CX_IMPORTED=true
MERGED_S7_41_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
LOST_CORE_D0_DIVIDES_CROSS_ROOT_SQUARE=true
CROSS_ROOT_EXCESS_G=H^2/D0
FIXED_D0_CROSS_ROOT_EXCESS_HAS_FIXED_SQUARECLASS=true
CROSS_ROOT_EXCESS_CHOICE_EXPONENT_AT_MOST=e/2
SAMESIDE_ROOT_GCD_SQUARE_SURVIVES_LOST_CORE_DIVISION=true
RESIDUAL_COLUMN_FORCED_DIVISOR=K^2*G
ROOT_GCD_EXCESS_FEASIBILITY=2kappa+e<=1/4-chi
ROOT_GCD_EXCESS_COMPLETE_COUNT=1/2-kappa-e/2
FIXED_POWER_SAMESIDE_ROOT_GCD_STRICTLY_SUBSQRT=true
FIXED_POWER_CROSS_ROOT_EXCESS_STRICTLY_SUBSQRT=true
SQRT_SATURATION_SAMESIDE_ROOT_GCD=Bo1
SQRT_SATURATION_CROSS_ROOT_EXCESS=Bo1
SQRT_SATURATION_LOST_CORE_EXPONENT=2s
SQRT_SATURATION_JOINT_CORE_EXPONENT=chi-2s
SQRT_SATURATION_JOINT_CORE_LOWER_EXPONENT=1/6
REMAINING_RECEIVER=SquareRootThetaQuarterCrossRootSquareMatchedLostCorePrimitiveSingleColumnIncidence
S7_41_MAINLINE_H_GATE_SUPERSEDED=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
T79_CROSS_PROMOTED_TO_MAINLINE=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4db
```
