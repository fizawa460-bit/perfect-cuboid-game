# Stage32-18AB — adaptive b16 c48x128 tail rescue

Stage32-18AA closed 42 of its 68 x64 rescue children and raised exact logical x16 closure to 23/48. Exactly 26 x64 classes remain as explicit `RESOURCE_WALL_NODE_CAP` walls. 18AB preserves every COMPLETE x16/x32/x64 component and refines only those 26 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 64 == s` class is exactly the disjoint union of `h48 mod 128 == s` and `h48 mod 128 == s+64`. Therefore only 52 new heavy children are required, not a full 384-child x128 sweep.

Frozen sources:

- 18Y x16 run `33030066426`, summary artifact `9631617459`;
- 18Z x32 run `33035492820`, summary artifact `9633913882`;
- 18AA x64 run `33041481560`, summary artifact `9635756996`;
- 18AA summary digest `sha256:c54356b49dd09ee2e96770baca0ec69a68e7a433bd20f3213fcbc3848b2257b5`;
- logical x16 classes already closed: 23/48;
- x64 node-cap classes to rescue: 26;
- new x128 children: 52.

The 26 source x64 walls are exactly:

- p436: `[48,51,5,6,57,42,59,60,62,15]`;
- p503: `[16,19,54,25,10,12,45,63]`;
- p922: `[32,17,51,38,13,14,15,31]`.

The immutable exact certifier remains artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Bound16, primary coordinate/modulus 54/1024, secondary coordinate48, exact rational branch rejection, Aut order1536, 256 DFS symmetry breakers, and the 18,000,000-node child cap are unchanged.

The summary must independently reload all frozen x16/x32/x64 evidence, verify the exact 26-wall x64 source set, replace each wall only by its two x128 children, then reconstruct all 48 logical x16 classes. Every COMPLETE component is source-lock checked; canonical dumps use `S32D16C1` framing with 141-byte records; reconstructed unions must be duplicate-free and reproduce their norm histograms.

Operational gates remain mandatory: dedicated ARM-only commit, max-parallel15 <= repository Stage ceiling18, 500MB nonexpired-artifact preflight, 1,000,000-byte child artifact cap, 7-day child retention, 14-day summary retention, and explicit node-cap/wallclock/artifact-size statuses.

If all 48 logical x16 classes close, the next leaf is `32-18AC-D16-B16-RESOURCE-SAFE-EXACT-PRODUCTION-DESIGN`. Otherwise only the remaining x128 resource walls advance to `32-18AC-D16-B16-C48X256-TAIL-RESCUE`.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
