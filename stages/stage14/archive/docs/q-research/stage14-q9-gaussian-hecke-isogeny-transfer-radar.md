# Stage14-q9 — Gaussian/Hecke and isogeny transfer radar

## Trigger contract

```text
TRIGGER_STAGE=Stage14-4bb + Stage14-s5p(draft) + Stage14-t25(draft)
EXACT_OBSTRUCTION=state-split E multi-edge tensor contraction on the local side + Gaussian allocation / dual-isogeny large-prime routing on the rank-active triple side
CURRENT_BEST_BOUND=14-4bb closes the K4 product-conductor obstruction with delta_K4=1/200 but leaves auxiliary-incidence and state-split E assembly; s5p removes auxiliary-progression loss and leaves active E tensor contraction; t25 forces the 3 mod 4 part of ru into p^2-q^2 but leaves 1 mod 4 Gaussian allocation and the C-column dual descent
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=q8 targeted the earlier one-small-variable linear boundary and torsion quartic collision. Those are now closed/superseded as the live obstructions: the local problem has moved into the Gaussian norm column E=m^2+n^2, while t has moved from torsion squareclass energy to an explicit rank [-1] cover with Gaussian and isogeny columns.
SEARCH_FAMILIES=quadratic large sieve over Q(i)/number fields; Gaussian Jacobi symbols; Hecke-family reciprocity; explicit 2/4/8-descent with rational 2-torsion; rational-isogeny Selmer families; short-interval quadratic-character second moments
LAST_RADAR_BASELINE=Stage14-q8
PROMOTION_STANDARD=an external theorem is DIRECT only after the Stage14 character/ideal dictionary and all coefficient/conductor hypotheses are exact; otherwise record the smallest falsifiable receiving-stage transfer lemma
```

This is a legitimate q9 trigger. The obstruction names and native algebraic objects have changed materially since q8.

No theorem below is promoted to the Stage14 main theorem. The purpose is to route concrete transfer tests into s5q/14-4bc and t26.

---

## 1. Local side: the remaining E-column is naturally Gaussian

The surviving norm column is

```text
E=m^2+n^2=(m+in)(m-in).
```

For every split rational prime `p=1 mod 4`, the two projective roots

```text
m = +r_p n (mod p),
m = -r_p n (mod p),
r_p^2=-1 (mod p)
```

are exactly the two prime-ideal choices above `p` in `Z[i]`, up to conjugation/unit normalization. This is the same signed-root structure already used by s5l--s5p, but q9 records the alternative ideal-language packaging:

```text
signed E root choice <-> Gaussian prime ideal factor of (m+in)
squarefree E state    <-> squarefree ideal supported on split Gaussian primes
root-sign reciprocity <-> quadratic Hecke/residue character after a finite ray-class correction
```

The point is not to replace the proved rational-lattice estimates. It is to ask whether the final **multi-edge E tensor** can be packaged as one quadratic Hecke-family operator rather than expanded root-pattern by root-pattern.

### 1.1 High-priority NEAR: Goldmakher--Louvel / Onodera quadratic large sieve over Q(i)

Goldmakher--Louvel, *A quadratic large sieve inequality over number fields* (arXiv:1112.1642; Math. Proc. Camb. Phil. Soc. 2013), proves the Heath-Brown quadratic large-sieve analogue for quadratic Hecke families over a number field. Their introduction explicitly records Onodera's earlier Q(i) quadratic Jacobi-symbol large sieve as the Gaussian special case.

The structural match is unusually close:

```text
Stage14 split E ideals     <-> squarefree ideals in Q(i)
E reciprocity edge         <-> quadratic Hecke-family value chi_a(b)
finite mod-4/unit choices  <-> fixed ray-class correction group
s5p Hilbert coefficients  <-> arbitrary complex/Hilbert coefficient vectors after coordinatewise lifting
```

The number-field theorem already includes the analogue of quadratic reciprocity through a finite ray-class correction and squarefree ideal indexing. This is exactly the bookkeeping that the state-split E root signs currently create by hand.

But it is **not DIRECT yet**. Three Stage14 compatibility lemmas remain:

1. every active E-edge character in one actual local monomial must be written as a product of a bounded number of quadratic Hecke-family symbols on Gaussian ideals, with only a fixed finite ray-class/unit factor left over;
2. the Euclid incidence `(m,n)` must not leave a two-variable coefficient depending simultaneously on both ideal arguments after the s5p auxiliary tensor packaging;
3. norm/height dyadic ranges for Gaussian ideals must match the theorem after conjugate/gcd/common-prime pieces are removed.

Therefore

```text
S5Q_GAUSSIAN_HECKE_LARGE_SIEVE_TRANSFER=NEAR_HIGH_PRIORITY
S5Q_GOLDMAKHER_LOUVEL_DIRECT=false
S5Q_ONODERA_QI_SPECIAL_CASE=NEAR_HIGH_PRIORITY
```

### Smallest falsifiable receiving-stage test

In Stage14-s5q, choose **one actual active state-split E multi-edge monomial** after s5p. Factor each squarefree E state into Gaussian ideals and attempt an exact rewrite

```text
sum_{a,b in Z[i] ideals} <A_a,B_b> chi_a(b)
```

(or a finite sum of such forms) with

```text
N(a)~A,
N(b)~B,
a,b squarefree and coprime outside a fixed bad ideal,
```

and coefficient norms already controlled by the s5p auxiliary-energy ledger.

Success criterion: obtain a power-saving dyadic bound with no new positive power of the auxiliary modulus. Failure criterion: exhibit the first residual dependence that is not one-ideal-at-a-time; that residual becomes the next q trigger.

This is the strongest q9 analogue of the alpha philosophy: the useful imported object is the **number-field large-sieve architecture**, not a theorem mentioning cuboids.

### 1.2 Secondary 2026 lead: Shparlinski--Xiao short-interval Legendre second moment

Shparlinski--Xiao, *Large sieve inequality for sums of Legendre symbols over short intervals* (arXiv:2604.23661, 2026), proves a second-moment saving for short shifted intervals against prime Legendre moduli, using Burgess plus Selberg sieve.

This is potentially useful only if s5q's Gaussian/Hecke packaging leaves a residual rational-prime slice whose summation variable is genuinely a short interval. It does **not** currently match the full squarefree-ideal tensor.

```text
S5Q_SHPARLINSKI_XIAO_SHORT_INTERVAL=NEAR_SECONDARY
S5Q_SHPARLINSKI_XIAO_FULL_E_TENSOR_DIRECT=false
```

### 1.3 Multivariate polynomial-modulus large sieve is not the right first tool

Halupczok--Munsch's multivariate polynomial-modulus large sieve concerns additive characters to polynomial moduli. The present E obstruction is multiplicative quadratic/Hecke reciprocity, so vocabulary overlap around "multivariate large sieve" is insufficient.

```text
S5Q_MULTIVARIATE_ADDITIVE_POLYNOMIAL_LARGE_SIEVE=BLOCKED_WRONG_CHARACTER_TYPE
```

---

## 2. Main 14-4 routing after s5p

Merged 14-4bb has already consumed s5o and removed the K4 product-conductor obstruction. Its remaining reciprocal-local gate is

```text
AUXILIARY_INCIDENCE_UNIFORMITY + STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

Draft s5p now proves the first term and reduces the residual to the E multi-edge tensor contraction. Therefore q9 does not recommend a new independent 14-4 proof architecture.

The correct routing is

```text
s5p merge
-> s5q Gaussian/Hecke transfer test
-> import the resulting E-sector estimate into 14-4bc
-> only then attempt the first complete reciprocal E_loc exponent
```

So:

```text
MAIN_14_4_AUXILIARY_INCIDENCE_EXPECTED_IMPORT_FROM_S5P=true
MAIN_14_4_NEW_INDEPENDENT_LITERATURE_BRANCH=false
MAIN_14_4_GAUSSIAN_HECKE_E_IMPORT_PRIORITY=true
HANDOFF_MAIN=Stage14-4bc after s5q/s5p imports
```

---

## 3. t side: q8 torsion weapon succeeded; the live problem is rank [-1] descent

q8 recommended square sieve / binary quartic character estimates for the torsion branch. Stage14-t24 subsequently closed that branch more directly:

```text
Q_tor(B)=O(B^(1/2+o(1))).
```

So the q8 torsion literature handoff is now **consumed**, not failed.

The live rank branch has the integral 4-torsion model

```text
E_{D,C}: Y^2=X(X^2+(4D^2-2C^2)X+C^4)
```

and physical `[-1]` cover

```text
W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4).
```

Stage14-t25 proves odd local minimality and forces every `3 mod 4` prime in the relevant `ru` part into

```text
p^2-q^2=(p-q)(p+q).
```

The remaining columns are explicitly:

- `1 mod 4` primes: Gaussian allocation;
- the `C` column: dual-isogeny descent;
- after those, pair counting within the same `(alpha,beta)` packet to obtain a fixed power saving for `Q_rank`.

### 3.1 High-priority NEAR: explicit higher descent for rational 2-torsion

Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point* (arXiv:1509.03234), develops practical higher descent when rational 2-torsion is present, extending the Bremner--Cassels architecture; with full rational 2-torsion it reaches 8-descent.

For Stage14 this is not a family-counting theorem, but it is a strong structural source for the exact **dual-cover normalization** that t26 needs before any analytic count.

```text
T26_FISHER_RATIONAL_2TORSION_DESCENT=NEAR_STRUCTURE_HIGH_PRIORITY
T26_FISHER_FAMILY_POWER_SAVING_DIRECT=false
```

Smallest transfer test in t26:

1. write the explicit degree-2 isogeny and dual isogeny for the t25 integral model;
2. derive the dual homogeneous-space equation for the `C` column in primitive integer variables;
3. factor out forced gcd/square parts and identify the exact moving squarefree columns;
4. verify that all odd bad primes are already among the t25 radical conductor factors;
5. only then couple the dual cover to the Gaussian allocation and count pairs.

This prevents a recurring failure mode: applying a Selmer theorem before the actual Stage14 physical cover and its height/gcd variables are explicit.

### 3.2 High-priority NEAR: Q(i) quadratic large sieve for the 1 mod 4 allocation

The same Goldmakher--Louvel/Onodera Gaussian large-sieve package has a second, independent potential use on t26.

For primes `ell=1 mod 4`, write

```text
ell=pi * conjugate(pi)
```

in `Z[i]`. The t25 sum-of-two-squares identities indicate that the unresolved prime routing is an allocation among Gaussian factors rather than a rational inert-prime obstruction.

If t26's explicit dual descent rewrites the pair condition as quadratic residue symbols between squarefree Gaussian ideal packets, the Q(i) large sieve can attack the **allocation energy** directly.

Again this is `NEAR`, because q9 has not proved the exact t26 ideal-character formula.

```text
T26_GAUSSIAN_ALLOCATION_HECKE_SIEVE=NEAR_HIGH_PRIORITY
T26_GAUSSIAN_ALLOCATION_DIRECT=false
```

### 3.3 Isogeny-Selmer family statistics remain background, not the small-point answer

Chan--Verzobio (arXiv:2508.21406, 2025) proves distributional results for Tamagawa ratios and isogeny Selmer groups in certain rational-isogeny families. Klagsbrun--Lemke Oliver and related work likewise show that rational 2-isogeny families can have nontrivial Selmer/Tamagawa statistics.

These are useful context for what the dual-isogeny local columns may look like statistically, but they do not provide the Stage14 bounded-height physical-point second moment, and the Stage14 `(D,C)` family has not been identified with their family hypotheses.

```text
T26_ISOGENY_SELMER_STATISTICS=BACKGROUND
T26_ISOGENY_SELMER_AS_QRANK_POWER_SAVING=BLOCKED
```

The q3 Le-Boudec architecture remains the family-height benchmark. t25 has now validated part of its large-prime routing rather than invalidating it.

```text
Q3_LE_BOUDEC_TRANSFER_PARTIALLY_VALIDATED_BY_T25=true
Q3_LE_BOUDEC_HEIGHT_ARCHITECTURE_REMAINS_PRIMARY=true
```

---

## 4. Promotion matrix

| Lead | Receiving route | State | Exact reason |
|---|---|---|---|
| Goldmakher--Louvel quadratic large sieve over number fields | s5q E tensor | **NEAR — high priority** | Native quadratic Hecke family over Q(i); exact Stage14 ideal-character/coefficient dictionary still required |
| Onodera Gaussian Jacobi-symbol large sieve | s5q E tensor | **NEAR — high priority** | Direct Q(i) precedent; same missing Stage14 packaging lemma |
| Shparlinski--Xiao 2026 short-interval Legendre second moment | s5q residual short slices | **NEAR — secondary** | Prime-modulus short interval theorem, not full squarefree Gaussian tensor |
| multivariate polynomial-modulus additive large sieve | s5q | **BLOCKED** | additive-character theorem, wrong native operator |
| Fisher higher descent with rational 2-torsion | t26 dual cover | **NEAR — structural high priority** | explicit descent architecture fits torsion structure; no moving-family count |
| Goldmakher--Louvel/Onodera Q(i) sieve | t26 Gaussian allocation | **NEAR — high priority** | plausible ideal-allocation energy tool after dual cover is explicit |
| Chan--Verzobio isogeny-Selmer statistics | t26 | **BACKGROUND / BLOCKED as final answer** | Selmer/Tamagawa distribution does not control physical least-point height or Stage14 second moment |
| Le Boudec large-prime + complete descent | t26 rank branch | **NEAR — retained primary** | t25 already proves a nontrivial part of the predicted large-prime forcing |

No source is promoted as a direct theorem for the full residual obstruction:

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
```

The strongest q9 change is conceptual: **both remaining proof lanes now contain genuinely Gaussian arithmetic, so Q(i) quadratic-Hecke large-sieve technology becomes a common transfer candidate for s5q and t26.**

---

## 5. Receiving-stage handoffs

### Handoff A — Stage14-s5q

```text
S5Q-TRANSFER-TEST
1. take one actual s5p active state-split E multi-edge monomial;
2. encode split E root signs as squarefree Gaussian ideals;
3. derive the exact quadratic Hecke-family symbol including finite ray-class/unit corrections;
4. use s5p auxiliary Hilbert-energy bounds as coefficient norms;
5. apply Goldmakher--Louvel/Onodera if the coefficient becomes one-ideal-at-a-time;
6. record a power-saving exponent or the first irreducible residual dependence.
```

### Handoff B — Stage14-t26

```text
T26-TRANSFER-TEST
1. derive the explicit isogeny and dual homogeneous space of the t25 integral model;
2. normalize primitive/gcd/square parts and expose the moving C-column squareclasses;
3. factor every 1 mod 4 prime column in Z[i];
4. test whether same-(alpha,beta) pair conditions become quadratic Hecke symbols between Gaussian packets;
5. combine the t25 3 mod 4 forcing, Gaussian allocation, and dual cover into one large-prime pair count;
6. seek any fixed delta>0 in Q_rank(B)=O(B^(1-delta)); otherwise isolate the exact remaining column.
```

### Handoff C — Stage14-4bc

Do not duplicate s5q. Import merged s5p/s5q results and assemble the first explicit reciprocal error exponent. Keep the diagonal/local-density term as a separate contract; do not relabel a reciprocal cancellation exponent as `rho_loc` without proving the constant/diagonal term.

---

## 6. q-route stop rule after q9

q9 again finds no black-box theorem that closes Stage14. It does find a common cross-domain transfer that did not become visible until s5p/t25 exposed Gaussian structure.

```text
STAGE14_Q9=COMPLETE_GAUSSIAN_HECKE_AND_ISOGENY_TRANSFER_RADAR
TRIGGER_STAGE=Stage14-4bb+Stage14-s5p+Stage14-t25
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q8_TORSION_HANDOFF_CONSUMED_SUCCESSFULLY=true
S5Q_GAUSSIAN_HECKE_LARGE_SIEVE_TRANSFER=NEAR_HIGH_PRIORITY
S5Q_ONODERA_QI_SPECIAL_CASE=NEAR_HIGH_PRIORITY
S5Q_SHORT_INTERVAL_2026_TRANSFER=NEAR_SECONDARY
T26_FISHER_RATIONAL_2TORSION_DESCENT=NEAR_STRUCTURE_HIGH_PRIORITY
T26_GAUSSIAN_ALLOCATION_HECKE_SIEVE=NEAR_HIGH_PRIORITY
T26_ISOGENY_SELMER_AS_QRANK_POWER_SAVING=BLOCKED
Q3_LE_BOUDEC_TRANSFER_PARTIALLY_VALIDATED_BY_T25=true
MAIN_14_4_NEW_INDEPENDENT_LITERATURE_BRANCH=false
HANDOFF_S=Stage14-s5q
HANDOFF_T=Stage14-t26
HANDOFF_MAIN=Stage14-4bc
NEXT_Q_STAGE=NONE_UNTIL_GAUSSIAN_TRANSFER_TEST_FAILURE_OR_NEW_STABLE_OBSTRUCTION
```

Do not open q10 merely because s5q/t26 advance one number. Reopen only if their exact transfer tests fail in a named way or produce a new stable operator that q1--q9 does not cover.
