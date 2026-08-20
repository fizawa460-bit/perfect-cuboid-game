# Stage28-30 — bridge-ratio corridor

```text
TASK_ID=Stage28-30
CHECKPOINT=30
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=DERIVED_FROM_AUDITED_THEOREM_INTERFACES
```

## 1. Primary bridge quantity

With the checkpoint10 common-host semantics,

\[
\mathcal R_{28}(B)
=
\frac{M_3(B)}{N_2(B)}
=
\frac{\Phi_{20}(B)}{\Sigma_{19}(B)}.
\]

This is a matched population-size ratio, not a literal survival probability.

## 2. Incoming certified bounds

Stage27 closes with

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Stage26 supplies the strongest current Euler lower and upper interfaces

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon},
\]

and, for every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

On the common no-space host `H_ge2~M2`, Stage26 also proves, for every fixed `0<delta<1/46`,

\[
\Phi_{20}(B)=\frac{M_3(B)}{H_{\ge2}(B)}=o((\log B)^{-\delta}),
\]

while Stage27/Stage18 give

\[
\Sigma_{19}(B)=\frac{N_2(B)}{H_{\ge2}(B)}
\gg B^{-3/4}(\log B)^{-5}
\]

and

\[
\Sigma_{19}(B)
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

## 3. Strongest legal lower corridor for `M3/N2`

Divide the Stage26 lower by the Stage27 upper. Given any fixed `zeta>0`, choose the two epsilon losses with total at most `zeta`. Then

\[
\boxed{
\mathcal R_{28}(B)
\gg_{\zeta} B^{-1/6-\zeta}
}
\qquad (\zeta>0).
\]

Equivalently, the common-host form follows by dividing the lower corridor for `Phi20` by the upper corridor for `Sigma19`; the logarithmic factors cancel at this strength.

This is only a lower bound on the bridge ratio. It does not show that the ratio stays positive away from zero, tends to infinity, or eventually exceeds one.

## 4. Strongest legal upper corridor for `M3/N2`

Using the stronger Stage26 host-share statement rather than only the coarse whole-family Euler upper, for every fixed `0<delta<1/46`,

\[
\Phi_{20}(B)=o((\log B)^{-\delta}).
\]

Since

\[
\Sigma_{19}(B)\gg B^{-3/4}(\log B)^{-5},
\]

we obtain

\[
\boxed{
\mathcal R_{28}(B)
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right)
}
\qquad (0<\delta<1/46).
\]

The weaker direct division of the whole-family bounds would give only

\[
\mathcal R_{28}(B)\ll_\eta B^{3/4}(\log B)^{5-\eta},
\]

so the common-host small-`o` form is retained as the strongest current checkpoint30 upper corridor.

## 5. Ordering status

The certified corridor is therefore broad:

\[
B^{-1/6-o(1)}
\lesssim
\mathcal R_{28}(B)
\lesssim
B^{3/4+o(1)}.
\]

This corridor contains all three qualitative possibilities `R28->0`, bounded/oscillatory behavior, and `R28->infinity`. Therefore the asymptotic ordering of Stage19 and Stage20 remains unresolved.

The progress conditions are explicit:

- a proof that `M3/N2 -> infinity` would require a substantially stronger lower comparison, for example an `M3` lower scale exceeding a valid `N2` upper scale, or another direct bridge theorem;
- a proof that `M3/N2 -> 0` would require a substantially stronger upper comparison, for example an `M3` upper scale below a valid `N2` lower scale, or another direct bridge theorem;
- current one-sided endpoint bounds do neither.

```text
BRIDGE_RATIO_LOWER=R28(B)>>_zeta B^(-1/6-zeta) for every fixed zeta>0
BRIDGE_RATIO_UPPER=R28(B)=o(B^(3/4)(log B)^(5-delta)) for every fixed 0<delta<1/46
BRIDGE_RATIO_LIMIT_IDENTIFIED=false
M3_EVENTUALLY_GT_N2_PROVED=false
M3_EVENTUALLY_LT_N2_PROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
```

## 6. Finite-data firewall

Checkpoint20 found `M3/N2<1` at the matched cutoffs through `B=1,000,000`, with a nonmonotone finite path. That panel is compatible with the theorem corridor but does not sharpen it asymptotically.

```text
FINITE_PANEL_USED_AS_THEOREM=false
FINITE_RATIO_LIMIT_PROMOTED=false
FINITE_EFFECTIVE_EXPONENT_PROMOTED=false
```

## 7. Exit

Checkpoint30 is a derived corridor checkpoint. It opens no new theorem branch and makes no OPEN_GATE declaration; checkpoints40 and50 will separately ledger the strongest upper-side and lower-side bridge implications before checkpoint60 causal synthesis.

```text
CHECKPOINT30_RATIO_CORRIDOR_COMPLETE=true
REPO_REUSE_PREFLIGHT=PASS
STRONGEST_KNOWN_CHECK=PASS_FOR_CURRENT_DERIVED_CORRIDOR
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage28-audit
```
