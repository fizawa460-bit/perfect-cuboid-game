# Stage14-Work-buX33 receiver / supersession matrix

| Route | Merged boundary | Current polynomial receiver | Exhausted / superseded | Still forbidden |
|---|---|---|---|---|
| global/main heavy | `4fp` | fixed-`E` outer support of physical short unitary-divisor existence, or polynomial `(E,m)` outer-pair support | inner unitary witness multiplicity is only `B^o(1)` | do not charge witness multiplicity, q14/Ford ambient density, or independence of canonical/reverse completion |
| s heavy | `s7-98` | same global heavy packet, refined into fixed-`E`, polynomial-`E` fixed-`m`, and polynomial `(E,m)` branches | earlier primitive-ratio and weighted-unitary coordinates are same-packet refinements | do not multiply s and main counts; do not freeze polynomial `E` or polynomial `m` at subpolynomial cost |
| fixed-U | `t136+tH30` | endpoint-short fixed Gaussian residue prime occupancy deficit OR long-headroom individual subpolynomial-modulus fixed Gaussian residue prime occupancy bias | opaque scalar norm weight, cofactor-side real/nonreal split, and tH29 Type-I/II cofactor adapter are superseded | do not transfer radial endpoint removal; do not claim uniform PNT in individual `d=B^o(1)` residue classes; do not ignore exceptional-real-character boundary |

## Cross-route locks

```text
GLOBAL_S_SAME_PACKET=true
GLOBAL_S_MAIN_S_COUNTS_MULTIPLICABLE=false
GLOBAL_S_INNER_UNITARY_MULTIPLICITY_POLYNOMIAL_OBSTRUCTION_EXHAUSTED=true
GLOBAL_S_OUTER_PHYSICAL_EXISTENCE_SUPPORT_RECEIVER_PROVED=true

FIXED_U_OPAQUE_COFACTOR_WEIGHT_OBSTRUCTION_EXHAUSTED=true
FIXED_U_TYPE_I_II_COFACTOR_ADAPTER_OBSTRUCTION_EXHAUSTED=true
FIXED_U_RECEIVER_RELOCATED_TO_PRIME_SIDE_ONLY=true

COMMON_OUTER_FAMILY_INNER_ARITHMETIC_WITNESS_LANGUAGE_PROVED=true
COMMON_PHYSICAL_MEASURE_ADAPTER_PROVED=false
COMMON_ARITHMETIC_INNER_SELECTOR_ADAPTER_PROVED=false
DIRECT_OUTER_SUPPORT_EXISTENCE_TO_FIXED_RESIDUE_PRIME_OCCUPANCY_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## Why the old weight-location comparison is superseded

`Work-btX32` compared

```text
global/s: inner-dependent W_unit(n,q,u)
fixed-U:  outer-only W_c(n) times prime selector.
```

After merged `t133..t136+tH30`, the fixed-U cofactor weight is not a black-box receiver any longer. It is unfolded into actual primitive Gaussian cofactors in one fixed sector and residue class. The remaining fixed-U difficulty is entirely prime-side.

So the minimal comparison is now

```text
global/s:
  outer physical support of existence of a short unitary-divisor witness

versus

fixed-U:
  fixed Gaussian residue prime occupancy in reciprocal intervals.
```

This is a stronger no-go boundary than the older weight-location mismatch: even after the fixed-U weight is opened, the witness species and charged measures still do not match.

## H matrix

| Route | H needed now? | Reason |
|---|---:|---|
| main heavy | no new H | existential canonical/reverse witness predicate still needs internal opening |
| s | no | same heavy packet, next internal branch opening first |
| fixed-U | no | `tH30` just audited the current exact frozen residue hyperbola; `t137+` must materially change endpoint/long-headroom receiver before `tH31` |
| existing non-heavy main | yes, pending | pre-existing three-divisor / mover / diffuse gates only |

```text
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH31_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## Next target

`PhysicalExistenceSupportVersusFixedResiduePrimeOccupancyTheoremIntersectionOrNoGo`

Normal revisit: approximately merged `4fs + s7-101 + t139`, or an earlier material theorem/adapter/exponent/receiver/H trigger.
