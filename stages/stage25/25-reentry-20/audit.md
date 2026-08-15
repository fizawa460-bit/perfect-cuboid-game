# Stage25-reentry-20 hostile audit — PASS

```text
TASK_ID=Stage25-u24-r002a
REENTRY_PHASE=20
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
```

## Verdict

The phase20 directional strengthening is accepted.

The new mathematical point is the R501 cone `9/2<t<5`. For the audited R501 formulas

`A=16t^2(t^4-9)`,
`B=(t^4-10t^2+9)(t^4+2t^2+9)`,
`C=4t(t^2+3)(t^4-10t^2+9)`,

we independently checked the exact factorizations

`B-C=(t-3)(t-1)(t+1)(t+3)Q1(t)`
with `Q1=t^4-4t^3+2t^2-12t+9`, and

`A-C=-4t(t^2+3)Q2(t)`
with `Q2=t^4-4t^3-10t^2+12t+9`.

On `9/2<t<5`, `Q1' = 4(t-3)(t^2+1)>0` and `Q1(9/2)=657/16>0`, hence `B>C`. Also `Q2'=4H`, `H=t^3-3t^2-5t+3`; `H` is positive and increasing from `9/2`, so `Q2` is increasing, while `Q2(5)=-56<0`. Therefore `Q2(t)<0` for `t<5`, hence `A>C`. Thus `C` is strictly the smallest raw edge throughout the cone and remains so after primitive reduction, making it canonical shared edge `a`.

The counting transfer is valid: the reduced parameters `m=5n-k`, `1<=k<n/2`, `gcd(k,n)=1`, `n<=T/5` give `asymp T^2` parameters in the cone, the audited R501 space height remains degree eight and primitive reduction only lowers height, and the invariant `C/D` gives a nonzero polynomial fiber equation of degree at most eight. The third-face condition is still the same raw `(A,B)` condition as in audited R501, so the same squarefree degree-16 / genus-seven Faltings exception argument applies. Consequently

`N2,a(B) >> B^(1/4)`.

The previously audited R501 cone gives canonical shared edge `b`, and audited R502 gives canonical order `0<A<B<C` with the guaranteed faces sharing `C`, hence canonical shared edge `c` and `N2,c(B)>>B^(1/4)`. Therefore

`N2,j(B) >>_j B^(1/4)` for `j=a,b,c`.

Combining with the audited Stage18 directional asymptotics `M2,j(B)~C_j B(log B)^5`, `C_j>0`, gives the stated Stage24 directional lower ratios and positive-divergent `J2,j`. The Stage23 pair-overlap consequences follow from which two canonical faces meet at shared edge `a`, `b`, or `c`.

## Scope firewall

Accepted:
- all three canonical shared-edge Stage19 chambers have quarter-power lower families;
- the corresponding directional Stage24 survival lower is `B^(-3/4)(log B)^(-5)` in every chamber;
- all three Stage23 pair-overlap channels receive quarter-power lower candidates for audited backflow.

Not claimed:
- any improvement of the global `N2(B)>>B^(1/4)` exponent;
- identification of the true `N2` exponent;
- a strict whole-family upper below half-power;
- moving-family/growing-modulus uniformity;
- reopening the audited external R503/R504/R505 gates;
- any perfect-cuboid existence or nonexistence conclusion.

## Backflow gate

The theorem-changing Stage19/23/24 backflow is correctly not applied inside the unaudited submission. Fresh audit PASS authorizes reserved derived route `Stage25-um-r008a`, but that route is not treated as already executed. Phase30 remains blocked until the audited phase20 PR is merged and the authorized backflow route is synchronized.

Submission-head CI `4354f5166b36a208f88d701dba2c9fa97774df87` passed:
- Stage25 reentry phase20 directional audit;
- Stage25 reentry roadmap contract;
- Stage25-70 closeout audit;
- Stage25 reentry phase10 interface synchronization.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
ADVANCE_ALLOWED=true
CURRENT_REENTRY_PHASE=20
NEXT_REENTRY_PHASE=20
PHASE20_STATUS=AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW
LIVE_DERIVED_ROUTES=NONE
QUEUED_PROPAGATION_PROPOSALS=Stage25-um-r008a
MERGE_ALLOWED=true
STAGE26_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #1003; then Stage25-reentry-main-batch
```
