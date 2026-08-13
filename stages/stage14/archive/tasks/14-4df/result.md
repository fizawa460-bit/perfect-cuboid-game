# Stage14-4df — consume s7-47 and expose the six-block complementary-square correlation

## Status

`COMPLETE_S7_47_MAINLINE_CONSUMPTION_SIX_BLOCK_PAIRWISE_SEPARATION_AND_SQUARE_RECONSTRUCTION`

Stage14-4df consumes merged `Stage14-s7-47`, merged `Stage14-s7-46`, and merged `Stage14-4de` as theorem inputs.  This rebased integration branch is based on latest main after later `s7-48 / sH48` progress; those later stages are preserved and are not reverted or rewritten here.

The entering canonical theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here.  The purpose is to import the s7-47 overlap theorem into the mainline without double charging it, and to record the resulting atomic six-block form of the remaining square-root obstruction.

## 1. Imported s7-47 theorem — no duplicate overlap saving

Merged s7-47 defines

```text
M_+ = oddpart(D^2+A^2)/C_*,
M_- = oddpart(D^2-A^2)/u_*,
W_+ = gcd(C_*,M_+),
W_- = gcd(u_*,M_-).
```

It proves the effective-modulus lift

```text
Q_eff=Q_mix*W_+*W_-
```

and, on fixed-power overlap strata,

```text
E<=1/2-w_+-w_-.
```

Hence every possible square-root-saturating sequence satisfies

```text
gcd(C_*,M_+)=B^o(1),
gcd(u_*,M_-)=B^o(1).
```

Combined with merged 4de plus/minus cross-coprimality, s7-47 proves

```text
C_*, M_+, u_*, M_-
```

pairwise separated at fixed-power scale.

Stage14-4df imports this theorem once:

```text
MERGED_S7_47_IMPORTED=true
S7_47_OVERLAP_THEOREM_REPROVED_BY_4DF=false
S7_47_AND_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false
```

## 2. Expand four-block separation to six atomic blocks

Merged s7-46 reconstructs

```text
M_+=S*T*B^o(1),
M_-=R*J*B^o(1),
```

with `R,S,T,J` pairwise coprime and squarefree in the physical packet.

After fixing the frozen endpoint/2-primary support decoration, every prime divisor of `S,T` belongs to `M_+`, and every prime divisor of `R,J` belongs to `M_-`.  Therefore the s7-47 four-block separation plus the s7-46 cellwise coprimality imply that

```text
boxed:
C_*, S, T, u_*, R, J
```

are pairwise separated at fixed-power scale.

```text
SIX_ATOMIC_NORM_BLOCKS_PAIRWISE_SEPARATED=true
```

This is a structural refinement of the receiver, not a fresh independent modulus saving.

## 3. Six-block products reconstruct the two physical squares

Merged s7-47 retains the coupled complementary-square system, in the common odd/fixed-power normalization,

```text
C_* S T = D^2+A^2,
u_* R J = D^2-A^2,
```

up to the frozen `B^o(1)` endpoint/2-primary decorations.

Condition on those decorations and define

```text
X_+ := C_* S T,
X_- := u_* R J.
```

Then

```text
boxed:
D^2=(X_++X_-)/2,

boxed:
A^2=(X_+-X_-)/2.
```

Thus a fixed six-block packet fixes the candidate squares.  Positivity/integrality require

```text
X_+>X_->0,
X_++X_- is twice a square,
X_+-X_- is twice a square.
```

If those selectors pass, `D>A>0` fixes `(D,A)` uniquely. Restoring the frozen endpoint/2-primary decoration contributes only `B^o(1)` possibilities. Hence

```text
fixed (C_*,S,T,u_*,R,J)
=> #(D,A)=B^o(1).
```

Equivalently,

```text
D_A_INDEPENDENT_FIXED_POWER_SUPPORT_AFTER_SIX_BLOCKS=false
SIX_BLOCK_PACKET_TO_BALANCED_PAIR_MULTIPLICITY=Bo1
```

## 4. Mixed-root datum is a consistency selector after six blocks

Once the six blocks and normalized `(D,A)` are fixed,

```text
Q_mix=C_*u_*.
```

If `gcd(A,Q_mix)=1`, the root label is forced by

```text
t == D*A^(-1) (mod Q_mix).
```

The required root types

```text
t^2=-1 mod C_*,
t^2=+1 mod u_*
```

are then consistency tests, not new polynomial support.

```text
MIXED_ROOT_LABEL_INDEPENDENT_SUPPORT_AFTER_SIX_BLOCKS=false
```

The reverse six-block view and the forward mixed-root determinant ledger describe the same physical mass and must not be multiplied.

## 5. Remaining mainline receiver

The following mechanisms are exhausted on a possible square-root equality packet:

```text
fixed-power same-sign overlap,
plus/minus cross gcd,
second reciprocal multiplicity,
xi-cell split multiplicity,
D/A multiplicity after six atomic blocks,
mixed-root label multiplicity after six atomic blocks.
```

The remaining obstruction is the density of pairwise-separated six-block packets satisfying both complementary-square conditions simultaneously, with all inherited physical interval/orientation/state masks retained.

The mainline receiver is

```text
SquareRootQuarterScaleSixBlockPairwiseSeparatedMixedFourthRootDualBalancedComplementarySquareCorrelationPhysicalDensity
```

Mandatory structure:

```text
C_*,S,T,u_*,R,J pairwise separated at fixed-power scale,
S,T,R,J squarefree at inherited physical scales,
C_*u_*=B^(1/4+o(1)),
C_*ST = D^2+A^2,
u_*RJ = D^2-A^2,
D,A=B^(1/4+o(1)), D>A>0,
all 4de/s7-46/s7-47 physical masks retained.
```

No deterministic count in the 4df source snapshot proves a fixed positive density loss on this zero-overlap six-block correlation.

## 6. Whole-family ledger

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 7. s-route lifecycle ownership

At the 4df theorem-source snapshot, merged s7-46/s7-47 had already reactivated the s route. Therefore 4df itself makes no yes/no reactivation judgment:

```text
S_ROUTE_REACTIVATION_DECISION_REQUIRED_AT_4DF_SOURCE=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED_AT_4DF_SOURCE=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true
```

The source-snapshot next stage was `Stage14-s7-48`, but later s work has already merged on current main.  Current route state is intentionally **not** frozen by this historical stage file:

```text
S_ROUTE_LIFECYCLE_OWNED_BY_CURRENT_ROADMAP=true
CURRENT_S_ROUTE_STATE_NOT_OVERWRITTEN_BY_4DF=true
LATER_MERGED_S7_48_SH48_PRESERVED=true
```

This rebased PR deliberately does not modify `stages/stage14/roadmap.md`.

## 8. H / fixed-U boundary

At the 4df source boundary the exact six-block complementary-square system had not yet been exhausted internally, so no new mainline H was requested:

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
```

Merged t86/tH24 remain fixed-`U` coefficient-space results with no charged-once adapter to this mainline receiver:

```text
T86_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false
```

## 9. Next mainline stage

```text
NEXT=Stage14-4dg
```

Later merged s-route work may further refine the receiver and should be consumed by `4dg` from the actual latest main rather than retroactively changing 4df.

## Stage boundary

```text
STAGE14_4DF=COMPLETE_S7_47_MAINLINE_CONSUMPTION_SIX_BLOCK_PAIRWISE_SEPARATION_AND_SQUARE_RECONSTRUCTION
SOURCE_THEOREM_SNAPSHOT=Stage14-s7-47
MERGED_4DE_IMPORTED=true
MERGED_S7_46_IMPORTED=true
MERGED_S7_47_IMPORTED=true
S7_47_OVERLAP_THEOREM_REPROVED_BY_4DF=false
S7_47_AND_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false
SIX_ATOMIC_NORM_BLOCKS_PAIRWISE_SEPARATED=true
SIX_BLOCK_PACKET_TO_BALANCED_PAIR_MULTIPLICITY=Bo1
D_A_INDEPENDENT_FIXED_POWER_SUPPORT_AFTER_SIX_BLOCKS=false
MIXED_ROOT_LABEL_INDEPENDENT_SUPPORT_AFTER_SIX_BLOCKS=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
REMAINING_RECEIVER=SquareRootQuarterScaleSixBlockPairwiseSeparatedMixedFourthRootDualBalancedComplementarySquareCorrelationPhysicalDensity
S_ROUTE_REACTIVATION_DECISION_REQUIRED_AT_4DF_SOURCE=false
S_ROUTE_REACTIVATION_CHECK_SUSPENDED_AT_4DF_SOURCE=true
S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true
S_ROUTE_LIFECYCLE_OWNED_BY_CURRENT_ROADMAP=true
CURRENT_S_ROUTE_STATE_NOT_OVERWRITTEN_BY_4DF=true
LATER_MERGED_S7_48_SH48_PRESERVED=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
T86_CROSS_PROMOTED_TO_MAINLINE=false
TH24_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dg
```