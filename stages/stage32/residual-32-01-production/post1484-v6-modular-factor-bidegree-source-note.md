# Stage32 post-1484 V6 modular-factor bidegree source note

Scope: fixed recovered V6 class only, target `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`. This note does not claim existence of an integral genus-one carrier. It supplies the source/geometry lock for the modular-factor fiber classes used by the accompanying exact replay.

## Pinned modular geometry

Primary source: Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495v1 / DOI 10.1307/mmj/1480734014.

Use only the following source facts.

1. Section 2 defines `Delta(4,8)` and Theorem 2.4 identifies the complex box variety with `(X(8) x X(8))/(Gamma[4]/Gamma[8])`, where the order-eight group acts diagonally.
2. Hence each factor projection descends to a morphism from the box variety to `X(4)=X(8)/(Gamma[4]/Gamma[8])`.
3. Proposition 2.5 gives the local node model. At the standard singular cusp one may use `p=exp(2*pi*i*z/8)`, `q=exp(2*pi*i*w/8)` and the stabilizer generator acts by `(p,q)->(-p,-q)`.
4. Proposition 2.7 identifies the 12 Satake-boundary elliptic curves as the two factor-cusp families. The retained Stage32 Satake marking source-locks these to labels 33..44 and splits the six first-factor labels from the six second-factor labels.

For `X(8)->X(4)`, the cusp widths are 8 and 4. Equivalently the source-locked element `T^4:z->z+4` sends the `X(8)` cusp parameter `p` to `-p`, so an `X(4)` cusp parameter is `u=p^2`. The same statement holds in the second factor with `q`.

## Resolved fiber divisor at a node

The node invariant ring is

`C[p,q]^{+/-1} = C[x,y,z]/(xz-y^2)`, with `x=p^2`, `y=pq`, `z=q^2`.

Let `L_p` and `L_q` denote the strict transforms of the two boundary axes and let `E` be the exceptional curve of the minimal A1 resolution. The total transforms of the two factor cusp parameters are

`div(x) = 2 L_p + E`,

`div(z) = 2 L_q + E`.

This can be checked directly on the two standard resolution charts. On the chart `p=q s`, write `Z=q^2`; then `x=Z s^2`, `y=Z s`, `z=Z`, so `div(x)` has coefficient one on `E:{Z=0}` and coefficient two on `L_p:{s=0}`. The other chart gives the symmetric formula for `z`.

Therefore, on the resolved box surface, the fiber over an `X(4)` cusp represented by a retained first-factor boundary curve `L` is

`F_z(L) = 2 L + sum_{E_j incident to L} E_j`,

and analogously for a second-factor boundary curve

`F_w(L) = 2 L + sum_{E_j incident to L} E_j`.

The retained exceptional-incidence certificate proves that every retained boundary label 33..44 has exactly eight incident exceptional curves, so these are exact integral fiber divisors rather than heuristic local corrections.

## Exact V6 intersections

The recovered V6 all-140 pairing vector and the retained 48-node incidence give the following identity for every boundary curve in each factor family:

- first factor labels `34,35,38,39,42,43`: `C.F_z = 105`;
- second factor labels `33,36,37,40,41,44`: `C.F_w = 81`.

Thus any integral curve in the exact V6 class has nonconstant modular factor maps from its normalization `N` to `X(4)` of degrees

`m_z=105`, `m_w=81`.

The positivity of these intersections rules out a constant factor map for a curve in this class.

## Transport to the product-cover projection degrees

Let `D` be a connected normalized pullback component used in the Stage32 product-cover argument. Write `q' in {1,2,4}` for its degree over the connected Beauville pullback `Y`; since `Y->N` has degree two, `D->N` has generic degree `q=2q'`.

For either factor there is a commuting diagram

`D -> X(8)`

`|      |`

`N -> X(4)`

with `deg(X(8)->X(4))=8`. If `n_i` is the degree of `D->X(8)` and `m_i` the corresponding degree of `N->X(4)`, equality of the two composite generic degrees gives

`8 n_i = 2 q' m_i`, hence `n_i = q' m_i / 4`.

For `(m_z,m_w)=(105,81)` this has the exact consequences:

- `q'=1`: both projected degrees are nonintegral, impossible;
- `q'=2`: both projected degrees are nonintegral, impossible;
- `q'=4`: `(n_z,n_w)=(105,81)`.

For `q'=4`, Riemann--Hurwitz for `D->X(8)` gives `q'O >= 8 n_i` for each projection. The first factor therefore gives

`4 O >= 8*105`, so `O>=210`.

This is strictly stronger than the previously audited `O>=188` wall for this fixed class and in particular excludes every exact `O=188` product-cover profile, including the previously retained q'=4 B/C named-host frontier.

At the new extremal value `O=210`, the first projection has ramification remainder `4*210-8*105=0`. The local cusp lower-bound adapter then forces every odd contact to have multiplicity one and every even contact to have multiplicity two. Since the total exceptional mass is 266, the unique extremal contact histogram is

`210 x m1 + 28 x m2`.

The second projection has source ramification remainder `4*210-8*81=192`; after the V4 etale descent this is ramification degree 48.

## Firewalls

- The fiber-class calculation is intersection theory for the exact V6 class; it does not prove an integral curve exists in that class.
- `O>=210` is a necessary condition, not a carrier existence statement.
- The `O=210` histogram is an exact necessary extremal profile. A nodewise integer split is not analytic realization.
- The prior O=186 audited exclusion and cusp-budget canonical `318ac76c...` are not reopened.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
- Promotion of the new `O>=210` boundary requires bounded hostile audit.