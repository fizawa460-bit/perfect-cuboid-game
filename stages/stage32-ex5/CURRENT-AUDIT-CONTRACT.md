# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged. BC2-29 hostile audit **PASS** is exact head `ca8e0ea7209b898d24d5f647dcce11be1aff03b2`, review `5183342658`.

## BC2-30 retained candidate boundary

BC2-30 boundary42 executed exactly once at head `53be207f91cfd6b13ee8533efcf0af64bdccf3d6`, workflow run `34647160641`, authorize job `103420588963`, compute job `103420643305`, artifact `10283165917`. Artifact ZIP digest is `3b790a100771ffb52662f5150b8849665e758dccbc4ce991e8124780b9f1ee28`; artifact raw JSON sha256 is `27607fd4266617f78515553832158bbe6b57aeb2a166c306b1ee7f83303117a8`; raw canonical is `61e9ed91020c56fba0d6addda5a31daca09a9765d7472e0ca1190c7d70e49521`; retained checkpoint canonical is `2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a`, blob `deb35f43ba1780e58091b55a1c2e162df8bc0993`.

The bounded result checked the exact boundary42 partition `p42=0..3`: `4 UNSAT / 0 UNKNOWN / 0 SAT`. Parent `1064` is newly UNSAT; **retained UNKNOWN=0**; known parent-UNSAT lower bound is `7164`. The separate `172` BC2-19 UNKNOWN identities remain explicitly uninferred. Consequently this result does **not** prove the whole first block UNSAT and grants no Stage32 MAIN/N350/FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid or merge credit.

The generation-1 BC2-30 runkey is consumed/disarmed. The one-shot BC2-30 executor is removed after retention, so ordinary synchronize cannot rerun the bounded computation. The retained verifier source-locks the hostile-audited BC2-29 predecessor, BC2-30 producer/manifest/preflight, executed runkey, executed workflow identity, checkpoint, and exact workflow/artifact/raw receipt.

BC2-31 is blocked until a later `stage32ex5-audit` PASS on this exact retained boundary. Merge authorization remains false and independent.
