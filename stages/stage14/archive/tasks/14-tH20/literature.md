# Stage14-tH20 literature applicability note

Target:

```text
SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
```

No source below is imported as a proof of the Stage14 receiver.

## Quadratic roots to prime moduli

W. Duke, J. B. Friedlander, H. Iwaniec, *Equidistribution of roots of a quadratic congruence to prime moduli*, Ann. of Math. 141 (1995), 423--441.

Relevant component: distribution of quadratic roots as the prime modulus varies.

Mismatch: t74 couples the root host to `c`, `g`, primitive short factors `(q-p,q+p)`, the short ellipse, and three physical hyperbolas.

## Primes represented by binary quadratic forms

A. Zaman, *Primes represented by positive definite binary quadratic forms*, arXiv:1710.08914.

P. C.-H. Lam, D. Schindler, S. Y. Xiao, *On prime values of binary quadratic forms with a thin variable*, arXiv:1809.10755.

Relevant component: primes represented by fixed binary quadratic forms, including thin-variable restrictions.

Mismatch: post-t74 `ell` is already the canonical Gaussian direction prime. The live obstruction is its coupling to the reconstructed primitive cover and short angular cofactor; no exact change of variables places the complete packet under these theorems.

## Friedlander--Iwaniec asymptotic sieve

J. Friedlander, H. Iwaniec, *The polynomial X^2+Y^4 captures its primes*, Ann. of Math. 148 (1998), 945--1040.

J. Friedlander, H. Iwaniec, *Asymptotic sieve for primes*, Ann. of Math. 148 (1998), 1041--1065.

Relevant component: deep bilinear/asymptotic-sieve mechanisms can detect primes in highly structured sparse polynomial sequences.

Mismatch: t74 has not produced a comparable polynomial sequence in which canonical `ell` is the prime output while all short-cover and hyperbola conditions become admissible coefficients.

## Modern Kloosterman / exceptional-Maass large sieve

V. Blomer, A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.

A. Pascadi, *Large sieve inequalities for exceptional Maass forms and the greatest prime factor of n^2+1*, arXiv:2404.04239; Forum Math. Pi 14 (2026), e8.

Relevant component: strong critical-range bilinear/dispersion estimates.

Mismatch: t74 has not produced a Kloosterman phase or Kuznetsov-compatible kernel. Range similarity alone is not a valid adapter.

## Conclusion

The literature supports this order:

```text
1. exhaust exact t74 divisor geometry in g, q-p, q+p;
2. isolate any residual balanced bilinear sum with its exact phase/kernel;
3. only then test DFI / asymptotic-sieve / Kloosterman-large-sieve technology.
```

Therefore no external theorem is directly applicable at tH20.
