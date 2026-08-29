# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_RELATIVE_PICARD_OVERLAP_COCYCLE_4_OF_5`

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

Therefore scalar norms and direct branch-partition products are not the named geometric J2 Sha class.

## NEW exact interface reduction: what the Leray edge must materialize

Stage33-05 already computed a different connecting map from the finite CV presentation

```text
0 -> R=im(x-alpha) -> LcE -> Br(Kc_bar)[2] -> 0.
```

For J2 that presentation connecting cocycle is exactly zero: J2 has a Galois-fixed lift in `LcE`. This does **not** mean its Ogg-Shafarevich torsor is trivial. The two connecting maps have different targets and different meanings.

For the elliptic K3 fibration `Kc -> P1_t` with section, the load-bearing map is

```text
Br(Kc_bar) -> Sha(E/Qbar(t)),
E: Y^2=X*(X-(t^2-1)^2)*(X-(t^4-6*t^2+1)).
```

The named J2 edge can be materialized on a cover `{U_i}` of the smooth base by choosing local relative degree-zero Picard trivializations `L_i` of the named CV Azumaya/Brauer gerbe. On overlaps define

```text
D_ij = L_j - L_i in Pic^0(E),
D_ij + D_jk + D_ki = 0.
```

Then `[D_ij] in H^1(U,Pic^0)` is the actual Sha/Weil-Chatelet class. Crucially, the `L_i` must be derived from the named CV Azumaya/corestriction class; an arbitrary 2-covering with matching support is not enough.

Certificate: `j2-brauer-to-sha-leray-edge-interface.json`; verifier: `certify_j2_brauer_to_sha_leray_edge_interface.py`.

This is a genuine narrowing of the missing interface: we no longer search for another scalar/Kummer formula. We need the local relative-Picard trivializations and their overlap divisor cocycle.

## Next exact leaf

```text
EXTRACT_LOCAL_RELATIVE_PICARD_TRIVIALIZATIONS_OF_THE_NAMED_CV_AZUMAYA_CLASS
AND_COMPUTE_THEIR_OVERLAP_DIVISOR_COCYCLE_Dij
```

Only after this cocycle is explicit should it be converted to a generic-fiber Weil-Chatelet or `E[2]` coordinate.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 Brauer-to-Sha Leray edge materialized = false
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
J2 torsor equation materialized = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
