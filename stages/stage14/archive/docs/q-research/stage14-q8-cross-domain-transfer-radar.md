# Stage14-q8 — Triggered cross-domain transfer radar for s5n / t24

## Trigger contract

```text
TRIGGER_STAGE=Stage14-s5m + Stage14-t23
EXACT_OBSTRUCTION=s5m one-small-variable switched Jacobi boundary operators + t23 active-direction rank/torsion second moment
CURRENT_BEST_BOUND=s5m closes central/medium dispersion but not switched boundary averages; t23 splits Q_active <= 2 Q_rank + 2 Q_tor but proves no power saving for either second moment
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=q2/q4 were recorded before these two reductions exposed a hyper-skewed one-small-variable operator and two explicit quartic squareclass packets
SEARCH_FAMILIES=neutraliser quadratic large sieve; hyperbolic Jacobi bilinear forms; Burgess bounds for characters at forms; square/polynomial sieve; binary quartic square-value counts; quadratic-twist 2-Selmer statistics
LAST_RADAR_BASELINE=Stage14-q7
PROMOTION_STANDARD=exact hypothesis match, or a receiving-stage transfer lemma with a falsifiable first test; no vocabulary-only promotion
```

This is a legitimate q8 trigger under q7: both receiving tracks have reduced their previous broad obstructions to explicit operators/forms that did not exist when q2/q4 were frozen.

No result below is promoted to a Stage14 theorem. `DIRECT` means the quoted external theorem is usable on an already-isolated Stage14 subexpression after routine normalization; `NEAR` means one nontrivial Stage14 compatibility lemma remains; `BLOCKED` records the exact reason a tempting shortcut is insufficient.

---

## 1. s5n trigger: the switched boundary is now hyper-skewed

Stage14-s5m reduces a large linear state divisor by exact complementary-divisor switching

```text
u > H_i/Z,
u | L_i(P),
k = |L_i(P)|/u < Z,
(u/v) = (|L_i(P)|/v)(k/v).
```

After the switch, the genuinely small object is `k`, while `v` can remain on a much larger dyadic scale. The unresolved task is not the already-closed six-linear medium determinant problem; it is to average this one-small-variable Jacobi operator together with the physical character and the finite local-state polynomial.

This is precisely the geometry in which a result optimized for **hyper-skewed quadratic-character bilinear sums** can be more relevant than a symmetric quadratic large sieve.

### 1.1 High-priority NEAR lead: Wilson 2025 neutraliser large sieve

Cameron Wilson, *An improved large sieve for quadratic characters via Hooley neutralisers and its applications*, arXiv:2506.22667v2 (2025), Theorem 1.1, proves a quadratic-character bilinear estimate of the form

```text
sum_{n<=N,m<=M} a_n b_m f(m) (n/m)
```

for bounded odd-supported coefficients and a multiplicative weight `f` satisfying

```text
0 <= f(p) <= 1,
f(p^r) <= f(p),
sum_{p<=X} f(p)/p = alpha log log X + O(1),  0<alpha<1.
```

The displayed theorem gives

```text
<<_eps M N^(1/2) log N / (log M)^(1-alpha)
 + M^(1/2+eps) N^(3/2) (log N)^(1/2) / (log M)^((1-alpha)/2).
```

Wilson explicitly identifies the theorem/corollary as most effective in hyper-skewed regions (roughly the regime in which the small variable is much shorter than the large one), and recommends combining it with Heath-Brown/Friedlander–Iwaniec-type bounds in the comparable-scale region.

### Stage14 dictionary

Candidate normalization for s5n:

```text
Wilson n      <-> small complementary cofactor k (or small state modulus)
Wilson m      <-> large squarefree state modulus v
(n/m)         <-> (k/v)
f(m)          <-> multiplicative admissibility/local-state support in v
b_m           <-> bounded residual v-state coefficient
a_n           <-> bounded small-cofactor coefficient
extra factor  <-> physical character (|L_i(P)|/v) and frozen local-state data
```

### Verified compatibility

- s5m has already produced a genuine one-small-variable / one-large-modulus Jacobi factor.
- the small variable is created by an exact divisor complement, not by a heuristic truncation;
- the relevant moduli are odd after the existing Stage14 2-adic split;
- Wilson's theorem is intentionally strongest in a highly skewed range, exactly where the old symmetric bulk treatment is least natural.

### Unverified compatibility — the real s5n test

The Stage14 term is **not yet literally** Wilson's product coefficient `a_k b_v f(v)(k/v)` because

```text
(|L_i(P)|/v)
```

and the remaining finite local-state/incidence restrictions still depend on the physical Euclid point. They must first be reorganized so that all non-Jacobi dependence is either

1. absorbed into bounded one-variable coefficients, or
2. represented by a finite number of multiplicative `f(v)` weights satisfying Wilson's prime-average hypothesis.

Until that is proved:

```text
S5N_WILSON2025_NEUTRALISER_TRANSFER=NEAR_HIGH_PRIORITY
S5N_WILSON2025_DIRECT_APPLICATION=false
```

### Smallest falsifiable receiving-stage test

Stage14-s5n should isolate one actual switched monomial from the full finite character polynomial and attempt the exact rewrite

```text
sum_{k~K} sum_{v~V} A_k B_v f(v) (k/v)
```

with `K << V` and `|A_k|,|B_v|<=B^o(1)` after normalizing divisor weights. Then:

- prove or disprove the required prime-average law for `f`;
- record the residual dependence that prevents separation if the rewrite fails;
- apply Wilson in the skewed blocks and the already-owned Heath-Brown/Wilson-type symmetric bounds elsewhere;
- sum the resulting exponent ledger over the s5m boundary partition.

This is the closest q8 analogue of the successful num-alpha transfer: do not import the whole external problem, import the architecture exactly where Stage14 has reduced to its native shape.

### 1.2 Old hyperbolic Jacobi theorem: useful warning, not the boundary solution

Wilson, *General bilinear forms in the Jacobi symbol over hyperbolic regions* (arXiv:2208.14909; later Monatshefte für Mathematik), proves cancellation for suitable squarefree Jacobi bilinear sums over hyperbolic regions **away from the axes** and also explains the obstruction when the near-axis region is included.

That theorem therefore validates the existing q7/s5m decomposition rather than closing s5n directly:

```text
S5N_WILSON2023_INTERIOR_GEOMETRY=CONSISTENT_WITH_EXISTING_BULK
S5N_WILSON2023_NEAR_AXIS_DIRECT_USE=BLOCKED
```

The new 2025 neutraliser estimate is the more natural literature transfer for the actual one-small-variable boundary.

### 1.3 Secondary NEAR lead: Burgess bounds at forms

Pierce–Xu, *Burgess bounds for short character sums evaluated at forms* (2019), develops Burgess-type cancellation for nonprincipal characters evaluated at admissible homogeneous forms in short multidimensional boxes.

Potential Stage14 use: after freezing the small cofactor and state data, the physical numerator `L_i(P)` or a later polynomial numerator may become a character evaluated at a fixed Euclid form.

Direct import is not currently justified because the published theorem is formulated for prime modulus / admissible-form boxes, while Stage14 carries squarefree composite state moduli and divisor-incidence restrictions.

```text
S5N_PIERCE_XU_FORM_BURGESS_TRANSFER=NEAR_SECONDARY
```

### 1.4 Spectral/Kloosterman escalation remains deferred

Recent bilinear Kloosterman improvements obtained via quadratic-character technology are potentially powerful only after a Poisson/Voronoi/Fourier transformation actually creates a Kloosterman kernel. s5m currently leaves a Jacobi-symbol operator, not a Kloosterman form.

```text
S5N_KLOOSTERMAN_SPECTRAL_ESCALATION=DEFERRED_NO_KERNEL_YET
```

This preserves the q7 anti-regression rule against jumping to deeper spectral machinery before the elementary switched operator is exhausted.

---

## 2. t24 trigger: t23 makes the torsion collision polynomial explicit

Stage14-t23 reduces the torsion-active branch to two Euclid quartic squareclass packets

```text
F_plus(m,n)  = m^4 + 6m^2 n^2 + n^4,
F_minus(m,n) = m^4 + n^4,

(alpha,beta) = (1, core(F_plus))
             or (2, core(F_minus)).
```

The active second moment satisfies

```text
Q_active <= 2 Q_rank + 2 Q_tor.
```

So t24 can attack the torsion squareclass collision and rank-active height frequency separately.

### 2.1 Exact q8 structural observation: the pair character correlation factors

For positive integers `A,B`, equality of squarefree kernels is equivalent to `AB` being a square. Therefore a torsion-packet collision is a square-value problem

```text
Y^2 = F(m,n) F(m',n').
```

But for every odd prime `p` away from the discriminant,

```text
chi_p(F(m,n) F(m',n'))
 = chi_p(F(m,n)) chi_p(F(m',n')).
```

Hence the square-sieve prime correlation **separates into two binary-quartic character sums**. This is materially sharper than treating t24 as a generic nonseparable four-variable polynomial-sieve problem.

Elementary discriminant audit of the dehomogenized quartics gives

```text
disc(x^4 + 1)             = 2^8,
disc(x^4 + 6x^2 + 1)     = 2^14.
```

Thus both quartics are separable modulo every odd prime. The only universal bad prime from these discriminants is `2`; Stage14 already isolates 2-adic data separately.

Also, because both forms are homogeneous of degree four, scaling `(m,n)` by `lambda` multiplies `F` by `lambda^4`, a square. Their squareclass therefore descends naturally to the reduced projective Euclid direction `[m:n]`.

Locks from this observation:

```text
T24_TORSION_COLLISION_IS_QUARTIC_SQUARE_VALUE_PROBLEM=true
T24_SQUARE_SIEVE_PRIME_CORRELATION_FACTORIZES=true
T24_FMINUS_DEHOMOG_DISCRIMINANT=2^8
T24_FPLUS_DEHOMOG_DISCRIMINANT=2^14
T24_QUARTIC_SQUARECLASS_PROJECTIVE_IN_DIRECTION=true
```

These are algebraic identities/reductions, not a power-saving theorem.

### 2.2 High-priority NEAR lead: square sieve + binary-form character estimates

The revised weapon order for the t24 torsion packet should be:

1. square sieve on the equality `core(F(u))=core(F(v))`;
2. exploit the exact factorization of each prime correlation;
3. bound the resulting **single binary-quartic character sums** using the strongest compatible complete/incomplete character estimates;
4. only invoke a genuinely nonseparable polynomial sieve if this separated route fails.

Pierce–Xu's Burgess-at-forms machinery is therefore a concrete `NEAR` building block for incomplete binary-quartic sums. `F_minus=m^4+n^4` is visibly of the diagonal-form type; `F_plus` still needs the precise admissibility/nondegeneracy hypotheses checked against the theorem rather than inferred from separability alone.

```text
T24_PIERCE_XU_BINARY_QUARTIC_TRANSFER=NEAR_HIGH_PRIORITY
T24_SQUARE_SIEVE_FIRST_AFTER_T23=true
```

### 2.3 Generic polynomial sieve is no longer the first move

Bonolis–Pierce, *Application of a polynomial sieve: beyond separation of variables*, supplies a powerful polynomial-sieve framework when the relevant hypersurface satisfies its nonsingularity/geometric hypotheses.

A naive Stage14 pair cover

```text
Y^2 = F(m,n)F(m',n')
```

has a reducible branch divisor and special intersections, so a black-box direct application of a generic smooth/nonseparable theorem is not currently justified. More importantly, t23's product structure means the prime correlation already separates, so forcing a nonseparable treatment may throw away useful structure.

```text
BONOLIS_PIERCE_GENERIC_NONSEPARABLE_DIRECT=false
T24_GENERIC_POLYNOMIAL_SIEVE=RESERVE_AFTER_FACTORIZED_ROUTE
```

The square-sieve / hyperelliptic-fibration literature remains useful as architecture if the separated character-sum route leaves a genuine geometric residual problem, but q8 does not promote such a result directly.

---

## 3. t24 rank-active branch: no new shortcut around the height gate

The t23 finite audit puts the observed B<=2m active edges in the positive-rank side, but this does not turn average-rank or Selmer-rank theorems into the needed family frequency theorem.

Modern 2-Selmer distribution results for quadratic twists with rational 2-torsion (for example Pan–Tian's work on distributions of 2-Selmer ranks) are tempting because the t22 quotient has rational torsion. Two independent obstacles remain:

1. the Stage14 direction family has not been identified as one fixed quadratic-twist family in the required sense;
2. even a rank/Selmer distribution does not control whether the **least physical non-torsion point** lies inside Stage14's logarithmic height window.

Therefore q7's height boundary survives:

```text
T24_RANK_PAN_TIAN_SELMER_AS_SMALL_POINT_FREQUENCY=BLOCKED
AVERAGE_RANK_ALONE_SUFFICIENT=false
Q3_LE_BOUDEC_HEIGHT_TRANSFER_REMAINS_PRIMARY=true
```

The receiving rank-side experiment remains the q3 `LE_BOUDEC_TRANSFER_TEST`: large prime factor on one of the five Euclid factors + exact Stage14 2-descent + physical small-height variable bounds + divisor/congruence count.

---

## 4. Main 14-4 routing

q8 does **not** recommend a new independent literature branch for `14-4` at this moment.

The current 14-4 residual boundary overlaps the s-track's microscopic/complementary-state analysis. The anti-duplication rule from q6 remains the correct order:

```text
s5n transfer test first
-> import any proved boundary estimate into 14-4
-> only then reopen q if a genuinely new main-track residual operator survives.
```

Thus:

```text
MAIN_14_4_NEW_LITERATURE_SCAN_REQUIRED=false
MAIN_14_4_IMPORT_S5N_FIRST=true
```

---

## 5. Promotion matrix

| Lead | Route | State | Exact reason |
|---|---|---|---|
| Wilson 2025 Hooley-neutraliser quadratic large sieve | s5n | **NEAR — high priority** | Native hyper-skewed Jacobi shape; residual physical/state dependence still must separate |
| Wilson 2023 hyperbolic Jacobi bilinear theorem | s5n | **BLOCKED for boundary / useful interior precedent** | Requires geometry away from axes; s5m boundary is deliberately near-axis |
| Pierce–Xu Burgess at forms | s5n | **NEAR — secondary** | Form-character cancellation relevant; modulus/incidence hypotheses not yet matched |
| square sieve + factorized binary quartic correlations | t24 torsion | **NEAR — high priority** | t23 makes correlation separable; still need uniform character-sum/exponent summation |
| Pierce–Xu on binary quartics | t24 torsion | **NEAR — high priority** | candidate incomplete quartic character estimate; exact admissibility check remains |
| generic Bonolis–Pierce polynomial sieve | t24 torsion | **BLOCKED as direct first move** | naive pair cover has special/reducible branch geometry; separated structure should be used first |
| Pan–Tian 2-Selmer distribution | t24 rank | **BLOCKED as small-point answer** | not yet a fixed twist family; Selmer/rank does not control first physical height |
| Le Boudec large-prime + complete 2-descent architecture | t24 rank / s height | **NEAR — retained primary** | already q3-approved architecture; Stage14 transfer theorem still to prove |
| new K3/Shimada scan | 14-4 | **BLOCKED absent new geometry** | fixed M4 package already consumed; current obstruction is analytic |

No q8 source gives the full Stage14 obstruction theorem unchanged:

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
```

But q8 does produce two concrete high-priority transfers that are sharper than the q7 shelf because the receiving objects are now explicit.

---

## 6. Receiving-stage handoffs

### Handoff A — Stage14-s5n

Primary test:

```text
S5N-TRANSFER-TEST
1. choose one actual switched boundary monomial;
2. expose k<<v and isolate (k/v);
3. absorb/freeze the physical character and local states into one-variable coefficients if possible;
4. prove the v-weight is multiplicative with Wilson's prime-average law, or record the exact failure;
5. use Wilson 2025 on hyper-skewed blocks;
6. use existing HB/QLS machinery on comparable blocks;
7. sum the boundary exponent ledger.
```

Success criterion: a fixed power saving for the complete one-small-variable boundary contribution, not merely one model sum.

### Handoff B — Stage14-t24

Primary torsion test:

```text
T24-QUARTIC-SQUARE-SIEVE-TEST
1. work projectively in primitive reduced directions [m:n];
2. write Q_tor as squarefree-kernel collision energy for F_plus/F_minus;
3. apply a square-sieve decomposition;
4. use chi_p(F(u)F(v))=chi_p(F(u))chi_p(F(v));
5. prove uniform binary-quartic character bounds on the actual Euclid boxes/congruence classes;
6. optimize sieve prime range and sum partitions;
7. test whether Q_tor=O(B^(1-delta)) follows for any fixed delta>0.
```

Rank branch remains separately routed to the Le-Boudec-style height transfer rather than being multiplied by torsion/local densities.

---

## 7. Sources audited

Primary/authoritative literature objects used in this pass:

- Cameron Wilson, *An improved large sieve for quadratic characters via Hooley neutralisers and its applications*, arXiv:2506.22667v2 (2025), especially Theorem 1.1 and Corollary 1.2.
- Cameron Wilson, *General bilinear forms in the Jacobi symbol over hyperbolic regions*, arXiv:2208.14909 / Monatshefte für Mathematik.
- Lillian B. Pierce and Junyan Xu, *Burgess bounds for short character sums evaluated at forms*.
- Sandro Bonolis and Lillian B. Pierce, *Application of a polynomial sieve: beyond separation of variables*.
- current 2-Selmer distribution literature for rational-2-torsion quadratic-twist families (Pan–Tian), audited only as a tempting but insufficient rank-side shortcut.

q3's Le Boudec / Petsche / Naccarato shelf and q4's square-sieve shelf remain inherited dependencies and are not reclassified without a new hypothesis check.

---

## 8. q8 locks

```text
STAGE14_Q8=COMPLETE_TRIGGERED_CROSS_DOMAIN_TRANSFER_RADAR
TRIGGER_STAGE=Stage14-s5m+Stage14-t23
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
S5N_WILSON2025_NEUTRALISER_TRANSFER=NEAR_HIGH_PRIORITY
S5N_WILSON2023_NEAR_AXIS_DIRECT_USE=BLOCKED
S5N_PIERCE_XU_FORM_BURGESS_TRANSFER=NEAR_SECONDARY
S5N_KLOOSTERMAN_SPECTRAL_ESCALATION=DEFERRED_NO_KERNEL_YET
T24_TORSION_COLLISION_IS_QUARTIC_SQUARE_VALUE_PROBLEM=true
T24_SQUARE_SIEVE_PRIME_CORRELATION_FACTORIZES=true
T24_FMINUS_DEHOMOG_DISCRIMINANT=2^8
T24_FPLUS_DEHOMOG_DISCRIMINANT=2^14
T24_QUARTIC_SQUARECLASS_PROJECTIVE_IN_DIRECTION=true
T24_PIERCE_XU_BINARY_QUARTIC_TRANSFER=NEAR_HIGH_PRIORITY
T24_SQUARE_SIEVE_FIRST_AFTER_T23=true
BONOLIS_PIERCE_GENERIC_NONSEPARABLE_DIRECT=false
T24_RANK_PAN_TIAN_SELMER_AS_SMALL_POINT_FREQUENCY=BLOCKED
Q3_LE_BOUDEC_HEIGHT_TRANSFER_REMAINS_PRIMARY=true
MAIN_14_4_NEW_LITERATURE_SCAN_REQUIRED=false
MAIN_14_4_IMPORT_S5N_FIRST=true
HANDOFF_S=Stage14-s5n
HANDOFF_T=Stage14-t24
NEXT_Q_STAGE=NONE_UNTIL_TRANSFER_TEST_FAILURE_OR_NEW_TRIGGER
```

## Boundary

This q8 pass changes the **weapon routing**, not the proved Stage14 exponent. In particular:

```text
S5N_BOUNDARY_POWER_SAVING_PROVED=false
T24_TORSION_SECOND_MOMENT_POWER_SAVING_PROVED=false
T24_RANK_SECOND_MOMENT_POWER_SAVING_PROVED=false
Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```
