# Stage14-s7-163 — principal mass versus nonprincipal L1/L2 test

## Status

`COMPLETE_PRINCIPAL_MASS_NORMALIZATION_AND_ORTHOGONALITY_NO_GO`

Fix one retained valuation pattern `nu` with `q=Q_nu>1` and write its nonnegative residue masses as

```text
S_nu(a) >= 0,
A_nu,0 = sum_a S_nu(a),
P_nu = A_nu,0/phi(q).
```

For the required reciprocal-CRT class `rho_nu`, character orthogonality gives exactly

```text
J_nu = S_nu(rho_nu),
E_nu = J_nu-P_nu.
```

Thus the principal term is the uniform residue-class mean. The missing assertion is not normalization; it is a lower-discrepancy theorem forcing the particular target class to receive mass comparable to that mean under the full witness-dependent conditioning.

## L1 test

Nonnegativity only gives

```text
|A_nu,chi| <= A_nu,0.
```

Termwise summation therefore yields

```text
|E_nu| <= (phi(q)-1) P_nu,
```

which loses the entire character-family size and is much weaker than

```text
|E_nu| <= (1-epsilon_B) P_nu.
```

Stage14-s7-162 shows that this loss is not uniformly `B^o(1)` on positive-modulus-exponent cells.

## L2/Parseval test

Parseval gives the exact identity

```text
sum_chi |A_nu,chi|^2 = phi(q) sum_a S_nu(a)^2
```

and equivalently

```text
sum_a |S_nu(a)-P_nu|^2
  = (1/phi(q)) sum_{chi != 1} |A_nu,chi|^2.
```

This is a variance identity. Without a new bound for the right-hand side at the scale `o(P_nu^2)` appropriate to the target class, Cauchy--Schwarz does not give a positive lower bound for `S_nu(rho_nu)`.

There is an exact logical countermodel to any deduction from nonnegativity plus orthogonality alone: put all residue mass on one unit class `a0 != rho_nu`. Then

```text
J_nu=0,
P_nu=A_nu,0/phi(q)>0,
E_nu=-P_nu,
|E_nu|=P_nu.
```

All Fourier and nonnegativity identities remain valid, while every strict principal-domination inequality fails. This is not claimed to be an actual perfect-cuboid counterexample; it shows that the currently proved axioms are insufficient and a genuine equidistribution/anti-concentration theorem is indispensable. Summing over valuation patterns does not repair the logical gap, since the aggregate can be supported on target-avoiding patterns.

The residual physical post-mask is still outside this arithmetic calculation, so even an arithmetic `J_ccs` lower bound would not by itself be full-physical main-term dominance.

```text
Q26_PRINCIPAL_MASS_NORMALIZATION_TEST=PASS_EXACT_RESIDUE_MEAN
Q26_NONPRINCIPAL_L1_TEST=FAIL_LOSSES_PHI_QNU
Q26_NONPRINCIPAL_L2_TEST=FAIL_VARIANCE_NOT_TARGET_CLASS_LOWER_BOUND
ORTHOGONALITY_ONLY_ZERO_TARGET_RESIDUE_COUNTERMODEL=true
COUNTERMODEL_IS_LOGICAL_NOT_PHYSICAL_CUBOID_COUNTEREXAMPLE=true
AGGREGATION_OVER_NU_AUTOMATICALLY_REPAIRS_DOMINATION=false
REDUCED_MODULUS_AGGREGATE_DISCREPANCY_BOUND_PROVED=false
FULL_PHYSICAL_MAIN_TERM_DOMINANCE_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-164
```
