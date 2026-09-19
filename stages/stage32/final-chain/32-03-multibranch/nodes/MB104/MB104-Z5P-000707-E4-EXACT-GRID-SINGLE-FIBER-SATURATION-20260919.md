# MB104 Z5' — 000707 e=4 exact grid and single-fiber saturation — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT PACKET REFINEMENT / NO CREDIT**

## Scope

Use the exact factor X(4)-cusp adapter on the dangerous equality-packet support

```text
Sigma=000707000f0f.
```

This note concerns the `e=4` case, where

```text
E=Z/G,
phi_1,phi_2:E->C8/G ~= X(4) ~= P1,
deg phi_i=56l.
```

Each supported node contributes exactly `8l` distinct unramified normalization points.

## Exact 14-node cell table

In the canonical 48-node ordering, the support is

```text
{0,1,2,3,8,9,10,11,24,25,26,32,33,34}.
```

The factor-cusp adapter assigns:

```text
nodes 0,1,2,3       -> ( 1,  1)
nodes 8,9,10,11     -> ( i, -i)
nodes 24,25,26      -> (-1,  1)
nodes 32,33,34      -> ( i,  i)
```

and no other branch-value cell is occupied.

Thus the four occupied cell masses are

```text
32l, 32l, 24l, 24l.
```

## Individual six-value passports

Order the values as

```text
(1,-1,i,-i,0,infinity).
```

The unramified counts are

```text
factor 1: (32,24,56,0,0,0)l,
factor 2: (56,0,24,32,0,0)l.
```

Therefore the simple-ramification counts are

```text
factor 1: (12,16,0,28,28,28)l,
factor 2: (0,28,16,12,28,28)l.
```

## Two exact single-fiber saturations

For factor 1, the seven nodes

```text
{8,9,10,11,32,33,34}
```

all have branch value `+i`.  Their normalization points total

```text
7*8l=56l=deg(phi_1).
```

Since they are distinct and unramified, they are the whole reduced fiber:

```text
phi_1^{-1}(i)
 = supported divisor on those seven nodes.
```

Likewise, for factor 2 the seven nodes

```text
{0,1,2,3,24,25,26}
```

all have branch value `+1`, so

```text
phi_2^{-1}(1)
 = supported divisor on those seven nodes.
```

This upgrades the archived pair-of-values saturation to **one exact X(4) fiber in each factor** in
the e=4 case.

## Relation to the two zero quartics

The retained zero-quartic node sets are

```text
Q0 nodes = {0,1,2,3,24,25,26,27},
Q1 nodes = {8,9,10,11,32,33,34,35}.
```

Hence

```text
Sigma cap Q0 = factor-2 saturated +1 fiber nodes,
Sigma cap Q1 = factor-1 saturated +i fiber nodes.
```

So the two zero-quartic seven-node packets are now individually identified with exact factor
branch values.

## Consequence

The remaining e=4 problem has strictly finer simultaneous data than the archived typewise packet:

```text
phi_1^{-1}(i)  = one seven-node packet,
phi_2^{-1}(1)  = the other seven-node packet,
and the joint 12-cell pairing is exact.
```

This does not by itself contradict the existence of the two maps.  The accompanying one-factor
Hurwitz-feasibility note proves that each individual six-value passport remains realizable for all
l.

Any further Z5' progress must use the **simultaneous** placement of these two saturated fibers in
the same common G-cover / joint correspondence.

## Firewalls

```text
e4_single_fiber_saturation_exact=true
e2_single_H_quotient_value_saturation_not_claimed=true
e4_excluded=false
two_factor_common_cover_realized=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
