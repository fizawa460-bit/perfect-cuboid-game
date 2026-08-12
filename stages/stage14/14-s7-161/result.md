# Stage14-s7-161 — recombine unit/nonunit CRT through valuation-averaged reduced moduli

## Status

`COMPLETE_UNIT_NONUNIT_RECOMBINATION_TO_VALUATION_AVERAGED_REDUCED_MODULUS_CHARACTER_RECEIVER`

Stage14-s7-159 gives an exact principal/nonprincipal character split on the unit pattern. Stage14-s7-160 shows that every admissible nonunit Q-supported valuation pattern `nu` reduces, after exact local stripping, to the same quotient-residue architecture modulo a reduced modulus

```text
Q_nu | Q.
```

Hence the exact common-core averaged CRT first moment may be regrouped as

```text
J_ccs = sum_nu J_nu,
```

where each `J_nu` retains the original scalar or polynomial `(E,m)` charged measure and all filtered-tau3 / side-host / q17 predicates compatible with that valuation pattern.

For `Q_nu>1`, character orthogonality gives

```text
J_nu = P_nu + E_nu,
P_nu = A_{nu,0}/phi(Q_nu),
E_nu = (1/phi(Q_nu))
       * sum_{chi != 1 mod Q_nu} conjugate(chi(rho_nu)) A_{nu,chi}.
```

For a fully saturated pattern `Q_nu=1`, define simply

```text
P_nu:=A_{nu,0},
E_nu:=0.
```

Therefore

```text
J_ccs = P_red + E_red,
P_red := sum_nu P_nu,
E_red := sum_nu E_nu.
```

This is exact. In particular, the previous four unit/nonunit theorem species are not intrinsically separate arithmetic gates. They reduce to two charged-measure variants of one valuation-averaged reduced-modulus problem.

A sufficient positive first-moment input is now the aggregate inequality

```text
|E_red| <= (1-epsilon_B) P_red
```

at the required survival scale, together with the principal-mass normalization already encoded in `P_red`. No separate nonunit positive-density theorem is required once its valuation strata are included in the reduced-modulus average.

This does not prove the aggregate discrepancy estimate. It only removes the artificial unit/nonunit receiver split without collapsing the common-core average or the polynomial `(E,m)` measure.

Scalar theorem species:

```text
UniformScalarFilteredTau3CommonCoreAndQValuationAveragedReducedModulusReciprocalCRTCharacterDiscrepancyBelowPrincipalMass
```

Polynomial outer-pair theorem species:

```text
UniformPolynomialOuterPairFilteredTau3CommonCoreAndQValuationAveragedReducedModulusReciprocalCRTCharacterDiscrepancyBelowPrincipalMass
```

The residual root-origin/canonical/allocation/cell/post-column mask remains separately charged.

```text
Q25_UNIT_NONUNIT_RECOMBINATION_TEST=PASS_EXACT_REDUCED_MODULUS_CHARACTER_RECOMBINATION
UNIT_NONUNIT_SEPARATE_ARITHMETIC_GATES_SUPERSEDED=true
S_REDUCED_MODULUS_CHARACTER_THEOREM_SPECIES_COUNT=2
REDUCED_MODULUS_AGGREGATE_DISCREPANCY_BOUND_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
RECEIVER_MATERIALLY_CHANGED=true
Q26_THEOREM_TARGET_NOW_STABLE=true
Q26_NEEDED=true
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-162
```