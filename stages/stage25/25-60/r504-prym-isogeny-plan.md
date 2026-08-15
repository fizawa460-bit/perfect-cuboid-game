# Stage25-60 R504 Prym/isogeny residual

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

The normalized degree-two family is
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1},\qquad a\ne b,
\]
\[
C_{a,b}: y^2=(a u^2+b)^4+(u^2+1)^4.
\]

The inherited involution gives one `E0` factor. The full Q-rational extra-involution locus has now been closed symbolically, so any surviving degree-two rank jump must come from a non-bielliptic elliptic factor of the two-dimensional Prym surface.

Repo reuse was checked against Stage14/15 Kummer and low-degree-isogeny infrastructure. Those assets do not provide a theorem computing this Prym split locus.

Primary-source preflight identifies the missing theorem species concretely:

- Bruin, *The arithmetic of Prym varieties in genus 3* (arXiv:math/0408069), providing explicit genus-3 Prym descriptions / associated genus-2 Jacobians;
- Shaska, *Genus 3 hyperelliptic curves with (2,4,4)-split Jacobians* (arXiv:1306.5284), providing explicit moduli criteria and elliptic subcovers for the split-Jacobian locus.

Thus the residual is no longer an unexecuted involution/base-change ansatz. The exact remaining task is to specialize one of those explicit Prym/split-Jacobian theorem packages to `C_(a,b)` and test whether the resulting elliptic factor is Q-isogenous/twist-compatible with `E0`.

```text
R504_PRYM_DIMENSION=2
R504_PRYM_TARGET_FACTOR=E0:y^2=x^3-4x
R504_EXTRA_INVOLUTION_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
R504_REPO_NATIVE_PRYM_SPLIT_THEOREM_FOUND=false
R504_EXTERNAL_PRIMARY_SOURCE_BRUIN=arXiv:math/0408069
R504_EXTERNAL_PRIMARY_SOURCE_SHASKA=arXiv:1306.5284
R504_EXTERNAL_THEOREM_GATE=PRYM_GENUS2_MODEL_PLUS_244_SPLIT_MODULI_SPECIALIZATION
R504_RESIDUAL_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

Fresh hostile audit must decide whether this now satisfies the unchanged normative `EXTERNAL_THEOREM_GATE` stop class. If audit rejects the boundary, the next repair is not another finite ansatz scan: specialize Bruin or Shaska explicitly to `C_(a,b)`.
