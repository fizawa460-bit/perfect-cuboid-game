# Stage15-6 final closeout — internal causal thinning investigation

Base: merged PR #885 (`7fb9837c624b916b885ee6716724d01549a67306`) and the subsequent fresh `Stage15-6-audit` verdict `PASS`, with `INTERNAL_ROUTE_REMAINS=false` and `MERGE_ALLOWED=true`.

Stage15-6 closes roadmap item 7: identify the structural mechanism behind the loss caused by imposing an integral space diagonal, and test whether the Stage14/Arsenal mechanisms admit exact same-measure reuse.

## 1. Final causal theorem

Use the Stage15 physical populations

\[
M_2(B)=\#\mathcal B_2(B),\qquad N_2(B)=\#\mathcal A_2(B),
\]

under the common primitive/canonical exactly-two cutoff `R<=B`.

Stage15-4 identifies the survivor condition as equality of two Gaussian norm squareclasses,

\[
\operatorname{sf}(A)=\operatorname{sf}(B),
\]

with

\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2.
\]

Stage15-6dy computes the exact local parity acceptance condition

\[
v_p(A)\equiv v_p(B)\pmod2.
\]

For inert odd primes `p=3 mod 4`, Gaussian norm valuations are automatically even, so the local acceptance is `rho_p=1`.

For every good split prime `p=1 mod 4`, the exact local acceptance density on the same charged physical toric measure is

\[
\boxed{
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
}
\]

and therefore

\[
\boxed{
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
}
\]

Stage15-6dz proves the congruence-refined count on the same `R<=B` physical measure: for every fixed finite set `S` of good split primes,

\[
M_{2,S}(B)
=
C_{M_2}\left(\prod_{p\in S}\rho_p\right)B(\log B)^5
+o_S(B(\log B)^5).
\]

Every survivor lies in every local acceptance set. Hence for fixed `S`,

\[
\limsup_{B\to\infty}\frac{N_2(B)}{M_2(B)}
\le
\prod_{p\in S}\rho_p.
\]

Now enlarge `S` only after taking `B->infinity`. Since the reciprocal-prime sum over split primes diverges and `1-rho_p=4/p+O(p^-2)`,

\[
\prod_{p\in S}\rho_p\longrightarrow0.
\]

Therefore Stage15-6 independently proves

\[
\boxed{
\frac{N_2(B)}{M_2(B)}\longrightarrow0.
}
\]

Equivalently,

\[
\boxed{N_2(B)=o(B(\log B)^5).}
\]

This is the final internal causal-thinning theorem of Stage15-6. It does not use the Stage15-5 half-power comparison theorem as its proof of zero density.

## 2. Quantitative boundary of the internal mechanism

Stage15-5 already proves the stronger comparison bound

\[
\frac{N_2(B)}{M_2(B)}
\ll_\epsilon B^{-1/2+\epsilon}(\log B)^{-5},
\]

but that fixed-power loss enters through the Stage14 numerator theorem. Stage15-6 did not rederive it from the internal Gaussian-squareclass mechanism.

The exact local profile itself gives only

\[
\prod_{\substack{p\le z\\p\equiv1\,(4)}}\rho_p
=(\log z)^{-2+o(1)}.
\]

Thus even a hypothetical polynomial-size effective prime block for this same parity tensor would naturally produce logarithmic thinning, not `B^{-delta}`.

Accordingly Stage15-6 closes with

```text
STAGE15_6_INTERNAL_FIXED_DELTA_PROVED=false
STAGE15_6_INTERNAL_SIGMA_PROVED=false
STAGE15_6_CAUSAL_ZERO_DENSITY_PROVED=true
```

This is a mechanism-specific boundary, not an impossibility theorem for every future global method.

## 3. Internal route ledger is closed

The fresh exhaustive-view and blind-rediscovery audits through 6ea leave no distinct untested internal fixed-power receiver. The tested families include reconstruction/finite completion, double-eliminant and factor incidence, `k=1` factor gaps, `k>1` Pell/unit orbits, pair-resultant support, centered character/Ramanujan dispersion, ambient/cell complementary switching, and the fixed-prime local overlap sieve.

The last route supplies the independent qualitative theorem above. The others are consumed, equivalent, or carry current-input negative certificates for a new fixed-power gain.

Hence

```text
STAGE15_6_INTERNAL_ROUTE_REMAINS=false
STAGE15_6_NEW_INTERNAL_ROUTE_ALLOWED=false
```

No `Stage15-6eb` or other new Stage15-6 mathematical route is opened by this closeout.

## 4. External future gates

The following are retained only as future external quantitative possibilities, not unfinished Stage15-6 routes:

- effective growing-modulus adelic/local sieving with uniform errors;
- stronger global correlation or reconstruction theorems outside the exhausted internal ledger;
- other external quantitative mechanisms capable of converting global squareclass coincidence into a fixed-power rate.

They may be revisited by a later program only with a new exact theorem contract. They do not keep Stage15-6 open.

## 5. Stage15 handoff

The merged Stage15 roadmap has eight items. Stage15-6 completes item 7. The next program target is roadmap item 8:

```text
Stage15-7
CAUSAL_COMPARISON_VERDICT_AND_FINAL_SELF_CONTAINED_BUNDLE
```

Stage15-7 should reconcile, without conflation:

1. the Stage15-5 quantitative survival theorem, whose fixed-power numerator input comes from Stage14;
2. the Stage15-6 independent causal theorem `N_2/M_2 -> 0` from the local squareclass sieve;
3. the fact that Stage15-6 proved no internal `delta>0` or `sigma>0`;
4. the exact normal forms, population/cutoff contracts, finite evidence, and provenance needed for a final self-contained Stage15 verdict.

It must not reopen Stage15-6 merely because an external stronger theorem could someday sharpen the rate.

```text
STAGE15_6_STATUS=CLOSED
STAGE15_6_FINAL_SUBSTAGE=6ea
STAGE15_6_FINAL_AUDIT=PASS
STAGE15_6_CAUSAL_THINNING_THEOREM=N2_OVER_M2_TO_ZERO
STAGE15_6_INTERNAL_FIXED_DELTA_PROVED=false
STAGE15_6_INTERNAL_SIGMA_PROVED=false
STAGE15_6_INTERNAL_ROUTE_REMAINS=false
STAGE15_6_EXTERNAL_FUTURE_GATES_SEPARATED=true
STAGE15_6_NEXT_STAGE15_TARGET=Stage15-7
STAGE15_6_EXIT=CLOSED_ADVANCE_TO_STAGE15_7
```
