# Stage28-60-r3 — fixed-curve spectrum deepening / bounded stop candidate

```text
TASK_ID=Stage28-60-r3
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_R2=AUDITED_PASS_MERGED_PR1281
```

## New causal differential, sharpened by exact lattice CI

The Stage19 space-cover physical quasi-polarization satisfies `M^2=8`. Audited Stage14-4ah proves every physical rational curve has `M.C>=4`, and Stage14-4ak proves the complete physical `M.C=4` stratum empty.

r3 reconstructs the same official Shimada physical anti-invariant lattice and obtains a rank-six positive Gram form of determinant `256` whose diagonal entries are divisible by four and off-diagonal entries are even. Hence every anti-invariant norm is divisible by four.

For a physical odd-degree curve `C`, the audited positive-branch firewall excludes ramification on the physical open, while a connected degree-two pullback has even physical degree. Thus an odd-degree curve must split into `C,delta(C)`. With `x=C-delta(C)`, the K3 even lattice and base adjunction parity imply

\[
\boxed{-x^2\equiv2(M\cdot C)\pmod4.}
\]

This contradicts the anti-invariant mod-four norm law whenever `M.C` is odd. Therefore the new candidate theorem is

\[
\boxed{\text{all physical Stage19 fixed rational curves have even }M\text{-degree}.}
\]

In particular

\[
\boxed{M\cdot C=5\text{ is impossible}.}
\]

Together with the audited M4 void, every fixed physical Stage19 rational curve has `M.C>=6`. Hence any finite union of fixed source rational curves contributes at polynomial exponent at most

\[
\boxed{O(B^{1/3})}.
\]

Exact-head GitHub Actions run `32437537363` concludes success and reproduces the physical Shimada labeling equivalence, anti-invariant rank `6`, determinant `256`, and norm congruence. Fresh mathematical audit remains required.

On the Stage20 side, the audited generalized Saunderson parametrization is a generically injective homogeneous degree-six rational family under the physical coordinate height, with `R asymp r^6` on the audited cone. It supplies a fixed rational target curve with

\[
\boxed{\Theta(B^{1/3})}
\]

points on that sector.

Thus the fixed-rational-curve spectra now meet at the same polynomial `1/3` scale at worst: the former possible Stage19 degree-five / `2/5` channel is closed.

## Why this still does not resolve the bridge

The source may possess physical M-degree-six rational curves. More importantly, Stage14-4al proves that the source's possible square-root-scale behavior is a moving-fibre activation / first-small-point problem after the degree-four fixed-curve mechanism was eliminated. Fixed-curve spectra therefore cannot be promoted to whole-population ordering without a complement theorem.

The audited r2 equivalence remains the direct bridge:

\[
M_3/N_2\sim (24\pi C_{M_2}/\kappa)\,K_{28},
\qquad K_{28}=(\log B)^2 I_{face}/I_{sp}.
\]

No r3 route places `I_face/I_sp` on one side of the critical `(log B)^(-2)` threshold.

## Literature boundary

McKinnon's hyperelliptic-K3 accumulating-curve theorem is structurally close but requires an ample divisor; the exact physical Stage19 polarization is big-and-nef non-ample, so direct transfer remains invalid. Rams--Schuett's 2025 quasi-polarized low-degree rational-curve bounds do not directly classify the required degree-six stratum at the present low quasi-polarization degree `M^2=8`.

## Final r3 receivers

The former M5/M6 finite receiver has been reduced to a single genuinely new finite classification:

```text
FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
INPUT=existing Shimada Stage14 lattice + physical M/deck/chamber/Q-descent data
OUTPUT=classify all Stage19 physical rational curves M.C=6, including split and invariant mechanisms
```

This is no longer a routine consequence of the M4 calculation: degree six permits both even-degree geometric mechanisms and the mod-four norm obstruction alone does not decide it.

Even a successful M6 spectrum classification remains only an intermediate causal certificate. The true global receiver is

```text
OPEN_GATE_60_R3=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
TARGET=I_face/I_sp relative to (log B)^(-2)
HEIGHT=physical R<=B
MAY_USE=fixed-curve spectrum, branch profile, same-host arithmetic
MUST_CONTROL=moving/collective complement
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

## Bounded-stop verdict candidate

Checkpoint60 parent/r2/r3 has now explored exact interaction algebra, local densities, growing-prime sieve, degree-two/K3 geometry, branch decomposition, construction efficiency, interaction curvature, McKinnon accumulating curves, quasi-polarized low-degree curves, exact Stage14 M4 lattice exclusion, and the new odd-degree anti-invariant congruence.

Further routine rearrangement of current repo theorems cannot cross the critical threshold. The only remaining repo-native low-degree task is a genuinely new complete M6 lattice/chamber/descent classification; the global unresolved lane needs a substantially new moving-complement theorem.

```text
CHECKPOINT60_R3_COMPLETE_AS_SUBMISSION=true
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=FIXED_CURVE_SPECTRUM_PLUS_ODD_DEGREE_OBSTRUCTION
STAGE19_PHYSICAL_M4_FIXED_CURVE=ABSENT_AUDITED
STAGE19_PHYSICAL_M5_FIXED_CURVE=ABSENT_CANDIDATE
STAGE19_PHYSICAL_ODD_FIXED_CURVE_DEGREES=ABSENT_CANDIDATE
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
STAGE20_SAUNDERSON_FIXED_CURVE_EXPONENT=1/3
R3_MATERIALLY_DISTINCT_ROUTES=6
LOW_DEGREE_EXACT_HEAD_CI=PASS_RUN_32437537363
SOURCE_TARGET_ORDERING_IDENTIFIED=false
MAXIMAL_BOUNDED_EXPLORATION_CANDIDATE=true
OPEN_GATE_RESEARCH_REQUEST_READY=true
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=70
NEXT_EXPECTED_COMMAND=Stage28-audit
PERFECT_CUBOID_CONCLUSION=NONE
```