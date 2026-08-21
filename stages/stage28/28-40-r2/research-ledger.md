# Stage28-40-r2 research ledger — U10 through U14

```text
TASK_ID=Stage28-40-r2
CHECKPOINT=40
MODE=POSTMERGE_DEEPENING
PRIOR_MERGED_BATCH=PR1276_U1_U9
NUMERIC_BRIDGE_UPPER_IMPROVED=false
```

## U10 — exact branch-component profile

Result: **new structural separation**.

Over `Qbar`, the Stage19 space branch decomposes into four irreducible rational `(1,1)` components, while the Stage20 third-face branch decomposes into two irreducible genus-one anticanonical components.

```text
SPACE_BRANCH_PROFILE=4x_genus0
THIRD_FACE_BRANCH_PROFILE=2x_genus1
SAME_TOTAL_CLASS=-2K_Y
BASE_AUTOMORPHISM_IDENTIFICATION=false
```

This identifies a global geometric difference invisible to the old total-class/K3-type comparison.  No counting inequality follows automatically.

## U11 — exact relative local Euler product

Result: **first-order cancellation sharpened to a finite local constant**.

The exact good-prime acceptance quotient satisfies

\[
\alpha_p/\beta_p=(1-\chi_4(p)/p)^2(1+O(p^{-2})).
\]

After extracting the Dirichlet `L(1,chi_4)^{-2}` factor and a fixed bad-prime correction, the remaining Euler product converges absolutely.

```text
RELATIVE_LOCAL_EULER_CONSTANT_EXISTS=true
POLYNOMIAL_LOCAL_DRIFT=0
FIRST_ORDER_LOG_LOCAL_DRIFT=0
GLOBAL_RATIO_CONSTANT_PROVED=false
```

A prime truncation through `10^6` gives a diagnostic relative product near `2.1123`; this is not promoted to a theorem about `M3/N2`.

## U12 — explicit Huang thin-cover transfer to the space cover

Result: **new matched theorem species**.

Huang v3, proof of Theorem 1.6(1), gives for the common base `r=6`, `dim=2`

\[
B(\log B)^5/N^{1-\varepsilon}
+N^{22+\varepsilon}B(\log B)^{9/2+\varepsilon}.
\]

Balancing with `N=(log B)^lambda` at the endpoint-free value near `lambda=1/46` yields for every fixed `eta<1/46`

\[
N_2(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Stage20 already has exactly the same explicit range from Stage14-e11 / PR #188.

```text
SPACE_THIN_COVER_ETA_RANGE=eta<1/46
THIRD_FACE_THIN_COVER_ETA_RANGE=eta<1/46
EXPLICIT_THIN_COVER_RANGE_MATCH=true
```

The stronger Stage19 half-power theorem remains the numerical upper champion.

## U13 — quadratic squareclass separation

Result: **new base-preserving non-equivalence**.

The quotient

\[
(1+t_1^2+t_2^2)/(t_1^2+t_2^2)
\]

is not a square in `Qbar(Y)^*`, because its branch divisor has odd valuation on components appearing in only one of the two branch supports.  Hence the two quadratic function-field extensions are distinct.

```text
SAME_QUADRATIC_EXTENSION_OVER_Y=false
BASE_PRESERVING_BIRATIONAL_EQUIVALENCE=false
ABSTRACT_K3_NONISOMORPHISM_PROVED=false
```

So the bridge cannot collapse by a hidden square rescaling or an automorphism of the common host.

## U14 — Kummer/accumulation literature rematch

Result: **negative transfer certificate**.

Merged Stage14-4ah / PR #164 identifies the Stage19 space surface over `C` as the Kummer surface `Km(E_i x E_i)` and locks the exact physical line bundle

\[
M=\pi^*(-K_Y),\qquad H_M=R,
\]

with `M` big and nef but not ample because of nonphysical null boundary curves.

McKinnon's bounded-height K3/Kummer counting theorem (`Counting Rational Points on K3 Surfaces`, JNT 84 (2000), arXiv:math/9903013) assumes an **ample** divisor/height.  Its accumulating-curve mechanism is relevant structural guidance, but the theorem cannot be imported directly to the exact Stage19 physical height.  This is already consistent with the merged Stage14-4ah firewall and the r2 branch decomposition does not remove that hypothesis mismatch.

```text
MCKINNON_DIRECT_PHYSICAL_HEIGHT_TRANSFER=false
AMPLENESS_ADAPTER_FOUND=false
NEW_N2_COUNT_FROM_KUMMER_LITERATURE=false
```

## Exhaustion verdict for checkpoint40 r2

After U1-U14, the following coarse/marginal comparison layers have been tested:

- independent endpoint bounds;
- exact finite data;
- first-order local sieve dimension;
- growing-prime local sieve;
- exact relative local Euler product;
- common base/degree/total branch class/K3 type;
- exact branch component genera and squareclasses;
- explicit Huang thin-cover exponent range;
- Kummer bounded-height transfer;
- same-host correlation/energy and endpoint-circularity firewalls;
- full StructureRadar rematch.

No remaining repo-native identity or already-classified theorem produces a strict improvement of

\[
M_3/N_2=o(B^{3/4}(\log B)^{5-\delta}).
\]

The remaining upper-side theorem receiver is now narrower than the PR #1276 receiver:

```text
OPEN_GATE_40_R2=DistinctBranchProfileDoubleCoverMarginalComparison
POPULATION=Stage19_N2_vs_Stage20_M3
COMMON_BASE=Y=Bl_4(P1xP1)
CUTOFF=physical_R<=B
SPACE_BRANCH_PROFILE=4_rational_components
THIRD_FACE_BRANCH_PROFILE=2_genus1_components
REQUIRED_OUTPUT=strict_bridge_upper_improvement_or_asymptotic_ordering
FORBIDDEN_INPUT=perfect_cuboid_endpoint_count_or_asymptotic
ACCEPTABLE_SPECIES=physical_height_rational_lift_comparison|cover_specific_dispersion|marginal_energy_without_joint_endpoint|uniform_accumulating_subvariety_count
```

This gate requires genuinely new global arithmetic input.  Repeating local-density, total branch-class, fixed-curve, or generic thin-cover arguments is no longer a materially new route.
