# Stage26-70 — bounded maximal synthesis / closeout

EVIDENCE_LEVEL=PROVED_SYNTHESIS_CANDIDATE
CHECKPOINT=70
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage26-10,20,30,40,50,60

## 1. Frozen population contract

Stage26 compares the disjoint adjacent strata on the same primitive/canonical no-space Euclidean population with physical cutoff `R<=B`:

- `M2(B)`: exactly two integral face diagonals;
- `M3(B)`: exactly three integral face diagonals (Euler cuboids).

`M3` is not a literal subset of `M2`. The literal physical-object host is

\[
H_{\ge2}=M_2+M_3,\qquad \Phi=\frac{M_3}{M_2+M_3},
\]

and the raw shared-edge incidence host is

\[
P=M_2+3M_3,\qquad \Theta=\frac{3M_3}{M_2+3M_3}.
\]

## 2. Final audited theorem stack entering closeout

Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

Checkpoint60 hostile audit accepted the generalized two-parameter Saunderson lower:

\[
\boxed{M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}}\qquad(\forall\varepsilon>0).
\]

Checkpoint40 retains the audited upper family, for every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Thus the strongest current whole-family envelope is

\[
\boxed{B^{1/3-\varepsilon}\ll_\varepsilon M_3(B)\ll_\eta B(\log B)^{5-\eta}}
\]

for fixed `epsilon>0` and fixed `0<eta<1/46`. The two sides do not match.

## 3. Literal completion theorem

Checkpoint30 proved

\[
\Phi(B)\to0,\qquad \Theta(B)\to0,
\]

with

\[
\Phi\sim \frac{M_3}{M_2},\qquad
\Theta\sim3\frac{M_3}{M_2},\qquad
\frac{\Theta}{\Phi}\to3.
\]

Checkpoint40 strengthens the upper side: for every fixed `0<delta<1/46`,

\[
\frac{M_3}{M_2},\Phi,\Theta=o((\log B)^{-\delta}).
\]

Checkpoint60 improves the lower side: for every fixed `epsilon>0`,

\[
\frac{M_3}{M_2},\Phi\gg_\varepsilon
B^{-2/3-\varepsilon}(\log B)^{-5},
\]

and `Theta` has the same polynomial/log scale with the exact raw-incidence multiplicity-three adapter.

Hence the final Stage26 completion corridor is

\[
\boxed{
B^{-2/3-\varepsilon}(\log B)^{-5}
\ll_\varepsilon \Phi(B),\Theta(B)
=o((\log B)^{-\delta})
}
\]

for fixed `epsilon>0` and fixed `0<delta<1/46`, with constants interpreted separately for the two observables.

Also

\[
H_{\ge2}(B)\sim P(B)\sim M_2(B)\sim C_{M_2}B(\log B)^5.
\]

## 4. What checkpoint60 changed

The old `B^(1/6)` lower came from a one-parameter specialization of Saunderson. Restoring all primitive Pythagorean inputs gives quadratically many Euclidean parameter pairs. Global injectivity is unnecessary: `w^3` survives as one of the three physical face diagonals and each fixed `w` has only divisor-size many Pythagorean representations. The hostile audit accepted the resulting `B^(1/3-epsilon)` lower.

```text
OLD_LOWER_EXPONENT=1/6
OLD_LOWER_BOTTLENECK=ONE_PARAMETER_SPECIALIZATION
OLD_LOWER_BOTTLENECK_REMOVED=true
CURRENT_LOWER_EXPONENT=1/3_MINUS_EPSILON
EPSILON_FREE_ONE_THIRD_PROVED=false
```

## 5. Mechanism boundary

The upper mechanism remains the degree-two K3 third-face cover over the split `4A1` quartic-del-Pezzo/two-face host, with the exact local blocker law, separate growing-prime Selberg sieve, and Huang thin-cover saving. The sieve and thin-cover savings are not multiplied.

The lower mechanism is the generalized Saunderson two-parameter primitive Pythagorean family with divisor-size output fibers.

These mechanisms do not currently meet. Stage26 therefore does not identify the true growth exponent or an asymptotic for `M3`.

## 6. Reusable artifact decisions

The transition has a reusable population adapter, literal completion theorem, endpoint-free upper family, and a new two-parameter lower theorem. A self-contained bundle and arsenal promotion are therefore both required and materialized.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage26/26-70/self-contained-bundle.md
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_MATERIALIZED=true
ARSENAL_PROMOTION_PATH=docs/stage26-arsenal-promotion.md
```

## 7. Open frontier after Stage26

The unresolved problem is now sharply localized:

```text
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
EPSILON_FREE_ONE_THIRD_LOWER_PROVED=false
UPPER_LOWER_MATCH=false
ENDPOINT_DELTA_1_OVER_46_PROVED=false
FIXED_POWER_SAVING_UPPER_PROVED=false
```

A future refinement must either improve the generalized-Saunderson lower beyond `1/3-o(1)`, remove its divisor-loss endpoint, or produce a genuinely polynomial K3-side upper bound. Finite census alone cannot close this gap.

## 8. Firewalls and exit

```text
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
EXACTLY_TWO_TO_EXACTLY_THREE_CALLED_LITERAL_SUBSET=false
RAW_INCIDENCE_AND_OBJECT_COUNTS_CONFLATED=false
K3_MANIN_TRANSFER=false
INDEPENDENCE_CLAIM=false
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=
NEXT_STAGE=
MERGE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
