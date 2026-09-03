# Stage32 post-1490 O210 deck-action object-mismatch correction

Scope: fixed recovered V6 target `g1-d186`, extremal `O=210`, `q'=4`. This correction does not exclude O210 and does not change the exact defect identity `delta_D+c_u+c_v+c_uv=8586`. It corrects the object on which the missing deck action must be source-locked.

## Exact quotient objects already retained

The retained Cartesian quotient certificate distinguishes

- `P=Z x Z`;
- `X=P/H_diag`, the Beauville cover surface;
- `B=P/G_diag`, the box surface on the retained open/normalization level;
- `C0=Z/H`.

The degree-four map whose three nonidentity deck translates occur in the defect decomposition is `X -> C0 x C0`, with deck group `H=Gamma'[4]/Gamma[8] ~= V4`. Therefore the required action is an action on `X` (or directly on the class of the upstairs carrier-image `D` in `X`).

The retained 140-class/Picard64 marking, by contrast, is the box-surface Picard interface inherited from the Stoll computation. An automorphism matrix on that retained B-side Picard lattice is not automatically a deck-action matrix on `Pic(X)`. An explicit pullback/strict-transform/class adapter from the B-side carrier data to `D` on X would be required before a quadratic expression such as `D^T G T_i D` could be interpreted as `D.t_i(D)`.

Hence the previous partial source-trace target — identify the modular deck elements among the retained 140-class automorphisms and immediately compute the three `D.t(D)` values — is not safe as written. The group labels alone do not supply the missing geometric transfer between `B` and `X`.

## Independent witness-binding firewall

There is a second, independent reason not to substitute the post-21bl Picard64 adapter class for `D`.

The exact recovered V6 witness body has Picard-coordinate SHA256

`2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`

and self-intersection `758`.

The later post-21bl adapter has Picard-coordinate SHA256

`0fcbe0c9cdf894a95704bcaf55536290fc2daa736387169c891e8262f2c565a7`

and self-intersection `858`. Its own interpretation explicitly says `representative_sample_only=true` and `picard_class_is_not_effective_curve_existence=true`. The effectivity-gap certificate likewise records that no actual effective/integral carrier certificate is present.

Thus the post-21bl representative is not the exact recovered V6 witness and cannot be silently promoted to the hypothetical carrier-image class `D`.

## Corrected live bridge

The total V4 defect decomposition remains closed as an exact reduction. The three individual pairings remain open.

The next valid datum is one of:

1. source-lock `Pic(X)`, the class of the Beauville upstairs carrier-image `D`, and the three `H` deck actions on that same lattice; or
2. source-lock the three intersection numbers `D.t(D)` directly from the quotient geometry `P/H_diag`; or
3. if B-side Picard data are used, first prove an explicit B-to-X pullback/strict-transform/class-binding formula including the exceptional/branch corrections, and only then transport the three actions.

Do not rederive the total defect `8586`, do not substitute the abstract two-character V4 torsor for the geometric action, and do not materialize the residual Rosati lattice.

Firewalls: no receiver, route, theorem, endpoint, or perfect-cuboid credit; O210 remains open; FULL178 remains inactive; merge remains unauthorized.
