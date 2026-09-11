# Stage32 32-01-178 N355 — full known-prefix block-sum census checkpoint

Status: `AUDIT_REQUIRED`. This checkpoint extends only the already hostile-audited N355 terminal-prefix necessary condition. It does not invent the 38 exceptional pairings absent from the current terminal prefix and does not claim FULL178 completion.

## Audited input

N355 hostile audit review `5165493296` passed exact head `a13a39ba5ec0a281fcd65601f9f75d41405b1da1` for the special-fibre prefix-max necessary cut and the certified label99 diagonal subset. After consuming that audited subset, current MAIN authority is

- `17128` strata;
- `30349852563549761636302131` terminals.

The audited N355 geometry identifies the ten known exceptional prefix labels in the two factor fibrations. On those ten labels the two factor block partitions coincide into the three nonempty known groups

- `{101,102,103}`;
- `{97,98,99}`;
- `{93,94,95,96}`.

Therefore the audited prefix condition `A1+A2<=d` reduces exactly, on the stored known prefix, to

`max(group1_sum, group2_sum, group3_sum) <= floor(d/2)`.

This is a condition only on the ten stored exceptional pairings. The omitted 38 exceptional pairings remain omitted and nonnegative exactly as in the audited N355 monotone partial-block argument.

## Exact census research

`verify_n355_full_prefix_block_sum_census.py` symbolically counts the complete current ten-exceptional prefix predicate while preserving:

- `x0<=x1` and the equal-branch lex symmetry contract;
- the retained parity condition;
- the exact N220 optimistic-support acceptance predicate;
- the audited N354 stratum predicate;
- the normal `x4` block multiplicity;
- exact containment of the already-audited label99 subset.

The dynamic program is independently brute-checked for block caps `h=0,1,2` before the FULL178 census.

CI run `34464153884` / job `102828669004` produced:

- N354 survivor mass replayed: `38560956534397137634780102`;
- audited label99 rejection replayed: `8211103970847375998477971`;
- full known-prefix rejection from N354: `38494493663845949006230192`;
- additional candidate rejection after the audited label99 subset: `30283389692998573007752221`;
- candidate residual: `17128` strata / `66462870551188628549910` terminals;
- per-stratum stream SHA-256: `920e6e0a1e8663b7045f4c56087905400035ca3d1926e37be7b2e777539482e0`;
- canonical result SHA-256: `7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775`.

The retained result is `FULL-PREFIX-RESULT.json`. The workflow regenerates the result and diffs it byte-for-byte against that retained JSON.

## Requested hostile-audit scope

Audit the exact symbolic census and its use of the already-audited N355 geometry. In particular verify:

1. the coincidence of the three nonempty known block groups in both factor directions;
2. the reduction of `A1+A2<=d` to the three group-sum caps on the current ten-exceptional prefix;
3. the unequal/equal branch counting and parity handling;
4. the N220 support-capacity transport;
5. the recordwise containment of the previously audited label99 subset;
6. the exact aggregate partition identities and retained result lock.

If PASS, the maximum allowed new MAIN credit is only

`EXACT_POST_AUDITED_N355_SUBSET_FULL_KNOWN_PREFIX_BLOCK_SUM_CUT_ONLY_30283389692998573007752221_ADDITIONAL_TERMINALS_REMAINING_17128_STRATA_66462870551188628549910_TERMINALS_NO_FULL178_COMPLETION_OR_THEOREM_CREDIT`.

## Firewalls

Until external hostile-audit PASS, current authoritative counts remain `17128 / 30349852563549761636302131`; the `66462870551188628549910` terminal residual is candidate-only. No N350 producer registration, production COMPLETE, N104 release, FULL178 completion, theorem/receiver/endpoint/Stage32 closure, Perfect Cuboid existence/nonexistence claim, heavy-compute authorization, or merge authorization.
