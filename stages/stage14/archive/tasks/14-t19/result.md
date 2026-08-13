# Stage14-t19 — conditioned discriminant identity and finite collision ledger

## Purpose

Stage14-t18 proposed instantiating the squareclass packet on the exact physical point ledger. Doing that carefully reveals an important conditioning boundary: the `x` used by the t14--t18 quotient is **not** the raw elliptic `x` coordinate recorded by s4a. One must first condition the t12 reciprocal quadratic on an actual raw physical point `(t,q)`.

That conditioning collapses the apparent new discriminant gate to the original missing-face square condition.

## Exact identity

Let `t=X/S` be the first-face slope and let the raw partner have half-angle

\[
q=\frac{X_2}{H_2+S_2},\qquad
u=\frac{X_2}{S_2}=\frac{2q}{1-q^2}.
\]

The already-existing raw point satisfies

\[
R^2=q^4+2\frac{1-t^2}{1+t^2}q^2+1.
\]

After t12, the quotient variable `x=r^2` obeys a reciprocal quadratic. If `Delta_x` denotes its discriminant, direct simplification gives

\[
\boxed{
\Delta_x=
\left(
\frac{t(1+t^2)(1-q^2)R}{q^2}
\right)^2
(t^2+\nu^2).
}
\]

Therefore

\[
\boxed{[\Delta_x]=[t^2+\nu^2]\in\mathbf Q^\times/\mathbf Q^{\times2}.}
\]

Under the primitive shared-edge gluing, `t^2+nu^2` is the missing third-face squared length divided by the square of the shared edge. Hence `Delta_x` is a rational square if and only if the missing face diagonal is rational. Since the actual cuboid sides are integers, rational square root of that integer squared-length is automatically integral.

So, **conditioned on an actual raw two-face object, the t12 discriminant-square gate is exactly the triple/third-face gate in another coordinate system.** It is not a new independent thinning factor.

This does not invalidate the unconditioned genus-3 / elliptic-quotient / branched-cover geometry from t13--t18. It fixes how that geometry may be used after conditioning on the raw Stage14 ledger.

## Exact finite ledger through B=2,000,000

The deterministic audit regenerates all 356 frozen exactly-two objects and both orientations of their raw pair incidences, giving 712 conditioned checks.

At every frozen cutoff:

```text
B          objects M   distinct missing-face classes   Q=sum n_c^2
1,000             2                 2                        2
2,000             5                 5                        5
5,000            15                15                       15
10,000           25                25                       25
20,000           42                42                       42
50,000           62                62                       62
100,000          89                89                       89
200,000         116               116                      116
500,000         188               188                      188
1,000,000       255               255                      255
2,000,000       356               356                      356
```

Thus the object-level missing-face squareclass is injective on the entire frozen finite census. The only duplication at oriented-incidence level is the forced two orientations of the same raw pair object.

At `B=2,000,000`:

```text
raw exactly-two objects                    356
conditioned oriented incidences             712
conditioned discriminant-square hits          0
conditioned C0 entries                        0
object squareclasses                        356 distinct
maximum object-class multiplicity             1
collision energy Q                           356
Q/M                                            1
observed prime-coordinate union rank          554
finite Fourier/Cauchy diagnostic bound   18.8679622641
```

The exact compact object ledger is frozen by SHA-256

```text
f6f86ab2509aabc2c0ebc59bf20d1d4d9df984b4218ec26f7bd350543c89c8f0
```

The zero conditioned `C0` population is only a finite statement: it is another exact expression of the already-known `T(B)=0` through `2m`, not a nonexistence theorem.

## Collision target replacing the naive t19 packet experiment

For an exactly-two object `O`, let

\[
\kappa(O)=[L_{miss}(O)]\in\mathbf Q^\times/\mathbf Q^{\times2}
\]

be the squareclass of its missing-face squared length, and define

\[
Q_\Delta(B)=\sum_c n_c(B)^2
=\#\{(O_1,O_2):d_i\le B,\ \kappa(O_1)=\kappa(O_2)\}.
\]

Since every triple lies in the trivial class,

\[
T(B)^2\le Q_\Delta(B).
\]

Consequently the clean sufficient target

\[
\boxed{Q_\Delta(B)=o(B)}
\]

would already imply

\[
T(B)=o(\sqrt B).
\]

This collision formulation avoids pretending that the conditioned discriminant and the missing-face square condition are two separate gates. The finite data are unusually clean (`Q_Delta=M` at all 11 cutoffs), but no asymptotic collision theorem is inferred from that observation.

## Boundary

```text
STAGE14_T19=COMPLETE_CONDITIONED_DISCRIMINANT_IDENTITY_AND_FINITE_COLLISION_LEDGER
CONDITIONED_DISCRIMINANT_SQUARECLASS_EQUALS_MISSING_FACE=true
CONDITIONED_DISCRIMINANT_IS_NEW_INDEPENDENT_GATE=false
FINITE_RAW_OBJECTS_B2M=356
FINITE_CONDITIONED_ORIENTED_INCIDENCES_B2M=712
FINITE_CONDITIONED_C0_ENTRIES_B2M=0
OBJECT_SQUARECLASS_INJECTIVE_AT_ALL_FROZEN_CUTOFFS=true
FINITE_COLLISION_Q_EQUALS_M=true
OBSERVED_PRIME_COORDINATE_RANK_B2M=554
FINITE_ZERO_IMPLIES_ASYMPTOTIC_ZERO=false
COLLISION_BOUND_Q_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t20 derive/count equal missing-face squareclass collisions over the raw-pair family and target Q_Delta(B)=o(B)
```
