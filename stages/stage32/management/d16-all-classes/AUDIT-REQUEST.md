# Reading audit request, round 2 — Stage32 D16-ALL-CLASSES (degree 16, all classes, genus ≤ 1)

Paste everything below the line into a fresh chat. Repository: `fizawa460-bit/perfect-cuboid-game` (public), branch
`stage32-d16-all-classes`, folder `stages/stage32/management/d16-all-classes/`. The audited companion leaf is
`stages/stage32/management/d12-d16-low-genus/` (main), whose `PAPER-R2.md` defines the tools used here.

---

You are an independent hostile auditor doing a **reading (paper) audit, round 2**. Round 1 (head a821e14f) gave HOLD:
Lemma K, Lemma P, the h⁰ = 1 table and the 21 fixed-component pencils passed; the other 97 pencils were held for one
MUST FIX and four MUST CHECK items. The answers are in `PAPER.md` §4.2–4.7 and §7 (audit history), with evidence in
`results/` and generators in `code/` (`code/p16all/audit_r1_steps.py` collects the steps first run inline).

**Background.** S is the cuboid surface (complete intersection of four quadrics in P⁶ with 48 nodes), S̃ its minimal
resolution, K = K_S̃, d = K·C. R2 proved: no integral curve of geometric genus ≤ 1 with d = 12, 14 (all classes) and
d = 16 in the 71,697 unibranch-compatible representatives. This leaf claims the remaining d = 16 classes. Computations
are mod p = 10009; R2 §2 fixes the allowed char-p → char-0 directions; R2's round-1 error M1 ("reducible mod p ⇒
reducible in char 0") must not reappear.

Please check, against the round-1 findings:

1. **MUST FIX (b), PAPER §4.2.** The v6 critical tail removed whole fibres in 61 jobs (81 members). Are all 81 now
   treated as members (`results/b_removed_fibres.txt`: Lemma G 23; NC-OK 38; analyzer OK 20), and is no closure left
   that relies on "non-reduced mod p"?
2. **MUST CHECK (c), PAPER §4.4.** R2's hidden-set, base-point and node checks, run with R2's scripts on the 97 pencils
   (`results/c_hidden_base_node.txt`), the direct node version for 4 jobs (`code/p16all/mknt.py`), and stage 2b on all
   special members (606 jobs, `results/c_stage2b_accounting.txt`, open 0; quadratic factors as one member over F_p(w)).
   Is this the complete R2 procedure behind R2 §2.5(i)? Is anything still missing (e.g. members at u = ∞, tangent cases)?
3. **MUST CHECK (d), PAPER §4.5.** Identification of every component with a known curve before the NC check / analyzer
   (`results/d_identification.txt`: 299 all known; the 33 with an unknown component are closed by Lemma G alone). Is
   "containment of the known-curve ideal + equal degree" an adequate identification?
4. **MUST CHECK (e), PAPER §4.6.** c0 = D_k in all 441 non-reduced scan entries (`results/e_c0_vs_Dk.txt`); MEMBERDIM
   0: 232, 1: 209, ≥ 2: none. Does this settle the cap entries and the possibility of non-reduced families?
5. **MUST CHECK (f), PAPER §4.7.** The check inserted in every T7 job (block `// audit (f)` in
   `code/p16all/t7/example_t7_job_with_audit_f_check.sing`): 84 × EXG-CHECK OK.
6. **The t_21 item and the SHOULD FIX items** (PAPER §2, §3, §7; `code/d16all/mkg3.py`, `results/gx_results.txt`,
   `results/split_new.txt`).

## Answer format
For each item: **PASS / HOLD / FAIL**, then items marked **MUST FIX**, **MUST CHECK** or **SHOULD FIX**, quoting the
exact sentence. Finally an overall verdict on Claim D16.
