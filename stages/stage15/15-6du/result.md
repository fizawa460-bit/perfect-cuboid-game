# Stage15-6du — fresh exhaustive view audit, blind rediscovery, and next-route selection

Base: Stage15-6dt. The Pell/unit representation materially changed the active receiver geometry, so the controller-required protocol is run immediately before any parking or route promotion.

## 1. EXHAUSTIVE_VIEW_AUDIT

Re-audit every materially distinct route against the now-exact recurrence receiver and the preserved physical measure.

| Candidate | Status after Pell audit | Reason |
|---|---|---|
| Pell/unit-orbit pointwise completion | CONSUMED / EXACT | 6ds gives the exact rank-one recurrence-orbit description; 6dt proves current pointwise/ideal inputs are exponent-neutral. |
| Pell/Lucas primitive-divisor or recurrence theorem | EXTERNAL GATE | Could shorten or rigidify individual orbits, but no same-measure theorem for the varying `(k,seed,base)` family is currently adapted; even `O(1)` per fixed base does not itself give `B^{-delta}`. |
| Norm-ideal averaging | CONSUMED / EXPONENT-NEUTRAL | AR-016 and 6dt: divisor/logarithmic moments only with current inputs. |
| Local valuation / fixed-prime recurrence sieve | LIVE / QUALITATIVE BACKUP | Genuine local rejection mechanism. AR-035 could yield qualitative thinning only after a Stage15 fixed-modulus refined asymptotic; no effective fixed-power adapter is present. |
| Mixed norm / linear-factor switching | EQUIVALENT / CONSUMED | Substituting the first Pell norm into the second gives exactly the 6dd/6dg double eliminant, so this is not a new independent receiver. |
| Root-ratio character / Ramanujan dispersion | CURRENT-INPUT NEGATIVE CERTIFIED | 6dp–6dr exposes the exact centered operator; no `kappa<1` same-measure large sieve is currently available. |
| Orientation-blind pair resultant | CURRENT-INPUT NEGATIVE CERTIFIED | Positive support incidence does not control centered occupancy bias. |
| Shared-support pair energy | DOMINATED | Controls large common support but not the surviving one-point/complementary obstruction. |
| Direct root-line lattice | LIVE LOCAL ENGINE | AR-009 remains valid locally but alone leaves the one-sided/complementary fringe. |
| Residual-cell complementary divisor switch | LIVE / UNTESTED | Explicitly preserved in 6cy and not consumed by Pell/character failures; `(q,H)=1` keeps the switched modulus transverse to the cell normalizer. |
| Fixed-prime overlap sieve on reconstructed base | LIVE / BACKUP | Potential causal thinning route, but presently only qualitative and missing the required refined asymptotic. |
| External genus-one/height theorem | PARKED EXTERNAL SPECIES | Earlier quartic/twist analyses showed no current exact height adapter yielding the needed family saving. |

No candidate is deleted merely because a related route failed.

## 2. BLIND_REDISCOVERY from the current equations

Ignore the historical route names and restart from the exact data:

\[
HMNUV\le B,\qquad (q,H)=1,
\]
\[
A_0=a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
B_0=b^4M^2V^2+c^4N^2U^2=kQ^2,
\]
\[
kg^2\mid\Delta,
\qquad
\Delta=(abM)^4-(cdN)^4,
\]
and the switched S/O channel congruences.

The Pell orbit makes the fourth-variable fiber thin but does not thin the set of base triples. The next place a polynomial saving can arise **internally** is therefore not another pointwise reconstruction. It must reduce the number of base triples/cores carrying a large switched divisor or produce a genuinely averaged deficit before the `B^{o(1)}` completion fiber is attached.

The exact cross-gcd cells already separate the normalizer `H` from the odd switched modulus. This suggests switching the large residual channel divisors to their complementary cofactors **after** the cell normalization and before the Pell postfilter, rather than reopening the same unit orbit or centered character problem.

This rediscovery independently returns the route left LIVE/UNTESTED in Stage15-6cy:
\[
\boxed{\text{RESIDUAL-CELL COMPLEMENTARY DIVISOR SWITCH}.}
\]

## 3. Selected next internal route

Select
\[
\boxed{\text{RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER}.}
\]

The next main task is to write, in the cell variables
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\]
the exact S/O residual forms and a multiplicity-one complementary switch for the decorated `(d_S,e_O)` divisors, preserving
\[
(q,H)=1,
\]
the exact `phi(d_S)phi(e_O)` weights, `kg^2|Delta`, and the Pell second-norm postfilter. The test is whether the switched complementary variables acquire an inverse-threshold moment or a one-sided fringe saving that was invisible before cell normalization.

A positive result must produce an actual polynomial `delta>0` and/or `sigma>0` on the same physical measure. A failure must be certified without converting `B^{o(1)}` Pell completion into a fake saving.

## 4. Parking and split decision

Parking is **rejected** because one materially distinct internal route remains LIVE/UNTESTED. The fixed-prime local sieve also remains a qualitative backup.

The two quantitative exponents are still not independently controlled:
\[
\delta>0:\ \text{unproved},\qquad
\sigma>0:\ \text{unproved}.
\]
There is no executable polynomial overlap window, and no split trigger fires.

## 5. Controller exit

```text
STAGE15_6_SUBSTAGE=6du
STAGE15_6DU_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6DU_BLIND_REDISCOVERY=true
STAGE15_6DU_PELL_GEOMETRY_CHANGE_CONSUMED=true
STAGE15_6DU_MIXED_NORM_LINEAR_ROUTE=EQUIVALENT_TO_DOUBLE_ELIMINANT
STAGE15_6DU_RESIDUAL_CELL_SWITCH=LIVE_UNTESTED_SELECTED
STAGE15_6DU_SELECTED_ROUTE=RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER
STAGE15_6DU_FIXED_PRIME_SIEVE=LIVE_QUALITATIVE_BACKUP
STAGE15_6DU_PARKING_ALLOWED=false
STAGE15_6DU_DELTA_PROVED=false
STAGE15_6DU_SIGMA_PROVED=false
STAGE15_6DU_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DU_SPLIT_TRIGGER=false
STAGE15_6DU_AUDIT_REQUIRED=true
STAGE15_6DU_CODEX_REQUIRED=false
STAGE15_6DU_MERGE_ALLOWED=false
STAGE15_6DU_EXIT=FRESH_AUDIT_OF_PELL_NEGATIVE_CERTIFICATE_AND_RESIDUAL_SWITCH_SELECTION
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6du
NEXT_GATE=FRESH_AUDIT_OF_PELL_NEGATIVE_CERTIFICATE_AND_RESIDUAL_SWITCH_SELECTION
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```
