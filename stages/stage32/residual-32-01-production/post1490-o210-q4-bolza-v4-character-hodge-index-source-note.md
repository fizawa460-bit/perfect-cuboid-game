# Stage32 post1490 O210 V4-character Hodge-index global constraint

## Scope

This leaf introduces genuinely new mathematical input after the V218 retained-source wall. It does not reopen the retained Picard64/tangent/effectivity search. It applies the Hodge index theorem directly to the hypothetical upstairs divisor `D` and its `V4` deck orbit on the smooth projective surface `X`.

Fixed target: `g1-d186`, `(d,e,g)=(186,266,1)`, `O=210`, `q'=4`.

## New external theorem input

Use the Hodge index theorem in the form:

> On a smooth projective surface, if `H` is ample and `E.H=0`, then `E^2 <= 0`; equivalently, the intersection form on `H^perp` is negative semidefinite (negative definite modulo numerical triviality).

Web source: Fei Ye, “Hodge Index Theorem”, published 2020-11-20, Section 1, Lemma 1 / Theorem 1:
`https://math.yfei.page/posts/2020-11-20-hodge-index/`

Standard reference: Hartshorne, *Algebraic Geometry*, Chapter V, Theorem 1.9.

No theorem is used to assert effectivity. The argument is conditional: every actual integral carrier `D` realizing the O210 candidate must satisfy the resulting numerical inequalities.

## V4-invariant ample class

Choose any ample divisor `H0` on the projective surface `X` and set

`H = H0 + u(H0) + v(H0) + uv(H0)`.

Automorphisms preserve ampleness and a finite sum of ample classes is ample, so `H` is ample and `V4`-invariant. Therefore

`H.D = H.u(D) = H.v(D) = H.uv(D)`.

The three nontrivial character combinations

- `E_u  = D + uD - vD - uvD`,
- `E_v  = D - uD + vD - uvD`,
- `E_uv = D - uD - vD + uvD`

are all orthogonal to `H`. Hodge index gives `E_chi^2 <= 0`.

## Exact V4 Gram arithmetic

From the retained V4 defect decomposition write

- `s = D^2 = -162 + 2*delta_D`,
- `a = D.uD  = 2*c_u`,
- `b = D.vD  = 2*c_v`,
- `c = D.uvD = 2*c_uv`,
- `delta_D + c_u + c_v + c_uv = 8586`.

In orbit order `(D,uD,vD,uvD)` the Gram matrix is V4-circulant:

`[[s,a,b,c],[a,s,c,b],[b,c,s,a],[c,b,a,s]]`.

Its nontrivial character eigenvalues are

- `lambda_u  = s+a-b-c = 4*(delta_D+c_u)-17334`,
- `lambda_v  = s-a+b-c = 4*(delta_D+c_v)-17334`,
- `lambda_uv = s-a-b+c = 4*(delta_D+c_uv)-17334`.

Since `E_chi^2 = 4*lambda_chi`, Hodge gives `lambda_chi <= 0`. Each displayed lambda is congruent to `2 mod 4`, hence equality is impossible and in fact `lambda_chi <= -2`.

Thus, for each `t in {u,v,uv}`,

`delta_D + c_t <= 4333`.

Adding the other two character inequalities gives the complementary lower bound

`c_t >= delta_D - 80`.

These inequalities are genuinely independent of the retained local multiplicity products: they come from the global signature of the intersection form on `X`.

## Consequences for the O210 corridor

The retained marked-singularity bound gives `delta_D >= 1046`. Combining with Hodge gives

`1046 <= delta_D <= 2206`.

Moreover every deck half-intersection satisfies

`delta_D - 80 <= c_t <= 4333 - delta_D`.

In particular `c_u,c_v,c_uv >= 966`; this dominates the previous marked-only lower bounds `(680,898,726)`.

The universal componentwise lower budget therefore improves from `3350` to

`1046 + 3*966 = 3944`,

so the residual slack relative to the exact `8586` identity drops from `5236` to `4642`.

At the endpoint `delta_D=2206`, the only ordered deck triples allowed by these Hodge bounds are permutations of `(2126,2127,2127)`.

This still does not exclude O210. It is a new exact global constraint and remains provisional pending hostile audit.

## Firewalls

- No actual effective carrier is claimed.
- No local equation, tangent direction, or infinitely-near data are inferred.
- No B-side Picard64 action is identified with `Pic(X)`.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit is released.
