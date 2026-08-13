# Stage14-4ap — character-sum reach and conditional global/height transfer

## Result

The merged s5g audit shows that the prime-level quadratic-character family must be centered by its exact finite-field mean. Raw traces have exact local resonances at `p=3,5,17`; therefore an uncentered cancellation statement is false even before global arithmetic enters.

After centering, a family large-sieve estimate would still control only the local-admissibility gate. Write

\[
N_0=A(B),\qquad N_1=\Sigma(B),\qquad N_2=R(B),\qquad N_3=\mathcal H(B;C).
\]

Then, with zero-denominator ratios interpreted as zero,

\[
N_3=N_0\frac{N_1}{N_0}\frac{N_2}{N_1}\frac{N_3}{N_2}.
\]

The centered local character system can address `N1/N0`. It does not determine whether a locally soluble cover has a rational point (`N2/N1`, including Sha), nor whether the first rational point enters the s3 logarithmic canonical-height window (`N3/N2`). Those are distinct arithmetic inputs.

## Conditional transfer contract

Suppose, uniformly in the family, that

\[
N_0(B)\ll B,
\quad \frac{N_1}{N_0}\ll B^{-\delta_{\rm loc}},
\quad \frac{N_2}{N_1}\ll B^{-\delta_{\rm glob}},
\quad \frac{N_3}{N_2}\ll B^{-\delta_{\rm ht}}.
\]

Multiplication gives the rigorous conditional implication

\[
\mathcal H(B;C)\ll
B^{1-\delta_{\rm loc}-\delta_{\rm glob}-\delta_{\rm ht}}.
\]

Since 4ao locked `V(B) <= H(B;C)`, the same conditional upper bound transfers to `V(B)`. Reaching a square-root upper-bound scale requires the combined saving

\[
\delta_{\rm loc}+\delta_{\rm glob}+\delta_{\rm ht}\ge \tfrac12.
\]

This is exponent bookkeeping, not an assertion that any of the three uniform retainer estimates has been proved.

## Finite diagnostic

At `H<=20,000`, the exact census remains

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.8174827369742624
V/R in [0.012738853503184714,0.01427061310782241]
```

Thus the finite local gate is common, while the observed small-point gate is severe. These values do not supply asymptotic exponents.

## Boundary

```text
STAGE14_4AP=LOCAL_CHARACTER_REACH_AND_CONDITIONAL_GLOBAL_HEIGHT_TRANSFER_BOUNDARY
EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true
LOCAL_CHARACTERS_DETERMINE_GLOBAL_SOLUBILITY=false
LOCAL_CHARACTERS_DETERMINE_FIRST_SMALL_POINT_HEIGHT=false
LOCAL_LARGE_SIEVE_ALONE_CONTROLS_HEIGHT_WEIGHTED_COUNT=false
CONDITIONAL_THREE_RETAINER_TRANSFER_FORMULATED=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No family large-sieve theorem, global-solubility density, first-small-point lower-tail theorem, power saving, or `sqrt(B)` asymptotic is claimed.

```text
NEXT=Stage14-4aq isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve
```
