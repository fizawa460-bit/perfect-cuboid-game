# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_DEGENERATE_CLIFFORD_EVEN_CONTACT_GLUE_4_OF_5`

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

The named J2 image remains a nontrivial order-2 genus-one K3 torsor target `X_J2` with relative Jacobian `Kc`, no section, and multisection-index target 2; no explicit torsor surface is promoted yet.

## Split Clifford fingerprint

Write

```text
r=(t^2-1)^2,
q=t^4-6*t^2+1,
E: Y^2=X*(X-r)*(X-q),
r-q=4*t^2.
```

The explicit split symmetric representation

```text
M_split = diag(X, X-r, X-q)
```

has determinant `X*(X-r)*(X-q)` and associated conic

```text
X*U^2 + (X-r)*V^2 + (X-q)*W^2 = 0.
```

Its three normalized ruling-cover squareclasses over geometric constants are exactly

```text
C0: X=0  -> q
Cr: X=r  -> 1
Cq: X=q  -> q
```

so the component fingerprint is `[q,1,q]`, with `q` squarefree and nonsquare over `Qbar(t)`. This matches the Stage33-05 named J2 branch normalization `z^2=q` at the fingerprint level only.

## NEW: contact combinatorics isolate the actual glue ambiguity

The pairwise branch contacts are now exact:

```text
C0 ∩ Cr: r=(t^2-1)^2 -> t=+1,-1, each contact order 2
C0 ∩ Cq: q=0 -> four simple transverse intersections
Cr ∩ Cq: r-q=4t^2 -> t=0 order 2, and t=infinity order 2
```

The infinity statement is checked in `u=1/t`, `x=X/t^4`, where

```text
r/t^4 - q/t^4 = 4u^2.
```

Normalized line families may be written over geometric constants as

```text
C0: z0^2=q,        (t^2-1)V + i*z0 W = 0
Cr: epsilon^2=1,  (t^2-1)U + 2 i t epsilon W = 0
Cq: zq^2=q,        zq U + 2 t V = 0.
```

At each of the four transverse `q=0` points, both nontrivial covers ramify and both specialized lines are the unique line `V=0`. Therefore those four node gluings are forced: they do not carry the remaining binary sheet-pairing ambiguity.

The remaining ambiguity is confined to exactly four even-contact points:

```text
t=+1, -1  on C0/Cr
t=0, infinity on Cr/Cq.
```

At these points the normalized covers are unramified while the original degenerate lines coalesce, so one must resolve the tangency and compute the induced sheet pairing/monodromy.

This also kills a tempting shortcut: `Dplus=t^2-2t-1` selects two of the four transverse q-roots, but those q-root gluings are already forced. Hence `Dplus` support alone cannot select the global theta characteristic.

Certificate: `j2-degenerate-clifford-contact-glue-reduction.json`; verifier: `certify_j2_degenerate_clifford_contact_glue_reduction.py`.

## Next exact leaf

```text
RESOLVE THE FOUR EVEN TANGENCIES LOCALLY,
COMPUTE THE CANONICAL SHEET PAIRING / MONODROMY OF M_split,
AND COMPARE THAT GLOBAL ADMISSIBLE COVER WITH THE NAMED CV J2 CLASS.
```

Only after that equality is certified may the Hermite inverse be used to materialize `X_J2` and compute its transcendental lattice. The existing minimum-norm fingerprints `4/8/12` remain the final marked-functional selector.

## Firewalls

```text
Stage33-12 visible progress = 4/5
split determinantal q-cover fingerprint = exact [q,1,q]
transverse q-root glue = forced exact
remaining glue locus = four even contacts {+1,-1,0,infinity}
global theta characteristic identified = false
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
