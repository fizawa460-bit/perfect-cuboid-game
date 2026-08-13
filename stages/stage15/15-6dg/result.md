# Stage15-6dg — normalized double-factor incidence and deterministic sparsity test

Base: Stage15-6df. Keep
\[
g=\gcd(P,Q),\qquad P=gp,\quad Q=gq,\quad (p,q)=1,
\]
and use the exact divisibility
\[
kg^2\mid\Delta.
\]
Define
\[
D:=\frac{\Delta}{kg^2}\in\mathbf Z_{>0}.
\]
Then the double eliminants become
\[
\boxed{DU^2=(b^2Mp-d^2Nq)(b^2Mp+d^2Nq),}
\]
\[
\boxed{DV^2=(a^2Mq-c^2Np)(a^2Mq+c^2Np).}
\]
Put
\[
\widetilde R_\pm=b^2Mp\pm d^2Nq,
\qquad
\widetilde S_\pm=a^2Mq\pm c^2Np.
\]
Stage15-6df gives
\[
\gcd(\widetilde R_-,\widetilde R_+)\in\{1,2\},
\qquad
\gcd(\widetilde S_-,\widetilde S_+)\in\{1,2\}.
\]
Thus all odd moving common support has been removed before the factor-incidence analysis.

## 1. What coprime factorization really buys

Away from the explicit 2-adic parity branch, every odd prime power in `DU^2` is assigned to exactly one of `R_tilde_-` or `R_tilde_+`; similarly for `S`. Therefore, after choosing a divisor splitting of the odd part of `D`, each sign factor is a fixed divisor of `D` times a square, up to sign and the bounded parity convention. The number of divisor/sign/parity decorations is `B^{o(1)}`.

This is a genuine simplification. It proves that the factor incidence has no hidden polynomial branching from moving gcds.

However the square variables themselves remain genuine free parameters. The two linear recovery identities are
\[
2b^2Mp=\widetilde R_++\widetilde R_-,
\qquad
2d^2Nq=\widetilde R_+-\widetilde R_-,
\]
with analogous formulas from the `S` pair. Divisor splitting controls the squareclasses of the factors; it does not make their square roots divisor-many.

## 2. Exact Cramer equivalence: no new algebraic equation

The original survivor equations, after substituting `P=gp,Q=gq`, are a linear system in `U^2,V^2`:
\[
\begin{pmatrix}
a^4M^2&d^4N^2\\
c^4N^2&b^4M^2
\end{pmatrix}
\binom{U^2}{V^2}
=
kg^2\binom{p^2}{q^2}.
\]
Its determinant is exactly
\[
\Delta=(abM)^4-(cdN)^4>0.
\]
Cramer's rule gives precisely the two normalized eliminants above. Conversely, because `Delta` is nonzero, those two Cramer formulas recover the unique `U^2,V^2` solving the original system. Therefore
\[
\boxed{\text{double eliminants are algebraically equivalent to the two original norm equations after fixing }M,N,k,g.}
\]
They are not a third independent equation.

This is the decisive deterministic-sparsity test. The mixed-factor rewrite exposes coprimality and squareclasses, but by itself it cannot lower the algebraic dimension of the reconstructed receiver.

## 3. Why a second B^o(1) reconstruction does not follow

Stage15-6da proved a vertical statement:
\[
\text{fixed cells + any three residual variables}\Rightarrow B^{o(1)}\text{ fourth-variable completions}.
\]
To remove another genuine degree of freedom deterministically, fixing only two residual base variables would have to leave a zero-dimensional exact receiver after legal decorations.

For fixed cells, `(M,N,k,g)` and nonzero `Delta`, the variables `(U,V,p,q)` are still constrained by exactly two independent quadratic equations. Equivalently, after projectivization this is the same one-dimensional two-quadric receiver already exposed earlier in Stage15; the Cramer/factor coordinates are an invertible re-expression on the nondegenerate physical chamber. Thus the current identities do not turn the remaining graph into a finite algebraic fiber.

This does **not** prove that a uniform arithmetic `B^{o(1)}` count on that curve is impossible. It proves the narrower point required here:

```text
DETERMINISTIC_SECOND_RECONSTRUCTION_FROM_DOUBLE_ELIMINANTS=false
```

Any such subpolynomial count would require an additional arithmetic theorem about the remaining one-dimensional receiver, not merely the exact gcd/factor splitting.

## 4. Averaged fixed-power test

The same diagnosis applies to the averaged target. After all exact gcd extraction, the new information costs only divisor-like choices and leaves the same one-dimensional exact graph over each fixed `(M,N,k,g)` package. No factor in the identities forces a uniform loss `B^{-delta}` in the number of base packages, and no inverse power of the switched threshold `D0` is created.

Hence the double-factor incidence, **without an additional averaging/cancellation theorem**, yields neither
\[
B^{1-\delta+o(1)}
\]
for a fixed `delta>0`, nor a `D_0^{-\sigma}` large-tail gain.

This is a rigorous mechanism-level negative certificate, not a claim that no deeper theorem can exploit these factors. The exact factorization remains a useful local input for the next route.

## 5. Route verdict

- exact moving-gcd classification: PROVED;
- `kg^2|Delta`: PROVED;
- normalized sign factors coprime up to `2`: PROVED;
- divisor/squareclass branching: `B^{o(1)}`;
- second deterministic graph-degree collapse: BLOCKED by Cramer equivalence / one-dimensional receiver;
- averaged fixed-power saving from factorization alone: NOT DERIVED;
- root-ratio discrepancy dispersion: should now be promoted from LIVE backup.

```text
STAGE15_6_SUBSTAGE=6dg
STAGE15_6DG_NORMALIZED_D=Delta/(k*g^2)
STAGE15_6DG_NORMALIZED_SIGN_PAIR_GCD_AT_MOST_2=true
STAGE15_6DG_DIVISOR_SQUARECLASS_BRANCHING=B^o(1)
STAGE15_6DG_DOUBLE_ELIMINANTS_CRAMER_EQUIVALENT=true
STAGE15_6DG_SECOND_DETERMINISTIC_RECONSTRUCTION=false
STAGE15_6DG_FIXED_DELTA_FROM_FACTOR_SPLIT=false
STAGE15_6DG_FIXED_SIGMA_FROM_FACTOR_SPLIT=false
STAGE15_6DG_NEGATIVE_CERTIFICATE=true
STAGE15_6DG_EXIT=DISPERSION_PROMOTION_AND_LEDGER_READY
```