# Stage32-18AA — adaptive b16 c48x64 tail rescue

Stage32-18Z refined only the 38 x16 node-cap parents and obtained 42 COMPLETE x32 children plus 34 explicit x32 node-cap walls. 18AA preserves every COMPLETE x16/x32 piece and refines only those 34 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 32 == s` class is exactly the disjoint union of `h48 mod 64 == s` and `h48 mod 64 == s+32`. Therefore the remaining wall requires exactly 68 new heavy children, not a full 192-child x64 sweep.

Frozen source:

- 18Y x16 run `33030066426`, summary artifact `9631617459`;
- 18Z x32 run `33035492820`, summary artifact `9633913882`;
- 18Z summary digest `sha256:d7821ecd335752334b04547ea4b255a0c407914022762574b8a1b88b1027a95c`;
- x32 COMPLETE children: 42;
- x32 node-cap children to rescue: 34;
- new x64 children: 68.

The immutable exact certifier remains artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Bound16, primary coordinate/modulus 54/1024, secondary coordinate48, exact rational branch rejection, Aut order1536, 256 DFS symmetry breakers, and the 18,000,000-node child cap are unchanged.

The summary must reload frozen x16 and x32 evidence, verify the exact 34-wall source set, replace each wall x32 class only by its two x64 children, and reconstruct each of the 48 logical x16 classes. Only a fully duplicate-free, histogram-consistent reconstruction may declare historical tail geometry closed.

Operational gates: dedicated ARM-only commit, max-parallel15 <= repository Stage ceiling18, 500MB nonexpired-artifact preflight, 1,000,000-byte child artifact cap, 7-day child retention, explicit node-cap/wallclock/artifact-size statuses.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
