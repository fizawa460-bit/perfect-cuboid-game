# MB104 Z33D — balanced16 four-orbit exceptional-landing gate — 2026-09-19

Status: **PRE-AUDIT EXACT LOCAL-LANDING NO-GO / NO CREDIT**

## Inputs

The archived uniform-ray quotient leaves exactly four balanced incidence-16 support orbits:

```text
0000770000ff   orbit 48
00007b0000ff   orbit 48
000707000f0f   orbit 768
00070b000f0f   orbit 768
```

with zero-pairing elliptic-quartic profiles

```text
orbit 48 : 4 zero quartics; every supported node lies on exactly 2
orbit 768: 2 zero quartics; every supported node lies on exactly 1.
```

Z33/Z33A further give `m=1` for every supported branch and:

```text
I16-O3  : both distinguished non-diagonal boundary bins forbidden,
           hence every branch is diagonal (A,B)=(1,1);

I16-O24 : one distinguished non-diagonal boundary bin forbidden
           at every supported node.
```

## Zero-pairing consequence

For a zero-pairing elliptic quartic `Q` and a hypothetical irreducible carrier `C in |lP|`,

```text
C.Q = 0.
```

Since `C` and `Q` are distinct effective irreducible curves on the smooth resolution, they must be disjoint there. Therefore any exceptional landing point occupied by the strict transform of `Q` at a shared box node is forbidden to branches of `C`.

This is a genuine local restriction.

## Why the restriction does not close any of the four orbits

At each fixed supported node, only finitely many zero-pairing elliptic quartics occur:

```text
orbit-48 supports  : 2 through the node,
orbit-768 supports : 1 through the node.
```

Each fixed proper transform meets the exceptional `P1` in a finite set. Hence the total set of landing points forbidden by all zero-pairing quartics through that node is finite.

Z33A, however, does not discretize the diagonal `m=1` landing locus. In the A1 chart

```text
x=p^2, y=pq, z=q^2,
```

the two distinguished non-diagonal bins are the two boundary endpoints of the exceptional `P1`. The diagonal `(A,B)=(1,1)` branches retain the open `G_m` family of nonzero finite landing parameters `lambda=q/p`.

The support hyperplane removes at most its own residual root on the exceptional line. Adding one or two zero-quartic landing sets still removes only finitely many points from this infinite diagonal locus.

Therefore, even in the strongest I16-O3 case,

```text
allowed diagonal landing locus
  = G_m minus a finite set
```

remains nonempty and infinite.

For I16-O24 the conclusion is weaker still: one distinguished non-diagonal bin survives in addition to the diagonal open locus.

Thus zero-quartic disjointness cannot by itself exclude any of the four support orbits.

## Important scope

This is a **local landing-only no-go**. It does not construct a global carrier and does not prove that arbitrary collections of nodewise landing choices globalize to an algebraic curve.

What it proves is that no contradiction can be obtained solely by saying:

```text
C.Q=0 for the retained zero quartics
+ Z33A forbids one/two distinguished boundary directions.
```

A successful continuation must impose a global relation coupling landing divisors across nodes.

## Next route

```text
MB104-Z33E-NULL-LOCUS-CONTRACTION-GLOBAL-COUPLING-PREFLIGHT
```

Target: use the big-nef class `P` and its `P.Q=0` elliptic quartics / exceptional null curves globally. Determine whether the null-locus contraction or the restriction of `lP` to the negative-definite null configuration forces cross-node conditions stronger than independent finite landing avoidance.

Stop if the contraction merely records that a carrier in `|lP|` avoids the null curves without additional divisor-class constraints.

## Source locks

Historical archive head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md` blob
  `1dfafccb9559c98ccf71cc4b98449d784941d48f`;
- certificate blob
  `f63d08b9005762a02935a727f35e6581ae52aaab`.

Current compact branch:

- Z33A note blob `2483de9c5c4da33e331f0b5b75ceb96f7304411d`;
- Z33A certificate blob `fc66b5df676660798417e11f194b68e950f3bc98`;
- Z33C routing note blob `0aacb7b0b1ff91d5337c77017e0af6ddba3a29d3`.

## Firewalls

```text
any_balanced16_orbit_excluded=false
global_carrier_constructed=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
