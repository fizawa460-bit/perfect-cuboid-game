# Stage32 MB104 — H5 arithmetic self-correspondence source note — 2026-09-18

Status: **EXTERNAL-SOURCE ADAPTER / NEGATIVE FINITENESS INPUT / NO MB104 CREDIT**

## Purpose

H5 asks whether the fixed genus-five factor

```
C8 = X(8)
```

has only finitely many, or effectively bounded, finite etale self-correspondences once the MB104 quotient symmetry is imposed.

This note records one obstruction to any finiteness claim that comes only from the ambient curve.

## 1. X(8) is the Wiman genus-five curve

F. Bars, A. Kontogeorgis, and X. Xarles, in their work on modular curves and automorphisms, identify `X(8)` over `C` with the Wiman genus-five curve and record its automorphism group of order `192`.

A convenient accessible copy is:
https://www.impan.pl/shop/en/publication/transaction/download/product/82331

The retained Stage32 factor `C8=H*/Gamma[8]` is this compact modular curve.

## 2. The full automorphism quotient has signature (2,3,8)

David Swinarski, *Equations of Riemann surfaces with automorphisms* (arXiv:1607.04778), lists the genus-five Wiman curve as the locus with automorphism group `(192,181)` and signature

```
(2,3,8).
```

Source:
https://arxiv.org/abs/1607.04778

Thus if `Gamma_C < PSL_2(R)` is the torsion-free cocompact group uniformizing the compact curve `C8`, then `Gamma_C` has finite index in the triangle group `Delta(2,3,8)`.

## 3. Delta(2,3,8) is arithmetic

K. Takeuchi, *Arithmetic triangle groups*, J. Math. Soc. Japan 29 (1977), 91--106, gives the complete list of arithmetic triangle groups. The type `(2,3,8)` occurs in that list.

DOI:
https://doi.org/10.2969/jmsj/02910091

Arithmeticity is invariant under passage to finite-index subgroups. Hence the compact surface group `Gamma_C` uniformizing `C8` is arithmetic.

## 4. Consequence for finite etale self-correspondences

For a lattice `Gamma_C < PSL_2(R)`, an element

```
g in Comm(Gamma_C)
```

defines a finite holomorphic self-correspondence by the common finite-index subgroup

```
Lambda_g = Gamma_C cap g Gamma_C g^{-1}.
```

The compact curve `H/Lambda_g` has two finite etale maps to `H/Gamma_C=C8`, one induced by inclusion and one by `g`.

The commensurator theorem says that an arithmetic lattice has dense commensurator in `PSL_2(R)`. For a reference formulation see, for example, the discussion of the Margulis commensurator theorem in the arithmetic-lattice literature; a modern accessible statement is:
https://www.math.ucdavis.edu/~kapovich/EPR/com.pdf

Biswas--Nag explicitly organize these objects as the commensurability automorphism group of a compact Riemann surface, whose elements are finite holomorphic self-correspondences:
I. Biswas and S. Nag, *Commensurability automorphism groups and infinite constructions in Teichmuller theory*, C. R. Acad. Sci. Paris 327 (1998), 35--40.

Therefore the fixed ambient curve `C8` does **not** have a finite universe of finite etale self-correspondences.

Moreover the correspondence degrees cannot be bounded. Indeed a finitely generated group has only finitely many subgroups of index at most `N`; a uniform degree bound would therefore leave only finitely many common finite-index subgroups/double-coset correspondences, contradicting the infinite arithmetic commensurator quotient.

## Scope firewall

This note does **not** prove that infinitely many of these ambient correspondences satisfy the exact MB104 support passport, diagonal `H`/`G` equivariance, or genus-one quotient condition.

Its use is narrower:

```
fixed target C8
+ etaleness
+ equal bidegree
```

cannot by itself yield a finite or bounded classification.

Any H5 success must therefore get its finiteness from the exact MB104 quotient/passport data. That makes the packet-to-correspondence F/R adapter load-bearing.
