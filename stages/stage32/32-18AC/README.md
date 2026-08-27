# Stage32-18AC — adaptive b16 c48x256 tail rescue

Stage32-18AB generation 1 completed successfully but closed only 26/48 logical x16 classes. Exactly 22 x128 descendants remain as explicit `RESOURCE_WALL_NODE_CAP` walls. 18AC preserves every COMPLETE x16/x32/x64/x128 component and refines only those 22 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 128 == s` class is exactly the disjoint union of `h48 mod 256 == s` and `h48 mod 256 == s+128`. Therefore 18AC requires 44 new heavy children rather than any global x256 sweep.

Frozen predecessor:

- 18AB branch head at handoff: `1fd8691b1d15de6f4883d28891accdd9a2b5d2db`;
- 18AB run `33046646974`;
- 18AB summary artifact `9637483930`;
- 18AB summary digest `sha256:ae45e1125ecbeae3571c0f9e3cfa1d0247890b6fa28b625c7a2b20a57f096c65`;
- logical x16 classes already closed: `26/48`;
- source x128 node-cap walls: `22`;
- new x256 children: `44`.

Frozen x128 walls:

- p436: `[48,115,5,57,106,123,124,62,15]`;
- p503: `[16,19,118,25,109,127]`;
- p922: `[32,17,115,38,13,78,15]`.

Immutable source chain:

- x16 run `33030066426`, summary artifact `9631617459`, digest `sha256:3607380f62285a7c89919f0b184bceb296713b8a18fc7ae81f135e289f79c0f2`;
- x32 run `33035492820`, summary artifact `9633913882`, digest `sha256:d7821ecd335752334b04547ea4b255a0c407914022762574b8a1b88b1027a95c`;
- x64 run `33041481560`, summary artifact `9635756996`, digest `sha256:c54356b49dd09ee2e96770baca0ec69a68e7a433bd20f3213fcbc3848b2257b5`;
- x128 run `33046646974`, summary artifact `9637483930`, digest `sha256:ae45e1125ecbeae3571c0f9e3cfa1d0247890b6fa28b625c7a2b20a57f096c65`;
- prepared exact certifier artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`.

Exact geometry remains bound16 with primary coordinate/modulus `54/1024`, primaries `[436,503,922]`, secondary coordinate48, Aut order1536, 256 DFS symmetry breakers, exact rational branch rejection, and per-child node cap18,000,000.

Operational gates remain mandatory:

- workflow triggers only on the dedicated 18AC run-key path;
- the ARM commit must change only that run key;
- max-parallel15 <= Stage heavy ceiling18;
- current nonexpired artifact storage plus worst-case new evidence must fit 524,288,000 bytes;
- child artifact uncompressed cap 1,000,000 bytes;
- child retention7 days, summary retention14 days;
- node-cap, wallclock, and artifact-size walls remain green resource outcomes rather than mathematical failures.

The final summary reloads all frozen x16/x32/x64/x128 evidence plus the current x256 children. It verifies the exact ancestor wall sets at each level, source locks, `S32D16C1` framing, dump hashes, duplicate-freedom, and reconstructed norm histograms before declaring any logical x16 class COMPLETE.

If all 48 logical x16 classes close, the next item is `32-18AD-D16-B16-RESOURCE-SAFE-EXACT-PRODUCTION-DESIGN`. Otherwise only the explicit remaining x256 resource walls may advance to `32-18AD-D16-B16-C48X512-TAIL-RESCUE`.

This is refinement **inside b16** and does not authorize b18 or higher. The Stage32 goal/stop contract still requires audited full-b16 production followed by the frozen `d<=176/d<=192` feasibility gate before any post-b16 norm escalation.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
