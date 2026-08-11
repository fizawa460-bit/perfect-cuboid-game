# Stage14-s7-48 — Gaussian norm / rotated coordinate-product finite-fiber reduction and resultant boundary

## Status

`COMPLETE_GAUSSIAN_NORM_ROTATED_COORDINATE_PRODUCT_FINITE_FIBER_AND_RESULTANT_NO_GO`

Stage14-s7-48 consumes merged `Stage14-s7-47` on the current square-root saturation packet.

The entering theorem is

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The purpose of this stage is to exhaust the exact two-square system left by s7-47 before emitting a new auxiliary theorem audit.

---

## 1. Imported pairwise-separated packet

Write the fixed-power normalization of the s7-47 packet as

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
A_phi=1/4-chi=1/2-2phi,
```

with

```text
C_*=B^(chi+o(1)),
u_*=B^(1/4-chi+o(1)),
S,T=B^(1/4-chi/2+o(1)),
R,J=B^(phi+o(1)).
```

The complementary products have scales

```text
S*T=B^(1/2-chi+o(1)),
R*J=B^(chi+1/4+o(1)).
```

All endpoint-small, 2-primary and harmless gcd decorations have `B^o(1)` possibilities.  Freeze one such decoration.  There are positive `B^o(1)` factors `epsilon_+`, `epsilon_-` for which the exact integer equations are

```text
epsilon_+ C_* S T = D^2+A^2,
epsilon_- u_* R J = D^2-A^2,                    (1.1)
```

with

```text
D>A>0,
D,A=B^(1/4+o(1)).
```

Merged s7-47 also forces, at fixed-power scale,

```text
C_*, S*T, u_*, R*J
```

to be pairwise separated.  In particular the same-side overlap savings have already been spent and must not be charged again.

---

## 2. One Gaussian integer contains the whole plus-side square equation

Set

```text
Z := D+iA.
```

Then the first equation in (1.1) is exactly

```text
N(Z)=D^2+A^2=epsilon_+ C_* S T.                 (2.1)
```

The second equation becomes a coordinate-product identity after the fixed Gaussian rotation

```text
(1+i) conjugate(Z)
  = (D+A)+i(D-A).                                (2.2)
```

Hence

```text
Re((1+i)conjugate Z) * Im((1+i)conjugate Z)
 = (D+A)(D-A)
 = D^2-A^2
 = epsilon_- u_* R J.                           (2.3)
```

Thus the entire s7-47 two-square receiver is equivalently one Gaussian norm together with the product of the two coordinates after a fixed 45-degree Gaussian rotation.

```text
GAUSSIAN_NORM_ROTATED_COORDINATE_PRODUCT_REDUCTION_PROVED=true
GAUSSIAN_STATE=Z=D+iA
GAUSSIAN_NORM_SUPPORT=epsilon_plus*C_star*S*T
ROTATED_COORDINATES=(D+A,D-A)
ROTATED_COORDINATE_PRODUCT_SUPPORT=epsilon_minus*u_star*R*J
```

No extra curve or second independent quadratic equation is created by retaining (1.1): both equations are the norm/coordinate-product projections of the same `Z`.

---

## 3. Fixed plus triple has only `B^o(1)` physical completions

Fix

```text
(C_*,S,T)
```

and the frozen `epsilon_+`.  Then

```text
N_+ := epsilon_+ C_* S T
```

is fixed.  The number of integral representations

```text
D^2+A^2=N_+
```

is bounded by

```text
r_2(N_+) <= 4*tau(N_+) = B^o(1).                (3.1)
```

For each such `(D,A)`, the integer

```text
N_- := D^2-A^2
```

is fixed.  The admissible ordered triples `(u_*,R,J)` are a subset of the ordered divisor factorizations of `N_-/epsilon_-`, so

```text
# {(u_*,R,J) for fixed (D,A)}
 <= tau_3(N_-)=B^o(1).                           (3.2)
```

The squarefree, balanced, pairwise-coprime, orientation and reciprocal masks only reduce this set.  Merged s7-46 then reconstructs the remaining reciprocal/post-column packet with `B^o(1)` multiplicity.

Therefore

```text
boxed:
fixed (C_*,S,T)
=> # full physical packets = B^o(1).             (3.3)
```

The ambient plus-side triple count has exponent

```text
chi + (1/4-chi/2) + (1/4-chi/2) = 1/2.          (3.4)
```

So the plus-side Gaussian norm coordinates give one complete charged-once `1/2` count.

```text
PLUS_TRIPLE_TO_PHYSICAL_PACKET_FIBER_MULTIPLICITY=Bo1
PLUS_COMPLETE_COUNT_EXPONENT=1/2
```

---

## 4. Fixed minus triple also has only `B^o(1)` physical completions

Conversely fix

```text
(u_*,R,J)
```

and `epsilon_-`.  Then

```text
N_- := epsilon_- u_* R J=(D-A)(D+A)
```

is fixed.  Every positive solution with `D>A>0` and the correct parity comes from a divisor pair

```text
L_- L_+ = N_-,
L_-=D-A,
L_+=D+A.
```

Hence

```text
# {(D,A)} <= tau(N_-)=B^o(1).                    (4.1)
```

For each such pair,

```text
N_+ := D^2+A^2
```

is fixed, and admissible `(C_*,S,T)` are a subset of the ordered three-factor divisor splittings of `N_+/epsilon_+`, again `B^o(1)`.

Thus

```text
boxed:
fixed (u_*,R,J)
=> # full physical packets = B^o(1).             (4.2)
```

The ambient minus-side triple exponent is

```text
(1/4-chi) + phi + phi
 = 1/4-chi + (chi+1/4)
 = 1/2.                                           (4.3)
```

Therefore the minus-side real factor coordinates are a second complete charged-once `1/2` count.

```text
MINUS_TRIPLE_TO_PHYSICAL_PACKET_FIBER_MULTIPLICITY=Bo1
MINUS_COMPLETE_COUNT_EXPONENT=1/2
```

The plus and minus complete counts are alternative coordinate systems for the same physical mass.  They cannot be multiplied as independent savings.

---

## 5. The two-square system has no fresh algebraic eliminant among the six norm blocks

For the eliminant question, absorb the frozen `epsilon_+`, `epsilon_-` into

```text
X := epsilon_+ C_* S T,
Y := epsilon_- u_* R J.
```

The two equations are simply

```text
X=D^2+A^2,
Y=D^2-A^2.                                        (5.1)
```

Equivalently

```text
D^2=(X+Y)/2,
A^2=(X-Y)/2.                                      (5.2)
```

Over an algebraic closure, `D` and `A` may be chosen as square roots of the two right-hand sides for generic `(X,Y)`.  Algebraically, the homomorphism

```text
Q[X,Y] -> Q[D,A],
X |-> D^2+A^2,
Y |-> D^2-A^2
```

is injective because the inverse linear relations (5.2) identify `D^2,A^2` with independent linear combinations of `X,Y`.

Hence

```text
< X-D^2-A^2, Y-D^2+A^2 > cap Q[X,Y] = {0}.       (5.3)
```

So eliminating `D,A` produces **no nonzero polynomial relation** among `X,Y`, and therefore no fresh polynomial resultant among

```text
C_*,S,T,u_*,R,J
```

from the two-square equations alone.

This is the precise reason a second deterministic resultant cannot beat `1/2` here.

```text
TWO_SQUARE_ELIMINATION_IDEAL_TRIVIAL=true
FRESH_ALGEBRAIC_RESULTANT_AMONG_SIX_NORM_BLOCKS=false
SECOND_DETERMINANT_OR_RESULTANT_MODULUS_AVAILABLE=false
```

This statement concerns algebraic elimination only.  The requirement that `(X+Y)/2` and `(X-Y)/2` be **integer squares with the physical factor masks** is an arithmetic condition and remains the live obstruction.

---

## 6. Why a second divisor switch also reproduces exactly `1/2`

The plus-side switch gives

```text
(C_*,S,T) -> N(Z) -> Z -> rotated coordinate product -> (u_*,R,J)
```

with only `B^o(1)` fibers, but the source triple already has exponent `1/2`.

The reverse switch gives

```text
(u_*,R,J) -> (D-A,D+A) -> Z -> N(Z) -> (C_*,S,T)
```

with only `B^o(1)` fibers, and its source triple also has exponent `1/2`.

Thus

```text
PLUS_TO_MINUS_DIVISOR_SWITCH_FIBER=Bo1
MINUS_TO_PLUS_GAUSSIAN_SWITCH_FIBER=Bo1
SECOND_DIVISOR_SWITCH_FIXED_POWER_SAVING=false
```

This is analogous to the earlier charged-once warnings: finite-fiber equivalence proves that two ledgers count the same mass; it does not provide a second saving.

---

## 7. Minimal surviving arithmetic obstruction

After all s-owned exact reductions, possible square-root saturation is equivalent, up to `B^o(1)` fibers and frozen endpoint decorations, to the following arithmetic problem.

Count pairwise-separated balanced triples

```text
(C_*,S,T)
```

of total exponent `1/2` for which at least one primitive Gaussian representation

```text
Z=D+iA,
N(Z)=epsilon_+ C_*ST,
D,A=B^(1/4+o(1))
```

has rotated coordinate product

```text
(D+A)(D-A)=epsilon_- u_*RJ
```

admitting a physical balanced squarefree factorization

```text
u_*=B^(1/4-chi+o(1)),
R,J=B^(phi+o(1)),
```

with all pairwise-separation, reciprocal, orientation and reconstruction masks retained.

Equivalently, start from `(u_*,R,J)` and demand that the reconstructed `(D,A)` have Gaussian norm admitting the balanced `(C_*,S,T)` split.

The required strict improvement is a uniform fixed `delta>0` such that

```text
# physical admissible packets
 << B^(1/2-delta+o(1))                              (7.1)
```

throughout

```text
1/6<=chi<=1/4.
```

This is no longer a gcd, CRT, root-line, finite-fiber, elementary divisor-count, or algebraic resultant problem.  It is a simultaneous arithmetic distribution problem for a Gaussian norm and the product of the rotated coordinates of the same Gaussian integer.

```text
BALANCED_SPLIT_CORRELATION_IS_ARITHMETIC_NOT_ALGEBRAIC=true
EXACT_S_ROUTE_ALGEBRA_EXHAUSTED_AT_THIS_RECEIVER=true
```

New receiver:

```text
SquareRootQuarterScalePairwiseSeparatedGaussianNormRotatedCoordinateProductDualBalancedCellFactorizationDensity
```

---

## 8. Auxiliary H decision

This receiver is materially different from the frozen `sH44` dual-root-line object.  `sH44` must not be reopened.

All obvious exact s-route reductions are now exhausted, and a theorem/applicability audit can change the next decision.  Therefore a new immutable H request is warranted.

```text
S7_48_NEW_AUXILIARY_H_NEEDED=true
S7_48_AUXILIARY_H_STAGE=Stage14-sH48
S7_48_H_REQUESTED_OBJECT=SquareRootQuarterScalePairwiseSeparatedGaussianNormRotatedCoordinateProductDualBalancedCellFactorizationPowerSaving
S_ROUTE_BLOCKED_WAITING_FOR_H=true
SH44_REOPENED=false
```

The durable target is

```text
stages/stage14/14-s7-48/sh48-target.md
```

and is governed by `stages/stage14/H-PROTOCOL.md`.

---

## 9. Whole-family theorem and boundary

No new global exponent is claimed in s7-48:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

Boundary:

```text
STAGE14_S7_48=COMPLETE_GAUSSIAN_NORM_ROTATED_COORDINATE_PRODUCT_FINITE_FIBER_AND_RESULTANT_NO_GO
MERGED_S7_47_IMPORTED=true
PAIRWISE_SEPARATED_FOUR_BLOCK_PACKET_IMPORTED=true
GAUSSIAN_NORM_ROTATED_COORDINATE_PRODUCT_REDUCTION_PROVED=true
PLUS_TRIPLE_TO_PHYSICAL_PACKET_FIBER_MULTIPLICITY=Bo1
MINUS_TRIPLE_TO_PHYSICAL_PACKET_FIBER_MULTIPLICITY=Bo1
PLUS_COMPLETE_COUNT_EXPONENT=1/2
MINUS_COMPLETE_COUNT_EXPONENT=1/2
TWO_SQUARE_ELIMINATION_IDEAL_TRIVIAL=true
FRESH_ALGEBRAIC_RESULTANT_AMONG_SIX_NORM_BLOCKS=false
SECOND_DIVISOR_SWITCH_FIXED_POWER_SAVING=false
BALANCED_SPLIT_CORRELATION_IS_ARITHMETIC_NOT_ALGEBRAIC=true
EXACT_S_ROUTE_ALGEBRA_EXHAUSTED_AT_THIS_RECEIVER=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_48_NEW_AUXILIARY_H_NEEDED=true
S7_48_AUXILIARY_H_STAGE=Stage14-sH48
S_ROUTE_BLOCKED_WAITING_FOR_H=true
SH44_REOPENED=false
NEXT=Stage14-s7-49_after_sH48
```
