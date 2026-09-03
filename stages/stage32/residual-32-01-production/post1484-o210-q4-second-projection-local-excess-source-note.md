# Stage32 post-1484 O210 q'=4 second-projection local-excess source note

Scope: fixed recovered V6 class only, target `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`, at the audited extremal profile `O=210`, `q'=4`. This note refines the exact second-projection ramification accounting. It does not prove or exclude an integral carrier.

## Locked inputs

Use only the following retained inputs.

1. `post1484-v6-modular-factor-bidegree-boundary.json`: modular degrees `(105,81)`, descended `Y -> C0` ramification totals `(0,48)`, first-factor `sum C.L=182`, second-factor `sum C.L=110`, and the unique extremal exceptional histogram `210 x m1 + 28 x m2`.
2. `post1473-o188-cusp-ramification-budget.json`: at an exceptional branch write `A_i=a_i/4` and `m=min(A1,A2)`. Then `A1` and `A2` have the same parity. For odd `m`, `Y->N` is ramified and the descended factor-map local degree is `A_i`; for even `m`, `Y->N` is unramified with two local points and the descended local degree at each is `A_i/2`.
3. `post1484-v6-modular-factor-bidegree-source-note.md`: on the A1 resolution the factor cusp fiber is `2L+sum E`. In the chart `p=q s`, with `Z=q^2`, one has `x=Z s^2`, `z=Z`. Thus at an exceptional endpoint the excess of one cusp exponent over the exceptional multiplicity is twice the intersection multiplicity with the corresponding strict boundary.
4. `post1484-o210-q4-second-projection-ramification-accounting.json`: if `T` is the number of second-factor strict-boundary-only normalization points over the six cusps, then `86<=T<=110`, cusp ramification of the descended second map is `220-2T`, and away-from-cusp ramification is `2T-172`.
5. `post1484-o210-q4-common-double-cover-cartesian-identity.json`: for an actual carrier both factor pullbacks define the same quadratic cover `Y/N`; away from the six cusp values this double cover is etale.

## First descended projection rigidity

The first descended map `Y -> C0` has degree 105 and total ramification zero. Apply this to every exceptional contact.

- If `m=1`, the local adapter gives first-map local degree `A1` at the unique point of `Y`; etaleness forces `A1=1=m`.
- If `m=2`, there are two points of `Y`, each of local degree `A1/2`; etaleness forces `A1/2=1`, hence `A1=2=m`.

Therefore every O210 exceptional contact satisfies

`A1=m`.

Since `A1` and `A2` have the same parity and `A2>=m`, write uniquely

`A2=m+2 k_P`, with `k_P>=0`.

In the resolution chart, `k_P` is exactly the second-factor strict-boundary intersection multiplicity occurring at the exceptional endpoint. The first factor has no endpoint excess.

The same etaleness fixes strict-boundary-only first-factor contacts. If the normalized carrier meets a first strict boundary with multiplicity `r`, then the `N->X(4)` cusp local degree is `2r`; after normalized quadratic base change there are two points of `Y`, each of degree `r` over `C0`. Etaleness forces `r=1`. Hence all first-factor `C.L=182` strict intersections are transverse.

## Exact second-map local ramification units

There are three possible sources of ramification for the descended second map `Y -> C0`.

### Exceptional contacts

At an exceptional contact `P`, write `A2=m+2k_P` as above.

- For `m=1`, the unique point of `Y` has local degree `1+2k_P`, so its ramification contribution is `2k_P`.
- For `m=2`, the two points of `Y` each have local degree `1+k_P`, so their total ramification contribution is again `2k_P`.

Define `U_exc=sum_P k_P`.

### Strict-boundary-only cusp points

Let `Q` be a second-factor strict-boundary-only point and let `r_Q>=1` be its intersection multiplicity with the strict boundary. Since the resolved cusp fiber has coefficient two on the strict boundary, the `N->X(4)` local degree is `2r_Q`. The normalized quadratic base change has two points above `Q`, each of local degree `r_Q` over `C0`, so the descended ramification contribution is

`2(r_Q-1)`.

Define `U_strict=sum_Q (r_Q-1)`.

### Away from the six cusps

At an away-from-cusp ramification point of `N->X(4)` with local degree `e_Q>=2`, the common quadratic cover `Y->N` is etale. Thus there are two lifted points and the descended ramification contribution is

`2(e_Q-1)`.

Define `U_away=sum_Q (e_Q-1)` over away-from-cusp ramification points.

## Global 24-unit identity

The descended second map has total ramification 48. Every contribution above is even, hence

`48 = 2(U_exc + U_strict + U_away)`,

so exactly

`U_exc + U_strict + U_away = 24`.

The second-factor strict-boundary intersection total is 110. The resolution-chart endpoint identity gives

`110 = U_exc + sum_Q r_Q = U_exc + T + U_strict`.

Therefore

`U_exc + U_strict = 110-T`,

while the retained away-ramification accounting gives

`U_away = T-86`.

These sum to 24 identically for every `86<=T<=110`.

Thus the scalar `T` does not close O210, but the entire second-map ramification is now localized into exactly 24 nonnegative integral excess units on the same common-cover geometry: exceptional endpoint excess, strict-boundary tangency, and off-cusp ramification.

## Firewalls and next leaf

- This is an exact local/global decomposition conditional on a hypothetical carrier; it is not a carrier construction.
- It does not exclude O210 by itself. Every `T` in `[86,110]` remains compatible with the scalar budget.
- The old O188 frontier and the old degree-93/93 odd-etale route are not reopened.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
- The next exact leaf is to constrain these 24 units using the simultaneous degree-105 etale / degree-81 ramified correspondence on the same `Y/N` and the fixed V6 resolved-surface class.
