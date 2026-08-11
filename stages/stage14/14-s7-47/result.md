# Stage14-s7-47 — within-side overlap peel and balanced cofactor-split density boundary

## Status

`COMPLETE_WITHINSIDE_OVERLAP_EFFECTIVE_MIXED_ROOT_AND_BALANCED_SPLIT_DENSITY_BOUNDARY`

Stage14-s7-47 consumes merged `Stage14-s7-46` and merged `Stage14-4de` on latest main.

An open parallel draft `Stage14-4df` studies a related within-side overlap. It is **not** used as theorem input here. The overlap theorem below is derived independently in the s-route from the merged s7-46 mixed-root/cofactor identities.

The entering whole-family theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved in this stage. The new contribution is twofold:

1. every fixed-power overlap of a mixed-root base factor with its same-sign complementary xi cofactor enlarges the effective root modulus and gives an equal fixed-power saving;
2. after those overlaps are removed, the mere existence of balanced squarefree two-cell divisor splits is not by itself a fixed-power sparse condition in the ambient cofactor ranges.

Thus the surviving s-receiver is no longer an overlap/gcd problem. It is a simultaneous arithmetic correlation between the pairwise-separated plus/minus cofactors and the mixed-root physical packet.

---

## 1. Imported mixed-root and cofactor packet

Merged s7-46 works on every possible square-root-saturating packet with

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/2-2phi=1/4-chi.
```

After the already-frozen endpoint-small, 2-primary, and unit peels there are odd integers

```text
C_*, u_*, Q_mix=C_*u_*
```

with

```text
gcd(C_*,u_*)=1,
Q_mix=B^(1/4+o(1)),
gcd(Q_mix,D*A)=1,
D,A=B^(1/4+o(1)),
D>A>0.
```

For

```text
t=D*A^(-1) (mod Q_mix),
```

merged 4de/s7-46 give

```text
t^2=-1 (mod C_*),
t^2=+1 (mod u_*),
t^4=1  (mod Q_mix),
D=t*A (mod Q_mix).
```

The root label recovers the factor allocation

```text
C_*=gcd(Q_mix,t^2+1),
u_*=gcd(Q_mix,t^2-1).
```

Put

```text
H_+=D^2+A^2,
H_-=D^2-A^2.
```

Merged s7-46 reconstructs the complementary xi cofactors

```text
M_+ := oddpart(H_+)/C_* = oddpart(S*T)*B^o(1),
M_- := oddpart(H_-)/u_* = oddpart(R*J)*B^o(1).
```

At fixed-power scale

```text
log_B M_+ = 1/2-chi,
log_B M_- = chi+1/4=2phi.
```

A physical completion requires balanced squarefree two-cell splits

```text
M_+=S*T*B^o(1),
S,T=B^(1/4-chi/2+o(1)),

M_-=R*J*B^o(1),
R,J=B^(1/8+chi/2+o(1))=B^(phi+o(1)).
```

For a fixed mixed-root tuple, the number of such ordered divisor splits is `B^o(1)` by merged s7-46.

---

## 2. Define the two same-sign overlaps

The 4de plus/minus cross-coprimality controls factors taken from opposite signs. It does not by itself force the two same-sign factorizations

```text
H_+=C_* M_+,
H_-=u_* M_-
```

to be coprime internally.

Define

```text
W_+ := gcd(C_*,M_+),
W_- := gcd(u_*,M_-).
```

These are genuine physical overlap variables, not new ambient sums. Once `(C_*,u_*)` and the mixed tuple are fixed,

```text
W_+|C_*,
W_-|u_*.
```

Hence their possible values are divisor-many:

```text
#W_+ <= tau(C_*)=B^o(1),
#W_- <= tau(u_*)=B^o(1).
```

Write dyadically

```text
W_+=B^(w_++o(1)),
W_-=B^(w_-+o(1)).
```

No exponent is charged for choosing the overlap after its parent mixed modulus is fixed.

---

## 3. The overlaps enlarge the mixed-root modulus

Because

```text
H_+=C_* M_+
```

and `W_+|M_+`, we have exactly

```text
C_* W_+ | H_+=D^2+A^2.
```

Likewise

```text
u_* W_- | H_-=D^2-A^2.
```

The original unit condition is enough for the larger moduli. Indeed every prime of `W_+` already divides `C_*`, and every prime of `W_-` already divides `u_*`; merged 4de has

```text
gcd(C_*u_*,D*A)=1.
```

Thus `A` is a unit modulo both enlarged factors and

```text
t^2=-1 (mod C_*W_+),
t^2=+1 (mod u_*W_-).
```

After removing only the already-permitted `B^o(1)` cross defects, the two enlarged factors remain coprime. Define

```text
Q_eff := Q_mix * W_+ * W_-.
```

Then

```text
boxed:
t^4=1 (mod Q_eff),

boxed:
D=t*A (mod Q_eff).
```

The effective modulus has fixed-power exponent

```text
log_B Q_eff = 1/4+w_++w_-.
```

This is a fresh modulus enlargement because `W_+W_-` was not included in the 4de/s7-46 root modulus. It is not a second use of `Q_mix`.

```text
WITHINSIDE_OVERLAP_EFFECTIVE_MIXED_ROOT_PROVED=true.
```

---

## 4. Fixed-overlap count

Peel the subpolynomial common gcd of `D,A` as before:

```text
D=h0*D0,
A=h0*A0,
gcd(D0,A0)=1,
h0=B^o(1).
```

On square-root saturation

```text
D0,A0=B^(1/4+o(1)),
D0*A0=B^(1/2+o(1)).
```

For fixed `Q_eff` and one fourth-root label, the primitive root-line spacing lemma gives

```text
#(D0,A0)
 << B^o(1)*(1+D0*A0/Q_eff).
```

Since

```text
D0*A0/Q_eff
 =B^(1/4-w_+-w_-+o(1)),
```

the root-line lift costs at most

```text
B^(max(0,1/4-w_+-w_-)+o(1)).
```

The parent quarter-scale mixed modulus has at most

```text
B^(1/4+o(1))
```

choices; `W_+,W_-` are divisor choices after the parent factors are fixed; fourth-root labels cost `B^o(1)`.

Therefore, uniformly in every fixed-overlap block,

```text
boxed:
E_s7-47(w_+,w_-)
 <= 1/4+max(0,1/4-w_+-w_-).
```

In particular, throughout the only relevant range `w_++w_-<=1/4`,

```text
boxed:
E_s7-47(w_+,w_-)
 <= 1/2-w_+-w_-.
```

If `w_++w_->1/4`, the same formula is even stronger:

```text
E_s7-47<=1/4.
```

Hence every fixed-power same-sign overlap is strictly sub-square-root.

```text
FIXED_POWER_WITHINSIDE_OVERLAP_SAVING_PROVED=true
FIXED_OVERLAP_SAVING=w_++w_-.
```

---

## 5. Consequence for possible square-root saturation

A sequence capable of saturating the merged `1/2` theorem must therefore satisfy

```text
boxed:
W_+=B^o(1),
W_-=B^o(1).
```

Equivalently,

```text
boxed:
gcd(C_*,M_+)=B^o(1),

boxed:
gcd(u_*,M_-)=B^o(1).
```

Merged 4de already gives the opposite-sign cross-coprimalities from

```text
gcd(H_+,H_-)=B^o(1).
```

Consequently any remaining square-root-saturating packet has, at fixed-power scale, the four blocks

```text
C_*, M_+, u_*, M_-
```

pairwise separated:

```text
boxed:
gcd(C_*,M_+)=
gcd(C_*,u_*)=
gcd(C_*,M_-)=
gcd(M_+,u_*)=
gcd(M_+,M_-)=
gcd(u_*,M_-)=B^o(1).
```

This is the clean pairwise-separated mixed-root packet required by all later s work.

```text
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true.
```

---

## 6. Why balanced squarefree split existence alone is not a fixed-power saving

After Section 5, the obvious remaining filters are

```text
M_+=S*T,
M_-=R*J,
```

with each factor pair balanced, squarefree and coprime.

For fixed `M_+` and `M_-`, the split multiplicity is already `B^o(1)`, so there is no multiplicity saving left to obtain by recounting divisor choices.

Could the **existence** of a balanced squarefree split itself force a `B^{-delta}` density loss among ambient cofactors? Not at the level of fixed-power exponent.

For a dyadic factor scale `Y`, choose two primes

```text
p in [Y, (1+eta)Y],
q in [(1+2eta)Y,(1+3eta)Y]
```

for any fixed small `eta>0`. Then

```text
M=pq
```

is squarefree, has a balanced coprime factorization, and different ordered prime pairs give different products after fixing the two disjoint intervals. By the prime number theorem, the number of such products is

```text
Y^(2-o(1)),
```

which has the full fixed-power exponent of the ambient product range `M~Y^2`.

The same construction applies independently at the `R,J` scale. Pairwise coprimality between the two cofactor products can be enforced by choosing disjoint prime intervals/supports without changing the `B` exponent.

This is only an ambient no-go statement; it does not assert that these synthetic products satisfy the full cuboid equations. Its purpose is precise: **balanced squarefree divisor existence, by itself, cannot justify a fixed `B`-power density loss.** Any future saving must use its correlation with the mixed-root quadratic identities and the physical completion.

```text
BALANCED_SQUAREFREE_SPLIT_ALONE_FIXED_POWER_SAVING=false
BALANCED_SPLIT_AMBIENT_FULL_EXPONENT_FAMILY_EXISTS=true.
```

---

## 7. The surviving exact coupled square system

On the pairwise-separated packet, retain the actual physical cell products rather than replacing them by an abstract divisor predicate. Up to the frozen `B^o(1)` decorations,

```text
M_+=S*T,
M_-=R*J.
```

The definitions of `H_+,H_-` give the exact coupled system

```text
boxed:
C_* S T = D^2+A^2,

boxed:
u_* R J = D^2-A^2,
```

again in the odd/fixed-power normalization used throughout 4de/s7-46.

Equivalently,

```text
boxed:
C_* S T + u_* R J = 2D^2,

boxed:
C_* S T - u_* R J = 2A^2.
```

The two square conditions share the same four pairwise-separated norm blocks and the same mixed-root allocation. Counting the two balanced factorizations independently would forget this coupling and is not permitted.

This exact two-square bilinear system is the correct next s object.

```text
DUAL_BALANCED_COFACTOR_COUPLED_SQUARE_SYSTEM_PROVED=true.
```

---

## 8. New receiver

The s7-46 receiver

```text
SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
```

is narrowed to

```text
boxed:
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorCorrelationPhysicalDensity.
```

Mandatory structure:

```text
Q_mix=C_*u_*=B^(1/4+o(1)),
t^2=-1 on C_*,
t^2=+1 on u_*,
D=t*A mod Q_mix,
D,A=B^(1/4+o(1)),

M_+=S*T,
M_-=R*J,
C_* S T = D^2+A^2,
u_* R J = D^2-A^2,

C_*,M_+,u_*,M_- pairwise coprime at fixed-power scale,
S,T balanced squarefree,
R,J balanced squarefree,
all reciprocal/orientation/reconstruction masks retained.
```

The next deterministic task is to keep both square equations simultaneously and test whether a bilinear/resultant or divisor-switch relation survives after the pairwise separation. A theorem about generic balanced divisors alone is not enough.

---

## 9. Relation to open Stage14-4df

During this stage, open Draft PR `#610` (`Stage14-4df`) independently exposed the same type of within-side overlap in mainline coordinates.

Because `#610` is not merged at this stage snapshot, it is not imported as a theorem source:

```text
OPEN_4DF_USED_AS_THEOREM_INPUT=false.
```

The s7-47 overlap proof above follows only from merged s7-46/4de identities. If 4df later merges, its result is compatible with this s-route theorem and should be treated as an independent/convergent derivation, not a second saving to multiply.

```text
S7_47_AND_OPEN_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false.
```

---

## 10. H / tH decision

No new auxiliary H/tH request is needed at s7-47.

Reason: the pairwise-separated packet still has an unexhausted **exact two-square bilinear system**

```text
C_*ST +/- u_*RJ = 2*(square),
```

and this should be reduced internally before asking for an external sieve/incidence theorem. The ambient balanced-divisor no-go does not show that the coupled physical system lacks an elementary resultant or divisor switch.

```text
S7_47_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH44_REOPENED=false
TH24_CROSS_PROMOTED_TO_S7_47=false.
```

---

## 11. Whole-family theorem and next stage

The current canonical theorem remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

But any square-root equality sequence is now forced into the pairwise-separated four-block packet of Section 5.

Next:

```text
Stage14-s7-48
```

It should work only with

```text
C_* S T + u_* R J = 2D^2,
C_* S T - u_* R J = 2A^2
```

and the mixed-root congruence, and test for a fresh bilinear/resultant/divisor-switch constraint. It must not reopen old common-core spacing, second reciprocal support, or split multiplicity.

---

## Stage boundary

```text
STAGE14_S7_47=COMPLETE_WITHINSIDE_OVERLAP_EFFECTIVE_MIXED_ROOT_AND_BALANCED_SPLIT_DENSITY_BOUNDARY
MERGED_S7_46_IMPORTED=true
MERGED_4DE_IMPORTED=true
OPEN_4DF_USED_AS_THEOREM_INPUT=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
WITHINSIDE_PLUS_OVERLAP=W_plus=gcd(C_*,M_+)
WITHINSIDE_MINUS_OVERLAP=W_minus=gcd(u_*,M_-)
EFFECTIVE_MIXED_ROOT_MODULUS=Q_mix*W_plus*W_minus
WITHINSIDE_OVERLAP_EFFECTIVE_MIXED_ROOT_PROVED=true
FIXED_OVERLAP_BLOCK_EXPONENT=1/2-w_plus-w_minus
FIXED_POWER_WITHINSIDE_OVERLAP_SAVING_PROVED=true
SQRT_SATURATION_REQUIRES_W_PLUS_BO1=true
SQRT_SATURATION_REQUIRES_W_MINUS_BO1=true
SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true
BALANCED_XI_CELL_SPLIT_MULTIPLICITY_GIVEN_COFACTORS=Bo1
BALANCED_SQUAREFREE_SPLIT_ALONE_FIXED_POWER_SAVING=false
BALANCED_SPLIT_AMBIENT_FULL_EXPONENT_FAMILY_EXISTS=true
DUAL_BALANCED_COFACTOR_COUPLED_SQUARE_SYSTEM_PROVED=true
REMAINING_RECEIVER=SquareRootQuarterScalePairwiseSeparatedMixedFourthRootDualBalancedXiCofactorCorrelationPhysicalDensity
S7_47_AND_OPEN_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false
S7_47_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH44_REOPENED=false
TH24_CROSS_PROMOTED_TO_S7_47=false
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_NEXT=Stage14-s7-48
NEXT=Stage14-s7-48
```
