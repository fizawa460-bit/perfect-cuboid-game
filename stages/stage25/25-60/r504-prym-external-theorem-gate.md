# Stage25-60 R504 Prym external-theorem gate

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

After symbolic closure of the full Q-rational extra-involution locus in the normalized generic degree-two family, the only surviving degree-two rank-jump mechanism is a non-bielliptic elliptic factor of the two-dimensional Prym surface.

## Current exact family

\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1},\qquad a\ne b,
\]
\[
C_{a,b}: y^2=(a u^2+b)^4+(u^2+1)^4.
\]

The involution `u -> -u` supplies the inherited elliptic quotient and inherited `E0` factor. The extra Q-rational involution locus was proved symbolically to be

\[
(a-b)^3(a+b)(ab-1)(ab+1)=0,
\]

and every nondegenerate Q-rational locus was closed against an additional `j=1728` factor.

## Surviving theorem species

A new independent pullback section can now only come from an elliptic factor of the Prym surface that is not induced by a second rational involution on `C_(a,b)`.

Repo reuse was repeated against the Stage14/15 Kummer and low-degree-isogeny infrastructure. Those assets classify low-degree elliptic/isogeny exceptions and supply Kummer incidence receivers, but they do not provide a theorem computing the non-bielliptic Prym split locus for this two-parameter family.

Primary-literature preflight identifies two directly relevant theorem species:

1. Bruin, *The arithmetic of Prym varieties in genus 3* (arXiv:math/0408069): explicit algebraic description of genus-3 Prym varieties and associated genus-2 Jacobians.
2. Shaska, *Genus 3 hyperelliptic curves with (2,4,4)-split Jacobians* (arXiv:1306.5284): explicit characterization of the two-dimensional locus of genus-3 hyperelliptic curves admitting degree-2 and degree-4 elliptic subcovers, including recovery of the elliptic subcovers from moduli invariants.

These are exactly the missing theorem species needed to turn the residual Prym question into an explicit moduli equation. No equivalent theorem or adapter is currently materialized in the repository.

```text
R504_PRYM_DIMENSION=2
R504_EXTRA_INVOLUTION_DEGREE2_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
R504_NON_BIELLIPTIC_PRYM_E0_FACTOR_LOCUS=OPEN
R504_REPO_NATIVE_PRYM_SPLIT_THEOREM_FOUND=false
R504_EXTERNAL_THEOREM_SPECIES_IDENTIFIED=true
R504_EXTERNAL_PRIMARY_SOURCE_BRUIN=arXiv:math/0408069
R504_EXTERNAL_PRIMARY_SOURCE_SHASKA=arXiv:1306.5284
R504_EXTERNAL_THEOREM_GATE=PRYM_GENUS2_MODEL_PLUS_244_SPLIT_MODULI_SPECIALIZATION
R504_RESIDUAL_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
```

## Exact work required to reopen internally

This gate may be reopened only by materializing one of the following:

- Bruin's explicit Prym/genus-2 construction specialized to `C_(a,b)` and then a split-Jacobian test for an `E0` factor;
- Shaska's explicit (2,4,4)-split moduli equations specialized to the invariants of `C_(a,b)`, followed by a Q-isogeny/twist check against `E0`;
- a new explicit degree >=3 map `C_(a,b) -> E0` not mediated by a second curve involution.

A finite search in `(a,b)` is not enough.

## Stop-rule consequence submitted

Under the unchanged normative checkpoint60 rule, this is now a candidate `EXTERNAL_THEOREM_GATE`, not a live unexecuted repo-native mutation: the obvious low-degree base-change families, the full rational extra-involution locus, and growing multiples have all been executed and closed; the remaining object requires a theorem species absent from the repository but identified in primary literature.

```text
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
```

Fresh hostile audit must decide whether the identified Prym theorem gate is sufficient for the normative deep-stop rule. No Stage70 advance is made by this artifact itself.
