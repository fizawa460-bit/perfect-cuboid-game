# Stage24-60 — causal interaction synthesis

EVIDENCE_LEVEL=PROVED_CAUSAL_SYNTHESIS_WITH_QUANTITATIVE_BRACKETS
CHECKPOINT=60
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Scope

Stage24 studies the literal subset transition

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\},
\]

where `M2(B)=#B2(B)` is the primitive canonical exactly-two-face population and `N2(B)=#A2(B)` is the same population with integral space diagonal, under the common physical cutoff `R<=B`.

Checkpoint60 compares this arrow against:

- Stage16S ambient integral-space baseline;
- Stage21 exactly-one-face space transition;
- Stage22 exactly-one to exactly-two comparison without space;
- Stage23 exactly-one to exactly-two comparison with space already present.

It also performs the mandatory double-charge audit.

## 2. Current Stage24 theorem state

Checkpoint30 proves

\[
\frac{N_2(B)}{M_2(B)}\to0
\]
by three independent routes, with quantitative inherited upper

\[
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Checkpoint50 now proves

\[
N_2(B)\gg\sqrt{\log B}
\]
and hence Stage19 unboundedness with infinitely many primitive exactly-two space-integral objects.

Since

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]
we obtain the new lower survivor-ratio bound

\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\gg
B^{-1}(\log B)^{-9/2}.
}
\]

Therefore

\[
\boxed{
B^{-1}(\log B)^{-9/2}
\ll
N_2/M_2
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]

The Stage24 transition is now rigorously classified as **zero-density but infinite**.

```text
STAGE24_ZERO_DENSITY=true
STAGE24_INFINITE_SURVIVORS=true
STAGE24_CAUSAL_CLASS=THIN_BUT_INFINITE
TRUE_SURVIVOR_EXPONENT_IDENTIFIED=false
```

## 3. Intrinsic ambient space cost

Stage16S proves

\[
\frac{N_S^{all}(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}\,B^{-1}.
\]

Thus integral space diagonal intrinsically costs one polynomial power in the ambient primitive/canonical population.

This is a comparison baseline, not a multiplicative saving to be combined with unrelated Stage14/19 bounds.

## 4. One-face interaction is positively logarithmic

Stage21 proves

\[
\frac{N_1(B)}{M_1(B)}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Relative to the Stage16S ambient baseline,

\[
\frac{N_1/M_1}{N_S^{all}/U}
\sim
\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty.
\]

Therefore one-face conditioning positively enhances space survival by `(log B)^2`, although the polynomial `B^-1` cost remains the same.

```text
STAGE21_INTERACTION_SIGN=POSITIVE
STAGE21_INTERACTION_SCALE=(log B)^2
```

## 5. Two-face interaction sign is not yet determined

Define

\[
\mathcal J_2(B)
=
\frac{N_2(B)/M_2(B)}{N_S^{all}(B)/U(B)}.
\]

The Stage24 lower and upper bounds give

\[
(\log B)^{-9/2}
\ll
\mathcal J_2(B)
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-5}.
\]

The certified interval contains `1`. Hence current theorems do **not** determine whether exactly-two-face conditioning globally enhances, suppresses, or leaves unchanged the ambient space-survival rate.

```text
STAGE24_GLOBAL_INTERACTION_SIGN=UNRESOLVED
STAGE24_RATIO_INDEPENDENCE_PROVED=false
STAGE24_RATIO_INDEPENDENCE_DISPROVED=false
```

The fact that Stage21 is positive does not authorize importing its `(log B)^2` factor into Stage24.

## 6. Alternate-path comparison: Stage22 versus Stage23

Stage22 proves the sharp no-space adjacent-stratum law

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B}.
\]

Stage23 starts after space has already been imposed. With checkpoint50's new lower theorem,

\[
\boxed{
B^{-1}(\log B)^{-5/2}
\ll
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
}
\]

The interval is not sharp enough to decide whether the second-face condition is globally easier or harder after conditioning on space.

The causal architectures are nevertheless distinct:

- Stage22 removes an order-`B` free complementary-edge degree of freedom by imposing a second Pythagorean face;
- Stage23 begins with that edge already coupled by the space Pythagorean extension and asks for an additional cross-leg face compatibility.

Thus the Stage22 mechanism does not transfer literally to Stage23.

## 7. Second-order interaction cross-ratio

Define

\[
\mathcal I(B)
=
\frac{N_2/M_2}{N_1/M_1}
=
\frac{N_2/N_1}{M_2/M_1}.
\]

This equality is an algebraic count identity. It does not turn the horizontal adjacent-stratum ratios into conditional probabilities.

The current theorems imply

\[
\boxed{
(\log B)^{-13/2}
\ll
\mathcal I(B)
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-7}.
}
\]

Since the bounds straddle `1`, the second-order face/space interaction sign remains unresolved.

## 8. Structural dependence inside the explicit Stage15 formula

The Stage15-2 algebraic construction exhibits exact arithmetic heterogeneity.

For coprime odd/odd parameters,

\[
17(p^4+q^4)\equiv2\pmod{16},
\]
so the space lift has no solutions.

Checkpoint50 reopens the same formulas at mixed parity. The slice

\[
p^4+q^4=17Z^2
\]
has positive-rank genus-one structure and produces infinitely many primitive exactly-two Stage19 objects after finitely many third-face exceptions are removed.

Therefore space survival is not uniform across natural arithmetic strata of this two-face construction.

```text
EXPLICIT_FORMULA_STRATUM_HETEROGENEITY=PROVED
ODD_ODD_SLICE_SPACE_SURVIVORS=0
MIXED_PARITY_C17_SLICE_SPACE_SURVIVORS=INFINITE
GLOBAL_INTERACTION_SIGN_FROM_THIS_FACT=NOT_INFERRED
```

This is structural dependence, not a global probabilistic correlation coefficient.

## 9. Exact Stage24 new condition

For the paired Gaussian-norm coordinates,

\[
R\in\mathbf Z
\iff
AB\in\mathbf Z^2
\iff
\operatorname{sf}(A)=\operatorname{sf}(B).
\]

Thus the space squareclass condition is genuinely new on the Stage18 -> Stage19 arrow and may be charged once there.

Its fixed-prime local sieve proves qualitative zero density. The checkpoint30 thin-cover argument supplies an independent qualitative proof. Neither proves the inherited half-power rate.

```text
SPACE_SQUARECLASS_IS_NEW_CONDITION=true
SPACE_SQUARECLASS_CHARGED_ON_STAGE24_ONCE=true
LOCAL_SIEVE_CAUSES_HALF_POWER=false
THIN_COVER_CAUSES_HALF_POWER=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
```

## 10. Double-charge verdict

The detailed firewall is in `double-charge-audit.md`. Its conclusions are:

- Stage16S `B^-1` is comparator only;
- Stage21 `(log B)^2` belongs to the one-face conditioned source and is not transferred;
- Stage23 already includes space, so the squareclass event is not charged again there;
- Stage22/23 horizontal ratios are adjacent-stratum comparisons, not subset-survival probabilities;
- the fixed-prime local-sieve saving is not multiplied onto the independent Stage14 half-power upper;
- the independent thin-cover zero-density route is not multiplied with either;
- checkpoint50's `C17` family is a lower witness, not a bulk factor.

```text
DOUBLE_CHARGE_CHECK=PASS
INDEPENDENCE_PRODUCT_USED=false
UNPROVED_SAVING_MULTIPLICATION_USED=false
```

## 11. Causal verdict

Checkpoint60 resolves the causal classification as far as current theorems permit:

1. `R integral` is intrinsically a `B^-1` ambient condition;
2. after one face, its survival is positively enhanced by `(log B)^2`;
3. after two faces, it defines a zero-density but infinite target;
4. its global interaction sign relative to the ambient space baseline remains unresolved because the Stage24 rate is not sharp;
5. the two-face source contains arithmetic strata with radically different space-survival behavior;
6. the inherited half-power upper remains unassigned to a proven causal mechanism;
7. no double charging is used.

No perfect-cuboid existence or nonexistence conclusion follows.

## 12. Exit

```text
DISCOVERY_CHECKPOINT=60
INTRINSIC_BASELINE_COMPARISON_COMPLETE=true
ALTERNATE_PATH_COMPARISON_COMPLETE=true
INDEPENDENCE_CORRELATION_CLASSIFICATION_COMPLETE=true
DOUBLE_CHARGE_CHECK=PASS
SPACE_SQUARECLASS_IS_NEW_CONDITION=true
HALF_POWER_RATE_ATTRIBUTED_TO_LOCAL_SIEVE=false
STAGE24_CLASS=THIN_BUT_INFINITE
STAGE24_GLOBAL_INTERACTION_SIGN=UNRESOLVED
SECOND_ORDER_INTERACTION_SIGN=UNRESOLVED
EXPLICIT_FORMULA_STRATUM_HETEROGENEITY=PROVED
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
