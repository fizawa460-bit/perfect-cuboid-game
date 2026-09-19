# MB104 P6H — full-G two-factor character-line coupling — 2026-09-19

Status: **PRE-AUDIT EXACT TWO-FACTOR COMMON-COVER REDUCTION / NO CREDIT**

## Target

P6G proves that the necessary one-factor six-value Hurwitz passport is abstractly realizable for every `l`. The next invariant must use that the two factor maps come from the **same** connected `G`-stable curve

```text
Z subset C8 x C8,
G ~= (Z/2)^3,
Z/G = E,
f_i:Z -> C8 etale of degree 56l,
psi_i:E -> C8/G ~= P1 of degree 56l.
```

P6D2 makes this package necessary for any hypothetical genus-one carrier on the hostile ray.

## 1. Full-G branch characters

The quotient

```text
pi:C8 -> C8/G ~= P1
```

has six order-two branch values, two for each of the three distinct singular inertia generators

```text
s1,s2,s3 in G.
```

P6D2 records that the three generators occur and generate all of `G`.

For a nontrivial character

```text
chi:G->{+1,-1},
```

let `w(chi)` be the number of `s_j` on which `chi` is nontrivial. Since `s1,s2,s3` form a basis of `G`,

```text
w(chi) in {1,2,3}.
```

The quadratic subcover `C8/ker(chi) -> P1` is branched at exactly `2w(chi)` of the six values. Its square-root building line on `P1` is therefore

```text
L_chi ~= O_P1(w(chi)).
```

This recovers the holomorphic character multiplicity pattern `0,0,0,1,1,1,2` by `h^0(K_P1 tensor L_chi)=max(w-1,0)`, but only the building-line degree is needed below.

## 2. Each factor reconstructs the same G-cover

Because `Z` is `G`-stable and `Z/G=E`, each `G`-equivariant factor projection descends to

```text
psi_i:E -> P1.
```

Generically both `Z->E` and the base change `E x_P1 C8 -> E` have degree eight. Normality and connectedness give

```text
Z = Norm(E x_(psi_i,P1,pi) C8)
```

for `i=1,2`.

Etaleness of `f_i:Z->C8` forces `psi_i` to be unramified away from the six branch values and to have only local indices `1` or `2` over them.

Put

```text
M_i := psi_i^* O_P1(1),
deg M_i = 56l.
```

## 3. Intrinsic character eigensheaves

For a character `chi` of weight `w`, let `R_(i,chi)` be the reduced divisor of simple ramification points of `psi_i` lying above the `2w` branch values seen by `chi`.

Normalize the pulled-back quadratic subcover. The doubled zeros at `R_(i,chi)` are removed, so its character building line on `E` is

```text
N_(i,chi)
  = M_i^w tensor O_E(-R_(i,chi)),
N_(i,chi)^2 ~= O_E(U_chi),
```

where `U_chi` is the branch divisor on `E` of the corresponding character subcover.

But the two factor constructions recover the same character-labelled `G`-cover `Z->E`. Hence the eigensheaf is intrinsic:

```text
N_(1,chi) ~= N_(2,chi)
```

for every character `chi`.

## 4. The weight-three character kills the factor-line ambiguity

Let `chi_all` be the unique character with

```text
w(chi_all)=3.
```

It sees all six branch values, so

```text
R_(i,chi_all) = Ram(psi_i).
```

Riemann--Hurwitz on the elliptic curve `E` gives the line-bundle identity

```text
O_E(Ram(psi_i))
 ~= K_E tensor psi_i^* K_P1^(-1)
 ~= M_i^2.
```

Therefore

```text
N_(i,chi_all)
 = M_i^3 tensor O(-Ram(psi_i))
 ~= M_i.
```

Since the `chi_all` eigensheaf is the same for both reconstructions,

```text
M_1 ~= M_2.                                    (FULL-G-LINE)
```

This is stronger than the archived `e=2` common-`H` result, which could reduce the factor-line difference only to a 2-torsion class. The full-deck `e=4` geometry supplies the weight-three character and removes that ambiguity.

## 5. Typewise ramification divisors match linearly

For each inertia type `j`, take the weight-one character `chi_j` which is nontrivial only on `s_j`. Let

```text
R_(i,j)
```

be the ramification divisor of `psi_i` over the two branch values of type `j`.

Then

```text
N_(i,chi_j)=M_i tensor O(-R_(i,j)).
```

Using `(FULL-G-LINE)` and the intrinsic equality of `N_(i,chi_j)` gives

```text
O_E(R_(1,j)) ~= O_E(R_(2,j)),   j=1,2,3.       (TYPE-RAM)
```

The P6D2 pair totals give the degrees

```text
deg R_(i,1)=32l,
deg R_(i,2)=48l,
deg R_(i,3)=32l.
```

The corresponding intrinsic branch divisors of `Z->E` have degrees

```text
48l, 16l, 48l.
```

## 6. What this does and does not prove

The two factor maps are no longer independent scalar Hurwitz covers. They are pencils in the **same degree-56l line bundle** on the elliptic normalization, and their ramification divisors match in `Pic(E)` separately for all three modular inertia types.

This is a genuine P6 two-factor adapter. It does not use the support-specific `000707/e=2` conductor pair map, residual sheet character, or its long downstream chain.

It is not yet a contradiction. Two distinct pencils inside `H^0(E,M)` can share the same line bundle and satisfy typewise divisor-class constraints.

## 7. Next gate

The next useful invariant must distinguish the two pencils inside the common line bundle `M`. Equivalent useful forms include:

```text
- an Abel--Jacobi constraint on the actual typewise ramification divisors,
- a square-class relation comparing the three type polynomials under psi_1 and psi_2,
- a full-G product-correspondence/Jacobian centralizer constraint valid for e=4,
- an exact classification showing that the only compatible pencil pairs come from forbidden diagonal/modular automorphisms.
```

Do not return to one-factor passport counts; P6G already constructs them for every `l`.

## Source locks

Current compact prerequisites:

- P6D2 certificate blob `3924212bb64e2f377dc8be2311ed6e15ba764cbf`;
- P6G certificate blob `0139b814d2cfdb18e3a066903ae3b8a626bff9c3`.

Historical analogy only, not a semantic dependency: the `000707/e=2` common-H factor-line method. No e=2 conclusion is imported into the e=4 proof.

## Firewalls

```text
M1_isomorphic_M2=true
typewise_ramification_linear_equivalence=true
pencils_equal=false
cuboid_carrier_exists=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
