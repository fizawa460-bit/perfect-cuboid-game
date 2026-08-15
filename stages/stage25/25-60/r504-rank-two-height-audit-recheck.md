# Stage25-60 R504 rank-two height hostile re-audit

Status: **PASS AFTER NARROW MOD-2 REPAIR; CHECKPOINT60 CONTINUES**

ROUTE=R504
CHECKPOINT=60
PR=995
PREVIOUS_AUDIT_VERDICT=FAIL

## Verdict

The narrow hostile-audit blocker is repaired. The full-rational-2-torsion Kummer map on

\[
E_H:y^2=x(x-2H)(x+2H)
\]

is used with

\[
\delta(Q)=([x],[x-2H],[x+2H])\in(K^*/K^{*2})^3,\qquad K=\mathbf Q(u).
\]

Its kernel is `2E_H(K)`. Exact factorization gives

```text
KUMMER_P=(-1,-2,2)
KUMMER_R=(1,2,2)
```

and these classes are independent mod `2` because `-1` and `2` are non-square constants in `Q(u)`.

For every nondegenerate physical quartic point, writing `w=M^2/z` gives

\[
H=w^2(t^4+1),\quad x=-4w^2t^2,
\]
\[
x-2H=-2w^2(t^2+1)^2,\quad x+2H=2w^2(t^2-1)^2,
\]

so the physical Kummer class is exactly `KUMMER_P`.

Conversely, from a point with that Kummer class choose

\[
x=-4r^2,\quad x-2H=-2q^2,\quad x+2H=2s^2.
\]

Then

\[
t=(q+s)/(2r),\qquad w=(q-s)/2
\]

satisfies `H=w^2(t^4+1)` and reconstructs the physical quartic. Therefore the physical image is exactly

\[
\boxed{P+2E_H(K)}.
\]

Hence for `Q=aP+bR`, Kummer homomorphy gives

\[
\boxed{Q\text{ physical}\iff a\equiv1\pmod2,\ b\equiv0\pmod2.}
\]

No ambient 2-saturation assumption is needed.

## Reused accepted height theorem

The previous hostile audit already accepted

\[
\deg_u(x(aP+bR)/H)=8(a^2+b^2),
\]

and, conditional on physicality,

\[
\deg_u t=2(a^2+b^2),\qquad L(a,b)=4+4(a^2+b^2).
\]

The repaired parity theorem makes these formulas unconditional on the physical subcoset. Norm `1` is only the degenerate `+/-P` class. The first nondegenerate physical norm is `5`, attained by `(+/-1,+/-2)`. The already audited `P+2R` class attains

\[
\deg t=10,\qquad L=24,
\]

and

\[
N_{R504,P+2R}(B)=\Theta(B^{1/12}).
\]

Therefore `1/12` is the best fixed-class exponent inside the known rank-two sublattice.

## Scope firewall

This PASS closes only the fixed-class physical-coset height classification in `<P,R>`. It does not prove a uniform summation over coefficient pairs growing with `B`, does not prove the full pulled-back Mordell-Weil rank is exactly `2`, and does not close the full-split Prym / `E0`-isogeny residual.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_ROSATI_HEIGHT_FORM_ACCEPTED=true
R504_RANK_TWO_2DESCENT_CHARACTER_CERTIFICATE=true
R504_PHYSICAL_IMAGE=P+2E_H(Q(u))
R504_PHYSICAL_COSET_PARITY_ACCEPTED=true
R504_PHYSICAL_COSET=a_odd,b_even
R504_MIN_NONDEGENERATE_NORM_5_ACCEPTED=true
R504_BEST_FIXED_CLASS_EXPONENT_1_12_ACCEPTED=true
R504_RANK_TWO_FIXED_CLASS_HEIGHT_CLASSIFICATION_AUDITED_PASS=true
R504_RANK_TWO_GROWING_LATTICE_UNIFORM_AGGREGATION_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #995; then Stage25-main-batch at checkpoint60
```
