# Stage32 MB103 — exact Aut(S) node-profile quotient

Status: **RETAINED / NO RECEIVER CREDIT**.

This node constructs the exact symmetry quotient required before any multibranch finite enumeration. It uses the published verification source at `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Exact reconstructed node action

The upstream source gives the box surface equations, asserts exactly 48 singular points, and gives nine explicit substitutions used to permute the known curves and singular points before descending to `Pic(S)`. It also constructs `AutS` from those generators and verifies `#Aut(S)=1536`.

The retained verifier reconstructs the node action independently from the source formulas. Starting from the singular point

`R1=[1:0:0:0:1:1:1]`,

the nine substitutions generate exactly **48** projective points. The induced permutation group on those 48 points has exact order **1536**, is transitive, and the stabilizer of one node has order **32**. The action on unordered pairs has exactly seven orbits, of sizes

`[24,48,48,48,192,384,384]`.

The local verifier chooses its own deterministic node ordering. It does **not** claim that this ordering equals Magma's internal `pts` order.

## Exact quotient contract

For any 48-entry node-indexed profile whose local entry is already an **intrinsic Aut-equivariant discrete signature**, define its orbit key to be the lexicographically minimum transformed profile over all 1536 node permutations.

This is an exact `Aut(S)` quotient on the node-indexed discrete data. For the current MB101/MB102 ledger, the intrinsic scalar payload includes

- `r_i`: number of normalization branches over node `i`;
- `M_i`: exceptional intersection mass `D.E_i`;
- `Delta_exc_i`: local delta supported on the exceptional fibre, when supplied;
- the derived multibranch bit `r_i>=2`.

The quotient also preserves `R=sum r_i`, `M=sum M_i`, the number of met nodes, the number of multibranch nodes, total exceptional-locus delta when supplied, and the histogram of intrinsic node signatures.

A histogram is **not** a complete orbit invariant. The seven distinct orbits on unordered node pairs give an exact counterexample: two binary profiles with two marked nodes can have the same histogram but lie in different `Aut(S)` orbits. Therefore later enumeration must use the full canonical orbit key, not only sorted node counts.

## Local-coordinate firewall

MB103 does not quotient raw chart data such as the labels `A<B` versus `A>B`, a raw exceptional landing coordinate `lambda`, or continuous tangent/jet moduli. `Aut(S)` acts inside the exceptional `P1` as well as permuting nodes. Such raw coordinates require a separate local-action adapter before they can be used as orbit tokens.

Canonically encoded intrinsic discrete data — for example an unlabeled resolved-landing partition or a multiset of branch multiplicities — may be carried as a node signature once its intrinsic encoding is separately established. MB103 does not manufacture such an encoding from raw `lambda` values.

## Consequence for the final chain

MB103 removes the node-label redundancy exactly, but symmetry alone gives no degree bound, no delta bound, and no effectivity statement. In particular:

- the Freitag–Salvati Manni unibranch `176/192` caps are still not imported;
- no multibranch finite degree/intersection window is proved;
- finite Picard enumeration remains blocked;
- no receiver, effectivity, theorem, endpoint, or Perfect Cuboid credit is granted.

The next load-bearing node is **MB104: population-wide finite degree/intersection restriction**. MB104 may consume the exact orbit canonicalizer, but it must derive an independent multibranch finite window rather than obtaining finiteness from symmetry alone.
