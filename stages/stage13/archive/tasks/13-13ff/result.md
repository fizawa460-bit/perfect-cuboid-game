# Stage13-13ff result — exact external theorem contracts

> STATUS: `COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS`

Gate F closes the R04/DeepSeek objection that the final proof referred to Hecke/Dirichlet continuation, conductor growth, and Vaaler approximation only through generic phrases.

The repaired proof-facing source is

```text
stages/stage13/13-13ff/external-theorem-contracts.md
```

## What is now explicit

### Gaussian-Hecke channel

For every retained nonzero angular index `k=8*ell`, `ell>=1`, the external contract states:

- entire/holomorphic continuation of `L(s,Xi_k)`;
- the completed functional equation
  `pi^{-(s+2|k|)} Gamma(s+2|k|) L(s,Xi_k) = xi(1-s,k)`;
- no pole at `s=1` for nonzero angular index;
- fixed finite residue twists are Hecke characters with fixed conductor once the inert-prime set is frozen.

Polynomial vertical/angular growth on the fixed strip is not left as an unexplained import. It is derived from absolute convergence on the right boundary, the functional equation, Stirling, and Phragmen--Lindelof.

### Gate D summatory interface

A second hidden shortcut is removed. Instead of asserting that a bare unsmoothed Perron shift plus polynomial growth automatically gives the ordinary partial-sum power saving, Gate F inserts a high-order Riesz/Perron kernel

```text
X^s / [s(s+1)...(s+m)]
```

with `m` larger than the fixed vertical-growth exponent. After the smoothed contour shift, finite differencing plus the coefficient majorant gives fixed constants `delta_H>0`, `C_H,D_H>=0` with

```text
S_ell(X) << X^(1-delta_H) (1+ell)^C_H (log(2X))^D_H
```

uniformly for all `X>=2`, `ell>=1`. This is exactly the interface used by Gate D.

### Vaaler channel

The only Vaaler black-box imported is the finite-degree sawtooth approximation. The interval majorant/minorant is derived inside Gate F. For degree `L`, the resulting interval polynomials satisfy

```text
P^- <= 1_I <= P^+
hat(P^±)(0) = |I| ± 1/(L+1)
|hat(P^±)(h)| <= 1/(pi|h|)+1/(L+1) < 1, 1<=|h|<=L.
```

Thus the Vaaler coefficient contributes no positive harmonic power, and for `L=floor((log B)^4)` the zero-mode excess remains `O(B(log B)^-1)`.

## Minimal external boundary after Gate F

The final R05 route does not require:

- a Gaussian-Hecke zero-free region;
- a general Selberg--Delange black box;
- a theorem uniform in a residue modulus growing with `B`;
- Dirichlet's theorem on primes in arithmetic progressions;
- an external Wiener lemma.

No theorem statement or directional constant changes in Gate F.

```text
STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS
HECKE_NONZERO_ENTIRE=true
HECKE_NONZERO_FUNCTIONAL_EQUATION=true
HECKE_NONZERO_POLE_AT_1=false
FIXED_RESIDUE_CONDUCTOR=true
NONTRIVIAL_HECKE_TWIST_HOLOMORPHIC_AT_1=true
L_CHI4_HOLOMORPHIC_AT_1=true
POLYNOMIAL_STRIP_GROWTH_DERIVED=true
POLYNOMIAL_ANGULAR_GROWTH_DERIVED=true
RIESZ_PERRON_SMOOTHING_EXPLICIT=true
HECKE_FAMILY_SUMMATORY_INTERFACE_DERIVED=true
VAALER_IMPORTED_OBJECT=SAWTOOTH_APPROXIMATION
VAALER_INTERVAL_MAJORANT_DERIVED_INTERNALLY=true
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
GENERAL_SELBERG_DELANGE_REQUIRED=false
GROWING_MODULUS_THEOREM_USED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fg
```
