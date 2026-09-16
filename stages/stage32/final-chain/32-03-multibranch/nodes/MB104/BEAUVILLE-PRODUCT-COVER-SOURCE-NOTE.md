# Stage32 MB104 source note — Beauville product cover

Status: **EXTERNAL PUBLISHED SOURCE ADAPTER / NO CLOSURE / NO CREDIT**

## Source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), arXiv:1303.6495, especially Sections 2 and 4.

Only the following published facts are imported by this adapter.

1. The compact modular curve

```text
C8 = H*/Gamma[8]
```

has genus `5`.

2. The subgroup `Gamma'[4]` contains `Gamma[8]` and

```text
Gamma'[4]/Gamma[8] ~= (Z/2Z)^2.
```

This quotient acts freely on `C8`.

3. The Beauville manifold is

```text
X = (C8 x C8)/(Gamma'[4]/Gamma[8])
```

for the diagonal action, and `X -> B` is the canonical degree-two cover of the box variety.

Consequently the quotient map

```text
P := C8 x C8 -> X
```

is a finite etale Galois cover of degree `4`.

4. For the product surface `P=C8 x C8`,

```text
K_P = pr1^* K_C8 + pr2^* K_C8,
deg K_C8 = 2*5-2 = 8.
```

The last line is standard product-curve geometry once genus `5` is imported.

## Scope firewall

This note does not classify curves in `P`, does not classify etale correspondences on `C8`, and does not assert that any formal MB104 packet globalizes. It only supplies the fixed product-cover geometry needed by the equality-rigidity adapter.
