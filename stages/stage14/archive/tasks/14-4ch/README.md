# Stage14-4ch

Stage14-4ch consumes merged 4cg and s7-21.

For fixed balanced eight cells and fixed common-core residual triple `(C,u,v)`, the exact factor products

```text
xi*(C*u)=H_k^+ H_k^-,
k *(C*v)=H_xi^+ H_xi^-
```

have only divisor-many factor pairs. Each valid pair uniquely recovers

```text
r1*r2, s1*s2, x1*x2, y1*y2,
```

and splitting those four products into the two states again costs only divisor functions. Therefore the physical lift multiplicity is `B^o(1)`.

The eight cells cannot yet be dropped: the same `(C,u,v)` can occur for different cell packets. The remaining receiver is

```text
CommonCoreResidualEightCellMultiplicity.
```

Residual triples themselves have support at most `B^(5/8+o(1))`; a `B^o(1)` cell multiplicity theorem would therefore imply a `5/8` endpoint count, but that theorem is not claimed here.

Current whole-family exponent remains `7/8`.

```text
MAINLINE_H_NEEDED=false
NEXT=Stage14-4ci
```
