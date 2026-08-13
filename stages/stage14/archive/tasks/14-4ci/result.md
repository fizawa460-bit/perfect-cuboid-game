# Stage14-4ci — full k-dual saturation inside the common-core residual packet

## Status

`COMPLETE_COMMON_CORE_FULL_K_DUAL_SATURATION_AND_NORMALIZED_HOST_REDUCTION`

Merged Stage14-4ch reduces the mainline endpoint to the residual triple

```text
q_k=C*u_res,
q_xi=C*v_res,
```

with all eight balanced cells retained and proves that fixed cells plus `(C,u_res,v_res)` have only `B^o(1)` physical lifts.  Merged Stage14-s7-22 independently refines the same physical pair by the `k` rank-one short direction and the `xi` rank/dual-resonance split.

Stage14-4ci connects these two descriptions exactly.  The main new fact is stronger than the rank-one statement recorded in s7-21/s7-22: after primitive reduction, the `z` direction itself belongs to the `k` CRT lattice.  Hence the corresponding dual character has **full order `k^2`**, with defect exactly one.

No whole-family fixed-power saving is claimed.  The current bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported common coefficient space

Keep the merged balanced collision packet

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta,
```

and physical roots

```text
(x_1,y_1,x_2,y_2),
(z_1,z_2),
(r_1,s_1,r_2,s_2),
(omega_1,omega_2).
```

The exact endpoint identities include

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},

gcd(k,xi*z_i)=1,
gcd(xi,k*omega_i)=1.
```

The common-core residual data are

```text
q_k=C*u_res,
q_xi=C*v_res.
```

Merged s7-21 defines the homogeneous two-dimensional CRT lattice

```text
Lambda_k subset Z^2
```

by the four cell-square congruences modulo

```text
alpha^2,beta^2,gamma^2,delta^2,
```

with exact determinant

```text
det Lambda_k=k^2.
```

Merged s7-22 fixes the primitive positive ratio of the physical `z` vector.

---

## 2. X0 physical-fiber adapter is now closed

Stage14-X0 recommended the lemma

```text
JointCommonCoreCRTPhysicalFiberLemma:
fixed legal (xi,k), cells, primewise orientations,
(C,u_res,v_res), and primitive z ratio
=> B^o(1) physical joint packets.
```

Merged 4ch proves the stronger statement

```text
fixed cells and (C,u_res,v_res)
=> B^o(1) physical lifts.
```

Fixing additional `(xi,k)`, orientations, or primitive ratio can only reduce that fiber.  Therefore the X0 adapter is now an immediate corollary:

```text
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true.
```

This closes a projection-fiber obligation only.  It does not supply the missing average fixed-power gain over moving cell packets.

---

## 3. Primitive z direction belongs to the full k CRT lattice

Write

```text
t=gcd(z_1,z_2),
z_1=t*a_z,
z_2=t*b_z,
gcd(a_z,b_z)=1.
```

Since `gcd(k,z_1 z_2)=1`,

```text
gcd(t,k)=1.
```

The physical vector `(z_1,z_2)` belongs to `Lambda_k`.  Every defining congruence of `Lambda_k` is homogeneous modulo a divisor of `k^2`.  Multiplication by `t^{-1}` modulo each cell square is therefore legal, giving

```text
boxed:
(a_z,b_z) in Lambda_k.                              (3.1)
```

Because `(a_z,b_z)` is a primitive integer vector, every integral vector on its rational line is an integral multiple of it.  Hence

```text
boxed:
Lambda_k cap Q*(a_z,b_z) = Z*(a_z,b_z).             (3.2)
```

The rank-one short direction is not merely a short rational direction: it is the primitive lattice line itself.

---

## 4. Full k-side dual saturation

Let

```text
n_k=(b_z,-a_z)
```

be the primitive normal to the line in (3.2), and define

```text
d_k=gcd{ n_k dot lambda : lambda in Lambda_k }.
```

As usual,

```text
d_k | det Lambda_k=k^2.
```

For a primitive hyperplane normal in dimension two, the exact covolume identity is

```text
covol_line(Lambda_k cap n_k^perp)
 = det(Lambda_k)*||n_k||/d_k.                       (4.1)
```

By (3.2), the left side is exactly `||(a_z,b_z)||`, and

```text
||n_k||=||(a_z,b_z)||.
```

Therefore

```text
boxed:
d_k=k^2.                                            (4.2)
```

Define the k-dual defect

```text
E_k=k^2/d_k.
```

Then

```text
boxed:
E_k=1.                                               (4.3)
```

Thus the k side is **fully saturated**.  This is stronger than the xi rank-three theorem of s7-22, where only

```text
E_H<=B^(3/16+o(1))
```

is currently known.

---

## 5. Cellwise consequence: every k cell has full dual order

The four k-cell congruences have pairwise-coprime moduli.  The determinant identity from s7-21 gives

```text
Z^2/Lambda_k
 ~= Z/alpha^2 Z
  x Z/beta^2 Z
  x Z/gamma^2 Z
  x Z/delta^2 Z.                                   (5.1)
```

The dual class `n_k/k^2` has order `k^2`.  Since the four component orders are pairwise coprime and their product is `k^2`, every component must have its maximal possible order:

```text
boxed:
k-cell dual component orders
 = alpha^2,beta^2,gamma^2,delta^2.                  (5.2)
```

Equivalently, once the primitive ratio `(a_z:b_z)` is fixed, the legal k-side orientation modulo each cell square is forced by that ratio.  There is no residual k-side dual defect to average over.

---

## 6. Common z scale is a square divisor of q_k

Use the 4cf/4cg positive host identity

```text
beta^2*q_k
 = alpha^2*r_2^4*z_1^2
   +delta^2*s_1^4*z_2^2.                            (6.1)
```

Substitute `z_1=t*a_z`, `z_2=t*b_z`:

```text
beta^2*q_k
 = t^2(
     alpha^2*r_2^4*a_z^2
     +delta^2*s_1^4*b_z^2
   ).                                               (6.2)
```

Because `beta|k` and `gcd(t,k)=1`, `gcd(t,beta)=1`.  Hence

```text
boxed:
t^2 | q_k=C*u_res.                                  (6.3)
```

Thus for fixed residual triple, the common `z` scale has only divisor-many possibilities:

```text
# {t : t^2|C*u_res} <= tau(C*u_res)=B^o(1).         (6.4)
```

This removes the apparent `B^(1/8)` scaling range when the s7 product ratio is intersected with the common-core residual packet.

---

## 7. Symmetric omega-scale square divisor

Put

```text
h=gcd(omega_1,omega_2),
omega_1=h*a_omega,
omega_2=h*b_omega,
gcd(a_omega,b_omega)=1.
```

From

```text
S^2*q_xi
 = R^2*x_2^4*omega_1^2
   +J^2*y_1^4*omega_2^2                              (7.1)
```

and `gcd(xi,omega_1 omega_2)=1`, hence `gcd(h,S)=1`, we obtain

```text
boxed:
h^2 | q_xi=C*v_res.                                 (7.2)
```

The omega variables are already `B^o(1)` at the endpoint, but (7.2) gives the exact symmetric scale normalization.

---

## 8. Exact normalized four-host system

Define

```text
Q_k=q_k/t^2,
Q_xi=q_xi/h^2.
```

Then the two k switched-host equations become

```text
boxed:
beta^2*Q_k
 = alpha^2*r_2^4*a_z^2
   +delta^2*s_1^4*b_z^2,                            (8.1)

gamma^2*Q_k
 = delta^2*s_2^4*a_z^2
   +alpha^2*r_1^4*b_z^2.                            (8.2)
```

Similarly the two xi switched-host equations become

```text
boxed:
S^2*Q_xi
 = R^2*x_2^4*a_omega^2
   +J^2*y_1^4*b_omega^2,                            (8.3)

T^2*Q_xi
 = J^2*y_2^4*a_omega^2
   +R^2*x_1^4*b_omega^2.                            (8.4)
```

These are exact integral equations on the same physical packet.  No local-density multiplication is used.

For fixed `(C,u_res,v_res)`, the scale choices `t,h` are divisor-bounded; the k primitive ratio carries full CRT order; and the remaining xi geometry is exactly the low-rank / rank-three conic / rank-three tangent split of s7-22.

---

## 9. Dyadic residual support is narrower than the global 5/8 ledger

Write as in 4cg

```text
alpha,delta=B^(theta+o(1)),
beta,gamma=B^(1/2-theta+o(1)),

R,J=B^(phi+o(1)),
S,T=B^(3/8-phi+o(1)).
```

On the surviving strip

```text
0<=theta-phi<=1/8,
theta+phi>=3/8.
```

4cg gives the blockwise bounds

```text
C <= B^(2theta+2phi-3/4+o(1)),
u_res <= B^(2theta-2phi+o(1)),
v_res <= B^(1/4+2phi-2theta+o(1)).
```

Therefore

```text
u_res*v_res <= B^(1/4+o(1))
```

and, more sharply, the number of residual triples in one fixed `(theta,phi)` block is

```text
boxed:
B^(2theta+2phi-1/2+o(1)).                            (9.1)
```

This ranges from exponent `1/4` on the lower boundary `theta+phi=3/8` to exponent `5/8` only at the far upper corner.  The global `5/8` support from 4ch is valid but cannot be combined with a cell-multiplicity maximum taken from an incompatible dyadic block.

This compatibility ledger is retained for the next optimization.

---

## 10. Refined remaining receiver

The old 4ch receiver

```text
CommonCoreResidualEightCellMultiplicity
```

is now refined to

```text
CommonCoreFullKDualXiStratifiedMultiplicity.         (10.1)
```

A surviving packet must simultaneously carry

```text
(C,u_res,v_res),
t^2|C*u_res,
h^2|C*v_res,
primitive (a_z:b_z),
full k-dual saturation d_k=k^2,
normalized equations (8.1)-(8.4),
and one of the s7-22 xi branches:
  rank<=2,
  rank3 non-tangent conic,
  rank3 tangent dual-product resonance.
```

Because 4ch gives `B^o(1)` physical lifts after cells and residual data are fixed, the only remaining fixed-power issue is the number of legal moving cell packets satisfying this normalized full-k-dual / xi-stratified system.

The k orientation fiber is no longer an obstruction.

---

## 11. What is not proved

Stage14-4ci does **not** prove that a fixed residual triple has `B^o(1)` cell packets.  It also does not prove a fixed-power saving in any of the three xi rank branches.

In particular, the following implication is still invalid:

```text
full k dual saturation
+ near-full xi dual saturation
=> average cell multiplicity B^o(1).
```

The normalized equations are a stronger exact coefficient space on which the next counting argument must operate.

Accordingly

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 12. H-line decision

Everything in 4ci is exact homogeneous CRT arithmetic, primitive-vector reduction, elementary lattice duality, and integer divisibility.  No external theorem is imported.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

`tH16` remains relevant only to the separate fixed-U/t route.  No new mainline H branch should be opened here.

---

## Stage boundary

```text
STAGE14_4CI=COMPLETE_COMMON_CORE_FULL_K_DUAL_SATURATION_AND_NORMALIZED_HOST_REDUCTION
MERGED_4CH_IMPORTED=true
MERGED_S7_22_IMPORTED=true
MERGED_X0_TRANSFER_AUDIT_IMPORTED=true
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true
K_PRIMITIVE_Z_DIRECTION_IN_LATTICE=true
K_PRIMITIVE_LINE_INTERSECTION_EQUALS_Z_DIRECTION=true
K_DUAL_SATURATION_ORDER=k^2
K_DUAL_DEFECT=1
K_EACH_CELL_DUAL_COMPONENT_FULL_ORDER=true
K_ORIENTATION_FORCED_BY_PRIMITIVE_Z_RATIO=true
COMMON_Z_SCALE_SQUARE_DIVIDES_QK=true
COMMON_Z_SCALE_FIXED_RESIDUAL_MULTIPLICITY=Bo1
COMMON_OMEGA_SCALE_SQUARE_DIVIDES_QXI=true
NORMALIZED_COUPLED_FOUR_HOST_SYSTEM_PROVED=true
DYADIC_RESIDUAL_TRIPLE_SUPPORT_EXPONENT=2*(theta+phi)-1/2
COMMON_CORE_FULL_K_DUAL_XI_STRATIFIED_MULTIPLICITY_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cj count CommonCoreFullKDualXiStratifiedMultiplicity from the normalized equations, separating xi rank<=2, rank3 conic, and rank3 tangent branches without paying an independent k-orientation or z-scale loss
```
