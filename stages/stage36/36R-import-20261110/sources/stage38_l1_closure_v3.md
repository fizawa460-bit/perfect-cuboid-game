# Stage38 · L1 — formal closure record (v3)

```text
STAGE=Stage38
LANE=L1   (CT pairing in arithmetic language; Reference Pack target A-G)
CLOSURE_DECISION=CLOSED
DECIDED=2026-10-13
MATHEMATICAL_BODY=Stage38_final_v2.md (Drive 1NJBAt6NrF6G56HApjAw0MXPFIjvn84ML), unchanged
THIS_FILE_SUPERSEDES=status/handoff flags of Stage38_final.md (v1) and Stage38_final_v2.md
SCOPE=Stage38 lane L1 only. NOT a judgement on Stage36, R29-CAMP2, Q11-CAMPEDELLI, lanes L2/L3, or the perfect cuboid.
```

## 1. Documents compared

1. **Stage38 Reference Pack** (`1CL6B_-gHy-eA93XRNbW1l8zgHRT4yk0F`): the focus statement and steps A–G.
2. **Stage38_final v2** (`1NJBAt6NrF6G56HApjAw0MXPFIjvn84ML`): S38-1 to S38-7 and §10.
3. **RESULTS (Claude Docs `dcb03d7b-1596-44fa-97f8-dae72a9d434b`)**: R-15 (corrected), R-18, R-20, R-23.
   - The Project copy `CAMPEDELLI_RESULTS.md` is a snapshot at R-10 (Stage36). The live RESULTS document is the Claude Docs one; the snapshot does not conflict with it.

The three documents were checked against each other:

- every theorem cited in RESULTS appears in v2 with a proof;
- every count in RESULTS equals §10 of v2;
- every A–G step of the pack has a theorem.

No inconsistency was found.

## 2. Audit round 1 findings — status

| finding | action | status |
|---|---|---|
| 1. overlap with registries in §10.6 | set difference computed; v2 §10.6, RESULTS R-23 | **resolved** |
| 2. S38-6 Galois/density proof | Kummer-degree proof added; density restricted to primes in general; no transfer to factors of `P(u)` | **resolved** |
| 3. evidence levels | v2 §10.7 table; no claim that the auditor re-certified the numerics | **resolved** |
| open item `ALL_LOCAL_FORMULAS_FULLY_INDEPENDENTLY_CERTIFIED = NO` | independent recomputation (§3 below) | **resolved by recomputation** |

## 3. Item ③ — independent re-verification of the local Cassels terms

This is not a text revision: the local terms were recomputed by a second, independent implementation (Drive `1p1W7JGwkWBm7RdhsyGQpI3TUzD5xImXm`).

**What is independent of the first implementation:**

- p-adic arithmetic: PARI `t_PADIC` instead of hand-written Hensel lifting;
- Hilbert symbols: PARI `hilbert()` instead of a hand-written formula;
- local points: exactly the points named in the proof (`S`, `R+`, `R-`, and the constructions at `v = 2, 7, e, f`) instead of random samples. At split places, `S` is cross-checked against a genuine affine point with `T = v^10`. This tests the "`T = 0` point" argument of v2 §3 directly.

**What is checked, for every curve and every bad place `{∞, 2, 3, 7, 41, d, e, f, p1, p2, q1, q2}`:**

1. the point lies on `D_{w1}` (both quadrics vanish to `v`-adic precision ≥ 72);
2. every valuation and squareness claim of S38-2;
3. the local contribution equals the value in S38-2.

**Results:**

| population | curves | curves with any discrepancy | formula vs PARI `ellrank` |
|---|---|---|---|
| `j ≤ 12M`, B=+1 | 367 | 0 | 0 mismatches |
| `12M < j < 112M`, B=+1 | 2040 | 0 | (sample of 50 earlier: 0 mismatches) |

**Sensitivity check (mutation tests).** Five deliberate errors were inserted and each was detected:

- wrong `c_41` flags 180 curves, exactly the number with `A = -1`;
- the `q`-term computed with `b1` instead of `b2` flags 143;
- wrong `c_e` flags 367;
- the near-`S` point perturbed flags 367;
- `β'3` altered flags 367.

The first run of the checker had one bug of its own: a 3-adic squareness test was done over `Q`. The contribution values already matched; the bug was fixed and the full run repeated.

**Remaining level.** This is an independent machine verification of every local claim on 2407 curves, together with the written proof. It is not a human proof check, and no further external AI audit has been run since v2.

## 4. Item ② — net increase (fixed-p exclusions, final)

| | curves | fixed p |
|---|---|---|
| scan set (bit-1, `j ≤ 1.12·10^8`, plus R-20 realizations) | 1168 | 4672 |
| already in registries (R-15 corrected: 57; R-20: 7, contained) | 57 | 228 |
| dim-2 registries (224 entries, R-16) | 0 overlap (different `dim Sel^2`) | 0 |
| **net increase** | **1111** | **4444** |

## 5. Item ④ — classification of results (as written into RESULTS)

| result | content | class |
|---|---|---|
| R-15 (corrected) | 103 B=+1 curves at `j ≤ 2.6M`, 57 rank 0, 228 fixed p | **proved** (PARI rank 0 with Cassels; torsion) |
| R-18 | Sel² basis; closed CT formula; bit 1 ⇒ `E(Q)=E[2]` | **proved** (external AI review; independent local recomputation, §3) |
| R-20 | unique `q*`; CRT class forcing bit 1; realizations | **proved** (forcing); realizations finite and APRCL-certified |
| R-23 prop. 1 | non-Legendre term = Frobenius in fixed degree-16 field | **proved** (degree, `Z/2` step); density for primes in general (Chebotarev); transfer to `P(u)`-factors **not claimed** |
| R-23 prop. 2 | forced class infinite ⇒ infinitely many fixed p | **conditional** (Schinzel H) |
| R-23 counts | 1168 / 4672; net 1111 / 4444 | **finite computation** (APRCL; formula; PARI samples) |
| bit-0 fibers: rank 2 or `Sha[4]`? | | **open** (needs 4-descent; blocked) |
| unconditional infinitude of the forced class | | **open** (contains the `n^2+1` problem) |

## 6. Item ⑤ — target A–G: achievement conditions and proofs (final)

| step | achievement condition (from the pack) | proof | met? |
|---|---|---|---|
| A | canonical Selmer basis fixed from the graph data | S38-1 (R-18) | yes |
| B | 2-cover data normalized globally | v2 §3 (rational conic points, primitive tangent forms) | yes |
| C | symbolic local Cassels term per support-prime type (P/Q/D) | S38-2 (a)–(d) (R-18); recomputed (§3) | yes |
| D | dyadic and real terms derived separately | S38-2 (a) `∞`, (e) `v=2`; recomputed | yes |
| E | point-choice independence proved symbolically, not statistically | v2 §3 (Cassels' theorem ⇒ per-place independence) + S38-2 (f) (Shukla–Stoll Cor 5.5) | yes |
| F | sum over all places, simplified by reciprocity | S38-3 with S38-L (R-18, R-20) | yes |
| G | after the exact formula exists, study whether nondegeneracy can be forced on an infinite/uniform subfamily | S38-5: forced on an explicit uniform congruence subfamily (proved). S38-7: its infinitude ⇐ Schinzel H (proved implication) | yes — the study is completed with a definite answer: unconditional forcing on the class; infinitude reduced to H |

**Reading of G.** The pack asks to *study whether* nondegeneracy can be forced. The answer is complete:

- it can be forced, uniformly, on an explicit class (theorem);
- whether that class is infinite is exactly a prime-tuple question (theorem: H ⇒ infinite), which current mathematics cannot settle.

That is the reached boundary. It is not an unfinished task inside Stage38.

## 7. Decision

```text
STAGE38_L1=CLOSED
```

**Reasons.**

1. Every step A–G of the Stage38 target has a written proof. The proofs are recorded in RESULTS (R-18, R-20, R-23).
2. All three findings of the external audit are resolved. The one remaining audit item (independent certification of the local terms) was resolved by an independent recomputation, not by rewording.
3. The only conditional statement, the infinitude of the forced subfamily, is an implication proved in full (H ⇒ infinitude). Its hypothesis is a famous open conjecture. Leaving L1 open would not change this.
4. The open questions do not belong to the Stage38 target, so they do not block closure. They are carried forward in §8.

**Why not CONDITIONAL_CLOSED.** No pending task is required to meet A–G, so there is no condition left to discharge. The conditionality of S38-7 is part of the mathematical statement, which is recorded as conditional in RESULTS; it is not a condition on the closure.

**Why not OPEN.** Nothing in A–G is unproved.

## 8. Carried forward (not Stage38-L1 blockers)

1. **Bit-0 fibers (CT pairing zero, 177 + 1068 curves).** Whether these have rank 2 or a large `Sha[4]`. This needs 4-descent (Magma `FourDescent` or equivalent), which is unavailable here (L1-17).
2. **Unconditional infinitude of a forced class.** This is beyond current methods: Schinzel H, `n^2+1`-type.
3. **Optional confirmation audit** of this closure record and of the independent local recomputation, by an external AI or a human.
4. **Receiver level (outside Stage38-L1):** `ALL_P_EXCLUSION=false`, `R29_CAMP2_CLOSED=false`.

## 9. State of the records after closure

| record | state |
|---|---|
| Stage38_final v2 (body) + this file (closure) | final; v1 superseded |
| RESULTS (Claude Docs) | R-15 corrected; R-18, R-20, R-23 promoted; "Stage38-L1 closure" status block added with the §5 classification |
| LOG L1 (Claude Docs) | L1-1D (independent recomputation) and L1-1E (closure) added |
| INDEX (Claude Docs) | L1 row added (CLOSED) |
| Handoff | Project document `claude/HANDOFF_STAGE38_L1.md` |

```text
STAGE38_L1=CLOSED
STAGE38_TARGET_A_TO_G=MET
CONDITIONAL_COMPONENT=S38-7 (Schinzel H), recorded as a conditional theorem, not a pending task
LOCAL_CT_TERMS_INDEPENDENTLY_RECOMPUTED=true (2407 curves, 0 discrepancies, mutation-tested)
FIXED_P_NET_NEW=4444 (1111 curves)
R29_CAMP2_CLOSED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
