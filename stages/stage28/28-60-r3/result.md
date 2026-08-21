# Stage28-60-r3 — fixed-curve spectrum deepening / bounded-stop candidate

```text
TASK_ID=Stage28-60-r3
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_R2=AUDITED_PASS_MERGED_PR1281
EXECUTION_MODE=SPLIT_AFTER_LONG_RUN_TIMEOUT
```

## 1. Source low-degree spectrum

Audited Stage14-4ah fixes the Stage19 space-cover physical quasi-polarization

\[
M_{sp}=\pi_{sp}^*(-K_Y),\qquad M_{sp}^2=8,
\]

with the actual physical cuboid cutoff as its height. Audited Stage14-4ak proves the complete physical `M_sp.C=4` rational-bisection stratum empty.

The r3 exact Shimada reconstruction gives a rank-six physical anti-invariant lattice of determinant `256`, with every integral norm divisible by four. For an odd-degree physical split curve, with `x=C-\delta C`, the lattice/adjunction identity is

\[
-x^2\equiv2(M_{sp}\cdot C)\pmod4.
\]

Hence every odd physical `M_sp`-degree is impossible, subject to fresh mathematical audit. In particular `M_sp.C=5` is excluded as an r3 candidate theorem. Together with the audited M4 void, the source fixed-curve degree floor becomes

\[
M_{sp}\cdot C\ge6
\]

at submission level, so any finite union of fixed source rational curves has polynomial exponent at most `1/3`.

The classical 40 distinguished Shimada roots have physical M-degree histogram

```text
0 : 16
2 : 24
6 : 0
```

but `L40` is not the complete root spectrum; source M6 remains open.

## 2. Split execution of the target degree question

The long r3 run was split into independent certificates:

```text
r3A = source polarization lock
r3B = target physical-polarization adapter
r3C = exact Saunderson physical M-degree-six certificate
```

Artifacts:

- `split-a-source-polarization-lock.md`
- `split-b-target-polarization-adapter.md`
- `split-c-saunderson-mdegree6-certificate.md`
- `saunderson_physical_degree6_probe.py`

### Common physical polarization normalization

Stage14-e3 fixes the common two-face toric base

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad L=-K_Y,
\]

and the physical edge-coordinate map `phi:Y->P2` with

\[
\phi^*\mathcal O_{\mathbf P^2}(1)=L.
\]

The Stage19 and Stage20 completion surfaces are different degree-two K3 covers of the same `Y`, but their physical quasi-polarizations are constructed identically:

\[
M_{sp}=\pi_{sp}^*L,\qquad M_{face}=\pi_{face}^*L,
\qquad M_{sp}^2=M_{face}^2=8.
\]

Thus “same physical polarization” means the same common-base line-bundle normalization, not literally the same divisor on the same K3. Both physical heights are read from the same edge-coordinate `O_{P2}(1)` model, with no power-loss adapter.

### Exact Saunderson M-degree

For homogeneous Euclid parameters `[r:s]`, put

\[
u=r^2-s^2,\quad v=2rs,\quad w=r^2+s^2,
\]

and signed Saunderson coordinates

\[
A=u(4v^2-w^2),\quad B=v(4u^2-w^2),\quad C=4uvw,
\]
\[
D=w^3,\quad E=u(4v^2+w^2),\quad F=v(4u^2+w^2).
\]

All six forms are homogeneous of degree six. The edge forms `A,B,C` have no common nonconstant factor, so the physical edge map pulls back `O_{P2}(1)` to `O_{P1}(6)`.

The full K3 map is generically birational because

\[
E-A=2uw^2,\qquad F-B=2vw^2,
\]

and therefore on a dense open set

\[
\boxed{\frac{s}{r}=\frac{F-B}{2D+E-A}}.
\]

Hence for the Saunderson image curve `C_S`,

\[
\boxed{M_{face}\cdot C_S=6}.
\]

On the audited positive-density cone the physical height is `R\asymp r^6`, so this fixed rational curve contributes exactly the expected polynomial scale

\[
\boxed{\Theta(B^{1/3})}.
\]

This upgrades the old informal “homogeneous degree-six family” language to an exact physical `M_face`-degree-six statement under the same Stage28 polarization normalization as the Stage19 spectrum, subject to fresh audit.

## 3. Route verdict

This is a materially distinct final r3 route:

```text
R28_COMMON_PHYSICAL_POLARIZATION_SAUNDERSON_M6_CERTIFICATE=SUCCESS_CANDIDATE
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE=6_CANDIDATE
STAGE20_FIXED_M6_RATIONAL_CURVE=PRESENT_CANDIDATE
STAGE19_M4_FIXED_CURVE=ABSENT_AUDITED
STAGE19_M5_FIXED_CURVE=ABSENT_CANDIDATE
STAGE19_M6_FIXED_CURVE_ABSENT=false
```

The low-degree spectra are therefore asymmetric through degree five, and Stage20 is certified at submission level to attain degree six. But the source may also possess physical M6 curves. So the new route is a genuine causal differential, not yet a strict degree-six spectral separation.

The remaining finite receiver is exactly

```text
FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```

including non-distinguished roots, invariant/split even-degree mechanisms, singular rational members, lattice gluing, effectivity/chamber, boundary, automorphism, Q-descent and physical-open filtering.

## 4. Why checkpoint60 is still not numerically resolved

The audited r2 bridge remains

\[
M_3/N_2\sim (24\pi C_{M_2}/\kappa)K_{28},
\qquad
K_{28}=(\log B)^2 I_{face}/I_{sp}.
\]

No r3 fixed-curve argument places `I_face/I_sp` on one side of the critical `(log B)^(-2)` threshold. Stage14-4al also leaves the Stage19 moving-fibre/rank-jump/first-small-point complement alive, so a fixed-curve classification cannot by itself order the full populations.

The global receiver remains

```text
OPEN_GATE_60_R3=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
TARGET=I_face/I_sp relative to (log B)^(-2)
HEIGHT=physical R<=B
MUST_CONTROL=moving/collective complement
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

## 5. Bounded-stop submission state

Checkpoint60 parent/r2/r3 has now exhausted the routine repo-native rearrangements tested so far. The two remaining tasks are genuinely new: complete source M6 classification and a global moving-complement theorem. Neither is silently inferred from current CI or finite diagnostics.

```text
CHECKPOINT60_R3_COMPLETE_AS_SUBMISSION=true
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=LOW_DEGREE_SPECTRUM_PLUS_ODD_DEGREE_OBSTRUCTION_PLUS_COMMON_POLARIZATION_M6_CERTIFICATE
STAGE19_PHYSICAL_M4_FIXED_CURVE=ABSENT_AUDITED
STAGE19_PHYSICAL_M5_FIXED_CURVE=ABSENT_CANDIDATE
STAGE19_PHYSICAL_ODD_FIXED_CURVE_DEGREES=ABSENT_CANDIDATE
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE=6_CANDIDATE
STAGE20_SAUNDERSON_FIXED_CURVE_EXPONENT=1/3
STRICT_SOURCE_TARGET_M6_SPECTRAL_SEPARATION=false
DISTINGUISHED_L40_M6_COUNT=0
DISTINGUISHED_L40_IS_COMPLETE_ROOT_SPECTRUM=false
R3_MATERIALLY_DISTINCT_ROUTES=8
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
