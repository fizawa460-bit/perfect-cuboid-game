# Stage32-18X — b16 real-leaf tail geometry pilot

Accepted predecessor: hostile-audited b14 census (44,450 canonical including zero, dump SHA256 `4d4680a87fab0c01ac8b54bcf404eecaa707cf5db782b31d5fa7357a52249d8a`) and hostile-audited b16 descendant profiles from 18W.

18W shows b16 work through p48 is not more skewed than b14, but b14 history also proves that a benign p48 profile can hide very deep leaf tails. Therefore 18X does not launch full b16 production. It tests actual leaf geometry on the three c54 residues that were the final b14 tails: `436`, `503`, `922`.

For each primary residue the pilot compares:

- direct exact c54 traversal at bound 16 with a 40M-node cap;
- the same fixed c54 residue, partitioned again at coordinate48 into four exact secondary shards, each with the same 40M-node cap.

This is 3 direct + 12 nested = 15 heavy jobs, matching the Stage32 concurrency ceiling. The nested shards preserve the original `h54 mod 1024` gate, so the comparison changes only execution partition geometry, not the mathematical set being enumerated.

If all four nested shards complete, they are unioned exactly; duplicate records are forbidden. If the direct traversal also completes, its binary must equal the sorted four-shard union byte-for-byte. A direct resource wall is allowed pilot evidence. A nested resource wall routes to a finer secondary split rather than to any numerical claim.

Firewalls: `D16_B16_NUMERICAL_CREDIT=false`, `GLOBAL_B16_AGGREGATION_COMPLETE=false`, `FULL_D16_G0_ROW_COMPLETE=false`, `THEOREM_CREDIT=false`, `RECEIVER_CREDIT=false`, `CONTROLLER_MODIFIED=false`.
