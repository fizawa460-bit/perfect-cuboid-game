# Stage32 MB104 — `000707000f0f` e=2 sheet-selected fiber Abel--Jacobi constraint

Status: **RETAINED CANDIDATE BRANCH-ALLOCATION GLOBALIZATION / TWO SHEET-SELECTED 28l-POINT DIVISORS DIFFER BY E[2] / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the retained residual-node representatives and the common-`H`-cover factor-line result

```text
M_i=psi_i^*O_R(1),
delta_fac=M_1 tensor M_2^(-1) in Pic^0(E)[2].
```

This note identifies `delta_fac` with an explicit difference of two degree-`28l` divisors made entirely from the unresolved residual-sheet allocation at the supported nodes.

## 1. First-factor full fiber from the Q1 packet

The retained residual coordinate representatives on the seven `Q1 / b2=0` supported nodes are

```text
P8,P10  -> (u,v),
P9,P11  -> (u,-v),
P32,P34 -> (u,-u),
P33     -> (u,u).
```

Thus in **every** displayed representative the first factor is

```text
r_z=+u.
```

At node `Pj`, exactly `x_j` of its `8l` normalization branches use the displayed representative and the remaining `8l-x_j` use its simultaneous negative.  Therefore the reduced divisor

```text
D_z^+
```

of normalization points with first-factor value `r_z=+u` contains exactly the displayed-side branches at

```text
j in {8,9,10,11,32,33,34}.
```

The retained Q1 saturation equation is

```text
x8+x9+x10+x11+x32+x33+x34=28l.
```

Since `deg psi_1=28l`, these supported points exhaust the complete fiber:

```text
D_z^+ = psi_1^*(+u)                             (DZ)
```

as a reduced degree-`28l` divisor.

## 2. Second-factor full fiber from the Q0 packet

For the seven `Q0 / b1=0` supported nodes the retained representatives are

```text
P0,P2   -> (a,a),
P1,P3   -> (a,-a),
P24,P26 -> (b,-a),
P25     -> (b,a).
```

Hence the second-factor `r_w=+a` fiber selects:

```text
- displayed-side branches at P0,P2,P25;
- simultaneous-negative branches at P1,P3,P24,P26.
```

Define the corresponding reduced divisor on the normalization by

```text
D_w^+.
```

Its degree is

```text
deg D_w^+
 = x0+x2+x25
   +(8l-x1)+(8l-x3)+(8l-x24)+(8l-x26)
 = 32l+(x0-x1+x2-x3-x24+x25-x26).
```

The retained Q0 equation gives

```text
x0-x1+x2-x3-x24+x25-x26=-4l,
```

so

```text
deg D_w^+=28l.
```

Boundary-fiber saturation says there are no additional points in that fiber.  Therefore

```text
D_w^+ = psi_2^*(+a)                             (DW)
```

as a reduced degree-`28l` divisor.

## 3. Exact Abel--Jacobi class of the sheet-selected allocation

By definition of the factor fiber line bundles,

```text
O_E(D_z^+) ~= M_1,
O_E(D_w^+) ~= M_2.
```

The common-`H`-cover refinement proved

```text
M_1 tensor M_2^(-1) in Pic^0(E)[2].
```

Thus

```text
delta_fac
 = O_E(D_z^+-D_w^+)
 in Pic^0(E)[2].                                (AJ2)
```

Equivalently,

```text
2D_z^+ ~ 2D_w^+.                               (DOUBLE)
```

This is an exact global constraint on the branch allocation, not merely a count equation.

## 4. Why this is stronger than the existing saturation equations

The retained saturation equations only say that the two selected divisors have equal degree `28l`.  Equal degree on an elliptic curve leaves a one-dimensional `Pic^0(E)` ambiguity.

`(AJ2)` collapses that continuous ambiguity to

```text
Pic^0(E)[2],
```

which has exactly four points.

Therefore any geometric branch allocation compatible with the e=2 common-cover structure must satisfy:

```text
AJ(D_z^+-D_w^+) in {0, eta_1, eta_2, eta_3},
```

where the three nonzero classes are the elliptic 2-torsion points of `E`.

No particular one of the four classes is selected here.

## 5. Direct connection to the conductor-sheet variable

The divisors `D_z^+` and `D_w^+` are built only from the branchwise simultaneous-sign choice

```text
(r_z,r_w) <-> (-r_z,-r_w)
```

at the supported nodes.  Thus `(AJ2)` is a global relation on the **same binary allocation** that controls the conductor residual-sheet character.

It does not by itself determine the weighted conductor cut, because it records the Abel--Jacobi sum of the selected points rather than the pairwise intersection weights among branches at one singular point.

Nevertheless it removes the possibility that the fourteen node allocations can be chosen independently subject only to the two integer saturation equations and parity conditions.

## 6. Concrete next target

The remaining question can now be stated on the elliptic normalization itself:

```text
compute AJ(D_z^+-D_w^+)
```

from the explicit ambient restrictions of the two lifted boundary fibers, or show that one/all of the nonzero classes in `E[2]` are incompatible with the singular-carrier conductor descent.

A successful identification of this class can then be combined with:

- the exact node-level counts `x_j`;
- the parity congruences from the etale-basechange passport;
- the exact A1 lift-energy formula;
- the generalized-Jacobian gluing character.

## Firewalls

- `(AJ2)` is linear equivalence on the smooth normalization `E`, not on the singular carrier.
- No equality between `delta_fac` and the retained residual half-branch class `eta` is asserted.
- No individual branch is assigned a conductor transition beyond its retained displayed/negative label.
- No weighted-cut upper bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
