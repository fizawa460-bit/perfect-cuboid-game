# Stage32 MB104 — Beauville-cover Miyaoka wall

Status: **RETAINED GLOBAL COVER INEQUALITY / DOMINATED / NONCLOSING**.

The base cuboid resolution has `K_S^2<c2(S)`, so Miyaoka's 2008 uniform canonical-degree theorem does not apply directly. This note checks the natural workaround: lift a hypothetical `R29-LG2-MB` carrier to the smooth Beauville cover, whose Chern ratio is favorable.

## Cover invariants

FSM/AL source-locks

`X=(C8 x C8)/H_diag`,

where `g(C8)=5`, `|H|=4`, and `H` acts freely. Hence `C8 x C8 -> X` is finite etale of degree 4.

For a product of genus-5 curves,

`K^2=8*(5-1)^2=128`, `c2=4*(5-1)^2=64`.

Dividing by the free degree-4 quotient gives

`K_X^2=32`, `c2(X)=16`.

Thus `K_X^2>c2(X)`.

## Miyaoka 2008 exact constant

Yoichi Miyaoka, *The Orbibundle Miyaoka-Yau-Sakai Inequality and an Effective Bogomolov-McQuillan Theorem*, Publ. RIMS 44 (2008), 403–417, DOI `10.2977/PRIMS/1210167331`, Theorem 1.1:

for an irreducible curve of geometric genus `G` on a minimal surface with `K^2>c2`, not a smooth rational curve,

`K_X.C <= a*(G-1)+b`,

with

`a=(2*K^2+sqrt(2*K^2*(3*c2-K^2)))/(K^2-c2)`,

`b=(K^2*(3*c2-K^2)+c2*sqrt(2*K^2*(3*c2-K^2)))/(2*(K^2-c2))`.

At `(K^2,c2)=(32,16)`, the square root is `32`, so

`a=6`, `b=32`.

## Carrier lift adapter

The retained minimal-branch lower bound gives at least one odd exceptional branch, so the normalized Beauville double pullback is connected. Let its normalization have genus `G`, and let `r` be the Beauville ramification count.

Double-cover Riemann-Hurwitz gives

`G-1=2*g-2+r/2`.

AM identifies the two factor degrees `n1,n2` with `n1+n2=d`, and on `X`

`K_X=f1^*K_Y+f2^*K_Y`, `g(Y)=2`.

Therefore the canonical degree of the integral upstairs image is

`K_X.Cbar=2*n1+2*n2=2d`.

Miyaoka then gives

`2d <= 6*(2*g-2+r/2)+32`

or exactly

`2d <= 3r+12g+20`.

Thus:

- `g=0`: `2d<=3r+20`;
- `g=1`: `2d<=3r+32`.

## Dominance check

Current MB104 already has

`r >= s_min >= d-4g+4`

because every FSM-minimal `(A,B)=(1,1)` branch has odd exceptional multiplicity and hence ramifies in the Beauville cover.

Substituting this retained lower bound into the Miyaoka right-hand side shows the Miyaoka inequality is automatically compatible:

- `g=0`, `r>=d+4`: RHS `>=3d+32 > 2d`;
- `g=1`, `r>=d`: RHS `>=3d+32 > 2d`.

So the favorable Chern ratio of the Beauville cover does not produce an upper bound on `d`; the lift genus grows linearly with the same ramification resource.

## Decision

The route

`lift to X with K_X^2>c2(X) -> apply Miyaoka uniform degree theorem`

is formally nonclosing for MB104 at the currently retained interfaces. Re-entry would require an independent upper bound on `r` with sufficiently small slope in `d`, not merely the existing lower bound.

No global carrier existence, finite degree window, receiver/theorem/endpoint credit, or merge authorization is claimed.
