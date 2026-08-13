# Stage14-4df

Stage14-4df consumes merged `Stage14-s7-47` as a fixed source theorem snapshot and does **not** reprove or double-charge its overlap saving.

Merged s7-47 already proves that possible square-root saturation has the four blocks

```text
C_*, M_+, u_*, M_-
```

pairwise separated at fixed-power scale, with

```text
M_+=S*T,
M_-=R*J,
C_*S*T=D^2+A^2,
u_*R*J=D^2-A^2
```

in the frozen odd/fixed-power normalization.

Using merged s7-46 pairwise coprimality of `R,S,T,J`, 4df expands this to the six atomic blocks

```text
C_*, S, T, u_*, R, J
```

being pairwise separated at fixed-power scale.

For fixed frozen endpoint/2-primary decoration, define

```text
X_+=C_*S*T,
X_-=u_*R*J.
```

Then

```text
D^2=(X_++X_-)/2,
A^2=(X_+-X_-)/2.
```

Thus after the six-block packet is fixed, `(D,A)` has only `B^o(1)` completion multiplicity; the square/positivity tests and mixed-root label are selectors, not new polynomial support.

No new whole-family exponent is claimed:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Mainline receiver:

```text
SquareRootQuarterScaleSixBlockPairwiseSeparatedMixedFourthRootDualBalancedComplementarySquareCorrelationPhysicalDensity
```

The s route was already active at the 4df source snapshot, so 4df makes no reactivation decision. Current s-route lifecycle is owned by the latest roadmap; this rebased PR deliberately does not modify `roadmap.md` and does not revert later merged `s7-48 / sH48` progress.

No new mainline H is needed at the 4df source boundary. Next mainline stage: `Stage14-4dg`.