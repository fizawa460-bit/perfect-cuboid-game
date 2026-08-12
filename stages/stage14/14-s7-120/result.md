# Stage14-s7-120 — split bare square-class reverse support from residual post-mask deficit

## Status

`COMPLETE_SQUARECLASS_REVERSE_EXISTENCE_VERSUS_POSTMASK_DEFICIT_LEDGER`

Consumes merged `Stage14-s7-117..119` and merged `Stage14-Work-cbX40` from batch start main `ede7e5d167d94790e241680f022e8489839683d3`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The aligned fixed-E two-sided realization remains parked at

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```

and is not used below.

For each of the three active nonaligned realizations and each precompletion candidate `chi`, merged s7-119 gives the exact finite witness set `Omega_sq(chi)` and the residual Boolean `R_sq_post(chi;omega)` with

```text
C_ext(chi)=1
iff
exists omega in Omega_sq(chi) with R_sq_post(chi;omega)=1,
#Omega_sq(chi)<=B^o(1).
```

Define nested supports on one frozen branch cell:

```text
S_pre  = {chi : C_pre(chi)=1},
S_sq   = {chi in S_pre : Omega_sq(chi) != empty},
S_phys = {chi in S_sq : exists omega in Omega_sq(chi), R_sq_post(chi;omega)=1}.
```

Thus exactly

```text
S_phys subseteq S_sq subseteq S_pre.
```

Write

```text
#S_pre  = B^(sigma_pre+o(1)),
#S_sq   = B^(sigma_sq+o(1)),
#S_phys = B^(sigma_phys+o(1)),

delta_sq   = sigma_pre-sigma_sq >= 0,
delta_post = sigma_sq-sigma_phys >= 0.
```

Then

```text
sigma_phys = sigma_pre-delta_sq-delta_post.
```

If the branch is required to carry heavy mass `B^(mu-o(1))`, survival forces

```text
sigma_pre-delta_sq-delta_post >= mu.
```

This is an exact support ledger. The `B^o(1)` witness multiplicity is not converted into density and is not recharged.

The three active branches retain distinct charged measures:

```text
fixed-E endpoint: scalar t;
polynomial-E fixed product: scalar E;
polynomial-E polynomial-product: outer pair (E,m), with z=Em only an internal square-class host.
```

Therefore s7-120 proves a common logical decomposition but not a common support theorem.

```text
S_SQUARECLASS_BARE_SUPPORT_DEFINED=true
S_SQUARECLASS_POSTMASK_SUPPORT_DEFINED=true
S_SQUARECLASS_DEFICIT_LEDGER_EXACT=true
S_SQUARECLASS_SURVIVAL_BUDGET=sigma_pre_minus_delta_sq_minus_delta_post_ge_mu
S_SQUARECLASS_WITNESS_MULTIPLICITY_RECHARGED=false
S_NONALIGNED_COMMON_OUTER_MEASURE_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-121
```
