# Stage32EX6 — rank-4 degree-113 fibration preflight and O266 adapter wall

Status: **EXPLORATORY EXACT BOUNDED WALL — NO MAIN CREDIT**.

This note records a re-entry preflight after the first `O266_ENDPOINT_NOT_CLOSED` decision. It does not reopen Stage32 MAIN and does not claim O266 exclusion.

## Source locks

Primary geometric source:

- Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, Section 5 (fibrations in curves of genus 5).
- The source states that the eleven rank-4 quadrics give two complementary genus-5 fibrations each. For the last four rank-4 quadrics the maps are morphisms on the singular box surface. Each such fibration has six bad fibers splitting into two `G3` curves and four exceptional curves, and twelve further fibers that are hyperelliptic genus-3 curves with two nodes at singular points of the box surface.

Exact computational source locks:

- Stoll–Testa verification repository `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- `Cuboids/Section5_fibrations.log`, blob `9cfef75aa58335655d6ae3e78597f5924b6c2433`;
- V6 canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`;
- V6 all-140 pairings SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`;
- retained Aut group order `1536`;
- Hperp all-140 adapter canonical `fc695b9405ec4becfbcf19866c0c70fceed9372186a5aa4974879f302ee8ffe9`.

Exact replay is

`stages/stage32-ex6/diagnose_stage32_ex6_rank4_fibration_orbit.py`.

## Exact orbit result

The known isotrivial pair has V6 fibration degrees `{81,105}`.

For the other rank-4 types, exact Aut-orbit reconstruction gives:

- next six rank-4 quadrics: `12` fibration classes, maximum V6 degree `104`;
- last four rank-4 quadrics: `8` fibration classes, maximum V6 degree `113`.

The unique degree-113 fibration class has six split `G3` bad-fiber supports. Their union uses exactly the 24 exceptional labels

`101..116` and `133..140`.

The total V6 exceptional mass on those 24 exceptional curves is exactly

`140`.

Thus the new rank-4 search genuinely improves the largest known V6 fibration degree from `105` to `113`. It does **not** reach `133` or `134`.

## Why degree 113 is tempting

If a hypothetical integral V6 carrier has normalization of genus one, restricting a degree-113 fibration gives a map

`Cbar -> P1`

of degree `113`. Riemann–Hurwitz fixes its total ramification degree to

`2*113 = 226`.

At O266 the endpoint contract gives `266` unit odd exceptional contacts. Therefore a proof that **every** O-contact contributes at least one unit of ramification for this rank-4 fibration would give the contradiction

`266 <= 226`.

That implication is not available.

## Exact adapter wall

The O-variable is defined through the Beauville double-cover exceptional contacts. It is not, by definition, the ramification divisor of an arbitrary rank-4 fibration.

The retained AN local model for an endpoint unit contact has FSM type `(A,B)=(1,1)`, exceptional multiplicity `m=1`, and a free nonzero exceptional landing parameter `lambda`. Distinct branches over the same surface node may have distinct landing parameters.

For the degree-113 rank-4 fibration, the six split bad fibers account for exceptional mass `140` on 24 exceptional curves. The Stoll–Testa description and the exact support reconstruction identify these exceptional curves as components joining the two `G3` components of the split fibers. The current retained data do not identify the hypothetical V6 branch landing parameters with the attachment/critical points of those fibers, and do not give a source-locked theorem forcing those 140 unit contacts to contribute positive ramification to `Cbar -> P1`.

Consequently the step

`O=266  =>  R_rank4 >= 266`

is not proved. In particular one may not compare `266` directly with the Riemann–Hurwitz total `226` and declare O266 impossible.

This is a semantic/local-landing obstruction to the naive degree-113 attack, not a claim that no stronger rank-4-fibration argument can exist.

## Decision

Promote only the bounded preflight facts:

- `MAX_RETAINED_RANK4_V6_FIBRATION_DEGREE = 113`;
- `DEGREE113_SPLIT_NODE_EXCEPTIONAL_MASS = 140`;
- `RANK4_DEGREE113_TO_O_RAMIFICATION_ADAPTER = MISSING`;
- `O266_ENDPOINT_EXCLUDED = false`.

A useful re-entry now requires one of:

1. a source-locked identification of V6 exceptional landing parameters with rank-4 special-fiber critical/attachment points;
2. a member-level jet/tangent theorem forcing enough of the 266 unit contacts to ramify under the degree-113 map;
3. a different simultaneous-fibration inequality that does not require the missing per-contact adapter.

## Firewalls

- No Stage32 MAIN authority/state edit.
- Q602/O210 and survivors `[73,97,235]` are unchanged.
- The degree-113 discovery is an exact exploratory fibration fact, not O266 exclusion.
- `O266_ENDPOINT_NOT_CLOSED` remains the EX6 endpoint decision.
- No descent to O264 is authorized.
- No receiver/theorem/endpoint/perfect-cuboid credit.
- No merge is implied.
