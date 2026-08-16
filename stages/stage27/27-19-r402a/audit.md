# Stage27-19-r402a — hostile audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R402A_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Scope

Fresh hostile intermediate audit of PR #1038 / Stage27-19-r402a. This audit does not close Stage27 checkpoint40 and does not advance to checkpoint50.

## 1. Physical slope-height bounds

Accepted.

For reduced positive slope pairs `gcd(m,n)=gcd(r,s)=1`, with

```text
E=4mnrs
X=2rs(m^2-n^2)
Y=2mn(r^2-s^2)
G=gcd(E,X,Y)
```

one has

```text
gcd(2mn,m^2-n^2)<=2
```

and therefore

```text
G<=4rs,
G<=4mn.
```

The exact integral face diagonals are

```text
F_X=2rs(m^2+n^2)/G,
F_Y=2mn(r^2+s^2)/G.
```

Hence

```text
F_X >= (m^2+n^2)/2,
F_Y >= (r^2+s^2)/2.
```

Because each face diagonal is strictly smaller than the positive geometric space diagonal `R`, the exact physical cutoff `R<=B` gives

```text
m^2+n^2 < 2B,
r^2+s^2 < 2B,
n^2 < B,
s^2 < B.
```

The primitive scale `G` is retained throughout; no raw toric parameter height is falsely identified with physical height.

```text
REDUCED_SLOPE_PAIR_HEIGHT_BOUND_ACCEPTED=true
M2_PLUS_N2_LT_2B_ACCEPTED=true
R2_PLUS_S2_LT_2B_ACCEPTED=true
N2_LT_B_ACCEPTED=true
S2_LT_B_ACCEPTED=true
```

## 2. Reduced tau height

Accepted.

For

```text
N0=s^2(m^2+n^2),
D0=n^2(r^2-s^2),
tau=(N0/g_tau)/(D0/g_tau),
g_tau=gcd(N0,D0),
```

the previous bounds imply

```text
0<N0<2B^2,
0<D0<2B^2.
```

Reduction can only decrease numerator and denominator, so for the standard rational height

```text
H(tau)=max(p,q)
```

one obtains the same-measure theorem

```text
H(tau)<2B^2.
```

```text
TAU_REDUCED_HEIGHT_BOUND_ACCEPTED=true
TAU_REDUCED_HEIGHT_BOUND=H(tau)<2B^2
TAU_HEIGHT_PHYSICAL_CUTOFF_MATCH=true
```

## 3. Support preflight and negative route certificate

Accepted with the stated scope.

The rational-height box gives only `O(B^4)` possible positive reduced rationals. Counting the two reduced slope pairs under the proved disk bounds gives only `O(B^2)` ambient toric inputs. Both are weaker than the inherited survivor support bound

```text
#T(B) <= N2(B) <<_epsilon B^(1/2+epsilon).
```

Combined with the hostile-audited r402 lower support bound, the certified corridor is therefore

```text
B^(1/4) << #T(B) <<_epsilon B^(1/2+epsilon).
```

No strict support exponent `sigma<1/2` follows from the current reduced-height theorem plus raw cardinality alone.

The marker

```text
HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true
```

is accepted only in that narrow sense. It is not an impossibility theorem for arithmetic sparsity of the realized survivor tau set.

```text
TAU_RATIONAL_HEIGHT_COUNT_EXPONENT_ACCEPTED=4
TAU_AMBIENT_TORIC_COUNT_EXPONENT_ACCEPTED=2
TAU_BEST_CERTIFIED_SUPPORT_UPPER=1/2_PLUS_EPSILON
TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
TAU_SUPPORT_EXPONENT_IDENTIFIED=false
HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED_ACCEPTED=true
```

## 4. Consequence for upper attack

r402a does not improve the global upper theorem. The current theorem remains

```text
N2(B) <<_epsilon B^(1/2+epsilon).
```

The next useful route is correctly shifted to actual fixed-tau fiber / same-measure anti-concentration or collision-energy control, rather than further raw label counting.

```text
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r402b
```

## 5. CI / lifecycle note

The dedicated `Stage27-19-r402a tau height support preflight` workflow is SUCCESS on submission head `d72bc15ef70348eb33f3804b729c2c714aa14036`.

The parent `Stage27-19-r402 tau pushforward upper reentry` regression is red only because its historical verifier still asserts that r402 itself has status `SUBMITTED_PENDING_FRESH_AUDIT`. r402a correctly synchronizes r402 as hostile-audited PASS + merged PR #1037 / merge `77dc7bc7eb29f4113d59c8255ab4b2148bd52690`. This is successor-lifecycle verifier debt, not a mathematical contradiction and not a blocker for r402a.

Older r401-series red regressions are the same class of historical successor-state debt. They should be repaired as maintenance but are not used to reject this fresh route.

```text
R402A_DEDICATED_CI=SUCCESS
R402_PARENT_RED_IS_SUCCESSOR_LIFECYCLE_DEBT=true
HISTORICAL_R401_RED_IS_SUCCESSOR_LIFECYCLE_DEBT=true
CI_BLOCKS_R402A=false
```

## Final verdict

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
STAGE27_19_R402A_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
REDUCED_SLOPE_PAIR_HEIGHT_BOUND_ACCEPTED=true
TAU_REDUCED_HEIGHT_BOUND_ACCEPTED=true
HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED_ACCEPTED=true
TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
NEXT_DERIVED_ROUTE=27-19-r402b
MERGE_ALLOWED=true
```
