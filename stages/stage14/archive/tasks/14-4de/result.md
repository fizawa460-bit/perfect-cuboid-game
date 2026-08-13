# Stage14-4de — full-residual cross-coprimality and quarter-scale mixed fourth-root compression

## Status

`COMPLETE_FULL_RESIDUAL_CROSS_COPRIMALITY_MIXED_FOURTH_ROOT_COMPRESSION_AND_S_ROUTE_REACTIVATION`

Stage14-4de consumes merged `Stage14-4dd`, merged `Stage14-X14`, merged `Stage14-s7-45`, and the roadmap reactivation rule merged in PR #605.

The entering theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family power saving is proved here. The new result is an exact arithmetic compression of the only possible square-root equality packet.

The compression is material for the closed s route: the full first residual and the common core become the two coprime sign parts of one quarter-scale fourth-root modulus. This exact bridge did not exist when `s7-45` closed the route, so the roadmap reactivation test is positive.

---

## 1. Imported square-root equality packet

Merged 4dd proves that every possible square-root-saturating sequence satisfies

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/2-2phi=1/4-chi,
u_res=B^(A_phi+o(1)),
P*Q=B^(1/2+o(1)),
P,Q,P+Q,P-Q=B^(1/4+o(1)).                 (1.1)
```

Use the exact signed reconstruction variables

```text
D=delta*s,
A=alpha*r,
D>A>0,
```

so that, after the endpoint-small common quotient `g=B^o(1)`,

```text
P=(D+A)/g,
Q=(D-A)/g.                                      (1.2)
```

Hence

```text
H_+ := D^2+A^2,
H_- := D^2-A^2=(D-A)(D+A).                     (1.3)
```

Merged X14, using merged 4cg, gives the plus-factor support

```text
oddpart(H_+) = C * oddpart(S*T) * B^o(1)         (1.4)
```

in the precise fixed-power/support sense of the already-frozen endpoint and good-core peels.

Merged s7-27 gives the minus-factor support

```text
oddpart(H_-) = oddpart(R*J) * oddpart(u_res)      (1.5)
```

again up to the finite/endpoint-small 2-primary decoration already absorbed throughout 4dc--4dd.

The fixed-power exponents on equality are

```text
C                 : chi,
u_res             : 1/4-chi,
S*T               : 1/2-chi,
R*J               : chi+1/4.                    (1.6)
```

In particular

```text
C*u_res = B^(1/4+o(1)).                           (1.7)
```

---

## 2. Plus and minus norm factors are odd-coprime up to `B^o(1)`

The elementary identity

```text
gcd(D^2+A^2,D^2-A^2)
 | gcd(2D^2,2A^2)
 | 2*gcd(D,A)^2                                  (2.1)
```

is exact.

Now

```text
D=delta*s,
A=alpha*r,
gcd(alpha,delta)=1.                              (2.2)
```

If an odd prime divides both `D` and `A`, then because it cannot divide both `alpha` and `delta`, it must divide the endpoint-small product `r*s`. Therefore

```text
oddpart(gcd(D,A)) | oddpart(r*s),                 (2.3)
```

and merged endpoint bookkeeping has

```text
r*s=B^o(1).                                       (2.4)
```

Consequently

```text
boxed:
oddpart(gcd(H_+,H_-))=B^o(1).                     (2.5)
```

Combining (1.4)--(1.5) with (2.5), every cross gcd between a plus-side factor and a minus-side factor is subpolynomial. In particular

```text
boxed:
gcd(C,oddpart(u_res))=B^o(1),                     (2.6)

boxed:
gcd(oddpart(S*T),oddpart(u_res))=B^o(1).          (2.7)
```

The second relation is a new exact bridge between the X14 xi-switch support and the 4dd full signed residual.

```text
FULL_RESIDUAL_PLUS_MINUS_CROSS_GCD_BO1=true
COMMON_CORE_FIRST_RESIDUAL_CROSS_GCD_BO1=true
XI_SWITCH_FIRST_RESIDUAL_CROSS_GCD_BO1=true.
```

---

## 3. Remove only subpolynomial gcd/unit defects

Let `C0=C/B^o(1)` be the merged good core of 4dc/4dd, and let `u0` be the odd fixed-power part of `u_res` after the same finite 2-primary convention.

By (2.6),

```text
G0:=gcd(C0,u0)=B^o(1).                            (3.1)
```

Remove this common divisor from both sides, and also remove the odd prime-power factors dividing `D*A`. Such unit defects are subpolynomial: if an odd prime divides `H_+` (or `H_-`) and also `D*A`, then it divides both `D` and `A`, hence belongs to (2.3).

Thus there exist odd integers

```text
C_* | C0,
u_* | u0,
Q_mix := C_* u_*                                  (3.2)
```

such that

```text
gcd(C_*,u_*)=1,
gcd(Q_mix,D*A)=1,
C_*=C*B^o(1)^(-1),
u_*=u_res*B^o(1)^(-1).         (3.3)
```

By the equality scales (1.7),

```text
boxed:
Q_mix=B^(1/4+o(1)).                               (3.4)
```

This quarter exponent is independent of `phi` across the entire square-root band.

---

## 4. Common core and first residual are opposite root types

Because `C_*|H_+` and `u_*|H_-`,

```text
D^2+A^2 == 0 (mod C_*),
D^2-A^2 == 0 (mod u_*).                           (4.1)
```

Since `A` is a unit modulo `Q_mix`, define

```text
t := D*A^{-1} (mod Q_mix).                        (4.2)
```

Then

```text
boxed:
t^2 == -1 (mod C_*),                             (4.3)

boxed:
t^2 == +1 (mod u_*).                             (4.4)
```

Because the two moduli are coprime,

```text
boxed:
t^4 == 1 (mod Q_mix).                            (4.5)
```

Thus the full-residual square-root packet lies on one primitive mixed fourth-root line modulo a quarter-scale modulus.

The root is not a generic fourth root with forgotten physical origin: the `-1` prime powers are precisely the common-core part and the `+1` prime powers are precisely the first-residual part after the subpolynomial peels.

```text
MIXED_FOURTH_ROOT_LINE_PROVED=true
MIXED_ROOT_MINUS_ONE_FACTOR=C_*
MIXED_ROOT_PLUS_ONE_FACTOR=u_*.
```

---

## 5. The root label recovers the `C/u_res` prime-power allocation

For odd `Q_mix`,

```text
gcd(t^2-1,t^2+1) | 2.                             (5.1)
```

Hence no odd prime power of `Q_mix` can divide both factors. Since `Q_mix|t^4-1`, every prime power of `Q_mix` lies wholly in exactly one of them.

Therefore the allocation is recovered exactly by

```text
boxed:
u_* = gcd(Q_mix,t^2-1),                          (5.2)

boxed:
C_* = gcd(Q_mix,t^2+1).                           (5.3)
```

up to the already-removed `B^o(1)` defects.

Thus replacing `(C_*,u_*)` by `(Q_mix,t)` loses no fixed-power physical information and introduces no divisor-allocation entropy.

```text
MIXED_ROOT_LABEL_RECOVERS_CORE_RESIDUAL_ALLOCATION=true
CORE_RESIDUAL_ALLOCATION_INDEPENDENT_SUPPORT=false.
```

---

## 6. Primitive fourth-root spacing and the exact `1/2` ledger

Peel

```text
h0=gcd(D,A)=B^o(1),
D=h0*D0,
A=h0*A0,
gcd(D0,A0)=1.                                    (6.1)
```

On square-root equality, merged 4dd gives

```text
D0,A0=B^(1/4+o(1)).                               (6.2)
```

For fixed `Q_mix` and fixed fourth-root label `t`, the pair satisfies

```text
D0 == t*A0 (mod Q_mix).                           (6.3)
```

Two distinct primitive pairs on the same root line have nonzero determinant divisible by `Q_mix`. The standard primitive dyadic root-line lemma therefore gives

```text
#(D0,A0 | Q_mix,t)
 <= B^o(1)*(1+D0*A0/Q_mix)
 <= B^(1/4+o(1)).                                 (6.4)
```

For an odd modulus, the number of fourth roots of unity is at most

```text
4^omega(Q_mix)=B^o(1).                            (6.5)
```

The number of possible quarter-scale moduli is at most `B^(1/4+o(1))`. Hence the complete deterministic ledger is

```text
Q_mix choice                : 1/4
mixed fourth-root lift      : 1/4
post-root physical filters  : 0
---------------------------------
total                       : 1/2.                (6.6)
```

So the new compression does **not** by itself prove a strict sub-square-root whole-family bound.

```text
MIXED_FOURTH_ROOT_COMPRESSION_GIVES_EXTRA_FIXED_POWER_SAVING=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2.
```

The old `C` root line, the `u_res` signed residual support, and the new `Q_mix` root line are alternative charged-once coordinate systems for the same equality mass and must not be multiplied as independent savings.

---

## 7. New receiver

The remaining mainline receiver is

```text
SquareRootQuarterScaleMixedFourthRootFullResidualPhysicalCompletionDensity.
```

It consists of primitive balanced pairs

```text
D0,A0=B^(1/4+o(1)),
Q_mix=B^(1/4+o(1)),
t^4=1 mod Q_mix,
D0=t*A0 mod Q_mix,
```

where the root label recovers the physical factorization

```text
Q_mix=C_*u_*,
t^2=-1 on C_*,
t^2=+1 on u_*,
```

and all original squarefree-cell, xi-switch, interval, reciprocal, Cayley, orientation and reverse-reconstruction masks are retained.

A strict sub-square-root result must prove power sparsity of the **physical completion selector** inside this quarter-scale mixed-root family, or find another exact relation not already encoded in `(Q_mix,t,D0,A0)`.

---

## 8. s-route reactivation decision — TRUE

Merged s7-45 closed the s route with

```text
NEXT_S_ROUTE=NONE_UNTIL_NEW_EXACT_STRUCTURE.
```

The merged roadmap requires every material receiver change to decide whether a new exact result creates an actionable s-specific receiver.

Stage14-4de does.

The exact new bridge is

```text
full-residual saturation
+ plus/minus cross-coprimality
+ X14 switch-support identification
=> Q_mix=C_*u_*=B^(1/4+o(1))
=> t^2=-1 on C_*, t^2=+1 on u_*
=> t^4=1 mod Q_mix
=> (Q_mix,t) recovers the C/u_res allocation.       (8.1)
```

This structure explicitly uses the s-owned signed residual `u_res` and its allocation against the common core. It was not available at the s7-45 closure snapshot and it is more than a renaming of the old positive zero-frequency receiver.

It therefore satisfies the roadmap reactivation rule:

```text
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true
S_ROUTE_REACTIVATION_TRIGGER=FULL_RESIDUAL_CROSS_GCD_AND_MIXED_FOURTH_ROOT_COMPRESSION
S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46
S_ROUTE_REACTIVATION_REASON=new quarter-scale mixed +/- root modulus couples the full signed residual to the common core and recovers their prime-power allocation in s coordinates.
```

The reactivated s receiver is

```text
SquareRootQuarterScaleMixedFourthRootSignedResidualPhysicalCompletionIncidence.
```

`Stage14-s7-46` should consume the new mixed-root factorization and test the second reciprocal / xi-switch completion against it. It must not reopen the already-exhausted s7 gcd/CRT/common-core spacing mechanisms or re-audit sH44.

```text
S7_46_SCHEDULED=true
SH44_REOPENED=false
NEW_S_AUXILIARY_H_NEEDED=false.
```

---

## 9. H / tH / fixed-U decision

The new mixed-root object is exact arithmetic and has not yet been exhausted internally. Therefore no new mainline H is requested.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false.
```

Merged t84 is a fixed-U primitive binary-norm / largest-prime receiver. No exact charged-once adapter from `(Q_mix,t,D0,A0)` to the t84 coefficient space is proved here.

```text
T84_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 10. Whole-family ledger and next stages

No global exponent change is claimed:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The mainline continues with

```text
NEXT=Stage14-4df.
```

The s route should now also restart at

```text
NEXT_S_ROUTE=Stage14-s7-46.
```

---

## Stage boundary

```text
STAGE14_4DE=COMPLETE_FULL_RESIDUAL_CROSS_COPRIMALITY_MIXED_FOURTH_ROOT_COMPRESSION_AND_S_ROUTE_REACTIVATION
MERGED_4DD_IMPORTED=true
MERGED_X14_IMPORTED=true
MERGED_S7_45_CLOSURE_IMPORTED=true
ROADMAP_S_REACTIVATION_RULE_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FULL_RESIDUAL_PLUS_MINUS_CROSS_GCD_BO1=true
COMMON_CORE_FIRST_RESIDUAL_CROSS_GCD_BO1=true
XI_SWITCH_FIRST_RESIDUAL_CROSS_GCD_BO1=true
MIXED_MODULUS_EXPONENT=1/4
MIXED_FOURTH_ROOT_LINE_PROVED=true
MIXED_ROOT_MINUS_ONE_FACTOR=C_*
MIXED_ROOT_PLUS_ONE_FACTOR=u_*
MIXED_ROOT_LABEL_RECOVERS_CORE_RESIDUAL_ALLOCATION=true
CORE_RESIDUAL_ALLOCATION_INDEPENDENT_SUPPORT=false
MIXED_FOURTH_ROOT_COMPRESSION_GIVES_EXTRA_FIXED_POWER_SAVING=false
REMAINING_RECEIVER=SquareRootQuarterScaleMixedFourthRootFullResidualPhysicalCompletionDensity
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true
S_ROUTE_REACTIVATION_TRIGGER=FULL_RESIDUAL_CROSS_GCD_AND_MIXED_FOURTH_ROOT_COMPRESSION
S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46
S_ROUTE_REACTIVATION_RECEIVER=SquareRootQuarterScaleMixedFourthRootSignedResidualPhysicalCompletionIncidence
S7_46_SCHEDULED=true
SH44_REOPENED=false
NEW_S_AUXILIARY_H_NEEDED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false
T84_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false
NEXT_S_ROUTE=Stage14-s7-46
NEXT=Stage14-4df
```
