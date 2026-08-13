# Stage14-4fb — heavy-ray atomic multiplicity bounded by short radial capacity

## Status

`COMPLETE_HEAVY_RAY_ATOMIC_MULTIPLICITY_RADIAL_CAPACITY_BOUND`

Consumes merged `Stage14-4fa`, merged `Stage14-Work-bpX28`, and the concentrated exact-`C` heavy-ray ledger of merged `Stage14-4el` / `Stage14-s7-77`.

The whole-family theorem remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Fix a concentrated exact polynomial common core `C` and one primitive reciprocal ray in the heavy-ray branch. Let `m_C(r)` be its charged-once unit-incidence multiplicity and `m_max(C)` the maximum over rays.

Merged 4fa proves that after freezing the ray, the large overlap `G`, its allocation, and the surviving primitive agreement pair, every physical incidence is determined by an exact radial scale `h` up to `B^o(1)` multiplicity, with

```text
#h <= B^(rho(phi)+o(1)),
rho(phi):=1/4-phi,
0<=rho(phi)<=1/24.
```

Therefore uniformly on the heavy-ray square-root packet,

```text
m_C(r) <= B^(rho(phi)+o(1)),
```

and hence

```text
boxed:
m_max(C) <= B^(1/4-phi+o(1)) <= B^(1/24+o(1)).
```

This is a true atomic-capacity estimate: the `B^o(1)` reverse fiber per exact `h` was already charged in merged 4eq and is not charged again.

No comparison with the required exact-`C` mass has yet been made.

```text
HEAVY_RAY_ATOMIC_CAPACITY_EXPONENT=rho(phi)=1/4-phi
HEAVY_RAY_ATOMIC_MULTIPLICITY_BOUND=B^(rho(phi)+o(1))
UNIFORM_HEAVY_RAY_ATOMIC_MULTIPLICITY_BOUND=B^(1/24+o(1))
FIXED_H_REVERSE_FIBER_RECHARGE_ALLOWED=false
RECEIVER_MATERIALLY_CHANGED=false
MAIN_ROUTE_H_NEEDED=false
NEXT=Stage14-4fc
```
