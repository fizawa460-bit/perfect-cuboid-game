# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`.

## Current retained boundary

PR #1776 contains the frozen BC2-27 boundary35 checkpoint. Its predecessor BC2-26 hostile audit PASS is exact head `34d6b030095b97c738f6faf6b9045f366622592c`, review `5177919212`.

BC2-27 refined the 23 BC2-26 residual p34 UNKNOWN leaves with exact `p35=0..floor(n2/2)`, at most 70 leaves. Result: 3 new parent UNSAT `[1066,1117,1133]`; `9` retained UNKNOWN parents; `13` UNKNOWN branches; `13` UNKNOWN p33 subbranches; `13` UNKNOWN p34 leaves; `13` timeout UNKNOWN p35 leaves; 0 SAT. Known parent-UNSAT lower bound is `7155`. The other `172` identities remain uninferred.

Checkpoint canonical: `0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462`; raw result canonical `6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd`; run `34593864110`; exact compute head `21828bcf36ea33d1e6c26465eea74c646ba26901`.

## Next route

Run `stage32ex5-audit` on BC2-27. BC2-28 is blocked until that PASS. UNKNOWN remains UNKNOWN and all `172` unrelated identities remain uninferred. No broad/heavy scale-out, Stage32 MAIN/N350 promotion, FULL178 closure, theorem/effectivity/receiver/endpoint credit, Perfect Cuboid conclusion, or merge is authorized.
