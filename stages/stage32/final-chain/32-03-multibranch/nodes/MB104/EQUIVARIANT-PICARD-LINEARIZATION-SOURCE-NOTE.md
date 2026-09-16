# Stage32 MB104 source note — equivariant Picard linearization obstruction

Status: **EXTERNAL STANDARD-THEOREM ADAPTER / NO MB104 CREDIT BY ITSELF**

## Purpose

The active `000707`, `e=2` product-correspondence leaf distinguishes two notions for a finite group `G` acting on a smooth projective curve `C`:

```text
G-invariant line-bundle class,
G-linearized line bundle.
```

The finite reduction below needs the standard obstruction map between them and the divisor interpretation of its kernel.

## 1. Equivariant Picard exact sequence

For a finite group `G` acting on a smooth projective complex variety `X`, let

```text
Pic^G(X)
```

denote the group of `G`-linearized line bundles and `Pic(X)^G` the invariant subgroup of the ordinary Picard group.  There is a standard exact sequence

```text
0 -> Hom(G,C^*)
  -> Pic^G(X)
  -> Pic(X)^G
  -> H^2(G,C^*).
```

Thus an invariant line-bundle class has an obstruction

```text
obs_G(L) in H^2(G,C^*)
```

and is `G`-linearizable exactly when this obstruction vanishes.

Source:

- Christian Böhning et al., *Equivariant birational types and derived categories*, Mathematische Nachrichten (2024), Section 2.2, which records the longer exact sequence beginning with the four terms above:
  `https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202400006`.

## 2. Divisor description for finite abelian groups

For a finite abelian group acting on a smooth projective complex variety, the image of the forgetful map

```text
Pic^G(X) -> Pic(X)^G
```

is exactly the subgroup represented by `G`-invariant divisors.  Equivalently, the kernel of `obs_G` can be computed from invariant divisors modulo rational equivalence.

Source:

- Sergey Galkin and Evgeny Shinder, *Exceptional collections of line bundles on the Beauville surface*, Advances in Mathematics 244 (2013), 1033–1050, Section 2, especially Lemma 2.1; arXiv `1210.3339`, DOI `10.1016/j.aim.2013.06.007`.

Only this general equivariant-Picard lemma is imported; no Beauville-surface-specific conclusion is used.

## 3. The obstruction group for the active deck group

For the active group

```text
G ~= (Z/2)^3,
```

and trivial coefficient action on `C^*`, the Schur multiplier is

```text
H^2(G,C^*) ~= Hom(ExteriorSquare(G),C^*) ~= (Z/2)^3.
```

One way to see the cardinality is that `C^*` is divisible, so the extension part vanishes and a projective commutator class is an alternating bicharacter.  Such a bicharacter on a three-dimensional `F_2` vector space is determined by its values on the three unordered basis pairs.  Hence

```text
|H^2(G,C^*)|=2^3=8.
```

This is the only group-cohomology cardinality used downstream.

## Firewalls

- This note supplies general external theory only.
- It does not assert that any particular Stage32 invariant class is linearizable.
- It does not assign a conductor sign or a residual `G/H` sheet.
- It grants no MB104, receiver, theorem, endpoint, or Perfect-Cuboid credit.
- No merge authorization.
