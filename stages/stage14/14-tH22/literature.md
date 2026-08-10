# Stage14-tH22 literature applicability note — t78 refined

Target:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

No source below is imported as a proof of the Stage14 receiver. The purpose is exact theorem-adapter auditing after t77 produces the projective ray-character kernel and merged t78 proves four-cell Möbius tensorization.

## 1. What merged t78 removes from the external-theorem problem

Merged Stage14-t78 / PR #567 proves internally

```text
M=K_ext/gcd(K_ext,g),
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true,
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true,
ell*g*c = ell*H*R*T.
```

Therefore an external theorem no longer needs to prove algebraic separation of the angular gcd. The remaining questions are:

```text
actual projective/Hecke conductor,
projective-family compression,
divisor-decomposed coefficient L2 norms,
nonprincipal pi x V character moments,
short ellipse / ell*H*R*T / ell*delta localization.
```

## 2. Projective characters and actual conductor

For `chi in dual G(M)`, inflate to a character of `(Z[i]/MZ[i])^x` trivial on rational scalars. After splitting the two possible values of `chi(i)`, the character is a standard Hecke character over `Q(i)`; the `chi(i)=-1` half needs one fixed archimedean type.

For a nontrivial local projective factor at a rational prime `p|M`:

- if `p=3 mod 4`, `(p)` is inert and the local projective quotient is `F_{p^2}^x/F_p^x`;
- if `p=1 mod 4`, the quotient is represented by the ratio on the two split factors, so a nontrivial character depends on both primes above `p`.

Thus if

```text
d_chi=product_{p|M, chi_p nonprincipal} p,
```

then

```text
f_fin(chi)=(d_chi),
N f_fin(chi)=d_chi^2.
```

The family size and the conductor norm must not be confused:

```text
|G(M)|=M*B^o(1),
N f_fin(chi)<=M^2.
```

## 3. Huxley-type large sieve over number fields

M. N. Huxley's large-sieve work over algebraic number fields is the correct ambient paradigm: modulus/conductor ideals are the arithmetic parameter.

Applicability issue here:

- the ambient conductor geometry sees norm up to `M^2`;
- the actual projective subfamily has only `M*B^o(1)` characters;
- no located theorem gives the compressed projective-subfamily moment at the desired `M + N` scale while simultaneously retaining the t78 divisor-decomposed coefficients.

Hence ambient Hecke large sieve is relevant but not directly applicable to the Stage14 full block.

## 4. Wu — conductor-aspect GL1 subconvexity

Han Wu, *Burgess-like subconvexity for GL1* (arXiv:1604.08551; Compositio Math. 155 (2019)).

Relevance:

- genuine conductor-aspect cancellation for Hecke characters over a fixed number field;
- provides a mechanism from an identified analytic conductor to individual character-sum savings.

Mismatch:

- not a projective-subfamily hybrid large sieve;
- does not itself control the t78 `pi x V` divisor-decomposed coefficient sequence.

## 5. Xie — ray-class short-sum input

Likun Xie, *Products of prime ideals in ray class groups* (arXiv:2606.30567, 2026).

The paper works with ray-class characters modulo an ideal `q` and takes

```text
Q=N(q)
```

as the modulus/conductor norm scale. Its explicit use of Wu gives short-character-sum exponent `103/256`.

For the t77/t78 projective character the corresponding standard norm scale is

```text
Q=d_chi^2,
```

not `d_chi`.

The balanced deficient cover has promising raw length because `M<R*T*B^o(1)` and `N(V)` is of exponent scale `R*T`; however Xie's sequence is an ordinary ray-class/ideal sequence, not the Stage14 primitive balanced four-cell divisor sequence.

## 6. Gaussian / number-field Bombieri–Vinogradov

Tanmay Khale, Cooper O'Kuhn, Apoorva Panidapu, Alec Sun, Shengtong Zhang, *A Bombieri-Vinogradov Theorem for primes in short intervals and small sectors* (arXiv:2008.09677).

Yujiao Jiang, Guangshi Lü, Jesse Thorner, Zihao Wang, *A Bombieri-Vinogradov theorem for higher rank groups* (arXiv:2104.02711).

Relevance:

- confirms that Hecke/sector restrictions on prime ideals can coexist with Bombieri–Vinogradov-type modulus averaging;
- provides the right conceptual Type-I/Type-II architecture.

Mismatch:

- on a fixed Stage14 packet, `M` has only divisor-many values rather than a broad free modulus average;
- standard conductor norm may be `M^2`;
- the moving canonical Gaussian prime remains coupled through the short ellipse and the `ell*H*R*T`, `ell*delta` localizations.

Therefore these theorems do not give a uniform full-range adapter.

## 7. Structured Hecke-character large sieves

Leo Goldmakher and Benoit Louvel, *A quadratic large sieve inequality over number fields* (arXiv:1112.1642).

Relevance:

- proves strong large-sieve inequalities for structured Hecke-character families over number fields.

Mismatch:

- t77 projective local character order divides `p-chi_4(p)` and is not a bounded quadratic family;
- a quadratic restriction would not reproduce projective character orthogonality.

## 8. Refined applicability conclusion

After t78, the external literature no longer has to solve angular-gcd tensorization. The exact missing theorem is narrower:

```text
ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve
```

It would have to combine:

1. projective family cardinality `M*B^o(1)` rather than paying ambient conductor norm `M^2` twice;
2. moving canonical Gaussian-prime character moments;
3. t78 four-cell Möbius/divisor-decomposed cover coefficients with uniform `L2` control;
4. balanced primitive cover and the short `ell*H*R*T`, ellipse, and `ell*delta` masks.

No located off-the-shelf theorem supplies all four simultaneously.

```text
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
MINIMAL_REMAINING_OBSTRUCTION=ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve
```
