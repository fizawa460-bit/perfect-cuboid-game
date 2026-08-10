# Stage14-s7-46 — mixed fourth-root sign allocation, cofactor reconstruction, and second-reciprocal finite fiber

## Status

`COMPLETE_MIXED_FOURTH_ROOT_SIGN_ALLOCATION_COFACTOR_RECONSTRUCTION_AND_SECOND_RECIPROCAL_FINITE_FIBER`

Stage14-s7-46 is the first stage after the s-route reactivation requested by merged `Stage14-4de`.
It consumes merged `Stage14-4de`, merged `Stage14-4dd`, merged `Stage14-X14`, merged `Stage14-s7-45`, and the exact signed reciprocal infrastructure of merged `s7-27`, `s7-31`, and `s7-42`.

The entering whole-family theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here. The new result is a finite-fiber reconstruction theorem for the reactivated mixed-root coordinates.

The main point is that the quarter-scale root datum from 4de does more than remember the product `C*u_res`: it recovers the plus/minus root type, the residual sign allocation, the two complementary xi-cell products, and hence all first-reciprocal signed data up to `B^o(1)`. The second reciprocal then contributes no independent fixed-power support.

---

## 1. Imported square-root mixed-root packet

Every possible square-root saturation sequence is already confined by merged 4dd/4de to

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/2-2phi=1/4-chi,
u_res=B^(A_phi+o(1)),
D=delta*s,
A=alpha*r,
D,A=B^(1/4+o(1)),
r,s=B^o(1).
```

After the fixed endpoint-small / 2-primary peels of 4de, there are odd integers

```text
C_* = C*B^o(1)^(-1),
u_* = u_res*B^o(1)^(-1),
Q_mix=C_*u_*,
```

with

```text
gcd(C_*,u_*)=1,
gcd(Q_mix,D*A)=1,
Q_mix=B^(1/4+o(1)).
```

Define

```text
t := D*A^(-1) (mod Q_mix).
```

Merged 4de proves

```text
t^2=-1 (mod C_*),
t^2=+1 (mod u_*),
t^4=1  (mod Q_mix),
```

and the exact allocation recovery

```text
C_* = gcd(Q_mix,t^2+1),
u_* = gcd(Q_mix,t^2-1).
```

The root line is

```text
D == t*A (mod Q_mix).
```

At fixed-power scale `gcd(D,A)=B^o(1)`; write

```text
D=h0*D0,
A=h0*A0,
gcd(D0,A0)=1,
h0=B^o(1).
```

Then the complete deterministic mixed-root ledger remains

```text
Q_mix choice           : 1/4
primitive root-line lift: 1/4
remaining completion   : 0
----------------------------
total                  : 1/2.
```

---

## 2. The mixed root recovers the signed first-residual allocation

Because `u_*` is odd and

```text
gcd(t-1,t+1) | 2,
```

the two integers

```text
u_- := gcd(u_*,t-1),
u_+ := gcd(u_*,t+1)
```

are coprime and satisfy

```text
boxed:
u_-*u_+=u_*.
```

Moreover

```text
D-A == 0 (mod u_-),
D+A == 0 (mod u_+).
```

Thus every fixed-power prime power of the first signed residual is assigned by the fourth-root label to exactly one of the two real linear factors.

This is stronger than knowing only `u_res`: the root itself remembers the residual sign allocation.

```text
MIXED_ROOT_RECOVERS_FIRST_RESIDUAL_SIGN_ALLOCATION=true.
```

This statement does not assert that `u_-` and `u_+` equal the raw signed quotients before endpoint/common-factor decorations. It asserts the exact prime-power placement of the peeled first-residual factor; the remaining overlap with the xi-agreement allocation is reconstructed below from the full cofactor.

---

## 3. The same tuple recovers the two complementary xi products

Put

```text
H_+ := D^2+A^2,
H_- := D^2-A^2=(D-A)(D+A).
```

Merged X14/4de give, after the same `B^o(1)` support convention,

```text
oddpart(H_+) = C_* * oddpart(S*T) * B^o(1),
oddpart(H_-) = u_* * oddpart(R*J) * B^o(1).
```

For a fixed mixed tuple and fixed subpolynomial decoration define the peeled complementary cofactors

```text
M_+ := oddpart(H_+)/C_*,
M_- := oddpart(H_-)/u_*.
```

Then

```text
boxed:
M_+ = oddpart(S*T)*B^o(1),
M_- = oddpart(R*J)*B^o(1).
```

The plus/minus cross-coprimality of merged 4de gives

```text
gcd(M_+,M_-)=B^o(1)
```

at fixed-power scale.

Their forced saturation scales are

```text
log_B M_+ = 1/2-chi = 1/2-(2phi-1/4)=3/4-2phi,
log_B M_- = chi+1/4 = 2phi.
```

Equivalently the physical xi-cell split must have

```text
S,T = B^(1/4-chi/2+o(1)),
R,J = B^(1/8+chi/2+o(1))=B^(phi+o(1)).
```

Hence the mixed-root tuple reconstructs the **products** of both xi switch cells and xi agreement cells.

```text
XI_SWITCH_PRODUCT_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
XI_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true.
```

---

## 4. Physical xi-cell splits are divisor-many after the mixed tuple is fixed

The four xi cells `R,S,T,J` are pairwise coprime and squarefree in the merged physical packet.

For fixed `M_+`, an ordered factorization

```text
M_+=S*T
```

with the required dyadic scales, squarefreeness and coprimality is a subset of the divisor factorizations of `M_+`. Therefore

```text
# {(S,T) for fixed M_+} <= tau(M_+)=B^o(1).
```

Likewise

```text
# {(R,J) for fixed M_-} <= tau(M_-)=B^o(1).
```

All endpoint-small support differences introduced in Section 3 have only `B^o(1)` possibilities.

Thus

```text
boxed:
fixed (Q_mix,t,D,A)
=> # {(R,S,T,J)} = B^o(1)
```

provided a physical split exists.

Existence is not automatic. The exact remaining selector includes the requirement that **both** complementary cofactors admit the balanced squarefree two-cell splits above.

```text
DUAL_BALANCED_XI_COFACTOR_SPLIT_REQUIRED=true.
```

---

## 5. Recover the first signed quotient pair from the agreement cofactor

Use the merged s7 signed allocation notation

```text
D+A=a*U,
D-A=b*V,
U*V=oddpart(R*J),
gcd(U,V)=1.
```

For fixed `M_-=oddpart(RJ)*B^o(1)` and fixed endpoint-small decoration, the actual odd agreement product `RJ` has only divisor-many possibilities. Once it is fixed, the agreement allocations are defined by

```text
U = gcd(oddpart(RJ),D+A),
V = gcd(oddpart(RJ),D-A),
```

up to the already-frozen 2-primary convention.

Since `U*V=oddpart(RJ)` and `gcd(U,V)=1`, this reconstructs the primitive agreement pair. Then

```text
a=(D+A)/U,
b=(D-A)/V
```

are forced.

Therefore

```text
boxed:
fixed mixed tuple
=> #(U,V,a,b)=B^o(1).
```

This proves that the first signed residual / xi-agreement split is not an additional polynomial coordinate after the 4de mixed-root compression.

```text
FIRST_SIGNED_QUOTIENT_PAIR_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
FIRST_AGREEMENT_PAIR_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true.
```

---

## 6. First reciprocal equation reconstructs the k-agreement product

Merged s7-27 gives the exact first reciprocal equation

```text
(aU)^2-(bV)^2
 =4*r*s*epsilon_k*p*q.
```

The left side is already fixed by the mixed tuple because

```text
aU=D+A,
bV=D-A,
```

so

```text
(aU)^2-(bV)^2=4DA.
```

For each endpoint-small factorization

```text
D=delta*s,
A=alpha*r,
r,s=B^o(1),
```

the pair `(r,s)` has only divisor-many possibilities, and therefore the odd k-agreement product

```text
p*q=oddpart(alpha*delta)
```

is fixed up to the finite 2-primary decoration.

An ordered coprime split `(p,q)` is divisor-many.

Hence

```text
boxed:
fixed mixed tuple
=> #(p,q)=B^o(1).
```

No second common-core spacing is used.

---

## 7. The second reciprocal completion has no independent fixed-power support

The opposite signed quotients satisfy

```text
Q_xi+P_xi=c*p,
Q_xi-P_xi=d*q,
```

and the common-core root equation

```text
C | p^2 c^2 + q^2 d^2.
```

Merged s7-42 proves throughout `theta=1/4` that the opposite signed quotient product exponent satisfies

```text
nu<=chi,
```

so after the outer data are fixed,

```text
boxed:
#(c,d)=B^o(1).
```

The outer data required by that theorem — `C`, `u_res`, the first signed quotient pair and primitive agreement data — have all been reconstructed in Sections 2–6 from the mixed tuple with `B^o(1)` multiplicity.

Finally merged s7-42/X13 gives

```text
first residual <-> single column = B^o(1) fibers,
post-column reverse reciprocal completion = B^o(1).
```

Therefore

```text
boxed:
fixed (Q_mix,t,D0,A0)
=> full physical signed-reciprocal completion multiplicity = B^o(1).
```

Equivalently,

```text
MIXED_ROOT_TO_SECOND_RECIPROCAL_FIBER_MULTIPLICITY=Bo1
SECOND_RECIPROCAL_INDEPENDENT_FIXED_POWER_SUPPORT=false
XI_SWITCH_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false.
```

This is the main s7-46 theorem.

---

## 8. Forward and reverse finite-fiber equivalence

Every physical square-root packet produces

```text
(Q_mix,t,D0,A0)
```

by merged 4de.

Conversely Sections 2–7 show that a fixed tuple has at most `B^o(1)` physical completions after all legal endpoint / 2-primary decorations are included.

Thus, on the possible square-root saturation family,

```text
boxed:
physical packets
<->
physical-admissible quarter-scale mixed fourth-root tuples
```

has `B^o(1)` fibers in both directions.

```text
MIXED_FOURTH_ROOT_TUPLE_PHYSICAL_PACKET_FINITE_FIBER_EQUIVALENCE=true.
```

The mixed tuple is therefore a canonical charged-once coordinate system for the reactivated s route.

---

## 9. Why there is still no strict sub-square-root saving

For fixed `Q_mix` and root label `t`, primitive determinant spacing gives

```text
#(D0,A0)
 <= B^o(1)*(1+D0*A0/Q_mix)
 <= B^(1/4+o(1)).
```

The number of quarter-scale `Q_mix` is at most

```text
B^(1/4+o(1)),
```

and fourth-root label entropy is `B^o(1)`.

The finite-fiber theorem of Section 8 therefore reproduces

```text
1/4 + 1/4 = 1/2.
```

The reverse quantifier order also gives exactly the same result:

```text
(D0,A0) choice : 1/2,
Q_mix | relevant fourth-root support : divisor-many,
completion : 0.
```

These are alternative descriptions of the same mass and must not be multiplied.

```text
MIXED_ROOT_FORWARD_REVERSE_LEDGER_BOTH_EQUAL_ONE_HALF=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

---

## 10. New exact receiver

After the second reciprocal is removed as an independent support, the remaining issue is no longer a dual reciprocal incidence.

For a primitive quarter-scale mixed-root tuple define

```text
M_+ = oddpart(D^2+A^2)/C_*,
M_- = oddpart(D^2-A^2)/u_*.
```

A physical tuple must satisfy simultaneously:

```text
Q_mix=B^(1/4+o(1)),
t^4=1 mod Q_mix,
D0=t*A0 mod Q_mix,
D0,A0=B^(1/4+o(1)),

C_*=gcd(Q_mix,t^2+1),
u_*=gcd(Q_mix,t^2-1),

M_+=S*T with S,T=B^(1/4-chi/2+o(1)),
M_-=R*J with R,J=B^(1/8+chi/2+o(1)),

R,S,T,J pairwise coprime and squarefree,
all original interval/statewise-reduced/orientation masks,
and the divisor-many reciprocal reconstruction of Sections 5–7.
```

The new minimal s receiver is

```text
SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity.
```

The only possible fixed-power gain must come from proving that simultaneous physical balanced cofactor splits of `M_+` and `M_-` are power-sparse inside the quarter-scale mixed-root family, or from another new exact relation among those split factors.

---

## 11. H / tH decision

No new auxiliary H is requested at s7-46.

Reason: 4de exposed a new exact cofactor pair, and s7-46 has only now isolated the simultaneous balanced xi-cell divisor-split selector. That selector has not yet been exhausted internally. A broad fourth-root / large-sieve / divisor-distribution theorem audit would be premature until the exact balanced split condition and its possible degeneracies are separated.

```text
S7_46_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH44_REOPENED=false
TH24_CROSS_PROMOTED_TO_S7_46=false
T85_CROSS_PROMOTED_TO_S7_46=false.
```

Merged fixed-U `t85/tH24` remains a different coefficient space; no charged-once bridge is proved here.

---

## 12. Route state and next stage

The 4de reactivation has now been consumed successfully. The s route is active again.

```text
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_REACTIVATION_CONSUMED_BY=Stage14-s7-46
S_ROUTE_REACTIVATION_NEEDED=false
S7_47_SCHEDULED=true
```

`Stage14-s7-47` should work only on the dual balanced cofactor split receiver of Section 10. It should test whether

```text
M_+=S*T,
M_-=R*J
```

with both splits balanced, squarefree, pairwise coprime and compatible with the same mixed-root tuple forces a fixed-power divisor-density saving or another exact resultant. Do not reopen the old `C` root-line spacing, row CRT lift, or sH44 theorem audit.

---

## Whole-family boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## Stage boundary

```text
STAGE14_S7_46=COMPLETE_MIXED_FOURTH_ROOT_SIGN_ALLOCATION_COFACTOR_RECONSTRUCTION_AND_SECOND_RECIPROCAL_FINITE_FIBER
MERGED_4DE_REACTIVATION_IMPORTED=true
MERGED_4DD_FULL_RESIDUAL_SATURATION_IMPORTED=true
MERGED_X14_SWITCH_SUPPORT_IMPORTED=true
MERGED_S7_45_CLOSURE_IMPORTED=true
MIXED_ROOT_RECOVERS_FIRST_RESIDUAL_SIGN_ALLOCATION=true
XI_SWITCH_PRODUCT_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
XI_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
DUAL_BALANCED_XI_COFACTOR_SPLIT_REQUIRED=true
FIRST_SIGNED_QUOTIENT_PAIR_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
FIRST_AGREEMENT_PAIR_RECONSTRUCTED_FROM_MIXED_ROOT_TUPLE=true
MIXED_ROOT_TO_SECOND_RECIPROCAL_FIBER_MULTIPLICITY=Bo1
SECOND_RECIPROCAL_INDEPENDENT_FIXED_POWER_SUPPORT=false
XI_SWITCH_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false
MIXED_FOURTH_ROOT_TUPLE_PHYSICAL_PACKET_FINITE_FIBER_EQUIVALENCE=true
MIXED_ROOT_FORWARD_REVERSE_LEDGER_BOTH_EQUAL_ONE_HALF=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
REMAINING_RECEIVER=SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
S7_46_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH44_REOPENED=false
T85_CROSS_PROMOTED_TO_S7_46=false
TH24_CROSS_PROMOTED_TO_S7_46=false
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_REACTIVATION_CONSUMED_BY=Stage14-s7-46
S_ROUTE_REACTIVATION_NEEDED=false
S7_47_SCHEDULED=true
NEXT=Stage14-s7-47
```
