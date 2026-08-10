# Stage14-tH21 literature applicability note

Target:

```text
SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
```

No item below is imported as a proof of the Stage14 receiver. The question is not whether the theorem is powerful, but whether an exact adapter preserves the t76 projective kernel and every physical mask.

## 1. Duke--Friedlander--Iwaniec: quadratic roots to prime moduli

William Duke, John B. Friedlander, Henryk Iwaniec,
*Equidistribution of roots of a quadratic congruence to prime moduli*,
Annals of Mathematics 141 (1995), 423--441.
DOI: 10.2307/2118527.

Relevant feature: root distribution while the prime modulus varies.

Stage14 mismatch:

```text
DFI varying modulus: prime p
Stage14 root modulus: K_clean | odd(kappa)
Stage14 moving prime: ell != K_clean
```

After fixed `(kappa,beta)` conditioning, `K_clean` is divisor-many/fixed. Thus the essential DFI prime-modulus average is absent.

## 2. Deshouillers--Iwaniec / Kuznetsov spectral framework

Jean-Marc Deshouillers, Henryk Iwaniec,
*Kloosterman sums and Fourier coefficients of cusp forms*,
Inventiones Mathematicae 70 (1982), 219--288.
DOI: 10.1007/BF01390728.

Relevant feature: trace formula and spectral large-sieve estimates for weighted sums of Kloosterman sums.

Stage14 mismatch: additive opening of

```text
t == rho*r mod K_clean
```

produces linear phases modulo fixed `K_clean`. The inverse in `rho` belongs to the moving Gaussian direction. No standard complete Kloosterman sum `S(m,n;c)` with a verified modulus family has yet been derived while retaining the cover/hyperbola weights.

## 3. Duke--Friedlander--Iwaniec: bilinear Kloosterman fractions

William Duke, John B. Friedlander, Henryk Iwaniec,
*Bilinear forms with Kloosterman fractions*,
Inventiones Mathematicae 128 (1997), 23--43.
DOI: 10.1007/s002220050135.

Relevant feature: cancellation in bilinear forms containing modular inverses.

Stage14 mismatch: the inverse-bearing coefficient is a rational function of two coordinates of the same Gaussian prime direction, while the cover coefficients and `ell,c,delta` masks are coupled. No factorization into arbitrary independent coefficient sequences of the DFI type has been proved.

## 4. Fouvry--Iwaniec Gaussian primes

Etienne Fouvry, Henryk Iwaniec,
*Gaussian primes*, Acta Arithmetica 79 (1997), 249--287.
DOI: 10.4064/aa-79-3-249-287.

Relevant feature: sieve/bilinear technology adapted to Gaussian-prime structure.

Stage14 relevance is genuine because, for fixed `U`, `(A,Bdir)` is a fixed linear transform of the canonical Gaussian prime `pi` with `N(pi)=ell`.

Direct-import failure: the Stage14 phase uses a growing composite modulus `K_clean`, a projective inverse `Bdir/A` or `A/Bdir`, and simultaneous short-cover/ellipse/double-hyperbola masks. No theorem in the cited Gaussian-prime setup gives that uniform weighted projective discrepancy over the full t76 deficient-modulus range.

## 5. Pascadi exceptional-Maass large sieve

Alexandru Pascadi,
*Large sieve inequalities for exceptional Maass forms and the greatest prime factor of n^2+1*,
Forum of Mathematics, Pi 14 (2026), e8.
DOI: 10.1017/fmp.2026.10025.

Relevant feature: improved large-sieve bounds for exceptional Maass Fourier coefficients, including sequences with sparse Fourier transforms arising from dispersion.

Direct-import failure: Stage14 has not yet produced the required automorphic level/coefficient sequence. Assigning level `K_clean` does not separate the moving Gaussian-prime coefficient and physical masks; assigning level `ell` loses the actual root modulus.

## 6. Blomer--Pascadi 2026 bilinear Kloosterman sums

Valentin Blomer, Alexandru Pascadi,
*Bilinear forms with Kloosterman sums via quadratic characters*,
arXiv:2607.24311 (2026).

Relevant feature: a power saving in critical bilinear Kloosterman ranges, including all moduli.

Direct-import failure: the t76 congruence has not been converted to the paper's Kloosterman-sum bilinear kernel. A numerical resemblance between `R,T` and a square-root modulus range is not an adapter.

## 7. Audit conclusion

The literature supports the following order:

```text
1. keep K_clean fixed after packet conditioning;
2. open the exact projective congruence only if useful;
3. preserve moving Gaussian-prime direction and every short-cover/hyperbola mask;
4. derive an actual complete Kloosterman or separated inverse-fraction bilinear form;
5. only then invoke DFI/Kuznetsov/Pascadi/Blomer-Pascadi technology.
```

At Stage14-tH21, step 4 is not proved. Therefore all direct Type-II imports remain false.
