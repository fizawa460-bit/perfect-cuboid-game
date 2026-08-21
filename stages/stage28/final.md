# Stage28 final — Stage19 -> Stage20 matched bridge comparison

```text
STAGE=Stage28
CHECKPOINT70_AUDIT=PASS
STATUS=AUDITED_FINAL_PENDING_PR_MERGE
COMPARISON=Stage19 -> Stage20
PHYSICAL_CUTOFF=R<=B
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Population contract

Stage28 compares two disjoint exact-face populations under the same primitive/canonical physical cutoff:

- `N2(B)`: exactly two integral face diagonals **and** integral space diagonal;
- `M3(B)`: exactly three integral face diagonals (Euler cuboids), with no space-diagonal requirement.

This is not an objectwise survival transition. With

\[
H_{\ge2}=M_2+M_3,\qquad
\Sigma_{19}=N_2/H_{\ge2},\qquad
\Phi_{20}=M_3/H_{\ge2},
\]

one has the exact common-host identity

\[
\boxed{M_3/N_2=\Phi_{20}/\Sigma_{19}}.
\]

## 2. Strongest certified theorem surface

The Stage28 closeout theorem stack is

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}>0,
\]

and, for every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Also

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

with `H_ge2(B)~M2(B)`.

Consequently the currently certified direct bridge corridor is

\[
\boxed{M_3/N_2\gg_\varepsilon B^{-1/6-\varepsilon}}
\]

and, for every fixed `0<delta<1/46`,

\[
\boxed{M_3/N_2=o\!\left(B^{3/4}(\log B)^{5-\delta}\right)}.
\]

Neither true population exponent is known, and no eventual ordering of `M3` and `N2` follows.

## 3. Normalized interaction compression

Define

\[
\mathcal I_{sp}=\frac{N_2/M_2}{N_1/M_1},
\qquad
\mathcal I_{face}=\frac{M_3/M_2}{M_2/M_1},
\]

\[
\mathcal J_{28}=\frac{\mathcal I_{face}}{\mathcal I_{sp}},
\qquad
\mathcal K_{28}=(\log B)^2\mathcal J_{28}.
\]

Then

\[
\boxed{
\frac{M_3}{N_2}
\sim \frac{24\pi C_{M_2}}{\kappa}\,\mathcal K_{28}.
}
\]

Thus the raw interaction threshold is `(log B)^(-2)`. The equality scale `M3/N2~1` is

\[
\boxed{\mathcal K_{28}\sim\frac{\kappa}{24\pi C_{M_2}}}
\]

or equivalently

\[
\boxed{
\mathcal J_{28}\sim
\frac{\kappa}{24\pi C_{M_2}}(\log B)^{-2}.
}
\]

Current bounds do not place `J_28` on either side of this threshold.

Because `H_ge2~M2`, both common-host shares satisfy

\[
\Sigma_{19}\to0,\qquad \Phi_{20}\to0.
\]

The unresolved Stage28 question is therefore their **relative vanishing rate**.

## 4. Causal/geometric synthesis

Both completion problems are degree-two K3 covers of the common toric base

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad L=-K_Y,
\]

with the same total branch class `-2K_Y`. The known normalized local quotient and generic thin-cover interfaces do not separate the two marginals by a power of `B` or by a first-order logarithmic power.

The first certified geometric differential is the branch profile:

```text
Stage19 space cover      = 4 x genus-0 branch components
Stage20 third-face cover = 2 x genus-1 branch components
```

Their physical quasi-polarizations use the same common-base normalization on distinct K3 surfaces:

\[
M_{sp}=\pi_{sp}^*L,\qquad
M_{face}=\pi_{face}^*L,\qquad
M_{sp}^2=M_{face}^2=8.
\]

The audited low-degree spectrum gives

```text
Stage19 physical M4 rational curves = absent
Stage19 every odd physical M-degree = absent
Stage20 Saunderson physical M-degree = 6
Stage19 physical M6 absence          = not proved
```

Hence Stage20 attains a fixed rational curve at physical degree six, while Stage19 has no fixed rational curve below six. This is a genuine causal differential, but it is not a global ordering theorem: Stage19 may have M6 curves and retains moving-fibre/rank-jump/first-small-point mechanisms.

## 5. Construction-side information

The strongest explicit construction scales currently certified are

```text
Stage19 N2 construction exponent = 1/4
Stage20 M3 construction exponent = 1/3
Stage20 explicit liminf coefficient = 27/(40*pi^2)
```

The selected-family exponent gap `1/12` is not promoted to a full-population exponent gap.

## 6. Finite evidence firewall

At matched cutoffs `B=10^4, 5*10^4, 2*10^5, 10^6`, the finite ratios are

```text
M3/N2 = 0.72, 0.677419355, 0.706896552, 0.858823529
```

They are diagnostics only. No finite trend, fitted exponent, or perfect-cuboid conclusion is used as theorem evidence.

## 7. Remaining receivers

Primary global receiver:

```text
OPEN_GATE=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
BASE=Y=Bl_4(P1xP1)
SPACE_BRANCH_PROFILE=4x_genus0
THIRD_FACE_BRANCH_PROFILE=2x_genus1
HEIGHT=physical R<=B
TARGET=J_28=I_face/I_sp
CRITICAL_SCALE=(log B)^(-2)
NORMALIZED_TARGET=K_28=(log B)^2*J_28
ORDERING_THRESHOLD=kappa/(24*pi*C_M2)
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

Optional finite refinement:

```text
PhysicalLowDegreeRootSpectrumM6
```

A complete M6 classification could decide strict fixed-curve degree-six separation, but cannot by itself control the moving complement or the global ratio.

Construction-side future receiver:

```text
UniformMovingEllipticFibreSquareLiftHeightCount
```

## 8. Reusable Stage28 weapons

Checkpoint70 audits the following Stage28 promotion cards for downstream reuse:

```text
S28-W01 = common-host bridge adapter
S28-W02 = normalized interaction-curvature adapter
S28-W03 = branch-profile geometric differential
S28-W04 = common-polarization fixed-curve differential
```

Their selection firewalls remain mandatory; in particular the `(log B)^2` normalizer is charged exactly once, and neither branch topology nor fixed-curve spectrum is promoted to a global population saving without a theorem controlling the moving complement.

## 9. Stage29 handoff

Stage29 should consume Stage28 as an unresolved but sharply normalized interaction comparison. It must retain `M3/N2` as a matched common-host size ratio, retain `K_28` and its threshold exactly once, distinguish local/branch/fixed-curve/moving/construction mechanisms, and preserve the perfect-cuboid endpoint firewall.

An already-open Stage29 PR (`#1283`) was created before the final Stage28-60-r3/70 state was available. It therefore requires refresh against the merged Stage28 final state before its own audit can be treated as authoritative.

```text
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
SYNTHESIS_STOP_RULE_SATISFIED=YES
STAGE28_CLASS=BOUNDED_SYNTHESIS_COMPLETE_WITH_RESEARCH_READY_OPEN_GATE
STAGE29_OPEN_PR_REQUIRES_STAGE28_FINAL_REFRESH=true
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PASS
MERGE_ALLOWED=true
```

Detailed provenance remains in `stages/stage28/28-70/`, the prior audited Stage28 checkpoint folders, and `docs/stage28-arsenal-promotion.md`.