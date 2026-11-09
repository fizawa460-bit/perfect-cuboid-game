# Reading audit request — Stage32 D16-ALL-CLASSES (degree 16, all classes, genus ≤ 1)

Paste everything below the line into a fresh chat. Repository: `fizawa460-bit/perfect-cuboid-game` (public), branch
`stage32-d16-all-classes`, folder `stages/stage32/management/d16-all-classes/`. The audited companion leaf is
`stages/stage32/management/d12-d16-low-genus/` (main), whose `PAPER-R2.md` defines the tools used here.

---

You are an independent hostile auditor doing a **reading (paper) audit**. The goal is to check that **nothing is
wrong**: every argument is valid, and each computation decides what it is claimed to decide. Re-running code is welcome
but optional.

**Background.** S is the cuboid surface (complete intersection of four quadrics in P⁶ with 48 nodes), S̃ its minimal
resolution with exceptional curves E_p, K = K_S̃, d = K·C. Known: 92 curves (32 conics, 60 quartics) and the 48 E_p.
The audited package R2 (`d12-d16-low-genus/PAPER-R2.md`) proved: no integral curve of geometric genus ≤ 1 with
d = 12, 14 (all classes), and with d = 16 in the classes of the 71,697 unibranch-compatible representatives. This leaf
claims the remaining d = 16 classes (1,665,666 representatives), so that **d = 16 is closed for all classes**.
Computations are mod p = 10009; R2 §2 fixes which char-p → char-0 directions are allowed (h⁰_p ≥ h⁰_0, g_p ≤ g_0 via
Lemma G, statements about all char-p members). R2's round-1 error M1 ("reducible mod p ⇒ reducible in char 0") must not
reappear.

Please read `PAPER.md` (main text), `RESULT.json`, `logs/32R-97_D16_ALL_CLASSES_CLOSED.md`, and as needed `code/` and
`results/`, and check:

1. **Lemma K (PAPER §2).** If the unique member of |x|_p is supported on known curves and the E_p, then |x|_0 has no
   integral member. Is the injectivity of specialization Pic(S̃_0) → Pic(S̃_p) correctly invoked (smooth proper model,
   known curves defined over Q(ζ₈))? Is h⁰_0 ≤ h⁰_p the only semicontinuity used? Does "LG-ONLY-KNOWN" in
   `code/d16all/mklg.py` (saturation by every contained known curve until dimension < 2) really mean that the member is
   supported on known curves, the E_p and the D-part? Could the D-part matter?
2. **Lemma P (PAPER §2).** Genus of the plane model = (e − 1)(e − 2)/2 − Σ δ over **all** singular points
   (`code/d16all/mkgx.py`): is the chart choice (line at infinity avoiding the singular locus) enough; is the
   birationality check sufficient; is the conjugate-split case handled correctly as a Lemma G lower bound?
3. **h⁰ = 1 table (PAPER §3).** Do the categories cover all 4,094 classes exactly once (3,112 + 4 + 978, with the 14
   non-reduced classes counted inside the 978)? Is each verdict a valid closure (T3 + Lemma G; Lemma P; Lemma G by
   components; Lemma K)?
4. **h⁰ = 2 (PAPER §4).**
   - the 21 pencils with a fixed component, checked in char 0 by exact h⁰ over Q(ζ₈) (R2's T2′, `code/p16all/mkfix0.py`,
     `results/fix0_char0.txt`);
   - reuse of the R2 pencil pipeline (v6 critical tail, fibre matching, stage 2, `always_hidden` empty) and of R2
     §2.5(i) for unlisted reduced members;
   - the 65 members of Σg ≤ 1: the normal-crossings check (36 OK) and the analyzer `m16/an2.py` (29), with data
     produced by `m16/tail.sing` where the member NN is **given** (`code/p16all/mkt7.py`) instead of searched — is that
     substitution sound?
   - the non-reduced scan (R2 §4.5): h⁰_p(D + 2Γ_k) for all 140 Γ_k, and the 'cap' entries run directly as member
     jobs (`code/p16all/scan.py`, `gennr.py`): is this complete (members with a multiple component that is a known
     curve or an E_p)?
5. **Scope.** Confirm that no step uses the odd-contact filter 32R-83 (valid only for unibranch curves), and that the
   split into old (R2) and new classes (`code/d16all/split_new.py`) loses nothing.

## Answer format
For each item: **PASS / HOLD / FAIL**, then a list marked **MUST FIX** (a wrong step), **MUST CHECK** (could not
verify) or **SHOULD FIX** (wording). Quote the exact sentence for each item.
