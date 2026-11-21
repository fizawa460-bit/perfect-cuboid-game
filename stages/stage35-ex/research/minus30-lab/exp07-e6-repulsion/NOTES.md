# EXP07 — E6: Deuring–Heilbronn repulsion variant (2026-11-21)

Lab copies of row383/row384 only; the repo clone was not modified.
Verifier: python-flint 0.9.0 (venv /tmp/flintenv, recreated 2026-11-21).
Scripts: `budgets.py`, `row384/scan_bands384.py` (+ `scan384.out`),
`row383/scan_bands383.py`, `row384/group_diag.py` (uses the patched copy
`row384/verify_group.py`, one line changed: `unknown_odd = 0`).

## Verdict (negative, three independent obstructions)

**No repulsion is available from these test functions.** Assuming one
character has a band zero changes the other characters' necessary-zero
conclusion by exactly nothing: no pushed-right region, no narrower
window, not even one extra forced zero orbit. The obstruction is
structural (obstruction 1), and the two quantitative escape routes are
closed by wide margins (obstructions 2 and 3). Do not retry E6 with the
row383/row384 test functions; §5 states the exact criterion a future
test function would have to meet.

## 1. The budget identity (the only place an assumed zero can enter)

For one character, Σ_ρ φ(ρ−1/2) = −105·B_χ (Poitou, repo normalization).
Splitting the zero sum at the certified band region R and using
Re φ ≥ −εW outside R with Σ W = M_χ ≤ M (certified M = 99.186384435239…):

  Z_in(χ) := Σ_{ρ: (u,t) ∈ R} Re φ(ρ−1/2) ≤ −105·B_χ + ε·M_χ.

For an N-character average with certified score lower bound S this gives
the **total in-band negativity budget**

  Σ_{χ∈X} Z_in(χ) ≤ −G_N,   G_N := 105·N·S − N·ε·M   (`budgets.py`).

| configuration | region R | G_N (certified values) | G_N (fixture thresholds) |
|---|---|---|---|
| row383 baseline (per char) | 3 bands, Re>0.562/0.572/0.605 | 0.046155 | 0.029 |
| row383 candG / EXP06 (per char) | same | 0.368671 | 0.3518725 |
| row384 (N=3) | Ω2: Re>0.63, t∈(0.26,0.77)∪(1.03,1.46) | 6.089742 | 2.1 |
| EXP05 7-char base (ε=7/200) | Ω2 | 42.696610 | — |
| EXP05 7-char cand6 (ε=9/100) | Re>0.64 / 0.68 | 4.509852 | 3.15 |

Answer to task question (a): `verify_average384.py` has no slot for an
assumed zero — it certifies S, M and exterior positivity, and the
assumption can only be applied to the derived budget inequality above.
That is what was done here.

Zeros enter Z_in in full symmetry orbits {ρ, ρ̄, 1−ρ, 1−ρ̄}: φ is even
and real on the real axis, so one orbit at (u,t), u = |Re ρ − 1/2|,
contributes exactly **4·Re φ(u+it)**.

## 2. Obstruction 1 — a scalar budget cannot localize (structural)

The N characters' zero sums enter the average through the single scalar
inequality Σ Z_in ≤ −G_N. Assume χ1 has exactly one orbit in R at
(u1,t1), contributing −c1 := 4·Re φ(u1+it1). Then the others must satisfy

  Σ_{χ≠χ1} Z_in(χ) ≤ −G_N + c1        (∗)

(and χ1's further orbits only weaken this). Consequences:

- If c1 ≥ G_N, (∗) is vacuous for the others.
- If c1 < G_N, (∗) forces negativity totalling G_N − c1 from the
  others — but **never localizes it**: for any proper subregion
  R′ ⊊ R with inf_{R∖R′} Re φ < 0, placing k orbits of χ2 at one
  deep point of R∖R′ supplies k·4·|Re φ| → ∞ of negativity, so
  configurations satisfying (∗) with χ2, χ1χ2 zerofree in R′ always
  exist. Zero multiplicities are unbounded; a budget is one linear
  constraint and cannot see *where* the others' zeros are.
- The only localization this formalism ever produces is the positivity
  region {Re φ + εW > 0} itself, which is independent of any assumed
  zero. Hence "the others are pushed right / into narrower windows"
  is unattainable from the row384/EXP05 average, for any assumed zero.
  (Two test functions do not rescue this in practice: φ383 and φ384
  have their negative patches in the same place — both attain their
  minima at (u,t) → (0.5, 0.44), −24.2 and −19.9 — so a deep orbit
  outside any proposed R′ satisfies both budgets at once.)

Measured assumed-zero shifts (φ384, from the scan): c1 ranges over
[−18.9, +79.7] depending on where ρ1 sits — e.g. c1 = +2.35 at
(u,t) = (0.2, 0.6), +31.1 at (0.5, 0.6), −0.015 at (0.14, 0.6)
(Re φ > 0 there: the zero *helps*), −18.9 at (0.14, 0.3) (Re φ = +4.72,
others' bill rises by 18.9 — still not localizing, see §3).

## 3. Obstruction 2 — one orbit eats the whole budget (counting fails)

The weakest conceivable gain would be counting: if one orbit could
supply at most c_max < G_N of negativity, the budget would force
≥ 2 orbits. Measured minima of Re φ over the band regions (arb point
evaluations with the verifier's own `phi0`; fast path cross-checked
against `transform_series`, agreement to ≥14 digits; grid step 0.005,
minima attained at the corner u → 0.5):

| test function | region | min Re φ | at (u,t) | c_max = −4·min |
|---|---|---|---|---|
| φ384 | Ω2 band 1 | −19.920 | (0.5, 0.435) | 79.68 |
| φ384 | Ω2 band 2 | −1.742 | (0.5, 1.16) | 6.97 |
| φ383 baseline | band 1 | −24.191 | (0.5, 0.44) | 96.76 |
| φ383 candG | band 1 | −24.203 | (0.5, 0.44) | 96.81 |
| φ383 (both) | band 2 / band 3 | −2.94 / −0.33 | (0.5, 1.175) / (0.5, 1.835) | 11.8 / 1.32 |

Counting ratios G_N / c_max (must exceed 1 for any counting gain):

- row383 baseline: 0.0462/96.76 ≈ 0.0005; candG: 0.3687/96.81 ≈ 0.0038
- row384: 6.0897/79.68 ≈ 0.076
- EXP05 7-char base: 42.6966/79.68 ≈ **0.536** (the closest call)
- EXP05 cand6: 4.5099/79.68 ≈ 0.057

All < 1, so a single deep orbit supplies 1.9×–2000× the entire budget
in every configuration: the assumed zero can absorb everything and the
others need contribute nothing. This exclusion is rigorous, not just
float: the budgets are certified, and one rigorously evaluated point
(Re φ384(0.5 + 0.435i) = −19.92…, arb interval radius ~1e-33) already
upper-bounds the true infimum, hence lower-bounds c_max. The depth is
driven by u → 1/2 (Re ρ → 1): min_t Re φ384 grows from −0.057 at
u = 0.14 to −19.92 at u = 0.5 (full profile in `scan384.out`). EXP06's
candG redesign does not help: it leaves φ383's in-band depth unchanged
(−24.20 vs −24.19).

## 4. Obstruction 3 — the classical DH channel is vacuous here

Classical Deuring–Heilbronn needs the FULL group {1, χ1, χ2, χ1χ2} in
the average: odd-power prime coefficients become (1+χ1+χ2+χ1χ2)/4 ∈
{0,1}, i.e. the undetermined-prime lower bound improves −1/3 → 0.
Diagnostic (`group_diag.py`, repo prime machinery with that one bound
changed; arch/moment of the trivial character taken as the repo's
stand-ins — flagged, not certified): group-average score
S_G ≈ 0.120221 (vs 0.052395 for the 3-char average), giving a group
budget G_group = 4·(105·S_G − ε·M) ≈ 36.6 at ε = 7/200. **But** the
trivial character's explicit formula carries the pole terms
φ(1/2) + φ(−1/2) = 2φ(1/2), and φ384(1/2) = 45.367…, so the pole
contributes **+90.7** to the zero side. The group inequality collapses
to Σ_{χ∈G} Z_in(χ) ≤ −36.6 + 90.7 = **+54.1**: it forces no in-band
negativity at all. The channel is vacuous before ζ_K's zeros even
enter — and independently, ζ_K's own in-band contribution Z_in(ζ_K)
has no available lower bound (per EXP03, literature zero-free regions
for ζ_E reach only Re ≈ 0.99986 at these heights, and zero-density at
σ = 0.63 with log-conductor ≈ 400 is astronomically weak), so nothing
could be attributed to χ2 even if the pole term were smaller. This is
presumably *why* the repo's averages exclude the trivial character.
(φ383 is worse: φ383(1/2) = 50.41, pole ≈ +100.8.)

## 5. What a future test function would need (criterion, for the record)

A counting/repulsion gain in an N-character average with budget G_N
requires a test function whose in-band depth is shallow:

  −min_{(u,t) ∈ R} Re φ(u+it) < G_N / 4.

For the EXP05 7-char configuration that means min Re φ > −10.67 on Ω2
(actual: −19.92; misses by a factor 1.87). For a per-character row383
statement it means min > −0.092 with candG (actual −24.20; misses by
263×). Shallow depth fights the mechanism itself: the bands are
necessary *because* φ dips negative, and |φ| grows like e^{T·u} toward
u = 1/2. A function with support/degree redesigned to cap the u-growth
is a different fixture family (cf. E2(c) length splits — still open,
but note E2(c)'s success criterion is narrower bands / larger gap,
not shallow depth; a depth-capped variant would be a new queue item,
not E6 retried).

## 6. Scope

No E1/endpoint credit; −30 is not closed under any outcome here, and
none was possible: E6 only ever aimed at a stronger *necessary*
condition. GRH is not assumed anywhere; §4's diagnostic is float-level
and flagged as such, §§1–3 rest on the repo's certified values plus
rigorous point evaluations. E6 is DONE (negative). Do not retry with
the row383/row384 test functions.
