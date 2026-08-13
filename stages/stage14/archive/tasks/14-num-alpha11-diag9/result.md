# Stage14-numα11-diag9 — shell survival drift and bridge residual

## Result

diag9 converts the cumulative diag8 panel through `B=1,000,000` into seven disjoint shells and separates the shell-to-shell exactly-two directional motion into two factors:

1. the Stage13-style raw source-face composition;
2. the conditional probability of acquiring a second integral face.

The exact bridge is

```text
endpoint_q ∝ raw_q × second-face-survival_q.
```

For a hypothetical exactly-two pair law `a:b:c=2:2:1`, the equivalent endpoint law is `ab:ac:bc=4:3:3`. Combining that with the proved Stage13 limiting source vector gives the previously derived target relative survival

```text
S_ab:S_ac:S_bc = 0.54831669:0.89625296:1.
```

## Raw source population is extremely stable shell-to-shell

Across all seven shells the raw source proportions stay close to

```text
ab ≈ 50.0%
ac ≈ 25.8%
bc ≈ 24.0%
```

For example:

```text
(100k,200k] : 0.501456, 0.258557, 0.239987
(500k,750k] : 0.503771, 0.257980, 0.238249
(750k,1m]   : 0.501606, 0.259774, 0.238620
```

Thus the source population itself is not visibly responsible for the large shell swings seen in exactly-two directions.

## Second-face survival is the volatile factor

Relative to `bc=1`, shell survival is

```text
(0,100k]     0.5704 : 0.9427 : 1
(100k,200k]  0.6913 : 0.5157 : 1
(200k,300k]  0.6146 : 0.7992 : 1
(300k,400k]  0.5645 : 0.9830 : 1
(400k,500k]  0.6746 : 1.0116 : 1
(500k,750k]  0.5864 : 0.8866 : 1
(750k,1m]    0.6796 : 1.3122 : 1
```

The corresponding exactly-two pair shell counts are

```text
(33,33,23)
(9,17,1)
(8,10,4)
(11,10,8)
(9,8,4)
(15,16,9)
(13,7,7)
```

so the late shell fluctuations remain large even though the raw source vector barely moves.

## Counterfactual volatility decomposition

Two counterfactual endpoint series were formed.

- **source-only:** keep each shell's actual raw source composition but fix survival to the hypothetical Stage13-limit + `2:2:1` bridge profile;
- **survival-only:** fix the source population at the proved Stage13 limit but keep each shell's actual survival profile.

Unweighted shell RMS dispersion is

```text
actual endpoint                       0.0692273
source-only counterfactual            0.00242820
survival-only counterfactual          0.0677177
survival/source RMS ratio             27.8881
```

Weighting shells by their exactly-two count gives

```text
actual endpoint                       0.0610908
source-only counterfactual            0.00264040
survival-only counterfactual          0.0598661
survival/source RMS ratio             22.6731
```

Therefore essentially all of the observed **shell-to-shell volatility** is carried by the second-face survival factor, not by movement of the Stage13-style source population.

This statement is about volatility, not about the signed mean offset from the hypothetical `4:3:3` target. A symmetric two-factor Shapley vector decomposition is also computed in the script so source and survival residual vectors add exactly to the observed endpoint residual; their L1/L2 magnitudes need not add because the two effects can cancel.

## Critical boundary

The shell exactly-two counts are still only

```text
21 <= N2_shell <= 89.
```

Therefore diag9 does **not** establish arithmetic shell heterogeneity. The survival-side series is mathematically the volatile factor after conditioning, but the volatility may still be largely finite multinomial/Poisson sampling noise.

The next diagnostic must test that null directly.

```text
STAGE14_NUM_ALPHA11_DIAG9=SHELL_SECOND_FACE_SURVIVAL_DRIFT_AND_BRIDGE_RESIDUAL_COMPLETE
SHELL_COUNT=7
RAW_SOURCE_SHELL_PROPORTION_STABLE_AT_PERCENT_SCALE=true
UNWEIGHTED_SURVIVAL_TO_SOURCE_RMS_RATIO=27.888062705291098
N2_WEIGHTED_SURVIVAL_TO_SOURCE_RMS_RATIO=22.673066726410056
SURVIVAL_SIDE_COUNTERFACTUAL_VOLATILITY_DOMINATES_SOURCE_SIDE=true
SHELL_N2_SMALL_ENOUGH_THAT_SAMPLING_NOISE_REMAINS_A_MAJOR_ALTERNATIVE=true
ARITHMETIC_SHELL_HETEROGENEITY_PROVED=false
ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM=false
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NEXT=Stage14-num-alpha11-diag10 finite-count heterogeneity test for shell survival
```
