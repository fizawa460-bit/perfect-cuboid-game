# Stage27-19-r401 — hostile audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Scope

Hostile audit of PR #1031 / Stage27-19-r401 lower reentry. This audit does not claim a lower exponent above `1/4`, does not close the active Stage27 checkpoint40 upper program, and does not identify the true `N2` exponent.

## 1. Current Stage19 receiver

Accepted. The authoritative receiver remains

\[
N_2(B)\gg B^{1/4},\qquad N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

The historical finite floor is superseded. No new lower exponent is asserted in r401.

## 2. R501 / R502 quarter-power saturation

Accepted with family-specific scope.

R501 has reduced rational parameter count `T^2`, homogeneous degree-eight space height, bounded parameter fibers, finite exactly-three exceptions, and Stage25-r507 proves the primitive gcd is uniformly bounded by `10368`. Hence its exact family growth is

\[
N_{R501}(B)=\Theta(B^{1/4}).
\]

R502 independently has the same parameter-count / height ledger and an exact primitive gcd bound `<=2592`, with bounded parameter fibers and finite exactly-three exceptions. Hence

\[
N_{R502}(B)=\Theta(B^{1/4}).
\]

Therefore re-estimating primitive gcds or taking any fixed finite union of these audited quarter-power families cannot by itself raise the polynomial exponent above `1/4`. This is not promoted to a statement about all possible Stage19 parametrizations.

```text
R501_QUARTER_SATURATION_ACCEPTED=true
R502_QUARTER_SATURATION_ACCEPTED=true
FIXED_FINITE_UNION_KNOWN_QUARTER_FAMILIES_UPGRADES_EXPONENT=false
GLOBAL_STAGE19_PARAMETRIZATION_EXHAUSTED=false
```

## 3. Generic lower-family exponent calculus

Accepted. Under the stated hypotheses

\[
#\Omega(T)\gg T^{\kappa-o(1)},\qquad R\ll T^{h+o(1)},
\]

with `T^{o(1)}` parameter-to-object fibers and no fixed-power physical-filter loss, choosing the largest admissible `T=B^{1/h-o(1)}` yields

\[
N_2(B)\gg B^{\kappa/h-o(1)}.
\]

Hence genuine fixed-power lower progress requires

\[
\boxed{\kappa/h>1/4}.
\]

For the coupled model

\[
#\Omega(T)\asymp T^{2+\lambda},\qquad R\asymp T^{8+q},
\]

the crossing test is exactly

\[
\frac{2+\lambda}{8+q}>\frac14\iff \boxed{4\lambda>q}.
\]

This is bookkeeping only; no new family is proved to satisfy the gate.

```text
LOWER_FAMILY_EXPONENT_CALCULUS_ACCEPTED=true
LOWER_PROGRESS_GATE=kappa/h>1/4
COUPLED_OUTER_PARAMETER_GATE=4*lambda>q
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
```

## 4. Master toric space receiver

Accepted with the stated firewall. Stage25 R505 gives

\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2,
\]

and the Stage19 space condition is exactly `AB` square, equivalently `sf(A)=sf(B)`. Setting

\[
x=m/n,\qquad y=r/s
\]

gives

\[
A/(n^2s^2)=x^2y^2+1,\qquad B/(n^2s^2)=x^2+y^2.
\]

For positive rationals, `AB` square iff `A/B` square, so the space condition is equivalent to the existence of positive rational `z` satisfying

\[
\boxed{x^2y^2+1=z^2(x^2+y^2)}.
\]

This receiver encodes only the space-diagonal condition inside the two-face toric host. Positivity/nondegeneracy, primitive and canonical normalization, parity/coprimality decorations, and exclusion of the third integral face remain mandatory for any lower construction.

```text
MASTER_SPACE_RECEIVER_ACCEPTED=true
MASTER_SPACE_RECEIVER=x^2*y^2+1=z^2*(x^2+y^2)
MASTER_SURFACE_DOMINANT_RATIONAL_PARAMETRIZATION_PROVED=false
FULL_STAGE19_PHYSICAL_ADAPTER_AUTOMATIC=false
```

## 5. Reopen boundary

Accepted. A genuine lower upgrade must provide at least one of:

- a lower-height family with `kappa/h>1/4`;
- a genuinely thicker polynomial family whose count gain beats its height cost;
- a moving-core / moving-fiber polynomial mass theorem in the exact physical measure;
- another polynomial admissible-support theorem with primitive/canonical/exactly-two control.

R505 already records that existing repo-native common-core relabelings do not supply such a theorem; this remains a repository-state boundary, not an impossibility theorem.

## 6. CI / lifecycle

Submission head `36aaa850738eec35f5d00fa41155d57e9267637f` passed the dedicated Stage27-19-r401 workflow and all relevant Stage27 regressions. One Stage25 phase70 handoff regression failed only because its historical verifier allowed `Stage27-audit` but not the legitimate derived-route command `Stage27-19-r401-audit`. The verifier was made successor-route aware during audit; no Stage25 mathematics or handoff theorem was changed.

The long-standing unrelated Stage25 phase10 / Stage15-8 lifecycle failures are not Stage27-19-r401 mathematical blockers.

```text
DEDICATED_STAGE27_19_R401_CI_SUBMISSION_HEAD=SUCCESS
STAGE25_PHASE70_FAILURE_CLASS=LIFECYCLE_ONLY_REPAIRED_DURING_AUDIT
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1031; then Stage27-main-batch with checkpoint40 retained
```
