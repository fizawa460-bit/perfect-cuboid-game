# Stage14-Work-biX21 receiver matrix

| Route | Prime support | Mass / energy | Exact arithmetic boundary | X21 status |
|---|---|---|---|---|
| Global range-stable arithmetic | `|Im(E_arith)|=B^o(1)` | `I=B^(1/2-o(1))`, `Energy>=B^(1-o(1))` | two-square mover / norm-ratio collision | one heavy `ell_*=B^o(1)` carries `B^(1/2-o(1))` state mass |
| Fixed-U | `r=omega(delta_G)=B^o(1)` | normalized mean influence and energy `B^(-o(1))` | SIGN / DIV / PROJ mover incidence | same concentration skeleton, different normalization |

## Common skeleton

```text
prime-index support K=B^o(1)
+
non-negligible mover mass
=>
max prime mass >= total/K
and
energy >= total^2/K.
```

This is a combinatorial concentration principle, not a cross-route arithmetic theorem.

## Global strengthening

Merged s7-62 already removes the diffuse image branch on the range-stable arithmetic receiver. Work-biX21 adds the immediate heavy-prime consequence:

```text
exists ell_*=B^o(1):
m(ell_*)=B^(1/2-o(1))
```

on any square-root-saturating range-stable arithmetic sequence.

The heavy-prime and collision-energy conclusions come from the same incidence mass and must not be double charged.

## Remaining mismatch

Global heavy-prime arithmetic:

```text
Q(ell*x,y) XOR Q(x,ell*y)
```

and fixed-prime norm-ratio collisions.

Fixed-U heavy-prime arithmetic:

```text
Gaussian orientation conjugation
-> SIGN / DIV / PROJ mover boundary
-> principal + centered split.
```

No finite-fiber adapter between those coefficient spaces is merged.

```text
COMMON_PRIME_SUPPORT_ENERGY_SKELETON_PROVED=true
COMMON_ARITHMETIC_COLLISION_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```
