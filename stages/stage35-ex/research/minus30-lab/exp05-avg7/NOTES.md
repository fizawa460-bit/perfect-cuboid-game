# EXP05 — row384 averaging generalized from 3 characters to 7 (c_Cl ≥ 3 case)

Date: 2026-11-21. Lab copy of repo row384; the repo clone was not modified.
Verifier: python-flint 0.9.0 (`/tmp/flintenv/bin/python`).

## What row384 did (baseline, replayed byte-identical)

row384 averages the Poitou explicit formula over the 3 nontrivial characters
χ1, χ2, χ1χ2 of a (Z/2)^2 subgroup of the quadratic class characters of K
(needs c_Cl ≥ 2). At a prime ideal 𝔭 whose character values are not forced
("undetermined"), the odd-power average is bounded below by −1/3: writing the
pattern as (χ1(𝔭), χ2(𝔭)) ∈ {±1}², either it is (+,+) and all three values
are +1 (average +1), or exactly one of χ1, χ2, χ1χ2 equals +1 and two equal
−1 (average −1/3). Even powers always contribute +1, forced splits +1.
Certified baseline (average384.json, replayed identically here in 45 s with
`--recount-tail 4`):

- prime term ≥ 0.3691698403775159885…
- average score ≥ 0.0523946411808995256… (threshold 1/25 = 0.04)
- moment ≤ 99.186384435239… < 100, ε = 7/200, contradiction gap 7/10
- necessary zero region Ω2 (at least one of the 3 characters has a zero):
  Re > 63/100 on |Im| ∈ (13/50, 77/100) ∪ (103/100, 73/50).

## The generalization (−1/3 → −1/7)

Assume c_Cl ≥ 3 and pick three independent quadratic class characters
χ1, χ2, χ3. Average over the 7 nontrivial characters of the (Z/2)^3 subgroup
they generate. At an undetermined prime ideal 𝔭, put
w = (w1, w2, w3) ∈ F2³ with χi(𝔭) = (−1)^wi. The 7 nontrivial characters are
χ^v(𝔭) = (−1)^(v·w), v ∈ F2³ \ {0}.

- If w = 0: all 7 values are +1, average +1.
- If w ≠ 0: exactly half of the 8 characters of (Z/2)^3 take the value +1 at
  𝔭; one of them is the trivial character, so among the 7 nontrivial ones
  exactly 3 give +1 and 4 give −1, average (3 − 4)/7 = −1/7.

Hence the uniform odd-power lower bound at undetermined primes improves from
−1/3 to −1/7. Even powers and forced splits are unchanged (+1). In the code
this is the single constant `unknown_odd = -arb(1)/character_count` in
`prime_bounds`, driven by the fixture field
`number_of_nontrivial_characters_in_average`; the only other edits were that
fixture field (3 → 7) and the verifier's `assert character_count == 3` → `== 7`
(both in the lab copy only). The moment bound does not involve the character
count (the log-derivative bound is per-character uniform), so it is unchanged.

Conclusion shape (same averaging argument as row384): if none of the 7
characters had a zero in the certified region, each zero sum would be
≥ −ε·Mχ with Mχ ≤ 100, forcing the averaged score ≤ ε·100/N = ε·100/105,
contradicting the certified score threshold. So at least one of the 7 has a
zero in the region.

## New certified score (7 characters, row384's region and ε)

Same fixture as row384 except character count 7 (file:
`fixture_avg7_base.json`; run output `avg7_run1.json`):

- prime term ≥ 0.4079279534386562419… (was 0.3691698403775159885…; Δ ≈ +0.0387581)
- **average score ≥ 0.0911527542420397790…** (was 0.0523946411808995256…)
- moment ≤ 99.186384435239… < 100 (unchanged), ε = 7/200, threshold 1/25.

The score headroom (0.09115… vs the 0.04 threshold row384 needed) is what
funds the narrowing below: the score threshold can be raised to 9/100 and ε
to 9/100 while keeping score > threshold and N·threshold = 9.45 > ε·100 = 9
(contradiction gap 9/20).

## Narrowing attempts (6 candidates, all with threshold/ε as stated)

Uniform Re raises (both bands same u_max c), ε and threshold raised together:

- cand1: c = 3/20 (Re > 0.65), ε = 1/20, thr = 3/50 — FAIL. Rectangle
  subdivision hit depth 42 at u → 3/20, t ≈ 0.709 (band 1).
- cand2: c = 17/100 (Re > 0.67), ε = 3/50, thr = 7/100 — FAIL at
  u → 17/100, t ≈ 0.729 (band 1).
- cand3: c = 1/5 (Re > 0.70), ε = 7/100, thr = 2/25 — FAIL at u → 1/5,
  t ≈ 0.743 (band 1).
- cand4: c = 1/4 (Re > 0.75), ε = 9/100, thr = 9/100 — FAIL at u → 1/4,
  t ≈ 0.748 (band 1).

Diagnostic (point evaluations of Re φ(u+it) + εW(u,t) via the verifier's own
`transform_series`; NOT a certificate — scripts `scan_phi.py`, `scan_phi2.py`):
the failures are genuine sign changes of Re φ, not slack in ε. In band 1,
min over t ∈ [0.55, 0.90] of Re φ + εW is +0.0196 at u = 0.13 (ε = 0.035),
+0.0080 at u = 0.14 (ε = 0.09), but −0.052 at u = 0.15 (ε = 0.09), −0.52 at
u = 0.20, −13.0 at u = 0.50 — a real negative patch around t ≈ 0.55–0.65
growing with u. In band 2 (t ∈ [0.95, 1.55], ε = 0.09) the minimum stays
positive through u = 0.17 (+0.0114 at t = 1.34) and turns negative at
u = 0.20 (−0.0084). So band 1 caps at c ≈ 0.14 and band 2 at c ≈ 0.18 for
this test function.

Mixed per-band u_max (ε = 9/100, thr = 9/100):

- cand5: band 1 c = 7/50, band 2 c = 17/100 — PASS (13 s). Region:
  Re > 16/25 = 0.64 (band 1), Re > 67/100 (band 2).
- cand6: band 1 c = 7/50, band 2 c = 9/50 — **PASS** (13 s). Region:
  Re > 16/25 = 0.64 (band 1), Re > 17/25 = 0.68 (band 2). Certified
  rectangles: gaps (u_max 1/2) 9 + 20 + 662 boxes; band 1 (7/50) 16 boxes;
  band 2 (9/50) 12 boxes. Output: `avg7_result.json`; reproducing fixture:
  `fixture_avg7_narrowed.json` (swap in as `fixture384.json` and run
  `verify_average384.py`).

## Final statement (c_Cl ≥ 3 case)

If c_Cl ≥ 3, then for any (Z/2)^3 subgroup of the quadratic class characters
of K, at least one of its 7 nontrivial characters χ has an L(s, χ) zero with

- |Im s| ∈ (13/50, 77/100) and Re s > 16/25 = 0.64, or
- |Im s| ∈ (103/100, 73/50) and Re s > 17/25 = 0.68,

certified with averaged score ≥ 0.0911527542420397790…, threshold 9/100,
ε = 9/100, moment ≤ 99.186384435239… < 100, contradiction gap 9/20.

Versus row384 (which covers c_Cl ≥ 2): the score nearly doubled
(0.0524 → 0.0912) and the necessary-zero region narrowed in Re from 0.63 to
0.64 (band 1) and 0.68 (band 2). The |Im| bands did not move — shrinking
them would push the φ-negative patch (t ≈ 0.55–0.77 at u ≳ 0.14) into the
gap rectangles, which must be certified up to u = 1/2, so t-shrinkage is
blocked by the same patch.

## What this does NOT do

This does not close −30 and gives no unconditional exclusion. It sharpens
the necessary condition in the c_Cl ≥ 3 case only. The hard core is now:
c_Cl = 1 (row383's three bands, Re > 0.562/0.572/0.605), c_Cl = 2 (row384's
Ω2, Re > 0.63, plus ZF2), and c_Cl ≥ 3 with zeros pushed to Re > 0.64/0.68.
Closing any case still needs zero-freeness in the respective region (ZF-type
input) or c_Cl = 0 by other means. Per EXP03, literature zero-free regions
reach only Re ≈ 0.99986 at these heights, so all cases remain far from
classical unconditional tools. No E1/endpoint credit is claimed.
