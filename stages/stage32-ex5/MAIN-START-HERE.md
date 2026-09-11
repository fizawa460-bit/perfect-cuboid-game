# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains the active work/audit surface.

BC2-26 hostile audit PASS is exact head `34d6b030095b97c738f6faf6b9045f366622592c`, review `5177919212`. BC2-27 then executed and is now frozen: 3 new parent UNSAT `[1066,1117,1133]`, known parent-UNSAT lower bound `7155`, `9` retained UNKNOWN parents, and `13` UNKNOWN branches / p33 subbranches / p34 leaves / timeout p35 leaves. The other `172` BC2-19 UNKNOWN identities remain uninferred; SAT count is 0.

Checkpoint canonical: `0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462`. Run `34593864110`, exact compute head `21828bcf36ea33d1e6c26465eea74c646ba26901`.

On `stage32ex5-mainbatch`, replay BC2-25/26/27 retained verifiers and preserve UNKNOWN/firewalls. The next command is `stage32ex5-audit`; BC2-28 is blocked until BC2-27 hostile-audit PASS. No merge or Stage32 MAIN/FULL178/theorem/effectivity/endpoint credit is authorized.
