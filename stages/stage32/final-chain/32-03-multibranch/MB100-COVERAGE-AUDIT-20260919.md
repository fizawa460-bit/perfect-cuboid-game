# Stage32 32-03 — MB entry coverage audit — 2026-09-19

Status: **COVERAGE AUDIT / PASS AFTER SEMANTIC REPAIR REQUIRED / NO CREDIT PROMOTION**

## Question

Does the current Stage32 split

- finite/unibranch side, and
- 32-03 MB101 node-multibranch side

cover every integral nonexceptional low-genus carrier, or can a carrier escape both sides because its normalization is nonbijective only over the smooth locus of the box surface?

## Source locks

Current / retained repository sources:

- Stage29 finite receiver split:
  `stages/stage29/29-02c-LG2/result.md`
  blob `820ed4e1b1a53db14085678de6f186b59ae0ea48`.
- Stage32 source note for Freitag--Salvati Manni Theorem 3.1:
  `stages/stage32/residual-32-01-production/post1648ah-fsm-unibranch-source-note.md`
  blob `a4b2e09f5eb7bf5c287554985141548ca3359de7`.
- MB101 exact node-profile definition:
  `stages/stage32/final-chain/32-03-multibranch/nodes/MB101/RESULT.md`
  blob `890f80ce208e402b14275d3e3279f9c02d5dc2fa`.
- MB101 certificate:
  blob `282fc94d8d5feb0221cf6bf096ed4b0030883563`.
- Stage32-00 audit:
  blob `a96a2d4e5cfb46290cebe4db0c7a6645593f938e`.

Historical MB104 exact source:

- archive branch `stage32mb-mainbatch-20260912`
- archive exact head `ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11`
- `FSM-MULTIBRANCH-POLE-LEMMA.md`
  blob `efe86334dfe7bf397ef6c370356b136e8280d1d1`
- `FSM-MULTIBRANCH-POLE-CERTIFICATE.json`
  blob `33ac3879f9dae466f90a1e67557eb928cdfc557b`
- verifier `verify_mb104_fsm_multibranch_pole.py`
  blob `de52df4b516782ea8e29321b9936bb83b61468f4`.

Primary external source:

E. Freitag and R. Salvati Manni,
*Parametrization of the box variety by theta functions*,
Section 3, proof of Theorem 3.1.
The paper states that the box variety has exactly 48 singularities, all nodes.
The published theorem assumes the normalization map is globally bijective.

## 1. The 48-node ambient picture is correct

The singular locus of the complex box surface consists of exactly 48 nodes.

Therefore, for an integral curve `C` with normalization `nu:Cbar->C`, define for the 48 box nodes

```
r_i = # nu^{-1}(node_i),
R = sum_i r_i.
```

There is no 49th ambient surface singularity missing from MB101.

This does **not** mean the curve itself has only 48 possible singular points; it may have singularities over the smooth locus of the surface.

## 2. The textual Stage32 split is not literally exhaustive as currently worded

The published Freitag--Salvati Manni theorem assumes

```
nu:Cbar->C globally bijective.
```

MB101, on the other hand, defines the 32-03 receiver by

```
N_MB >= 1,
```

equivalently `r_i>=2` for at least one of the 48 box nodes.

Thus the wording alone leaves an apparent middle case:

```
nu not globally bijective,
but r_i<=1 for every box node.
```

Such nonbijectivity can occur only over the smooth ambient locus, for example at a self-node of the curve.

MB102's `Delta_off` does not by itself repair entry coverage: MB102 is downstream of MB101 and therefore only records off-exceptional singularities for curves already admitted to the node-multibranch receiver.

Hence the statement

```
published globally-bijective population
UNION
MB101 node-multibranch population
= all low-genus carriers
```

is **not justified merely from the two current entry definitions**.

## 3. However, the historical branchwise FSM lemma repairs the gap

The historical MB104 branchwise pole extraction proves the stronger necessary inequality

```
d <= 16g - 16 + 4 R8,
```

where `R8` is the number of normalization branches over the 48 box nodes having the FSM-minimal cusp type

```
(A,B)=(1,1).
```

This extraction explicitly removes the final use of global bijectivity in the published proof.

The source proof works as follows:

```
16(2g-2)k = #zeros - #poles,
#zeros >= 2kd,
#poles <= 8k R8.
```

Hence

```
d <= 16g - 16 + 4R8.
```

Crucially, self-identifications or multibranch singularities over the **smooth locus** create no additional poles in this tensor argument. The poles occur only over the exceptional divisors above the 48 box nodes.

Therefore, if

```
r_i <= 1 for every box node,
```

then automatically

```
R8 <= R <= 48,
```

and the same finite bound follows:

```
d <= 16g -16 +4*48 = 176+16g.
```

Thus:

```
g=0 -> d<=176,
g=1 -> d<=192.
```

The published theorem is recovered as a special case, but global bijectivity is stronger than necessary for the finite-degree conclusion.

## 4. Exhaustive repaired population split

A complete split can therefore be made solely from node-preimage multiplicity:

### FINITE SIDE

```
P_FIN = { C : r_i<=1 for all 48 box nodes }.
```

This population includes:

- globally bijective normalization;
- smooth-locus cusps or other bijective singularities;
- smooth-locus self-nodes / other nonbijective singularities,
  provided no box node has multiple normalization preimages.

For all of `P_FIN`:

```
R8<=48
=> d<=176+16g.
```

### CLASS-3 / MB SIDE

```
P_MB = { C : r_i>=2 for at least one box node }.
```

This is exactly MB101's `N_MB>=1` population.

It may also have arbitrary smooth-locus singularities; those are retained by MB102 through `Delta_off`.

The two sets are tautologically disjoint and exhaustive:

```
P_FIN disjoint_union P_MB
= all integral nonexceptional carriers.
```

No third smooth-locus-only Class-3 receiver is required.

## 5. Required semantic repair before final receiver discharge

The mathematics needed for coverage is already present in the historical MB104 branchwise FSM lemma, but the Stage32 entry wording has not been synchronized to this stronger split.

Before 32-01/02/03 are used as an exhaustive low-genus decomposition for 32-04, an explicit adapter should state:

```
OLD FINITE-SIDE LABEL:
globally bijective normalization

REPAIRED FINITE-SIDE SEMANTICS:
at most one normalization preimage over each of the 48 box nodes
(equivalently max_i r_i<=1),
with smooth-locus nonbijectivity allowed.
```

This does not import the 176/192 bound into MB101. It moves only the nodewise-unibranch complement of MB101 to the finite side, justified by the branchwise FSM pole inequality.

The finite Picard reduction in Stage29 uses only the degree bound, `H.C=d`, and the genus/adjunction lower bound after the degree window is supplied. Its lattice finiteness argument does not intrinsically require global bijectivity. Effectivity/member certification remains a separate downstream obligation.

## 6. Other useful viewpoint: N is not the fundamental pole variable

MB101 correctly records

```
N = number of met box nodes,
R = number of normalization branches over box nodes,
M = exceptional contact mass.
```

The branchwise FSM argument shows that the direct pole-complexity variable is actually

```
R8 = number of minimal (1,1) branches.
```

Thus:

- `48` is the ceiling for the **support axis** `N`;
- `R`, `R8`, and `M` may still grow with fixed `N`;
- the current N-based Z21/Miyaoka work is a valid partial route, not the only natural coordinate system.

This is why `N=10,...,48` should not be interpreted as 39 independent cases that must be killed one by one.

## Audit verdict

```
BOX_SURFACE_SINGULAR_LOCUS_48_NODES = PASS
MB101_INTERNAL_NODE_PROFILE_SEMANTICS = PASS
MB101_STARTS_32_03 = PASS
CURRENT_TEXTUAL_GLOBAL_BIJECTIVE_VS_NODE_MB_SPLIT = INCOMPLETE_AS_WRITTEN
SMOOTH_LOCUS_ONLY_NONBIJECTIVE_NEW_CLASS3_REQUIRED = NO
HISTORICAL_BRANCHWISE_FSM_REPAIRS_COVERAGE = PASS_AS_RETAINED_NECESSARY_INEQUALITY
REPAIRED_EXHAUSTIVE_SPLIT = NODEWISE_UNIBRANCH_FINITE_SIDE vs MB101_NODE_MULTIBRANCH
STAGE32_ENTRY_SEMANTIC_SYNC_REQUIRED_BEFORE_32_04 = YES
MB104_CLASS3_RESEARCH_INVALIDATED = NO
N10_PLUS_RESEARCH_INVALIDATED = NO
NEW_RECEIVER_CREDIT = NO
THEOREM_CREDIT = NO
ENDPOINT_CREDIT = NO
MERGE_AUTHORIZED = NO
```

The audit therefore finds a **documentation/receiver-scope gap, not a new mathematical population gap**.
