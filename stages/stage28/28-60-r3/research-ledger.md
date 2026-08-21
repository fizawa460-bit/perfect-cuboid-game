# Stage28-60-r3 — final bounded exploration ledger

Checkpoint60 parent + r2 already tested causal decomposition, double-charge control, interaction ladders, normalized interaction curvature, branch-profile comparison, common-host reformulations, local/Huang/K3 symmetry, and bounded branch-sensitive literature rematches.

r3 intentionally avoids repeating those routes.  It adds five materially distinct checks:

1. `R21_FIXED_CURVE_SPECTRUM_COMPARISON`: reuse Stage14-4ak's exact physical `M.C=4` void and compare it against the Stage20 Saunderson degree-six rational family.
2. `R22_MCKINNON_REMATCH`: test whether McKinnon's singular-branch hyperelliptic-K3 counting theorem can be imported under the exact physical height; reject direct import because the repo height is big-and-nef non-ample.
3. `R23_QUASIPOLARIZED_LOW_DEGREE_REMATCH`: test Rams--Schuett low-degree rational-curve bounds; reject direct degree-5/6 classification because the required high-degree regime does not match `M^2=8`.
4. `R24_STAGE19_MOVING_MECHANISM_FIREWALL`: propagate Stage14-4al: absence of a fixed `M.C=4` curve does not improve the global `N2` exponent because a collective moving-fibre/first-small-point mechanism remains live.
5. `R25_FINITE_LATTICE_RECEIVER`: reduce the only remaining low-degree fixed-curve question to a finite Shimada-lattice enumeration for source/target physical degree 5/6 spectra.

## New certified-candidate causal statement

From audited Stage14-4ah and 4ak:

```text
all physical Stage19 rational curves have M.C>=4
physical Stage19 M.C=4 curves = none
```

so any finite union of fixed physical rational curves contributes at polynomial exponent at most `2/5`.

From audited Stage28-50-r2, the generalized Saunderson family supplies a generically injective homogeneous degree-six rational target curve and hence a fixed-curve `B^(1/3)` contribution.

This is a genuine mechanism differential but does not resolve the interaction-curvature threshold.

## Stop test

After r3, every remaining route belongs to one of two categories:

- a **bounded finite computation**: physical low-degree root spectra `M.C=5,6` on the two K3 covers;
- a **substantially new global theorem**: control the moving/collective complement strongly enough to transfer fixed-curve or branch-profile data to `J_28` at the critical `(log B)^(-2)` scale.

No further algebraic rearrangement of the current endpoint bounds, local densities, Huang exponents, Manin log ledgers, or interaction identities changes the bridge corridor.

```text
R3_MATERIALLY_DISTINCT_ROUTES=5
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=true
FIXED_CURVE_SPECTRUM_DIFFERENTIAL=true
MAXIMAL_BOUNDED_EXPLORATION_CANDIDATE=true
FURTHER_ROUTINE_REPO_ALGEBRA_EXPECTED_TO_PROGRESS=false
```