# Stage14-4df — within-side overlap amplification and pairwise-separated square-root saturation

## Status

`COMPLETE_WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_AND_PAIRWISE_SEPARATED_SQRT_SATURATION`

Stage14-4df consumes merged `Stage14-4de` and the exact factor identities imported there from `4cg`, `s7-27`, `4dd`, and `X14`.

The entering theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family power saving is proved here. The new result is a fixed-stratum saving which eliminates every square-root packet carrying a fixed-power overlap between the two factors on either side of the `D^2 +/- A^2` decomposition.

---

## 1. Imported 4de equality packet

Every possible square-root-saturating sequence satisfies

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

Merged 4cg and s7-27 give, on odd parts,

```text
oddpart(H_+) = C * X_o,
X_o := oddpart(S*T),

oddpart(H_-) = R_o * u_o,
R_o := oddpart(R*J),
u_o := oddpart(u_res),
```

up to the frozen 2-primary convention.

Merged 4de removes only subpolynomial cross/unit defects and supplies odd factors

```text
C_* | C,
u_* | u_o,
Q_mix=C_*u_*,
gcd(C_*,u_*)=1,
gcd(Q_mix,D*A)=1,
Q_mix=B^(1/4+o(1)).
```

It also proves every plus/minus cross gcd is `B^o(1)`. The mixed root is

```text
t=D*A^(-1) mod Q_mix,
t^2=-1 mod C_*,
t^2=+1 mod u_*.
```

The 4de complete ledger is exactly `1/2`.

---

## 2. The two same-side overlaps

Define

```text
W_+ := gcd(C_*,X_o),
W_- := gcd(u_*,R_o).
```

Write

```text
W_+=B^(w_++o(1)),
W_-=B^(w_-+o(1)).
```

Since

```text
W_+|C_*,
W_-|u_*,
```

once `(C_*,u_*)` has been chosen, the possible pair `(W_+,W_-)` is only divisor-many:

```text
#(W_+,W_- | C_*,u_*)
 <= tau(C_*) tau(u_*)
 = B^o(1).
```

Thus `w_+` and `w_-` are not new ambient support exponents.

Also

```text
0<=w_+<=chi,
0<=w_-<=A_phi,
w_++w_-<=1/4.
```

---

## 3. Overlap lifts the actual root modulus

From

```text
oddpart(H_+)=C*X_o
```

and `W_+|X_o`, primewise valuations give

```text
C_* W_+ | H_+.
```

Likewise

```text
u_* W_- | H_-.
```

After the already-known `B^o(1)` plus/minus cross peel, define

```text
C_eff:=C_*W_+,
u_eff:=u_*W_-,
Q_eff:=C_eff*u_eff
      =Q_mix*W_+*W_-.
```

Then

```text
D^2+A^2 == 0 mod C_eff,
D^2-A^2 == 0 mod u_eff,
```

and, with `t_eff=D*A^(-1) mod Q_eff`, exact CRT gives

```text
t_eff^2 == -1 mod C_eff,
t_eff^2 == +1 mod u_eff,
t_eff^4 == 1 mod Q_eff.
```

Therefore

```text
WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true.
```

The extra overlap powers introduce only `B^o(1)` root-label multiplicity.

---

## 4. Primitive effective-root spacing

Remove the endpoint-small coordinate gcd:

```text
D=h0*D0,
A=h0*A0,
h0=B^o(1),
gcd(D0,A0)=1.
```

On square-root equality

```text
D0,A0=B^(1/4+o(1)),
D0*A0=B^(1/2+o(1)).
```

For fixed effective root label,

```text
D0 == t_eff*A0 mod Q_eff.
```

The primitive dyadic root-line lemma gives

```text
#(D0,A0 | C_*,u_*,W_+,W_-,t_eff)
 << B^o(1)*(1+D0*A0/Q_eff).
```

Since

```text
Q_eff=B^(1/4+w_++w_-+o(1)),
```

we obtain

```text
E_root <= 1/4-w_+-w_-.
```

---

## 5. Charged-once fixed-overlap count

Use the legal order

```text
C_*,u_*
-> divisor overlaps W_+,W_-
-> effective mixed-root label
-> primitive (D0,A0)
-> retained physical filters.
```

The common-core/full-residual support costs

```text
chi+A_phi=1/4.
```

The overlap choice and root label cost `0` at fixed-power scale. Hence

```text
boxed:
E_4df(w_+,w_-)
 <=1/4+(1/4-w_+-w_-)
 =1/2-w_+-w_-.
```

Therefore every fixed-power same-side overlap is strict sub-square-root:

```text
FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true
FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true
COMBINED_WITHIN_SIDE_OVERLAP_SAVING=w_++w_-.
```

---

## 6. Square-root equality is pairwise separated

Any sequence still saturating `1/2` must have

```text
w_+=0,
w_-=0.
```

Equivalently,

```text
gcd(C_*,X_o)=B^o(1),
gcd(u_*,R_o)=B^o(1).
```

Merged 4de already proves every plus/minus cross gcd is `B^o(1)`. Combining the cross relations with these two same-side relations yields

```text
C_*, X_o, u_*, R_o
```

pairwise separated at fixed-power scale.

Thus the only possible square-root equality packet has

```text
plus norm : H_+ ~ C_* X_o,
minus norm: H_- ~ u_* R_o,
```

with no fixed-power prime support shared among the four blocks.

```text
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true.
```

---

## 7. Refined receiver

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

On the zero-overlap stratum the ledger remains

```text
C_*,u_* support : 1/4
primitive root   : 1/4
----------------------
total            : 1/2.
```

Therefore

```text
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

---

## 8. s-route lifecycle — no repeated reactivation decision while active

Stage14-4de already made the positive reactivation decision and scheduled

```text
Stage14-s7-46.
```

Therefore Stage14-4df does **not** repeat the yes/no reactivation test. It only refines the receiver supplied to the already-reactivated s route:

```text
S_ROUTE_CURRENT_STATE=REACTIVATED_SCHEDULED_AT_STAGE14_S7_46
S_ROUTE_REACTIVATION_DECISION_REQUIRED=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true
S_ROUTE_ACTIVE_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootSignedResidualPhysicalCompletionIncidence
S7_46_SCHEDULED=true
SH44_REOPENED=false
NEW_S_AUXILIARY_H_NEEDED=false.
```

Operational rule:

```text
while s route is active or already scheduled after a reactivation:
    do not ask/recompute whether to reactivate s
when s route declares CLOSED again:
    resume the reactivation check on later material receiver changes
```

The new `W_- = gcd(u_*,R_o)` peel is passed to `s7-46` because it is directly in the signed-residual/agreement coordinates, but that is an input refinement, not another reactivation decision.

---

## 9. H / tH / fixed-U decision

The mainline still has unexhausted exact arithmetic after the pairwise-separation peel, so no new mainline H is requested.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false.
```

Merged `t85` and `tH24` remain in a fixed-`U` coefficient space. No exact charged-once adapter is proved here.

```text
T85_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 10. Whole-family ledger and next stages

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The local theorem is

```text
WITHIN_SIDE_OVERLAP_EXPONENT=w_++w_-
=> E<=1/2-(w_++w_-).
```

Next mainline:

```text
NEXT=Stage14-4dg.
```

Already-reactivated s route:

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
S_ROUTE_CURRENT_STATE=REACTIVATED_SCHEDULED_AT_STAGE14_S7_46
S_ROUTE_REACTIVATION_DECISION_REQUIRED=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true
S_ROUTE_ACTIVE_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootSignedResidualPhysicalCompletionIncidence
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