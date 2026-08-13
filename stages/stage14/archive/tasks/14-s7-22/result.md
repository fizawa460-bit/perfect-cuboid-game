# Stage14-s7-22 — rank-three dual saturation and bilinear tangent-resonance split

## Status

`COMPLETE_RANK_THREE_DUAL_SATURATION_AND_TANGENT_RESONANCE_SPLIT`

Merged Stage14-s7-21 reduces every balanced endpoint collision to two compatible short-vector lattices.  The `k`-side short lattice has rank at most one and therefore fixes a primitive positive product ratio

```text
(z_1,z_2)=t*(u,v),
gcd(u,v)=1,
```

hence the exact bilinear equation

```text
v*g_2*x_1*y_1 = u*g_1*x_2*y_2.                    (0.1)
```

Stage14-s7-22 now stratifies the remaining `xi`-side short lattice by rank.

The new point is that rank three is already a very strong arithmetic resonance.  If three independent endpoint-short vectors span a rational hyperplane `H`, then the primitive normal of `H` defines a dual character of the `xi` CRT lattice whose order consumes all but at most `B^(3/16+o(1))` of the exact discriminant-group order `xi^2=B^(3/2+o(1))`.  Thus a rank-three packet cannot be generic in the dual CRT group.

The bilinear surface (0.1) then gives a second exact dichotomy:

- non-tangent rank three: the section of the bilinear quadric by `H` is a smooth rational conic;
- tangent rank three: the normal itself satisfies a reciprocal product equation and the section splits into two rational planes.

No average fixed-power saving is promoted yet.  The current whole-family exponent remains `7/8`.

---

## 1. Imported endpoint object

Keep the merged s7-21 notation.  For one balanced physical orientation packet `Pi`,

```text
Lambda_xi(Pi) subset Z^4
```

is the exact root CRT lattice on

```text
X=(x_1,y_1,x_2,y_2)
```

with

```text
det Lambda_xi = xi^2 = B^(3/2+o(1)).               (1.1)
```

The endpoint root box has scale

```text
L=B^(1/16+o(1)),
|x_i|,|y_i|<=B^(1/16+o(1)).                        (1.2)
```

After fixing one legal `k`-side short direction, write

```text
A=v*g_2,
B=u*g_1.                                           (1.3)
```

The compatible physical roots lie on the split bilinear quadric

```text
Q_{A,B}(X)
 := A*x_1*y_1-B*x_2*y_2
 =0.                                                (1.4)
```

Here `g_i in {1,2}` and `(u,v)` is primitive.  No auxiliary character average is used.

Merged s7-21 proves

```text
rank span_Q(
  Lambda_xi cap [-C L,C L]^4
) <= 3                                              (1.5)
```

for every fixed constant `C` on the endpoint.

---

## 2. Rank stratification

Define the endpoint-short span

```text
S(Pi)
 = span_Q(
     Lambda_xi(Pi) cap [-C L,C L]^4
   ).                                               (2.1)
```

There are only two cases:

```text
LOW-RANK:
  dim S(Pi) <= 2;

RANK-THREE:
  dim S(Pi) = 3.                                    (2.2)
```

The low-rank branch is already confined to a rational plane or line before the physical bilinear equation is imposed.  This is a genuine dimension reduction, but it does not by itself imply average packet sparsity: an abstract matching may still place one physical pair in each low-rank packet.

Therefore Stage14-s7-22 does not discard the low-rank branch.

---

## 3. Primitive normal of a rank-three short span

Assume `dim S(Pi)=3`.  Let

```text
H=S(Pi)
```

and let

```text
c=(c_1,c_2,c_3,c_4) in Z^4
```

be the primitive integer normal, unique up to sign, so

```text
H={X in Q^4 : c dot X=0},
gcd(c_1,c_2,c_3,c_4)=1.                             (3.1)
```

Choose three independent vectors

```text
w_1,w_2,w_3 in Lambda_xi cap [-C L,C L]^4.
```

The coordinates of a primitive normal are the primitive reduction of the four `3 x 3` minors of the matrix with rows `w_i`.  Hadamard gives

```text
boxed:
||c||_infty << L^3.                                (3.2)
```

At the endpoint,

```text
boxed:
||c||_infty <= B^(3/16+o(1)).                      (3.3)
```

This height bound is unconditional and uses only the existence of three independent short vectors.

---

## 4. Hyperplane saturation order

Let

```text
d_H
 := gcd{ c dot lambda : lambda in Lambda_xi }.      (4.1)
```

Because `c` is primitive, the map

```text
Z^4 -> Z,
X |-> c dot X
```

is surjective, while its image on `Lambda_xi` is `d_H Z`.  Hence the induced quotient map

```text
Z^4/Lambda_xi -> Z/d_H Z
```

is surjective.  Therefore

```text
boxed:
d_H | [Z^4:Lambda_xi]=xi^2.                        (4.2)
```

Let

```text
Lambda_H=Lambda_xi cap H.
```

The standard height/covolume identity is exact:

```text
boxed:
covol_H(Lambda_H)
 = det(Lambda_xi)*||c||_2/d_H.                     (4.3)
```

Indeed, choose `b in Lambda_xi` with `c dot b=d_H`; its Euclidean height above `H` is `d_H/||c||_2`, and multiplying that height by `covol_H(Lambda_H)` gives `det Lambda_xi`.

On the other hand the three short vectors `w_i` generate a sublattice of `Lambda_H`, so

```text
covol_H(Lambda_H)
 <= vol_3(w_1,w_2,w_3)
 << L^3.                                             (4.4)
```

Combining (4.3)-(4.4),

```text
boxed:
d_H
 >> det(Lambda_xi)*||c||_2/L^3.                    (4.5)
```

In particular `||c||_2>=1`, so

```text
boxed:
d_H >> xi^2/L^3.                                   (4.6)
```

At the endpoint,

```text
log_B d_H
 >= 3/2-3/16-o(1)
 = 21/16-o(1).                                      (4.7)
```

Thus rank three forces a dual character of order at least

```text
boxed:
d_H >= B^(21/16-o(1)).                             (4.8)
```

inside a group of total order `xi^2=B^(24/16+o(1))`.

---

## 5. Near-full-order dual defect

Define the exact integer defect

```text
E_H := xi^2/d_H.                                    (5.1)
```

By (4.2), `E_H` is a positive integer.  By (4.5),

```text
E_H
 << L^3/||c||_2
 <= L^3.                                             (5.2)
```

Therefore

```text
boxed:
E_H <= B^(3/16+o(1)).                               (5.3)
```

Equivalently a rank-three short packet uses a dual element whose order misses the full CRT order by at most exponent `3/16`.

This is the first average-ready arithmetic certificate extracted from the rank-three condition: the existence of three short primal vectors is converted into a **near-full-order dual CRT character**.

No density statement is inferred from this conversion.

---

## 6. Cellwise form of the dual resonance

Recall the s7-21 `xi` lattice equations

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2),
x_2 == lambda_S*y_1 (mod S^2),
y_2 == lambda_T*x_1 (mod T^2),                     (6.1)
```

with pairwise-coprime squarefree cells `R,S,T,J` and

```text
R*S*T*J=xi.                                         (6.2)
```

Let the corresponding primitive row vectors be

```text
rho_R=(0,1,0,-lambda_R),
rho_J=(1,0,-lambda_J,0),
rho_S=(0,-lambda_S,1,0),
rho_T=(-lambda_T,0,0,1).                            (6.3)
```

Modulo integers, the dual quotient is

```text
Lambda_xi^*/Z^4
 ~= Z/R^2 Z
  x Z/J^2 Z
  x Z/S^2 Z
  x Z/T^2 Z,                                       (6.4)
```

with generators `rho_C/C^2`.  The product is direct because the four cell-square orders are pairwise coprime.

The element

```text
c/d_H + Z^4
```

has exact order `d_H`.  Hence there are coefficients

```text
t_R mod R^2,
t_J mod J^2,
t_S mod S^2,
t_T mod T^2                          (6.5)
```

such that

```text
c/d_H
 == t_R*rho_R/R^2
  + t_J*rho_J/J^2
  + t_S*rho_S/S^2
  + t_T*rho_T/T^2
    (mod Z^4).                                      (6.6)
```

Let

```text
d_C = C^2/gcd(t_C,C^2),
e_C = gcd(t_C,C^2)=C^2/d_C.                         (6.7)
```

Because the four cell-square orders are pairwise coprime,

```text
d_H=d_R*d_J*d_S*d_T,
E_H=e_R*e_J*e_S*e_T.                                (6.8)
```

Therefore every individual defect obeys

```text
boxed:
e_C <= E_H <= B^(3/16+o(1)),                       (6.9)
```

and every cell component has order

```text
boxed:
d_C >= C^2/E_H.                                    (6.10)
```

Since each endpoint `xi` cell satisfies

```text
C>=B^(1/8-o(1)),                                    (6.11)
```

we get the uniform lower scale

```text
boxed:
d_C >= B^(1/16-o(1))                              (6.12)
```

for every one of the four cell components.

Thus rank three is not produced by one exceptional cell carrying all the dual order: every balanced cell participates by a positive-power dual component.

---

## 7. Bilinear tangent criterion

Now impose the fixed product-ratio quadric

```text
Q_{A,B}(X)=A*x_1*y_1-B*x_2*y_2=0,
A=v*g_2,
B=u*g_1.                                            (7.1)
```

The hyperplane `H={c dot X=0}` is tangent to the projective quadric `Q_{A,B}=0` exactly when its normal lies on the dual quadric.

The gradient is

```text
grad Q
 =(A*y_1, A*x_1, -B*y_2, -B*x_2).                  (7.2)
```

Solving `c` proportional to `grad Q` at a point of `Q=0` gives the exact criterion

```text
boxed:
B*c_1*c_2 = A*c_3*c_4.                             (7.3)
```

Equivalently, in physical notation,

```text
boxed:
u*g_1*c_1*c_2
 =v*g_2*c_3*c_4.                                    (7.4)
```

This is the reciprocal/self-dual product relation associated with the physical equation

```text
v*g_2*x_1*y_1
 =u*g_1*x_2*y_2.                                    (7.5)
```

So the rank-three branch splits canonically into

```text
RANK3_NONTANGENT:
  u*g_1*c_1*c_2 != v*g_2*c_3*c_4;

RANK3_TANGENT:
  u*g_1*c_1*c_2  = v*g_2*c_3*c_4.                  (7.6)
```

---

## 8. Geometry of the two rank-three sections

The quadratic form `Q_{A,B}` is nondegenerate of rank four.

### 8.1 Non-tangent hyperplane

If (7.3) fails, the restriction

```text
Q_{A,B}|_H
```

has rank three.  Projectively,

```text
P(H) cap {Q=0}
```

is a smooth conic.  Because a physical point exists in a surviving packet, this conic has a rational point and is rationally parametrizable.

This creates the receiver

```text
NonTangentRankThreeConicIncidence.                  (8.1)
```

A uniform average count over the moving CRT hyperplanes is still required; no generic conic estimate is imported with uncontrolled coefficient-height loss.

### 8.2 Tangent hyperplane

If (7.3) holds, the restriction has rank two.  Since the original form is split and the tangent point is rational, the tangent section is the union of the two rational ruling planes through the tangent point:

```text
P(H) cap {Q=0}
 = Plane_+ union Plane_-.                           (8.2)
```

This is the plane-rich resonance branch

```text
TangentRankThreeDualProductResonance.               (8.3)
```

The split is exact over `Q`; it is not a finite-field approximation.

---

## 9. Tangent normals are fixed-power sparse inside the raw normal box

Put

```text
M := O(L^3).                                        (9.1)
```

By (3.2), every rank-three primitive normal satisfies

```text
|c_i|<=M.                                           (9.2)
```

For fixed positive `A,B`, tangent normals satisfy

```text
B*c_1*c_2=A*c_3*c_4.                               (9.3)
```

Let `g=gcd(A,B)`, `A=g*A_0`, `B=g*B_0`, with `gcd(A_0,B_0)=1`.  Distributing the prime powers of `A_0,B_0` among the two coordinates on their respective sides costs only

```text
tau(A_0 B_0)^{O(1)}=B^o(1)                         (9.4)
```

in the Stage14 range.  After that allocation, the remaining count is bounded by the multiplicative energy

```text
#{(a,b,c,d): |a|,|b|,|c|,|d|<=M, ab=cd}.           (9.5)
```

For nonzero positive variables this is `O(M^2 log M)` by the elementary parameterization

```text
a=h*r,
c=h*s,
gcd(r,s)=1,
b=s*t,
d=r*t,                                             (9.6)
```

and summing `O((M/max(r,s))^2)` over coprime `(r,s)`.  Signs and zero-coordinate cases contribute only the same order.

Hence

```text
boxed:
# tangent primitive normals for fixed (A:B)
 << M^2 B^o(1)
 = L^6 B^o(1).                                      (9.7)
```

At the endpoint,

```text
boxed:
tangent-normal exponent <= 6/16=3/8.               (9.8)
```

The full raw normal box has exponent

```text
4*(3/16)=3/4.                                       (9.9)
```

Thus tangency is genuinely fixed-power sparse **inside the normal parameter box**.

This does **not** yet prove a fixed-power saving for physical collision packets, because the map from orientation packets to near-full-order dual normals has not been shown to have bounded average fibers.

---

## 10. The stratified remaining energy

The exact `BalancedDualCRTShortVectorEnergy` from s7-21 is now partitioned into three disjoint branches:

```text
E_low:
  dim S(Pi)<=2;

E_conic:
  dim S(Pi)=3
  and u*g_1*c_1*c_2 != v*g_2*c_3*c_4;

E_tan:
  dim S(Pi)=3
  and u*g_1*c_1*c_2  = v*g_2*c_3*c_4.              (10.1)
```

For both rank-three branches the additional exact certificate is

```text
d_H | xi^2,
d_H>=B^(21/16-o(1)),
E_H=xi^2/d_H<=B^(3/16+o(1)),                        (10.2)
```

with positive-power participation from all four balanced `xi` cells.

Define the umbrella receiver

```text
ProductRatioStratifiedXiDualResonanceEnergy.         (10.3)
```

A sufficient next theorem is

```text
E_low+E_conic+E_tan
 << B^(7/8-delta+o(1))                              (10.4)
```

for some fixed `delta>0`.

No one of the three terms is declared power-saved in s7-22.

---

## 11. Relation to merged 4cg and toolbox

Merged Stage14-4cg concerns the same balanced physical collision pair and derives a different exact coupling of the four Gaussian residual hosts through a common odd core `C` and reduced norms.

That theorem is compatible with the present CRT rank stratification, but s7-22 does not use the 4cg common-core norm count to infer any short-vector density.  In particular,

```text
4cg fixed-(C,u_res,v_res) divisor multiplicity
```

is not cross-promoted into a bound for

```text
ProductRatioStratifiedXiDualResonanceEnergy.
```

This preserves the current toolbox promotion contract.

```text
MERGED_4CG_COMPATIBILITY_CHECKED=true
FOUR_CG_COMMON_CORE_PROMOTED_INTO_S7_22_ESTIMATE=false
```

---

## 12. Why the whole-family exponent does not move yet

The new facts are strong but structural:

- rank three implies a dual character of order `>=B^(21/16-o(1))`;
- its total defect is `<=B^(3/16+o(1))`;
- each balanced cell contributes positive-power order;
- tangent rank three additionally forces the dual product equation (7.4);
- tangent normals occupy only `B^(3/8+o(1))` possibilities for a fixed product ratio inside a raw `B^(3/4+o(1))` normal box.

What is still missing is an average **packet-to-dual-normal fiber theorem**.  Without it, one cannot charge each physical packet injectively or boundedly to `(u:v,c,d_H)` and sum the normal sparsity.

Accordingly

```text
V(B) << B^(7/8+o(1))
```

remains the unconditional whole-family theorem.

---

## 13. tH / auxiliary-line decision

No new tH line is needed for s7-22.  Every step above is exact geometry of numbers, finite-index lattice duality, or the elementary bilinear tangent criterion on the physical positive pair space.

The existing tH14 R2 quadratic-large-sieve adapter still lives on a different coefficient space and is not required here.

```text
TH16_NEEDED_BY_S7_22=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

If the next step requires an external average theorem for near-full-order dual CRT characters, that theorem should be audited only after the exact packet-to-normal coefficient space is fixed.

---

## 14. Quantitative ledger

Endpoint scales:

```text
xi exponent                  = 3/4,
det Lambda_xi exponent       = 3/2,
root scale L exponent        = 1/16,
rank-three normal height     <= 3/16,
rank-three saturation order  >= 3/2-3/16=21/16,
rank-three dual defect       <= 3/16.               (14.1)
```

Cellwise consequence:

```text
min xi-cell exponent         = 1/8,
min cell-square exponent     = 1/4,
min dual component order     >= 1/4-3/16=1/16.      (14.2)
```

Tangent-normal count for fixed `(A:B)`:

```text
M=L^3,
# tangent normals << M^2 B^o(1)=L^6 B^o(1),
exponent <= 3/8.                                    (14.3)
```

No new whole-family exponent:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.          (14.4)
```

---

## 15. Next receiver

Stage14-s7-23 should attack the new packet-to-dual-normal fiber problem.

The preferred order is

```text
fixed primitive product ratio (u:v)
-> rank<=2 branch separately
-> rank3 primitive normal c
-> near-full saturation order d_H
-> cellwise dual coefficients t_R,t_J,t_S,t_T
-> split tangent vs non-tangent by
   u*g_1*c_1*c_2 = v*g_2*c_3*c_4
-> count how many legal physical orientation packets can realize
   one fixed near-full-order dual datum.             (15.1)
```

The immediate target is a bound of the form

```text
average packet fiber over fixed (u:v,c,d_H)
 <= B^o(1),                                         (15.2)
```

or any fixed-power substitute strong enough to turn the normal-level tangent sparsity / conic incidence into a saving for the original physical collision energy.

---

## Stage boundary

```text
STAGE14_S7_22=COMPLETE_RANK_THREE_DUAL_SATURATION_AND_TANGENT_RESONANCE_SPLIT
MERGED_S7_21_IMPORTED=true
MERGED_S7_20_TRANSITIVELY_IMPORTED=true
MERGED_4CG_COMPATIBILITY_CHECKED=true
PRODUCT_RATIO_FIXED_BEFORE_XI_RANK_SPLIT=true
XI_SHORT_RANK_LE_2_BRANCH_DEFINED=true
XI_SHORT_RANK3_BRANCH_DEFINED=true
RANK3_PRIMITIVE_NORMAL_DEFINED=true
RANK3_NORMAL_HEIGHT_UPPER_EXPONENT=3/16
RANK3_HYPERPLANE_SATURATION_DIVIDES_XI2=true
RANK3_HYPERPLANE_SATURATION_LOWER_EXPONENT=21/16
RANK3_DUAL_DEFECT_DEFINED=true
RANK3_DUAL_DEFECT_UPPER_EXPONENT=3/16
RANK3_DUAL_QUOTIENT_CELL_DECOMPOSITION_EXACT=true
RANK3_EACH_CELL_DEFECT_AT_MOST_GLOBAL_DEFECT=true
RANK3_EACH_CELL_DUAL_COMPONENT_ORDER_LOWER_EXPONENT=1/16
RANK3_TANGENT_CRITERION=u*g1*c1*c2=v*g2*c3*c4
RANK3_NONTANGENT_SECTION_SMOOTH_CONIC=true
RANK3_TANGENT_SECTION_TWO_RATIONAL_PLANES=true
FIXED_PRODUCT_RATIO_TANGENT_NORMAL_COUNT_EXPONENT=3/8
TANGENT_NORMAL_FIXED_POWER_SPARSE_IN_RAW_NORMAL_BOX=true
PACKET_TO_DUAL_NORMAL_AVERAGE_FIBER_PROVED=false
PRODUCT_RATIO_STRATIFIED_XI_DUAL_RESONANCE_ENERGY_REQUIRED=true
PRODUCT_RATIO_STRATIFIED_XI_DUAL_RESONANCE_ENERGY_PROVED=false
FOUR_CG_COMMON_CORE_PROMOTED_INTO_S7_22_ESTIMATE=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH16_NEEDED_BY_S7_22=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-s7-23
```
