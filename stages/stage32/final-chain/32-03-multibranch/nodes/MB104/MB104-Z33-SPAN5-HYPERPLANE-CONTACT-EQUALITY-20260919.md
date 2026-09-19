# MB104 — Z33: span-five hyperplane-contact equality and reduced branch divisor

Status: **RESEARCH CHECKPOINT / PRE-AUDIT / NO CREDIT**

## Purpose

The Z31/Z32 work moves the unbounded low-genus support frontier to `N>=14`.
For genus one, BTVA leaves two projective-span sectors: support spanning a hyperplane
`P^5`, and full-span `P^6`.

The span-five sector already has an exact finite ambient classification:

- 1,655 node-spanned hyperplanes containing at least 14 box nodes;
- 12 exact `Aut(S)` hyperplane orbits;
- the balanced hostile support `000707` lies in one of these hyperplanes.

This checkpoint adds a population-wide constraint that was not used in the previous
hyperplane classification: **if all box-node branches of a low-genus carrier lie over
one hyperplane, the hyperplane degree itself bounds the total exceptional contact
mass from above.**

For genus one, the retained lower bound gives equality everywhere.

## 1. Local A1 hyperplane-contact lemma

Let `s` be one of the 48 A1 box nodes and write the analytic surface germ as

```
xz=y^2.
```

On the `x`-chart of the minimal resolution,

```
y=xu,
z=xu^2.
```

A normalization branch with FSM exponents `A<=B` has exceptional contact

```
m=A=min(A,B).
```

Let `h` be the restriction of an ambient hyperplane passing through `s`.
Because `h` vanishes at the node, its germ belongs to the maximal ideal
`(x,y,z)`.  After pullback to the resolution every term is divisible by the local
exceptional parameter `x`:

```
h = x * q(x,u)
```

for a regular germ `q`.  Therefore along the normalization branch

```
ord_b(h) >= ord_b(x)=m.
```

The symmetric `z`-chart gives the same statement when `B<=A`.

Thus for every branch over a box node lying on the hyperplane,

```
ord_b(h) >= m_b.                              (HLOC)
```

No assumption on the landing parameter `lambda` is used.

## 2. Global upper bound M<=d

Let `C` be an integral nonexceptional low-genus carrier, `nu:Cbar->C` its
normalization, and let

```
d = H.C = deg nu^* O_X(H).
```

Assume every box node met by `C` lies in one ambient hyperplane `L`, and that
`C` is not contained in `L`.

The pulled-back hyperplane section `nu^*L` is an effective divisor of degree `d`.
Summing (HLOC) over every normalization branch above every met box node gives

```
d = deg div(nu^*h)
  >= sum_b m_b
  = M.                                        (HUP)
```

Hence

```
M<=d.                                         (Z33-HUP)
```

For the potentially unbounded span-five sector, the support spans the hyperplane.
The alternative that the carrier itself is contained in a node-spanned hyperplane is
already in the BTVA classified hyperplane-section low-genus sector and does not supply
the unbounded MB tail.  Z33 is therefore applicable to the active span-five Class-3
sector.

## 3. Genus-zero hyperplane-supported MB sector disappears

The retained multibranch lower bound gives

```
g=0: M>=d+4.
```

Together with (Z33-HUP),

```
d+4<=M<=d,
```

which is impossible.

Therefore an unbounded genus-zero MB carrier cannot have all of its node support in a
hyperplane.  This agrees with the BTVA full-span conclusion, but follows here directly
from the exact branch/contact bookkeeping.

## 4. Genus-one equality package

For genus one the retained lower bound is

```
M>=d.
```

Thus (Z33-HUP) forces

```
M=d.                                          (Z33-M)
```

The revived Z6 auxiliary inequality gives

```
O>=d,
```

where `O` is the number of odd-contact normalization branches.  Always

```
O<=R<=M.
```

Consequently

```
O=R=M=d.                                      (Z33-EQ)
```

Since every branch has `m_b>=1` and

```
M=sum_b m_b = R,
```

every branch has

```
m_b=1.                                        (Z33-SIMPLE)
```

Hence every branch is transverse to its exceptional curve.  Because `m=1` and
`A+B` is even, the diagonal branches are exactly the FSM-minimal type
`(A,B)=(1,1)`; every other branch is non-diagonal with one exponent equal to one.

This is substantially stronger than merely knowing a lower bound on the number of
odd branches.

## 5. The hyperplane section is exactly the reduced node-branch divisor

The inequalities above are equalities branch by branch.

Indeed `nu^*L` has degree `d), while there are exactly

```
R=d
```

normalization branches over the box nodes and every one contributes at least one zero
of the hyperplane section.  Therefore there is no degree left for any additional
intersection and no branch can contribute order greater than one.

Let

```
B_node = sum_{b over box nodes} [b]  on Cbar.
```

Then `B_node` is reduced, has degree `d`, and

```
div(nu^*h) = B_node,                           (Z33-DIV)
nu^* O_X(H) ~= O_Cbar(B_node).                 (Z33-LINE)
```

Consequences:

1. the carrier meets the support hyperplane nowhere away from the node-preimages;
2. at every node branch the strict-transform residual hyperplane factor is nonzero at
   the landing point;
3. the entire hyperplane degree is exhausted by the node branches;
4. for genus one, the node-preimage divisor is a complete degree-`d` representative
   of the canonical hyperplane line bundle on the normalization.

The previous static-landing wall remains valid: statement (2) forbids only the finite
landing set cut by the hyperplane on each exceptional `P^1`; it does not by itself
bound the free diagonal `lambda` values.

## 6. Equality in the Beauville/product-cover estimate

Because every branch has odd contact and `O=d`, the revived Z6 Riemann--Hurwitz chain

```
q'(4g-4+O)
 >= 8 max(n1,n2)
 >= 4(n1+n2)
 = q'd
```

is an equality for `g=1`.

Hence on every relevant connected product-cover component,

```
n1=n2=q'd/8
```

and each nonconstant projection to `X(8)` is etale.

This does **not** reopen H5/U10: bare equal-degree etale correspondences of `X(8)`
were already shown to form an unbounded arithmetic commensurator universe.  The new
information in Z33 is the preceding branch/contact and reduced-divisor equality,
not correspondence existence by itself.

## 7. What Z33 changes in the span-five search

The old span-five finite reduction classified ambient hyperplanes but still allowed
arbitrary positive exceptional coefficients and arbitrary branch contact masses.

For an unbounded genus-one span-five MB carrier, Z33 now replaces that population by

```
one of the 12 node-hyperplane Aut(S) orbits,
plus
M_i=r_i=number of branches at node i,
sum_i M_i=d,
every branch m=1,
B_node=div(nu^*h) reduced.
```

Thus unequal node populations remain possible, but **higher contact multiplicity is
gone completely**.

This makes the next finite-geometry question sharper:

> for each of the 12 hyperplane orbits, can an irreducible genus-one carrier have a
> reduced node-branch divisor exhausting its hyperplane degree while satisfying the
> component geometry of the hyperplane section?

The incidence-24 orbits are the first test because their hyperplane sections are
already known exactly as unions of eight smooth conics.  The previous fixed-component
argument handled only the uniform ray; Z33 supplies the missing simple-contact
constraint needed to revisit arbitrary unequal branch populations without assuming
uniform coefficients.

## 8. Optional N=14 delta checksum

At `N=14`, `M=d` gives by Hodge and Cauchy

```
Delta_total <= d/2 + 3d^2/224.
```

If `T` is the number of non-diagonal branches, Z14-COLL gives

```
T^2/56 - T/2 <= Delta_total,
```

hence

```
T <= 14 + (1/2)*sqrt(3d^2+112d+784).
```

Since all contacts are one, the remaining branches are FSM-minimal and

```
R8=d-T.
```

Asymptotically this yields

```
R8/d >= 1-sqrt(3)/2+o(1).
```

This is only a checksum; the retained FSM pole inequality already gives the stronger
population-wide genus-one bound `R8>=d/4`.  No credit is claimed from the weaker
N=14 estimate.

## Decision

```
SPAN5_HYPERPLANE_CONTACT_UPPER_BOUND = M<=d
GENUS0_MB_HYPERPLANE_UNBOUNDED_SECTOR = EMPTY_PRE_AUDIT
GENUS1_SPAN5_EQUALITY = M=R=O=d
GENUS1_SPAN5_ALL_BRANCH_CONTACTS = m=1
GENUS1_SPAN5_NODE_DIVISOR = div(nu^*h)=B_node_REDUCED
BARE_ETALE_CORRESPONDENCE_ROUTE_REOPENED = false
NEXT_TARGET = SPAN5_HYPERPLANE_ORBIT_COMPONENT_GEOMETRY_WITH_SIMPLE_CONTACT
MB104_COMPLETE = false
FINITE_DEGREE_WINDOW_PROVED = false
R29_LG2_MB_DISCHARGED = false
RECEIVER_CREDIT = false
THEOREM_CREDIT = false
ENDPOINT_CREDIT = false
MERGE_AUTHORIZED = false
```

## Source boundary

Current retained inputs:

- `MB101/CERTIFICATE.json`, blob `282fc94d8d5feb0221cf6bf096ed4b0030883563`;
- `MB102/CERTIFICATE.json`, blob `f852f66c67343b6a553b5c20e15dc0a0f55d5226`;
- `MB104-Z-REVIVED-DEEPENING-PASS-2-20260919.md`, blob
  `1ea3003c1587d94a9301fe08f50c0c97a529b85f`;
- `MB104-Z32-N14-SUPPORT-HILBERT-GATE-20260919.md`, blob
  `79fb7ae150f7a25d86426d6c5944894b9f690927`.

Historical exact span-five classification remains frozen at the archived MB104 surface;
Z33 does not rewrite or promote it.

All statements here remain pre-audit research and grant no downstream credit.
