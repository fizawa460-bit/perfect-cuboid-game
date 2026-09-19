# MB104 P6K — full-G character square-class coupling — 2026-09-19

Status: **PRE-AUDIT EXACT COMMON-COVER SQUARE-CLASS REDUCTION / TAUTOLOGICAL WALL / NO CREDIT**

## Target

P6H and P6J leave the same exact full-deck geometry:

```text
G ~= (Z/2)^3,
Z/G = E,
psi_i:E -> C8/G ~= P1,
Z = Norm(E x_(psi_i,P1) C8),  i=1,2.
```

For each of the three weight-one characters `chi_j`, let

```text
C_j := C8/ker(chi_j) -> P1
```

be the corresponding quadratic subcover. Choose any square-class representative

```text
q_j in k(P1)^*/k(P1)^{*2}
```

for that subcover. Its odd divisor is exactly the pair of branch values of inertia type `j`.

## 1. Same character subcover gives exact square-class equality

Pulling `C_j` back through either factor map and normalizing gives the same intrinsic character-labelled quadratic subextension

```text
Z/ker(chi_j) -> E.
```

Therefore the two Kummer classes in `k(E)^*/k(E)^{*2}` are equal:

```text
[q_j(psi_1)] = [q_j(psi_2)].
```

Equivalently, for each `j=1,2,3` there is some `h_j in k(E)^*` with

```text
q_j(psi_1) / q_j(psi_2) = h_j^2.                 (SC_j)
```

No equality of rational functions is asserted before quotienting by squares.

## 2. Exact equality of the reduced unramified type divisors

Let `B_j` be the two branch values of `C_j -> P1`. For factor `i`, let

```text
U_(i,j)
```

be the reduced divisor of points `p in E` such that

- `psi_i(p) in B_j`, and
- `psi_i` is unramified at `p`.

At a point over `B_j`, the valuation of `q_j(psi_i)` is odd exactly when the local degree of `psi_i` is one; simple ramification contributes an even valuation. Hence the parity divisor of `q_j(psi_i)` is exactly `U_(i,j)`.

Taking parity divisors in `(SC_j)` gives the stronger pointwise statement

```text
U_(1,j) = U_(2,j)                                  (U_j)
```

as actual reduced divisors on `E`, not merely as linearly equivalent divisor classes.

P6D2 exhausts the unramified capacity by the supported odd/minimal branches, so their degrees are

```text
deg U_1 = 48l,
deg U_2 = 16l,
deg U_3 = 48l.
```

Thus the inertia type of every branch point of the intrinsic full-`G` cover `Z->E` is factor-independent.

## 3. Relation to P6H

P6H retained

```text
M_1 ~= M_2
```

and typewise linear equivalence of the ramification divisors. P6K records the function-field refinement supplied by the full common cover:

```text
same character quadratic extension
  => same Kummer square class
  => same reduced unramified type divisor.
```

This is more explicit than the P6H line-bundle statement. However it is not an independent obstruction: every pair of factor maps that really comes from the same labelled full-`G` cover already satisfies `(SC_j)` and `(U_j)` automatically.

Therefore P6K does not reduce the common-cover moduli by itself.

## 4. Where the packet-sensitive information still lives

For each inertia type, `B_j` contains two distinct branch values. P6K forgets which of those two values each point of the common divisor `U_j` lands on in factor 1 and in factor 2.

That missing binary split is exactly where the box-node support can enter: a supported box node records a pair of fixed-point orbits in the two factors and therefore a pair of branch values inside one inertia type.

The next useful invariant is the typewise `2 x 2` branch-value incidence matrix:

```text
N_j(alpha,beta)
 = number / divisor mass of common U_j-points
   with psi_1-value alpha and psi_2-value beta,
alpha,beta in B_j.
```

The hostile support is finite and exact, so this matrix should be derived from the retained 48-node model rather than guessed from the pair totals.

Next leaf:

```text
MB104-P6L-FULL-G-BRANCH-VALUE-PAIR-INCIDENCE
```

Success would be a packet-specific row/column or diagonal/off-diagonal restriction not already present in the scalar passport.

## Source locks

Current compact branch:

- P6H note blob `cbc8307689ae91b08f547fe1c69606086d06dec1`;
- P6H certificate blob `5c9b3eafed5e55d0a360870722cea7ea81758745`;
- P6J certificate blob `8ff1c1138aec6e0d936effda8ff605180c8ec860`.

No historical e=2 conductor-square class is imported.

## Firewalls

```text
square_class_equalities_proved=true
typewise_unramified_divisors_equal=true
factor_pencils_equal=false
packet_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
