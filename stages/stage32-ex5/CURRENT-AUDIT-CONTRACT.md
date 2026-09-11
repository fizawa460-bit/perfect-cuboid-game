# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged. BC2-28 hostile audit **PASS** is exact head `4221d7f9816590e808976da37ba479880f35dc22`, review `5183082213`.

## BC2-29 retained candidate boundary

BC2-29 boundary39 executed exactly once at head `ddbb75a8d07a6d5c8f3a466bb713708b80488efc`, workflow run `34644942182`, authorize job `103413347381`, compute job `103413402930`, artifact `10281797941`. Artifact ZIP digest is `cef9a3e9d6eb748140bb5e8ed5b908ca16361f1c598fd2d7ced0698bb398e762`; artifact raw JSON sha256 is `cf2ff678247cd46efcb9558a1890dd27b1f799831a1b2073ec545d7dea97c50d`; raw canonical is `e3284337761fd966a26a4c8b720b132de7e6a481746343403454707eff28a77b`; retained checkpoint canonical is `e02b94819d44d0d74e5ce393746efcc4b069075f98c4c00ad2895246e941fe1d`.

The bounded result checked all 16 p39 leaves: 15 UNSAT / 1 UNKNOWN / 0 SAT. New parent UNSAT set is `[1048,1050,1103]`; retained UNKNOWN parent is `1064`, with exact residual leaf `n1=2,n2=6,p33=1,p34=3,p35=3,p38=1,p39=3`; known parent-UNSAT lower bound is `7163`; the other `172` BC2-19 UNKNOWN identities remain uninferred. This retained result is **not hostile-audited yet** and grants no Stage32 MAIN/N350/FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid or merge credit.

The generation-1 runkey is consumed/disarmed. The one-shot BC2-29 executor is removed after retention, so ordinary synchronize cannot rerun the bounded computation. The retained checkpoint/verifier source-locks the audited BC2-28 predecessor, BC2-29 producer/manifest/preflight, executed runkey, workflow identity and exact workflow/artifact/raw receipt.

BC2-30 is blocked until a later `stage32ex5-audit` PASS on this exact retained boundary. Merge authorization remains false and independent.
