# Stage25-60 R504 Q-degree-2 normal-form/descent audit

STATUS=CORRECTION_REQUIRED
ROUTE=R504
CHECKPOINT=60

## Question

Can every quadratic rational map over `Q` be reduced by `PGL_2(Q)` to
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}?
\]

## Answer

No. The claimed form is not a complete `Q`-normal form for arbitrary degree-two rational maps.

Classical quadratic-rational-map moduli theory gives a two-dimensional moduli space, but a `Q`-rational moduli point does not imply that every representative is `Q`-conjugate to this even form. Complete `K`-conjugacy classifications distinguish automorphism-group cases and use different normal forms; for example a generic class with two distinct fixed points can be written as
\[
g_{a,b}(z)=\frac{z(z+a)}{bz+1},\qquad ab\ne1,
\]
while special automorphism cases require separate forms. The even form `(a u^2+b)/(u^2+1)` has the visible involution `u -> -u` on the source representation and therefore describes a symmetry-adapted subfamily, not all quadratic maps over `Q`.

Primary references checked:
- Milnor, *Remarks on quadratic rational maps* (1993): moduli and complex normal forms;
- Manes--Yasufuku, *Explicit descriptions of quadratic maps on P1 defined over a field K* (2010/2011): complete `K`-conjugacy classification with automorphism-group cases;
- Silverman moduli results: `M_2 ~= A^2`, field of moduli versus field of definition issues handled separately from a single even normal form.

## Consequence for R504

The symbolic computation on
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}
\]
remains valid **for that symmetry-adapted two-parameter subfamily**, including the exact extra-involution locus
\[
(a-b)^3(a+b)(ab-1)(ab+1)=0.
\]
But it may not be promoted to a classification of all `Q`-degree-two base changes.

```text
R504_Q_DEGREE2_EVEN_NORMAL_FORM_COMPLETE=false
R504_Q_DEGREE2_EVEN_NORMAL_FORM_SCOPE=SYMMETRY_ADAPTED_SUBFAMILY
R504_GENERAL_DEGREE2_FULL_CLASSIFICATION_PREVIOUS_CLAIM=WITHDRAWN
R504_EXTRA_INVOLUTION_SYMBOLIC_RESULT_WITHIN_SUBFAMILY=RETAINED
R504_Q_DEGREE2_DESCENT_CLASSIFICATION_REQUIRED=true
R504_PRYM_EXTERNAL_GATE_DEEP_STOP_ALLOWED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Correct next target

Build a genuinely complete `Q`-degree-two descent by splitting according to `Aut(phi)` / fixed-point Galois structure, using a complete `Q`-conjugacy normal-form theorem. For each normal-form stratum, translate the R504 pullback cover and determine whether it is already represented by the even subfamily or creates a new Prym/isogeny locus. Only after all `Q`-conjugacy strata are covered may the general degree-two route be called classified.
