# Stage28 arsenal promotion

```text
REGISTRY=STAGE28-ARSENAL-R01
STATUS=AUDITED_ACTIVE_PENDING_PR_MERGE
SOURCE_STAGE=Stage28
SOURCE_CHECKPOINT=70
AUDIT_VERDICT=PASS
```

These cards passed the Stage28 checkpoint70 audit and are approved for downstream Stage29 reuse after the closeout PR is merged.

## S28-W01 — common-host bridge adapter

**Type:** `ADAPTER`

For the primitive/canonical physical cutoff `R<=B`, Stage19 `N2` and Stage20 `M3` are disjoint exact-face strata. With

\[
H_{\ge2}=M_2+M_3,
\qquad
\Sigma_{19}=N_2/H_{\ge2},
\qquad
\Phi_{20}=M_3/H_{\ge2},
\]

one has

\[
\boxed{M_3/N_2=\Phi_{20}/\Sigma_{19}}.
\]

```text
ID=S28-W01
SEMANTICS=MATCHED_POPULATION_SIZE_RATIO
LITERAL_SURVIVAL_PROBABILITY=false
COMMON_HOST=H_ge2=M2+M3
```

## S28-W02 — normalized interaction-curvature adapter

**Type:** `INVARIANT_ADAPTER`

Define

\[
\mathcal I_{sp}=\frac{N_2/M_2}{N_1/M_1},
\qquad
\mathcal I_{face}=\frac{M_3/M_2}{M_2/M_1},
\]

\[
\mathcal J_{28}=\mathcal I_{face}/\mathcal I_{sp},
\qquad
\mathcal K_{28}=(\log B)^2\mathcal J_{28}.
\]

Using the audited `N1` and `M2` asymptotics,

\[
\boxed{
M_3/N_2\sim \frac{24\pi C_{M_2}}{\kappa}\mathcal K_{28}.
}
\]

Hence the raw critical scale is `J_28~(log B)^(-2)`, and the equality threshold is

\[
\boxed{
K_{28}\sim\frac{\kappa}{24\pi C_{M_2}}
}
\]

or equivalently

\[
J_{28}\sim\frac{\kappa}{24\pi C_{M_2}}(\log B)^{-2}.
\]

```text
ID=S28-W02
NORMALIZER=(log B)^2
ORDERING_THRESHOLD=kappa/(24*pi*C_M2)
DOUBLE_CHARGE_NORMALIZER_FORBIDDEN=true
```

## S28-W03 — branch-profile geometric differential

**Type:** `GEOMETRIC_DIFFERENTIAL`

On the common base `Y=Bl_4(P1xP1)`, both completion problems are degree-two K3 covers with total branch class `-2K_Y`, but their branch-component profiles differ:

```text
Stage19 space cover      = 4 x genus0
Stage20 third-face cover = 2 x genus1
```

The normalized local quotient and generic Huang thin-cover interfaces do not currently convert this difference into a power or first-order log-power marginal comparison.

```text
ID=S28-W03
BRANCH_PROFILE_DIFFERENT=true
GLOBAL_COUNT_SAVING_FROM_PROFILE=false
RECEIVER=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
```

## S28-W04 — common-polarization fixed-curve differential

**Type:** `FIXED_CURVE_DIFFERENTIAL`

With `L=-K_Y`, the distinct Stage19 and Stage20 K3 surfaces use the same physical degree normalization

\[
M_{sp}=\pi_{sp}^*L,
\qquad
M_{face}=\pi_{face}^*L,
\qquad
M_{sp}^2=M_{face}^2=8.
\]

Audited Stage28-60-r3 gives

```text
Stage19 physical M4 curves = absent
Stage19 odd physical M-degrees = absent
Stage20 Saunderson physical M-degree = 6
Stage19 physical M6 absence = not proved
```

Thus the spectra are asymmetric through degree five and Stage20 attains degree six, but strict M6 separation and whole-population ordering are not proved.

```text
ID=S28-W04
STRICT_M6_SOURCE_TARGET_SEPARATION=false
FIXED_CURVE_DIFFERENTIAL_IS_GLOBAL_ORDERING=false
OPTIONAL_FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```

## Selection firewalls

- Do not treat `S28-W01` as an objectwise survival probability.
- Do not multiply `S28-W02` by the `(log B)^2` intermediate-population gap again.
- Do not promote `S28-W03` branch topology alone to a counting saving.
- Do not promote `S28-W04` to strict M6 separation or to a full-population order.
- Do not use the deferred perfect-cuboid endpoint to discharge any Stage28 receiver.

```text
ARSENAL_WEAPONS=S28-W01,S28-W02,S28-W03,S28-W04
PROMOTION_AUDIT=PASS
PROMOTION_ACTIVE_AFTER_MERGE=true
PERFECT_CUBOID_CONCLUSION=NONE
```
