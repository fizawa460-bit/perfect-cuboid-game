# Stage32 MB104 — `000707000f0f` e=2 half-hyperplane factorization

Status: **RETAINED CONDITIONAL CONSEQUENCE OF EXACT PICARD64 PARITY PLUS CANDIDATE AMBIENT H1 LINEARIZATION / EFFECTIVE CONJUGATE HALF-HYPERPLANE DIVISORS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the exact Picard64 consequence

```text
x_j=2*y_j
```

and the retained candidate ambient-H1 linear equivalence

```text
(C_1-C_2) ~ -sum_j (d_j/2)F_j,
F_j=E_j^+-E_j^-,
d_j=2*x_j-8*l.
```

The parity input makes all coefficients below integral. The linear-equivalence conclusions remain conditional on the already-retained candidate ambient-H1 leaf.

## 1. Two effective conjugate integral divisors

Since `0<=x_j<=8l`,

```text
0<=y_j<=4l.
```

Define effective divisors on the smooth residual double-cover model `pi:Y->S` by

```text
G_1
 := C_1
    +sum_j [ y_j E_j^+ +(4*l-y_j)E_j^- ],

G_2
 := C_2
    +sum_j [ (4*l-y_j)E_j^+ +y_j E_j^- ].      (G12)
```

The deck involution exchanges them:

```text
tau(G_1)=G_2.
```

Their difference is

```text
G_1-G_2
 =(C_1-C_2)
  +sum_j (2*y_j-4*l)(E_j^+-E_j^-)
 =(C_1-C_2)+sum_j(d_j/2)F_j.
```

Therefore the retained candidate ambient-H1 relation gives

```text
G_1 ~ G_2.                                     (GEQ)
```

This is stronger than merely saying that a formal half-class exists: both representatives are effective and are exchanged by the residual deck involution.

## 2. Their sum forgets the branch allocation completely

The preimage of a supported exceptional curve splits as

```text
pi^*E_j=E_j^++E_j^-.
```

Also the e=2 split cover satisfies

```text
pi^*C=C_1+C_2,
```

where the hypothetical carrier has class

```text
[C]=D_l=7*l*H-4*l*sum_supported E_j.
```

Adding the two divisors in `(G12)` gives coefficient `4l` on both lifts of every supported exceptional. Hence

```text
G_1+G_2
 =pi^*(C+4*l*sum_supported E_j)
 ~pi^*(7*l*H).                                 (SUM)
```

Combining `(GEQ)` and `(SUM)`,

```text
2*G_1 ~ pi^*(7*l*H),
2*G_2 ~ pi^*(7*l*H).                           (HALF-H)
```

Thus every e=2 realization satisfying the retained candidate linearization produces **effective conjugate square roots of the fixed pullback hyperplane class `pi^*(7lH)`**. The allocation variables disappear from the doubled line-bundle class.

## 3. Uniqueness from the retained Picard-torsion kill

The same ambient-H1 leaf gives

```text
Pic^tau(Y)=0,
```

in particular no nontrivial two-torsion in `Pic(Y)`.

If `L` and `L'` are two line bundles satisfying

```text
L^2 ~= (L')^2 ~= pi^*O_S(7*l*H),
```

then `(L tensor (L')^-1)^2` is trivial, so torsion-freeness forces

```text
L~=L'.
```

Therefore the half-hyperplane line bundle in `(HALF-H)` is unique whenever the candidate ambient-H1 input is accepted:

```text
O_Y(G_1) ~= O_Y(G_2) =: Lambda_l.              (UNIQUE)
```

The branch allocation changes the effective representative inside `|Lambda_l|`, not the line-bundle class itself.

## 4. Even-l specialization is a pure pullback

If

```text
l=2*m,
```

then the obvious pullback line bundle

```text
pi^*O_S(7*m*H)
```

also squares to `pi^*O_S(7*l*H)`. By uniqueness,

```text
Lambda_(2m) ~= pi^*O_S(7*m*H).                 (EVEN-PULLBACK)
```

Since `G_1` and `G_2=tau(G_1)` are distinct effective divisors in this same pullback linear system, a defining section of `G_1` is not a pure `+` or pure `-` deck eigenvector: otherwise its zero divisor would be deck-invariant.

Let `L_abs` be the retained branch half-line of the residual double cover, so

```text
pi_*O_Y ~= O_S direct_sum L_abs^(-1).
```

Projection formula then gives the necessary even-l eigensection condition

```text
H^0(S,O_S(7*m*H)) != 0,
H^0(S,O_S(7*m*H) tensor L_abs^(-1)) != 0.      (EIG-EFF)
```

The first space is expected from the hyperplane system; the second is an additional effectivity target. No vanishing or nonvanishing theorem for the second space is asserted here.

## 5. Odd-l primitive-root formulation

For odd `l`, choose integers `u,v` with

```text
u*l+2*v=1.
```

In additive Picard notation define

```text
Lambda_* := u*Lambda_l + 7*v*pi^*H.
```

Using `2*Lambda_l=7*l*pi^*H` gives

```text
2*Lambda_* = 7*pi^*H.                          (PRIMITIVE-HALF)
```

Torsion-freeness then gives back

```text
Lambda_l = l*Lambda_*.
```

Thus any odd-l e=2 realization on this fixed residual surface lies in a multiple of one primitive half-hyperplane class. This does not prove that the required effective divisor exists; it only normalizes the line-bundle problem.

The exact Picard64 parity result already shows why such a ramified half-class is not ruled out merely modulo two: the hyperplane class maps into the absent exceptional span in the relevant quotient.

## 6. Relation to the Cartier pencil and the active conductor problem

The previous Cartier refinement shows that the intermediate `Gamma,tau Gamma` are honest Cartier members. The present construction is the smooth-model form of the same phenomenon: the two effective divisors `G_1,G_2` lie in the unique line bundle `Lambda_l` and are exchanged by `tau`.

Their two-dimensional span has invariant and anti-invariant eigen-sections. On the function-field side, the ratio of those eigen-sections is a `tau`-anti-invariant generator and hence differs from the explicit retained Kummer generator `r_z` (or `r_w`) by an invariant factor in `k(B)^*`.

A concrete continuation is therefore:

1. determine the downstairs eigensection classes/vanishing along the supported exceptionals;
2. identify the invariant multiplier relating the pencil generator to `r_z`;
3. specialize that relation on conductor normalization preimages.

This is closer to the active missing residual-sheet map than repeating Picard divisibility.

## Firewalls

- `(GEQ)`, `(HALF-H)`, uniqueness, and the eigensection conclusions inherit the candidate status of the ambient-H1/torsion-kill leaf.
- Exact Picard64 parity alone does not prove `(GEQ)`.
- No claim is made that the second eigensection space in `(EIG-EFF)` vanishes or is nonzero independently of a hypothetical e=2 realization.
- No individual conductor pair is assigned a residual sign.
- No weighted-cut upper bound is proved.
- The balanced allocation remains formally possible.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
