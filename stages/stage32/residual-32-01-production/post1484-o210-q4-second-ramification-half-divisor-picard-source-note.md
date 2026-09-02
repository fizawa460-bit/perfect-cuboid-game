# Stage32 post-1484 O210 q'=4 second-ramification half-divisor Picard source note

Scope: fixed recovered V6 class only, target `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`, at `O=210`, `q'=4`. This note starts from the exact 24-unit local-excess decomposition and identifies its global line-bundle class. It does not exclude or construct a carrier.

## Fixed geometry

Write

- `pi:Y->N` for the common connected quadratic cover forced by the Cartesian identity;
- `f1,f2:Y->C0` for the two descended maps of degrees `105,81`;
- `h:C0->X(4)=P1` for the degree-two quotient;
- `z,w:N->P1` for the two modular factor maps.

The Cartesian square gives

`h o f1 = z o pi`,

`h o f2 = w o pi`.

The retained V4 quotient certificate gives `g(C0)=2`, `deg(h)=2`, and six branch/Weierstrass points. Therefore `h` is the genus-two hyperelliptic map and its degree-two pencil is the canonical pencil:

`K_C0 ~= h^* O_P1(1)`.

The first descended map has total ramification zero; the second has ramification divisor `R2` of degree 48.

## Define the degree-24 divisor on N

Use the local-excess notation from the preceding certificate.

At each exceptional contact `P`, write `A2=m+2k_P`, `k_P>=0`.

At each second-factor strict-boundary-only point `Q`, write `r_Q>=1` for the strict-boundary intersection multiplicity.

At each away-from-cusp ramification point `S` of `w`, write `e_S>=2` for its local degree.

Define the effective divisor on `N`

`E = sum_P k_P P + sum_Q (r_Q-1) Q + sum_S (e_S-1) S`.

The exact local budget proves

`deg(E)=U_exc+U_strict+U_away=24`.

## Exact divisor pullback identity R2 = pi^* E

Check each local type.

1. Exceptional `m=1`: `pi` is ramified. The unique point upstairs has second-map ramification coefficient `2k_P`, while `pi^*(P)=2 P_Y`; hence the local contribution is `pi^*(k_P P)`.
2. Exceptional `m=2`: `pi` is unramified with two points upstairs, each with ramification coefficient `k_P`; this is `pi^*(k_P P)`.
3. Strict-boundary-only point: `pi` is unramified with two points upstairs, each with ramification coefficient `r_Q-1`; this is `pi^*((r_Q-1)Q)`.
4. Away from the six cusps: the common quadratic cover is etale, and the two lifted points each have ramification coefficient `e_S-1`; this is `pi^*((e_S-1)S)`.

Therefore, as divisors on `Y`,

`R2 = pi^* E`.

## Canonical-bundle comparison

Riemann--Hurwitz for the two maps gives

`K_Y ~= f1^* K_C0`

because `f1` is etale, while

`K_Y ~= f2^* K_C0 tensor O_Y(R2)`.

Hence

`O_Y(R2) ~= f1^*K_C0 tensor f2^*K_C0^{-1}`.

Using `K_C0 ~= h^*O(1)` and the two commuting squares,

`f1^*K_C0 tensor f2^*K_C0^{-1}`

`~= pi^*( z^*O(1) tensor w^*O(-1) )`.

Together with `R2=pi^*E`,

`pi^* O_N(E) ~= pi^*( z^*O(1) tensor w^*O(-1) )`.

## Why pullback on Pic(N) is injective here

The cover `pi:Y->N` is connected and ramified: the O210 profile has 210 odd exceptional contacts, exactly the branch points of the quadratic Beauville pullback.

Suppose a line bundle `L` on `N` has `pi^*L` trivial. Norm gives `L^2` trivial. If `L` were a nontrivial 2-torsion line bundle, it would define a connected etale quadratic cover `N_L->N`. Triviality of `pi^*L` means that etale double cover becomes split after pullback to `Y`, equivalently `pi` lifts through `N_L`. Since both covers have degree two over `N`, that lift would identify `Y` with the etale cover `N_L`, contradicting that `pi` is ramified. Thus `L` is trivial.

So `pi^*:Pic(N)->Pic(Y)` is injective, and the preceding equality descends to the exact identity

`O_N(E) ~= z^*O_P1(1) tensor w^*O_P1(-1)`.

Its degree check is

`deg(E)=105-81=24`.

## Consequence and firewall

This turns the 24-unit ramification budget into one fixed degree-24 Picard class on the hypothetical genus-one carrier. The remaining condition is not merely a partition of 24: that class must admit an effective representative whose support/coefficient pattern is exactly the exceptional-endpoint / strict-tangency / off-cusp pattern allowed by the common resolved-surface geometry.

There is still no standalone exclusion. On a genus-one curve every line bundle of positive degree 24 has nonzero sections (indeed `h^0=24`), so effectivity of the abstract class alone is automatic. Any further obstruction must use the restricted support, the fixed V6 surface realization, or another simultaneous-correspondence constraint.

The old O188 and 93/93 routes remain closed. No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows. Promotion requires bounded hostile audit.
