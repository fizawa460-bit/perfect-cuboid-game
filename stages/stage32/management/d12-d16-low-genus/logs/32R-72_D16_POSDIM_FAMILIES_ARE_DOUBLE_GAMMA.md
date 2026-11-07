# 32R-72 — d=16 D-check: the positive-dimensional "bad" families are members containing 2Γ (2026-11-03)

Status: working log (mod 10009, same arithmetic as the D-check). No credit. §"Rigorous follow-up" supersedes the sampling.

## Context

- The D-point check (`stoll/n16/mkdchk.py`, 28 jobs over 10 classes, run b6jl0gfg4) finished.
- 11 jobs give finitely many bad members: 27740 ×3, 27771 ×3, 27940 ×3, 28445 ×2.
- 17 jobs report a POSITIVE-DIM-BAD-FAMILY on some D-curve Γ: 27882, 27988, 28246, 28255, 28261, 34761.

## Finding

- **Every** positive-dimensional family in the 28 jobs is a family of net members G_q that are **singular along the whole curve Γ**, i.e. G_q ≥ 2Γ.
  - Checked by `fam/mkfam.py`: 2 sample members per linear family, 3 per nonlinear family (27988_0 G34, degree 8, mult-2 curve).
- For such members the residual R_q = G_q − D still contains Γ. So the test "mult_p(G_q) ≥ m + 2 at p ∈ Γ" is satisfied automatically. These members belong to the decomposition with Γ counted once more. They are not D-point failures of the decomposition being checked.
- **Rechecking with Γ counted once more** (mult ≥ m + 3 at a smooth point of S on Γ and on no other D-curve):
  - no such point on any sampled member, in all 17 jobs;
  - six jobs (27882 ×3, 27988 ×3) first showed 1–3 points. These were intersections with other D-curves; they disappear once those curves are excluded, as in the D-check itself (`fam/g_*.out`).
- **Why the same linear forms recur:**
  - s0 + 1202u − 1124v (curves G31/G32, G36, G44, G5/G6) and s0 − 3678u + 3649v (G7/G8).
  - Several classes share the same base curves and hence the same net, so the same random basis gives the same line.
- **Exception, outside the 28 jobs:** the older run 27685s_0, curve G86, has a degree-2 family whose members are **not** singular along Γ. This is a different phenomenon and is not resolved here.

## What is not done

- The sampling shows the generic member of each family is clean. Finitely many special members of a family could still fail.
- A rigorous closure needs the D-check redone on each family (q restricted to Q = 0) with Γ at multiplicity m + 1. This is the same kind of job as `mkdchk.py`, with smaller parameter space.
- 27685s_0 G86 needs a separate look.

## Files

- `stoll/n16/fam/mkfam.py`: generator.
- `stoll/n16/fam/f_*.out`: first pass, without excluding other D-curves.
- `stoll/n16/fam/g_*.out`: rerun of the six jobs with that exclusion.

## Rigorous follow-up (`fam/mkfam2.py`, `fam/h_*.out`)

For each family (job, Γ, m, Q), with the two random field triples of the D-check:

- **A:** every word of length ≤ m of F_q reduces to 0 modulo std(Γ + S + (Q)). So **every** member with Q(q) = 0 contains (m+1)Γ. This is an identity, not a sample.
- **B:** the D-check for D' = D + Γ, restricted to Q = 0: points on Γ (smooth on S, on no other D-curve) with mult ≥ m + 3. Then eliminate the point.

**Results, all 17 jobs of the 28-job run:**

| Family | A: contains (m+1)Γ | B: bad members on the family |
|---|---|---|
| all m = 1 families (16 jobs, plus 27988_0 G40/G44) | yes, both triples | finite (projective dim 0, degree ≤ 4) or none |
| 27988_0 G34 (m = 2, degree-8 Q) | **no** (9 of 13 words nonvanishing, both triples) | B not applicable |

- No family stays positive-dimensional (`STILL-POSITIVE-DIM`: 0).
- So, apart from 27988_0 G34, the positive-dimensional bad sets reduce to finitely many special members. These are of the same kind as the finite bad members of the 11 clean jobs and go to the same downstream treatment.
- **27685s_0 (outside the 28; μ = 16 class):**
  - G14/G16 (m = 1) satisfy A.
  - G1 (m = 2, degree-5 Q) and G86 (m = 1, degree-2 Q) **fail A**: their members do not contain one more copy of Γ, so the mechanism is different.
  - B is finite where it was computed.
  - Whether μ = 16 classes need the D-check at all is to be confirmed from the pipeline records (`dlist2.txt` took only μ ≥ 18).
- **Caution for 27988_0 G34 (m = 2):** the sampling pass ("singular along Γ") is automatic when m = 2, so it says nothing there. The 27685s_0 G1 case shows that an m = 2 family can fail A. So 27988_0 G34 is genuinely open until its run finishes.

## 27988_0 G34: a genuine positive-dimensional D-point family

- A fails: the members of the degree-8 family Q = 0 contain 2Γ (from D) but not 3Γ.
- So the family consists of members whose residual R_q = G_q − 2Γ is singular at a point of Γ. For a net, this is expected to happen only finitely often; here it happens along a whole curve of the net.
- This is the only one of the 28 jobs left with a positive-dimensional bad set.
- **Genus of general members** (`n16/g34/mkg34.py`, run with OK; three random F_p-points of Q = 0, same basis and seed as e_27988_0):
  - the residual after removing G34, G40 and G44 is irreducible of degree 16 with p_a = 13;
  - the singular superset is 3 points, with δ = 1 each;
  - **geometric genus ≥ 10** for all three members.
- Genus ≤ 1 is a closed condition in the family, so it holds only at finitely many special members of G34's family. G34 is thereby reduced to finitely many members, like every other job.

## Overall status of the 28-job D-check

- No positive-dimensional bad family remains.
- Each job's bad set is now finite: the original finite sets, the finitely many members per 2Γ-family (B above), and the finitely many special members of the G34 family (not yet listed explicitly).
- **Still to do:** feed these finite members into the existing per-member genus pipeline (`mkcand.py` style). For G34 they must first be located: members of the degree-8 family whose residual has δ ≥ 12.

## Closing the finite parts (2026-11-03, later)

- **2Γ-families need no member work at all.** A member G ≥ D + Γ has residual R = G − D ⊇ Γ, so R is reducible. The finite B-sets above are therefore irrelevant.
- **Candidate members (m_ jobs) of the 28 jobs:** 8 were still open:
  - 28445_0_2 and 28445_1_2;
  - 34761_0 #1, #6, #11, #18, #19, #20.
  They were genus bound ≤ 1 with no reducibility job yet. New r_ jobs (`n16/r_*.sing`): **all RESIDUAL-REDUCIBLE**. The candidate stage of all 28 jobs is now closed.
- **D-check finite bad members** (`n16/mkdmem.py` → `n16/dm/`):
  - 154 member jobs (degree 1: 140, degree 2: 11, degree 4: 3), deduplicated by ideal per job. This includes the shape s0·v² = cubic.
  - Results: genus ≥ 2 ×109, member reducible ×25; 20 undecided (bound ≤ 1 ×14, "singular superset not finite" ×6).
  - The 20 rd_ jobs: **all RESIDUAL-REDUCIBLE**.
- **Remaining for d=16 (μ ≥ 18 nets): only the special members of the 27988_0 G34 family.**
  - The general member has genus ≥ 10 (δ = 3), and genus ≤ 1 needs δ ≥ 12.
  - In progress: the off-D singular incidence over the family (`n16/g34/sl.sing`), to list the finitely many members where δ can jump.

## The G34 family closed by the cross-decomposition argument (no family-wide computation needed)

**Design of the nets (net_plan.py, net_tail_c.sing):**
- A singular point of a curve C in class x can lie on a D-curve Γ only if x·Γ ≥ 2 ("danger" curves).
- Each decomposition t sees μ_p(C) only at points off its base locus.
- The decompositions are chosen so that the hidden set H = ∩_t (∪ danger curves of D_t), minus the nodes, is as small as possible.
- If every singular point of a genus ≤ 1 member C is visible in some decomposition, then Σ_t visible ≥ δ ≥ p_a − 1. So some t sees ≥ THR, and C is a candidate there.

**27988 specifics:**
- p_a = 11, three decompositions, thr3 = 4.
- Decomposition 0 = 2·G34 + G40 + G44 (danger: G34). Decomposition 1 has danger curves G90 and G92; decomposition 2 has G38, G77 and G79.
- H (decompositions 0 and 1) is a single point P0 = (1, 1, 3303, 0, 0, 4419, 1), non-reduced of degree 2. P0 also lies on supp(D_2) (hc_27988_2), so P0 is the only point hidden in all three decompositions.
- `g34/p0.sing`: P0 lies on G34 and on G40, and is not a node.

**Argument for a G34-family member C of genus ≤ 1:**
- **C not singular at P0:** every singular point is visible in some decomposition, so C is a candidate in some decomposition. All candidates of 27988_0/1/2 are closed (genus ≥ 2 or reducible).
- **C singular at P0:** P0 = G34 ∩ G40, where D has multiplicity 3, so mult_P0(G_q) ≥ 5.
  - These are linear conditions on q: words of length ≤ 4 at P0, with the fields spanning there. They have rank 2 for both field triples.
  - So there is exactly **one member, q = (−3811 : −3427 : 1)**. That member contains a further D-curve (residual degree 12 < 16), so it is reducible.
- Independent observation: for three random family members, the forced singular point on G34 is a single point different from P0 (`g34/where.sing`). So the family's singular point moves.

**Conclusion (research level, char p = 10009, same caveats as the rest of the pipeline):**
- The G34 family contains no genus ≤ 1 curve. All 28 jobs of the μ ≥ 18 nets are closed, and **d = 16 nets are done**.
- Remark: the same cross-decomposition argument also covers most D-check members. The D-check remains as an independent safety net.
- The family-wide incidence computation `g34/sl.sing` was stopped as unnecessary.
