# EXP09 — E7: tail extension to 10^7 (2026-11-21)

Extends the row383 tail table (exact degree-one prime counts) from
p ≤ 1,982,760 to p ≤ 10^7 and measures what the longer tail buys in
the row383 verifier. All runs are the FULL verifier
(verify_spectral383.py, check_exterior included), on lab copies; the
repo clone was not modified.

## 1. What the tail table counts (semantics)

For every rational prime p with B = 5003 < p ≤ LIMIT, one CSV row
"p,c" with

    c(p) = deg gcd(f mod p, x^p − x)  in F_p[x],

f = the degree-105 stem polynomial (curve_C29.json, F_ascending).
c(p) is the number of DISTINCT roots of f in F_p (x^p − x is
separable, so a repeated root mod p is counted once). This is the
definition in both prior implementations, which agree:
row382_inputs.degree_one_count (python-flint) and the original
generator row380/roots379.cpp (row379, GMP C++). Stored table:
147,058 primes in (5003, 1982760], sum(c) = 147,527, sha256
572183b2… (the value pinned in row382_inputs.SHA).

## 2. How the verifier consumes it (verify_spectral383.py)

prime_bounds, with σ = 7/5, x = log p, q = p^σ, and
known(p) = number of forced-split ideals above p (from
mod2_supports382; 3,552 split primes in the old range, 273 more in
the extension range, one ideal each):

- log_deriv (moment side): each tail prime contributes
  x·((c − known)/(q+1) − known/(q−1)).
- score_prime: a tail prime contributes (2·known − c)·x/√p·f(x)
  ONLY if x < support t = 7237/500 ≈ 14.474, i.e. p ≲ 1.93·10^6.
  Every such prime is already in the OLD table, so the score is
  structurally independent of any extension past 1,982,760.
- The finite cutoff produces exactly one bound term, for the
  unenumerated primes p > LIMIT in log_deriv (Chebyshev
  θ(y) ≤ log(4)·y):  N·log4·σ/(σ−1)·LIMIT^{1−σ}/(1 − LIMIT^{−σ}).
  Raising LIMIT replaces the (LIMIT, 10^7] part of that bound by
  exact counts and shrinks the residue. The verifier requires
  e^t < LIMIT < B² = 25,030,009; 10^7 satisfies this.

## 3. Validation (step 2 — exact reproduction)

count_roots.py (python-flint nmod_poly gcd, same definition)
recounted ALL 147,058 primes in (5003, 1982760]: the output
(recount_old.csv) is BYTE-IDENTICAL to the stored table
(sha256 572183b2eccf… = the pinned value), sum 147,527.
28.4 s with 3 workers (0.19 ms/prime effective; 0.29 ms/prime
single-worker benchmark near the top of the range). No semantics
discrepancy anywhere.

## 4. Extension (step 3)

516,851 primes in (1982760, 10^7], counted in 8 checkpointed
chunks (chunks/tail_*.csv, one per million-wide range, ~15 s
each, 124 s total), sum of counts 516,809. Assembled table:

- tail_roots_10m.csv — 663,909 rows (5003 < p ≤ 10^7),
  sum(c) = 664,336, 6,551,781 bytes,
  sha256 e5c2e2bed583ed3ac20c4ceb956a2a62438e558a679746aada89889c61735644.

Verifier runs use lab copies with LIMIT = 10000000, the len/sum
asserts updated to 663,909 / 664,336, and the row382_inputs SHA
entry updated to the new table's hash (run-base/, run-candG/,
run-base-thr/, run-candG-thr/). Each full run: 15–17 s.

## 5. Certified before/after (step 4)

| fixture | tail | score_lower | moment_upper | gap |
|---|---|---|---|---|
| base | 1,982,760 | 0.0098858898430937020… | 99.1863844352390574… | 29/1000 |
| base | 10^7 | 0.0098858898430937020… | **98.4550015213825703…** | 29/1000 |
| candG (EXP06) | 1,982,760 | 0.0103597391213032410… | 99.1863844352390574… | 140749/400000 |
| candG (EXP06) | 10^7 | 0.0103597391213032410… | **98.4550015213825703…** | 140749/400000 |
| base, moment_thr 100→99 | 10^7 | 0.0098858898430937020… | 98.4550015213825703… | **39/1000** |
| candG, moment_thr 9919/100→9846/100 | 10^7 | 0.0103597391213032410… | 98.4550015213825703… | **71433/200000** |

- score_lower is IDENTICAL to the last digit in both fixtures
  (prime term also identical: base 0.2846007880573495856…,
  candG 0.2849749902353319635…), as §2 predicts. Bands,
  certified rectangles and tail ratio are identical to the
  corresponding old-tail outputs.
- moment_upper improves by Δ = 0.7313829138564871 in both
  fixtures (the moment is weights-independent — cf. EXP08).
  Decomposition (arb, verifier's own expressions): the Chebyshev
  term falls 1.5424274344666490 → 0.8074447222926290
  (gain 0.7349827121740200), minus the exact sum over the newly
  covered primes, 0.0035997983175329 (exact sum over the old
  range, for reference: 0.0542988145584509). Net 0.7313829138564871,
  matching the verifier outputs exactly.
- The reported gap is a function of the fixture THRESHOLDS, so
  with fixtures as-is it does not move. Converted into gap by
  the legitimate threshold redesign of EXP06 (thresholds are
  free constants policed by the verifier's asserts; certified
  moment 98.4550015213825703… < 9846/100 < 99), two extra FULL
  runs certify: base gap 0.029 → 0.039 (+34%), candG gap
  0.3518725 → 0.357165 (+0.0052925, +1.5%).

## 6. Ceiling of this direction

The residual Chebyshev term at LIMIT = 10^7 is still
0.8074447222926290 — most of the remaining tail part of
log_deriv (0.8653433351686128). LIMIT is capped at B² =
25,030,009 by the verifier's assert, and even at LIMIT → B²
the term only falls to 0.5594076547027249: at most ≈ 0.248
more moment is buyable by tail extension, ever, at the price
of counts to 2.5·10^7. The score cannot move at all (§2).

## Verdict

E7 DONE. The tail extension buys exactly one thing: moment
headroom (99.186 → 98.455), worth gap 0.029 → 0.039 in the
base configuration and 0.3518725 → 0.357165 on top of EXP06's
candG after threshold redesign. It buys no score and no band
movement, and the direction is now within 0.248 of its
absolute ceiling. −30 NOT closed; no exclusion; no credit.

Files: count_roots.py (counting code), tail_roots_10m.csv
(extended table), chunks/ (8 checkpoint CSVs), recount_old.csv
(validation recount), run-base/ run-candG/ run-base-thr/
run-candG-thr/ (patched verifier copies + result_*.json).
