# Stage32 post-1490 O210 X local multiplicity adapter

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`. The named relative-H node translations `u,v,uv` are already locked by canonical `d03cfe8c...`. This note identifies the retained exceptional vector with the multiplicity of the upstairs carrier-image `D` at the 48 unique X-lifts, and uses that identification only to produce rigorous local **lower bounds** for `D.t(D)`.

The retained Beauville multibranch note fixes the last 48 V6 pairings as the exceptional intersections `C.E_j` on the resolved box surface. For the normalization `N` of a hypothetical carrier, a local branch above node `j` has positive contact `m=ord_P(s)` with `E_j`, and the sum of these contacts over all normalized branches above the node is exactly `C.E_j`. The common-double-cover certificate identifies `Y` with the normalization of the Beauville pullback `N x_B X`.

Locally after blowing up, the double cover is `s=r^2`, with ramification divisor `F_j=(r=0)` upstairs. For a downstairs normalized branch `s=t^m*unit`, normalization of `r^2=t^m*unit` gives: if `m` is odd, one upstairs branch with `F_j`-contact `m`; if `m` is even, two upstairs branches, each with contact `m/2`. In either case the total upstairs contact contributed by that downstairs branch is `m`. Summing over all branches above node `j` therefore gives

`Dtilde.F_j = mult_{x_j}(D) = C.E_j`.

There is no net factor-of-two correction. Hence the exact multiplicities at node labels 93..140 are the recovered V6 last-48 vector

`[1,1,1,2,2,0,1,2,8,4,7,2,9,5,1,10,5,11,7,1,3,1,13,1,6,2,12,16,4,3,5,6,5,10,8,1,10,15,11,2,5,11,4,10,2,4,3,13]`,

with total 266, 47 positive entries, and the unique zero at label 98.

For distinct curves on the smooth surface X, the standard local intersection inequality is

`I_x(D,t(D)) >= mult_x(D) mult_x(t(D))`.

The exact relative-H certificate supplies the named permutations of the 48 nodes, so `mult_x(t(D))` is read from the multiplicity at the inverse translated node. Summing the 48 marked contributions gives

- `D.u(D) >= 1360`, hence `c_u >= 680`;
- `D.v(D) >= 1796`, hence `c_v >= 898`;
- `D.uv(D) >= 1452`, hence `c_uv >= 726`.

Thus `c_u+c_v+c_uv >= 2304`. Combining only with the already locked exact budget

`delta_D + c_u + c_v + c_uv = 8586`

gives `delta_D <= 6282`.

These are lower bounds, not exact pairings. Intersections away from the 48 marked points or infinitely-near contributions can increase `D.t(D)`. This leaf does not exclude O210 and gives no receiver, route, theorem, endpoint, or perfect-cuboid credit. It also makes no Pic(B)-to-Pic(X) divisor-class identification.
