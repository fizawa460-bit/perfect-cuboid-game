# Stage26 handoff candidate from Stage25-reentry

STATUS=SUBMITTED_PENDING_PHASE70_FRESH_AUDIT
SOURCE_TASK=Stage25-um-r007a
SOURCE_PHASE=70

## Entry object

Stage26 should start from the primitive canonical no-space exactly-two / raw-pair host under the same Euclidean cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B,
\qquad 0<a<b<c,
\qquad \gcd(a,b,c)=1.
\]

For a shared-edge direction `j`, the raw two-face incidence population is

\[
P_j=M_{2,j}+M_3.
\]

Globally, incidence counting gives

\[
P=M_2+3M_3.
\]

No integral-space-diagonal condition is imposed at this Stage26 entry point.

## Primary observable

Use the literal same-measure third-face completion rates

\[
\Theta_j=\frac{M_3}{P_j},
\qquad
\Theta=\frac{3M_3}{P}.
\]

The audited incoming corridor is

\[
B^{-5/6}(\log B)^{-5}\ll_j\Theta_j
\ll_{j,\eta}(\log B)^{-\eta},
\]

with the analogous global statement, for every fixed `eta<1/46`.

Also

\[
\Theta_j/\Theta_k\to C_k/C_j.
\]

Thus the completion rates tend to zero but are quantitatively bounded below by a positive power family through the current Saunderson construction.

## Incoming geometry

The raw exactly-two host is the audited split `4A1` quartic-del-Pezzo / `Bl_4(P1xP1)` geometry. Imposing the third face produces the audited degree-two K3 cover.

The Stage25 r011a Manin ledger explains the source transitions

\[
M_1:(2,2),\quad N_1:(1,4),\quad M_2:(1,6),
\]

but **must not** be extended to `M3` by a naive Picard-rank subtraction. The K3 target has a different height/counting regime.

## Incoming weapon packet

Mandatory first-use interfaces:

1. `S20-W01_EXPLICIT_EULER_THIN_COVER_UPPER`;
2. `S20-W02_PRIMITIVE_SAUNDERSON_LOWER`;
3. `S20-W03_EULER_LOCAL_BLOCKER_LAW`;
4. `S25-W05_RAW_PAIR_EULER_COMPLETION_ADAPTER`;
5. `S25-W06_GEOMETRIC_MANIN_TRANSITION_LEDGER` with the K3 firewall.

Secondary archive for later stages: `S25-W01` through `S25-W04`.

## Stage26 first questions

Stage26 should attack, in order of value:

1. Can the upper `B(log B)^(5-eta)` be sharpened on the exact raw-pair completion measure?
2. Can the lower exponent `1/6` be improved by a new primitive family or by converting a larger-dimensional rational family without hidden gcd/multiplicity collapse?
3. Can `Theta_j` or `Theta` receive a matching power/log law, or at least a narrower corridor?
4. Can the local blocker law be combined with the global K3/thin-cover geometry without illicit independence multiplication?
5. Is there a same-measure spectral, height, or arithmetic input strong enough to reopen any Stage14/15 P3 route? If not, leave those routes closed.

## Non-goals at entry

- Do not infer a square-root law from finite Euler-brick counts.
- Do not treat `M3/M2` as a conditional probability.
- Do not multiply the local sieve and thin-cover saving as independent losses.
- Do not infer a perfect-cuboid conclusion from the no-space Euler-brick population.
- Do not reopen Q07–Q10 without a genuinely new independent equation, height monotonicity, or same-measure spectral theorem.

```text
STAGE26_ENTRY_INTERFACE_VALID_CANDIDATE=true
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_MATCH=true
QUANTIFIER_MATCH=true
TRUE_M3_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
PHASE70_AUDIT_REQUIRED=true
STAGE26_ALLOWED=false
```
