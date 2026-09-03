# Stage32 post-1490 — Beauville blow-up/double-cover Picard adapter and exact delta lock

## Scope

This note stays on the fixed recovered V6 class `g1-d186`, `z=(-15,62,-44,26,32)`, with `O=210`, `q'=4`.
It does not assert that the retained integral Picard class is effective. It is a conditional class-binding statement: if the still-hypothetical integral genus-one carrier exists in the exact recovered V6 class, then its Beauville pullback divisor on `X` has the exact self-intersection computed below.

## Retained source locks

1. `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`
   - canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`
   - exact resolved-box Picard self-intersection `C^2=758`
   - the last 48 entries of the locked all-140 pairing vector are the exceptional intersections `m_j=C.E_j`.

2. `stages/stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md`
   - blob `cb20a9b287430c2e238f79d3151500c262905468`
   - source-locks the Freitag–Salvati Manni quotient geometry: after blowing up the 48 fixed points upstairs and the 48 nodes downstairs, `pi:Xtilde -> Btilde` is a double cover ramified along the 48 exceptional curves.
   - it also source-locks that the exact recovered V6 last-48 vector is the exceptional intersection vector.

3. `stages/stage32/residual-32-01-production/post1490-o210-q4-deck-action-object-mismatch-correction.json`
   - canonical `d652154f42aca4524ed37f2f38363c2c662e2ee63bd814419d716148b71de578`
   - explicitly requires an `B -> X` pullback/strict-transform adapter including exceptional/branch corrections before B-side Picard data can be used on `Pic(X)`.

4. `stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json`
   - canonical `cdc186f8da6eff760a79f98b50106de19d565ebf806dc58b00cc105e4d983af2`
   - on the current X-side divisor `D`, `D^2=-162+2*delta_D` and `delta_D+c_u+c_v+c_uv=8586`.

5. `stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-character-hodge-index-global-constraint.json`
   - canonical `b5d66b6adfe518880bc376825c4990197a8ba20786967ec260352346b06e7855`
   - for every nontrivial deck element, `delta_D-80 <= c_t <= 4333-delta_D`.

## Exact adapter

Let `beta:Xtilde -> X` be the blow-up of the 48 fixed points and let `pi:Xtilde -> Btilde` be the resolved degree-two quotient.
For a hypothetical carrier `C` in the exact recovered V6 class, the connected Beauville pullback has strict transform

`Dtilde = pi^* C`.

Projection formula for the finite degree-two map gives

`Dtilde^2 = 2 C^2`.

Let `Etilde_j` be the exceptional curve above the j-th fixed point and `E_j` its branch exceptional curve on `Btilde`.
The local quotient is the resolved `A1` model, so `pi|Etilde_j:Etilde_j -> E_j` has degree one. Therefore

`Dtilde.Etilde_j = C.E_j = m_j`.

Under the blow-down `beta`, these are exactly the multiplicities of `D` at the 48 blown-up fixed points, hence

`D^2 = Dtilde^2 + sum_j m_j^2 = 2 C^2 + sum_j m_j^2`.

This is the missing exceptional-correction adapter. It does not identify an arbitrary B-side Picard64 class with `Pic(X)`; it applies only to the exact recovered V6 class under the hypothetical-carrier condition above.

## Exact arithmetic

The locked last-48 exceptional vector is

`[1,1,1,2,2,0,1,2,8,4,7,2,9,5,1,10,5,11,7,1,3,1,13,1,6,2,12,16,4,3,5,6,5,10,8,1,10,15,11,2,5,11,4,10,2,4,3,13]`.

It has

- `sum m_j = 266`,
- `sum m_j^2 = 2358`,
- `sum binom(m_j,2) = 1046`.

With `C^2=758`,

`D^2 = 2*758 + 2358 = 3874`.

Combining with the exact X-side formula `D^2=-162+2*delta_D` gives

`delta_D = 2018`.

Thus

`c_u+c_v+c_uv = 8586-2018 = 6568`.

The Hodge character inequalities collapse to

`1938 <= c_t <= 2315`.

Equivalently, for `r_t=2315-c_t`,

`r_t >= 0`, `r_u+r_v+r_uv=377`,

and the three nontrivial V4-character eigenvalues/squares are

`lambda_t = -2-4*r_t`,
`E_t^2 = -8-16*r_t`.

The componentwise lower budget is now `2018+3*1938=7832`, leaving only `754` units above the individual Hodge floors, versus the previous corridor slack `4642`.

## Firewalls

- This does not prove effectivity, integrality, irreducibility, or existence of the carrier.
- The post-21bl representative sample is not substituted for the exact recovered V6 class.
- No arbitrary B-side Picard64 deck action is promoted to `Pic(X)`.
- No retained tangent/local-jet search is reopened.
- `O=210` is not excluded by this adapter alone.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
