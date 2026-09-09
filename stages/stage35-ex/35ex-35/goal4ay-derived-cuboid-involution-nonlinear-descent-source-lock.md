# Stage35-EX Goal4AY source lock — classical derived-cuboid involution and nonlinear full-endpoint descent boundary

Scope: execute the Goal4AS candidate `GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT` after exact-green Goal4AX. Audited Stage35-EX authority remains V74 / Goal4AK (hostile review `5142248509`). Goal4AY is provisional. It does not assert that all possible nonlinear descent maps are impossible; it audits the source-locked and literature-visible candidates and isolates the exact failure of the strongest classical candidate.

## 1. Required descent contract

A genuine infinite-descent leaf must provide a total rule on the positive primitive **full endpoint** population:

```text
Phi : endpoint -> endpoint
```

such that for every endpoint:

1. all three face-square equations are preserved;
2. the space-square equation is preserved;
3. positivity and primitive normalization are preserved;
4. every parity/orientation branch and exceptional locus is covered;
5. a well-founded positive height `H` satisfies `H(Phi(P)) < H(P)`.

Goal4I already closed the common-scalar `v2` attempt because primitive endpoints do not admit a common factor 2. Goal4AY therefore tests nonlinear candidates only.

## 2. Classical pair-product / derived-cuboid map

A classical construction, already described by Spohn (1974) and Leech (1981), sends an Euler brick with edge triple `(A,B,C)` to the pair-product triple

```text
(AB, AC, BC)                                                   (AY-D0)
```

up to common scaling and permutation. Face-square preservation is immediate:

```text
(AB)^2+(AC)^2 = A^2(B^2+C^2) = (A*D_BC)^2,
(AB)^2+(BC)^2 = B^2(A^2+C^2) = (B*D_AC)^2,
(AC)^2+(BC)^2 = C^2(A^2+B^2) = (C*D_AB)^2.            (AY-D1)
```

Thus this is a genuine nonlinear self-map of the three-face Euler-brick population.

Literature boundary:

- W. G. Spohn, *On the Derived Cuboid*, Canadian Mathematical Bulletin 17 (1974), 575–577, DOI `10.4153/CMB-1974-102-6`, explicitly records that if `(x,y,z)` satisfies the three face equations then `(xy,xz,yz)` does too and calls the reduced triple the derived cuboid.
- J. Leech, *A Remark on Rational Cuboids*, Canadian Mathematical Bulletin 24 (1981), 377–378, DOI `10.4153/CMB-1981-058-1`, describes the pair-product construction as known to Euler. Its non-perfectness result concerns the displayed Euler/Saunderson parametric family and its derived family; it is not a theorem that the derived triple of every arbitrary Euler brick is non-perfect.

Goal4AY uses only the general pair-product construction from this literature. The new involution calculation below is derived directly from the current Stage35-EX primitive pair-gcd dictionary.

## 3. Exact primitive reduction through the six-variable dictionary

For a positive primitive endpoint write

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,                                             (AY-SIX)
```

with

```text
gcd(x,y)=gcd(x,z)=gcd(y,z)=1,
gcd(a,b)=gcd(a,c)=gcd(b,c)=1,
gcd(a,z)=gcd(b,y)=gcd(c,x)=1.
```

The raw pair products are

```text
AB = x^2*y*z*a*b,
AC = x*y^2*z*a*c,
BC = x*y*z^2*b*c.
```

Factor `x*y*z`. The remaining triple is

```text
x*a*b,  y*a*c,  z*b*c.                              (AY-D2)
```

Its common gcd is exactly one. Indeed,

```text
gcd(x*b, y*c)=1,
gcd(x*a, z*c)=1,
gcd(y*a, z*b)=1
```

by the displayed coprimalities, so any common prime of `x*a*b`, `y*a*c`, `z*b*c` would have to divide all of `a,b,c` after the corresponding pairwise reductions, which is impossible. Hence

```text
gcd(AB,AC,BC)=x*y*z.                                (AY-D3)
```

The primitive derived edges are therefore exactly

```text
A_D=x*a*b,
B_D=y*a*c,
C_D=z*b*c.                                          (AY-D4)
```

Their pair gcds are

```text
gcd(A_D,B_D)=a,
gcd(A_D,C_D)=b,
gcd(B_D,C_D)=c.                                     (AY-D5)
```

Consequently the residual variables of the derived triple are

```text
a_D=x,
b_D=y,
c_D=z.                                             (AY-D6)
```

So on the six-variable primitive Euler-brick dictionary the classical derived-cuboid operator is exactly

```text
D : (x,y,z ; a,b,c) -> (a,b,c ; x,y,z).             (AY-SWAP)
```

This is the key exact result of Goal4AY.

## 4. Reduced face data also close under the swap

With

```text
D_AB=x*r_AB,
D_AC=y*r_AC,
D_BC=z*r_BC,
```

the primitive derived face diagonals from `(AY-D1)` are

```text
D^D_AB = a*r_BC,
D^D_AC = b*r_AC,
D^D_BC = c*r_AB.                                   (AY-D7)
```

Equivalently the derived reduced hypotenuses are

```text
r^D_AB=r_BC,
r^D_AC=r_AC,
r^D_BC=r_AB.                                       (AY-D8)
```

Thus the pair-product construction is completely compatible with the three-face primitive dictionary; no hidden common-factor or parity exception remains at the Euler-brick level.

## 5. The fourth-square gate is not automatic

For the original full endpoint,

```text
W^2=(x*y*a)^2+(x*z*b)^2+(y*z*c)^2.                 (AY-W0)
```

For the primitive derived Euler brick, a rational/integer space diagonal would require the **dual fourth square**

```text
W_D^2=(x*a*b)^2+(y*a*c)^2+(z*b*c)^2.               (AY-W1)
```

Goal4AY does not derive `(AY-W1)` from `(AY-W0)` and the three face equations. Therefore the classical derived operator is not presently a source-locked total map on the full endpoint population.

In raw edge variables, writing

```text
Q=A^2*B^2+A^2*C^2+B^2*C^2,
```

one has the exact identity

```text
(D_AB*D_AC*D_BC)^2 + (A*B*C)^2
  = W^2 * Q.                                       (AY-W2)
```

Hence the derived raw pair-product triple has a space diagonal exactly when `Q` is a square, equivalently when the right-hand Pythagorean completion in `(AY-W2)` exists. This is an additional condition, not a consequence credited here.

## 6. Even hypothetical full preservation cannot give universal strict descent

Apply `(AY-SWAP)` twice:

```text
D^2(x,y,z ; a,b,c)=(x,y,z ; a,b,c).                (AY-I1)
```

Therefore primitive derived-cuboid reduction is an involution on the ordered primitive Euler-brick population.

Suppose, hypothetically, that `(AY-W1)` were automatic for every full endpoint, so that `D` became a total self-map of full endpoints. Let `H` be **any** real-valued or integer-valued height. A universal strict descent would require

```text
H(D(P)) < H(P).                                     (AY-I2)
```

Applying the same requirement to `D(P)` and using `D^2(P)=P` gives

```text
H(P) < H(D(P)),                                     (AY-I3)
```

a contradiction. Thus the classical derived-cuboid operator cannot be a universal strict-descent map even under the stronger hypothetical assumption that it preserved the fourth square everywhere.

This obstruction is independent of which well-founded height is chosen.

## 7. Other currently visible nonlinear candidates

### 7.1 Elliptic multiplication

Goal4L maps a physical endpoint to a non-torsion point on a specialized elliptic curve, but Goal4L explicitly does **not** claim endpoint equivalence of arbitrary elliptic points. Therefore `[n]P` on that elliptic curve is not a source-locked full-endpoint self-map. It cannot be used as a descent operator without a new reconstruction theorem preserving the other face conditions.

### 7.2 AX torus transformations

Goal4AX gives a six-coordinate norm-torus chart equivalent to the positive endpoint open. Sign changes, leg swaps, coordinate reciprocals, and unit/conjugation operations are chart symmetries or leave the positive chart; they do not supply a proved total strict height-decreasing endomorphism. Coordinatewise torus powering is not recorded as preserving the four cross-face incidence identities.

### 7.3 AU/AV Kummer relation

The relation `d_A*d_B*d_C=1` and its split coefficient package contain no map from one full endpoint to a second full endpoint. Goal4AV already froze this as a non-pruning common-cover shadow.

### 7.4 Current external divisibility-descent claim boundary

A scoped current-literature check also inspected Stéphane Yelle, *An Elementary Obstruction to the Existence of a Perfect Cuboid*, arXiv:`2602.00239v2` (9 February 2026). Version 2 describes a triangular-remainder divisibility propagation and says factoring a propagated common divisor gives a smaller configuration of the same *gluing type*, but the paper explicitly states that it does **not** claim to resolve the perfect-cuboid existence problem and concludes that fundamentally different mechanisms remain open. Goal4AY therefore does not import that prose as a full-endpoint descent map.

This literature check is scoped, not an exhaustive proof that no other map exists.

## 8. Candidate audit result

The currently source-locked candidates are therefore classified as follows:

```text
CLASSICAL_DERIVED_PAIR_PRODUCT
  = EXACT_THREE_FACE_SELF_MAP
  + EXACT_PRIMITIVE_INVOLUTION
  + FOURTH_SQUARE_NOT_AUTOMATIC
  + UNIVERSAL_STRICT_DESCENT_IMPOSSIBLE_FOR_THIS_OPERATOR

ELLIPTIC_MULTIPLICATION
  = NO_FULL_ENDPOINT_RECONSTRUCTION

AX_TORUS_SYMMETRIES
  = REPARAMETRIZATION_OR_UNPROVED_COMPATIBILITY_PRESERVATION

AU_AV_KUMMER
  = RELATION_NOT_SELF_MAP

YELLE_V2_DIVISIBILITY_PROPAGATION
  = EXPLORATORY_GLuing_DESCENT_NOT_FULL_ENDPOINT_RESOLUTION
```

Thus

```text
GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT
  -> FAIL_CLOSE_CURRENT_SOURCE_LOCKED_CANDIDATES
```

with the essential firewall:

```text
ALL_POSSIBLE_NONLINEAR_DESCENT_MAPS_PROVED_IMPOSSIBLE=false.
```

No infinite descent and no E1 closure are obtained.

## 9. Next lens

The next remaining Goal4AS untested route is amplification / stronger counting:

```text
NEXT=35EX-35_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_PREFLIGHT
```

The next leaf should ask whether one hypothetical endpoint forces sufficiently many distinct endpoint classes / marked receiver points below a controlled height to contradict Goal4M's `O(B^(1/2+o(1)))` population ceiling. It must prove distinctness and quantitative height control; mere symmetry or finite orbit multiplication is insufficient.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
