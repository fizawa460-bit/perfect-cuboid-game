# Stage14-t101 — principal-density / centered-discrepancy split for one mover boundary

## Status

`COMPLETE_SINGLE_MOVER_BOUNDARY_PRINCIPAL_CENTERED_SPLIT`

Stage14-t101 consumes merged Stage14-t100 and merged frozen Stage14-tH27. The tH27 snapshot is not reopened.

Merged tH27 certifies that none of the three elementary t99 boundary classes has a uniform fixed-power density deficit under the full canonical-LPF physical packet. Its preferred next reduction is to split principal boundary mass from centered discrepancy. Stage14-t100 further restricts square-root saturation to a nontrivial mover boundary.

Fix one surviving mover boundary event `E(x)` on the frozen packet and let `mu_E` denote its conditional density with respect to the charged-once packet measure `nu` after all fixed background labels other than the mover coordinate are frozen:

```text
mu_E := E_nu 1_E.
```

Then pointwise and before absolute values,

```text
1_E = mu_E + (1_E-mu_E),
E_nu(1_E-mu_E)=0.
```

Hence every single-boundary contribution splits exactly into

```text
principal density contribution
+
centered boundary discrepancy.
```

This is not a saving by itself. It is a structural separation of the obstruction certified by tH27.

For the three branches:

1. SIGN mover: `mu_E` is the conditional angular/conic occupancy of the explicit quadratic-cone XOR. The centered remainder has zero conditional mean and is the part eligible for angular discrepancy / harmonic analysis.

2. DIV mover: `mu_E` is the conditional density of one nontrivial fixed-divisor residue XOR. The centered remainder is an exact zero-mean residue-class function and therefore admits a finite additive/multiplicative character expansion modulo the fixed divisor after the principal coefficient is removed.

3. PROJ mover: `mu_E` is the conditional density of one nontrivial endpoint projective residue XOR modulo `d=B^o(1)`. The centered remainder is an exact zero-mean function on the finite projective quotient and therefore expands only in nonprincipal characters of that quotient.

Thus the tH27 principal-mass obstruction is isolated entirely in `mu_E`. Existing discrepancy/large-sieve/character technology should only be charged against the centered term; it cannot be used to claim removal of `mu_E`.

The fixed-power localization consequences are immediate but conditional:

```text
if mu_E = B^(-delta+o(1)), delta>0,
then that boundary layer is already sub-square-root by the existing positive-density/occupancy ledger;

if mu_E = B^(-o(1)),
then any remaining square-root obstruction lies in the principal mover density, while the centered remainder is a separate oscillatory receiver.
```

No uniform fixed `delta` for `mu_E` is proved here, and no centered discrepancy saving is promoted to the whole family.

```text
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
SINGLE_MOVER_BOUNDARY_PRINCIPAL_CENTERED_SPLIT_PROVED=true
SIGN_PRINCIPAL_DENSITY_ISOLATED=true
DIV_PRINCIPAL_DENSITY_ISOLATED=true
PROJ_PRINCIPAL_DENSITY_ISOLATED=true
DIV_CENTERED_NONPRINCIPAL_CHARACTER_EXPANSION_READY=true
PROJ_CENTERED_NONPRINCIPAL_CHARACTER_EXPANSION_READY=true
SIGN_CENTERED_ZERO_MEAN_DISCREPANCY_READY=true
UNIFORM_FIXED_POWER_PRINCIPAL_DENSITY_DEFICIT_PROVED=false
CENTERED_BOUNDARY_FIXED_POWER_SAVING_PROVED=false
FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleMoverBoundaryPrincipalDensityPlusCenteredDiscrepancy
NEXT=Stage14-t102
```
