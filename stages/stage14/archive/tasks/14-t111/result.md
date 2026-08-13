# Stage14-t111 — discharge standalone projective-class density and isolate the joint cofactor/prime correlation

## Status

`COMPLETE_PROJECTIVE_CLASS_STANDALONE_DENSITY_NOGO_AND_JOINT_CORRELATION_RECEIVER`

Consumes Stage14-t110 on the same batch branch together with merged Stage14-tH26 and Stage14-tH28 as negative applicability boundaries.

For fixed packet modulus `d=B^o(1)` and a fixed physical prime interval `I`, let

```text
P(I,d)
```

be the canonical split Gaussian prime labels `pi_ell` with rational prime norm `ell in I` and `gcd(ell,d)=1`.  Every such label has exactly one projective class

```text
[pi_ell] in G(d),
```

so the sets

```text
P_c(I,d)={pi in P(I,d):[pi]=c},
c in G(d),
```

partition `P(I,d)`.

Because

```text
|G(d)| <= |(Z[i]/dZ[i])^x| <= d^2 = B^o(1),
```

projective localization has only subpolynomially many cells.

Consequently there cannot be a fixed `delta>0` bound of the form

```text
|P_c(I,d)|
 <= B^(-delta+o(1)) |P(I,d)|
```

uniformly for every projective class `c` whenever `P(I,d)` is nonempty: summing such a bound over all `B^o(1)` classes would give

```text
|P(I,d)|
 <= B^(-delta+o(1)) |P(I,d)|,
```

which is impossible for sufficiently large `B`.

Thus the endpoint projective condition, viewed only as localization into one of `B^o(1)` prime classes, cannot itself be charged as a uniform fixed-power density loss.  This is compatible with merged tH26: a subpolynomial Hecke/projective character family has no polynomial family length to trade for a fixed power.

This argument does **not** claim that the particular physical class selected by every cofactor ray is always heavily occupied.  The selected class moves with the primitive cofactor:

```text
c_U(a,gamma)=([gamma][a])^(-1).
```

Therefore a remaining saving could only come from the **joint correlation** between

```text
1. the ell-independent physical cofactor core C_U(a,gamma),
2. the moving selected class c_U(a,gamma),
3. Gaussian prime occupancy of that class in the n-dependent interval I_B(N(gamma)).
```

The standalone ray-class density has been discharged; the coupled cofactor-to-prime-class assignment has not.

Equivalently, the live projective relation is the multiplicative incidence

```text
[gamma]*[a]*[pi_ell]=1 in G(d)
```

conditioned on the primitive physical cofactor core.  This is a material receiver change from a generic projected norm-form support problem to an explicit cofactor/prime projective-class correlation.

Merged tH26 already certifies that generic Hecke large sieve/BV/BDH machinery does not handle the full nonmultiplicative physical cofactor coefficient, while merged tH28 certifies that the unseparated projected support has no applicable off-the-shelf theorem.  No new tH is justified until the cofactor core is opened further into a theorem-compatible density/centered decomposition.

```text
PROJECTIVE_CLASSES_PARTITION_CANONICAL_PRIME_LABELS=true
PROJECTIVE_CLASS_COUNT=Bo1
UNIFORM_ALL_CLASS_FIXED_POWER_DEFICIT_IMPOSSIBLE=true
ENDPOINT_PROJECTIVE_SELECTOR_STANDALONE_FIXED_POWER_SOURCE=false
PARTICULAR_SELECTED_CLASS_HEAVY_OCCUPANCY_PROVED=false
JOINT_COFACTOR_SELECTED_CLASS_PRIME_CORRELATION_REMAINS=true
RECEIVER_MATERIALLY_CHANGED=true
TH26_NEGATIVE_BOUNDARY_RETAINED=true
TH28_NEGATIVE_BOUNDARY_RETAINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUPrimitiveGaussianCofactorPhysicalCoreSelectedProjectivePrimeClassCorrelation
NEXT_INTERNAL_TARGET=PrimitiveGaussianCofactorPhysicalCoreDensityPlusSelectedClassCenteredCorrelation
NEXT=Stage14-t112
```
