# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_INDEX2_GENUS_ONE_TORSOR_TARGET_4_OF_5`

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

## Retained exact rejections

```text
constant d=2 -> geometrically trivial after Qbar base change
q=t^4-6*t^2+1 -> single-isogeny homogeneous space has an explicit Q(t)-point
Dplus=t^2-2*t-1 -> half-divisor pushforward/support datum only
naive CV branch pair-products -> split-E[2] triple (1,2,2), hence trivial over Qbar(t)
```

Stage33-05's zero presentation connecting cocycle only means that J2 has a fixed lift in the CV presentation module; it is not Sha-triviality.

## Brauer-to-Sha interface retained

For the elliptic K3 fibration `Kc -> P1_t` with section,

```text
Br(Kc_bar) ~= Sha(Kc_bar/P1),
E: Y^2=X*(X-(t^2-1)^2)*(X-(t^4-6*t^2+1)).
```

The named J2 class must be materialized through the relative Picard/twisted-Poincare descent, not through scalar norms or direct branch pair-products.

## NEW exact target refinement: the torsor is an index-2 genus-one K3

J2 is already certified geometrically nontrivial and of exact order 2. For an elliptic K3 torsor `X` over its Jacobian surface `S`, the standard Brauer-Sha correspondence gives:

```text
alpha_X = 0  <=>  X has a section,
multisection_index(X) = order(alpha_X).
```

Therefore the named J2 image is forced to be a genus-one K3 torsor `X_J2` satisfying

```text
J^0(X_J2) ~= Kc,
X_J2 has no section,
multisection index(X_J2) = 2.
```

Equivalently, the universal object is a `(1 x J2)`-twisted Poincare invertible sheaf on `X_J2 x_{P1} Kc` over the smooth base. Local untwisted trivializations of that twisted Poincare object glue by translations in `Pic^0`; those translations are the actual Sha Cech cocycle.

This corrects an overly loose formulation from the previous leaf: arbitrary line-bundle differences on `Kc` alone are not enough. The local data must come from the named Azumaya/twisted-Poincare descent.

Certificate: `j2-twisted-poincare-torsor-target.json`; verifier: `certify_j2_twisted_poincare_torsor_target.py`.

The existing exact CV graph lifts remain useful only as branch-side divisor input for constructing local splitting modules of the named Q-defined CSA. They are not promoted directly to Sha data.

## Next exact leaf

```text
CONSTRUCT_AN_EXPLICIT_GENUS_ONE_K3_MODEL_X_J2
OR EQUIVALENT LOCAL AZUMAYA SPLITTING MODULES,
VERIFY J^0(X_J2)=Kc,
VERIFY NO SECTION,
VERIFY A DEGREE-2 MULTISECTION,
THEN COMPUTE T(X_J2) OR THE OVERLAP TRANSLATION COCYCLE.
```

Once `T(X_J2)` is explicit, the existing lattice fingerprints select the marked J2 functional by minimum norm 4/8/12.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 explicit torsor surface materialized = false
J2 Brauer-to-Sha Leray edge materialized = false
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
