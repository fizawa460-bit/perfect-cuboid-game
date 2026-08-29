# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_DEGENERATE_CLIFFORD_THETA_GLUE_4_OF_5`

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

The constant `d=2`, the scalar `q` viewed as a single chosen isogeny coordinate, the `Dplus` support pushforward, and the naive CV branch pair-products do not materialize the named geometric J2 Sha torsor. Stage33-05's zero presentation connecting cocycle only gives a fixed lift in the CV presentation module; it is not Sha-triviality.

The named J2 image is a nontrivial order-2 genus-one K3 torsor `X_J2` with

```text
J^0(X_J2) ~= Kc,
no section,
multisection index = 2.
```

## Degenerate Hermite inverse target

For the Kc generic fiber write

```text
r=(t^2-1)^2,
q=t^4-6*t^2+1,
E: Y^2=X*(X-r)*(X-q),
r-q=4*t^2.
```

The Weierstrass branch cubic therefore splits into the three sections `X=0`, `X=r`, `X=q`. Van Geemen Section 8.7 places this in the three-component degenerate symmetric-determinantal/conic-bundle case rather than the general smooth trigonal case.

## NEW: exact split Clifford q-cover fingerprint

There is an explicit symmetric determinantal representation

```text
M_split = diag(X, X-r, X-q),
det(M_split)=X*(X-r)*(X-q).
```

Its associated conic is

```text
X*U^2 + (X-r)*V^2 + (X-q)*W^2 = 0,
```

and the diagonal even-Clifford symbol is

```text
(-X*(X-r), -X*(X-q)).
```

Restricting the ruling double cover to the three branch components and comparing squareclasses over the geometric function field gives

```text
X=0 : q
X=r : 1
X=q : q
```

so the exact component-cover fingerprint is

```text
[q,1,q].
```

This is genuinely geometric: `q=t^4-6*t^2+1` is squarefree and non-square over `Qbar(t)`. In particular this does not suffer from the old constant-`d=2` base-change collapse.

Stage33-05's named J2 branch normalization is exactly

```text
z^2=q(t).
```

Hence `M_split` reproduces the same nonconstant `q`-cover fingerprint on the two nontrivial components. This is new load-bearing geometric information.

It is not yet a proof that the global even-Clifford class of `M_split` equals the named CV J2 class: componentwise squareclasses do not determine the node gluing/admissible double cover or its global theta characteristic. Therefore the Hermite inverse and marked Brauer coordinate are not promoted yet.

Certificate: `j2-degenerate-clifford-q-fingerprint-adapter.json`; verifier: `certify_j2_degenerate_clifford_q_fingerprint_adapter.py`.

## Next exact leaf

```text
MATCH THE GLOBAL NODE GLUE / ADMISSIBLE DOUBLE COVER / THETA CHARACTERISTIC
OF THE [q,1,q] SPLIT-CLIFFORD COMPONENT COVERS
TO THE NAMED CV J2 CLASS.
```

If that global match succeeds, use the resulting J2-selected symmetric representation in the Hermite inverse to recover the binary-quartic genus-one K3 `X_J2`, verify Jacobian/no-section/bisection-index-2, and compute `T(X_J2)`. The existing minimum-norm fingerprints `4/8/12` then select the marked J2 functional.

## Firewalls

```text
Stage33-12 visible progress = 4/5
split determinantal q-cover fingerprint = exact [q,1,q]
global theta/node glue identified = false
named CV J2 = split Clifford class certified = false
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
