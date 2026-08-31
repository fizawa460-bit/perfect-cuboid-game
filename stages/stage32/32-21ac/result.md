# Stage32-21ac — cheap exact anti-fixed coset pruning predicate

Status: `CLOSED_AUDITED`

## Result

`PASS_STAGE32_21AC_CHEAP_EXACT_ANTIFIXED_COSET_BOUND`

For a fixed projected slice, integer rank-2 free coordinates `(u,v)` move the Reynolds residue only inside one exact 128-element subgroup coset `C`. Define

`lambda_C = min_{r in C} lambda_32-21aa(r)`.

Because 32-21aa proves `lambda(r) <= -q^2`, every integral lift in that slice satisfies

`x^2 <= p^2 - lambda_C`.

The existing exact rank-2 concave integer-QP evaluator can therefore be reused with required projected threshold `lower + lambda_C`; the rational threshold is scaled to integers, so no floating-point root or comparison is used.

Exact package CI run `33308996594`, job `99250520551` certified:

- projection classes: `16384`;
- free subgroup order: `128`;
- quotient cosets: `128`;
- positive minimum-penalty cosets: `127`;
- zero minimum-penalty cosets: `1`;
- minimum positive coset lower bound: `1/572`;
- canonical 32-21ac certificate SHA256: `2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e`;
- package artifact `9731412581`, size `3008` bytes.

Fresh boundary audit run `33309333080`, job `99251414877` passed after independently reconstructing the finite quotient and all coset minima. Audit SHA256: `5dfd1087d7d1c20baa3475e05e1768edbb9e8f063b20d01ca467a6725b657f1e`.

The audit's 81-case synthetic Smith panel found `old rank2 false -> new true = 0` and `old true -> new false = 1`. This demonstrates nontrivial strengthening only on the audit panel; it is not a FULL178 numerical census result.

## Safe semantics

A negative 32-21ac decision rigorously prunes the original integral Picard slice. A positive decision remains only a necessary-condition survivor.

## Firewalls

- FULL178 census run: false;
- terminal-family materialization: false;
- 59-dimensional anti-fixed CVP: false;
- legacy prefix DFS re-arm: false;
- UNKNOWN is not UNSAT;
- numerical row complete: false;
- theorem / receiver / route credit: false;
- perfect-cuboid existence/nonexistence claims: false.

The aa->ab->ac package is now an audited checkpoint. `32-21ad` remains blocked until this checkpoint PR is merged and a separate execution phase is opened.
