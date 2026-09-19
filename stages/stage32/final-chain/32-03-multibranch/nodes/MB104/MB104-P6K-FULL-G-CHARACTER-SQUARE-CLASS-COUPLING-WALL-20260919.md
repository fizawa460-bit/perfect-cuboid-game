# MB104 P6K — full-G character square-class coupling wall — 2026-09-19

Status: **PRE-AUDIT EXACT FUNCTION-FIELD REFORMULATION / NO NEW OBSTRUCTION / NO CREDIT**

## Target

P6H reconstructs the same connected character-labelled `G ~= (Z/2)^3` cover
`Z -> E` from both factor maps
`psi_i:E -> C8/G ~= P1`.
For the three basis characters, choose rational branch functions `q_j` on `P1`
whose odd divisor is the corresponding pair of branch values.

The quadratic character subextension obtained from factor `i` is

```text
k(E)( sqrt(q_j o psi_i) ).
```

Because the two reconstructions are the same labelled quadratic subextension of
`k(Z)/k(E)`, Kummer theory gives exactly

```text
(q_j o psi_1)/(q_j o psi_2) in k(E)^{*2},  j=1,2,3.
```

This is equality of square classes, not equality of rational functions.

## Divisor consequence

Write `D_(i,j)=psi_i^*(branch-pair_j)`.  Since local indices over the six modular
branch values are only 1 or 2, each pullback splits as

```text
D_(i,j) = U_j + 2 R_(i,j),
```

where `U_j` is the branch divisor on `E` of the intrinsic quadratic character
subcover and `R_(i,j)` is the reduced ramification divisor of `psi_i` over that
branch pair.

The same labelled quadratic subextension has the same actual branch divisor
`U_j` for both reconstructions.  Taking divisors of the square-class equality gives

```text
D_(1,j)-D_(2,j)=2 div(r_j)
```

for some `r_j in k(E)^*`.  Cancelling the common `U_j` yields

```text
R_(1,j)-R_(2,j)=div(r_j).
```

Thus

```text
O_E(R_(1,j)) ~= O_E(R_(2,j)),
```

which is exactly the typewise ramification line-bundle equality already retained in P6H.

## Disposition

The three square-class equalities are exact, but they are the function-field/Kummer
encoding of the same intrinsic character-subcover statement already used by P6H.
They do not add an independent Abel--Jacobi condition.

Multiplying the three equations or changing the branch functions `q_j` only changes
the chosen Kummer representatives by squares and does not create a fourth independent
constraint.

Therefore P6K is closed as a **tautological reformulation wall**.  It gives no finite
degree window and no carrier exclusion.

## Next route

The next route must use information not already contained in the common full-G cover.
A shallow high-level candidate is a low-genus curve inequality on the resolved cuboid
surface itself:

```text
MB104-P6L-LOW-GENUS-MIYAOKA-BOGOMOLOV-PREFLIGHT
```

Target: test whether a source-complete Miyaoka/Bogomolov-type inequality for integral
genus-one curves on this exact surface can bound `K_S.C=112l` (or exclude the hostile
ray) without assuming the Bombieri--Lang conjecture.  Stop immediately if the available
theorems require hypotheses not verified for this surface or only give inequalities
compatible with unbounded `l`.

## Source locks

- P6H note blob `cbc8307689ae91b08f547fe1c69606086d06dec1`;
- P6H certificate blob `5c9b3eafed5e55d0a360870722cea7ea81758745`;
- P6J certificate blob `8ff1c1138aec6e0d936effda8ff605180c8ec860`.

## Firewalls

```text
square_class_equalities_exact=true
new_Abel_Jacobi_obstruction=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
