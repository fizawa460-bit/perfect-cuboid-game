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

## Why this is required by N104/N106

N104 requires every canonical terminal rank in every one of the 64,111 exact strata to receive exactly one registered exact disposition, with no gaps, overlaps, extras or unknowns. Renumbering only survivors and discarding the old rank identity would therefore break the completeness authority.

N106 likewise source-locks work-unit identity to a stratum-local `CompressedTerminalIndexer(e,d)` rank domain. N220 may reduce execution load, but it must not silently redefine that audited coordinate.

Therefore every N220 production receipt must retain at least

- locked FULL178 manifest identity;
- `(row_id,d,e)`;
- old canonical local rank or old canonical half-open rank interval;
- exact N220 disposition digest/counts;
- if accepted work is re-sharded by survivor rank, the survivor-rank interval plus an exact mapping certificate back to old canonical ranks.

## Symbolic implementation target

The retained N220 counter already refines exceptional prefixes by exact `(M10,S10)` while preserving the current symmetry/lex/parity grammar. After audit PASS, the implementation target is a prefix-count DP that answers exact accepted-subtree counts under that same grammar.

This supports filtered rank/unrank without materializing the 27-digit family:

1. **rank survivor**: traverse the existing canonical grammar for `x(r)`, summing accepted counts of earlier sibling subtrees;
2. **unrank survivor**: traverse the grammar, choosing the unique child whose cumulative accepted count contains `k`;
3. **old-rank replay**: retain/reconstruct the corresponding old canonical rank using the existing grammar/indexer;
4. **stratum certificate**: prove `rejected_count + survivor_count = old_terminal_count` exactly.

The exact child order of the current production indexer remains a source-lock requirement. This architecture intentionally does not guess or replace that order. Production implementation is blocked until the concrete old-rank grammar/order is located and source-locked, and until N220 itself receives hostile-audit PASS.

## Count factorization retained

Because N220 depends on the ten exceptional prefix coordinates and `(g,d,e)` but not on the normal coordinate `x4`, the accepted count in one stratum still factors as

`(19*d - 5*e + 1) * C_N220(g,d,e)`,

where `C_N220` is the accepted exceptional-prefix count under the exact retained symmetry/lex/parity grammar and N220 predicate.

This is a counting optimization only. It does not change canonical terminal identity.

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

Locate and source-lock the concrete current `CompressedTerminalIndexer(e,d)` canonical child/rank order, then implement an accepted-subtree DP wrapper whose replay verifier checks the four rank identities above and the per-stratum partition equation before any scaled execution is authorized.
