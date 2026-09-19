# MB104 Z5' — exact factor X(4)-cusp pair adapter and hostile 2x2 incidence — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT MODULAR ADAPTER / PACKET REOPEN / NO CREDIT**

## Purpose

Reopen the original Z5' packet-sensitive arithmetic/product route.

P6N/P6O parked because the retained sources identified only the three inertia types and did not
supply

```text
box node -> (individual branch value in factor 1,
             individual branch value in factor 2).
```

The published theta parametrization actually contains enough invariant bilinear data to recover the
two factor cusp coordinates separately.

## 1. Single-factor X(4) coordinate

Freitag--Salvati Manni use the five single-factor theta forms

```text
a = theta00(z),
b = theta10(z),
c0 = theta01(z),
d = theta00(2z),
e = theta10(2z),
```

with relations

```text
a^2  = d^2+e^2,
c0^2 = d^2-e^2,
b^2  = 2de.
```

The quotient by Gamma[4]/Gamma[8] has genus zero.  Use the projective coordinate

```text
t=[d:e] on X(4) ~= P1.
```

The six order-two branch/cusp values are

```text
t in {0, infinity, +1, -1, +i, -i}.
```

They group by the vanishing theta coordinate:

```text
theta10=0 -> {0,infinity},
theta01=0 -> {+1,-1},
theta00=0 -> {+i,-i}.
```

## 2. Recovering both factor coordinates from box invariants

The box convention is

```text
(a1,a2,a3,b1,b2,b3,c)=(W1,W2,W3,Z1,Z2,Z3,C).
```

The theta parametrization gives, writing factor coordinates (d_z,e_z) and (d_w,e_w),

```text
A = d_z d_w = (C+W3)/2,
B = e_z e_w = (C-W3)/2,
U = e_z d_w = (W1-i W2)/2,
V = d_z e_w = (W1+i W2)/2.
```

This is the complete rank-one outer-product matrix

```text
[ A  V ]   [d_z] [d_w e_w]
[ U  B ] = [e_z].
```

Therefore the two X(4) coordinates are recovered projectively by

```text
t_z=[d_z:e_z]=[A:U] whenever that column is nonzero,
                  =[V:B] otherwise,

t_w=[d_w:e_w]=[A:V] whenever that row is nonzero,
                  =[U:B] otherwise.
```

Equivalently away from poles,

```text
t_z=(c+a3)/(a1-i a2),
t_w=(c+a3)/(a1+i a2).
```

No square-root choice is involved.

## 3. Exact replay on the retained 48-node model

Apply the formulas to the canonical ordered 48-node model used by the archived Stage32 verifiers.

The result consists of exactly twelve factor-cusp cells, each containing four box nodes:

```text
b1=0 / theta01 type:
(+1,+1), (+1,-1), (-1,+1), (-1,-1), each size 4.

b2=0 / theta00 type:
(+i,+i), (+i,-i), (-i,+i), (-i,-i), each size 4.

b3=0 / theta10 type:
(0,0), (0,infinity), (infinity,0), (infinity,infinity), each size 4.
```

Thus the desired P6N factorwise branch-value refinement exists as an exact rational adapter.

## 4. Hostile support exact 2x2 matrices

For the P6 hostile support

```text
Sigma={1,2,3,5,10,14,16,17,18,19,20,21,24,27}
```

in the retained zero-based node indexing, the exact cell counts are:

### b1=0 / values (+1,-1)

Rows are factor-1 (+1,-1), columns factor-2 (+1,-1):

```text
[3 0
 2 1]
```

Total: 6 nodes.

### b2=0 / values (+i,-i)

Rows are factor-1 (+i,-i), columns factor-2 (+i,-i):

```text
[0 1
 1 0]
```

Total: 2 nodes.

### b3=0 / values (0,infinity)

Rows are factor-1 (0,infinity), columns factor-2 (0,infinity):

```text
[2 0
 0 4]
```

Total: 6 nodes.

The totals recover the retained inertia counts (6,2,6).

## 5. Individual six-value unramified passports

Every supported node carries 8l unramified normalization branches in the equality packet.

Hence factor-1 individual unramified fiber counts are

```text
b1 pair: (24l,24l),
b2 pair: ( 8l, 8l),
b3 pair: (16l,32l).
```

Factor-2 counts are

```text
b1 pair: (40l, 8l),
b2 pair: ( 8l, 8l),
b3 pair: (16l,32l).
```

Since each fiber has degree 56l and all remaining points over a branch value are simply ramified,

```text
u_q + 2 r_q = 56l,
```

the individual ramification counts are therefore:

factor 1
```text
(16l,16l), (24l,24l), (20l,12l);
```

factor 2
```text
( 8l,24l), (24l,24l), (20l,12l).
```

Each factor sums to 112l ramification points as required.

## 6. What this does and does not prove

This removes the P6N/P6O source-interface wall.

It does not by itself contradict Hurwitz or prove nonexistence of the two pencils.  The scalar and
typewise totals remain compatible.

The genuinely new packet data are:

- the exact twelve-cell node partition;
- the asymmetric individual b1 passport between the two factors;
- the exact common supported-point incidence inside the 6x6 branch-value grid.

Any next Z5' step must use this finer grid data rather than returning to type totals or generic
Kummer/Nielsen equivalence.

## Source anchors

Published:
- E. Freitag, R. Salvati Manni, *Parametrization of the box variety by theta functions*,
  Michigan Math. J. 65 (2016), Theorems 2.1 and 2.4.

Retained archive:
- `AUTS-NODE-ACTION-SOURCE-NOTE.md` blob
  `cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693`;
- `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md` blob
  `a29161602c0b38f0607794e56e61068b8cb9735d`;
- canonical node enumeration in
  `verify_mb104_genus1_span5_known_conic_balanced_quotient.py`
  blob `fe55e8a7bcd5b790f8d65419a9a88ba59106ba54`.

## Firewalls

```text
factorwise_branch_label_adapter_constructed=true
P6N_incidence_reopened=true
hostile_2x2_incidence_exact=true
new_packet_obstruction=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
