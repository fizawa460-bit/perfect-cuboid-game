# N220 filtered-rank architecture

Status: **AUDIT-GATED PREPARATION ONLY**. This document does not consume or self-grant the N220 hostile-audit result.

## Goal

If the N220 prefix exceptional-support cut passes hostile audit, use it without destroying the already-audited N104/N106 canonical rank/completeness contracts.

The authoritative pre-N220 domain remains, for each exact `(row_id,d,e)` stratum, the existing local canonical rank interval

`R_old = [0, CompressedTerminalIndexer(e,d).terminal_count)`.

N220 must be represented as an exact disposition of that domain, not as a replacement domain whose old ranks disappear.

## Exact predicate

For one old canonical terminal tuple `x=(x0,...,x10)`, with `x4` the sole normal coordinate, define

- `M10 = sum(x_i for i != 4)`;
- `S10 = count(i != 4 with x_i > 0)`;
- `K = ceil((d-16g+16)/4)`.

The audit-gated N220 acceptance predicate is

`A(x;g,d,e) := S10 + min(38,e-M10) >= K`.

No production code may use `A` as authoritative pruning before hostile-audit PASS.

## Resolved source lock: exact old canonical order

The concrete source is now locked:

`stages/stage32/residual-32-01-production/compressed_terminal_indexer.py`

Git blob:

`4fb0a8dd34909494bd62646373e42877ed7a3c9e`

Its certificate names the order

`EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST`.

More precisely, if `B = normal_budget+1 = 19*d-5*e+1`, then the old indexer implements

`old_rank = exceptional_rank * B + x4`

and

`exceptional_rank, x4 = divmod(old_rank,B)`.

Thus the old canonical order is no longer an unresolved input to this design.

## Preserve canonical rank; add only a secondary survivor rank

For an old canonical rank `r`, let `x(r)` denote the existing exact terminal unrank result.

Define the old-domain disposition

- `N220_REJECTED` if `A(x(r))` is false;
- `N220_SURVIVOR(k)` if `A(x(r))` is true, where

`k = F(r) := # { q in [0,r) : A(x(q)) }`.

Thus `k` is a **secondary filtered execution rank**. It is never the N104/N106 canonical identity.

Conversely, for `0 <= k < S`, where

`S = # { r in R_old : A(x(r)) }`,

define filtered unrank as the unique old rank

`U(k) = min { r : F(r+1) = k+1 }`.

Required identities are

- `F(U(k)) = k`;
- `A(x(U(k))) = true`;
- for every accepted old rank `r`, `U(F(r)) = r`;
- every old rank has exactly one disposition: rejected or survivor;
- rejected and survivor sets are disjoint and their union is all of `R_old`.

## New simplification: preserve every x4 block exactly

N220 depends only on the ten exceptional coordinates and `(g,d,e)`. It does **not** depend on `x4`.

Because `x4` is already the old indexer's innermost coordinate, an exceptional tuple is either accepted for all `B` values of `x4` or rejected for all `B` values.

Let `er` be an old exceptional rank and let

`E(er) = # { prior exceptional ranks q<er accepted by N220 }`.

Then for every accepted old terminal

`old_rank = er*B + x4`

we may define the secondary filtered rank exactly as

`filtered_rank = E(er)*B + x4`.

Filtered unrank is likewise

1. `filtered_exceptional_rank,x4 = divmod(filtered_rank,B)`;
2. unrank only the accepted exceptional-rank axis;
3. restore the same `x4` unchanged.

Therefore N220 filtering never needs to reorder, enumerate, or rebuild the normal-coordinate block. Only the exceptional-rank axis requires an accepted-subtree rank/unrank DP.

## Why old rank remains required by N104/N106

N104 requires every canonical terminal rank in every one of the 64,111 exact strata to receive exactly one registered exact disposition, with no gaps, overlaps, extras or unknowns. Renumbering only survivors and discarding the old rank identity would therefore break the completeness authority.

N106 likewise source-locks work-unit identity to a stratum-local `CompressedTerminalIndexer(e,d)` rank domain. N220 may reduce execution load, but it must not silently redefine that audited coordinate.

Therefore every N220 production receipt must retain at least

- locked FULL178 manifest identity;
- `(row_id,d,e)`;
- old canonical local rank or old canonical half-open rank interval;
- exact N220 disposition digest/counts;
- if accepted work is re-sharded by survivor rank, the survivor-rank interval plus an exact mapping certificate back to old canonical ranks.

## Symbolic implementation target

The retained N220 counter already refines exceptional prefixes by exact `(M10,S10)` while preserving the current symmetry/lex/parity grammar. After audit PASS, implement accepted-subtree counts in the exact source-locked exceptional order:

`UNEQUAL(x0<x1)` followed by `EQUAL(x0=x1)`.

This supports filtered rank/unrank without materializing the 27-digit family:

1. **rank survivor exceptional tuple**: traverse the existing exceptional grammar, summing N220-accepted counts of earlier sibling subtrees;
2. **unrank survivor exceptional tuple**: traverse the grammar, selecting the unique child whose cumulative accepted count contains the requested accepted exceptional rank;
3. **append x4 unchanged** using the exact `B`-sized inner block;
4. **old-rank replay**: reconstruct the old exceptional rank with the existing indexer and then `old_rank=er*B+x4`;
5. **stratum certificate**: prove `rejected_exceptional_count + accepted_exceptional_count = old_exceptional_count`, hence after multiplication by `B`, `rejected_terminal_count + survivor_terminal_count = old_terminal_count`.

A bounded replay implementation is retained at

`stages/stage32/32-01-178/nodes/N220/verify_n220_filtered_rank_small.py`.

It keeps old rank authority and exhaustively checks the filtered-rank roundtrip on bounded `(g1,d8,e=4)` and `(g1,d8,e=5)` cases. This remains preparation, not N220 hostile-audit credit.

## Count factorization retained

Because N220 is independent of `x4`, the accepted count in one stratum factors exactly as

`(19*d - 5*e + 1) * C_N220(g,d,e)`,

where `C_N220` is the accepted exceptional-prefix count under the exact retained symmetry/lex/parity grammar and N220 predicate.

This factorization is now also compatible with the old rank order, not merely with total counting.

## Audit / credit firewall

- N220 hostile-audit PASS: **not yet present** at the time of this checkpoint.
- Production pruning authorized: **false**.
- New canonical rank authority: **false**; old N104/N106 rank remains authoritative.
- Heavy compute authorized: **false**.
- FULL178 complete: **false**.
- Numerical-row/theorem/receiver/endpoint/existence/nonexistence credit: **false**.
- EX5 BC2-02/BC2-03 completion work duplicated: **false**.
- Merge authorized: **false**.

## Next exact implementation step after audit PASS

Implement accepted-exceptional-subtree counts by adapting the source-locked `CompressedTerminalIndexer` branch grammar, then hostile-replay the rank identities and per-stratum partition equation before any scaled execution is authorized.
