# Stage32 MB104 — population-wide finite-window reduction / global-member barriers

Status: **RETAINED PARTIAL MB104 / FINITE DEGREE WINDOW NOT YET PROVED / NO RECEIVER CREDIT**.

This checkpoint does not complete MB104. It records the strongest retained population-wide restrictions and the nonclosure walls accumulated through the current global-member stage. Let `D` be the strict transform of a nonexceptional integral carrier in `R29-LG2-MB`, with geometric genus `g in {0,1}`. Write

`d=K_S.D=n1+n2`, `M=sum_i M_i`, `R=sum_i r_i`,

and let `s_min` be the number of FSM-minimal `(A,B)=(1,1)` node branches.

## 1. Core population-wide identities

The two modular factor directions give

`6*n_i=2*q_i+M`,

hence `q_i=3*n_i-M/2` and `M<=3d`.

The exact two-factor slack identity is

`M-d+4g-4=sigma_1+sigma_2>=0`,

so

- `g=0`: `d+4<=M<=3d`;
- `g=1`: `d<=M<=3d`.

The branch-resource argument gives the stronger direct lower bound

`s_min>=d-4g+4`,

therefore `s_min>=d+4` for genus zero and `s_min>=d` for genus one. A genuinely independent upper bound `M<=alpha*d+beta` or `s_min<=alpha*d+beta` with `alpha<1` would close MB104.

## 2. Picard/Hodge mass bound

With `H=K_S`, `H^2=16`, the 48 disjoint exceptional `(-2)` curves and negative-definiteness of `H^perp` give

`sum_i M_i^2<=d^2/8+2d-4g+4`.

Cauchy yields

`M^2<=6d^2+96d-192g+192`.

Its asymptotic coefficient is `sqrt(6)>1`, so this is useful pruning but not a finite degree bound.

## 3. Local lambda-capacity wall

For the minimal type `(A,B)=(1,1)`, the resolved A1 germ is

`gamma_lambda(t)=(t,lambda*t,lambda^2*t)`, `lambda in C^*`.

Arbitrarily many pairwise-distinct local landing values are allowed by the retained local model, and the FSM weighted local order does not see `lambda`. Pure exceptional-`P^1` landing cardinality therefore cannot produce the required subunit coefficient.

## 4. Known-curve cone and effective scaling ray

The exact cuboid computation has 140 known curves: 32 conics, 12 Satake-boundary elliptics, 48 other elliptics, and 48 exceptional curves. The integral Picard classes

`D_k=6kH-k*sum_i E_i`, `k>=1`,

satisfy

`d=96k`, `M=96k=d`, `D_k^2=480k^2`,

and have strictly positive intersection with all 140 known curves. Riemann--Roch gives

`chi(O(D_k))=240k^2-48k+8>0`,

and `K_S-D_k` cannot be effective, so every `D_k` is represented by an effective divisor.

This does **not** imply an integral member and does not imply geometric genus `0` or `1`. It proves that the known-curve nonnegative cone, even together with divisor-class effectivity, does not bound degree.

## 5. Exact A1 contraction debt

Contracting the exceptional `(-2)` curve back to a box-surface A1 node adds

`p_a(C)-p_a(D)=floor(M_i^2/4)`.

Thus

`Delta_image=Delta_strict+Q_A1`,
`Q_A1=sum_i floor(M_i^2/4)`.

Discrete convexity over the 48 nodes gives

`Q_A1>=M^2/192-12`.

Consequently

- `g=0`: `Q_A1>=(d+4)^2/192-12`;
- `g=1`: `Q_A1>=d^2/192-12`.

This is a genuine quadratic conductor debt, but image arithmetic genus and discriminant degree can grow quadratically as well.

## 6. Generic and ambient conductor-capacity walls

The S32-PW09 interface `Disc(pi)=Br(f)+2A` does not cap the index from degree and special-value count alone. The quadratic orders

`B_N=A+t^N uA`, `u^2=t`,

have normalized projection degree `2`, one special value, index `N`, and discriminant valuation `2N+1`.

More strongly, unbounded index occurs inside the actual box-node equation `xz=y^2`:

`(x,y,z)=(s^2,s^(2m+1),s^(4m))`.

The first-factor degree stays `2`, exceptional mass stays `2`, while the normalization index is `m`. The ambient A1 equation therefore does not supply a local conductor-capacity bound.

The ambient wall's AM dependency was repaired in this checkpoint: it now source-locks the authoritative JSON

`post1648am-beauville-fibration-picard-source-lock.json`

at blob `aa14d340e8b68f863d4013d34fb0eee7b306c0ee`; the previous verifier referred to a nonexistent `.md` path and could not pass an exact-head source-lock replay.

## 7. Simultaneous arbitrary-degree analytic profile

For the effective ray `D_k`, take `2k` distinct-lambda minimal branches at each of the 48 nodes. Then

`d=M=R=s_min=96k`,
`n1=n2=48k`,
`M_i=2k`,
`Q_A1=48k^2=d^2/192`.

The retained special-fibre and factor-map Riemann--Hurwitz ledgers can be saturated simultaneously. The required strict-transform genus defect is quadratic and is locally analytically realizable. This gives an arbitrary-degree **analytic/scalar compatibility witness**, not a global algebraic curve.

## 8. Lu--Miyaoka ordinary-singularity debt

For the cuboid resolution,

`K_S^2=16`, `chi(O_S)=8`, `c2(S)=80`.

Lu--Miyaoka gives for an integral carrier

`d<=4*(g-1)+224+n_ot`,

where `n_ot` is the coarse count of ordinary double and ordinary triple points. Hence

- `g=0`: `n_ot>=max(0,d-220)`;
- `g=1`: `n_ot>=max(0,d-224)`.

This kills the particular zero-ordinary-node globalization model at high degree, but the forced debt is only `O(d)`, whereas the retained delta and Riemann--Roch scales on `D_k` are `O(d^2)`. It therefore does not close the degree direction.

## 9. Beauville-cover Miyaoka wall

The smooth Beauville cover

`X=(C8 x C8)/H_diag`

has

`K_X^2=32`, `c2(X)=16`,

so the favorable `K^2>c2` Miyaoka theorem applies upstairs. If `r` is the ramification count of the connected normalized pullback and `G` its genus, then

`G-1=2g-2+r/2`,
`K_X.Cbar=2d`,

and Miyaoka gives

`2d<=3r+12g+20`.

But MB104 already has

`r>=s_min>=d-4g+4`.

The upstairs inequality is therefore compatible with the existing scaling direction and supplies no finite degree window without an independent upper bound on `r`.

## 10. Two factor directions share one Beauville cover

The two AM factor directions are two projections of the **same** degree-two Beauville cover. They do not provide independent ramification ledgers `r1,r2`.

For each direction,

`r>=2*n_i-4g+4`.

Combining the two inequalities gives only

`r>=2*max(n1,n2)-4g+4>=d-4g+4`.

Thus the two directions cannot be added as if they came from two independent double covers. Any future ramification closer needs either an upper bound on this shared `r` or a genuinely distinct cover/branch divisor.

## 11. BTVA exact projective-span filter

Bruin--Thomas--Várilly-Alvarado, Theorem 1.2, gives cuboid-specific global restrictions:

- every rational curve passes through at least six surface singularities;
- every rational curve other than the 32 known conics passes through at least seven singularities spanning `P^6`;
- a genus-one curve is either a component of a hyperplane section or passes through at least six singularities spanning a hyperplane.

Because `H=K_S`, `H^2=16`, and `H` is nef, an integral component of a canonical hyperplane section has `d<=16`. Hence the Stage32 receiver gets the executable filters

- `g=0`, `d>2`: met-node count `N>=7` and exact node-coordinate rank `7`;
- `g=1`, `d>16`: `N>=6` and exact node-coordinate rank at least `6`.

Using the exact 48-node coordinates reconstructed by MB103 over `Q(i)`, the full node set has vector rank `7`. Explicit zero-based witnesses in the MB103 ordering are

- `[0,1,2,4,8,9]`: rank `6`, spanning `P^5`;
- `[0,1,2,4,8,9,24]`: rank `7`, spanning `P^6`.

This is a real future fixed-degree node-profile filter. It does not close MB104 because the retained scaling profile meets all 48 nodes and therefore survives the span requirement.

## 12. Current MB104 boundary

The main certificate is now V7 and the main verifier source-locks the downstream ambient-A1, Lu--Miyaoka, Beauville-Miyaoka, BTVA-span, and same-cover verifiers and executes them during a repository replay.

The active sub-obligation is

`MB104_CUBOID_SPECIFIC_ORDINARY_SINGULARITY_OR_GLOBALIZATION_BOUND`.

A closing input must be genuinely global and cuboid-specific. Examples include:

- `n_ot<=alpha*d+beta` with `alpha<1`;
- a global jet/interpolation theorem excluding the repaired scaling profile in the actual Picard linear systems;
- an upper bound on the shared Beauville ramification with sufficiently small slope;
- a genuinely distinct modular cover with independently chargeable ramification;
- a global irreducibility/member theorem that forbids the surviving analytic profile;
- or a subunit-slope bound on `M` or `s_min`.

For fixed `d`, MB103 symmetry, Hodge pruning, A1 debt, and the new exact BTVA projective-span filter can all be used. The degree direction is not yet bounded, so finite Picard enumeration remains unreleased.

## Firewalls

No Freitag--Salvati Manni unibranch `176/192` cap is imported into the multibranch population. Surface nodes traversed by the image curve are not identified with ordinary self-nodes of the strict transform. The two factor directions are not treated as independent Beauville covers. Effectivity of `D_k` is not promoted to existence of an integral low-genus member. No finite degree window, `R29-LG2-MB` discharge, receiver/effectivity/final-milestone/theorem/endpoint/Stage32/Perfect-Cuboid credit is claimed. Merge remains unauthorized.
