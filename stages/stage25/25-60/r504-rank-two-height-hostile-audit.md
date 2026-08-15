# Stage25-60 R504 rank-two height hostile audit

Status: **FAIL; NARROW REPAIR REQUIRED; CHECKPOINT60 CONTINUES**

ROUTE=R504
CHECKPOINT=60
PR=995

## Verdict

The Rosati/height quadratic form on the known rank-two sublattice is accepted, but the submitted identification of the entire physical 2-cover coset with coefficient parity

\[
a\equiv1\pmod 2,\qquad b\equiv0\pmod 2
\]

is not yet proved. Therefore the downstream claims that norm `5` is the first nondegenerate physical class and that `1/12` is the best fixed-class exponent in the whole known rank-two lattice are not accepted in this audit.

This is a narrow boundary failure. The previously audited `P+2R` family `Theta(B^(1/12))` remains valid and is not reopened.

## Accepted mathematics

On the untwisting genus-three cover, the two known directions have distinct `V4` differential characters. Hence the Rosati cross term vanishes. The basis degrees are both `8`, so for the homomorphism/free-section direction represented by

\[
Q=aP+bR
\]

the accepted quadratic degree formula is

\[
\boxed{\deg_u(x(Q)/H)=8(a^2+b^2)}.
\]

For any class already known independently to lie on the physical quartic 2-cover, the receiver

\[
\frac{x(Q)}H=-\frac{4t^2}{t^4+1}
\]

has degree `4` in `t`, so

\[
\boxed{\deg_u t=2(a^2+b^2)}
\]

for that physical class. The fixed-class projective edge map has no nonconstant common factor, so primitive specialization changes height only by a class-dependent absolute constant. Thus the conditional fixed-class box-degree formula

\[
\boxed{L(a,b)=4+4(a^2+b^2)}
\]

is accepted whenever physical lift membership for the class has separately been established.

```text
R504_ROSATI_HEIGHT_FORM_ACCEPTED=true
R504_ROSATI_CROSS_TERM_ACCEPTED=0
R504_ROSATI_NORM_P_ACCEPTED=8
R504_ROSATI_NORM_R_ACCEPTED=8
R504_X_OVER_H_DEGREE_FORM_ACCEPTED=8*(a^2+b^2)
R504_PHYSICAL_T_DEGREE_FORM_CONDITIONAL_ACCEPTED=2*(a^2+b^2)
R504_FIXED_CLASS_BOX_DEGREE_FORM_CONDITIONAL_ACCEPTED=4+4*(a^2+b^2)
```

## Audit blocker: mod-2 physical-coset identification

A rational point on a 2-cover maps to a coset of `2E(K)` in the Jacobian. To conclude that the intersection with the known sublattice `<P,R>` is exactly

\[
P+2\langle P,R\rangle
\]

one needs a mod-2 / saturation certificate for the classes of `P` and `R` in the ambient Mordell-Weil group, or an equivalent explicit 2-descent character calculation.

The currently materialized facts are:

- `P` is the inherited physical class (degenerate at the original generator level);
- `R` itself is not a physical quartic lift;
- `P+R` and `P-R` are not physical lifts;
- `P+2R` is a physical lift.

These finite coset samples do not by themselves prove the coefficient rule for every `aP+bR`. In particular, the submission has not materialized a proof that `<P,R>` is 2-saturated in the relevant ambient free lattice, nor an explicit pair of independent mod-2 descent characters whose kernel/coset gives exactly `a odd, b even`.

Accordingly the following are **not yet accepted**:

```text
R504_PHYSICAL_COSET_A_ODD_B_EVEN_ACCEPTED=false
R504_RANK_TWO_MOD2_SATURATION_CERTIFICATE=false
R504_RANK_TWO_2DESCENT_CHARACTER_CERTIFICATE=false
R504_MIN_NONDEGENERATE_NORM_5_ACCEPTED=false
R504_BEST_FIXED_CLASS_EXPONENT_1_12_GLOBAL_WITHIN_KNOWN_LATTICE_ACCEPTED=false
```

A potential norm-4 class such as `2R` need not actually be physical; the point is that the present artifact has not yet supplied the theorem that excludes it. No counterexample is asserted.

## Existing theorem firewall

The explicit `P+2R` physical family from the preceding hostile audit remains fully accepted:

\[
N_{R504,P+2R}(B)=\Theta(B^{1/12}).
\]

Likewise the global Stage25 lower remains

\[
N_2(B)\gg B^{1/4}.
\]

No previously audited Stage19 result is reopened.

```text
R504_P_PLUS_2R_PREVIOUS_THEOREM_REOPENED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
```

## Discovery / reuse audit

The current-round reuse handoff and discovery ledger are complete for this theorem chunk. The failure is not a discovery-ledger failure; it is a missing proof at the physical-coset boundary.

```text
REPO_REUSE_PREFLIGHT=PASS
DISCOVERY_LEDGER_STATUS=COMPLETE_FOR_THIS_THEOREM_CHUNK
DISCOVERY_AUDIT_VERDICT=PASS
```

## Required repair

Provide one of the following equivalent certificates:

1. an explicit 2-descent/Kummer character computation showing that physical lift membership inside `<P,R>` is exactly `a odd, b even`; or
2. a proof that the relevant physical image is `P+2E(K)` together with a 2-saturation/mod-2 independence certificate for `P,R` sufficient to identify its intersection with `<P,R>`; or
3. a direct symbolic physical-lift criterion for general `aP+bR` whose parity reduction is proved, not sampled.

After that repair, the Rosati norm calculation can be reused without reopening it.

## Audit footer

```text
PREVIOUS_AUDIT_VERDICT=PASS
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_ROSATI_HEIGHT_FORM_ACCEPTED=true
R504_PHYSICAL_COSET_PARITY_ACCEPTED=false
R504_RANK_TWO_MOD2_SATURATION_CERTIFICATE=false
R504_MIN_NONDEGENERATE_NORM_5_ACCEPTED=false
R504_BEST_FIXED_CLASS_EXPONENT_1_12_ACCEPTED=false
R504_P_PLUS_2R_EXACT_FAMILY_GROWTH_RETAINED=Theta(B^(1/12))
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
