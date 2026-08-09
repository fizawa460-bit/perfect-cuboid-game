# Stage13-13fg — result

Gate G expands the fixed inert-prime overlap transfer that R04 compressed too aggressively.

The repair separates two logically different operations:

1. p-adic divisibility strata are handled by the exact inert valuation states `U`, `R_b`, `S_c`;
2. unit residue predicates are handled by finite character orthogonality and CRT at a fixed finite prime set `S`.

For every inert odd prime,

\[
\lambda_p=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1},
\]

so `lambda_p<=3/4` for every inert `p>=7`.

For fixed `S`, the simultaneous tagged local test has a finite character expansion. The all-principal tuple preserves the raw pole order and contributes exactly

\[
2D_q\left(\prod_{p\in S}\lambda_p\right)B(\log B)^3.
\]

Every nonprincipal tuple replaces at least one pole-producing principal Dirichlet/Gaussian-Hecke factor by a fixed-conductor factor holomorphic at `s=1`. Gate B phase-uniform Wiener control keeps the mixed split-prime correction holomorphic, so it cannot restore the lost pole. The sum of all nonprincipal tuples is therefore

\[
o_S(B(\log B)^3).
\]

Hence, for fixed `S`,

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

No modulus depends on `B`. Choosing `k` inert primes `p>=7` and then letting `k->infinity` after the `B`-limsup gives

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3).
\]

No perfect-cuboid nonexistence assumption is used.

The deterministic audit independently enumerates the unit-state acceptance for `p=7,11,19,23`, checks `(p+1)^2/2`, `alpha_p`, and the exact `lambda_p`, and locks the principal/nonprincipal and order-of-limits interfaces. These finite checks are reproducibility evidence only; the symbolic character argument in `fixed-inert-transfer.md` is authoritative.

```text
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
INERT_LAMBDA=(p+5)/(2(p+1))
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_TUPLE_MULTIPLIER=product_{p_in_S}_lambda_p
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_TUPLE_POLE_LOSS_AT_LEAST_ONE=true
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
