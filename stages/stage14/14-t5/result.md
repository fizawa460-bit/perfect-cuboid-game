# Stage14-t5 — root-pair triple bridge after 14-4aj

## Purpose

Reactivate the triple-correction track using the new `14-4aj` fixed-curve structure. The main track has reduced every surviving minimal physical `M`-degree-4 bisection to one component `C` of a split singular anticanonical pullback

```text
M = C + delta(C),
C^2 = delta(C)^2 = -2,
M.C = 4,
C.delta(C) = 6,
```

with the Stage14 Kummer deck involution

```text
delta(P) = (0,0) - P = tau_(0,0) o [-1].
```

This is enough to sharpen the triple restriction before the explicit Shimada root enumeration lands.

## Third-square cover restricted to a surviving root

The third-face square condition is the Stage14-t relative double cover with branch class `2M`. Therefore on any surviving rational root `C`,

```text
(2M).C = 8.
```

Let `B_C` be the branch divisor on the normalization `C ~= P1`. Write `b_odd(C)` for the number of geometric points at which the branch multiplicity is odd, after cancellations of even contact multiplicity. The normalized restricted triple curve `T_C -> C` satisfies

```text
g(T_C) = b_odd(C)/2 - 1.
```

Hence the possible low-genus escape mechanisms are exactly

```text
b_odd = 0  -> disconnected/square restriction;
b_odd = 2  -> genus 0;
b_odd = 4  -> genus 1;
b_odd >= 6 -> genus >= 2;
generic simple branch: b_odd = 8 -> genus 3.
```

Thus `14-t5` no longer needs to inspect arbitrary `M`-degree-4 curves. It only needs the finite `14-4ak` root list and, for each root, the parity pattern of the eight intersection units with the third-square branch divisor.

## Delta-pair symmetry

Because `M=C+delta(C)`, the two components occur as a deck pair. The triple condition is intrinsic on the Kummer surface and its branch class is deck invariant, so `C` and `delta(C)` have the same total branch degree `8`. The classification can therefore be done orbitwise under `delta` and the relevant Shimada symmetry subgroup rather than twice per split anticanonical member.

The exact low-genus test is not `C` being special as a divisor class; it is special **branch contact on `C`**. In particular, the root-pair identity alone does not force any cancellation among the eight branch intersections.

## Finite handoff from 14-4ak

For every effective Shimada root surviving

```text
C^2 = -2,
fsigma.C = 2,
M.C = 4,
delta(C) = M-C,
```

`14-t5` requires the following payload:

1. a rational parametrization of the normalization `C ~= P1` or an equivalent function-field description;
2. the third-square branch function restricted to `Q(C)`;
3. factorization of its divisor modulo `2`;
4. `b_odd(C)` and the resulting normalized genus;
5. if genus `0` or `1`, explicit rational-point / rank analysis;
6. if genus `>=2`, the strongest available rational-point bound together with physical-height translation;
7. `Q`-descent and physical-open filtering.

This is the exact bridge from the Shimada root enumeration to the triple correction term.

## What is proved now

```text
STAGE14_T5=REACTIVATED_ROOT_PAIR_TRIPLE_BRIDGE
TRIPLE_BRANCH_DEGREE_ON_ANY_SURVIVING_M4_ROOT=8
GENUS_FORMULA_BY_ODD_BRANCH_SUPPORT_LOCKED=true
GENERIC_SURVIVING_ROOT_TRIPLE_GENUS=3
LOW_GENUS_ESCAPE_REQUIRES_BRANCH_PARITY_COLLISION=true
DELTA_PAIR_ORBIT_REDUCTION_VALID=true
EXPLICIT_14_4AK_ROOT_LIST_IMPORTED=false
T_O_SQRT_B_PROVED=false
EXACTLY_TWO_SQRT_B_TRANSFER_PROVED=false
```

## Next

Wait only for `14-4ak` to output the finite effective root list and actual Shimada vector `M`. Then run the branch-parity test root-by-root. A proof that every physical root has `b_odd>=6` would remove genus-0/1 triple accumulation on the entire minimal fixed-curve sqrt(B) stratum; a stronger uniform count on the resulting genus-2/3 lifts would feed directly into `T(B)=o(sqrt(B))`.
