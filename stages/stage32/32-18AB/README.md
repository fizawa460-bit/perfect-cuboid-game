# Stage32-18AB — adaptive b16 c48x128 tail rescue

Stage32-18AA closed 42 of its 68 x64 rescue children and raised exact logical x16 closure to 23/48. Exactly 26 x64 classes remained as explicit `RESOURCE_WALL_NODE_CAP` walls. 18AB preserved every COMPLETE x16/x32/x64 component and refined only those 26 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 64 == s` class is exactly the disjoint union of `h48 mod 128 == s` and `h48 mod 128 == s+64`. Therefore only 52 new heavy children were required, not a full 384-child x128 sweep.

## Frozen sources

- 18Y x16 run `33030066426`, summary artifact `9631617459`;
- 18Z x32 run `33035492820`, summary artifact `9633913882`;
- 18AA x64 run `33041481560`, summary artifact `9635756996`;
- 18AA summary digest `sha256:c54356b49dd09ee2e96770baca0ec69a68e7a433bd20f3213fcbc3848b2257b5`;
- prepared certifier artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`;
- immutable Aut group order `1536`, DFS symmetry breakers `256`.

The 26 source x64 walls were exactly:

- p436: `[48,51,5,6,57,42,59,60,62,15]`;
- p503: `[16,19,54,25,10,12,45,63]`;
- p922: `[32,17,51,38,13,14,15,31]`.

## Frozen generation-1 result

Workflow run `33046646974` completed successfully. Summary job `98445454202` reloaded the complete x16/x32/x64 ancestry and all 52 current x128 children, verified source locks, binary framing/hashes, duplicate-freedom, and reconstructed histograms.

Summary artifact:

- id `9637483930`;
- name `stage32-18ab-b16-adaptive-x128-rescue-summary-g1`;
- ZIP SHA256 `ae45e1125ecbeae3571c0f9e3cfa1d0247890b6fa28b625c7a2b20a57f096c65`;
- size `1886` bytes.

Exact outcome:

- new x128 children: `52`;
- x128 COMPLETE: `30/52`;
- remaining resource walls: `22/52`, all `RESOURCE_WALL_NODE_CAP`;
- logical x16 closure: `26/48` (up from `23/48`);
- no wallclock or artifact-size wall appears in the frozen remaining set;
- all three primaries still contain at least one unresolved logical class.

Remaining x128 walls are exactly:

- p436: `[48,115,5,57,106,123,124,62,15]` (9);
- p503: `[16,19,118,25,109,127]` (6);
- p922: `[32,17,115,38,13,78,15]` (7).

Frozen verdict:

`B16_TAIL_GEOMETRY__ADAPTIVE_C48X128_INSUFFICIENT__FINER_SPLIT_REQUIRED`

Frozen next item:

`32-18AC-D16-B16-C48X256-TAIL-RESCUE`

Only these 22 explicit x128 walls may be refined. Every COMPLETE x16/x32/x64/x128 component is immutable evidence and must not be recomputed merely to raise the split modulus.

This continuation is still inside the b16 calibration stop contract: it does **not** authorize b18 or any larger norm bound. Once the b16 pilot tail closes, Stage32 must move to resource-safe full-b16 exact production/audit and then the mandatory frozen-census feasibility gate.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
