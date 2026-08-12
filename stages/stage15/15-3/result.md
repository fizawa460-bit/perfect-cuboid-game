# Stage15-3 — matched numerical A/B comparison under one denominator

Base: merged Stage15-2b (`PR #828`, main merge commit `44797f4`). Stage15-2b proved

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

while Stage14 supplies the integral-space-diagonal subpopulation `N_2(B)`. Stage15-3 is deliberately numerical: it measures what `R\in\mathbf Z` removes when both populations are counted with the exact same primitive/canonical convention and the exact same real geometric cutoff

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}\le B.
\]

No finite-data slope or ratio is promoted to an asymptotic theorem here.

## 1. Frozen verdict

The matched baseline is complete through `B=100000`.

```text
STAGE15_3_COMMON_CUTOFF=R<=B
STAGE15_3_MAX_EXACT_BOUND=100000
STAGE15_3_M2_AT_MAX=796698
STAGE15_3_N2_AT_MAX=89
STAGE15_3_SURVIVAL_RATIO_AT_MAX=0.00011171108751371284
STAGE15_3_GLOBAL_N2_SLOPE_GATE=false
STAGE15_3_DIRECTIONAL_RATE_GATE=false
STAGE15_3_FINITE_DATA_ASYMPTOTIC_CLAIM=false
STAGE15_3_EXIT=MATCHED_NUMERICAL_BASELINE_COMPLETE
```

The numerical picture is therefore strong enough to diagnose mechanisms, but not strong enough to infer a survival exponent from the `N_2` data alone.

## 2. Exact cumulative comparison

All counts below are exact outputs of the same shared-edge generator used by the validated Stage15 paired enumerator.

| `B` | `M_2(B)` | `N_2(B)` | `N_2/M_2` | local slope `M_2` | local slope `N_2` |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 1,838 | 2 | 1.08814e-3 | — | — |
| 2,000 | 4,812 | 5 | 1.03907e-3 | 1.3885 | 1.3219 |
| 5,000 | 16,710 | 15 | 8.97666e-4 | 1.3586 | 1.1990 |
| 10,000 | 41,666 | 25 | 6.00010e-4 | 1.3182 | 0.7370 |
| 20,000 | 102,522 | 42 | 4.09668e-4 | 1.2990 | 0.7485 |
| 50,000 | 331,731 | 62 | 1.86898e-4 | 1.2815 | 0.4250 |
| 100,000 | 796,698 | 89 | 1.11711e-4 | 1.2640 | 0.5215 |

The ambient local slope decreases slowly, exactly as expected for a function of shape `B(log B)^5`: its effective log-log slope is `1+5/log B+o(1)`, hence remains above one at these bounds. This is only a consistency check because Stage15-2b already proved the ambient asymptotic.

The survivor count is too small for the displayed `N_2` slopes to be interpreted. Stage15-3 predeclares a minimum of `N_2>=200` before any global survivor-slope interpretation. The maximum-bound count is only `89`, so the gate fails.

The observed survival ratio falls from about `1.09e-3` at `B=1000` to `1.12e-4` at `B=100000`. This is strong finite evidence of thinning, but it is not a proof of any power law or density statement beyond what is already independently certified.

## 3. Directional comparison

At `B=100000`, with directions `a,b,c` denoting the smallest, middle, and largest canonical edge as the unique shared edge,

| direction | `M_2` | `N_2` | observed ratio |
|---|---:|---:|---:|
| `a` | 253,718 | 33 | 1.30065e-4 |
| `b` | 339,972 | 33 | 9.70668e-5 |
| `c` | 203,008 | 23 | 1.13396e-4 |

The ambient direction split is already large enough to be numerically stable. The survivor split is not: Stage15-3 requires at least `50` survivors in **each** direction before interpreting directional survival-rate differences. The current vector `(33,33,23)` fails that gate.

Thus the data do not justify saying that the space-diagonal condition preferentially kills one direction.

## 4. Space-diagonal defect

Define

\[
\Delta_R=\operatorname{nearestSquare}(R^2)-R^2,
\qquad
\delta_R=\frac{\Delta_R}{2R}.
\]

The normalization makes `delta_R` approximately the signed distance from `R` to the nearest integer. At `B=100000` over all `796698` ambient exactly-two boxes:

```text
mean(delta_R)       = -0.0005460574
median(delta_R)     = -0.0007456009
mean(|delta_R|)     =  0.2481787031
median(|delta_R|)   =  0.2470147504
10%-90% delta range = [-0.4001820, 0.3976198]
1%-99% delta range  = [-0.4899460, 0.4896922]
```

The ten equal-width bins on `[-1/2,1/2]` contain

```text
79946, 78067, 80860, 78002, 82697,
80238, 81141, 78660, 79742, 77345
```

points. The distribution is therefore visually/quantitatively close to flat at this coarse archimedean scale, with no visible pile-up near `delta_R=0`. This is a finite-data observation only; it is not an independence theorem for the square condition.

The directional mean absolute normalized defects are also nearly identical:

```text
a: 0.2488881858
b: 0.2489347049
c: 0.2460259407
```

so the elementary real-place defect distribution does not explain the tiny survivor count.

## 5. Exact local lemma exposed by the data

The modular scan shows that `R^2` is never divisible by `3`, `7`, or `11`. In fact there is a clean exact statement.

**Lemma.** Let `(e,x,y)` be a primitive shared-edge box with

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2.
\]

Then no prime `p\equiv3\pmod4` divides

\[
R^2=e^2+x^2+y^2.
\]

**Proof.** Since

\[
R^2=u^2+y^2=v^2+x^2,
\]

if `p\equiv3 (mod 4)` divides `R^2`, the sum-of-two-squares criterion modulo `p` forces `p|u,y` and `p|v,x`. From `u^2=e^2+x^2`, with `p|u,x`, one gets `p|e`. Hence `p|e,x,y`, contradicting primitivity. ∎

Thus every prime divisor of ambient `R^2` is either `2` or `1 mod 4`. This is a genuine arithmetic restriction already present **before** imposing `R\in\mathbf Z`; it should be carried into Stage15-4 when the extra square condition is normalized.

At `B=100000` the observed `R^2 mod 8` counts are exactly

```text
1 : 445200
2 : 190882
5 : 160616
```

with no other residues. The evidence file also records small-prime valuation-parity signatures for `R^2` and `|Delta_R|`; these are local squareclass diagnostics, not full squarefree-kernel factorizations.

## 6. Statistical discipline

Two interpretation gates are frozen before looking farther out:

```text
minimum N2 for global slope interpretation          = 200
minimum N2 in every direction for rate comparison  = 50
```

At `B=100000` they evaluate to

```text
global:      89 < 200       -> FAIL
directional: (33,33,23)     -> FAIL
```

Therefore Stage15-3 records no empirical survivor exponent, no directional survival law, and no claim that the observed ratio has stabilized.

## 7. Reproducible artifacts

- `stages/stage15/scripts/stage15_3_compare.py` — compact exact matched comparator; emits JSON and plot-ready TSV.
- `stages/stage15/evidence/stage15_3_baseline.json` — frozen exact baseline through `B=100000`.
- `stages/stage15/replay/verify_stage15_3.py` — small-bound exact replay and cross-check against the Stage15-1 enumerator.
- `.github/workflows/stage15-3-matched-comparison.yml` — dedicated CI.

The JSON contains cumulative counts, local log-log slopes, directional vectors, `Delta_R` quantiles/histogram, congruence data, and small-prime squareclass signatures. The TSV generated by the script is the canonical input for the cumulative-count, slope, and survival-ratio plots required by the roadmap.

## 8. Stage15-3 verdict and next target

The comparison has now separated three facts cleanly:

1. the ambient exactly-two population is large and has the proved `B(log B)^5` law;
2. the integral-space-diagonal survivors are extremely rare on the tested common denominator;
3. the coarse real defect `Delta_R/(2R)` looks essentially unexceptional, while nontrivial arithmetic restrictions on `R^2` are already forced by the two-face structure.

The next primary target is therefore Stage15-4: write `R\in\mathbf Z` as the simplest exact arithmetic condition in the ambient shared-edge/toric coordinates, carrying the `p\equiv3 (mod 4)` exclusion and the observed local squareclass structure explicitly rather than treating the square condition as a generic random event.
