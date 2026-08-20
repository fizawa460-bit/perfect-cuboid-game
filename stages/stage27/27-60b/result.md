# Stage27-60b — roadmap causal decomposition: mechanism and double-charge ledger

```text
TASK_ID=Stage27-60b
CHECKPOINT=60
PARENT=Stage27-60a
ROADMAP_TRANSITION=Stage16 -> Stage20
ROUTE_KIND=CAUSAL_MECHANISM_AND_DOUBLE_CHARGE_LEDGER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Second-face mechanism: Stage16 -> Stage18

Stage22 identifies the leading mechanism behind

\[
M_2/M_1\asymp (\log B)^4/B.
\]

The Stage16 source has one scaled primitive Pythagorean face together with a
complementary edge that is free at polynomial order `B`.  Passing to Stage18
replaces that free complementary-edge degree of freedom by a second Pythagorean
condition coupled through the unique shared edge.  The target bulk is represented
by the smooth split rank-6 anticanonical toric resolution.

Thus the certified leading ledger is

```text
SECOND_FACE_NEW_RESTRICTION=shared-edge coupled second Pythagorean condition
SECOND_FACE_POLYNOMIAL_COST=B^-1
SECOND_FACE_LOG_COMPENSATION=(log B)^4
SECOND_FACE_FINE_LOG4_FACTORIZATION_PROVED=false
```

Primitivity, canonicalization, the common `R<=B` cutoff, and physical multiplicity
are shared interfaces and are not new causes.  The third-face-square exclusion in
Stage18 is lower order, so it is not charged as part of the leading Stage16 -> 18
loss.

## 2. Third-face mechanism: Stage18 -> Stage20

Stage26 identifies a genuinely new arithmetic condition on the already-coupled
two-face host: the remaining face diagonal must also be integral.  The upper
analysis realizes this as a degree-two K3 third-face cover over the split `4A1`
quartic-del-Pezzo/two-face host, with an exact local blocker law, a growing-prime
Selberg sieve, and a Huang thin-cover saving.  Those two savings are alternative/
complementary parts of the certified upper mechanism and are explicitly not
multiplied as independent powers.

The lower mechanism is different: the generalized two-parameter Saunderson family
constructs Euler cuboids with divisor-size output fibers and proves

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}.
\]

The upper and lower mechanisms do not meet.  Consequently Stage27 can certify that
adding the third face is zero-density inside the two-face population, but it cannot
assign a sharp polynomial exponent to that extra loss.

```text
THIRD_FACE_NEW_RESTRICTION=remaining face square on the two-face host
THIRD_FACE_ZERO_DENSITY=true
THIRD_FACE_UPPER_MECHANISM=K3 cover + local blocker + growing-prime sieve/thin-cover control
THIRD_FACE_LOWER_MECHANISM=generalized two-parameter Saunderson construction
THIRD_FACE_TRUE_POLYNOMIAL_COST_IDENTIFIED=false
THIRD_FACE_MECHANISM_INDEPENDENT_OF_SECOND_FACE_PROVED=false
```

## 3. Space-diagonal firewall

The roadmap Stage27 transition is `16 -> 20`; neither endpoint requires an integral
space diagonal.  Stage21 proves that the space-diagonal condition itself has a
sharp intrinsic polynomial cost `B^-1` in its own transition, with a `(log B)^2`
interaction enhancement after one-face conditioning.  That is valuable comparison
information, but it is **not** a Stage27 charge.

Accordingly none of the Stage17/19 space-diagonal losses, and none of the deep
Stage27-19 `N2` reentry work, may be multiplied into the `M3/M1` thinning law.
They remain auxiliary interaction evidence for Stage28 or future endpoint work.

```text
SPACE_DIAGONAL_COST_KNOWN_ELSEWHERE=true
SPACE_DIAGONAL_CHARGED_IN_STAGE27=false
STAGE27_19_N2_REENTRY_CHARGED_IN_STAGE27_16_TO_20=false
```

## 4. Double-charge verdict

The two leading Stage27 causes occupy different conditional interfaces:

- the second-face condition removes the free complementary-edge polynomial freedom;
- the third-face condition imposes a new square condition on the resulting two-face
  host.

This is enough to distinguish the restrictions structurally.  It is **not** enough
to prove probabilistic or exponent-level independence.  In particular, the exact
population-ratio identity

\[
M_3/M_1=(M_2/M_1)(M_3/M_2)
\]

does not license an independence claim.

```text
DISTINCT_CONDITIONAL_RESTRICTIONS_IDENTIFIED=true
DOUBLE_CHARGE_CHECK=PASS
MECHANISM_INDEPENDENCE_PROVED=false
LOCAL_PROBABILITY_PRODUCT_PROVED=false
NEXT_DERIVED_ROUTE=27-60c
```
