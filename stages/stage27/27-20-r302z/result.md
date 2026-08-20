# Stage27-20-r302z — exact odd square-collision multiplicity and the singular-frequency weight

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302y
SOURCE_STAGE=Stage20

R302y isolates the odd square-collision relation

```text
v^2 = u^2 (mod m),
m=q'_odd.
```

Its local multiplicity can be computed exactly. Let `p^k || m` and put `s=v_p(u)` truncated at `k`. The number of residues `v mod p^k` satisfying

```text
v^2 = u^2 (mod p^k)
```

is

```text
2 p^s,              if 2s<k,
p^floor(k/2),       if 2s>=k.
```

In particular it is at most

```text
2 p^min(s,floor(k/2)).
```

Define the square-root singular modulus

```text
m_* = product_{p^k || m} p^floor(k/2).
```

CRT then gives the uniform collision-degree bound

```text
#{v mod m : v^2=u^2 mod m}
 <= 2^omega(m) gcd(u,m_*).
```

Because `m` lies in the existing polynomial-height modulus range,

```text
2^omega(m) <= tau(m) = B^o(1).
```

Hence unit frequencies `(u,m)=1` have only `B^o(1)` odd square-collision partners. Large collision fibers can occur only on singular frequencies sharing a nontrivial factor with `m_*`.

This separates the collision branch into

1. a regular/unit part whose graph degree is subpolynomial; and
2. a singular part measured by the explicit weight `gcd(u,m_*)`.

No fixed-power saving follows from this multiplicity statement alone. It is a routing reduction for the collision contribution.

```text
FIRST_MISSING_LEMMA=
MAINWallPrimitiveSquareCollisionSingularFrequencyWeightedEnergyControl

STAGE27_20_R302Z_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ODD_PRIME_POWER_COLLISION_COUNT_PROVED=true
CRT_COLLISION_DEGREE_BOUND_PROVED=true
UNIT_COLLISION_DEGREE_SUBPOLYNOMIAL=true
SINGULAR_COLLISION_WEIGHT=gcd(u,m_*)
SINGULAR_WEIGHTED_ENERGY_DEFICIT_PROVED=false
NONZERO_SQUARED_FREQUENCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302aa
NEXT_BATCH=Stage27-20-r302-main-batch
```