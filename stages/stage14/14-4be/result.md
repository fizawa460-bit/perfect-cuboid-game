# Stage14-4be — instantiate the first explicit local retainer from the closed full local system

## Result

Stage14-4bd closed the complete nonconstant reciprocal analysis and froze the conservative Euclid-scale saving

```text
E_rec(M) << M^(2-1/200+o(1)).
```

Merged Stage14-s5s then supplied the logically stronger statement needed for the physical upper bound: the **actual complete locally-soluble descent-class count**, including its constant and nonconstant Fourier modes together, satisfies on regular Euclid boxes

```text
N_loc(Omega_M) <<_epsilon M^(2-1/200+epsilon),
```

and cumulatively under `H=m^2+n^2<=B`

```text
N_loc(B) <<_epsilon B^(399/400+epsilon).
```

The purpose of Stage14-4be is to insert this theorem into the 14-4as retainer language without confusing the earlier constant-mode decomposition with the now-available full-system estimate.

The main conclusion is:

```text
UNWEIGHTED cumulative specialization W=1:

S(B) <= rho_loc(B) A(B) + E_loc(B),

rho_loc(B) <<_epsilon B^(-1/400+epsilon),
E_loc(B) = 0.
```

Thus the main track obtains its first explicit positive local retainer exponent

```text
delta_loc = 1/400
```

on the physical `B` scale.

This does **not** assert that the old constant Fourier mode `D_loc` is zero or separately power-saving. The point is that the full local polynomial is now controlled before taking absolute values mode-by-mode, so the old `D_loc + sum |B_omega|` decomposition is no longer the sharp route for the unweighted upper bound.

---

## 1. Ambient base denominator

Let

```text
A(B)=#{primitive oriented Pythagorean first-face bases F=(S,X,H): H<=B}.
```

Merged Stage14-4al proved

```text
A(B)=B/pi+O(sqrt(B) log B).
```

Hence there are constants `B_0,c_A,C_A>0` such that for `B>=B_0`,

```text
c_A B <= A(B) <= C_A B.
```

Only the lower bound is needed below.

---

## 2. Full local system majorizes the base Selmer/local gate

For a base `F`, let `s(F)` be the nontrivial local/Selmer-gate indicator used in the 14-4 chain, and put

```text
S(B)=sum_{H(F)<=B} s(F).
```

Stage14-4au established the pointwise nonnegative support-count domination

```text
s(F) <= N_loc(F),
```

where `N_loc(F)` counts locally admissible nontrivial descent states/classes over the base.

Therefore

```text
S(B) <= N_loc(B):=sum_{H(F)<=B} N_loc(F).
```

Merged s5r closes the actual finite local character polynomial, and merged s5s converts its regular-box estimate to the cumulative physical scale:

```text
N_loc(B) <<_epsilon B^(399/400+epsilon).
```

No global-solubility or Sha converse is needed for this upper bound.

---

## 3. Direct retainer instantiation

Combine

```text
S(B) <= N_loc(B) <<_epsilon B^(399/400+epsilon)
```

with

```text
A(B) >= c_A B
```

for large `B`. Then

```text
S(B)/A(B)
 <<_epsilon
 B^(-1/400+epsilon).
```

Equivalently, for the unweighted cumulative family,

```text
S(B)
 <= rho_loc(B) A(B) + E_loc(B)
```

with the valid choice

```text
rho_loc(B)=C_epsilon B^(-1/400+epsilon),
E_loc(B)=0.
```

For finitely many small `B`, enlarge `C_epsilon` if necessary. Thus this is a uniform asymptotic retainer statement rather than a finite-data fit.

The exponent conversion is exact:

```text
Euclid parameter scale: M^(-1/200)
physical H/B scale:     B^(-1/400),
```

because `B~M^2` on the dominant regular boxes.

---

## 4. Why `E_loc=0` is legitimate here

The 14-4as inequality only asks for any deterministic pair satisfying

```text
S <= rho_loc A + E_loc.
```

Once a direct full-system bound proves

```text
S <= C B^(399/400+epsilon)
```

and `A>>B`, the entire local contribution may be placed in the multiplicative retainer. No additive error is required.

Therefore

```text
E_loc=0
```

is a valid choice for this **unweighted cumulative specialization**.

It is not a statement that the reciprocal error from 4bd vanishes. Rather, 4bd and s5r are ingredients in the theorem proving the full-system bound; after that theorem is available, their internal error decomposition need not be retained in the outer 4as interface.

---

## 5. Why this does not prove `D_loc=0`

Stage14-4au wrote the support-count Fourier expansion as

```text
N_loc = D_loc + sum_{omega!=0} B_omega.
```

For an early upper bound it used

```text
N_loc <= D_loc + sum |B_omega|.
```

That absolute-value step deliberately destroyed cancellation between the constant mode and nonconstant modes and therefore required a separate estimate of `D_loc`.

The later s5r theorem does not proceed by this lossy final triangle inequality. It controls the **actual complete local polynomial**. Consequently a power-saving bound for `N_loc` does not imply that `D_loc` itself has the same power saving.

Accordingly Stage14-4be records

```text
D_LOC_SEPARATE_POWER_SAVING_PROVED=false.
```

But the separate diagonal estimate is no longer required for the present unweighted upper bound:

```text
D_LOC_SPLIT_REQUIRED_FOR_CURRENT_UNWEIGHTED_UPPER_BOUND=false.
```

If a future argument needs arbitrary external nonnegative weights for which the full s5r cancellation is unavailable, the old `D_loc` interface may become relevant again.

---

## 6. Scope: unweighted cumulative family, not arbitrary weights

The proved retainer is instantiated for the physical/unweighted family

```text
W(F)=1,
H(F)<=B.
```

This is sufficient for the current physical upper bound because 14-4as explicitly allows the unweighted specialization for transfer to the physical count.

Stage14-4be does **not** claim the same

```text
rho_loc << B^(-1/400)
```

uniformly for every adversarial nonnegative weight `W_Q(F)`. Such a weighted theorem would require the full s5r local-system cancellation to be stable under that external weight, which has not been proved.

Thus

```text
ARBITRARY_WEIGHT_LOCAL_RETAINER_PROVED=false.
```

This scope distinction prevents the new local theorem from being silently promoted to the stronger s5g arbitrary-coefficient family large-sieve candidate.

---

## 7. Updated 14-4as ledger

For the unweighted cumulative family, 14-4as may now use

```text
rho_loc(B) << B^(-1/400+epsilon),
E_loc(B)=0.
```

If future global and height retainers satisfy

```text
rho_glob << B^(-delta_glob+o(1)),
rho_ht   << B^(-delta_ht+o(1)),
```

then the 14-4as main term becomes

```text
B^(1-1/400-delta_glob-delta_ht+o(1)).
```

Because `E_loc=0`, the propagated local-error term

```text
rho_ht rho_glob E_loc
```

vanishes identically in this specialization.

To reach a square-root main-term exponent through the three-retainer architecture one would still need

```text
delta_glob + delta_ht >= 199/400.
```

The global and height additive errors must separately satisfy the 14-4as propagated-error budget. No such global or height exponents are proved here.

---

## 8. Relation to the direct s5s physical upper bound

There are now two consistent descriptions of the same theorem-level progress.

### Direct one-sided route

Merged s5s gives immediately

```text
V(B) <= #L_B << B^(399/400+epsilon).
```

This route bypasses the global/Sha and small-point distribution gates because physical hits inject into locally soluble classes.

### Three-retainer route

Stage14-4be expresses the same local saving as

```text
delta_loc=1/400,
E_loc=0
```

inside the older 14-4as architecture. This is useful if later work obtains additional global or height thinning and wants to multiply it onto the already-proved local retainer.

The two descriptions are complementary; neither changes the theorem boundary.

---

## 9. What is now closed and what remains

Closed:

```text
actual complete local character polynomial average,
root-sawtooth transition,
positive local family saving,
physical-height insertion for a one-sided upper bound,
unweighted cumulative local retainer instantiation,
local additive error in that specialization.
```

Still open:

```text
arbitrary externally weighted local retainer,
separate D_loc asymptotic/density if ever needed,
positive global/Sha thinning exponent,
positive conditional small-point/height thinning exponent,
sqrt(B) upper bound or asymptotic.
```

The direct physical theorem already gives

```text
V(B) << B^(399/400+epsilon),
```

but the observed `B^(1/2)` scale remains far away.

---

## Boundary

```text
STAGE14_4BE=UNWEIGHTED_FULL_LOCAL_RETAINER_INSTANTIATED
S5R_S5S_FULL_LOCAL_SYSTEM_BOUND_IMPORTED=true
STAGE14_4AL_BASE_ASYMPTOTIC_IMPORTED=true
BASE_COUNT_ASYMPTOTIC=A(B)=B/pi+O(sqrt(B)logB)
UNWEIGHTED_CUMULATIVE_LOCAL_RETAINER_PROVED=true
UNWEIGHTED_RHO_LOC_B_EXPONENT=1/400
UNWEIGHTED_E_LOC=0
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=true
EXPLICIT_COMPLETE_E_LOC_PROVED=true
LOCAL_DELTA_IN_4AS_B_SCALE=1/400
LOCAL_ERROR_ZERO_IN_UNWEIGHTED_SPECIALIZATION=true
D_LOC_SEPARATE_POWER_SAVING_PROVED=false
D_LOC_SPLIT_REQUIRED_FOR_CURRENT_UNWEIGHTED_UPPER_BOUND=false
ARBITRARY_WEIGHT_LOCAL_RETAINER_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED=true
ACTIVE_PHYSICAL_BASE_UPPER_BOUND=B^(399/400+epsilon)
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
SQRT_MAIN_TERM_REQUIRES_DELTA_GLOB_PLUS_DELTA_HT_GE_199/400=true
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bf stress-test the 1/400 physical-scale local exponent against Stage14-s5t, decide whether the local bottleneck should be optimized further or frozen, and then refocus the main-track ledger on the remaining global/height thinning needed beyond the direct B^(399/400+epsilon) bound
```
