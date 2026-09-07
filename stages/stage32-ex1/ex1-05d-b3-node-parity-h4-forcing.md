# EX1-05D — exact b3-node parity adapter and h=4 forcing

Status: provisional same-PR candidate. No hostile-audit, Stage32 MAIN, or full-target credit is granted here.

The EX1-05C residual gate was exact: the only h=2 component-stabilizer choice not already excluded by class-mass capacity forbids the w-sign inertia class, i.e. the 16 nodes on `b3=0`. For h=2 to survive, every V6 exceptional pairing on those 16 nodes would have to be even.

## Exact source-order replay

The source lock is `MichaelStollBayreuth/Verification/Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`. A scratch GitHub Actions replay used the same surface equations, `pts := Points(SingularSubscheme(S))`, and the source `C2s` definitions. It checked both the coordinate condition and the union of the four corresponding C2 incidence rows.

Scratch evidence:

- branch: `stage32ex1-scratch-05d-b3-index`;
- workflow commit: `fa194af320297796d93b56ce2208086d78efd74e`;
- run: `34124129143`;
- job: `101748682959`;
- conclusion: `success`;
- no artifact upload was used.

The exact source-side classes are

- `b1=0`: `[17..32]`;
- `b2=0`: `[9..16,33..40]`;
- `b3=0`: `[1..8,41..48]`.

The replay asserted that each class has 16 points, the three classes are pairwise disjoint, and they partition `1..48`. It also asserted that the `b3=0` coordinate test equals the union of the four source C2 `b3=0` rows.

## V6 parity on the forbidden h=2 class

Using the retained EX1-05B V6 exceptional-pairing vector, the `b3=0` values are

`[1,1,1,2,2,0,1,2,5,11,4,10,2,4,3,13]`.

Their sum is `62`, exactly reproducing the independent EX1-05C `b3=0` class mass. The other two source classes likewise reproduce `96` and `108`, so the source-order adapter also replays the complete `96+108+62=266` class partition.

The odd `b3=0` indices are

`[1,2,3,7,41,42,47,48]`,

with values `[1,1,1,1,5,11,3,13]`.

EX1-05B gives `q_i congruent m_i (mod 2)`. The sole surviving h=2 stabilizer from EX1-05C forbids w-sign ramification, hence requires `q_i=0` at every `b3=0` node. Any odd `m_i` contradicts that requirement. There are eight such witnesses.

Therefore **h=2 is excluded, and h=4 is forced at the component-stabilizer layer**.

This is still only a branch-exclusion refinement. It does not dispose all h=4 residual configurations, does not close the global delta/contact/intersection ledger, and does not exclude all V6 genus-1 carriers.

Next route: `EX1-05E_H4_ONLY_RESIDUAL_CONFIGURATION_DISPOSAL`.
