# Stage32 MB104 — `000707000f0f` e=2 zero-quartic torsion congruences

Status: **RETAINED CONDITIONAL ZERO-QUARTIC 2-TORSION NECESSARY CONDITIONS / TWO NEW MOD-4 BRANCH CONGRUENCES / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the exact Picard64 consequence

```text
x_j is even for every supported node,
```

and write, for arbitrary `l>=1`,

```text
y_j=x_j/2,
b_j=y_j-2l=x_j/2-2l,
d_j=4b_j.
```

The conclusions below also use the already-retained candidate ambient-H1 linear equivalence through the half-hyperplane factorization. They therefore inherit that candidate status.

## 1. The two used zero quartics split in the residual double cover

The residual double cover `pi:Y->S` is the Kummer cover of the absent-type square class. For one product factor this class is represented by

```text
f_t=(t-i)/(t+i),
```

whose zero and pole are the two absent-type bad fibers. The complementary product factor has the analogous representative `f_u`, and the retained cuboid identity proves

```text
[f_t]=[f_u]
```

already in the ambient function-field square-class group.

For each used zero quartic `Qk`, choose the product factor for which that quartic is the fixed used-type boundary fiber. Its corresponding representative (`f_t` or `f_u`) restricts to a nonzero constant on `Qk`: the used fiber is distinct from the two absent zero/pole fibers. Since the two factor representatives define the same ambient square class, this computes the restriction of the actual residual double cover.

Over the complex ground field every nonzero constant is a square. Therefore

```text
pi^{-1}(Qk)=Qk^+ disjoint_union Qk^-,
k=0,1.
```

Choose `Qk^+` by the residual factor value used in the exact node-orbit table:

```text
Q0^+ : fixed second-factor value r_w=+a,
Q1^+ : fixed first-factor value  r_z=+u.
```

This componentwise splitting does not assert that the two `+` components glue to one global sheet across both intersection points of `Q0` and `Q1`; no such assertion is needed below.

## 2. Restriction of the candidate linearization

The retained effective conjugate divisors are

```text
G1=C1+sum_j[y_j E_j^+ +(4l-y_j)E_j^-],
G2=C2+sum_j[(4l-y_j)E_j^+ +y_j E_j^-].
```

Their difference is

```text
G1-G2=(C1-C2)+2 sum_j b_j F_j,
F_j=E_j^+-E_j^-.
```

The candidate ambient-H1 input gives

```text
G1~G2.
```

The original carrier has `D_l.Qk=0`, so an integral carrier distinct from `Qk` is disjoint from `Qk` on the smooth resolution. Hence `C1` and `C2` are disjoint from `Qk^+`. Restricting the principal class `G1-G2` to `Qk^+` therefore gives

```text
2 D_k ~ 0 in Pic^0(Qk),
```

where

```text
D_0 = b0 P0-b1 P1+b2 P2-b3 P3-b24 P24+b25 P25-b26 P26,
D_1 = b8 P8+b9 P9+b10 P10+b11 P11+b32 P32+b33 P33+b34 P34.
```

The signs are exactly the residual-lift orientations from the retained node table. The boundary-fiber saturation equations are precisely

```text
deg D_0=0,
deg D_1=0.
```

Thus every geometric realization satisfying the candidate linearization must obey

```text
O_Q0(D_0) in Pic^0(Q0)[2],
O_Q1(D_1) in Pic^0(Q1)[2].                    (Q2)
```

## 3. Exact box-node torsion partition on a zero quartic

Use the representative elliptic quartic model

```text
Q: z^2=x^2-y^2,
   w^2=x^2+y^2.
```

Its eight box nodes split into

```text
A: y=0, four nodes,
B: x=0, four nodes.
```

Choose one `A` node as the elliptic origin.

The planes

```text
z=+x, z=-x, w=+x, w=-x
```

cut `Q` in divisors consisting of two `A` nodes, each with multiplicity two. Hence differences among the four `A` nodes are 2-torsion. Since there are exactly four distinct `A` nodes, they are exactly `Q[2]`.

Likewise the planes

```text
z=+i y, z=-i y, w=+y, w=-y
```

cut `Q` in two `B` nodes with multiplicity two. Therefore differences among the four `B` nodes are 2-torsion, so all four have the same image under doubling. That common double cannot be zero: otherwise all four `B` nodes would also lie in the already exhausted four-point set `Q[2]`. Thus the common double is one fixed nonzero element of `Q[2]`.

Consequently, for every degree-zero divisor

```text
D=sum_P c_P P
```

supported on the eight box nodes,

```text
[D] in Pic^0(Q)[2]
iff
sum_(P in B) c_P == 0 mod 2.                  (TORSION-TEST)
```

This criterion is invariant under the retained projective `Aut(S)` transport.

## 4. Apply the test to Q0 and Q1

For `Q0`, the eight nodes are

```text
P0,P1,P2,P3,P24,P25,P26,P27,
```

with the first four in the `y=0` half and the last four in the `x=0` half. The current support omits `P27`. Applying `(TORSION-TEST)` to `D_0` gives

```text
b24+b25+b26 == 0 mod 2.                       (B0)
```

Since `b_j=x_j/2-2l`, this is exactly

```text
x24+x25+x26 == 0 mod 4.                       (X0a)
```

Using the exact Q0 saturation equation, it is equivalently

```text
x0+x1+x2+x3 == 0 mod 4.                       (X0b)
```

For `Q1`, the eight nodes are

```text
P8,P9,P10,P11,P32,P33,P34,P35,
```

with the first four in one torsion half and the last four in the other; `P35` is omitted. Therefore

```text
b32+b33+b34 == 0 mod 2,                        (B1)
```

i.e.

```text
x32+x33+x34 == 0 mod 4,                        (X1a)
```

and, using Q1 saturation, equivalently

```text
x8+x9+x10+x11 == 0 mod 4.                     (X1b)
```

## 5. Rank and relation to older parity conditions

Modulo two in the `b_j` variables, the two saturation rows are

```text
b0+b1+b2+b3+b24+b25+b26=0,
b8+b9+b10+b11+b32+b33+b34=0.
```

The two new torsion rows are

```text
b24+b25+b26=0,
b32+b33+b34=0.
```

These four rows have rank four over `F2`; hence the zero-quartic torsion test contributes **two independent new bits** beyond the two centered saturation equations.

The previously retained determinant passport only gave

```text
x0+x1+x2+x3 == 0 mod 2,
x8+x9+x10+x11 == 0 mod 2,
```

which are automatic after the exact Picard64 result `x_j even`. The present conditions strengthen those statements to mod four and are not automatic from all-even parity.

The balanced allocation

```text
x_j=4l
```

satisfies both new congruences, so this refinement does not close `e=2`.

## Route consequence

The unresolved branch allocation now satisfies, in addition to the exact integer saturation and all-even Picard64 conditions, two source-locked zero-quartic 2-torsion congruences:

```text
x0+x1+x2+x3 == 0 mod 4,
x8+x9+x10+x11 == 0 mod 4.
```

These conditions act on the same residual simultaneous-sign allocation that controls the conductor gluing character. They should therefore be included in any future thin-shell or conductor-preimage evaluation.

## Firewalls

- The 2-torsion conclusion inherits the candidate status of the ambient-H1 linearization used by the half-hyperplane factorization.
- Componentwise split over `Q0,Q1` is not promoted to a global same-sheet choice on their two-point union.
- No claim is made that an arbitrary allocation satisfying these congruences globalizes to a curve.
- No individual conductor pair is assigned a residual sign.
- No weighted-cut upper bound is proved.
- The balanced allocation remains admissible.
- `e=2`, `e=4`, `000707000f0f`, MB104, span5, finite-window, receiver, effectivity, theorem, endpoint and Perfect-Cuboid credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
