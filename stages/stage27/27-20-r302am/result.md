# Stage27-20-r302am — exact joint odd/2-primary singular energy as projected physical coset concentration

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302al
SOURCE_STAGE=Stage20

R302al reduces the full primitive-unit quadratic form to the joint singular weight

```text
gcd(y_odd,m_*) gcd(y_2,2_*)
```

when `nu>=2`, with

```text
q'=2^nu m,
2_*=2^{floor(nu/2)}.
```

For `nu<=1` there is no nontrivial 2-primary square-label weight and the r302ab projected odd formula applies unchanged.

## 1. Exact joint divisor expansion for `nu>=2`

Use

```text
gcd(y_odd,m_*)
 = sum_{r|gcd(y_odd,m_*)} phi(r),

gcd(y_2,2_*)
 = sum_{s|gcd(y_2,2_*)} phi(s),
```

where `r` is odd and `s` is a power of `2`.

The primitive admissibility is `b'=b/d` even. Since

```text
y_odd=b'/2 (mod m),
y_2=b'/2 (mod 2^{nu-1}),
```

we have

```text
r|y_odd  <=> r|b',
s|y_2    <=> 2s|b'.
```

Because `(r,2s)=1` apart from the displayed factor `2`, the joint condition is exactly

```text
2 r s | b'.
```

Thus, with

```text
M_{r,s}=2 d r s,
```

the arithmetic-progression Fourier identity from r302ab gives

```text
sum_{b: M_{r,s}|b}|c_b|^2
 = C_{M_{r,s},0}(W)/(q M_{r,s}).
```

Therefore the exact joint singular weighted energy is

```text
sum_{b in Adm_d}
 gcd(y_odd,m_*)gcd(y_2,2_*) |c_b|^2

= (1/(2 d q))
  sum_{r|m_*}
  sum_{s|2_*}
    (phi(r)/r)(phi(s)/s)
    C_{2drs,0}(W).
```

The base admissible energy is the `(r,s)=(1,1)` term:

```text
sum_{b in Adm_d}|c_b|^2
 = C_{2d,0}(W)/(2dq).
```

## 2. Zero-fixed-power-loss adapter

Consequently a sufficient full joint singular-energy adapter is

```text
sum_{r|m_*}
 sum_{s|2_*}
   (phi(r)/r)(phi(s)/s) C_{2drs,0}(W)
 <= B^{o(1)} C_{2d,0}(W).
```

The number of `(r,s)` pairs is subpolynomial: `tau(m_*)=B^o(1)` and `tau(2_*)=O(log B)=B^o(1)` on the existing polynomial-height modulus range.

As in r302ac, each `C_{2drs,0}` is a coarse grouping of the base `2d` projected blocks. Therefore it is enough to prove the corresponding joint projected fine-block support multiplicity is `B^o(1)` uniformly for every `(r,s)`.

For `nu=0` or `1`, use the already-auditable r302ab-ac progression `(M_r,b_r)` that preserves respectively the unrestricted or odd primitive local class. No artificial 2-primary weight is inserted in those cases.

This converts the second r302al missing lemma into a concrete physical block-concentration adapter. It supplies no fixed power by itself.

```text
FIRST_MISSING_LEMMA=
MAINWallJointPrimitiveProjectedFineBlockMultiplicitySubpowerAdapter

STAGE27_20_R302AM_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
JOINT_GCD_WEIGHT_DIVISOR_EXPANSION_PROVED=true
JOINT_SINGULAR_FOURIER_ENERGY_PROGRESSION_IDENTITY_PROVED=true
TWO_PRIMARY_ADMISSIBILITY_PRESERVED=true
JOINT_PROJECTED_BLOCK_MULTIPLICITY_SUBPOWER_SUFFICIENT=true
JOINT_PROJECTED_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
JOINT_UNIT_FIBER_NONCONCENTRATION_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302an
NEXT_BATCH=Stage27-20-r302-main-batch
```