# Stage15-6dr — character large-sieve negative certificate and next preserved route

Base: Stage15-6dp exact operator/dual receiver and Stage15-6dq updated-Arsenal audit.

The question is now precise: do the currently certified Stage15 graph identities plus the R02 Arsenal prove
\[
\mathfrak B_P(Q_0)
\ll X^{1+\kappa}Q_0B^{o(1)}
\]
for some fixed `kappa<1`, where `X=|G(P)|`?

## 1. What is proved exactly

The following are certified:

1. the centered decorated occupancy operator `T_P` and its exact dual;
2. zero-mode subtraction before absolute values;
3. exact primitive reduced-frequency recombination by `t=(u,v,q)`;
4. the occupied-node locks
   \[
   q\mid\Delta_x,
   \qquad kg^2\mid\Delta_x;
   \]
5. the occupied-pair resultant lock from 6dk/6dm;
6. Stage15-6da `B^o(1)` fourth-variable reconstruction;
7. the trivial same-measure second-moment scale
   \[
   \boxed{
   \mathfrak B_P(Q_0)
   \ll X^2Q_0B^{o(1)}.
   }
   \]

The last line corresponds to `kappa=1`.

## 2. Why the character rewrite does not lower kappa by itself

The character identity is an exact Fourier representation of the same centered occupancy residual. It does not create new independence.

At a fixed legal small modulus, the occupied root-line union has positive local density `Omega/q^2`. The implications `q|Delta` and `q^2|pair-resultant` hold **after** occupancy is imposed; they do not give an upper bound forcing
\[
N_{d,e}=\frac{\Omega}{q^2}X+o(X)
\]
or any fixed-power version of that relation.

Equivalently, in the dual operator, a `kappa<1` bound is exactly a spectral anti-concentration statement for
\[
K_P(x,y;Q_0)
=\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega_{d,e}}
F_{d,e}(x)F_{d,e}(y).
\]
None of the current divisibility or reconstruction identities estimates this centered kernel after summing over varying graph bases.

The stronger frequency-separated majorant from 6dp also does not close the gate. Orthogonality reduces it to equidistribution of the full value map `(L_1,L_2) mod q`. That is a new theorem requirement and is strictly stronger than the target-root occupancy statement.

Thus `character expansion + Parseval + divisor support` is not a proof of cancellation. AR-026 certifies precisely this logical boundary.

## 3. Why the natural one-dimensional large-sieve slice is not yet legal

For example, use `(M,N,U)` as reconstructed base variables and let `V` be a 6da completion. The first root-line phase contains a linear term in `M`, but the second contains the completion `V=V(M,N,U,nu)`. If the latter exponential is absorbed into a coefficient, that coefficient depends on `(q,omega,u,v)`.

A standard fixed-coefficient large-sieve inequality therefore cannot be applied to the `M` sequence without first proving a new bilinear/completion-phase adapter. The symmetric slices in `N,U,V` have the same issue.

This is not a claim that such an adapter is impossible. It is a certificate that **no fixed-coefficient large-sieve theorem currently present in the repository applies to the exact reconstructed graph sums**.

## 4. Updated-Arsenal closure of the current character attempt

The six required weapons give the following exhaustive result for the present route:

- **AR-025:** exact reduced-modulus reindexing succeeds, exponent-neutral;
- **AR-026:** soft Fourier moments cannot dominate the moving target class;
- **AR-027:** only native decorated-modulus / exact physical-packet averages are legal;
- **AR-033:** no scalar coprime-rectangle coefficient factorization exists for the graph sums;
- **AR-035:** fixed-prime overlap sieve is qualitative `o` without effective uniformity and no reconstructed-graph fixed-modulus asymptotic has been proved;
- **AR-037:** no conductor-uniform Euler factorization exists, and its certified output is fixed logarithmic saving rather than a fixed `B` power.

AR-009, AR-017, AR-023/024 and AR-028 were also rechecked as supporting/firewall entries and supply no missing same-measure exponent.

Therefore
\[
\boxed{
\text{CURRENT TOOLKIT DOES NOT PROVE ANY }\kappa<1
\text{ FOR THE CHARACTER OCCUPANCY OPERATOR.}
}
\]
This is a **route/input negative certificate**, not a theorem that no character large sieve could ever exist.

```text
CHARACTER_LARGE_SIEVE_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY
MATHEMATICAL_IMPOSSIBILITY_CLAIMED=false
```

## 5. Delta, overlap and sigma ledger

The best certified occupancy exponent remains
\[
\kappa=1.
\]
Hence the conditional formula
\[
\delta<\frac{1-\kappa}{2}-\frac\theta2
\]
gives no positive `delta` for any polynomial modulus window `theta>0`.

So
\[
\boxed{\delta>0\text{ is not proved},}
\qquad
\boxed{\text{executable polynomial overlap window: NONE}.}
\]

The large complementary receiver also still has no
\[
D_0^{-\sigma}
\]
gain, so
\[
\boxed{\sigma>0\text{ is not proved}.}
\]
No split trigger fires.

## 6. Parking audit: parking is premature because preserved internal routes remain

The reconstructed-graph exhaustive ledger from 6dc/6dd was not exhausted merely by blocking deterministic graph sparsity, root-ratio/occupancy dispersion, pair-resultant support, and the present character form.

The following routes are still preserved:

- `PELL_UNIT_ORBIT_SECOND_NORM_CORRELATION` — LIVE/UNTESTED as an averaged arithmetic route;
- `NORM_IDEAL_FACTOR_AVERAGING` — LIVE/UNTESTED;
- reconstructed divisor switching — LIVE as a supporting threshold reorganization, though no exponent is currently certified;
- local valuation structure — LIVE supporting layer;
- AR-035 fixed-prime thinning — LIVE qualitative route, not a current power-saving theorem.

Therefore a Stage15-6 parking declaration would be premature.

Among the remaining **quantitative** internal candidates, the highest-priority next route is
\[
\boxed{
\text{PELL_UNIT_ORBIT_SECOND_NORM_CORRELATION}.
}
\]
It is native to the exact 6da reconstruction: for fixed `(M,N,U,k)` the first survivor norm equation is one Pell/norm orbit, and the second survivor norm equation becomes a squareclass condition along that orbit. Unlike the character attempt, this route keeps the completion dynamics rather than treating its phase as an uncontrolled frequency-dependent coefficient.

This route was already present in the 6dc/6dd exhaustive/blind ledger, so selecting it does not invent a new receiver or discard a previously LIVE route. Execution must wait for a fresh audit of the character negative certificate and this route promotion.

## 7. Required stop audits

### Arsenal trigger search
Completed against R02, including AR-025/026/027/033/035/037 and the supporting entries listed above.

### Exact reconstruction search
Stage15-6da remains the unique proved dimension collapse; no second deterministic collapse was found.

### Measure and quantifier audit
`R<=B`, the exact reconstructed graph, `kg^2|Delta`, decorated `(d,e)`, exact `phi(d)phi(e)` weights, zero-mode subtraction, all survivor masks and no-double-charge rules remain unchanged. No Stage14 fixed-packet exponent is imported.

## 8. Controller exit

```text
STAGE15_6_SUBSTAGE=6dr
STAGE15_6DR_CHARACTER_LARGE_SIEVE_NEGATIVE_CERTIFICATE=true
STAGE15_6DR_NEGATIVE_SCOPE=CURRENT_CERTIFIED_INPUTS_ONLY
STAGE15_6DR_KAPPA_BEST_CERTIFIED=1
STAGE15_6DR_KAPPA_LT_1_PROVED=false
STAGE15_6DR_DELTA_PROVED=false
STAGE15_6DR_SIGMA_PROVED=false
STAGE15_6DR_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DR_PARKING_ALLOWED=false
STAGE15_6DR_NEXT_PRESERVED_ROUTE=PELL_UNIT_ORBIT_SECOND_NORM_CORRELATION
STAGE15_6DR_SPLIT_TRIGGER=false
STAGE15_6DR_AUDIT_REQUIRED=true
STAGE15_6DR_CODEX_REQUIRED=false
STAGE15_6DR_MERGE_ALLOWED=false
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6dr
NEXT_GATE=FRESH_AUDIT_OF_CHARACTER_LARGE_SIEVE_NEGATIVE_CERTIFICATE_AND_PELL_ROUTE_PROMOTION
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```
