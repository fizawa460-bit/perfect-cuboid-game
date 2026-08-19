# SR-STR-024 deep closure attempt

Date: 2026-08-19
Status: `FIRST_MISSING_LEMMA_IDENTIFIED`
Arsenal decision: unchanged (`EXTERNAL_GATE`).

## Closed reduction

For each retained principal cell and valuation pattern `nu`, the exact residue mass admits the character decomposition

```text
S_nu(rho_nu)=A_{nu,0}/phi(Q_nu)
 + (1/phi(Q_nu)) sum_{chi != 1} conjugate(chi(rho_nu)) A_{nu,chi},
```

with exact Parseval variance

```text
V_nu=(1/phi(q)) sum_{chi != 1} |A_{nu,chi}|^2.
```

Finite allocation labels, parity/sign charts, dyadic smoothing, fixed-modulus coprimality, and valuation stripping can be handled at `B^{o(1)}` cost. The obstruction is not the Nguyen modulus range or off-diagonal estimate.

The exact twisted coefficient is a witness-coupled quotient-character sum

```text
A_{nu,chi}=
sum_lambda sum_{f n=W_1(lambda)}
R_nu(lambda;f,n) chi(n_nu) conjugate(chi(f_nu)),
```

where the moving common core and additive side hosts `C_+=B_*y^2+A_*x^2`, `C_-=B_*y^2-A_*x^2` remain in `W_1(lambda)`. On the pair branch, `(E,m)` must remain the charged pair measure.

The reciprocal inner layer alone has a Dirichlet-convolution form, but the full outer coefficient sequence is not known to be multiplicative and has no proved fixed-degree Euler product/functional equation. Thus Nguyen's first analytic dualization step cannot legally start, and no one-dimensional host length `X_nu` can yet be defined for range comparison.

## First missing lemma

```text
FIRST_MISSING_LEMMA=UniformFilteredQuotientCharacterVoronoiFunctionalEquationAdapter
```

Required content: decompose each exact `A_{nu,chi}` into `B^{o(1)}` many Dirichlet/Mellin sums with a fixed-degree functional equation, explicit conductor and dual length, while preserving the moving common core and the original scalar/pair charged measure. The resulting transform must be strong enough to reproduce Nguyen's individual-modulus variance mechanism.

Until this adapter exists, only the trivial Parseval/nonnegativity scale is available and can lose a polynomial factor in `phi(Q_nu)` relative to the target-class principal mass.

```text
CHARACTER_PARSEVAL_REDUCTION=PROVED
NGUYEN_STANDARD_TAU3_SURROGATE_RANGE=q^(2+delta)..q^(3-delta)
LEGAL_ONE_VARIABLE_COEFFICIENT_ADAPTER=OPEN
PAIR_TO_SCALAR_COLLAPSE_FORBIDDEN=true
SR_STR_024_STATUS=EXTERNAL_GATE
ADAPTER_CLOSURE_VERDICT=FIRST_MISSING_LEMMA_IDENTIFIED
```
