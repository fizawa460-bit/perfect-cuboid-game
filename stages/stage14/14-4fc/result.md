# Stage14-4fc — repeated-ray energy forces exact-C mass below radial capacity

## Status

`COMPLETE_HEAVY_RAY_ENERGY_TO_MASS_CAPACITY_THRESHOLD`

Consumes Stage14-4fb and merged Stage14-4el / Stage14-s7-77.

On one concentrated exact modulus `C`, write

```text
M_C=B^(mu+o(1)), mu>0,
K_ray(C)=sum_r m_C(r)(m_C(r)-1).
```

Merged s7-77 gives the exact upper bound

```text
K_ray(C) <= m_max(C) M_C.
```

Stage14-4fb gives

```text
m_max(C) <= B^(rho(phi)+o(1)),
rho(phi)=1/4-phi.
```

Hence

```text
K_ray(C) <= B^(rho(phi)+mu+o(1)).                 (1)
```

For the heavy-ray branch to carry exponent-zero pair mass, merged s7-77 requires

```text
K_ray(C)=M_C^2 B^(-o(1))=B^(2mu-o(1)).           (2)
```

Comparing (1) and (2) forces

```text
boxed:
mu <= rho(phi)=1/4-phi.
```

Equivalently, for every fixed `epsilon>0`, if

```text
mu >= 1/4-phi+epsilon,
```

then repeated-ray energy is fixed-power too small and the concentrated branch must lie on the genuine mover alternative.

Uniformly, because `phi>=5/24`,

```text
mu <= 1/24
```

is necessary for a heavy-ray survivor.

This is stronger than Work-bpX28's conditional capacity statement: it identifies the exact threshold directly from the collision-energy requirement. It does not exclude the low-mass region `0<mu<=1/4-phi`.

```text
HEAVY_RAY_SURVIVAL_REQUIRES_MU_LE_1_4_MINUS_PHI=true
UNIFORM_HEAVY_RAY_SURVIVAL_REQUIRES_MU_LE_1_24=true
MU_GT_RADIAL_CAPACITY_FORCES_GENUINE_MOVER=true
HEAVY_RAY_CLOSED=false
RECEIVER_MATERIALLY_CHANGED=false
MAIN_ROUTE_H_NEEDED=false
NEXT=Stage14-4fd
```
