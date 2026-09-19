# MB104 Z33A — span-five simple-contact orbit scan — 2026-09-19

Status: **PRE-AUDIT EXACT FINITE GEOMETRY / NO CREDIT**

## Input boundary

Use only:

- hostile-audited predecessor head `b28adadc95776762754e1415a0ecab0da1d4cd8e`;
- historical geometry archive `ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11`;
- the compact restart branch for current routing.

Z33 gives, in the potentially unbounded genus-one span-five sector,

```
M=R=O=d,
m_b=1 for every box-node branch,
div(nu^*h)=B_node reduced.
```

Thus every supported branch contributes hyperplane order exactly one.

## Local test

At an A1 box node use

```
x=p^2, y=pq, z=q^2.
```

The two Z14 distinguished non-diagonal landings are the two Satake-boundary tangent directions, corresponding to the `A<B` and `A>B` bins.

For a support hyperplane `h`:

1. if `dh` vanishes on the projective Zariski tangent space of the box surface at the node, then `h in m_node^2`; every branch with `m=1` has `ord_b(h)>=2), contradicting Z33. Such a node is not support-eligible.
2. otherwise the residual hyperplane factor cuts the exceptional P1. Count how many of the two distinguished boundary directions are zeros of that residual factor. Those fixed Z14 bins are forbidden by Z33.

The exact replay uses the retained 48-node Q(i) model and the 12 archived Aut(S) ambient-hyperplane orbits.

## Exact orbit table

```
orbit       inc  size   order>=2 nodes   fixed bins forbidden per order-1 node
I24-O4       24     4       0             24 x 0
I24-O24      24    24       0             24 x 0

I20-O48      20    48       0              8 x 0, 8 x 1, 4 x 2
I19-O48      19    48       3             16 x 0

I16-O3       16     3       0             16 x 2
I16-O24      16    24       0             16 x 1

I15-O256     15   256       0              9 x 0, 6 x 1

I14-O96      14    96       2             12 x 0
I14-O192A    14   192       0             14 x 0
I14-O192B    14   192       0             14 x 0
I14-O384A    14   384       0             10 x 0, 4 x 1
I14-O384B    14   384       0             10 x 0, 4 x 1
```

The incidence/orbit-size totals match the archived complete quotient.

## Incidence 24 result

For both incidence-24 orbits the two hyperplane-section tangent directions at every supported node avoid both Z14 distinguished directions.

So the first hoped-for mechanism does **not** occur:

```
hyperplane equality
=> one fixed A<B/A>B bin forbidden
```

is false on incidence 24.

Instead the hyperplane removes only non-boundary landing values. This is a finite static exclusion inside the free diagonal `(A,B)=(1,1)` lambda-line and therefore does not beat the archived static-landing wall.

The eight section conics are nevertheless all disjoint from the carrier on the resolution under Z33 equality. This gives extra numerical orthogonality / node-mass balance constraints, but uniform mass patterns remain feasible, so no tail closure is claimed from that observation here.

## Z14 collision refinement

Let

```
T = number of non-diagonal m=1 branches,
q = number of surviving distinguished fixed landing bins on the actual node support.
```

Branches sharing one surviving fixed bin contribute pairwise resolved intersection. Hence

```
Delta_exc >= T^2/(2q) - T/2          if q>0,
q=0 => T=0.
```

The finite orbit scan gives:

```
I20-O48:
  q <= 24,
  more sharply q_max(N)=min(N+8,24), 14<=N<=20.

I16-O3:
  q=0.
  Therefore every Z33 branch is diagonal and, since m=1,
  every branch has (A,B)=(1,1).

I16-O24:
  q=N,
  so Delta_exc >= T^2/(2N)-T/2.

I15-O256:
  q_max(N)=N+9 for N=14,15.

I14-O384A/B:
  q=24 for the full 14-node support.
```

For incidence 24 and the surviving incidence-19/14-192 sectors, this simple-contact scan does not improve the old `2N` fixed-bin count.

No population-wide degree cutoff follows from these inequalities because `T` can be zero and the diagonal nonzero `lambda` values remain free away from finitely many hyperplane roots.

## One exact elimination

The size-96 incidence-14 orbit is different.

Its ambient hyperplane contains exactly 14 box nodes. The exact local scan finds two nodes where the hyperplane has order at least two along every `m=1` branch. Z33 therefore forbids those two nodes from the support, leaving at most 12 eligible nodes.

But the audited BTVA entry for an unbounded genus-one family requires

```
N>=14.
```

Hence

```
I14-O96
```

cannot support the unbounded Z33 span-five sector.

This eliminates one of the five incidence-14 ambient orbits for arbitrary Z33 simple-contact populations, without assuming uniform exceptional coefficients.

## Disposition

The full 12-orbit simple-contact gate is now finite and exact.

What survives:

- both incidence-24 orbits;
- incidence 20;
- incidence 19 on at most 16 eligible nodes;
- both incidence-16 orbits, with strong branch-type restrictions;
- incidence 15;
- four of the five incidence-14 orbits.

What closes:

- incidence-14 orbit size 96.

Therefore simple-contact geometry sharpens the span-five population but does not close it.

The next shallow gate should use the new survivor structure rather than repeat finite-lambda or fixed-jet arguments. The two legitimate follow-ups are:

1. test whether the all-diagonal / reduced-fixed-bin sectors force primitive support-Hilbert growth or another global compatibility condition; or
2. park span-five simple-contact and move to the genus-one full-span P6 sector.

Do not return to N=10, bare etale correspondence finiteness, or fixed finite jet depth.

## Credit firewall

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
