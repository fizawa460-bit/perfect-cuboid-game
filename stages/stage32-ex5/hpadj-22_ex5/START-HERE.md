# Stage32EX5 HPADJ22 — exact HPADJ08 deletion-correlation refinement

Status: **FULL178 PRODUCTION READY / COLD / ZERO MAIN CREDIT**

Parent audited producer boundary:

- PR #1818
- HPADJ21 audited exact head: `265fbef0a67014494fcf773af6c3a9f1b095ef95`
- HPADJ21 post-audit MAIN handoff head: `33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2`
- HPADJ21 hostile-audit review: `5242670540`
- HPADJ21 audited candidate upper bound: `157570677819451133507`
- composition: same-population non-additive refinement

## Research OS inheritance

This successor remains governed by the repository-wide Research OS policies, including
`docs/research-os/policies/hostile-audit-and-freshness.md` section 7 for long-lived shared research PRs.

In particular, retained growth on this new PR is measured from this PR's starting boundary / latest hostile-audited checkpoint:

- around 90 unaudited retained commits: enter the warning zone and plan the next intermediate hostile-audit checkpoint;
- no later than the first retained checkpoint at or beyond 100 unaudited retained commits: freeze an exact head and run an intermediate hostile audit before appending further substantive retained research;
- after PASS, the same PR may continue with a fresh audit-debt count from that audited checkpoint;
- scratch/off-PR work does not count until retained into this shared PR.

This is inherited governance only; it grants no mathematical or MAIN credit.

## Route objective

HPADJ21 retains the exact full `q_A` histogram but still relaxes the location of the HPADJ08 whole-block deletions by using post-mass constraints at cell level.

HPADJ22 will test a strictly finer same-population bound by retaining/recomputing the exact HPADJ08 deletion correlation:

`q_A + q_{BC} <= cutoff_g(d)`

and applying the HPADJ21 q/Picard survivor count only to blocks that survive that exact HPADJ08 necessary condition.

This route is a refinement/replacement candidate, **not** an additive subtraction route.

## First exact gate

Before any FULL178 scaleout:

1. formalize the joint `(q_A,q_{BC},support,required parity)` bounded replay;
2. reproduce the frozen HPADJ08 bounded exact-square rejection total on the same scope;
3. reproduce the HPADJ21 bounded objective on the same cells;
4. prove/check pointwise `HPADJ22 <= HPADJ21`;
5. require at least one strict bounded witness;
6. retain zero MAIN credit until hostile audit of any later FULL178 result.

The earlier private bounded measurements are motivation only and are not repository authority.


## Retained bounded result

Exact-head CI run `35292495419` on head `77858ca5f8dde4ad93338e8a0e5a2bae798b120a` established:

- 26 / 26 bounded rows (`d<=32`) are strict versus HPADJ21;
- 208 exact cells are all no-weaker; 36 cells are strict;
- HPADJ08 exact-square rejected mass is reproduced exactly as `25,770,706,503,487`;
- every cell satisfies exact pre/rejected/post conservation against the retained HPADJ21 post-mass certificate;
- HPADJ21 bounded floor sum: `323,299,108,813`;
- HPADJ22 exact correlated survivor sum: `287,982,138,108`;
- bounded strict improvement: `35,316,970,705`;
- retained canonical: `b3387e3f07a02a30bfc5558ad72859c72c25a5289320abd22ac1947bf53b3d77`.

This remains bounded evidence only. The exact b-chunk worker passes direct-vs-split equivalence on both genus-0 and genus-1 d=16 rows (canonical `02ecf8fe47ee8e7a6ec18bbbe784ab3527f9d0e8c1046ea0caf653a088f2554b`).

The FULL178 producer surface is now prepared but intentionally cold:

- exact HPADJ15 b-bands: `[0..11],[12..23],[24..35],[36..47],[48..59],[60..71],[72..83],[84..96]`;
- 178 durable row checkpoints inside each band, so timeout/cancellation resumes only missing rows;
- eight band artifacts maximum, plus compact recovery/final artifacts;
- production max-parallel: 8, with arm-time requirement `other Stage32 heavy concurrency <= 10`;
- final aggregate must reproduce audited HPADJ21 `157570677819451133507` and audited HPADJ08 rejection `40886299509963924857401` exactly before accepting any HPADJ22 candidate;
- production runkey starts at `generation=0, armed=false`.

Storage preflight uses comparable completed evidence instead of requiring a new heavy diagnostic: HPADJ21 run `35279651998` had 59 artifacts with maximum measured chunk artifact `482162` bytes; HPADJ08 run `34935380596` used exactly 8 band artifacts with maximum `6611` bytes. The incomplete noncredit HPADJ22 representative measurement run `35293574861` is discarded/retired and grants no credit.

The only remaining execution action is a distinct production-runkey arm commit after heavy-workflow overlap is acceptable.

## Firewalls

- Stage32 MAIN pruning credit: false
- MAIN consumption performed: false
- additive subtraction: false
- exact incremental rejected identity set claimed: false
- FULL178 complete: false
- effectivity / receiver / route / theorem / endpoint / Perfect Cuboid credit: false
- merge authorization: false

Do not merge. Continue on this PR as the delta-bounded successor to closed PR #1818.
