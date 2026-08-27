# Stage32-18AD — adaptive b16 c48x512 tail rescue

Stage32-18AC generation 1 completed successfully but closed only 32/48 logical x16 classes. Of 44 x256 rescue children, 28 were COMPLETE and exactly 16 remain explicit `RESOURCE_WALL_NODE_CAP` walls. 18AD preserves every completed ancestor and refines only those 16 walls.

For fixed primary `h54 mod 1024`, an `h48 mod 256 == s` class is exactly the disjoint union of `h48 mod 512 == s` and `h48 mod 512 == s+256`. Therefore 18AD requires 32 new heavy children rather than any global x512 sweep.

Frozen predecessor:

- 18AC branch head at handoff: `02eee493c77c30e1f020821cdd5c6d6243d9804d`;
- 18AC run `33056615975`;
- 18AC summary artifact `9641903146`;
- 18AC summary digest `sha256:8ffc77a50851d540985ff6dc0f4085fc655e62e7163bda76ae0fbaa80a8755f4`;
- logical x16 classes already closed: `32/48`;
- source x256 node-cap walls: `16`;
- new x512 children: `32`.

Frozen x256 walls:

- p436: `[176,115,5,106,190]`;
- p503: `[144,147,118,153,237]`;
- p922: `[32,17,115,38,13,78]`.

Immutable source:

- x256 run `33056615975`, summary artifact `9641903146`, digest `sha256:8ffc77a50851d540985ff6dc0f4085fc655e62e7163bda76ae0fbaa80a8755f4`;
- prepared exact certifier artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`.

Exact geometry remains bound16 with primary coordinate/modulus `54/1024`, primaries `[436,503,922]`, secondary coordinate48, Aut order1536, 256 DFS symmetry breakers, exact rational branch rejection, and per-child node cap18,000,000.

Operational gates remain mandatory:

- workflow triggers only on the dedicated 18AD run-key path;
- the ARM commit must change only that run key;
- max-parallel15 <= Stage heavy ceiling18;
- current nonexpired artifact storage plus worst-case new evidence must fit 524,288,000 bytes;
- child artifact uncompressed cap 1,000,000 bytes;
- child retention7 days, summary retention14 days;
- node-cap, wallclock, and artifact-size walls remain green resource outcomes rather than mathematical failures.

The final summary source-locks and reloads the frozen 18AC reconstruction certificate and verifies all current x512 child certificates/dumps. Each unresolved logical x16 cell entering 18AD has exactly one x256 wall; therefore that logical cell closes exactly when both x512 children of that wall are COMPLETE.

If all 48 logical x16 classes close, the next item is `32-18AE-D16-B16-RESOURCE-SAFE-EXACT-PRODUCTION-DESIGN`. Otherwise only explicit remaining x512 resource walls may advance to `32-18AE-D16-B16-C48X1024-TAIL-RESCUE`.

This remains refinement **inside b16**. It does not authorize b18 or higher, and it does not grant numerical, theorem, receiver, global-aggregation, or controller credit.

Firewalls remain false:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
