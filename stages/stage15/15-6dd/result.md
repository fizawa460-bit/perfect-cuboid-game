# Stage15-6dd — BLIND_REDISCOVERY on the reconstructed three-variable/Pell graph

Base: Stage15-6dc. This substage deliberately forgets the prior route ranking and starts only from the reconstructed graph facts:

1. fixed cells + any three residual variables give `B^o(1)` fourth-variable completions;
2. the exact survivor equations are
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
b^4M^2V^2+c^4N^2U^2=kQ^2;
\]
3. `HMNUV<=B`, `(q,H)=1`, and local S/O orientations are finite/divisor-like.

## Rediscovery 1: the graph should be counted before the modulus

Because the fourth residual variable is no longer an independent support, the natural population is a three-variable base graph decorated by a divisor-many completion list. Any modulus average that still treats all four residual variables independently is structurally wasteful.

This rediscovers a graph-first discrepancy formulation: build exact graph nodes first, then measure their root-ratio distribution modulo `q`.

## Rediscovery 2: eliminate the completion variable instead of averaging it

Let `X=abM`, `Y=cdN`, `Delta=X^4-Y^4`. Direct elimination of the two norm equations gives
\[
\Delta U^2=k(R_-R_+),
\qquad R_\pm=b^2MP\pm d^2NQ,
\]
\[
\Delta V^2=k(S_-S_+),
\qquad S_\pm=a^2MQ\pm c^2NP.
\]

This is stronger structurally than the original Pell display because both exact survivor equations have been consumed at once. It independently rediscovers a **double factor-incidence route**: after removing the already-charged odd core from `Delta`, each residual square must be represented by a product of two correlated linear forms.

## Rediscovery 3: Pell orbit plus second-square test

If one instead fixes `(M,N,U,k)`, the first equation gives a finite initial ideal-divisor set times a unit orbit. Substituting that orbit into the second norm equation asks when a linear recurrence in the unit power lands in a squareclass prescribed by the same `k`.

This is a one-dimensional orbit-intersection problem, not a four-variable lattice problem. It may be approachable by recurrence/height rigidity, but no uniform fixed-power estimate is presently proved.

## Rediscovery 4: average the norm ideals rather than their worst-case divisor counts

The Pell representation associates each completion to a principal ideal divisor of `(a^2MU)^2` in `Q(sqrt(k))`. Summing those ideal divisors over graph bases could be reorganized by the ideal first and the base variables second. This is an ideal-factor switching/averaging route and may save logarithms or reveal forbidden alignments. A fixed power is not automatic.

## Rediscovery 5: reconstructed divisor thresholding

The large receiver weights `phi(d_S)phi(e_O)` and the threshold `d_Se_O>D0` can be imposed after graph reconstruction. Since the completion fiber is divisor-many, large-modulus nodes may be studied through how often the graph's linear factors or norm ideals support a divisor product above `D0`. This is a different threshold geometry from the ambient complementary-cofactor sum.

## Rediscovery 6: local valuation split of the double factors

At odd `p|q`, all cell coefficients are units. In the double eliminants, `v_p(R_-)+v_p(R_+)` and `v_p(S_-)+v_p(S_+)` must match the valuation of the charged `Delta/k^circ` plus twice the residual-square valuation, up to bounded 2-adic conventions. For odd `p`, the two factors in each pair have gcd dividing `2` times a fixed coefficient combination, so away from a finite exceptional support a prime power is forced primarily into one sign factor.

This creates a local branch rigidity not visible when only the quadratic forms were kept.

## Rediscovery 7: graph sparsity without cancellation

The most internal possibility is to use the two factor incidences simultaneously to reduce one more genuine degree of freedom. A successful statement would have the form:

```text
fixed cells + two residual base variables + charged core/sign-factor orientation
-> third residual variable has B^o(1) possibilities
```

or an averaged variant with total `B^{1-delta+o(1)}` graph size. This is not proved, but it is the only rediscovered route that could produce a power saving without a new whole-family cancellation theorem.

## Blind ranking

Starting from the reconstructed graph only, before consulting the earlier route ranking:

1. **Double-eliminant mixed factor incidence / deterministic graph sparsity**: first, because it consumes both exact survivor equations and may reduce graph dimension without cancellation.
2. **Pell unit-orbit intersection with the second norm equation**: second, because it is a one-dimensional exact orbit problem after 6da.
3. **Root-ratio discrepancy dispersion on graph nodes**: third, high quantitative leverage but requires a new whole-family average theorem/adapter.
4. **Reconstructed divisor switching / ideal-factor averaging**: fourth, useful threshold and bookkeeping refinements.
5. **Local valuation analysis**: supporting layer for the first four routes.

Comparison with 6dc shows that all rediscovered route families are already present in the exhaustive ledger. No materially distinct graph route was missed.

```text
STAGE15_6_SUBSTAGE=6dd
STAGE15_6DD_BLIND_REDISCOVERY=true
STAGE15_6DD_GRAPH_FIRST_COUNTING=true
STAGE15_6DD_DOUBLE_FACTOR_INCIDENCE_REDISCOVERED=true
STAGE15_6DD_PELL_SECOND_CONDITION_ORBIT=LIVE_UNTESTED
STAGE15_6DD_IDEAL_FACTOR_AVERAGING=LIVE_UNTESTED
STAGE15_6DD_RECONSTRUCTED_THRESHOLDING=LIVE_UNTESTED
STAGE15_6DD_LOCAL_FACTOR_VALUATION=LIVE_SUPPORTING
STAGE15_6DD_DETERMINISTIC_GRAPH_SPARSITY=LIVE_UNTESTED
STAGE15_6DD_BLIND_TOP_ROUTE=DOUBLE_ELIMINANT_MIXED_FACTOR_INCIDENCE
STAGE15_6DD_EXIT=RECONSTRUCTED_GRAPH_ROUTE_SELECTION_READY
```