# Stage13-13fg — result

Gate G expands the fixed inert-prime overlap transfer that R04 compressed too aggressively.

The repair separates two logically different operations:

1. p-adic divisibility strata use the exact inert states `U`, `R_b`, `S_c`;
2. unit residue predicates use finite character orthogonality and CRT for a fixed finite prime set `S`.

For every inert odd prime,

\[
\lambda_p=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1},
\]

so `lambda_p<=3/4` for every inert `p>=7`.

The character expansion is grouped by **induced pole behavior**, not by a potentially unsafe shorthand requiring every auxiliary character symbol to be literally trivial. The principal pole sector consists of all tuples whose induced characters on every pole-producing multiplicative channel are principal. This includes any harmless auxiliary-character aliasing caused by algebraic relations among coordinates.

Finite Fourier inversion over that entire sector gives the exact leading multiplier

\[
\prod_{p\in S}\lambda_p.
\]

Every tuple outside the principal pole sector makes at least one pole-producing channel nonprincipal. Gate F then replaces that pole by a fixed-conductor Dirichlet/Gaussian-Hecke factor holomorphic at `s=1`. Gate B's phase-uniform Wiener control keeps the mixed split-prime correction holomorphic, so it cannot restore the lost pole. Thus all pole-losing sectors together are

\[
o_S(B(\log B)^3).
\]

Therefore, for fixed `S`,

\[
A^{tag}_{q,S}(B)
=
2D_q\left(\prod_{p\in S}\lambda_p\right)B(\log B)^3
+o_S(B(\log B)^3).
\]

The quantifier order is

```text
fix S
-> B -> infinity
-> enlarge S.
```

No modulus depends on `B`. Choosing `k` inert primes `p>=7` and only then letting `k->infinity` after the `B`-limsup gives

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3).
\]

No perfect-cuboid nonexistence assumption is used.

The deterministic audit independently enumerates unit-state acceptance for `p=7,11,19,23`, verifies `(p+1)^2/2`, `alpha_p`, the exact `lambda_p`, the sample product bound, and the proof-interface locks. These finite checks are reproducibility evidence only; the symbolic transfer in `fixed-inert-transfer.md` is authoritative.

```text
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
INERT_LAMBDA=(p+5)/(2(p+1))
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
AUXILIARY_CHARACTER_ALIASING_INCLUDED=true
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
PAIR_OVERLAP=o(B(log B)^3)
TRIPLE_OVERLAP=o(B(log B)^3)
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fh
```
