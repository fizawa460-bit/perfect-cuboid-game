# Stage28-60-r3 — final bounded exploration ledger

Checkpoint60 parent + r2 already tested causal decomposition, double-charge control, interaction ladders, normalized interaction curvature, branch-profile comparison, common-host reformulations, local/Huang/K3 symmetry, and bounded branch-sensitive literature rematches.

r3 intentionally avoids repeating those routes. It adds seven materially distinct checks:

1. `R21_FIXED_CURVE_SPECTRUM_COMPARISON`: reuse Stage14-4ak's exact physical `M.C=4` void and compare it against the Stage20 Saunderson degree-six rational family.
2. `R22_MCKINNON_REMATCH`: test whether McKinnon's singular-branch hyperelliptic-K3 counting theorem can be imported under the exact physical height; reject direct import because the repo height is big-and-nef non-ample.
3. `R23_QUASIPOLARIZED_LOW_DEGREE_REMATCH`: test Rams--Schuett low-degree rational-curve bounds; reject direct degree-5/6 classification because the required high-degree regime does not match `M^2=8`.
4. `R24_STAGE19_MOVING_MECHANISM_FIREWALL`: propagate Stage14-4al: absence of low-degree fixed curves does not improve the global `N2` exponent because a collective moving-fibre/first-small-point mechanism remains live.
5. `R25_FINITE_LATTICE_RECEIVER`: reduce the remaining low-degree fixed-curve question to the exact Shimada physical lattice/chamber/Q-descent data.
6. `R26_ODD_DEGREE_ANTI_INVARIANT_CONGRUENCE`: reconstruct the Stage14-4ak anti-invariant lattice on exact official Shimada data and prove that every anti-invariant norm is divisible by four; combine this with the split-curve parity identity to eliminate every physical odd `M`-degree, in particular `M.C=5`.
7. `R27_DISTINGUISHED_ROOT_M6_DIAGNOSTIC`: evaluate the physical `M`-degree of all 40 distinguished Shimada roots. The histogram is `0:16, 2:24`; no distinguished root has degree six. This is diagnostic only because `L40` is not the complete root spectrum.

## New r3 causal statement

From audited Stage14-4ah and 4ak:

```text
all physical Stage19 rational curves have M.C>=4
physical Stage19 M.C=4 curves = none
```

The exact-head r3 lattice probe gives a rank-six positive anti-invariant Gram matrix of determinant `256` with diagonals divisible by four and off-diagonals even. Therefore every anti-invariant norm is `0 mod 4`.

For a physical odd-degree curve `C`, the positive branch firewall forces the curve into a split deck pair. With `x=C-delta(C)`, one has

\[
-x^2\equiv2(M\cdot C)\pmod4.
\]

Thus odd `M.C` would require anti-invariant norm `2 mod 4`, impossible. Consequently the candidate strengthened fixed-curve floor is

```text
physical Stage19 fixed rational curve degree >= 6.
```

Any finite union of fixed source rational curves therefore contributes at polynomial exponent at most `1/3`.

From audited Stage28-50-r2, the generalized Saunderson family supplies a generically injective homogeneous degree-six rational target curve and hence a fixed-curve `B^(1/3)` contribution.

Thus the possible source `2/5` fixed-curve channel is closed. The source and target fixed-curve mechanisms now meet at the same `1/3` exponent threshold unless the remaining Stage19 M6 stratum is empty.

The distinguished-root diagnostic finds no M6 witness among Shimada's classical 40 roots. Any source M6 curve, if present, lies beyond that distinguished configuration and requires a complete low-degree class analysis.

## Exact CI support

Latest exact diagnostic workflow:

```text
Stage28-60-r3 low-degree K3 spectrum
run_id=32438047573
conclusion=success
L40_M_DEGREE_HISTOGRAM={0:16,2:24}
L40_M6_COUNT=0
```

The run reconstructs the physical Shimada labeling up to `AutX0f`, the anti-invariant rank-six lattice, determinant `256`, the mod-four norm law, and the distinguished-root histogram. The theorem-level promotion remains subject to fresh Stage28 audit.

## Stop test

After the new odd-degree closure and L40 diagnostic, every remaining route belongs to one of two categories:

- a **bounded but genuinely new complete lattice/linear-system classification**: physical Stage19 M-degree-six rational curves, including split and invariant mechanisms, non-distinguished root classes, and singular rational members of positive-self-intersection classes, with full gluing/effectivity/Q-descent/physical filtering;
- a **substantially new global theorem**: control the moving/collective complement strongly enough to transfer fixed-curve or branch-profile data to `J_28` at the critical `(log B)^(-2)` scale.

No further algebraic rearrangement of the current endpoint bounds, local densities, Huang exponents, Manin log ledgers, interaction identities, or the finite L40 configuration changes the bridge corridor.

```text
R3_MATERIALLY_DISTINCT_ROUTES=7
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=true
ODD_PHYSICAL_M_DEGREE_OBSTRUCTION_CANDIDATE=true
STAGE19_M5_FIXED_CURVE_ABSENT_CANDIDATE=true
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
DISTINGUISHED_L40_M6_WITNESS_FOUND=false
FIXED_CURVE_SPECTRUM_DIFFERENTIAL=true
MAXIMAL_BOUNDED_EXPLORATION_CANDIDATE=true
FURTHER_ROUTINE_REPO_ALGEBRA_EXPECTED_TO_PROGRESS=false
NEXT_FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```