# Dual four-quadric web — exact adapter screen

Let the four endpoint quadrics be

```text
Q1 = a1^2+a2^2-b3^2
Q2 = a2^2+a3^2-b1^2
Q3 = a1^2+a3^2-b2^2
Q4 = a1^2+a2^2+a3^2-c^2.
```

For `[t1:t2:t3:t4] in P3`, the web member `t1 Q1+t2 Q2+t3 Q3+t4 Q4` is diagonal with coefficients

```text
a1^2 : t1+t3+t4
a2^2 : t1+t2+t4
a3^2 : t2+t3+t4
b1^2 : -t2
b2^2 : -t3
b3^2 : -t1
c^2  : -t4.
```

Hence the discriminant is, up to a nonzero scalar,

```text
t1*t2*t3*t4
*(t1+t3+t4)
*(t1+t2+t4)
*(t2+t3+t4)=0.
```

This is an exact seven-plane arrangement in the dual parameter `P3`.

## Rank-stratum audit candidate

The committed dependency-free checker establishes:

```text
rank<=4 locus: 17 projective points, no positive-dimensional component
rank<=3 locus: exactly 6 points, all rank exactly 3
```

Thus the classical Adler–van Moerbeke route in which a special four-quadric intersection compactifies to an Abelian surface because the web contains a nondegenerate curve / union of lines of rank-<=4 quadrics does not trigger here.

## Clifford screen

The universal quadric over this `P3` is generically a rank-7 quadratic form. Even-Clifford technology is available for quadric fibrations, but the especially sharp rank-4 quadric-surface criterion

```text
Clifford Brauer class trivial <=> rational section
```

cannot be transplanted to this rank-7 family by analogy. A common endpoint point would indeed give a constant isotropic line for every web member, but a nontrivial rank-7 Clifford invariant is not by itself certified here to exclude isotropy.

Therefore:

```text
R29-QWEB0=EXACT_DUAL_WEB_ADAPTER
R29-QWEB1=EXACT_RANK_STRATA
R29-QWEB-ABELIAN=RED_NO_RANK4_CURVE
R29-QWEB-CLIFFORD=AMBER_NEEDS_NEW_ISOTROPY_OBSTRUCTION_THEOREM
INDEPENDENT_FOUNDATION=false
```

## Relation to existing foundations

This dual web is a genuinely useful second coordinate picture of the F1 complete intersection, but its seven coefficient hyperplanes and six deepest rank points strongly reflect the already-audited F7 sign/line combinatorics. Until it creates an arithmetic receiver not expressible inside F1/F7, it is an adapter, not a ninth foundation.
