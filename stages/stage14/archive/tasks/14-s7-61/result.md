# Stage14-s7-61 — single-prime two-square influence residue support

## Status

`COMPLETE_SINGLE_PRIME_TWO_SQUARE_INFLUENCE_RESIDUE_SUPPORT_BOUNDARY`

Consumes merged `Stage14-s7-60`, merged `Stage14-4dr` when available as canonical localization, merged `Stage14-4dq`, and latest main. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-s7-60 reduced any square-root-saturating zero-mode arithmetic uplift to an exponent-zero conditional influence from one active split-prime allocation bit `ell`. This stage writes the local arithmetic transition explicitly and audits whether influence forces `ell` into a thin residue family.

## 1. Two allocation states

Freeze one full-conductor interior-dense six-block packet and all allocation data except one odd split prime `ell` that may be assigned to either side of one balanced cofactor split. After absorbing the fixed state into coprime positive integers `x,y`, the two local states may be written, up to the already-frozen side convention, as

```text
state + : (X_+,Y_+)=(ell*x, y),
state - : (X_-,Y_-)=(x, ell*y),
```

with

```text
gcd(ell,2xy)=1.
```

Physical complementary-square admissibility is

```text
Q(X,Y)
 = 1_{(X+Y)/2 is a square}
   1_{(X-Y)/2 is a square},
```

with positivity/range/chart/orientation masks retained outside this arithmetic test.

The single-prime influence event is the symmetric difference

```text
Q(ell*x,y) XOR Q(x,ell*y).
```

## 2. Exact square equations

If the `+` state is admissible there exist integers `D_+,A_+` such that

```text
ell*x + y = 2 D_+^2,
ell*x - y = 2 A_+^2.
```

Hence

```text
ell*x = D_+^2 + A_+^2,
y     = D_+^2 - A_+^2.
```

If the `-` state is admissible there exist integers `D_-,A_-` such that

```text
x + ell*y = 2 D_-^2,
x - ell*y = 2 A_-^2,
```

hence

```text
x       = D_-^2 + A_-^2,
ell*y   = D_-^2 - A_-^2.
```

These are exact, not heuristic, and retain the complementary-square structure used throughout the reactivated s route.

## 3. Local congruence consequences at ell

Because `ell` is coprime to `x,y`, admissibility of the `+` state gives

```text
D_+^2 + A_+^2 == 0 (mod ell),
```

so on units

```text
(D_+ A_+^{-1})^2 == -1 (mod ell).
```

Therefore a generic odd influential split prime must satisfy

```text
-1 is a quadratic residue mod ell,
```

hence

```text
ell == 1 (mod 4)
```

apart from already-frozen exceptional/2-primary support.

Likewise the minus-state difference equation yields a real-square ratio condition on the corresponding local factors. These conditions are consistent with the existing mixed fourth-root / Gaussian split-prime packet; they do not create a new independent congruence support.

```text
INFLUENTIAL_SPLIT_PRIME_REQUIRES_GAUSSIAN_SPLITTING=true
INFLUENTIAL_SPLIT_PRIME_MOD4_SUPPORT=1
```

## 4. Why this is not thin enough

The condition

```text
ell == 1 (mod 4)
```

has positive prime density. More generally, fixing one square-root orientation modulo `ell` gives only `O(1)` local root choices for each already-eligible split prime; it does not force `ell` into a residue class modulo a growing external modulus.

The exact local equations above therefore recover the already charged Gaussian split-prime condition, but no fresh factor `ell^{-1}`, no fixed-power density loss, and no growing-modulus residue sparsity.

```text
FRESH_THIN_RESIDUE_SUPPORT_PROVED=false
LOCAL_CONGRUENCE_ONLY_REPRODUCES_EXISTING_SPLIT_PRIME_SUPPORT=true
SINGLE_PRIME_CONGRUENCE_DOUBLE_CHARGE_ALLOWED=false
```

## 5. Simultaneous two-state admissibility is stronger, but not the influence event

If both allocation states were admissible simultaneously, then four square equations would hold. Subtracting the state equations gives identities coupling the two square pairs and `ell`. This is a genuine higher-energy condition.

However single-prime influence is an XOR event: exactly one state may be physically admissible. Therefore a theorem about simultaneous admissibility cannot be charged against the full influence receiver without first proving that exponent-zero influence forces a positive-density simultaneous or collision subfamily.

```text
BOTH_STATES_ADMISSIBLE_IS_STRONGER_THAN_INFLUENCE=true
SIMULTANEOUS_STATE_ENERGY_NOT_YET_CHARGEABLE=true
```

## 6. New minimal receiver

The residue test is exhausted internally. The surviving arithmetic problem is not that influential primes lie in an unknown thin residue class. It is the frequency with which toggling one already-Gaussian split prime crosses the physical two-square admissibility boundary while all side masks are retained.

Thus the next receiver is

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
SingleGaussianSplitPrimeTwoSquareBoundaryCrossingInfluence.
```

Equivalently, after freezing the outer packet, estimate the conditional edge boundary of the Boolean two-square admissibility function on one prime-allocation bit.

## 7. H decision

No new auxiliary H is opened at s7-61.

Reason: the local congruence calculation has just shown that ordinary residue sparsity cannot give a new fixed-power saving. Before an external theorem audit, the s route should test the next internal possibility: whether exponent-zero XOR influence forces either (i) a short arithmetic boundary interval for `ell`, (ii) a two-state collision/energy packet, or (iii) a low-degree boundary equation in the frozen cofactor coordinates.

```text
S7_61_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_61=COMPLETE_SINGLE_PRIME_TWO_SQUARE_INFLUENCE_RESIDUE_SUPPORT_BOUNDARY
SINGLE_PRIME_TWO_STATE_EQUATIONS_EXPLICIT=true
INFLUENTIAL_SPLIT_PRIME_REQUIRES_GAUSSIAN_SPLITTING=true
INFLUENTIAL_SPLIT_PRIME_MOD4_SUPPORT=1
FRESH_THIN_RESIDUE_SUPPORT_PROVED=false
LOCAL_CONGRUENCE_ONLY_REPRODUCES_EXISTING_SPLIT_PRIME_SUPPORT=true
SINGLE_PRIME_CONGRUENCE_DOUBLE_CHARGE_ALLOWED=false
BOTH_STATES_ADMISSIBLE_IS_STRONGER_THAN_INFLUENCE=true
SIMULTANEOUS_STATE_ENERGY_NOT_YET_CHARGEABLE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_61_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanSingleGaussianSplitPrimeTwoSquareBoundaryCrossingInfluence
NEXT=Stage14-s7-62
```