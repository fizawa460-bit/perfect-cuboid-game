# Stage32 MB104 — `000707000f0f` e=2 Rosati zero-correspondence constraint

Status: **RETAINED CANDIDATE CONSEQUENCE OF THE PRODUCT-CORRESPONDENCE LINEARIZATION / `Phi_Z=0` / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

This note consumes the retained candidate product-correspondence linearization for the same support and e=2 branch. In that candidate boundary the product-surface image

```text
Zbar subset P=C8 x C8
```

has both projection degrees

```text
n=28l,
```

self-intersection

```text
Zbar^2=1568l^2,
```

and induces the Jacobian correspondence

```text
Phi_Z=(f_2)_* f_1^*: J(C8)->J(C8).
```

The purpose here is to use the full intersection pairing on a product of curves, rather than only the previously retained full-`G` centralizer statement.

## 1. Product-correspondence intersection identity

Let `C` be a smooth projective complex curve and let `D` be a divisor on `C x C` with bidegrees `(d_1,d_2)`. Let

```text
Phi_D:J(C)->J(C)
```

be the homomorphism induced by the correspondence `D`, and let `Phi_D^dagger` denote its Rosati adjoint for the canonical principal polarization.

The Neron-Severi/Kunneth decomposition separates the two fiber-degree directions from the `H^1(C) tensor H^1(C)` correspondence component. With the usual normalization one has

```text
D^2 = 2 d_1 d_2 - Tr_H1(Phi_D Phi_D^dagger).    (ROSATI-INT)
```

The normalization is checked by the diagonal: for `D=Delta`, `d_1=d_2=1`, `Phi_D=id`, and

```text
Delta^2=2-(2g)=2-2g.
```

Rosati positivity gives

```text
Tr_H1(Phi Phi^dagger) >= 0,
```

with equality if and only if `Phi=0`.

This is the only general correspondence fact used below.

## 2. The retained e=2 numbers saturate the Rosati bound

For the retained product image `Zbar`, both bidegrees are `n=28l`. Hence

```text
2 n^2 = 2(28l)^2 = 1568l^2.
```

But the retained self-intersection is exactly

```text
Zbar^2=1568l^2.
```

Substituting into `(ROSATI-INT)` gives

```text
Tr_H1(Phi_Z Phi_Z^dagger)
 = 2(28l)^2-Zbar^2
 = 1568l^2-1568l^2
 = 0.
```

Therefore Rosati positivity forces

```text
Phi_Z=0.                                             (ZERO)
```

Equivalently, the `H^1 tensor H^1` / `Hom(J(C8),J(C8))` component of the Neron-Severi class of `Zbar` vanishes.

## 3. Consequence for the previous full-G centralizer route

The previous retained note proved, conditionally on the ambient torsion-kill chain, that

```text
Phi_Z in End(J(C8))^G.
```

`(ZERO)` is strictly more specific:

```text
Phi_Z=0 in End(J(C8))^G.
```

Thus an exact decomposition of the full-`G` centralizer is no longer needed merely to determine which centralizer element the candidate correspondence occupies: it occupies the zero element.

This does **not** rule out the geometric correspondence. A singular irreducible curve on `C8 x C8` can have nonzero bidegrees while its induced Jacobian correspondence is zero; the large retained normalization defect

```text
delta(Zbar)=784l^2+112l
```

is compatible with the fact that `Zbar` is very far from a smooth graph.

## 4. Refined next target

Because the homomorphism component is zero, any remaining obstruction must live beyond that component. Two concrete continuations are now sharper than an unrestricted endomorphism-ring search:

1. determine the factor line-bundle/orbifold-descent part of `O_P(Zbar)` once its correspondence component is zero, and test compatibility with the diagonal `H` stabilizer plus `Zbar~Tdiag(Zbar)`;
2. classify or obstruct degree-`28l` common etale covers `f_1,f_2:Z->C8` whose trace correspondence `(f_2)_*f_1^*` is zero and whose product image has the retained `000707` support passport.

The original conductor-preimage residual-sheet map remains an admissible direct route. This note does not assign any conductor pair a sign.

## Firewalls

- This note inherits every candidate/audit dependency of the retained product-correspondence linearization.
- `Phi_Z=0` is a constraint on the induced Jacobian homomorphism, not a statement that `Zbar` is linearly equivalent to zero.
- No claim that a zero Jacobian correspondence is geometrically impossible.
- No conductor sign or weighted opposite-sheet bound is computed.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
