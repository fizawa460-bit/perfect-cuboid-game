# Stage15-6dt — branchwise same-measure test for k=1 factor and k>1 Pell receivers

Base: repaired Stage15-6ds. The squarefree survivor-core population is now split into the degenerate branch `k=1` and the real-quadratic branch `k>1`. Test both on the same reconstructed physical measure and do not charge the 6da completion multiplicity twice.

The target remains a genuine polynomial deficit on the outer reconstructed-base population, not an improvement of one `B^{o(1)}` completion fiber to another.

## 1. Quantitative contribution of the k=1 factor branch

For fixed `(a,b,c,d,M,N,U)` with `k=1`, Stage15-6ds gives
\[
(P-L_1)(P+L_1)=C_1^2,
\qquad
(Q-L_2)(Q+L_2)=C_2^2,
\]
where
\[
C_1=a^2MU,\quad L_1=d^2NV,
\qquad
C_2=c^2NU,\quad L_2=b^2MV.
\]
Enumerate only the first primitive factor pair. It gives at most
\[
\tau(C_1^2)=B^{o(1)}
\]
possible values of `V`; the second factor equation and all physical masks are postfilters. Hence if `\mathcal B_1(B)` denotes the reconstructed base tuples for which the legal core is `k=1`, then the certified contribution is only
\[
\boxed{
N_{k=1}(B)
\le B^{o(1)}\,\#\mathcal B_1(B),
}
\]
with one completion charge.

The simultaneous factor-gap condition
\[
\frac{s_1-r_1}{2d^2N}
=\frac{s_2-r_2}{2b^2M}
\]
is a genuine arithmetic restriction on a base completion. But algebraically the factor-pair data are reversible to `(P,Q,V)`, and 6dg already proves the original two quadrics are equivalent to the double-eliminant pair when `Delta!=0`. Therefore the `k=1` factor branch is **not a new independent codimension**.

Could the factor-gap representation nevertheless yield a distinct same-measure thinning theorem? Only if one proves that a polynomial fraction of outer bases admit no compatible pair of primitive divisor gaps. No such family theorem is supplied by the factorization itself. Counting divisor pairs pointwise gives only `B^{o(1)}`; averaging ordinary divisor moments gives logarithmic/subpolynomial factors. Thus
\[
\boxed{\text{k=1 factorization alone proves no fixed-power outer thinning}.}
\]

Operationally, the factor gaps are still valuable: they expose the exact data that a **residual-cell complementary divisor switch** would act on. That is the already-preserved next route, not an additional saving that may be charged now.

## 2. Quantitative contribution of squarefree k>1 Pell branch

For `k>1`, repaired 6ds retains the exact rank-one unit-orbit receiver. For fixed `(a,b,c,d,M,N,U,k)` the first norm has divisor-many principal-ideal seeds and `O(log B)` physically bounded unit exponents per seed. This is already one `B^{o(1)}` completion charge from 6da.

The second norm selects intersections of two unit orbits in the same `Q(sqrt(k))`. Even a theorem reducing `O(log B)` orbit intersections to `O(1)` would improve only that already-subpolynomial completion fiber. A fixed-power family saving requires instead a theorem showing that a polynomial fraction of reconstructed bases/cores admit no legal second-orbit intersection. The current norm-ideal, recurrence-period and local-valuation inputs do not prove such a statement.

Therefore if `\mathcal B_{>1}(B)` denotes the reconstructed base/core tuples with squarefree `k>1`, the current certified contribution is
\[
\boxed{
N_{k>1}(B)
\le B^{o(1)}\,\#\mathcal B_{>1}(B),
}
\]
again with exactly one completion charge.

The previous Pell negative certificate is retained:
\[
\boxed{\text{no same-measure fixed-power saving follows from current k>1 Pell inputs}.}
\]
It remains a current-input negative certificate, not an impossibility theorem.

## 3. Union bound and no-double-charge accounting

Since the squarefree core is uniquely either `1` or `>1`,
\[
N_{\rm surv}(B)=N_{k=1}(B)+N_{k>1}(B).
\]
The branchwise reconstruction yields only
\[
\boxed{
N_{\rm surv}(B)
\le B^{o(1)}
\bigl(\#\mathcal B_1(B)+\#\mathcal B_{>1}(B)\bigr),
}
\]
where `B^{o(1)}` is the single 6da completion multiplicity. We do not multiply the `k=1` first/second divisor counts, and we do not multiply the `k>1` first/second Pell seed counts.

Thus the branch split corrects the receiver geometry but does not itself produce `delta>0` or `sigma>0`.

## 4. Arsenal audit after the branch split

### AR-016 — applicable to both branches, exponent-neutral

For `k=1`, AR-016 controls the first primitive factor-pair enumeration. For `k>1`, it controls ideal/divisor seeds and fixed finite decorations. In both cases the output is multiplicity only and cannot be charged as a density saving.

### AR-023 / AR-024 — measure firewalls remain active

Neither branch may replace `(M,N,U,k,cells,channel decorations)` by a scalar such as `C_1`, `C_2`, `Delta`, a factor gap, or a recurrence discriminant merely because scalar fibers are divisor-many. The survivor and switched-channel masks remain base-dependent.

### AR-028 — no recharge

The common core, the 6da fourth-variable completion, and the double-eliminant structure have already been charged. The `k=1` factor variables and `k>1` Pell seeds are branchwise parametrizations/postfilters of the same survivor equations, not independent savings.

### AR-033 — no current scalar rectangle adapter

Neither the simultaneous primitive factor-gap condition for `k=1` nor the varying Pell intersection for `k>1` has been converted into the required two-variable scalar coprime convolution with the certified weighted coefficient norm. No Stage12 `3/4+epsilon` error transfers.

### AR-035 — qualitative backup only

Fixed primes may reject some `k=1` factor-gap states or some `k>1` recurrence states, but a congruence-refined asymptotic on the same reconstructed base measure is still missing. Without uniformity as the prime set grows, AR-035 supplies at most a qualitative `o(1)` mechanism, not the fixed power required here.

### AR-037 — no uniform Euler/Dirichlet adapter

No uniform fixed-conductor Euler factorization has been established for either the simultaneous factor-gap family or the varying real-quadratic unit family. A finite-order Selberg--Delange contract therefore does not presently apply, and logarithmic saving alone would not solve the polynomial gate.

### Pell/recurrence and factor assets

The active Arsenal contains no dedicated theorem that gives a same-measure fixed-power zero-density result for the varying Pell family. The `k=1` factor branch uses only the generic divisor/factor machinery already covered by AR-016 and the existing double-eliminant/factor-incidence route.

## 5. Branchwise verdict

- `k=1`: exact primitive factor-gap receiver; algebraically equivalent to the original survivor quadrics/double eliminants; no distinct certified fixed-power thinning. Its only unconsumed leverage is to feed the residual complementary switch.
- squarefree `k>1`: exact Pell recurrence-intersection receiver; current-input fixed-power negative certificate retained.
- union: one `B^{o(1)}` completion charge, no extra multiplication across postfilters.

Consequently
\[
\boxed{\delta>0\text{ remains unproved},\qquad \sigma>0\text{ remains unproved}.}
\]
No polynomial overlap window is executable from the branchwise completion analysis alone.

Because the corrected receiver is the union of two materially different branch geometries, the fresh `EXHAUSTIVE_VIEW_AUDIT` and `BLIND_REDISCOVERY` must now be rerun on that union before route confirmation.

```text
STAGE15_6_SUBSTAGE=6dt
STAGE15_6DT_BRANCHWISE_TESTED=true
STAGE15_6DT_K1_FACTOR_BRANCH_TESTED=true
STAGE15_6DT_K1_FACTOR_BRANCH_OUTER_FIXED_POWER=false
STAGE15_6DT_K1_FACTOR_BRANCH_ROLE=INPUT_TO_RESIDUAL_COMPLEMENTARY_SWITCH
STAGE15_6DT_KGT1_PELL_AVERAGING_TESTED=true
STAGE15_6DT_KGT1_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY
STAGE15_6DT_AR016=APPLICABLE_EXPONENT_NEUTRAL
STAGE15_6DT_AR023_024=FIREWALL_PASS
STAGE15_6DT_AR028=NO_RECHARGE_PASS
STAGE15_6DT_AR033=NO_ADAPTER
STAGE15_6DT_AR035=QUALITATIVE_ONLY_NO_STAGE15_BASE_ADAPTER
STAGE15_6DT_AR037=NO_UNIFORM_EULER_ADAPTER
STAGE15_6DT_COMPLETION_MULTIPLICITY_CHARGED_ONCE=true
STAGE15_6DT_DELTA_PROVED=false
STAGE15_6DT_SIGMA_PROVED=false
STAGE15_6DT_EXIT=UNION_EXHAUSTIVE_AND_BLIND_PROTOCOL_REQUIRED
```
