# Stage28 self-contained closeout bundle

`STATUS=CHECKPOINT70_CANDIDATE_PENDING_FRESH_AUDIT`

## Population contract

Under the common primitive/canonical Euclidean cutoff `R<=B`, Stage28 compares

\[
N_2(B)=\#\{\text{exactly two integral faces + integral space diagonal}\}
\]

with

\[
M_3(B)=\#\{\text{exactly three integral faces; no space requirement}\}.
\]

They are disjoint exact-face strata, not an objectwise transition. On the literal common host

\[
H_{\ge2}=M_2+M_3,
\qquad
\Sigma_{19}=N_2/H_{\ge2},
\qquad
\Phi_{20}=M_3/H_{\ge2},
\]

one has the exact matched-size identity

\[
\boxed{M_3/N_2=\Phi_{20}/\Sigma_{19}}.
\]

## Frozen theorem stack

The strongest current Stage28 inputs are

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

\[
\liminf_{B\to\infty}M_3(B)/B^{1/3}\ge 27/(40\pi^2)>0,
\]

and, for fixed `0<eta<1/46`,

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

and `H_ge2~M2`.

Consequently

\[
M_3/N_2\gg_\varepsilon B^{-1/6-\varepsilon}
\]

while, for fixed `0<delta<1/46`,

\[
M_3/N_2=o\!\left(B^{3/4}(\log B)^{5-\delta}\right).
\]

No limit or eventual ordering follows.

## Relative-interaction compression

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
\sim A_{28}\mathcal K_{28},
\qquad
A_{28}=\frac{24\pi C_{M_2}}{\kappa}>0.
}
\]

Thus the raw critical interaction scale is `(log B)^(-2)`. More precisely, the equality threshold is

\[
\boxed{
\mathcal K_{28}\sim \frac{\kappa}{24\pi C_{M_2}}
}
\]

or equivalently

\[
\boxed{
\mathcal J_{28}\sim
\frac{\kappa}{24\pi C_{M_2}}(\log B)^{-2}.
}
\]

A theorem placing `K_28` eventually strictly above this constant would prove `M3>N2`; placing it eventually strictly below would prove `M3<N2`. No such theorem is certified.

Because `H_ge2~M2`, both common-host shares vanish:

\[
\Sigma_{19}\to0,
\qquad
\Phi_{20}\to0.
\]

The Stage28 issue is their relative vanishing rate.

## Causal comparison

Both completion problems live over the common toric base

\[
Y=Bl_4(P^1\times P^1),\qquad L=-K_Y.
\]

At the generic-cover/local level the known machinery does not separate them by a power of `B` or by a first-order log-power: both are degree-two covers with total branch class `-2K_Y`, and the normalized good-prime local quotient contributes only a finite Euler-product bias.

The first sharp geometric differential is

```text
Stage19 space cover:      4 rational branch components
Stage20 third-face cover: 2 genus-one branch components
```

The physical quasi-polarizations use the same base normalization,

\[
M_{sp}=\pi_{sp}^*L,
\qquad
M_{face}=\pi_{face}^*L,
\qquad
M_{sp}^2=M_{face}^2=8,
\]

but live on distinct K3 surfaces.

The audited low-degree comparison gives

```text
Stage19 physical M4 rational curve: absent
Stage19 every odd physical M-degree: absent
Stage20 Saunderson physical M-degree: 6
Stage19 M6 absence: not proved
```

So Stage20 realizes a fixed rational curve with `B^(1/3)` height count, while Stage19 has no fixed rational curve of physical degree below six. This is a real causal differential, but it is not a global population ordering theorem: Stage19 may have M6 curves and retains moving-fibre/rank-jump/first-small-point mechanisms.

## Construction comparison

The strongest known explicit construction scales are

```text
Stage19 N2: exponent 1/4
Stage20 M3: exponent 1/3, explicit positive liminf coefficient 27/(40*pi^2)
```

The selected-family exponent gap `1/12` is not a population exponent gap because neither true population exponent is known.

## Finite evidence firewall

The matched finite ratios at `B=10^4, 5*10^4, 2*10^5, 10^6` are

```text
M3/N2 = 0.72, 0.677419355, 0.706896552, 0.858823529.
```

They are nonmonotone on this panel and are used only as finite diagnostics. No finite effective exponent, trend, or perfect-cuboid conclusion is promoted.

## Open receivers

Primary Stage28 frontier:

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
```

Optional finite refinement:

```text
PhysicalLowDegreeRootSpectrumM6
```

This could decide strict fixed-curve M6 separation but cannot by itself control the moving complement or the full ratio `M3/N2`.

A separate construction-side future theorem species remains

```text
UniformMovingEllipticFibreSquareLiftHeightCount
```

which could improve Stage20's one-third construction scale or furnish a stronger matched marginal input.

## Stage29 handoff

Stage29 should consume Stage28 as an unresolved but sharply normalized interaction comparison:

- retain `M3/N2` as a matched common-host size ratio, never a survival probability;
- retain `K_28` and its equality threshold constant exactly once;
- preserve the distinction among local, branch-geometric, fixed-curve, moving-family, and explicit-construction mechanisms;
- record that current theorems do not identify the Stage19/Stage20 ordering;
- keep all perfect-cuboid endpoint counts outside the Stage28 comparison.

```text
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
SYNTHESIS_STOP_RULE_SATISFIED=YES
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
```