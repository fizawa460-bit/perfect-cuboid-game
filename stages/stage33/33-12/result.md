# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_DEGENERATE_HERMITE_INVERSE_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked Brauer functional is still one of the three nonzero functionals.

## Retained semantic firewalls

The constant `d=2`, the scalar `q`, the `Dplus` support pushforward, and the naive CV branch pair-products do not materialize the named geometric J2 Sha torsor. Stage33-05's zero presentation connecting cocycle only gives a fixed lift in the CV presentation module; it is not Sha-triviality.

The named J2 image is a nontrivial order-2 genus-one K3 torsor `X_J2` with

```text
J^0(X_J2) ~= Kc,
no section,
multisection index = 2.
```

## NEW: explicit construction route is the degenerate Hermite inverse problem

Van Geemen's Hermite construction starts from a genus-one fibration with a double section

```text
w^2=a0*v^4+4*a1*v^3+6*a2*v^2+4*a3*v+a4
```

and recovers its Jacobian together with a symmetric `3 x 3` determinantal conic bundle

```text
M = [[a0, a1, a2+2*x],
     [a1, a2-x, a3],
     [a2+2*x, a3, a4]].
```

The conic bundle / even Clifford algebra is the order-2 Brauer datum defining the genus-one torsor.

For our Kc generic fiber

```text
E: Y^2=X*(X-r1)*(X-r2),
r1=(t^2-1)^2,
r2=q=t^4-6*t^2+1,
```

the affine cubic branch is exactly

```text
X=0  union  X=r1  union  X=r2.
```

These are three generically distinct sections because `r1-r2=4*t^2`. Hence this is not the smooth trigonal branch situation: it is the three-component degenerate Hermite/conic-bundle case. Van Geemen Section 8.7 explicitly notes Wittenberg's three-irreducible-component case as a degenerate instance of this construction.

Therefore we do not apply the general smooth-branch Theorem 7.6 directly. The exact inverse problem is now:

```text
construct a Hermite-form symmetric matrix M_J2
such that its determinant is the Kc cubic branch
(up to an explicitly certified Weierstrass coordinate/scaling change)
and its even-Clifford Brauer class is the named CV J2 class;
then read off a0,...,a4 and obtain X_J2.
```

This is stronger than the previous abstract relative-Picard interface: the unknown is now a concrete symmetric determinantal representation / binary quartic.

Certificate: `j2-degenerate-hermite-inverse-construction-target.json`; verifier: `certify_j2_degenerate_hermite_inverse_construction_target.py`.

## Next exact leaf

```text
SOLVE_THE_DEGENERATE_HERMITE_SYMMETRIC_DETERMINANTAL_REPRESENTATION
FOR_THE_NAMED_CV_J2_CLASS,
RECOVER_THE_BINARY_QUARTIC_GENUS_ONE_K3_X_J2,
VERIFY JACOBIAN=Kc / NO SECTION / BISECTION INDEX 2,
THEN COMPUTE T(X_J2).
```

Once `T(X_J2)` is explicit, the existing minimum-norm fingerprints `4/8/12` select the marked J2 functional.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 explicit torsor surface materialized = false
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
