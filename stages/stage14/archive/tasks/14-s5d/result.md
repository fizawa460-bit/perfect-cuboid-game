# Stage14-s5d — unselected odd bad-prime rows and 2-adic finite-state reduction

## Purpose

Stage14-s5c derived the exact local rows at odd bad primes selected in the full-2-descent support. This stage closes the complementary **unselected odd bad-prime rows** and reduces the remaining prime-2 problem to an explicit finite squareclass/lifting computation. It does not promote a finite-depth 2-adic search to a theorem without a stabilization proof.

Write

```text
z1=d1*u1^2, z2=d2*u2^2, z3=d3*u3^2,
z1-z2=S^2,
z3-z1=X^2,
z3-z2=H^2,
d1*d2*d3 = square class.
```

At an unselected odd bad prime `p`, all `d_i` are p-adic units.

## Exact unselected odd rows

Let `chi` be the Legendre symbol on p-adic unit parts. Because `d1*d2*d3` is a square class,

```text
chi(d1) chi(d2) chi(d3)=+1.
```

### p | S

Modulo p,

```text
d1*u1^2 = d2*u2^2,
d3*u3^2 - d1*u1^2 = X^2 != 0.
```

If `chi(d1*d2)=-1`, the first equation forces `u1=u2=0 mod p`, and then the second requires `chi(d3)=+1`; by the product-square constraint these two assertions are equivalent. If `chi(d1*d2)=+1`, identify the first two variables and the second equation is a nonsingular binary conic over F_p, hence has an affine point; Hensel lifting applies.

Therefore

```text
p|S, p unselected  <=>  chi(d3)=+1.
```

### p | H

Similarly, modulo p,

```text
d3*u3^2 = d2*u2^2,
d1*u1^2-d2*u2^2 = S^2 != 0,
```

and the product-square constraint gives

```text
p|H, p unselected  <=>  chi(d1)=+1.
```

### p | X

Modulo p,

```text
d3*u3^2=d1*u1^2,
d1*u1^2-d2*u2^2=S^2 != 0.
```

If `chi(d1*d3)=+1`, the first pair can be identified and the remaining binary conic is soluble. If `chi(d1*d3)=-1`, both variables in that equality must vanish modulo p, leaving

```text
-d2*u2^2=S^2,
```

which is soluble iff `chi(-d2)=+1`.

Since `chi(d1*d3)=chi(d2)`, the exact criterion is

```text
p|X, p unselected  <=>  chi(d2)=+1 OR chi(-d2)=+1.
```

Equivalently,

```text
p == 3 mod 4 : automatic;
p == 1 mod 4 : chi(d2)=+1.
```

Thus every odd bad-prime row, selected or unselected, is now an explicit Boolean combination of quadratic-character bits from the s5b reciprocity matrix.

## Prime 2: exact finite-state reduction, not yet a closed theorem table

For primitive opposite-parity Euclid parameters,

```text
S,H odd,
v2(X)>=2.
```

The 2-adic squareclass group has eight classes represented by

```text
1,3,5,7,2,6,10,14
```

(or equivalently `±1,±2,±5,±10`). Together with `d1*d2*d3` square, there are only 64 ordered squareclass triples before the covering equations are imposed. The s5c valuation argument already shows that if 2 is selected, its valuation label is forced to `13`.

After dividing the covering by the odd square `S^2`, write `t=X/S`, so `v2(t)>=2` and

```text
z1-z2=1,
z3-z1=t^2,
z3-z2=1+t^2.
```

Hence the remaining Q2 problem is a finite squareclass/lifting problem indexed by

```text
(d1,d2,d3) in (Q2*/Q2*2)^3,
product square,
selected/unselected 2-state,
k=v2(t)>=2.
```

The accompanying audit implements residue-tree lifting modulo powers of 2 for all 64 squareclass triples and a configurable range of `k`, and records whether branches survive. This is a deterministic diagnostic and a concrete finite-state interface for the next stage.

What is **not** claimed here is that survival to the chosen modulus is equivalent to Q2 solubility uniformly in all `k`. That last implication needs either an explicit Hensel/stabilization lemma for the singular residue branches or a direct Hilbert-symbol derivation. Therefore the full local matrix is complete at every odd prime, while the prime-2 matrix is reduced to a finite exact target but not yet theorem-closed.

## Boundary

```text
STAGE14_S5D=COMPLETE_ODD_LOCAL_MATRIX_AND_Q2_FINITE_STATE_REDUCTION
ODD_UNSELECTED_S_ROW=chi(d3)=+1
ODD_UNSELECTED_X_ROW=chi(d2)=+1_OR_chi(-d2)=+1
ODD_UNSELECTED_H_ROW=chi(d1)=+1
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_SQUARECLASS_STATE_SPACE_SIZE=64
P2_SELECTED_LABEL_FORCED_TO_13=true
P2_FINITE_STATE_LIFTING_INTERFACE_IMPLEMENTED=true
P2_COMPLETE_LOCAL_MATRIX_DERIVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5e close the Q2 stabilization/Hilbert table, then state the full character-sieve system
```
