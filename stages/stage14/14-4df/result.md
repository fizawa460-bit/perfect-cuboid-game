# Stage14-4df — within-side overlap amplification and pairwise-separated square-root saturation

## Status

`COMPLETE_WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_AND_PAIRWISE_SEPARATED_SQRT_SATURATION`

Stage14-4df consumes merged `Stage14-4de`, together with the exact factor identities already imported there from `4cg`, `s7-27`, `4dd`, and `X14`.

The entering theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family power saving is proved here.  The new result is a fixed-stratum saving which eliminates every square-root packet carrying a fixed-power overlap between the two factors on either side of the `D^2 +/- A^2` decomposition.

---

## 1. Imported 4de equality packet

Every possible square-root-saturating sequence already satisfies

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/2-2phi=1/4-chi,
u_res=B^(A_phi+o(1)),
D,A=B^(1/4+o(1)),
gcd(D,A)=B^o(1).
```

Put

```text
H_+ := D^2+A^2,
H_- := D^2-A^2>0.
```

Merged 4cg gives exactly on odd parts

```text
oddpart(H_+) = C * X_o,
X_o := oddpart(S*T),                               (1.1)
```

and merged s7-27 gives

```text
oddpart(H_-) = R_o * u_o,
R_o := oddpart(R*J),
u_o := oddpart(u_res),                                      (1.2)
```

up to the already-frozen finite 2-primary convention.

Merged 4de removes only subpolynomial cross/unit defects and supplies odd factors

```text
C_* | C,
u_* | u_o,
Q_mix=C_*u_*,
gcd(C_*,u_*)=1,
gcd(Q_mix,D*A)=1,
Q_mix=B^(1/4+o(1)).                                (1.3)
```

It also proves every plus/minus cross gcd is subpolynomial.  In particular, after an additional `B^o(1)` cross-support peel when needed,

```text
gcd(C_*X_o,u_*R_o)=1                              (1.4)
```

at fixed-power scale.

The mixed root is

```text
t=D*A^(-1) mod Q_mix,
t^2=-1 mod C_*,
t^2=+1 mod u_*.                                   (1.5)
```

The 4de complete ledger is exactly `1/2`.

---

## 2. The two unpeeled same-side overlaps

Define the odd same-side overlaps

```text
W_+ := gcd(C_*,X_o),
W_- := gcd(u_*,R_o).                               (2.1)
```

Write their dyadic fixed-power sizes as

```text
W_+=B^(w_++o(1)),
W_-=B^(w_-+o(1)).                                  (2.2)
```

Because

```text
W_+|C_*,
W_-|u_*,                                           (2.3)
```

once `(C_*,u_*)` has been chosen, the possible overlap pair `(W_+,W_-)` is only divisor-many:

```text
#(W_+,W_- | C_*,u_*)
 <= tau(C_*) tau(u_*)
 = B^o(1).                                         (2.4)
```

Thus `w_+` and `w_-` are not new ambient support exponents.

The trivial size constraints are

```text
0<=w_+<=chi,
0<=w_-<=A_phi,
w_++w_-<=chi+A_phi=1/4.                           (2.5)
```

---

## 3. Overlap forces an extra copy of the root modulus

Equation (1.1) and `W_+|X_o` give

```text
C_* W_+ | H_+.                                    (3.1)
```

Indeed primewise

```text
v_p(C_*W_+)
 =v_p(C_*)+min(v_p(C_*),v_p(X_o))
 <=v_p(C)+v_p(X_o)
 =v_p(oddpart(H_+)).                               (3.2)
```

Likewise (1.2) and `W_-|R_o` give

```text
u_* W_- | H_-.                                    (3.3)
```

After removing the `B^o(1)` plus/minus cross defect already bounded by 4de, the two effective moduli

```text
C_eff:=C_*W_+,
u_eff:=u_*W_-                                      (3.4)
```

are odd and coprime at fixed-power scale and remain coprime to `D*A`.

Therefore

```text
D^2+A^2 ==0 mod C_eff,
D^2-A^2 ==0 mod u_eff.                             (3.5)
```

With

```text
t_eff:=D*A^(-1) mod Q_eff,
Q_eff:=C_eff*u_eff
       =Q_mix*W_+*W_-,                             (3.6)
```

we obtain

```text
t_eff^2 == -1 mod C_eff,
t_eff^2 == +1 mod u_eff,
t_eff^4 == 1  mod Q_eff.                           (3.7)
```

Thus a same-side overlap is not merely a repeated prime in a factorization: it **amplifies the actual primitive root-line modulus by one extra copy of the overlap**.

```text
WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true.
```

---

## 4. Root multiplicity remains subpolynomial

For every odd prime power `p^e`, the congruences

```text
x^2=+1 mod p^e,
x^2=-1 mod p^e
```

have at most two roots of the prescribed type.  Hensel lifting across the extra overlap powers introduces no polynomial multiplicity.

Hence for fixed `(C_*,u_*,W_+,W_-)`, the number of effective mixed-root labels is at most

```text
4^omega(Q_eff)=B^o(1).                             (4.1)
```

No root-orientation support is charged independently.

---

## 5. Primitive effective-root spacing

Peel the already-known endpoint-small coordinate gcd:

```text
D=h0*D0,
A=h0*A0,
h0=B^o(1),
gcd(D0,A0)=1.                                    (5.1)
```

On square-root equality

```text
D0,A0=B^(1/4+o(1)),
D0*A0=B^(1/2+o(1)).                               (5.2)
```

For fixed effective root label,

```text
D0 == t_eff*A0 mod Q_eff.                         (5.3)
```

Two distinct primitive points on this line have a nonzero determinant divisible by `Q_eff`.  The primitive dyadic root-line lemma therefore gives

```text
#(D0,A0 | C_*,u_*,W_+,W_-,t_eff)
 << B^o(1)*(1+D0*A0/Q_eff).                       (5.4)
```

Now

```text
Q_eff
 =B^(1/4+w_++w_-+o(1)).                           (5.5)
```

and (2.5) ensures `w_++w_-<=1/4`.  Therefore

```text
boxed:
E_root <= 1/4-w_+-w_-.                            (5.6)
```

At the extreme `w_++w_-=1/4`, the root-line fiber is `B^o(1)`.

---

## 6. Charged-once fixed-overlap count

It is convenient here to use the legal 4de coordinate order

```text
C_*,u_*
-> divisor overlaps W_+,W_-
-> effective mixed-root label
-> primitive (D0,A0)
-> old physical completion filters.
```

The common-core and full-residual choices cost

```text
chi+A_phi=1/4.                                    (6.1)
```

By (2.4) the overlap choices cost `0` at fixed-power scale.  By Section 4 the root label costs `0`, and by Section 5 the primitive pair costs `1/4-w_+-w_-`.

All remaining cell, interval, reciprocal, Cayley, orientation and reverse-reconstruction conditions are retained as filters/fibers exactly as in merged 4de.

Hence

```text
boxed:
E_4df(w_+,w_-)
 <=1/4+(1/4-w_+-w_-)
 =1/2-w_+-w_-.                                    (6.2)
```

Therefore every stratum with

```text
w_++w_->=epsilon
```

for a fixed `epsilon>0` satisfies

```text
E_4df<=1/2-epsilon.                               (6.3)
```

```text
FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true
FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true
COMBINED_WITHIN_SIDE_OVERLAP_SAVING=w_++w_-.
```

---

## 7. Square-root equality is pairwise separated

A sequence which still saturates the global `1/2` theorem must have

```text
w_+=0,
w_-=0.                                            (7.1)
```

Equivalently,

```text
boxed:
gcd(C_*,X_o)=B^o(1),

boxed:
gcd(u_*,R_o)=B^o(1).                              (7.2)
```

Merged 4de already proves every cross gcd between a plus factor and a minus factor is `B^o(1)`.  Combining those cross relations with (7.2) gives the complete fixed-power separation

```text
boxed:
C_*, X_o, u_*, R_o
are pairwise coprime up to B^o(1).                 (7.3)
```

Thus the only possible square-root equality packet has four separated norm blocks:

```text
plus norm : H_+ ~ C_* X_o,
minus norm: H_- ~ u_* R_o,
```

with no fixed-power prime support shared anywhere between the four blocks.

```text
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true.
```

---

## 8. Refined receiver

The mainline receiver is now

```text
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootFullResidualPhysicalCompletionDensity.
```

It retains

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/4-chi,
C_*u_*=B^(1/4+o(1)),
D0,A0=B^(1/4+o(1)),
t^2=-1 on C_*,
t^2=+1 on u_*,
C_*,X_o,u_*,R_o pairwise separated at fixed-power scale,
all original physical masks and finite-fiber reverse reconstruction.
```

On the zero-overlap stratum the deterministic ledger is still

```text
C_*,u_* support : 1/4
primitive root   : 1/4
----------------------
total            : 1/2.                           (8.1)
```

So

```text
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The next mainline step should exploit the now pairwise-separated complementary quotients `X_o` and `R_o` against the physical reciprocal completion, rather than repeating the same mixed-root spacing.

---

## 9. s-route reactivation decision — remains TRUE

This stage materially refines the receiver, so the roadmap reactivation check is mandatory.

```text
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true.
```

The original 4de trigger remains valid, and 4df adds a new s-specific refinement:

```text
S_ROUTE_REACTIVATION_TRIGGER=FULL_RESIDUAL_MIXED_ROOT_PLUS_WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT
S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46
S_ROUTE_REACTIVATION_REASON=the s-owned signed residual overlap gcd(u_*,R_o) is a zero-cost divisor stratum whose extra copy lifts the +1 root modulus and yields a fixed-power saving; the surviving s packet is therefore the pairwise-separated mixed-root incidence.
```

The refined s receiver is

```text
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootSignedResidualPhysicalCompletionIncidence.
```

No new `sH` request is opened.  `s7-46` should consume this exact pairwise-separated receiver and test the second reciprocal / signed allocation structure without reopening the exhausted pre-closure gcd/CRT arguments.

```text
S_ROUTE_REACTIVATION_CONFIRMED_BY_STAGE14_4DF=true
S7_46_SCHEDULED=true
SH44_REOPENED=false
NEW_S_AUXILIARY_H_NEEDED=false.
```

---

## 10. H / tH / fixed-U decision

The mainline still has unexhausted exact arithmetic after the pairwise-separation peel, so no new mainline H is requested.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false.
```

Merged `t85` and `tH24` remain in a fixed-`U` primitive-binary-norm / selector-square coefficient space.  No exact charged-once adapter from the current global mixed-root packet is proved.

```text
T85_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 11. Whole-family ledger

No global exponent change is claimed:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The new local theorem is

```text
WITHIN_SIDE_OVERLAP_EXPONENT=w_++w_-
=> E<=1/2-(w_++w_-).
```

Next mainline stage:

```text
NEXT=Stage14-4dg.
```

Next s-route stage:

```text
NEXT_S_ROUTE=Stage14-s7-46.
```

---

## Stage boundary

```text
STAGE14_4DF=COMPLETE_WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_AND_PAIRWISE_SEPARATED_SQRT_SATURATION
MERGED_4DE_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PLUS_WITHIN_SIDE_OVERLAP=W_+=gcd(C_*,X_o)
MINUS_WITHIN_SIDE_OVERLAP=W_-=gcd(u_*,R_o)
WITHIN_SIDE_OVERLAP_CHOICES_AFTER_C_U=Bo1
EFFECTIVE_PLUS_ROOT_MODULUS=C_*W_+
EFFECTIVE_MINUS_ROOT_MODULUS=u_*W_-
EFFECTIVE_MIXED_ROOT_MODULUS=Q_mix*W_+*W_-
WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true
FIXED_OVERLAP_COMPLETE_COUNT_EXPONENT=1/2-w_+-w_-
FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true
FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true
SQRT_SATURATION_REQUIRES_W_PLUS=0
SQRT_SATURATION_REQUIRES_W_MINUS=0
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true
REMAINING_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootFullResidualPhysicalCompletionDensity
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true
S_ROUTE_REACTIVATION_CONFIRMED_BY_STAGE14_4DF=true
S_ROUTE_REACTIVATION_TRIGGER=FULL_RESIDUAL_MIXED_ROOT_PLUS_WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT
S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46
S_ROUTE_REACTIVATION_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootSignedResidualPhysicalCompletionIncidence
S7_46_SCHEDULED=true
SH44_REOPENED=false
NEW_S_AUXILIARY_H_NEEDED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
T85_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dg
NEXT_S_ROUTE=Stage14-s7-46
```