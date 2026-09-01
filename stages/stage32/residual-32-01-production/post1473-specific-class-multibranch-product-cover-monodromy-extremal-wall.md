# Stage32 post-1473 fixed-V6 multibranch product-cover monodromy extremal wall

## Scope

This note continues only the exact fixed V6 class for `g1-d186`, with `d=186`, exceptional mass `e=266`, after hostile re-audit review `5076097948` passed the Beauville/product-cover necessary-condition nonexclusion wall at audited head `ccc1ee386de0f73141321ac0f09af1121c0f70f1`.

The audited input is:

- a hypothetical integral geometric-genus-one multibranch carrier has normalization `N`;
- the pulled-back Beauville double cover `Y -> N` ramifies at the `O` odd exceptional contacts, so `2g(Y)-2=O`;
- a connected component `D` of the pulled-back unramified product cover has degree `q' in {1,2,4}` over `Y`;
- `q'=1` is impossible for `d=186`;
- writing the two projection degrees `D -> X(8)` as `n1,n2`, with `g(X(8))=5`, one has
  `2 q' d = 8(n1+n2)` and `q'O >= 8 n_i` for each nonconstant projection;
- the previous audited conclusion was only `O>=186`, `S1>=146`, with surviving coarse branch partitions.

No new global curve existence is assumed here.

## Exact integer sharpening

Since `q'` is now only `2` or `4`, retain the integer projection degrees rather than replacing `max(n1,n2)` by a real-valued half-sum.

### Case q'=2

The canonical identity gives

`n1+n2 = q'd/4 = 93`.

Riemann--Hurwitz gives, for either projection (and trivially also if a projection is constant),

`n_i <= floor(q'O/8) = floor(O/4)`.

Therefore

`93 <= 2 floor(O/4)`.

The ramification number `O` is even. At `O=186`, the right side is `2*46=92`, impossible. The first allowed even value is therefore

`O >= 188`.

With total exceptional mass `e=266`, the same odd-branch mass inequality

`e >= S1 + 3(O-S1) = 3O-2S1`

gives

`S1 >= ceil((3O-e)/2) >= 149`.

Thus a `q'=2` component cannot realize the coarse extremal `O=186` state.

### Case q'=4 and the extremal O=186 boundary

Now

`n1+n2 = 186`,

and Riemann--Hurwitz gives

`n_i <= O/2`.

If `O=186`, then both inequalities must be equalities:

`n1=n2=93`.

Define the projection ramification remainders

`R_i := q'O - 8n_i >= 0`.

Using `n1+n2=q'd/4`,

`R_1+R_2 = 2q'(O-d)`.

Hence at `q'=4`, `O=d=186`,

`R_1=R_2=0`.

So both maps `D -> X(8)` must be unramified/etale covers of degree `93`.

## V4 monodromy meaning of q'=4

The product cover `P=X(8)xX(8) -> X` is the connected regular etale cover with deck group `(Z/2)^2`. Pull it back to the connected curve `Y`. If the monodromy image is `H <= (Z/2)^2`, then each connected component of the pullback has degree `|H|` over `Y`; equivalently `q'=|H| in {1,2,4}`.

Therefore the extremal `O=186` survivor requires **full V4 monodromy** `H=(Z/2)^2` in addition to the two degree-93 etale projection conditions.

This is a necessary-condition sharpening, not an exclusion.

## Retained tangent evidence and the present wall

The exact retained tangent certificate

`stages/stage33/33-07/exceptional-p1-tangent-coordinates.json`

has canonical SHA256

`beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636`.

It materializes the 48 exceptional P1 tangent-coordinate models and the physical-side crossing tangent data, but its own constructive-progress flags explicitly leave the following unmaterialized:

- `order2_source_first_residue_functions_materialized=false`;
- `project_14x26_L_squareclass_tensor_materialized=false`;
- `absolute_delta_loc_computed=false`;
- `chosen_global_geometric_lifts_materialized=false`.

Repository search at this leaf found no separately materialized artifact for those residue/squareclass/absolute-local/monodromy layers.

Accordingly, the retained physical-side tangent points MUST NOT be substituted for the unknown tangent/residue data of a hypothetical V6 carrier branch. The current evidence is sufficient to state the extremal full-V4/etale necessary condition, but not sufficient to evaluate whether the hypothetical carrier realizes that monodromy.

## Verdict / firewall

Authoritative only after hostile audit:

- if `q'=2`, necessarily `O>=188` and `S1>=149`;
- if `O=186`, necessarily `q'=4`, full V4 monodromy, `n1=n2=93`, and both projections are etale;
- current retained tangent/intersection evidence does not decide that full-V4 carrier-branch monodromy condition.

DO NOT USE THIS FOR:

- analytic realization of any coarse branch partition;
- existence of an integral carrier;
- exclusion of all multibranch carriers;
- FULL178 geometric closure or heavy-production authorization;
- general genus-<=1 classification;
- receiver, route, theorem, endpoint, or perfect-cuboid credit.
