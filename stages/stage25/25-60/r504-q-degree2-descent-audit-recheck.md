# Stage25-60 R504 complete Q-degree-2 source descent hostile re-audit

Status: **PASS FOR DESCENT REPAIR; CHECKPOINT60 CONTINUES**

## Scope

This re-audit reviews the repair to the previous hostile FAIL on PR #992. The previous FAIL remains authoritative history for the overbroad claim that `(a u^2+b)/(u^2+1)` was a complete Q-rational degree-two normal form.

The current repair changes the equivalence problem to the correct R504 one: target coordinate `k` fixed, source reparametrization only by `PGL_2(Q)`.

## Independent verification

Let `phi in Q(u)` have degree two. Then `[Q(u):Q(phi)]=2`. In characteristic zero the extension is separable; every separable quadratic extension is Galois, so it has a unique nontrivial deck automorphism. Because it fixes `Q(phi)` and hence `Q`, it lies in `Aut_Q Q(u)=PGL_2(Q)`.

An involution in `PGL_2(Q)` may be represented by a trace-zero matrix

`M=[[p,q],[r,-p]]`, with `M^2=(p^2+qr) I`.

Since `M` is invertible, `p^2+qr != 0`. The squareclass of `p^2+qr` is the fixed-point discriminant squareclass.

- Split squareclass: the involution has two Q-rational fixed points and is Q-conjugate to `u -> -u`; its fixed field is `Q(u^2)`.
- Nonsplit squareclass `d`: the involution is Q-conjugate to `u -> d/u`; its fixed field is `Q(u+d/u)`.

Because `Q(phi)` equals the corresponding fixed field, if `t` denotes `u^2` or `u+d/u`, then `Q(phi)=Q(t)`. Two Q-generators of a rational function field differ by a Möbius transformation, so `phi=M_0(t)` with `M_0 in PGL_2(Q)`. This yields exactly the submitted normal-form species

- split: `(A*u^2+B)/(C*u^2+D)`;
- nonsplit: `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`;

with `AD-BC != 0`, and `d` defined modulo Q-squares.

The word “species” is important: this audit does not assert uniqueness of the coefficient tuple `(A,B,C,D)` after residual source centralizer actions. It certifies completeness of the split/nonsplit source-equivalence classification.

## Verdict on the repair

The previous normalization blocker is repaired.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_Q_DEGREE2_SOURCE_EQUIVALENCE=TARGET_FIXED_SOURCE_PGL2_Q
R504_Q_DEGREE2_DECK_INVOLUTION_DEFINED_OVER_Q=true
R504_Q_DEGREE2_INVOLUTION_CLASSES=SPLIT_OR_NONSPLIT_SQUARECLASS
R504_Q_DEGREE2_COMPLETE_DESCENT_ACCEPTED=true
R504_PREVIOUS_EVEN_NORMAL_FORM_COMPLETE_CLAIM=false
R504_PREVIOUS_EVEN_NORMAL_FORM_SCOPE=STRICT_SPLIT_SUBFAMILY
```

## Scope firewall

This PASS does **not** close the degree-two route. The submitted even-family symbolic elimination remains valid only for its strict split subfamily. The complete split family and all nonsplit squareclasses still require analysis.

```text
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_FULL_Q_RATIONAL_EXTRA_INVOLUTION_LOCUS_CLOSED=false
R504_PRYM_AS_SOLE_DEGREE2_RESIDUAL_ACCEPTED=false
R504_EXTERNAL_THEOREM_GATE_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #992; then Stage25-main-batch at checkpoint60
```
