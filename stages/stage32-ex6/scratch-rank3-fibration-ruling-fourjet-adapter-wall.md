# Stage32EX6 scratch — rank-3 fibration ruling / four-jet adapter wall

Status: `SCRATCH_EXACT_BOUNDED_RANK3_RULING_GLOBALIZATION_FOURJET_ADAPTER_WALL_NO_ENDPOINT_CREDIT`

This is a scratch diagnostic only.  It does not update `MAIN-STATE`, does not
exclude O266, does not authorize O264 descent, and carries no hostile-audit or
Stage32 MAIN credit.

## Source locks

- audited/retained EX6 source head inspected here:
  `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`
- pinned Stoll--Testa verification source:
  `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- pinned `Cuboids/cuboids.magma` blob:
  `0422b69847f2afb97cb7b3ed02ebef91279f61b1`
- retained current V6 witness:
  `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`
- retained AN local A1 source note:
  `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`
- Stoll--Testa, *The surface parametrizing cuboids*, arXiv:1009.0388v2.

The six rank-three quadrics are the three

`q_j = a_j^2 + b_j^2 - c^2`

and the three complementary rank-three quadrics `r_j`; their singular loci meet
the box surface in six disjoint eight-node sets.  This diagnostic uses only the
rank-three-cone local algebra below plus the standard pencil divisor relation.

## 1. A rank-three fibration algebraizes its exceptional ruling coordinate

Use `q_1=0` as representative.  Put

`X = c+a1`, `Y = c-a1`, `B = b1`.

Then exactly

`XY = B^2`.

The Stoll--Testa fibration parameter can be taken as

`T = (c+a1)/b1 = X/B`.

On the A1 resolution chart

`B = X*u`, `Y = X*u^2`,

so, identically,

`T = 1/u`.

Thus the exceptional ruling/slope coordinate `u` is not merely analogous to a
global fibration coordinate: for the rank-three cone it is algebraized by the
global pencil, up to the fixed Möbius transformation `u -> 1/u`.

The coordinate permutations/automorphisms carrying the six rank-three quadrics
to one another give the analogous statement for all six eight-node base sets.

## 2. Four-flatness in the rank-three chart has a genuine RH charge

Let a hypothetical genus-one V6 normalization branch meet one of these base
exceptionals minimally and use the local normalization parameter `x`.  Write

`u(x) = lambda + c1*x + c2*x^2 + c3*x^3 + c4*x^4 + O(x^5)`.

Define **rank3-four-flat** at this branch by

`c1=c2=c3=c4=0`, equivalently `u-lambda = O(x^5)`.

Since `T` is a Möbius transform of `u` with nonzero derivative at finite nonzero
`lambda`, rank3-four-flatness implies

`T-T0 = O(x^5)`.

Hence the local degree of the induced map to `P1` is at least five and the local
Riemann--Hurwitz ramification contribution is at least four.

For one rank-three base block let

`M = sum of the eight exceptional intersection multiplicities`.

For V6 degree `d=186`, the rank-three pencil relation

`2F = H - sum_{base} E`

gives

`n := C.F = (186-M)/2`.

Because the normalization has genus one, the full RH ramification degree of the
map `N -> P1` is

`deg R = 2n = 186-M`.

Therefore, if `m4` of the branches over that eight-node base block are
rank3-four-flat, then

`4*m4 <= 186-M`,

so exactly

`m4 <= floor((186-M)/4)`.

Also trivially `m4 <= M`.  Thus the block capacity is

`m4 <= min(M, floor((186-M)/4))`.

This is a genuine global ramification charge; unlike the branch-dependent local
rulings in the preceding scratch leaf, the rank-three ruling is one fixed global
pencil.

## 3. Current six-block mass ledger is not yet promoted to exhaustive credit

The retained V6 exceptional mass is 266.  The current sampled EXC/block adapter
from the preceding bounded inspection gives the six contiguous eight-node mass
sums

`[10,46,42,54,62,52]`

and corresponding pencil degrees

`[88,70,72,66,62,67]`.

If that EXC-to-rank3-block adapter is confirmed 48/48, the rank3-four-flat
capacities would be

`[10,35,36,33,31,33]`,

with total capacity

`178`.

Since O266 retains at least 186 minimal branches, this would imply that at least
8 minimal branches are **not** rank3-four-flat.

However the large retained exceptional-coordinate certificate is deliberately
not whole-fetched, and the compact generated side-coordinate JSON is not retained
at the inspected #1715 head.  Therefore the exact 48/48 EXC-to-six-rank3-block
numbering adapter is still unmaterialized in this scratch chain.  The number 178
is consequently conditional here and must not be used as endpoint credit.

## 4. More importantly: AN four-flatness is not yet rank3 four-flatness

AN uses the modular/FSM A1 chart

`x=p^2`, `y=pq`, `z=q^2`, with exceptional slope `u_AN=q/p`.

The rank-three cone above has its own algebraic A1 chart and slope `u_rank3`.
Their restrictions to the exceptional curve can be related by a Möbius
coordinate change, but a zero-jet identification on `E` does **not** identify the
coefficients of

`u-lambda` through orders `x,x^2,x^3,x^4`.

Normal-direction coordinate corrections can alter those four coefficients.
Therefore the previously obtained AN/formal four-flat condition cannot yet be
charged into the rank-three RH budget.

A sufficient missing adapter would be, in compatible normal coordinates,

`u_rank3 - M(u_AN) = O(x^5)`

for a fixed Möbius `M`, or an invariant replacement proving that AN four-flatness
forces rank3-four-flatness.

This is now the precise load-bearing bridge.

## Canonical scratch conclusions

- `SIX_RANK3_FIBRATIONS_GLOBALIZE_THEIR_OWN_EXCEPTIONAL_RULING = true`
- `RANK3_FIBRATION_PARAMETER_IS_MOBIUS_OF_RANK3_A1_SLOPE = true`
- `RANK3_FOURFLAT_BRANCH_RH_COST_AT_LEAST = 4`
- `RANK3_BLOCK_FOURFLAT_CAPACITY = min(M,floor((186-M)/4))`
- `EXC_TO_SIX_RANK3_BLOCK_ADAPTER_48_OF_48 = UNMATERIALIZED`
- `CONDITIONAL_SAMPLED_SIX_BLOCK_CAPACITY_TOTAL = 178`
- `AN_TO_RANK3_SLOPE_FOURJET_ADAPTER = UNTESTED`
- `AN_FOURFLAT_IMPLIES_RANK3_FOURFLAT = false_as_current_credit`
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`
- `O266_ENDPOINT_EXCLUDED = false`
- `O264_DESCENT_AUTHORIZED = false`

## Next exact micro-leaf

Either:

1. materialize a compact 48/48 EXC-to-six-rank3-base certificate without
   whole-fetching the 118904-byte retained tangent certificate; or
2. compute the formal coordinate transition between the AN modular A1 chart and
   one rank-three cone chart through normal order four.

The second route is mathematically more load-bearing: a four-jet-compatible
transition would turn the existing formal-neighborhood question into a fixed
global RH budget.
