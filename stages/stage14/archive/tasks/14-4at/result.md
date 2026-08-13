# Stage14-4at — dyadic Euclid instantiation and first quantitative gap

## Result

Stage14-4as gives the common weighted end-to-end inequality

\[
H_{Q,C}\le
\rho_{\rm ht}\rho_{\rm glob}\rho_{\rm loc}A_Q
+\rho_{\rm ht}\rho_{\rm glob}E_{\rm loc}
+\rho_{\rm ht}E_{\rm glob}
+E_{\rm ht}.
\]

Stage14-4at now places this on the standard dyadic decomposition of primitive opposite-parity Euclid pairs.

For a box

\[
\mathcal B(M,N)=\{(m,n):m\asymp M,\ n\asymp N\},
\]

inside `m^2+n^2<=B`, one has

\[
M,N\ll B^{1/2},\qquad A(M,N)\ll MN,
\]

and the whole region is covered by `O((log B)^2)` boxes. Hence all dyadic summation losses are `B^{o(1)}` and the bulk boxes have `MN` up to order `B`.

## The only currently available Q-scale

Merged Stage14-s5g does not prove a local sieve theorem. It only formulates the centered prime-level second-moment candidate

\[
\sum_{p\le Q}\sum_{e\ne0}
\left|\sum_{(m,n)\in\mathcal B(M,N)}a_{m,n}C_{p,e}(m,n)\right|^2
\ll_\varepsilon
(MN+Q^4)(MNQ)^\varepsilon\sum|a_{m,n}|^2.
\]

The `Q^4` term therefore gives a natural analytic depth ceiling. Write `Q=B^theta` on a bulk box `MN\asymp B`. Then

\[
MN+Q^4\asymp B+B^{4\theta}.
\]

Thus:

```text
theta < 1/4  : volume term B dominates
 theta = 1/4 : transition scale
 theta > 1/4 : Q^4 is super-volume
```

Accordingly the benchmark global choice is

\[
Q_*(B)=B^{1/4-\eta}\qquad(\eta>0\text{ fixed}),
\]

with the box-adaptive clipped choice

\[
Q_{M,N}=\min\left(B^{1/4-\eta},(MN)^{1/4-\eta}\right)
\]

when a uniform all-box statement is required. This keeps `Q^4` below the local box volume up to `B^{o(1)}` factors.

This is only a safe **candidate depth** for the s5g second moment. It is not yet a value for `rho_loc` or `E_loc`.

## Why Q cannot yet be optimized into the 4as theorem

The s5g inequality is a second moment for centered prime-level traces. The 4as theorem requires a nonnegative full-local indicator bound

\[
S_Q\le\rho_{\rm loc}A_Q+E_{\rm loc}.
\]

No theorem currently converts the former into the latter. In particular:

1. the complete local indicator contains reciprocal off-diagonal divisor interactions between squarefree pieces of the five Euclid factors;
2. the exact finite-field centering terms must be retained;
3. a signed centered trace estimate is not itself an upper bound for a nonnegative Selmer/base count;
4. the scale `MN+Q^4` is the second-moment cost, not an identified additive counting error `E_loc`.

Therefore it would be invalid to set `E_loc=Q^4`, to read a power `delta_loc` from `Q=B^{1/4-eta}`, or to insert the finite s5g decay as an asymptotic density.

## Error-budget audit

For bookkeeping only, suppose a future local-indicator theorem supplies

\[
\rho_{\rm loc}\ll B^{-\delta_{\rm loc}},\qquad
E_{\rm loc}\ll B^{\kappa_{\rm loc}},
\]

and similarly `rho_glob<<B^{-delta_glob}`, `rho_ht<<B^{-delta_ht}` with

\[
E_{\rm glob}\ll B^{\kappa_{\rm glob}},\qquad
E_{\rm ht}\ll B^{\kappa_{\rm ht}}.
\]

Then the four final exponents are

\[
1-\delta_{\rm loc}-\delta_{\rm glob}-\delta_{\rm ht},
\]

\[
\kappa_{\rm loc}-\delta_{\rm glob}-\delta_{\rm ht},
\qquad
\kappa_{\rm glob}-\delta_{\rm ht},
\qquad
\kappa_{\rm ht}.
\]

A square-root upper bound requires every one of them to be at most `1/2+o(1)`.

At present none of `delta_loc`, `kappa_loc`, `delta_glob`, `kappa_glob`, `delta_ht`, or `kappa_ht` has been proved. The first missing quantity in the actual proof chain is already `rho_loc/E_loc`: the centered prime-level s5g candidate has not yet been promoted to a full local-indicator theorem.

## First quantitatively insufficient component

The first obstruction is therefore **not** a bad numerical choice of `Q`. It is the missing conversion

```text
centered prime-level second moment
        -> full local 2-descent indicator bound
        -> explicit rho_loc(B,Q), E_loc(B,Q).
```

The benchmark `Q_*(B)=B^(1/4-eta)` shows where such a theorem should operate without paying a super-volume `Q^4` cost on bulk boxes. But until the reciprocal off-diagonal expansion is controlled, the local retainer cannot even be inserted quantitatively into 4as.

Even after that gap is closed, 4aq currently gives no positive `delta_glob`, and 4ar gives no positive `delta_ht`; so a square-root theorem would still require new global/Sha and/or small-point input. The local conversion is simply the **first** unresolved quantitative interface in the ordered chain.

## A useful conditional checkpoint

If a future local conversion at the benchmark depth gives `rho_loc=O(1)` only, then it contributes no power saving regardless of how well the `Q^4` term is controlled. If it gives a positive local power saving but the global and height retainers remain only `O(1)`, the combined exponent still cannot reach `1/2` unless `delta_loc>=1/2`. Thus the architecture makes immediately visible how much saving each later gate must supply.

No such exponent is claimed here.

## Boundary

```text
STAGE14_4AT=DYADIC_Q_BUDGET_INSTANTIATED_AND_FIRST_QUANTITATIVE_GAP_IDENTIFIED
DYADIC_EUCLID_BOX_COUNT=O_LOG2_B
BULK_BOX_VOLUME_SCALE=O_B
S5G_Q4_TRANSITION_THETA=1/4
BENCHMARK_Q_B= B^(1/4-eta)
BOX_ADAPTIVE_Q_CLIPPED=true
S5G_SECOND_MOMENT_IS_LOCAL_INDICATOR_BOUND=false
E_LOC_IDENTIFIED_WITH_Q4=false
RHO_LOC_EXPLICITLY_PROVED=false
E_LOC_EXPLICITLY_PROVED=false
FIRST_QUANTITATIVE_GAP=FULL_LOCAL_INDICATOR_CONVERSION
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No family large-sieve theorem, full local-indicator bound, propagated square-root error budget, positive global/Sha exponent, positive height exponent, or `sqrt(B)` asymptotic is proved.

```text
NEXT=Stage14-4au close the first local quantitative gap by expanding the full centered local indicator on dyadic Euclid boxes and deriving explicit rho_loc/E_loc bounds, or isolate the reciprocal off-diagonal obstruction in coordination with Stage14-s5h
```
