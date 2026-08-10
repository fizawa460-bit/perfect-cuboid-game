# Stage14-4cj — xi rank-two elimination and rank-one physical-root rigidity

## Status

`COMPLETE_XI_RANK_TWO_ELIMINATION_AND_RANK_ONE_PHYSICAL_ROOT_RIGIDITY`

Stage14-4cj works on the exact balanced physical packet already carrying all merged Stage14-4ci data:

```text
common-core residual triple (C,u_res,v_res),
full k-dual saturation d_k=k^2,
normalized four-host equations,
xi CRT lattice Lambda_xi.
```

Merged Stage14-s7-23 eliminates every physical rank-three xi-short packet.  The only remaining branch there was `rank<=2`.  Stage14-4cj eliminates rank two as well, by using the cell-square moduli directly on the Plucker minors of two short vectors.

The consequence is stronger than a further stratification:

```text
physical xi short span rank = 1 exactly.
```

For a fixed legal oriented xi-CRT packet, reducedness then makes the physical root vector unique.

No whole-family fixed-power saving is promoted yet, because the number of moving rank-one cell/orientation packets above the common-core residual support is still unresolved.

---

## 1. Imported packet

Use merged s7-21 notation.  The xi-side CRT lattice is

```text
Lambda_xi subset Z^4,
X=(x_1,y_1,x_2,y_2),
```

with exact congruences

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2),
x_2 == lambda_S*y_1 (mod S^2),
y_2 == lambda_T*x_1 (mod T^2),                     (1.1)
```

and

```text
R*S*T*J=xi,
det Lambda_xi=xi^2.
```

The balanced endpoint scales are

```text
|x_i|,|y_i| <= B^(1/16+o(1)),
R,S,T,J >= B^(1/8-o(1)).                            (1.2)
```

Hence every cell square satisfies

```text
R^2,S^2,T^2,J^2 >= B^(1/4-o(1)).                   (1.3)
```

Merged s7-23 gives

```text
RANK3_PHYSICAL_ENDPOINT_PACKETS_EXIST=false.        (1.4)
```

Therefore only rank one or rank two can remain.

---

## 2. Assume rank two and form Plucker minors

Assume for contradiction that the endpoint-short span has rank two.  Choose two independent short vectors

```text
w=(x_1,y_1,x_2,y_2),
w'=(x'_1,y'_1,x'_2,y'_2)
```

in `Lambda_xi`, both with sup norm `O(B^(1/16+o(1)))`.

For `1<=i<j<=4` write

```text
p_ij = w_i*w'_j-w_j*w'_i.                          (2.1)
```

Then

```text
|p_ij| <= B^(1/8+o(1)).                             (2.2)
```

The Plucker coordinates of a rank-two plane are not all zero and satisfy

```text
p_12*p_34-p_13*p_24+p_14*p_23=0.                  (2.3)
```

---

## 3. The four CRT rows kill the four mixed minors

Apply each congruence in (1.1) to both `w` and `w'`.

### R row

Since

```text
y_1 == lambda_R*y_2,
y'_1 == lambda_R*y'_2          (mod R^2),
```

we have

```text
R^2 | y_1*y'_2-y_2*y'_1 = p_24.                   (3.1)
```

### J row

Similarly

```text
J^2 | x_1*x'_2-x_2*x'_1 = p_13.                   (3.2)
```

### S row

Likewise

```text
S^2 | y_1*x'_2-x_2*y'_1 = p_23.                   (3.3)
```

### T row

And

```text
T^2 | x_1*y'_2-y_2*x'_1 = p_14.                   (3.4)
```

By (1.3), every modulus on the left is `B^(1/4-o(1))`, whereas by (2.2) every corresponding minor is only `B^(1/8+o(1))`.  The exponent gap is

```text
1/4-1/8=1/8.                                       (3.5)
```

Therefore, for sufficiently large `B`, divisibility is possible only if

```text
boxed:
p_13=p_14=p_23=p_24=0.                            (3.6)
```

No large-sieve or density estimate is used; this is exact modulus-versus-height rigidity.

---

## 4. Plucker relation eliminates rank two

Substitute (3.6) into (2.3):

```text
p_12*p_34=0.                                       (4.1)
```

Because `w,w'` are independent, at least one Plucker coordinate is nonzero.

### Case A: `p_12 != 0`

Then columns 1 and 2 of the `2 x 4` matrix with rows `w,w'` are independent.  Since

```text
p_13=p_23=0,
```

column 3 is simultaneously proportional to both independent columns and therefore must be zero.  Likewise `p_14=p_24=0` forces column 4 to be zero.

Hence every vector in the rational plane spanned by `w,w'` has

```text
x_2=y_2=0.                                         (4.2)
```

But a physical root vector has

```text
x_2>0,
y_2>0.                                            (4.3)
```

Contradiction.

### Case B: `p_34 != 0`

The same argument gives

```text
x_1=y_1=0
```

for every vector in the plane, contradicting physical positivity of state 1.

### Case C: `p_12=p_34=0`

Then all six Plucker minors vanish, so `w,w'` are dependent, contradicting rank two.

Thus

```text
boxed:
XI_RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false.     (4.4)
```

Together with merged s7-23,

```text
boxed:
XI_PHYSICAL_SHORT_SPAN_RANK=1.                      (4.5)
```

The rank cannot be zero because the actual positive physical root vector itself belongs to `Lambda_xi` and lies in the endpoint short box.

---

## 5. The physical root vector is primitive

For state 1,

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
```

and the physical state is reduced:

```text
gcd(P_1,Q_1)=1.                                    (5.1)
```

Therefore

```text
gcd(x_1,y_1)=1.                                    (5.2)
```

Similarly

```text
gcd(x_2,y_2)=1.                                    (5.3)
```

In particular

```text
gcd(x_1,y_1,x_2,y_2)=1.                            (5.4)
```

So the actual root vector

```text
X=(x_1,y_1,x_2,y_2)
```

is a primitive integer vector.

Since the endpoint-short span is the rational line `Q*X`, every integer vector on that line is an integer multiple of `X`.

---

## 6. Fixed oriented xi-CRT packet has at most one physical root vector

Fix the complete legal oriented xi-CRT packet: cells, the finite auxiliary coefficient data already fixed in s7-21, and one primewise sign/Gaussian-root branch in each cell.  Its short span is rank one and contains a physical primitive vector `X`.

Any other positive physical root vector `Y` in the same short span must satisfy

```text
Y=m*X
```

for some positive integer `m`.

If `m>=2`, then in state 1

```text
P'_1=(R*S)*(m*x_1)^2,
Q'_1=(T*J)*(m*y_1)^2
```

have common factor `m^2`, contradicting reducedness.  Hence

```text
m=1.
```

Therefore

```text
boxed:
# {physical root vectors in a fixed legal oriented xi-CRT packet}
<=1.                                                (6.1)
```

Equivalently,

```text
ORIENTED_XI_CRT_PACKET_PHYSICAL_ROOT_VECTOR_MULTIPLICITY=1.
```

This sharpens the earlier divisor-many pointwise statement on the xi side.

---

## 7. Relation to the common-core/full-k-dual packet

Merged 4ci already proves simultaneously

```text
q_k=C*u_res,
q_xi=C*v_res,
K_PRIMITIVE_Z_DIRECTION_IN_LATTICE=true,
K_DUAL_SATURATION_ORDER=k^2,
K_DUAL_DEFECT=1,
gcd(z_1,z_2)^2 | q_k,
gcd(omega_1,omega_2)^2 | q_xi.                     (7.1)
```

Hence after 4cj both short-vector sides are line-rigid:

```text
k side:
  one primitive z direction, exact full dual saturation;

xi side:
  one primitive physical root direction, no rank-2 or rank-3 physical branch.
```

The remaining issue is no longer short-span geometry.  It is the number of moving legal cell/orientation packets that can realize these two compatible primitive directions while lying over the common-core residual support.

Define the new receiver

```text
CommonCoreRankOneXiCRTCellMultiplicity.             (7.2)
```

It counts the surviving balanced cell/orientation packets after imposing:

- fixed common-core residual data;
- normalized four-host equations;
- full k-dual primitive direction;
- xi rank-one primitive physical direction;
- all original physical masks.

The fixed oriented packet has root multiplicity one, but the number of such packets is not yet bounded by `B^o(1)` over `(C,u_res,v_res)`.

---

## 8. Why the exponent still does not move

4ci gives the dyadic residual-triple support exponent

```text
2*(theta+phi)-1/2,                                 (8.1)
```

which reaches `5/8` only at the upper corner.

A primitive xi root direction lies in a four-coordinate box of total raw exponent

```text
4*(1/16)=1/4.                                       (8.2)
```

Thus the crude compatible support ledger still permits

```text
5/8+1/4=7/8.                                       (8.3)
```

The rank-one theorem removes internal multiplicity inside one oriented packet, but it does not by itself show that the moving packet support occupies fewer than `B^(1/4+o(1))` effective root-direction/cell choices at the upper corner.

Accordingly

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.         (8.4)
```

The next saving must come from coupling the primitive root direction to the normalized four-host/common-core equations, not from another xi-rank stratification.

---

## 9. H-line decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

4cj uses only:

- merged exact CRT congruences;
- a determinant identity for `2 x 2` minors;
- the Plucker relation;
- endpoint modulus/height comparison;
- physical positivity and reducedness.

No external incidence theorem or analytic estimate is imported.  A new H line should be considered only if 4ck chooses to invoke an external theorem for the remaining rank-one cell/common-core incidence.

---

## Stage boundary

```text
STAGE14_4CJ=COMPLETE_XI_RANK_TWO_ELIMINATION_AND_RANK_ONE_PHYSICAL_ROOT_RIGIDITY
MERGED_4CI_IMPORTED=true
MERGED_S7_23_IMPORTED=true
MERGED_X1_CHARGE_ADAPTER_COMPATIBLE=true
XI_RANK3_PHYSICAL_ENDPOINT_PACKETS_EXIST=false
XI_RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false
XI_PHYSICAL_SHORT_SPAN_RANK=1
XI_MIXED_PLUCKER_MINORS_ZERO=true
XI_PLUCKER_MODULUS_HEIGHT_GAP_EXPONENT=1/8
PHYSICAL_XI_ROOT_VECTOR_PRIMITIVE=true
ORIENTED_XI_CRT_PACKET_PHYSICAL_ROOT_VECTOR_MULTIPLICITY=1
K_DUAL_SATURATION_ORDER=k^2
K_DUAL_DEFECT=1
COMMON_CORE_RANK_ONE_XI_CRT_CELL_MULTIPLICITY_REQUIRED=true
COMMON_CORE_RANK_ONE_XI_CRT_CELL_MULTIPLICITY_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4ck couple the primitive xi root direction with the normalized four-host/common-core equations and count the remaining rank-one cell/orientation packet support
```
