# Stage27-20-r302as — canonical actual-residue receiver is root multiplicity times physical root energy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ar
SOURCE_STAGE=Stage20

For one retained packet let

```text
R_q(C) = #Root_q(C),
E_all(W) = sum_{f mod q}|W(f)|^2,
E_root(W;C) = sum_{f in Root_q(C)}|W(f)|^2.
```

The exact local arithmetic sum from r302aq is

```text
S_C(W)=sum_{f in Root_q(C)} W(f).
```

Cauchy on the **actual** root set gives

```text
|S_C(W)|^2
 <= R_q(C) * E_root(W;C).
```

Therefore a sufficient coefficient-specific fixed-power input, charged against the original physical Fourier energy, is

```text
R_q(C) * E_root(W;C)
 <= B^{-2delta+o(1)} E_all(W)
```

for one fixed `delta>0`, in the exact packet/summation form required by the same-`H_phys^MAIN` receiver.

Equivalently, when `E_all(W)>0`, define the physical root-energy fraction

```text
rho_root(W;C)
 = E_root(W;C)/E_all(W).
```

Then the canonical local sufficient condition is

```text
R_q(C) * rho_root(W;C)
 <= B^{-2delta+o(1)}.
```

This formulation has three advantages over the r302v-an `A/B/C` package:

1. it is written directly in the original residue coefficient `W` and exact quadratic root set;
2. it automatically includes singular growth in the number of roots;
3. it asks only for the actual physical coefficient class, consistent with the projector-norm obstruction in r302ar.

No lower bound for `E_all(W)` and no root-energy deficit is asserted here. In particular, root cardinality alone is not a saving unless it is subpolynomial **and** the actual physical `L2` energy is sufficiently spread away from those roots.

This also preserves the r302j firewall: divisor-many reconstruction of an occupied root fiber does not by itself prove that the physical coefficient has polynomially more energy outside that fiber.

```text
FIRST_MISSING_LEMMA=
MAINWallActualResidueQuadraticRootEnergyProductDeficit

STAGE27_20_R302AS_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ACTUAL_ROOT_SET_CAUCHY_REDUCTION_PROVED=true
ROOT_MULTIPLICITY_FACTOR_RETAINED=true
ACTUAL_PHYSICAL_ROOT_ENERGY_FRACTION_DEFINED=true
ROOT_CARDINALITY_ALONE_FIXED_POWER=false
ROOT_ENERGY_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302at
NEXT_BATCH=Stage27-20-r302-main-batch
```