# Stage14-4df — within-side overlap amplification after s7-46

## Status

`COMPLETE_S7_46_COFACTOR_OVERLAP_EFFECTIVE_MODULUS_LIFT_AND_PAIRWISE_SEPARATED_SQRT_SATURATION`

Stage14-4df consumes merged `Stage14-4de` and merged `Stage14-s7-46`.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family power saving is proved here. The new theorem eliminates every fixed-power overlap between the mixed-root sign modulus and the complementary balanced xi cofactors reconstructed by s7-46.

---

## 1. Imported canonical mixed-root/cofactor packet

Merged 4de and s7-46 confine possible square-root saturation to

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/4-chi=1/2-2phi,
D,A=B^(1/4+o(1)),
gcd(D,A)=B^o(1).
```

After the standard odd/endpoint peels,

```text
Q_mix=C_*u_*,
C_*=gcd(Q_mix,t^2+1),
u_*=gcd(Q_mix,t^2-1),
t^4=1 mod Q_mix,
D=t*A mod Q_mix,
Q_mix=B^(1/4+o(1)).
```

Merged s7-46 proves finite-fiber equivalence between physical square-root packets and physical-admissible mixed tuples. It also reconstructs the complementary cofactors

```text
M_+ := oddpart(D^2+A^2)/C_*
     = oddpart(S*T)*B^o(1),

M_- := oddpart(D^2-A^2)/u_*
     = oddpart(R*J)*B^o(1),
```

with balanced squarefree divisor splits

```text
M_+=S*T,
M_-=R*J
```

up to `B^o(1)` decorations. The second reciprocal and post-column completion have `B^o(1)` multiplicity.

Thus the current pre-4df receiver is exactly

```text
SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity.
```

---

## 2. Define the two same-side overlap divisors

Set

```text
W_+ := gcd(C_*,M_+),
W_- := gcd(u_*,M_-).
```

Write

```text
W_+=B^(w_++o(1)),
W_-=B^(w_-+o(1)).
```

The overlap pair has no independent polynomial support. For a fixed mixed tuple s7-46 reconstructs `M_+,M_-` with `B^o(1)` multiplicity; even without using that stronger statement,

```text
W_+|C_*,
W_-|u_*
```

makes the overlap choice divisor-many after `(C_*,u_*)` is fixed.

Hence

```text
OVERLAP_PAIR_INDEPENDENT_FIXED_POWER_SUPPORT=false.
```

The trivial scale bounds are

```text
0<=w_+<=chi,
0<=w_-<=A_phi,
w_++w_-<=1/4.
```

---

## 3. The overlaps lift the actual mixed-root modulus

By definition of `M_+`, after the same `B^o(1)` decoration peel,

```text
D^2+A^2 = C_* M_+ * B^o(1).
```

Because `W_+|C_*` and `W_+|M_+`, primewise valuations give

```text
C_*W_+ | D^2+A^2
```

up to the already-removed subpolynomial defect.

Likewise

```text
u_*W_- | D^2-A^2.
```

Merged 4de gives plus/minus cross-coprimality at fixed-power scale, so the effective moduli

```text
C_eff=C_*W_+,
u_eff=u_*W_-
```

remain coprime after `B^o(1)` peels. Define

```text
Q_eff=C_eff*u_eff
     =Q_mix*W_+*W_-.
```

Since `A` is a unit modulo the effective modulus, with

```text
t_eff=D*A^(-1) mod Q_eff,
```

we obtain

```text
t_eff^2=-1 mod C_eff,
t_eff^2=+1 mod u_eff,
t_eff^4=1 mod Q_eff.
```

Thus

```text
WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true.
```

The extra prime powers do not create polynomial root-label entropy: prescribed `+1/-1` roots over odd prime powers still have at most two Hensel lifts each, so the full label multiplicity is `B^o(1)`.

---

## 4. Primitive spacing on the effective line

Write

```text
D=h0*D0,
A=h0*A0,
h0=B^o(1),
gcd(D0,A0)=1.
```

The equality packet has

```text
D0,A0=B^(1/4+o(1)),
D0*A0=B^(1/2+o(1)).
```

For fixed effective root label,

```text
D0=t_eff*A0 mod Q_eff.
```

The primitive determinant-spacing lemma yields

```text
#(D0,A0 | effective root)
 << B^o(1)*(1+D0*A0/Q_eff).
```

Since

```text
Q_eff=B^(1/4+w_++w_-+o(1)),
```

we get

```text
E_root<=1/4-w_+-w_-.
```

---

## 5. Charged-once complete count

Use the legal s7-46 coordinate order

```text
(C_*,u_*) support
-> mixed root / primitive pair
-> M_+,M_- and balanced xi splits by finite-fiber reconstruction
-> signed reciprocal completion.
```

The first support costs

```text
chi+A_phi=1/4.
```

The overlap pair and root labels cost `0` at fixed-power scale. Section 4 costs `1/4-w_+-w_-`. All physical completion data are retained and s7-46 proves their multiplicity is `B^o(1)`.

Therefore

```text
boxed:
E_4df(w_+,w_-)
 <=1/2-w_+-w_-.
```

Consequently every fixed-power overlap stratum is strict sub-square-root:

```text
FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true
FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true
COMBINED_WITHIN_SIDE_OVERLAP_SAVING=w_++w_-.
```

---

## 6. Square-root saturation forces four-block separation

Any sequence saturating the global `1/2` theorem must have

```text
w_+=0,
w_-=0,
```

hence

```text
gcd(C_*,M_+)=B^o(1),
gcd(u_*,M_-)=B^o(1).
```

Merged 4de already supplies every plus/minus cross gcd as `B^o(1)`. Therefore all six pairwise gcds among

```text
C_*, M_+, u_*, M_-
```

are subpolynomial at fixed-power scale.

Equivalently, the four blocks are pairwise separated:

```text
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true.
```

Since s7-46 identifies

```text
M_+ ~ oddpart(S*T),
M_- ~ oddpart(R*J),
```

this is also a pairwise-separation theorem for the common-core, first-residual, xi-switch, and xi-agreement blocks.

---

## 7. Refined receiver

The remaining mainline receiver is

```text
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity.
```

It retains

```text
Q_mix=C_*u_*=B^(1/4+o(1)),
D0,A0=B^(1/4+o(1)),
t^2=-1 on C_*,
t^2=+1 on u_*,
M_+=S*T,
M_-=R*J,
S,T and R,J at the s7-46 balanced scales,
C_*,M_+,u_*,M_- pairwise separated at fixed-power scale,
all original physical masks,
full s7-46 finite-fiber reciprocal reconstruction.
```

On the zero-overlap stratum the complete deterministic ledger is still

```text
(C_*,u_*) support : 1/4
primitive root     : 1/4
completion         : 0
------------------------
total              : 1/2.
```

Thus

```text
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The next mainline step should attack the **simultaneous balanced divisor-split density under pairwise-separated support**, rather than reuse mixed-root spacing.

---

## 8. s-route lifecycle

Merged s7-46 has already consumed the 4de reactivation and put the s route into

```text
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED.
```

Therefore Stage14-4df performs **no reactivation yes/no decision**.

The operational rule is now

```text
S_ROUTE_REACTIVATION_DECISION_REQUIRED=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true.
```

4df only refines the receiver passed to the active s route:

```text
S_ROUTE_CURRENT_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
S_ROUTE_NEXT=Stage14-s7-47.
```

When a future s-stage explicitly closes the route again, the reactivation check becomes active for subsequent mainline/X/t/toolbox/q stages. Until then it is not repeated.

---

## 9. H / fixed-U decision

There remains unexhausted exact divisor-split structure, so no new mainline H is needed.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false.
```

Merged `t86/tH24` remain fixed-`U` coefficient-space results with no charged-once global adapter:

```text
T86_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 10. Whole-family boundary

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Next mainline:

```text
NEXT=Stage14-4dg.
```

Active s route:

```text
NEXT_S_ROUTE=Stage14-s7-47.
```

---

## Stage boundary

```text
STAGE14_4DF=COMPLETE_S7_46_COFACTOR_OVERLAP_EFFECTIVE_MODULUS_LIFT_AND_PAIRWISE_SEPARATED_SQRT_SATURATION
MERGED_4DE_IMPORTED=true
MERGED_S7_46_IMPORTED=true
S7_46_MIXED_TUPLE_PHYSICAL_FINITE_FIBER_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PLUS_WITHIN_SIDE_OVERLAP=W_+=gcd(C_*,M_+)
MINUS_WITHIN_SIDE_OVERLAP=W_-=gcd(u_*,M_-)
OVERLAP_PAIR_INDEPENDENT_FIXED_POWER_SUPPORT=false
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
REMAINING_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_REACTIVATION_DECISION_REQUIRED=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true
S_ROUTE_CURRENT_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
S_ROUTE_NEXT=Stage14-s7-47
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
T86_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dg
NEXT_S_ROUTE=Stage14-s7-47
```