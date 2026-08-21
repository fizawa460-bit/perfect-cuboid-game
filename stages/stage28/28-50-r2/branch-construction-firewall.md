# Stage28-50-r2 — branch-profile construction firewall

```text
ROUTE=L12_STAGE19_BRANCH_PROFILE_AS_CONSTRUCTION
STATUS=NEGATIVE_CERTIFICATE
TARGET=N2
PARENT_GEOMETRY=Stage28-40-r2
```

Checkpoint40-r2 proved that the Stage19 space double cover has four geometric rational `(1,1)` branch components, whereas the Stage20 third-face cover has two genus-one components.  A natural lower-side question is whether the four rational branch components themselves seed a denser Stage19 physical family.

They do not.

On the exact Stage19 space radicand, after multiplying the conjugate factors, the branch polynomial is represented on the real physical chart by a product of sums of squares:

\[
F_{sp}/4=
(u_1^2u_2^2+v_1^2v_2^2)
(u_1^2v_2^2+u_2^2v_1^2).
\]

For positive physical Pythagorean parameters every factor is strictly positive.  Thus the geometric branch divisor has no point on the positive real physical torus.  Its four rational components appear only after geometric factorisation over `Q(i)` and on boundary/complex loci; they are not a positive physical family of Stage19 objects.

Consequently

```text
SPACE_BRANCH_COMPONENTS_RATIONAL_GEOMETRICALLY=true
SPACE_BRANCH_POSITIVE_PHYSICAL_POINTS=false
BRANCH_LOCUS_SEEDS_N2_LOWER_FAMILY=false
```

This also prevents a false comparison in which `4 x genus0` is interpreted as automatically producing more rational physical lifts than `2 x genus1`.  Rational-point abundance on the branch divisor is not the same counting problem as rational lifts off the branch under the physical height.

A legitimate use of the branch-profile difference still requires the checkpoint40 receiver: a theorem comparing rational lifts of the two distinct double covers away from the branch under the common physical height.

```text
BRANCH_PROFILE_TO_CONSTRUCTION_SHORTCUT_REJECTED=true
N2_PROGRESS_GATE_ONE_QUARTER_UNCHANGED=true
AUDIT_REQUIRED=true
```
