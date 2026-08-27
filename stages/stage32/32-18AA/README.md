# Stage32-18AA — adaptive b16 c48x64 tail rescue

Stage32-18Z refined only the 38 x16 node-cap parents and obtained 42 COMPLETE x32 children plus 34 explicit x32 node-cap walls. 18AA preserved every COMPLETE x16/x32 piece and refined only those 34 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 32 == s` class is exactly the disjoint union of `h48 mod 64 == s` and `h48 mod 64 == s+32`. Therefore this rescue used exactly 68 new heavy children, not a full 192-child x64 sweep.

Frozen source:

- 18Y x16 run `33030066426`, summary artifact `9631617459`;
- 18Z x32 run `33035492820`, summary artifact `9633913882`;
- 18Z summary digest `sha256:d7821ecd335752334b04547ea4b255a0c407914022762574b8a1b88b1027a95c`;
- x32 COMPLETE children: 42;
- x32 node-cap children rescued here: 34;
- new x64 children: 68.

Frozen 18AA execution:

- workflow run `33041481560`: SUCCESS;
- summary artifact `9635756996`;
- summary ZIP digest `sha256:c54356b49dd09ee2e96770baca0ec69a68e7a433bd20f3213fcbc3848b2257b5`;
- new x64 COMPLETE children: 42/68;
- remaining x64 resource walls: 26/68, all `RESOURCE_WALL_NODE_CAP`;
- wallclock walls: 0;
- artifact-size walls: 0;
- reconstructed logical x16 classes: 23/48.

Remaining x64 walls are exactly:

- p436: `[48,51,5,6,57,42,59,60,62,15]` (10);
- p503: `[16,19,54,25,10,12,45,63]` (8);
- p922: `[32,17,51,38,13,14,15,31]` (8).

Verdict:

`B16_TAIL_GEOMETRY__ADAPTIVE_C48X64_INSUFFICIENT__FINER_SPLIT_REQUIRED`

Next item:

`32-18AB-D16-B16-C48X128-TAIL-RESCUE`.

18AB must preserve all COMPLETE x16/x32/x64 evidence and refine only the 26 remaining x64 walls. Each `h48 mod 64 == s` wall is exactly the disjoint union of its two x128 children `s` and `s+64`, requiring only 52 new heavy jobs rather than a full 384-child x128 sweep.

The immutable exact certifier remains artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Bound16, primary coordinate/modulus 54/1024, secondary coordinate48, exact rational branch rejection, Aut order1536, 256 DFS symmetry breakers, and the 18,000,000-node child cap are unchanged.

Operational gates remain mandatory: dedicated ARM-only commit, max-parallel15 <= repository Stage ceiling18, 500MB nonexpired-artifact preflight, 1,000,000-byte child artifact cap, 7-day child retention, explicit node-cap/wallclock/artifact-size statuses.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
