# Stage27-20-r301 — Stage20 upper-mechanism reentry

```text
TASK_ID=Stage27-20-r301
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage20
TRIGGER_CHECKPOINT=30
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Purpose

Re-open the closed Stage20 Euler-brick upper machinery as a source of upper-bound mechanisms for the Stage27 target

\[
N_2(B)=\#\{0<a<b<c,\ \gcd(a,b,c)=1,\ R\in\mathbf Z,\ R\le B,\ \text{exactly two integral face diagonals}\}.
\]

This route does **not** identify the Stage20 population `M3` with `N2` and does not infer an `N2` upper bound from the Stage20 theorem by population inclusion.

## 2. Population non-containment firewall

Stage20 counts primitive canonical Euler bricks with all three face diagonals integral and no condition on the space diagonal. Stage27 `N2` counts objects with exactly two integral face diagonals and an integral space diagonal. Therefore neither population contains the other in general.

```text
M3_SUBSET_N2=false
N2_SUBSET_M3=false
STAGE20_UPPER_DIRECTLY_BOUNDS_N2=false
```

Any useful import must occur at the level of a common pre-completion host and a new completion condition.

## 3. Common two-face host and orientation partition

Every `N2` object has exactly two integral faces. There are three choices for the missing face, and at least one integral face contains the largest edge `c`. Thus `N2` decomposes into at most three oriented two-face hosts, each defined by two primitive Pythagorean constraints plus the physical cutoff.

Stage20 e10/e11 also starts from the same species of shared-edge two-face toric host and then imposes the **third-face completion** condition.

For Stage27, after fixing an oriented exactly-two-face host, the new completion condition is instead the **space-diagonal square condition**, while the missing face must remain nonsquare.

Hence the legal transfer interface is

```text
COMMON_HOST=SHARED_EDGE_TWO_FACE_TORIC_HOST
STAGE20_COMPLETION=THIRD_FACE_SQUARE
STAGE27_COMPLETION=SPACE_DIAGONAL_SQUARE
STAGE27_EXCLUSION=MISSING_FACE_NONSQUARE
```

The target polynomial/squareclass is different, so Stage20 local densities and thin-cover constants cannot be copied verbatim.

## 4. Stage20 e8 divisor-envelope transfer test

Stage20 checkpoint40 / Stage14-e8 projects the Euler-brick population to a Pythagorean pair on the two largest edges and bounds the remaining completion multiplicity by a divisor envelope, giving

\[
M_3(B)\ll B\log B\exp(O(\log B/\log\log B))=B^{1+o(1)}.
\]

The projection/divisor method is structurally reusable on an oriented Stage27 two-face host, but without exploiting the integral-space condition it can provide at best a linear-scale host estimate. Stage27 already has the much stronger audited bound

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

Therefore the raw Stage20 e8 divisor-envelope transplant is dominated and cannot improve the Stage27 exponent by itself.

```text
E8_PROJECTION_STRUCTURALLY_REUSABLE=true
E8_RAW_TRANSPLANT_STRICT_SUBHALF=false
E8_RAW_TRANSPLANT_DOMINATED_BY_STAGE27_HALFPOWER=true
```

## 5. Stage20 e10/e11 thin-cover transfer test

Stage20 e10/e11 obtains a log-saving thin-cover theorem and an exact local blocker law for the third-face square condition on the common two-face host. The local odd-prime defect is of order `2/p` and the resulting sieve is logarithmic in strength.

For Stage27 the selected square is the space diagonal, not the third face. Stage15-6 already supplies the relevant same-measure local squareclass law for the Stage27 space condition; its product is likewise logarithmic and checkpoint40 has already certified that the same local tensor alone cannot yield a fixed power of `B`.

Thus importing the Stage20 **specific third-face local factors** is illegal, while importing only the general thin-cover architecture does not currently beat the Stage27 half-power wall.

```text
STAGE20_THIRD_FACE_LOCAL_FACTORS_TRANSFER_TO_SPACE=false
THIN_COVER_ARCHITECTURE_REUSABLE_IN_PRINCIPLE=true
LOG_SIEVE_ALONE_FIXED_POWER=false
```

## 6. Exact useful reopen contract

The Stage20 reentry is useful only if the common two-face host admits a new theorem for the **space-diagonal completion cover** with a same-physical-measure fixed-power deficit on the saturation band.

A sufficient form is any theorem that, on each retained Stage27 saturation cell / oriented two-face host, gives

\[
\#\{\text{space-square survivors}\}
\ll B^{-\delta}\,\#\{\text{corresponding complete host}\}
\]

for one fixed `delta>0`, with the missing-face nonsquare restriction charged at most once and with only `B^{o(1)}` multiplicity loss.

Equivalent acceptable interfaces include:

1. a Stage20-style thin-cover theorem for the **space-diagonal cover** whose physical-height exponent genuinely drops below the existing `1/2` host envelope;
2. a horizontal support theorem on the common two-face host with a fixed-power deficit;
3. a weighted exceptional-mass theorem for the space-square target classes in the actual Stage27 physical measure.

Merely reproducing Stage20's `B^(1+o(1))` divisor envelope or a logarithmic local sieve is not progress.

## 7. Result

```text
STAGE27_20_R301_EXECUTED=true
SOURCE_STAGE20_UPPER_READ=true
POPULATION_NONCONTAINMENT_PROVED=true
COMMON_TWO_FACE_HOST_IDENTIFIED=true
E8_RAW_TRANSPLANT_DOMINATED=true
STAGE20_LOCAL_FACTORS_DIRECT_TRANSFER_FORBIDDEN=true
SPACE_DIAGONAL_THIN_COVER_FIXED_POWER_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_DERIVED_ROUTE=27-20-r301a
NEXT_EXPECTED_COMMAND=Stage27-20-r301-audit
```

## 8. Next route

`27-20-r301a` should build the actual Stage27 space-diagonal double-cover equation over the Stage20 shared-edge two-face toric host and compare its branch geometry with the Stage20 third-face K3 cover. The first question is geometric: same cover type or genuinely different surface? Only after that should local factors or thin-cover estimates be attempted.
