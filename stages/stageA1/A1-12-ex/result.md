# StageA1 A1-12-ex — independent certification of the 384-class exclusion

## Purpose

This is a **separate verification line**. It does not advance A1-13 and does not modify the StageA1 controller.

The only question here is:

> Is it really proved that, inside the corrected Bremner–Elsholtz–Ulas equation-(6) family, any nondegenerate perfect-cuboid candidate must have its elliptic multiplier `n` in the A1-12 set of 384 residue classes modulo `3416490`?

A1-12-ex rederives the implication by a route that is deliberately more direct than the A1-8/A1-12 presentation and independently recomputes the finite-field sieve and the final residue set.

## The family-specific theorem being certified

Let a nondegenerate rational anchored member of equation (6) survive all conditions necessary to be a perfect-cuboid candidate. Put

```text
x=c/d,
k=x^2,
z=k+1/k.
```

Then, necessarily,

```text
z+2=(x+1/x)^2,
z-2=(x-1/x)^2.
```

Thus the two square-coordinate conditions used by A1-12 are not heuristic filters: they are exact necessary conditions for every nondegenerate equation-(6) candidate.

The corrected anchor discriminant from A1-3 gives a rational point on

```text
Q(z)=v^2,
Q(z)=z^4-20z^2+256z-412.
```

The quartic is birational to

```text
E: y^2=x^3+x^2+95x+703
```

by

```text
z=-(y+32)/(x-3),
v=2x+4-z^2,
```

with inverse

```text
x=(v+z^2-4)/2,
y=-z(x-3)-32.
```

Official LMFDB data for `6080.r1` records rank `1`, trivial torsion, and Mordell–Weil generator `(3,32)`. Therefore

```text
E(Q)=Z P,  P=(3,32),
```

so every rational quartic point is represented by an integer multiplier `n` (with the two points at infinity handled by the birational exceptional chart).

For each selected good prime `p`, reduction modulo `p` is a group homomorphism. If `nP` has finite `z`-reduction and both rational numbers `z+2` and `z-2` are squares over `Q`, their reductions are quadratic residues or zero in `F_p`. If the reduction is a pole of the `z` map, the corresponding residue class is retained rather than discarded. Hence no genuine rational survivor is lost through denominator/pole handling.

Independent finite-field recomputation gives

```text
p     ord(P mod p)     necessary n classes
7          9           {0,1,2,-1}
23        29           {0,1,2,-1}
37        10           {0,1,2,-1}
257       22           {0,1,2,-1}
263       34           {0,1,2,-1}
863       21           {0,1,2,-1}
```

Therefore every equation-(6) candidate satisfies all six congruence restrictions simultaneously.

Let

```text
M=lcm(9,29,10,22,34,21)=3416490.
```

A1-12-ex does **not** trust the CRT-merging implementation from A1-12 for the final count. It independently scans every residue

```text
0 <= n < 3416490
```

and keeps exactly those satisfying all six displayed congruence tests. The result is exactly

```text
384
```

residue classes, with sorted-list SHA-256

```text
63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874.
```

Thus the exact certified implication is:

```text
nondegenerate equation-(6) perfect-cuboid candidate
    => n mod 3416490 lies in S_A1_12
    => |S_A1_12|=384.
```

Equivalently:

> **Inside this specific equation-(6) family, every multiplier class outside the 384-class set is rigorously excluded from producing a perfect cuboid.**

This is an all-integers congruence statement, not a bounded-height search.

## What still depends on an external certified Mordell–Weil computation

The finite-field sieve and the 384-class count are elementary and independently reproducible. The global step saying that **every** rational quartic point is `nP` uses the completeness of the Mordell–Weil description

```text
E(Q)=Z(3,32).
```

A1-12-ex therefore treats this as the single most important external dependency and checks it in two ways:

1. official LMFDB `6080.r1`: rank `1`, trivial torsion, generator `(3,32)`;
2. a separate Sage/eclib computation with database lookup disabled and proof mode enabled, requiring a proved rank and proved generators.

The Sage verification must report that the generator set is certain. If that certified computation fails, A1-12-ex does **not** promote the 384 theorem beyond the LMFDB-backed status.

## Scope firewall

This theorem is still **family-specific**. A1-3 proved that equation (6) is not known to be a universal reverse parametrization of arbitrary perfect cuboids. Therefore A1-12-ex does not claim

```text
arbitrary perfect cuboid => one of these 384 n-classes.
```

It certifies only

```text
equation-(6) candidate => one of these 384 n-classes.
```

No perfect-cuboid existence or nonexistence conclusion is made.

```text
A1_12_EX_TARGET=INDEPENDENT_384_CLASS_CERTIFICATION
A1_12_EX_CONTROLLER_CHANGED=false
A1_12_EX_FAMILY_SPECIFIC_ONLY=true
A1_12_EX_FULL_RESIDUE_SCAN_SIZE=3416490
A1_12_EX_SURVIVING_CLASSES=384
A1_12_EX_SHA256=63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874
A1_12_EX_GLOBAL_MW_DEPENDENCY=E(Q)=Z(3,32)
A1_12_EX_ARBITRARY_CUBOID_COVERAGE_PROVED=false
```
