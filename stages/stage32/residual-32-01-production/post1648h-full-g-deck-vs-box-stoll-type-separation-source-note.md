# Stage32 post1648H full-G deck versus retained box-Stoll type separation

Scope: fixed target `g1-d186`, `O=210`, `q'=4`, `Q=602`. This is a route-typing correction only. It does not identify the principal `b3` member and does not contract the Q602 survivor set.

The exact quotient square is already source-locked:

- `P = Z x Z`, with `Z=X(8)`;
- `H = Gamma'[4]/Gamma[8]`, order 4;
- `G = Gamma[4]/Gamma[8]`, order 8;
- `X = P/H_diag`;
- `B = P/G_diag`, the retained box surface on the relevant open/normalization level;
- `X -> B` has deck group `G/H ~= C2`.

Therefore any representative `g in G-H` acts nontrivially on `X` as the deck involution `tau`, but its induced action on `B=P/G_diag` is the identity by definition of the quotient. The source-locked full-G normalizer leaf uses exactly such a `g` to represent the nontrivial `G/H` coset.

This must be distinguished from the retained relative-`H` Stoll actions. The source-locked Beauville deck adapter identifies

- `u = g7*g9`,
- `v = g7*g8`,
- `uv = g8*g9`,

with the nontrivial transformations induced by `(h,1)` on the relative quotient; these are not diagonal `h` and therefore are genuine nontrivial automorphisms on the retained box/Picard action.

Consequently the post1629 re-entry formulation “identify T4 / the nontrivial G/H deck involution as a nontrivial retained Stoll member on B” is type-incompatible. There is no such nontrivial box automorphism to identify: the diagonal `G/H` deck element is upstairs on `X` and disappears on `B`.

The post1648F order-8 subgroup found as the kernel of the retained six-Weierstrass quotient action, and the four outside-H words retained by post1648G, are therefore not promoted to modular `G` or to `T4`. Their agreement in order and boundary behavior is insufficient and in fact occurs on the wrong quotient object.

The correct continuation is to source-bind the principal `b3` / `beta_B` action itself on the retained box marking, for example by a marked curve or modular generator adapter. The full-G extra deck involution cannot be used as a nontrivial Stoll(B) anchor.

Firewalls: survivors remain `[73,97,235]`; `Q602_excluded=false`; `O210_excluded=false`; conditional residue 235 is not promoted; no controller/receiver/route/theorem/endpoint/perfect-cuboid credit.
