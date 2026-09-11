# Stage32 MB104 — Beauville blow-up/down bridge

Status: **RETAINED GEOMETRY ADAPTER / NO NEW DEGREE CREDIT**.

This note separates two smooth surfaces that must not be conflated in the Beauville-cover route.

Let `S` denote the minimal resolution of the 48-node cuboid canonical surface. Stage32 retains

`K_S^2=16`, `c2(S)=80`,

and 48 disjoint exceptional curves `E_i` with `E_i^2=-2` and `K_S.E_i=0`.

Freitag–Salvati Manni / the retained AL source identifies the Beauville degree-two cover of the singular canonical surface. After resolving the quotient diagram one obtains a finite double cover

`f: Xhat -> S`

branched along

`B=sum_i E_i`.

Write `2L=B`. Since the exceptional curves are disjoint,

`B^2=-96`, `L^2=-24`, `K_S.L=0`.

The standard double-cover canonical formula gives

`K_Xhat = f^*(K_S+L)`

and therefore

`K_Xhat^2 = 2*(K_S+L)^2 = 2*(16-24) = -16`.

Topologically,

`c2(Xhat)=e(Xhat)=2*e(S)-e(B)=160-96=64`,

because `B` is the disjoint union of 48 copies of `P^1`.

For each branch component, `f^*E_i=2R_i`, hence

`R_i^2=E_i^2/2=-1`.

Blowing down the 48 disjoint ramification `(-1)` curves gives the minimal Beauville surface `X`. Thus

`K_X^2 = K_Xhat^2+48 = 32`,

`c2(X) = c2(Xhat)-48 = 16`.

These agree with the independent product quotient description

`X=(C8 x C8)/H_diag`, `g(C8)=5`, `|H|=4` acting freely.

## Carrier adapter

Ramification parity of a carrier branch along an exceptional `E_i` is naturally read in the finite cover `Xhat -> S`. The normalization of the lifted carrier is birationally unchanged when `Xhat -> X` blows down the ambient ramification `(-1)` curves, so its geometric genus is unchanged.

The Miyaoka `K^2>c2` inequality used in `BEAUVILLE-MIYAOKA-COVER-WALL` is applied only on the minimal surface `X`, where `(K^2,c2)=(32,16)`. It is not applied to `Xhat`, where `K^2=-16<c2=64`.

The canonical-degree identity `K_X.Cbar=2d` remains sourced from the two factor fibrations on the minimal Beauville surface, not from incorrectly substituting `K_Xhat`.

## Firewalls

- `Xhat` and `X` are distinct surfaces.
- Branch-divisor intersection/ramification bookkeeping lives on `Xhat -> S`.
- Favorable-Chern Miyaoka bookkeeping lives on minimal `X`.
- This bridge proves no new finite degree window and grants no receiver/theorem/endpoint credit.
- Merge remains unauthorized.
