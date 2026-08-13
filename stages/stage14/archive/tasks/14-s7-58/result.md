# Stage14-s7-58 — arithmetic factorization test for positive zero-mode conditional uplift

## Status

`COMPLETE_ORIENTATION_HEECKE_PARTIAL_FACTOR_AND_NONMULTIPLICATIVE_MASK_BARRIER`

Consumes merged `s7-57`, merged `4dn`, merged `4dm`, merged `Stage14-AM`, and current latest main.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged 4dn reduces the positive zero-mode pairwise branch to the conditional uplift

```text
Uplift_{+|-}
 := [ E(W_- | A_+=1) - E(W_- | A_+=0) ]^+.
```

Stage14-s7-58 tests whether this statistic admits the multiplicative / Gaussian-Hecke factorization suggested by q11 and audited globally in Stage14-AM.

## 1. Physical mask decomposition

Write the plus cofactor selector schematically as

```text
A_+
 = O_+ * P_+ * G_+ * R_+ * B_+ * Q_+,
```

where

```text
O_+ : Gaussian/root orientation data,
P_+ : primitive / squarefree support,
G_+ : pairwise gcd/separation conditions,
R_+ : dyadic range/angular inequalities,
B_+ : balanced cofactor split conditions,
Q_+ : charged-once / reciprocal completion bookkeeping.
```

The minus selector has the analogous decomposition.

This is only a logical factorization of indicator conditions; it does not claim probabilistic independence.

## 2. Orientation component is Hecke/Walsh factorable

Merged Stage14-AM proves that for squarefree full-conductor support the prescribed Gaussian orientation projector admits an exact Walsh expansion

```text
O_+
 = 2^(-omega(C_*))
   sum_{S subset supp(C_*)} epsilon_S * chi_S,
```

where each `chi_S` is a Gaussian ideal-/Hecke-multiplicative phase on the coprime factor domain.

Hence

```text
number of orientation phases = 2^omega(C_*) = B^o(1),
coefficient l1 cost = 1.
```

Therefore the orientation component itself is not the fixed-power barrier.

```text
ZERO_MODE_ORIENTATION_HECKE_EXPANSION_PROVED=true
ZERO_MODE_ORIENTATION_PHASE_COUNT=Bo1
ZERO_MODE_ORIENTATION_L1_COST=1
```

## 3. Primitive projection alone is not the decisive obstruction

Primitivity can be written by Mobius inversion,

```text
1_{gcd(x_1,...,x_r)=1}
 = sum_{d | gcd(x_1,...,x_r)} mu(d).
```

On one fixed dyadic packet the divisor count is `B^o(1)`. Thus formal Mobius expansion of a fixed finite gcd condition is compatible with subpolynomial combinatorial complexity.

However this does not solve the physical selector transfer, because the expanded terms remain multiplied by the nonmultiplicative range/balance/charged-once masks below.

```text
FINITE_GCD_MOBIUS_EXPANSION_COMBINATORIAL_COST=Bo1
PRIMITIVITY_ALONE_IS_MINIMAL_BARRIER=false
```

## 4. Nonmultiplicative masks block a complete Hecke expansion

The following retained conditions are not multiplicative functions of the Gaussian/integer factor variable:

```text
1. dyadic and angular interval restrictions;
2. balanced two-cell factorization conditions such as S*T=M_+ with both factors in prescribed physical windows;
3. coupled separation constraints involving simultaneously C_*,u_*,M_+,M_-;
4. charged-once identification of the three Pythagorean pair charts;
5. reciprocal-completion masks whose admissibility depends jointly on several already-conditioned coordinates.
```

For example, the balanced-split indicator

```text
B_M(n)
 = 1_{exists d|n : d in I_1 and n/d in I_2}
```

is not multiplicative: even for coprime `n_1,n_2`, a balanced divisor of `n_1 n_2` may use prime factors from both inputs while neither `n_1` nor `n_2` has an admissible balanced divisor. Hence in general

```text
B_M(n_1 n_2) != B_M(n_1) B_M(n_2).
```

Likewise an interval indicator `1_{n in [X,2X]}` is nonmultiplicative.

Thus the exact `B^o(1)` orientation expansion cannot be promoted to an exact `B^o(1)` Hecke-phase expansion of the whole physical selector by multiplicativity alone.

```text
FULL_ZERO_MODE_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_PROVED=false
BALANCED_SPLIT_MASK_MULTIPLICATIVE=false
RANGE_MASK_MULTIPLICATIVE=false
CHARGED_ONCE_MASK_MULTIPLICATIVE=false
RECIPROCAL_COMPLETION_MASK_MULTIPLICATIVE=false
```

## 5. Consequence for conditional uplift

After expanding only the orientation component, the conditional uplift becomes a `B^o(1)` linear combination of terms of the form

```text
E( W_- | chi_S * N_+ = 1 )
 - E( W_- | N_+ = 0/other ),
```

where `N_+` still contains the nonmultiplicative physical masks from §4.

No theorem in merged AM converts these conditional physical densities into a uniform fixed-power deficit. The primitive `k=1` versus multiplicative-Folner mismatch also remains.

Therefore

```text
ORIENTATION_FACTORING_REMOVES_ZERO_MODE_BARRIER=false
CONDITIONAL_UPLIFT_FIXED_POWER_DEFICIT_PROVED=false
```

## 6. Minimal remaining internal adapter

The failed object is now smaller than the full AM selector transfer. One does not need a Hecke expansion of every Stage14 weight. For the zero-mode branch it suffices to control the sensitivity of the minus selector under toggling one plus cofactor mask.

Define the physical influence

```text
Inf(A_+ -> W_-)
 := E(W_- | A_+=1) - E(W_- | A_+=0).
```

The next internal target is:

```text
Physical Cofactor Influence Decomposition Lemma.

Decompose Inf(A_+ -> W_-) into
(a) Gaussian orientation influences, already B^o(1)-Hecke expandable,
(b) balanced/range/gcd/charged-once influences,
with no double charge, and determine whether every nonorientation influence
has fixed-power deficit or reduces to one explicit residual arithmetic receiver.
```

This is a deterministic sensitivity decomposition problem, not yet an external theorem problem.

## 7. H decision

No new H is opened.

The current obstruction is the exact decomposition of nonmultiplicative physical-mask influence. Stage14-AM already audited the relevant multiplicative literature and returned BLOCKED. Reopening an H before extracting the explicit residual influence receiver would duplicate that audit.

```text
S7_58_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
AM_REOPENED=false
```

## Boundary

```text
STAGE14_S7_58=COMPLETE_ORIENTATION_HEECKE_PARTIAL_FACTOR_AND_NONMULTIPLICATIVE_MASK_BARRIER
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MERGED_4DN_IMPORTED=true
MERGED_AM_IMPORTED=true
ZERO_MODE_ORIENTATION_HECKE_EXPANSION_PROVED=true
ZERO_MODE_ORIENTATION_PHASE_COUNT=Bo1
ZERO_MODE_ORIENTATION_L1_COST=1
FINITE_GCD_MOBIUS_EXPANSION_COMBINATORIAL_COST=Bo1
FULL_ZERO_MODE_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_PROVED=false
BALANCED_SPLIT_MASK_MULTIPLICATIVE=false
RANGE_MASK_MULTIPLICATIVE=false
CHARGED_ONCE_MASK_MULTIPLICATIVE=false
RECIPROCAL_COMPLETION_MASK_MULTIPLICATIVE=false
ORIENTATION_FACTORING_REMOVES_ZERO_MODE_BARRIER=false
CONDITIONAL_UPLIFT_FIXED_POWER_DEFICIT_PROVED=false
S7_58_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=PositiveConditionalPhysicalCofactorInfluenceWithNonmultiplicativeMasks
NEXT=Stage14-s7-59
```
