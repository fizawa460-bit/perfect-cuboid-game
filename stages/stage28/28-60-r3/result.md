# Stage28-60-r3 — fixed-curve spectrum deepening / bounded stop candidate

```text
TASK_ID=Stage28-60-r3
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_R2=AUDITED_PASS_MERGED_PR1281
```

## New causal differential

The Stage19 space-cover physical quasi-polarization satisfies `M^2=8`.  Audited Stage14-4ah proves every physical rational curve has `M.C>=4`, and Stage14-4ak proves the complete physical `M.C=4` stratum empty.  Hence any finite union of fixed physical Stage19 rational curves has polynomial bounded-height contribution at most

\[
O(B^{2/5}).
\]

On the Stage20 side, the audited generalized Saunderson parametrization is a generically injective homogeneous degree-six rational family under the physical coordinate height, with `Rasymp r^6` on the audited cone.  It supplies a fixed rational target curve with

\[
\Theta(B^{1/3})
\]

points on that sector.

Thus fixed-rational-curve spectra form a genuine Stage19/Stage20 causal differential not detected by the common local/K3/thin-cover ledger.

## Why this still does not resolve the bridge

The source may still have physical degree-five or degree-six rational curves. More importantly, Stage14-4al proves that the source's possible square-root-scale behavior is a moving-fibre activation / first-small-point problem after the degree-four fixed-curve mechanism was eliminated.  Therefore fixed-curve spectra cannot be promoted to whole-population ordering without a complement theorem.

The audited r2 equivalence remains the direct bridge:

\[
M_3/N_2\sim (24\pi C_{M_2}/\kappa)\,K_{28},
\qquad K_{28}=(\log B)^2 I_{face}/I_{sp}.
\]

No r3 route places `I_face/I_sp` on one side of the critical `(log B)^(-2)` threshold.

## Literature boundary

McKinnon's hyperelliptic-K3 accumulating-curve theorem is structurally close but requires an ample divisor; the exact physical Stage19 polarization is big-and-nef non-ample, so direct transfer remains invalid.  Rams--Schuett's 2025 quasi-polarized low-degree rational-curve bounds do not directly classify the required degree-five/six strata at the present low quasi-polarization degree `M^2=8`.

## Final r3 receivers

A bounded finite computation remains available:

```text
FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM5M6
INPUT=existing Shimada Stage14 lattice + physical M/deck/chamber/Q-descent data
OUTPUT=classify Stage19 physical rational roots M.C=5,6; compare Stage20 physical degree<=6 spectrum
```

But even a successful spectrum classification is only an intermediate causal certificate. The true global receiver remains

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

The checkpoint has now used parent/r2/r3 routes covering exact interaction algebra, local densities, growing-prime sieve, degree-two/K3 geometry, branch decomposition, construction efficiency, interaction curvature, McKinnon accumulating curves, quasi-polarized low-degree curves, and exact Stage14 lattice exclusions.

Further routine rearrangement of current repo theorems cannot cross the critical threshold.  Remaining work requires either the explicit finite degree-5/6 lattice computation above or a substantially new global moving-complement theorem.

```text
CHECKPOINT60_R3_COMPLETE_AS_SUBMISSION=true
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=FIXED_CURVE_SPECTRUM
STAGE19_PHYSICAL_M4_FIXED_CURVE=ABSENT
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX=2/5
STAGE20_SAUNDERSON_FIXED_CURVE_EXPONENT=1/3
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