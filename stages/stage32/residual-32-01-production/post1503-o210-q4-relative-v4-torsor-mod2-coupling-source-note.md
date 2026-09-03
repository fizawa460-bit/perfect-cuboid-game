# Stage32 post-1503 O210 relative-V4 torsor / mod-2 Rosati coupling

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, at the hostile-audited repaired boundary `Gamma^2=15806`, `sigma(Gamma)=1204`, `Q(T)=602`. This is a new coupling input. It does not reuse the #1501 generic inference that shared-cover geometry by itself forces strict Rosati loss.

## Locked geometry

Let

- `Z=X(8)`;
- `H=Gamma'[4]/Gamma[8] ~= (Z/2)^2`;
- `C0=Z/H`, with `Z -> C0` a connected finite etale H-torsor of degree 4;
- `P=Z x Z`;
- `X=P/H_diag`;
- `q:X -> C0 x C0=P/(H x H)`.

The retained pair-map reduction source-locks `q` as finite etale of degree four with deck group `(H x H)/H_diag ~= H`, and the retained X(8) quotient certificate source-locks `Z -> C0` as the connected etale V4 cover.

There is a canonical fiberwise interpretation of `X`: a point represented by `(z1,z2)` modulo diagonal H determines the H-equivariant isomorphism

`phi_(z1,z2): Z_{c1} -> Z_{c2},  h*z1 |-> h*z2`.

Changing `(z1,z2)` by diagonal H does not change `phi`; conversely an H-equivariant isomorphism of the two H-torsor fibers is determined this way. Thus `X` is the relative H-isomorphism torsor between the two pullbacks of `Z` on `C0 x C0`.

## Carrier consequence in H^1(-,F2)

Let `Y` be the normalization of the hypothetical O210 carrier image upstairs and let

`f1,f2:Y -> C0`

be its two projections, of degrees 105 and 81. Since the pair map lifts through `X`, the preceding relative-torsor interpretation gives an H-torsor isomorphism

`f1^* Z ~= f2^* Z`.

For every character `chi:H -> F2`, let `alpha_chi in H^1(C0,F2)` be the corresponding etale double-cover class. Then

`f1^*(alpha_chi) = f2^*(alpha_chi)`.

Because `Z -> C0` is connected with group H, the character map `H^* -> H^1(C0,F2)` is injective. Its image

`W := span_F2{alpha_chi : chi in H^*}`

has dimension exactly two.

Let the two correspondence maps on mod-2 cohomology be

`T_12 = f2_* f1^*`,  `T_21 = f1_* f2^*`.

They are Rosati-adjoint orientations of the same geometric correspondence. For `alpha in W`, the torsor equality and finite-map push-pull give

`T_12(alpha) = f2_* f2^*(alpha) = 81 alpha = alpha  (mod 2)`,

`T_21(alpha) = f1_* f1^*(alpha) = 105 alpha = alpha (mod 2)`.

Hence the actual O210 correspondence must have a common two-dimensional fixed subspace for `T` and `T^dagger` on mod-2 cohomology. Via the principal polarization this is equivalently a common two-dimensional fixed subspace on the four-dimensional `J(C0)[2]` module. Only the dimension condition is used below; no unidentified basis for W is assumed.

## Exact Q=602 residue preflight

Use the retained integral endomorphism coordinates

`(t11.a,t11.b,t12.a,t12.b,t21.a,t21.b,t22.a,t22.b)`

for `Z[r]`, `r^2=-2`, with the exact 8x8 Rosati trace Gram matrix and its unimodular isometry to `D4 direct-sum D4`.

Reduce modulo two. Then `r` becomes `eps` with `eps^2=0`, so the coefficient ring is

`F2[eps]/(eps^2)`.

The retained principal Hermitian matrix reduces to

`H_2 = [[0,1+eps],[1+eps,0]]`,

and `H_2^{-1}=H_2`; conjugation is trivial modulo two. Therefore

`T^dagger = H_2 T^t H_2`

can be replayed exactly on the 4-dimensional F2 module.

A bounded enumeration of D4 residue classes by exact norm, followed by the retained unimodular change of basis, gives for the exact shell `Q(T)=602`:

- total integral vectors in the shell: `1,312,836,096`;
- realized coordinate residue classes modulo two: `96`;
- common fixed-space dimension distribution for `(T,T^dagger)`:
  - dimension 0: `32` residue classes;
  - dimension 1: `36` residue classes;
  - dimension 2: `24` residue classes;
  - dimension 3: `3` residue classes;
  - dimension 4: `1` residue class;
- geometric relative-V4 condition `dim Fix(T) intersect Fix(T^dagger) >= 2` leaves exactly `28` residue classes and `382,918,016` integral norm-602 vectors.

Thus this new coupling removes 68 of the 96 mod-2 residue classes, about 70.8% of the exact norm-602 shell, without materializing the full Rosati frontier.

## Decision and next leaf

This does **not** exclude `Q=602`: 28 mod-2 residue classes survive. It is nevertheless new positive coupling evidence satisfying the #1501 re-entry rule, because it maps the actual relative-V4 lift geometry to a machine-checkable Rosati congruence constraint.

The next exact leaf is to source-lock the specific two-plane `W subset J(C0)[2]` defined by the etale cover `X(8)->C0` in the retained Bolza/Jacobian basis, and then test the 28 surviving residue classes against pointwise fixation of that exact W. A mod-4 refinement is secondary and should only be attempted if the exact W embedding still leaves survivors.

Firewalls:

- no inference `Gamma^2=2*d1*d2`;
- no inference `sigma=0` from shared-cover geometry;
- no claim that every integral endomorphism is a geometric correspondence;
- O210 remains open unless the exact W test removes all survivors;
- O212 and later remain blocked;
- no FULL178, receiver, route, theorem, endpoint, existence, or nonexistence credit follows.
