# Stage14 — exactly-two integral-face population

Current canonical source: `stages/stage14/main.md`, with the latest gate boundary recorded in `14-4aq/result.md` and `roadmap.md`.

```text
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
STAGE14_4AO=COMPLETE_FULL_LOCAL_MATRIX_AND_HEIGHT_WEIGHTED_COUNTING_INTERFACE
STAGE14_4AP=LOCAL_CHARACTER_REACH_AND_CONDITIONAL_GLOBAL_HEIGHT_TRANSFER_BOUNDARY
STAGE14_4AQ=GLOBAL_SHA_RETAINER_ISOLATED_AND_WEIGHTED_TARGET_FORMULATED
MAX_VERIFIED_B=2000000
FULL_RANK_SELMER_CENSUS_MAX_H=20000
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=true
FULL_LOCAL_SELMER_MATRIX_COMPLETE=true
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true
SHA_TRAP_INDICATOR_EXACT=true
GLOBAL_RETAINER_IDENTITY_R_EQ_SIGMA_MINUS_SHA_TRAP=true
GLOBAL_RETAINER_UNIFORM_AVERAGING_TARGET_FORMULATED=true
GLOBAL_SOLUBILITY_DENSITY_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4ar isolate the positive-rank-to-first-small-point retainer and formulate a uniform weighted lower-tail target using the s3 height window
```

## Current reduction

For a primitive oriented Pythagorean base `F=(S,X,H)`,

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2)
\]

has full rational 2-torsion. The fixed rational-curve square-root mechanism is closed by 4ak, so the count is collective.

Stage14-4am separates

```text
A ⊇ Sigma ⊇ R ⊇ V,
V/A=(Sigma/A)(R/Sigma)(V/R).
```

At `H<=20,000`:

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427]
```

so the dominant finite thinning is after positive rank, at the first-small-point gate.

## Local gate: 4an–4ap

Using the global square-class relation, the selected s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Merged s5d supplies all unselected odd rows, and merged s5f leaves exactly 8 covering-soluble `Q_2` states among the 64 product-square states. Thus the full local 2-descent character system is explicit.

Stage14-4ap imports the s5g centering obstruction: a centered local character estimate can address only `Sigma/A`. Global solubility/Sha and first-small-point height remain distinct retainers. Conditional exponents add, but no individual power saving is proved.

## 4aq — exact global/Sha split

Because the family has full rational 2-torsion,

\[
0\to E(\mathbf Q)/2E(\mathbf Q)\to\operatorname{Sel}_2(E)\to\Sha(E)[2]\to0
\]

implies

\[
\dim Sel_2(E)=2+\operatorname{rank}E(\mathbf Q)+\dim\Sha(E)[2].
\]

For base indicators `s(F)=1_{dim Sel_2>2}` and `r(F)=1_{rank>0}`, the exact Sha-trap indicator is `tau(F)=s(F)-r(F)`. Hence

\[
R(B)=\Sigma(B)-T_{\Sha}(B),\qquad R/\Sigma=1-T_{\Sha}/\Sigma.
\]

The identity is compatible with any nonnegative centered-local sieve weight `W_Q`: if `S_Q=sum W_Q s`, `G_Q=sum W_Q r`, and `T_Q=sum W_Q tau`, then exactly `G_Q=S_Q-T_Q`. The uniform global target is therefore

\[
G_Q\le\rho_{glob}(B,Q)S_Q+E_{glob}(B,Q),
\]

or equivalently a lower bound on the weighted Sha-trap term. No global density or positive `B`-power saving is assumed.

At `H<=20,000`, the rank interval implies `970..1425` Sha-trap bases among `Sigma=5209`, so `R/Sigma` lies in `0.7264..0.8138`. This is a substantial constant-factor gate, not evidence for a positive asymptotic thinning exponent.

## Next

`Stage14-4ar` isolates the positive-rank-to-first-small-point retainer and formulates the uniform weighted lower-tail target dictated by s3. This is the gate that finite data currently identify as the dominant source of thinning.

Primary 4aq artifacts:

```text
stages/stage14/14-4aq/result.md
stages/stage14/data/14-4/global_sha_retainer_summary.json
stages/stage14/scripts/14-4/global_sha_retainer_audit.py
.github/workflows/stage14-4aq-global-sha-retainer.yml
```
