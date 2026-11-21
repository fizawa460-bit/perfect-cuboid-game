# EXP03 (E3) — ZF2 reality check: explicit zero-free regions vs the −30 bands

Date: 2026-11-21. Question: can any published *explicit, unconditional*
zero-free region prove ZF2 — i.e., that the relevant quadratic Hecke
characters χ of K have no L(s, χ) zeros in the row383/row384 bands
(Re s > 0.562–0.63, |Im s| ≤ 2.12)? Expected answer was no; this file
records exactly how far off the literature is, so the check is never
retried as new. No endpoint credit is claimed.

## 1. Reduction to a Dedekind zeta function

The characters χ are the nontrivial quadratic Hecke characters of K
attached to unramified quadratic extensions E/K (they are the class-group
characters; c_Cl ≥ 1 is what produces one). For such an E,

  ζ_E(s) = ζ_K(s) · L(s, χ),

so every zero of L(s, χ) is a zero of ζ_E. Since E/K is unramified, the
relative discriminant is trivial and

  n_E = 210,   |d_E| = |d_K|²,   rd_E = rd_K ≈ 44.5,
  log d_K = 105 · log 44.5 = 398.53,   log d_E = 797.05.

(The analytic conductor of L(s, χ) itself has log ≈ 399, matching the
"400+" in the lab notes; using ζ_E with log d_E = 797.05 is the rigorous
vehicle and is also the less generous choice.) Explicit zero-free
regions for ζ_E therefore apply verbatim to L(s, χ).

## 2. Best published explicit regions used

1. **Das–Gaba–Lee–Savalia–Wong (2025)**, "New zero-free regions for
   Dedekind zeta-functions at small and large ordinates",
   arXiv:2506.19319 — the current best, refining Kadiri and Lee.
   - Thm 1.1 (|t| ≥ 1, n_L ≥ 3): ζ_L(σ+it) ≠ 0 for
     σ ≥ 1 − 1/(C1 log d_L + C2 n_L log|t| + C3 n_L + C4) with
     (C1, C2, C3, C4) = (12.21124, 9.54177, −11.59548, 4.57803).
   - Thm 1.2 (|t| ≤ 1, n_L ≥ 2): at most one zero in
     σ ≥ 1 − 1/(A log d_L), A′ = 0, with A = 11.51910 for n_L ≥ 7;
     that zero, if it exists, is the exceptional (real) zero.
   - Thm 1.3 (Deuring–Heilbronn, conditional on an exceptional zero with
     ν = 0.05, n_L ≥ 9): A improves to 1.806471.
   - Thm 1.4 (real zeros, n_L ≥ 7): at most one real zero in
     σ ≥ 1 − 1/(A′′ log d_L), A′′ = 1.61094.
2. **Kadiri (2012)**, "Explicit zero-free regions for Dedekind zeta
   functions", Int. J. Number Theory 8, 1–23 (arXiv:1106.1868):
   |t| ≥ 1 region with log M = 12.55 log d_K + 9.69 n_K log|t|
   + 3.03 n_K + 58.63; |t| ≤ 1 region 1/(12.74 log d_K), at most one
   (real, simple) zero. (Needs d_K "sufficiently large" — satisfied here;
   Das et al. remove the condition anyway.)
3. **Lee (2020)**, "On an explicit zero-free region for the Dedekind
   zeta-function", arXiv:2002.05456: constants
   (12.2411, 9.5347, 0.05017, 2.2692) for |t| ≥ 1; small-ordinate
   constant 12.43436.
4. Dirichlet comparison: **Kadiri (2005/2018)**, "Explicit zero-free
   regions for Dirichlet L-functions", Mathematika 64, 445–474:
   R = 5.60 in σ ≥ 1 − 1/(R log(q max(1,|t|))). (Kadiri–Lumley–Ng's
   explicit work, arXiv:2101.12263, is a zero-*density* estimate, not a
   zero-free region; it does not exclude individual zeros and cannot
   serve ZF2.) Lagarias–Odlyzko (1977) is the historical origin of the
   number-field region and is superseded by the constants above.
   Vinogradov–Korobov-type regions are a large-|t| shape and are not
   competitive at |t| ≤ 2.12 (log|t| ≤ 0.76); the classical region is
   the governing one at band heights.

## 3. What the best region gives at band heights (L = E, log d_E = 797.05, n_E = 210)

Das et al. 2025, Thm 1.2 (small ordinate, covers Ω2 band |t| ∈ (0.26, 0.77)):
  deficit = 1/(11.51910 × 797.05) = 1/9181.9 = 1.089×10⁻⁴
  ⇒ no (non-exceptional) zeros for Re s ≥ 0.99989.

Das et al. 2025, Thm 1.1 (large ordinate, covers |t| ∈ (1.03, 1.46) and
the row383 band up to |t| = 2.12), D(t) = 12.21124·797.05
+ 9.54177·210·log t − 11.59548·210 + 4.57803 = 7302.9 + 2003.8·log t:
  t = 1.03: D = 7361.8, deficit 1.358×10⁻⁴ ⇒ Re s ≥ 0.99986
  t = 1.46: D = 8060.8, deficit 1.241×10⁻⁴ ⇒ Re s ≥ 0.99988
  t = 2.12: D = 8808.2, deficit 1.135×10⁻⁴ ⇒ Re s ≥ 0.99989

Older results are slightly weaker at these parameters (Kadiri 2012:
boundary 0.99990–0.99992; Lee 2020: 0.99990–0.99991), same order.
Even the Deuring–Heilbronn region of Thm 1.3 — which is *conditional on
an exceptional zero existing*, the favourable case for repulsion —
only reaches Re s ≥ 0.99931. Even Kadiri's Dirichlet constant R = 5.60,
illegally but generously applied with log-conductor = log d_E, reaches
only Re s ≥ 0.99978 (with log-conductor = log d_K: 0.99955).

**Headline: the best unconditional literature boundary at every band
height is Re s ≈ 0.99986–0.99989.**

## 4. The gap to ZF2

ZF2 needs zero-freeness throughout Re s > 0.63 (Ω2; row383's weakest
band needs Re s > 0.562).

- Gap in Re: 0.99986 − 0.63 ≈ **0.370**.
- Gap in deficit (1 − Re): needed 0.37; literature supplies
  ≈ 1.1–1.4×10⁻⁴. Shortfall factor ≈ **2.7×10³** (at t = 1.03) to
  **3.4×10³** (small ordinate). Against row383's weakest threshold
  0.562 (needed deficit 0.438): factor ≈ **4.0×10³**.
- Equivalently: in Das Thm 1.2 the constant A·log d_E ≈ 9182 would have
  to shrink to ≈ 2.7 (A ≈ 0.0034 instead of 11.51910). No incremental
  refinement of the Stechkin/Kadiri trigonometric-polynomial method
  moves constants by three orders of magnitude; the whole 1977→2025
  literature improved the deficit at fixed conductor by tens of percent.

## 5. Exceptional (Landau–Siegel) zero caveat — checked, does not matter

The small-ordinate theorems allow at most one zero in the region, and
that zero must be **real** (Im s = 0 exactly), simple. Every band point
in rows 383/384 has |Im s| ≥ 0.26 > 0 (Ω2: (0.26, 0.77) ∪ (1.03, 1.46);
row383: (0.26, 0.77), (1.03, 1.46), (1.70, 2.12)). Hence:
- a Landau–Siegel zero cannot itself be the zero whose existence the
  bands assert — the necessary condition is about non-real zeros;
- in the small-ordinate regime the theorems exclude all *non-real*
  zeros outright down to the boundary computed above; the exceptional
  zero allowance does not weaken the band conclusion in any way.
The reasoning "a real zero alone does not satisfy the necessary
condition" is therefore consistent with the band shapes. (For the
record, even on the real line itself the literature only excludes a
second real zero above Re s = 0.99922, Das Thm 1.4 — the real line is
simply not where the bands live.)

## 6. Verdict

ZF2 cannot be discharged, or even approached, from published explicit
zero-free regions: the best boundary is Re s ≈ 0.99986 against the
required 0.63, a deficit shortfall of ~3×10³. This route is CLOSED.
Any future ZF2 progress must come from the problem's own explicit
formula (rows 383/384 machinery, cf. E2/E5/E6), from a verified
computation for these specific characters (none exists — the characters
are not even enumerated, cf. T1), or from new theory. Do not re-run
this literature check unless a zero-free region with constant improved
by orders of magnitude (not percent) appears.
