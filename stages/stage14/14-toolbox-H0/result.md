# Stage14-toolbox-H0 — independent centered-collision / Gaussian-dispersion interface audit

## Scope

This is the optional parallel H-line requested by merged `Stage14-toolbox-an` and isolated by `toolbox-h-independence-contract.md`. It reads merged sources only, writes only in the H workspace, does not alter toolbox-main `NEXT`, does not replace tH14, and claims no new Stage14 theorem.

Primary merged inputs:

- `Stage14-s7-15`: exact centered `(xi,k)` collision amplifier;
- `Stage14-s7-16`: inert split-k Fourier self-duality and absolute-completion barrier;
- `Stage14-t50/t51`: selector-sensitive two-modulus boundary and alias-free residue diagonal;
- `Stage14-tH14 R2`: QLS product-row adapter plus `PhysicalWeightedSquareclassFiberEnergy` obstruction;
- `Stage14-t52/t53`: principal/nonprincipal post-residue split;
- `Stage14-toolbox-an/ao`: obstruction routing and interface dictionary.

Open/unmerged descendants are not used as premises.

## Independent verdict

The merged routing picture is consistent, but the collision-to-Gaussian implication is **conditional, not proved**. `toolbox-ao` correctly gives a common coefficient-space contract; H0 finds that four additional logical bridges are indispensable before a Gaussian dispersion estimate can control the positive centered `(xi,k)` collision count.

### 1. Positivity bridge is missing for arbitrary signed coefficients

The s receiver counts unit-weight ordered same-`k` pairs and is nonnegative. The ao/tH common coefficient space is signed. For two same-`k` states with identical character rows but weights `+1,-1`, the signed centered Gaussian form equals `-2P^2` while the unit collision count is `2`.

Therefore a signed Gaussian upper bound does not automatically control `C_off`. The implication must be specialized to unit/nonnegative physical coefficients or upgraded to an explicit PSD domination.

### 2. Same-k does not automatically mean same Gaussian character row

The s7-15 amplifier uses `(k/p)`. The t/tH Gaussian receiver uses `chi_p(Ftilde(z))`. H0 finds no merged theorem asserting that, on a fixed `xi` packet,

\[
\chi_p(\widetilde F(z))=\eta_\xi(p)(k(z)/p)
\]

with a state-independent twist `eta_xi`.

Without such a bridge, two states with equal `k` can have decorrelated Gaussian rows. The explicit split-prime model with primes `5,13` and Gaussian squareclasses `1,6` gives rows `(+,+)` and `(+,-)`, hence zero correlation despite a same-`k` collision.

### 3. Raw Gaussian natural scale is too weak for the s centered scale

For unit weights the t50/tH raw target has scale `H_xi P^2`; s7-15 needs centered scale `H_xi^2 P`. If `P>H_xi`, the raw estimate is weaker by `P/H_xi`.

At the critical conditional choice

```text
H_xi <= B^(1/8+o(1)),
P     = B^(1/7+o(1)),
```

the missing factor is exactly `B^(1/56)`. Thus the raw selector-sensitive two-prime theorem, even if supplied at natural scale, is not by itself the `6/7` collision theorem. A genuinely diagonal-subtracted bound is required.

### 4. tH14 R2 QLS is not a rho=1/7 adapter under the current conductor envelope

R2 gives

\[
M\ll (K+L^2)E_{sq}B^{o(1)},
\qquad 2\rho\ge d
\]

for `K<=B^(d+o(1))`. The merged safe envelope is `d=4`, so direct use requires `rho>=2`. At `rho=1/7`, `2rho=2/7<4`.

Therefore the current R2 QLS adapter does not certify the s7-15 `rho=1/7` conditional target. One would need either a block conductor bound `d<=2/7`, or a different centered dispersion theorem.

## Additional guards confirmed

- the exact state diagonal must be subtracted once only;
- the alias-free oriented residue diagonal is not an additional state diagonal;
- principal squareclass coherence remains separate from residue cleanup;
- `PhysicalWeightedSquareclassFiberEnergy` cannot be assumed to prove the same principal/collision energy noncircularly;
- the s7-16 inert-prime local Fourier identity cannot be inserted into a split-prime Gaussian theorem without a prime-family transfer;
- signed common refinement, shared `U/V`, divisor hyperbola, canonical selector and all physical masks remain mandatory;
- angular completion must precede ordered-pair cross-kernel collapse.

## What is sufficient

The connection becomes valid if all of the following are proved on the same critical physical packet:

1. exact state lift preserving `(xi,k)` and the physical diagonal;
2. unit/nonnegative collision specialization or PSD domination;
3. same-`k` Gaussian row coherence up to `o(P)` bad primes;
4. exact-once diagonal subtraction;
5. a centered Gaussian bound `R_G(xi)<<H_xi^2 P B^o(1)` (or equivalent fixed saving);
6. common auxiliary-prime family and admissible conductor scale;
7. noncircular selector/squareclass control from independent physical geometry;
8. all merged ao order/mask gates.

Under these hypotheses,

\[
C_{off}(\xi)P^2(1-o(1))\le R_G(\xi)\ll H_\xi^2PB^{o(1)},
\]

hence `C_off(xi)<<H_xi^2/P * B^o(1)`.

## H0 boundary

```text
STAGE14_TOOLBOX_H0=COMPLETE_INDEPENDENT_CONNECTION_HYPOTHESIS_AND_COUNTEREXAMPLE_AUDIT
MERGED_SOURCES_ONLY=true
TOOLBOX_MAIN_FILES_MODIFIED=false
TOOLBOX_MAIN_BLOCKED_BY_H0=false
NEW_STAGE14_THEOREM_CLAIMED=false
SAME_COEFFICIENT_SPACE_SUFFICIENT_FOR_COLLISION_IMPLICATION=false
SIGNED_POSITIVITY_BRIDGE_REQUIRED=true
SAME_K_TO_GAUSSIAN_ROW_COHERENCE_REQUIRED=true
CENTERED_SCALE_HP2_TO_H2P_BRIDGE_REQUIRED=true
EXACT_STATE_DIAGONAL_SUBTRACT_ONCE=true
RESIDUE_DIAGONAL_IS_SECOND_STATE_DIAGONAL=false
PRIME_FAMILY_COMPATIBILITY_REQUIRED=true
TH14_R2_SAFE_QLS_DIRECTLY_REACHES_RHO_1_7=false
PHYSICAL_SQUARECLASS_ANTICOHERENCE_MUST_BE_NONCIRCULAR=true
CENTERED_XI_K_DISPERSION_PROVED=false
SELECTOR_SENSITIVE_TWO_AUXILIARY_GAUSSIAN_SECOND_MOMENT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
H0_RESULT=CONDITIONAL_INTERFACE_WITH_EXPLICIT_MISSING_BRIDGES
H0_NEXT=PARK_OR_CONSUME_ONLY_AFTER_CANONICAL_CONTRACT_RECHECK
```

The detailed assumptions are in `hypothesis-map.md`; finite/synthetic guards are in `counterexample-catalogue.md` and `interface_counterexample_audit.py`.
