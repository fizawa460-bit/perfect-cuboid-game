# Stage24-50 fresh audit

AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
CHECKPOINT=50
PR=976

## Verdict

The mixed-parity quartic lift is accepted as a genuine lower-side breakthrough for the exact Stage19 population.

The audited construction starts from

\[
e=4pq,\qquad x=4p^2-q^2,\qquad y=4q^2-p^2
\]

and imposes the exact integral-space condition

\[
p^4+q^4=17Z^2,\qquad D=17Z.
\]

For coprime positive reduced parameters on this quartic, both-odd parity is excluded modulo 16, so the parameters are opposite parity. The resulting edge triple is primitive, the two displayed face diagonals are integral, and on the open cone

\[
1<q/p<(1+\sqrt2)/2
\]

the canonical ordering is fixed and the parameter ratio is recoverable from the box.

The genus-one quartic

\[
17z^2=t^4+1
\]

maps nontrivially to

\[
E:Y^2=X^3-1156X.
\]

The point `(t,z)=(2,1)` maps to `P=(-16,120)`. The exact good-reduction checks `#E(F31)=32`, `#E(F41)=52`, together with exact order `16` for `P mod 31`, exclude rational torsion and certify positive rank. The repository CI independently verifies these arithmetic identities and certificates.

The physical cone contains the exact rational point `(p,q,Z)=(38,43,569)`. Positive rank and the real elliptic-circle dynamics therefore place infinitely many rational points in the cone. The remaining third-face-square condition cuts out the connected biquadratic cover

\[
17z^2=t^4+1,\qquad w^2=17t^4-16t^2+17,
\]

whose two quartic branch sets are simple and disjoint. Riemann-Hurwitz gives genus 5, so Faltings leaves only finitely many rational triple-face exceptions in this special family. Thus infinitely many primitive canonical exactly-two Stage19 objects remain.

The quantitative lower bound is also accepted. For a fixed non-torsion translation sequence on the genus-one curve, standard elliptic height theory gives `h(t(Q_n))=O(n^2)`, hence physical space height at most `exp(C n^2)`. A fixed positive proportion of indices enter a compact subinterval of the physical cone, the `t`-projection has bounded degree, and the physical box map is injective on reduced positive `t` in that cone. Consequently

\[
\boxed{N_2(B)\gg\sqrt{\log B}}.
\]

This proves unboundedness but not a positive power of `B`.

## Historical-scope audit

The Stage23 R60-01 modulo-16 argument remains correct for its literal historical hypothesis: coprime **odd/odd** parameters in the Stage15-2 family. What is superseded is any broader reading that the underlying algebraic formula is dead for every parity class. The mixed-parity `C17` slice is a revived variant.

Historical Stage19/Stage23 PASS verdicts are not revoked. Their lower-bound statements were correct at audit time and receive a later Stage24 supersession addendum.

## Search-policy audit

Checkpoint50 satisfies the required fresh lower search:

- fresh Stage19 lower surgeon executed first;
- explicit unbounded-family search executed;
- positive-power lower search executed but no positive-power bound proved;
- Stage18 explicit-family space-lift test executed;
- four fresh candidate classes were recorded;
- finite census data are not used as the infinitude proof;
- the eight-old-dead-branch negative-result gate is not triggered because F50-S1 is a positive breakthrough.

## Boundary

```text
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PASS
AUDIT_VERDICT=PASS
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
NEW_LOWER_BOUND=N2(B)>>sqrt(log B)
LOWER_BOUND_CLASS=LOGARITHMIC_UNBOUNDED
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
R60_01_ODD_ODD_DEATH_STILL_VALID=true
R60_01_BROADER_FORMULA_DEATH_SUPERSEDED=true
REVIVED_VARIANT=MIXED_PARITY_C17
HISTORY_SUPERSESSION_BACKFLOW_REQUIRED=true
FINITE_DATA_USED_AS_PROOF=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```

Advancement and merge permission are granted only together with the history-backflow artifacts committed on this audited branch.