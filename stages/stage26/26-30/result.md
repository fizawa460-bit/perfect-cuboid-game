# Stage26-30 — literal third-face completion corridor

EVIDENCE_LEVEL=PROVED_DERIVED_THEOREM_CANDIDATE
CHECKPOINT=30
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage26-10,Stage26-20,Stage18,Stage20,Stage25-reentry-60

## 1. Common object host

Under the frozen primitive/canonical no-space Euclidean cutoff `R<=B`, let

\[
M_2(B)=\#\{\text{exactly-two-face objects}\},\qquad
M_3(B)=\#\{\text{Euler exactly-three-face objects}\}.
\]

These exact strata are disjoint. Put

\[
H_{\ge2}(B)=M_2(B)+M_3(B),\qquad
\Phi(B)=\frac{M_3(B)}{H_{\ge2}(B)}.
\]

Thus `Phi` is a literal physical-object fraction inside the at-least-two-face host. It is not the adjacent-stratum quotient `M3/M2`.

For the raw shared-edge incidence host,

\[
P(B)=M_2(B)+3M_3(B),\qquad
\Theta(B)=\frac{3M_3(B)}{P(B)}.
\]

Writing

\[
r(B)=\frac{M_3(B)}{M_2(B)},
\]

one has the exact identities

\[
\Phi=\frac{r}{1+r},\qquad
\Theta=\frac{3r}{1+3r},
\]

and the exact odds bridge

\[
\boxed{\frac{\Phi}{1-\Phi}=r},\qquad
\boxed{\frac{\Theta}{1-\Theta}=3r}.
\]

Equivalently,

\[
\boxed{\Theta=\frac{3\Phi}{1+2\Phi}},\qquad
\boxed{\Phi=\frac{\Theta}{3-2\Theta}}.
\]

## 2. Frozen asymptotic inputs

Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

Stage20 gives

\[
M_3(B)\gg B^{1/6}
\]

and for every fixed

\[
0<\eta<1/46,
\]

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Therefore

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll r(B)
\ll_\eta(\log B)^{-\eta}
}
\]

for every fixed `0<eta<1/46`. In particular

\[
\boxed{r(B)\to0}.
\]

## 3. Literal completion theorem candidate

Since `r(B)->0`, the exact transforms above yield

\[
\Phi(B)\sim r(B),\qquad
\Theta(B)\sim3r(B),
\]

and hence

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll \Phi(B)
\ll_\eta(\log B)^{-\eta}
}
\]

and

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll \Theta(B)
\ll_\eta(\log B)^{-\eta}
}
\]

for every fixed `0<eta<1/46`.

Consequently

\[
\boxed{\Phi(B)\to0},\qquad
\boxed{\Theta(B)\to0},
\]

while

\[
\boxed{\frac{\Theta(B)}{\Phi(B)}\to3}.
\]

This is the Stage26 checkpoint30 transition statement: among primitive canonical physical cuboids having at least two integral face diagonals, the fraction having all three integral face diagonals tends to zero. The factor three in the raw-incidence model is exactly the Euler-object shared-edge multiplicity and is not an independence factor.

## 4. Host asymptotics

The same `r(B)->0` statement gives

\[
\boxed{H_{\ge2}(B)\sim M_2(B)\sim C_{M_2}B(\log B)^5}
\]

and

\[
\boxed{P(B)\sim M_2(B)\sim C_{M_2}B(\log B)^5}.
\]

Thus the exactly-two stratum asymptotically exhausts both the at-least-two physical-object host and the raw-pair host after multiplicity normalization:

\[
\frac{M_2}{M_2+M_3}\to1,\qquad
\frac{M_2}{M_2+3M_3}\to1.
\]

This does not identify an asymptotic for `M3` itself.

## 5. Relation to checkpoint20 finite panel

Checkpoint20 is a consistency/regression panel only. No row of the finite table is used to prove the limits above. The proof uses only the audited Stage18 asymptotic, the audited Stage20 lower/upper corridor, and the exact Stage26-10 measure adapters.

```text
FINITE_PANEL_USED_AS_ASYMPTOTIC_PROOF=false
OBJECT_COMPLETION_RATE=Phi_EQUALS_M3_OVER_M2_PLUS_M3
RAW_INCIDENCE_RATE=Theta_EQUALS_3M3_OVER_M2_PLUS_3M3
ADJACENT_STRATUM_RATIO=r_EQUALS_M3_OVER_M2
EXACT_ODDS_BRIDGE=true
RATIO_CORRIDOR_PROVED_CANDIDATE=true
PHI_TO_ZERO_PROVED_CANDIDATE=true
THETA_TO_ZERO_PROVED_CANDIDATE=true
THETA_OVER_PHI_TO_3_PROVED_CANDIDATE=true
AT_LEAST_TWO_HOST_ASYMPTOTIC_PROVED_CANDIDATE=true
TRUE_M3_EXPONENT_IDENTIFIED=false
INDEPENDENCE_CLAIM=false
K3_MANIN_TRANSFER=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
