# Stage32 32-01-178 N351 — general factor-Hurwitz mass cap

Status: `AUDIT_REQUIRED`. This is a necessary-condition research adapter only.

## Scope

Let `C` be a hypothetical integral curve on the resolved box surface whose normalization `Cbar` has genus `g in {0,1}`. For either retained factor fibration to `X(4) ~= P1`, let `n>0` be the degree of `Cbar -> P1`.

For the six retained special fibres in that factor direction, write:

- `e` for the total intersection mass with all 48 exceptional curves;
- `q` for the sum of the intersections with the six multiplicity-two boundary elliptics;
- `B` for the total number of normalization preimages lying over exceptional components among those six fibres.

The source-locked resolved fibre formula is

`F_E = 2E + sum(8 incident exceptional curves)`.

The six exceptional 8-sets partition all 48 exceptional curves. Therefore

`6n = 2q + e`.

## Hurwitz inequality

At a normalization point over one of the six special fibres, let `a>=0` be exceptional intersection multiplicity and `b>=0` boundary-elliptic intersection multiplicity. The local fibre pullback order is `a+2b`; its ramification contribution is `a+2b-1` when positive.

Exactly as in the retained post1648AO source note, summing locally gives

`R >= e - B + q`.

Every exceptional preimage counted by `B` has `a>=1`, so `B<=e`. Hence the weaker but vector-independent necessary inequality is

`R >= q`.

Riemann--Hurwitz for `Cbar -> P1` gives

`R = 2g - 2 + 2n`.

Combining with `6n=2q+e` gives

`n <= e/2 + 2g - 2`,

or equivalently the integer linear pack-sum cap

`q <= e + 6g - 6`.

Thus every admissible class must satisfy this cap in **both** factor directions.

For `e=48` this is:

- genus 0: each six-boundary pack sum `q <= 42`;
- genus 1: each six-boundary pack sum `q <= 48`.

## Independence from N349/N260

This contract does **not** use:

- N349 local `(4,4)` equality;
- `[1]^48` exceptional-vector rigidity from N260;
- fixed `x4`;
- self-square;
- N310 or N341.

The exact feasibility adapter may retain only:

- Picard64 integrality;
- all 140 known-curve pairings nonnegative;
- exact exceptional total `sum(labels93..140)=e`;
- exact normal total `sum(labels1..92)=19*d-5*e`;
- the two six-pack caps above.

UNSAT under this relaxed system is a candidate necessary obstruction for the entire `(g,d,e)` stratum. SAT is no existence/member credit. UNKNOWN is zero credit.

## Source lock

Primary retained geometry source:

`stages/stage32/residual-32-01-production/post1648ao-special-fibre-hurwitz-budget-source-note.md`

Git blob at contract creation: `242088adab5c86292154a6de9bc3563ba73b4f43`.

The extension from the source note's displayed genus-1 case to `g in {0,1}` is the standard Riemann--Hurwitz identity `R=2g-2+2n` combined with the same local inequality; this extension is itself part of the N351 hostile-audit scope.

## Firewalls

No N351 MAIN pruning credit before external hostile audit. No N260/N280/N310/N341/N349 promotion, no production-leaf/N104/N350 credit, no FULL178 completion, no theorem/receiver/endpoint/Stage32 closure, no Perfect Cuboid existence/nonexistence claim, and no merge authorization.
