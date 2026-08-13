# Stage14-s7-24 — Plucker elimination of rank two and primitive root-line saturation

## Status

`COMPLETE_RANK_TWO_PLUCKER_ELIMINATION_AND_PRIMITIVE_ROOT_LINE_SATURATION`

Merged Stage14-s7-23 proves that the `xi`-side endpoint short span cannot have rank three.  Stage14-s7-24 now treats the only remaining apparent higher-rank case, namely rank two.

The result is stronger than the planned generic Plucker encoding:

```text
there are no physical rank-two endpoint packets.
```

Indeed the four `xi` CRT congruences force four Plucker coordinates of any two short lattice vectors to be divisible by the four balanced cell squares.  The endpoint Plucker coordinates are only of size `B^(1/8+o(1))`, while every cell square is at least `B^(1/4-o(1))`; hence all four coordinates vanish.  The Plucker relation then forces the rank-two plane to be one of two coordinate planes, contradicting the positivity of the physical root vector.

Consequently every surviving physical endpoint packet has

```text
xi short-span rank exactly one.
```

The actual physical root vector is primitive, so the surviving rational line has integral lattice

```text
Lambda_xi cap Q*X = Z*X.
```

Quotienting by this primitive line preserves the entire finite CRT quotient.  Therefore the rank-one `xi` line has full saturation order `xi^2` and dual defect exactly one.  This is the `xi` analogue of the full `k`-side saturation proved in merged Stage14-4ci.

No whole-family fixed-power saving is claimed yet.  The remaining obstruction is no longer a short-vector-rank problem; it is the multiplicity of balanced eight-cell packets above a fixed common-core residual triple and primitive physical root direction.

The current unconditional exponent remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported exact packet

Keep one balanced endpoint orientation packet `Pi` and the exact lattice

```text
Lambda_xi(Pi) subset Z^4
```

on coordinates

```text
X=(x_1,y_1,x_2,y_2).
```

Merged s7-21 gives the four homogeneous CRT congruences

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2),
x_2 == lambda_S*y_1 (mod S^2),
y_2 == lambda_T*x_1 (mod T^2),                      (1.1)
```

where

```text
R,S,T,J
```

are pairwise-coprime squarefree cells with

```text
R*S*T*J=xi,
R,S,T,J >= B^(1/8-o(1)),
R,S,T,J <= B^(1/4+o(1)).                            (1.2)
```

The endpoint root scale is

```text
L=B^(1/16+o(1)),
|x_i|,|y_i|<=L.                                     (1.3)
```

Merged s7-23 proves

```text
rank span_Q(Lambda_xi cap [-CL,CL]^4) <= 2          (1.4)
```

for every fixed `C`, because the rank-three physical branch is empty.

The actual physical root vector `X` belongs to the short set, so the short span is nonzero.

---

## 2. Assume rank two and define Plucker coordinates

Assume for contradiction that the endpoint short span has rank two.  Choose two independent short vectors

```text
w=(w_1,w_2,w_3,w_4),
w'=(w'_1,w'_2,w'_3,w'_4)
```

in

```text
Lambda_xi cap [-CL,CL]^4.
```

Define the six Plucker coordinates

```text
p_ij = w_i*w'_j-w_j*w'_i,
1<=i<j<=4.                                          (2.1)
```

Since both vectors have sup norm `O(L)`,

```text
boxed:
|p_ij| << L^2 = B^(1/8+o(1)).                       (2.2)
```

The decomposable two-vector `w wedge w'` is nonzero and satisfies the exact Plucker relation

```text
boxed:
p_12*p_34-p_13*p_24+p_14*p_23=0.                   (2.3)
```

No geometry-of-numbers estimate is used in the next step; only the four exact CRT rows are used.

---

## 3. Each xi cell square divides one cross Plucker coordinate

Apply the same congruence in (1.1) to `w` and `w'`.

### 3.1 R row

From

```text
w_2  == lambda_R*w_4  (mod R^2),
w'_2 == lambda_R*w'_4 (mod R^2),
```

we obtain

```text
p_24=w_2*w'_4-w_4*w'_2 ==0 (mod R^2).
```

Hence

```text
boxed:
R^2 | p_24.                                          (3.1)
```

### 3.2 J row

Similarly

```text
boxed:
J^2 | p_13.                                          (3.2)
```

### 3.3 S row

From `x_2 == lambda_S*y_1 (mod S^2)` for both vectors,

```text
boxed:
S^2 | p_23.                                          (3.3)
```

up to the irrelevant sign convention for `p_23`.

### 3.4 T row

From `y_2 == lambda_T*x_1 (mod T^2)` for both vectors,

```text
boxed:
T^2 | p_14.                                          (3.4)
```

Thus the four balanced cells control four different cross minors:

```text
J^2 | p_13,
T^2 | p_14,
S^2 | p_23,
R^2 | p_24.                                         (3.5)
```

---

## 4. Endpoint scale forces the four cross minors to vanish

By (1.2), every cell square satisfies

```text
C_cell^2 >= B^(1/4-o(1)).                            (4.1)
```

while by (2.2),

```text
|p_ij| <= B^(1/8+o(1)).                              (4.2)
```

The exponent gap is

```text
1/4-1/8=1/8.                                         (4.3)
```

Therefore a nonzero integer `p_ij` cannot be divisible by its corresponding cell square for sufficiently large endpoint parameter `B`.  Consequently

```text
boxed:
p_13=p_14=p_23=p_24=0.                              (4.4)
```

This is a uniform endpoint statement; all dyadic `B^o(1)` widths are swallowed by the fixed exponent gap `1/8`.

---

## 5. Plucker relation leaves only coordinate planes

Substitute (4.4) into (2.3):

```text
p_12*p_34=0.                                         (5.1)
```

Because `w,w'` are independent, not all six Plucker coordinates vanish.  Hence exactly one of the following holds:

```text
CASE A:
  p_12 !=0,
  p_34=0;

CASE B:
  p_34 !=0,
  p_12=0.                                            (5.2)
```

In Case A, the first two coordinate columns of the `2 x 4` matrix with rows `w,w'` are independent.  Since

```text
p_13=p_23=0,
p_14=p_24=0,
```

the third and fourth coordinate columns are both zero.  Thus the rank-two plane is

```text
span_Q(e_1,e_2).                                     (5.3)
```

Every vector in it has

```text
x_2=y_2=0.
```

In Case B the same argument gives

```text
span_Q(e_3,e_4),                                     (5.4)
```

so every vector in the plane has

```text
x_1=y_1=0.
```

But the physical root vector satisfies

```text
x_1,y_1,x_2,y_2>0.                                   (5.5)
```

It cannot lie in either coordinate plane.

Therefore

```text
boxed:
RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false.         (5.6)
```

Together with merged s7-23,

```text
rank three = impossible,
rank two   = impossible.                             (5.7)
```

---

## 6. The surviving xi short span has rank exactly one

The actual physical root vector `X` belongs to `Lambda_xi` and has endpoint size `O(L)`.  Hence the short span has rank at least one.

Sections 4--5 and merged s7-23 give rank at most one.  Therefore

```text
boxed:
rank span_Q(Lambda_xi cap [-CL,CL]^4)=1             (6.1)
```

for every surviving physical endpoint packet.

Thus the complete short-vector geometry has collapsed to one rational line.

This is an exact structural reduction, not an average estimate.

---

## 7. The physical root vector is primitive

For state one,

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
```

and the reduced physical packet has

```text
gcd(P_1,Q_1)=1.
```

Therefore

```text
gcd(x_1,y_1)=1.                                     (7.1)
```

In particular

```text
gcd(x_1,y_1,x_2,y_2)=1.                             (7.2)
```

So the physical root vector

```text
X=(x_1,y_1,x_2,y_2)
```

is a primitive integer vector.

Every integer point on its rational line is consequently an integer multiple of `X`:

```text
boxed:
Z^4 cap Q*X = Z*X.                                   (7.3)
```

Since `X in Lambda_xi`,

```text
boxed:
Lambda_xi cap Q*X = Z*X.                             (7.4)
```

The surviving short direction is therefore the primitive physical root line itself.

---

## 8. Full xi-side quotient saturation on the primitive root line

Let

```text
pi_X: Z^4 -> Z^4/Z*X ~= Z^3                         (8.1)
```

be the quotient map.  Put

```text
M_X=pi_X(Lambda_xi).
```

Because `Z*X subset Lambda_xi`, the induced map gives an exact isomorphism

```text
boxed:
Z^4/Lambda_xi
 ~= (Z^4/Z*X)/M_X.                                   (8.2)
```

Merged s7-21 gives

```text
[Z^4:Lambda_xi]=xi^2.                               (8.3)
```

Hence

```text
boxed:
[Z^3:M_X]=xi^2.                                     (8.4)
```

Define the primitive-root-line quotient saturation order by

```text
d_X=[Z^3:M_X].                                      (8.5)
```

Then

```text
boxed:
d_X=xi^2,                                           (8.6)
```

and the corresponding defect

```text
E_X=xi^2/d_X
```

satisfies

```text
boxed:
E_X=1.                                               (8.7)
```

Thus there is no residual `xi` dual defect on the surviving physical line.

This is the exact codimension-three analogue of merged 4ci's `k`-side statement

```text
K_DUAL_SATURATION_ORDER=k^2,
K_DUAL_DEFECT=1.
```

---

## 9. Every xi cell survives with its full cyclic order

The exact CRT quotient from s7-21 is

```text
Z^4/Lambda_xi
 ~= Z/R^2 Z
  x Z/J^2 Z
  x Z/S^2 Z
  x Z/T^2 Z.                                        (9.1)
```

By (8.2), quotienting the ambient lattice by the primitive physical line loses none of this finite quotient.  Hence all four cell components retain their maximal orders:

```text
boxed:
root-line quotient component orders
 = R^2,J^2,S^2,T^2.                                 (9.2)
```

Equivalently, once the primitive physical root direction is fixed, every legal primewise `xi` orientation is tested on the full cell-square modulus; there is no smaller defect modulus left to average over.

This does **not** imply that the cell sizes themselves are determined by `X`.  The moving moduli `R,S,T,J` remain the central multiplicity variable.

---

## 10. Legal merge with X1 and 4ci

Merged Stage14-X1 proves the charge-preserving adapter

```text
fixed eight cells + fixed (C,u_res,v_res)
=> B^o(1) decorated physical joint packets.         (10.1)
```

Merged Stage14-4ci adds, on the same physical packet,

```text
k-side primitive z line has defect 1,
t^2 | q_k=C*u_res,
h^2 | q_xi=C*v_res,                                  (10.2)
```

and the exact normalized four-host system.

Stage14-s7-24 may therefore retain simultaneously, with only `B^o(1)` charging,

```text
- residual triple (C,u_res,v_res),
- all eight balanced cells,
- primitive physical root line X,
- full k primitive z-line quotient,
- full xi primitive root-line quotient,
- all physical masks.                               (10.3)
```

No hypothetical gain from these descriptions is multiplied independently.  They are exact refinements of the same physical pair.

---

## 11. The true remaining fiber

For a fixed residual triple define

```text
m_{C,u,v}(X)
 := # {
      legal balanced eight-cell/orientation packets
      with primitive physical root direction X
      and residual triple (C,u,v)
    }.                                               (11.1)
```

X1 converts physical collision mass to this charged-once packet count:

```text
physical endpoint collision mass
 <= B^o(1)
    * sum_{C,u,v}
      sum_{primitive positive X}
        m_{C,u,v}(X).                                (11.2)
```

The new minimal receiver is

```text
PrimitiveRootDirectionCommonCoreCellMultiplicity.   (11.3)
```

A sufficient theorem is

```text
boxed target:
sum_{C,u,v}
 sum_X m_{C,u,v}(X)
 << B^(7/8-delta+o(1))                              (11.4)
```

for some fixed `delta>0`.

A stronger pointwise theorem

```text
m_{C,u,v}(X) <= B^o(1)                              (11.5)
```

would reduce the count to the residual support times the raw primitive-root-direction support.  Stage14-s7-24 does not claim (11.5).

---

## 12. Dyadic endpoint budget and the unique saturation corner

Merged 4ci records the dyadic residual-triple support exponent

```text
sigma_res(theta,phi)
 = 2*(theta+phi)-1/2,                                (12.1)
```

where

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4.                               (12.2)
```

The primitive root vector has four coordinates of scale at most `B^(1/16+o(1))`, so the raw number of possible positive primitive directions is at most

```text
B^(4/16+o(1))=B^(1/4+o(1)).                         (12.3)
```

Therefore, **if** the remaining fixed-`(C,u,v,X)` cell fiber (11.5) is `B^o(1)`, the dyadic packet exponent would be

```text
sigma_res(theta,phi)+1/4
 = 2*(theta+phi)-1/4.                                (12.4)
```

Its maximum over (12.2) is

```text
2*(5/16+1/4)-1/4
 =7/8.                                               (12.5)
```

The maximum occurs only at the extreme corner

```text
boxed:
theta=5/16,
phi=1/4.                                             (12.6)
```

Thus a pointwise `B^o(1)` root-direction cell-fiber theorem would automatically power-save every dyadic block with

```text
theta+phi <= 9/16-epsilon,                           (12.7)
```

by a margin `2 epsilon`.

At the unique saturation corner the cell scales are

```text
alpha,delta ~ B^(5/16),
beta,gamma  ~ B^(3/16),
R,J         ~ B^(1/4),
S,T         ~ B^(1/8).                               (12.8)
```

This corner is therefore the sharp place where the next cell-multiplicity argument must be strongest.

No off-corner saving is promoted in s7-24 because (11.5) remains unproved.

---

## 13. Why rank geometry is now exhausted

The sequence s7-21 through s7-24 has exhausted the short-rank alternatives:

```text
rank 4: impossible by det Lambda_xi versus root box,
rank 3: impossible by cellwise dual-support saturation (s7-23),
rank 2: impossible by cell-square Plucker divisibility (s7-24),
rank 1: the only physical endpoint branch.           (13.1)
```

On rank one,

```text
primitive physical line quotient defect = 1.        (13.2)
```

There is no further rank drop available because the physical root vector itself is nonzero.

Accordingly the next stage should not repeat geometry-of-numbers rank arguments.  It must count moving cell moduli over a fixed primitive root direction and residual shell.

---

## 14. Relation to external analytic machinery

No auxiliary large sieve, Gaussian dispersion theorem, or tH result is required for s7-24.

The proof uses only

```text
- merged exact xi CRT congruences,
- balanced endpoint cell lower bounds,
- the elementary Plucker relation,
- reducedness/positivity of the physical roots,
- finite abelian quotient exactness,
- merged X1/4ci charge-preserving adapters.          (14.1)
```

Therefore

```text
TH16_NEEDED_BY_S7_24=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false.                (14.2)
```

A future H/tH line would be justified only if the next cell-modulus multiplicity receiver is reduced to a genuine external analytic estimate with fully matched coefficient space.

---

## 15. Next stage

Stage14-s7-25 should attack

```text
PrimitiveRootDirectionCommonCoreCellMultiplicity
```

directly.

The preferred order is

```text
fixed residual triple (C,u_res,v_res)
-> divisor-bounded common scales t,h from 4ci
-> fixed primitive root vector X
-> full-order k and xi line quotients
-> use the normalized four-host equations
-> count admissible balanced cell packets
   (R,S,T,J;alpha,beta,gamma,delta).                 (15.1)
```

The first target is

```text
m_{C,u,v}(X) <= B^o(1)                              (15.2)
```

outside the extreme corner, or any uniform fixed-power substitute.  At the corner `(theta,phi)=(5/16,1/4)`, the large cells `R,J,alpha,delta` and small cells `S,T,beta,gamma` should be separated explicitly before any analytic averaging.

---

## Stage boundary

```text
STAGE14_S7_24=COMPLETE_RANK_TWO_PLUCKER_ELIMINATION_AND_PRIMITIVE_ROOT_LINE_SATURATION
MERGED_S7_23_IMPORTED=true
MERGED_X1_IMPORTED=true
MERGED_4CI_IMPORTED=true
XI_SHORT_RANK_THREE_PHYSICAL_PACKETS_EXIST=false
XI_RANK2_PLUCKER_COORDINATES_DEFINED=true
XI_RANK2_J2_DIVIDES_P13=true
XI_RANK2_T2_DIVIDES_P14=true
XI_RANK2_S2_DIVIDES_P23=true
XI_RANK2_R2_DIVIDES_P24=true
XI_RANK2_PLUCKER_COORDINATE_UPPER_EXPONENT=1/8
XI_CELL_SQUARE_LOWER_EXPONENT=1/4
XI_RANK2_FOUR_CROSS_PLUCKER_COORDINATES_ZERO=true
XI_RANK2_PLUCKER_RELATION_FORCES_COORDINATE_PLANE=true
XI_RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false
XI_PHYSICAL_ENDPOINT_SHORT_RANK_EXACT=1
PHYSICAL_ROOT_VECTOR_PRIMITIVE=true
XI_PRIMITIVE_ROOT_LINE_INTERSECTION=Z*X
XI_ROOT_LINE_QUOTIENT_SATURATION_ORDER=xi^2
XI_ROOT_LINE_DUAL_DEFECT=1
XI_ROOT_LINE_ALL_CELL_COMPONENTS_FULL_ORDER=true
X1_JOINT_CHARGE_ADAPTER_IMPORTED=true
FOUR_CI_K_FULL_SATURATION_IMPORTED=true
FOUR_CI_COMMON_SCALE_SQUARE_DIVISIBILITY_IMPORTED=true
PRIMITIVE_ROOT_DIRECTION_COMMON_CORE_CELL_MULTIPLICITY_REQUIRED=true
PRIMITIVE_ROOT_DIRECTION_COMMON_CORE_CELL_MULTIPLICITY_PROVED=false
DYADIC_RESIDUAL_SUPPORT_EXPONENT=2*(theta+phi)-1/2
RAW_PRIMITIVE_ROOT_DIRECTION_SUPPORT_EXPONENT=1/4
CONDITIONAL_BO1_FIBER_DYADIC_EXPONENT=2*(theta+phi)-1/4
UNIQUE_CONDITIONAL_7_8_SATURATION_CORNER=(theta,phi)=(5/16,1/4)
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH16_NEEDED_BY_S7_24=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-s7-25
```
