# Stage32 MB104 — Lu–Miyaoka ordinary-node/triple debt

Status: **RETAINED GLOBAL MEMBER-LEVEL NECESSARY CONDITION / NONCLOSING**.

This note tests whether known global low-genus curve inequalities already kill the arbitrary-degree analytic scaling wall retained in `AMBIENT-A1-SCALING-WALL.json`.

## External theorem lock

Primary source:

Steven Shin-Yi Lu and Yoichi Miyaoka, *Bounding curves in algebraic surfaces by genus and Chern numbers*, Mathematical Research Letters 2 (1995), 663–676, DOI `10.4310/MRL.1995.V2.N6.A1`.

The exact contract used here is the singular-curve bound restated in Ciro Ciliberto and Claudio Fontanari, *Variations on the Weak Bounded Negativity Conjecture*, Advances in Geometry 24 (2024), DOI `10.1515/advgeom-2023-0027`, discussion following their Theorem 4:

for an integral curve `C` of geometric genus `g` on a smooth projective surface `S`, if some positive multiple of `K_S+C` is effective, then

`K_S.C <= 4*(g-1) + 3*c2(S) - K_S^2 + n_ot`,

where `n_ot` is the number of ordinary double points and ordinary triple points of `C`.

We use the coarse coefficient `1` for every ordinary triple point. Lu–Miyaoka note that the triple-point contribution can be improved; that improvement is not used here.

The hypothesis on a positive multiple of `K_S+C` is automatic for the present population: `C` is effective and `S` is of general type, so for some `m>0`, `mK_S` is effective and hence `m(K_S+C)=mK_S+mC` is effective.

## Cuboid-surface constants

The retained Stage32 geometry has

`K_S^2=16`.

`KNOWN-CURVE-CONE-WALL.json` source-locks `chi(O_S)=8`. By Noether's formula,

`c2(S)=12*chi(O_S)-K_S^2=96-16=80`.

Therefore

`3*c2(S)-K_S^2 = 240-16 = 224`.

For every integral `R29-LG2-MB` carrier strict transform `D` of geometric genus `g in {0,1}` and canonical degree `d=K_S.D`, Lu–Miyaoka gives

`d <= 4*(g-1)+224+n_ot`.

Equivalently:

- `g=0`: `n_ot >= max(0,d-220)`;
- `g=1`: `n_ot >= max(0,d-224)`.

Thus high-degree low-genus carriers must accumulate ordinary nodes/triple points linearly in `d`.

## Effect on the retained scaling ray

For `D_k=6kH-k*sum E_i`, `d=96k`.

If a genus-one integral member existed, then

`n_ot >= max(0,96k-224)`.

If a genus-zero integral member existed, then

`n_ot >= max(0,96k-220)`.

This immediately kills the previous *specific* analytic globalization model that put the entire strict-transform delta into one complicated cusp and used no ordinary nodes/triples once `k` is large enough.

It does **not** kill the degree direction. The scalar analytic witness can be repaired by spending part of the available delta budget on ordinary nodes.

For genus one,

`Delta_strict=240k^2+48k`.

Choose

`n1(k)=max(0,96k-224)`

ordinary nodes and assign the residual delta

`Delta_res,1=240k^2+48k-n1(k)`

to one irreducible plane branch `v^2=u^(2*Delta_res,1+1)` at a smooth point of the ambient surface. `Delta_res,1` is positive for every `k>=1`.

For genus zero,

`Delta_strict=1+240k^2+48k`.

Choose

`n0(k)=max(0,96k-220)`

ordinary nodes and put the remaining

`Delta_res,0=1+240k^2+48k-n0(k)`

into one irreducible plane branch of the same form. Again the residual is positive for every `k>=1`.

Hence Lu–Miyaoka converts arbitrary-degree globalization into a new **linear ordinary-singularity debt**, but current Stage32 interfaces do not upper-bound `n_ot` with coefficient `<1` in `d`.

## Dimension-count firewall

For the same `D_k`, retained Riemann–Roch gives only

`h0(D_k) >= chi(O(D_k)) = 240k^2-48k+8`.

The forced Lu–Miyaoka ordinary-node debt is only `O(k)`, while the linear-system size and total genus-defect budget are `O(k^2)`. Therefore a naive count saying “each ordinary node costs one condition” is asymptotically far too weak to close the ray, even before independence of conditions is addressed.

A closing route now needs a **cuboid-specific global upper bound** on ordinary node/triple count, or a theorem coupling these singularities to the two modular factor maps / Picard class with subunit slope.

## Literature boundary

Miyaoka's stronger uniform canonical-degree theorem requires `K_S^2>c2(S)`. It does not apply here because `16<80`. This matches the published cuboid-surface discussion that the usual Bogomolov/Miyaoka bounded-low-genus theorem does not cover this surface.

## Firewalls

- No claim is made that the repaired local singularity collection globalizes to an algebraic member.
- `n_ot` counts only ordinary double and ordinary triple points; arbitrary other singularities are not silently counted.
- The Lu–Miyaoka inequality is a necessary condition, not a finite-degree theorem here.
- No unibranch `176/192` cap is imported.
- No finite Picard enumeration, `R29-LG2-MB`, receiver, theorem, endpoint, or Perfect-Cuboid credit.
- Merge is not authorized.
