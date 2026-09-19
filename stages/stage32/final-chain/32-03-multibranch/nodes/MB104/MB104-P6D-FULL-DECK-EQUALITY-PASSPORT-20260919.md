# MB104 P6D — full-span equality packet / full-deck passport — 2026-09-19

Status: **PRE-AUDIT CONDITIONAL EXACT REDUCTION / NO CREDIT**

## Target

Use the current full-span hostile support

```
Sigma = 0000093f442e
nodes = {1,2,3,5,10,14,16,17,18,19,20,21,24,27}.
```

This leaf is conditional on an actual genus-one carrier realizing the equality-shaped packet

```
D_l = 7lH - 4l sum_(p in Sigma) E_p,
d=112l,
r_i=M_i=8l at all 14 nodes,
all branches (A,B)=(1,1), m=1,
R8=r_odd=M=d=112l.
```

The leaf does not claim such a carrier exists and does not promote this packet to every P6 carrier.

## Node-type replay

The three Beauville singular-stabilizer types are read from the unique zero among

```
b1,b2,b3.
```

For the current support the exact counts are

```
(b1=0,b2=0,b3=0) = (6,2,6).
```

All three distinct outside involutions therefore occur.

## Equality rigidity survives outside P5

The retained Beauville equality argument uses only

```
g=1,
r_odd=d,
```

not the existence of a support hyperplane.

Let `Y` be the normalized connected Beauville double-cover pullback. Then

```
g(Y)=56l+1.
```

Pull `Y` back to

```
P=C8 x C8 -> X=P/G0,
G0 ~= (Z/2)^2.
```

For a connected component `Z`, equality in the product-cover Riemann--Hurwitz bounds forces both projections

```
Z -> C8
```

to be etale.

## Three node types force the full deck stabilizer

At an odd branch point of node type `s in G\G0`, the corresponding singular stabilizer fixes the full four-point `P->X` fiber. Therefore every connected component of the etale pullback is stabilized by every node-stabilizer type occurring in the support.

The current support contains all three outside involutions. Three distinct elements of the nonzero coset of the index-two plane `G0 < G~=(Z/2)^3` generate all of `G`.

Consequently every connected component is stabilized by all of `G0`, and the component degree is forced to

```
e=4.
```

Thus the product pullback is connected and

```
g(Z)=224l+1,
Z -> C8 has degree 56l on each factor,
both factor maps are etale,
Z/G = E
```

where `E` is the original genus-one normalization.

This is a genuine strengthening relative to a generic equality packet: the `e=1,2` cases disappear.

## Six-branch-value quotient passport

Quotient either factor by the full `G):

```
C8/G ~= P1.
```

The quotient has six order-two branch values, two for each node-stabilizer type.

The induced genus-one map has degree

```
phi:E -> P1,
deg phi = 56l.
```

For a branch value `q`, write

```
u_q = number of unramified points above q,
r_q = number of simple ramification points above q.
```

Then

```
u_q+2r_q=56l.
```

Riemann--Hurwitz on `E` gives

```
sum_q r_q=112l,
sum_q u_q=112l.
```

Every one of the `112l` supported odd/minimal normalization points is unramified over one of the six branch values, so they exhaust the unramified capacity.

The current node-type totals therefore give exactly

```
type pair             sum u_q       sum r_q
b1=0                    48l           32l
b2=0                    16l           48l
b3=0                    48l           32l
```

This coarse passport is numerically compatible. For example the symmetric split

```
u = (24,24,8,8,24,24)l,
r = (16,16,24,24,16,16)l
```

satisfies every retained scalar Hurwitz condition.

No existence of a cover with this exact tuple is claimed by that numerical witness.

## Why the old U12 spin lever disappears

The old `000707` packet had seven supported nodes of one type on a retained zero quartic. Since each node carried `8l` branches,

```
7*8l = 56l
```

filled one entire reduced Weierstrass fiber of a degree-`56l` etale factor map. That exact divisor equality produced the unsquared theta/spin relation used by U12.

The current support has type counts

```
(6,2,6).
```

Even under maximal concentration of all nodes of one type into one branch value, the supported unramified contribution is at most

```
6*8l = 48l < 56l.
```

Thus no node type can force complete Weierstrass-fiber saturation.

The retained packet therefore does **not** imply an equality of the form

```
p_2^* O(w0) ~= p_1^* O(w1)
```

or another unsquared odd-theta equality by the old argument.

This matters because the bare Bolza/commensurator degree route is already known to allow infinitely many degrees of the form `56l`. The old packet-sensitive U12 lever does not transfer to this P6 support.

## Disposition

For the current equality packet:

```
all three node types        -> e=4 forced
full product pullback       -> connected
factor maps                 -> etale, degree 56l
six-value Hurwitz passport  -> compatible at scalar level
old unsquared-spin lever    -> not forced
packet excluded             -> false
whole P6 closed             -> false
```

So the equality/product-cover route has been sharpened but does not close this hostile P6 packet.

A further arithmetic correspondence search is not justified unless a **new packet-sensitive condition** is produced. Bare degree/index or generic etale-correspondence existence must not be reopened.

## Source locks

Historical archive exact head:

```
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- equality-rigidity certificate blob `62a2d01447016731001d35cc5915880daa2bfada`;
- full-deck stabilizer certificate blob `1c03b78456a704e50f8af0640e1d23dc36948a3c`;
- six-branch passport note blob `d421c11ecd6577234823b6e9604c8cc99ce48fec`;
- node-stabilizer source note blob `a29161602c0b38f0607794e56e61068b8cb9735d`.

Current compact restart:

- P6A certificate blob `ab16e0757607c702fbc548dd9393d16d6c5f899b`;
- P6C certificate blob `fbbf357fddb9a482385e30098649bdaf0d64a3eb`.

## Firewalls

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
