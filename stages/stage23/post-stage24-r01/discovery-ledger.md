# Stage23 post-Stage24 reinvestigation — discovery ledger R01

## Trigger

Historical Stage23 closed before Stage24 checkpoint50 proved the target lower theorem

\[
N_2(B)\gg\sqrt{\log B}.
\]

Stage24 checkpoint50 and checkpoint60 are both audited PASS and merged. This lane reuses those later theorems without revoking historical Stage23 PASS.

## Reused theorem interfaces

1. **Stage17 source:**
   \[
   N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
   \]
   and each pair-overlap channel is `o(B(log B)^3)`.

2. **Historical Stage23 upper:**
   \[
   N_2/N_1\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
   \]

3. **Stage24-50 lower breakthrough:**
   \[
   N_2(B)\gg\sqrt{\log B},
   \]
   with an infinite primitive exactly-two mixed-parity `C17` family.

4. **Stage22 no-space comparator:**
   \[
   M_2/M_1\sim C_{22}(\log B)^4/B,
   \quad C_{22}>0.
   \]

5. **Stage24-60 interaction algebra:**
   \[
   (\log B)^{-13/2}\ll
   \frac{N_2/N_1}{M_2/M_1}
   \ll_\varepsilon
   B^{1/2+\varepsilon}(\log B)^{-7}.
   \]

## Fresh deductions in this lane

### D1 — two-sided Stage23 ratio

\[
B^{-1}(\log B)^{-5/2}
\ll N_2/N_1
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

### D2 — transition classification

The target is simultaneously zero-density relative to the Stage17 source and provably unbounded:

```text
TRANSITION_CLASS=ZERO_DENSITY_WITH_INFINITE_TARGET
```

### D3 — specific overlap channel lower bound

The `C17` family has canonical assignment `(a,b,c)=(x,y,e)` and guaranteed integral faces `ac` and `bc`. Hence

\[
N_{2,c}(B)\gg\sqrt{\log B}
\]

and

\[
A_{ac,bc}(B)\gg\sqrt{\log B}.
\]

This is new relative to historical Stage23, which had only the overlap upper `o(B(log B)^3)`.

### D4 — arithmetic heterogeneity is structural, not a finite-data observation

- old odd/odd Stage15-2 slice: zero integral-space lifts by mod 16;
- mixed-parity `C17` slice: infinitely many exactly-two integral-space lifts.

Thus a single algebraic ambient family can split into dead and infinite arithmetic strata after imposing space integrality.

### D5 — Stage22 vs Stage23 interaction sign remains unresolved

The new Stage23 lower bound sharpens the comparison but the cross-ratio bounds still straddle `1`. No global positive/negative/independent interaction sign is certified.

## Searches/rechecks performed

- historical Stage23 controller and closeout bundle;
- Stage17 final source asymptotic and pair-overlap interface;
- Stage22 controller and sharp no-space ratio;
- Stage24-50 result and fresh audit;
- Stage24-60 audited/merged interaction synthesis;
- existing Stage23 post-Stage24 supersession addendum.

No new census extension is needed. No finite sample is used to prove any asymptotic statement.

## Numerical reuse

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NONE
NUM_POPULATION_MATCH=NOT_APPLICABLE
NUM_EVIDENCE_LEVEL=NOT_APPLICABLE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

This reinvestigation is theorem-interface work; the lower theorem was already audited through exact construction regression in Stage24-50.

## Open gates

- positive-power lower bound for `N2`;
- true target exponent;
- matching half-power lower bound;
- intrinsic source-host mechanism for the half-power upper;
- asymptotic order of `A_ac,bc`;
- global sign of the Stage22/23 second-order interaction.

```text
HISTORICAL_STAGE23_PASS_REVOKED=false
FRESH_AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage23-audit
```
