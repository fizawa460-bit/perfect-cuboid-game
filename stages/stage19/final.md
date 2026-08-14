# Stage19 final self-contained interface bundle — R01

```text
BUNDLE_ID=STAGE19-FINAL-SELF-CONTAINED-20260814-R01
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=FROZEN_AUDIT_PASS
STAGE=Stage19
SELF_CONTAINMENT=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
POPULATION=primitive canonical cuboids with exactly two integral face diagonals and integral space diagonal
COUNT=N_2(B)
CUTOFF=R<=B
SPACE_DIAGONAL_REQUIRED=true
EXACT_FACE_MULTIPLICITY=2
```

This bundle is the proof-facing Stage19 interface for downstream Stages20, 23, 24, 25 and 28. It deliberately separates four evidence species that must not be conflated: the inherited half-power upper theorem, the independent squareclass zero-density mechanism, exact finite numerical evidence, and the audited unresolved lower-bound gate.

## 1. Executive theorem statement

Let
\[
R=\sqrt{a^2+b^2+c^2}
\]
and let `I_ab,I_ac,I_bc` be the three face-square predicates. Define
\[
\mathcal A_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ I_{ab}+I_{ac}+I_{bc}=2,\ R\in\mathbf Z\},
\]
\[
N_2(B)=\#\mathcal A_2(B).
\]

The strongest certified Stage19 conclusions are:

1. **Whole-family upper bound**
   \[
   \boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}=B^{1/2+o(1)}.}
   \]
2. **Matched survival bound** against the Stage18 exactly-two population
   \[
   M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
   \]
   hence
   \[
   \boxed{\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}\to0.}
   \]
3. **Exact new arithmetic predicate**
   \[
   \boxed{R\in\mathbf Z\iff \operatorname{sf}(A)=\operatorname{sf}(B)},
   \]
   for the paired Gaussian norms defined below.
4. **Independent causal zero-density theorem** from the same-measure split-prime parity sieve:
   \[
   \boxed{N_2(B)/M_2(B)\to0.}
   \]
   This proof does not use the Stage14 half-power theorem as its source of zero density.
5. **Exact finite floor** from the frozen numerical observatory:
   \[
   N_2(500{,}000{,}000)=3495,
   \]
   so by monotonicity
   \[
   \boxed{N_2(B)\ge3495\quad(B\ge500{,}000{,}000).}
   \]
6. No unbounded primitive construction, positive-power lower bound, matching half-power lower bound, or asymptotic for `N_2(B)` is certified.

## 2. Scope, population, cutoff and multiplicity

Stage19 counts physical edge triples exactly once under
\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]
Permutation copies are removed by strict canonical ordering and scale copies by primitivity. Exactly two, not at least two, face diagonals are integral. Exactly-three-face cuboids are outside Stage19.

On a Stage19 object the integral space diagonal is the geometric quantity `d=R`. Therefore
\[
\boxed{R\le B\iff d\le B}
\]
exactly. No comparable-height or constant-factor cutoff adapter occurs.

Two successful faces share exactly one edge. Choosing that unique shared edge is an intrinsic description of the physical object, not an additional multiplicity. The positive toric parameterization used below is uniquely reconstructible from the physical shared-edge incidence after the frozen chamber convention, so no hidden parameter multiplicity is introduced.

## 3. Frozen upstream interface A: Stage18 denominator

```text
UPSTREAM_STAGE=Stage18
UPSTREAM_THEOREM=M_2(B) ~ C_M2 B(log B)^5 with C_M2>0 on primitive canonical exactly-two cuboids under R<=B
POPULATION_MATCH=true before imposing R integral
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
CURRENT_RELATION=Stage19 = Stage18 intersect {R integral}
```

Thus Stage18 supplies the literal matched source population for the Stage18-to-Stage19 ratio.

## 4. Frozen upstream interface B: Stage14 quantitative numerator theorem

```text
UPSTREAM_STAGE=Stage14
UPSTREAM_THEOREM=N_2(B) <<_epsilon B^(1/2+epsilon) for the primitive canonical exactly-two integral-space population under d<=B
POPULATION_MATCH=true after exact-two mask selection
CUTOFF_MATCH=true because d=R on Stage19
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=strongest certified whole-family upper bound
MATCHING_LOWER_BOUND_IN_SOURCE=false
ASYMPTOTIC_IN_SOURCE=false
```

The Stage14 theorem is imported only as an upper bound. Nothing in Stage19 converts exponent `1/2` into a true growth exponent.

## 5. Frozen upstream interface C: Stage15 exact squareclass normal form

On the positive shared-edge toric coordinates `(m:n),(r:s)`, define raw quantities
\[
E=4mnrs,
\quad X=2rs(m^2-n^2),
\quad Y=2mn(r^2-s^2),
\]
and let `G=gcd(E,X,Y)` be the primitive scaling factor. The physical edges are `(e,x,y)=(E,X,Y)/G`.

Define
\[
A=m^2r^2+n^2s^2=N(mr+i\,ns),
\qquad
B=m^2s^2+n^2r^2=N(ms+i\,nr).
\]
Direct expansion gives
\[
E^2+X^2+Y^2=4AB.
\]
Because `R^2=e^2+x^2+y^2`,
\[
G^2R^2=4AB.
\]
The factors `G^2` and `4` are squares. Moreover if `4AB=T^2`, then `G^2|T^2`, hence `G|T`, so there is no divisibility gap when returning to the primitive physical diagonal. Therefore
\[
R\in\mathbf Z\iff AB\in\mathbf Z^2.
\]

For a positive integer `n`, let
\[
\operatorname{sf}(n)=\prod_{v_p(n)\text{ odd}}p.
\]
A product `AB` is a square exactly when the parity vectors of the prime valuations of `A` and `B` agree. Hence
\[
\boxed{R\in\mathbf Z\iff AB\in\mathbf Z^2\iff \operatorname{sf}(A)=\operatorname{sf}(B).}
\]
Equivalently, uniquely,
\[
A=kP^2,\qquad B=kQ^2
\]
for a squarefree `k>0`.

This derivation is printed here because the normal-form equivalence is load-bearing for the Stage19 causal interpretation.

## 6. Frozen upstream interface D: Stage15 same-measure local sieve

For every survivor and every prime,
\[
v_p(A)\equiv v_p(B)\pmod2.
\]
For inert odd primes `p=3 mod 4`, Gaussian norm valuations are automatically even and the local acceptance is `rho_p=1`.

For every good split prime `p=1 mod 4`, the frozen same-measure local density is
\[
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)},
\]
so
\[
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
\]
For every fixed finite set `S` of good split primes,
\[
M_{2,S}(B)=C_{M_2}\left(\prod_{p\in S}\rho_p\right)B(\log B)^5+o_S(B(\log B)^5).
\]
Every Stage19 survivor lies in every accepted local set, so for fixed `S`,
\[
\limsup_{B\to\infty}\frac{N_2(B)}{M_2(B)}
\le \prod_{p\in S}\rho_p.
\]
Take `B->infinity` first. Only afterward enlarge the finite set `S`. Since the reciprocal-prime sum over `p=1 mod 4` diverges and `1-rho_p=4/p+O(p^-2)`,
\[
\prod_{p\in S}\rho_p\to0.
\]
Therefore
\[
\boxed{N_2(B)/M_2(B)\to0.}
\]

The quantifier order is essential: no growing-modulus uniformity is claimed. The corresponding local product has logarithmic profile and is not credited with producing the separate half-power upper theorem.

## 7. Stage19 internal implication chain

The new work of Stage19 is principally interface locking and theorem-species separation. The load-bearing implications are as follows.

### 7.1 Exact matched survival ratio

Stage19 is literally Stage18 intersected with `R integral`, under the same primitive/canonical physical measure and exact cutoff. Therefore `N_2(B)/M_2(B)` is a legal source-to-target survival ratio with no adapter loss.

### 7.2 Quantitative thinning from separate frozen interfaces

Using
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]
and
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]
division gives
\[
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]
For any fixed `epsilon<1/2`, this tends to zero.

This proof and the local-sieve zero-density proof are different theorem species. Their savings are not multiplied.

### 7.3 Finite lower floor

The exact finite census certifies 3495 distinct physical Stage19 objects with `R<=500,000,000`. Since the sets `A_2(B)` are nested as `B` increases,
\[
B\ge500,000,000\implies A_2(500,000,000)\subseteq A_2(B).
\]
Thus
\[
N_2(B)\ge3495.
\]
This proof yields a constant floor only. Because Stage19 is primitive, nontrivial scalar multiples of known objects are excluded and cannot generate an unbounded primitive family.

## 8. Numerical evidence interface

The numerical observatory contract is

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_POPULATION_ADAPTER=select exact-two face mask from primitive canonical integral-space ledger; d=R gives d<=B iff R<=B
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

The frozen B500m endpoint is
\[
N_2=3495,
\qquad (N_a,N_b,N_c)=(1374,1371,750).
\]
The predeclared sample-size gate is passed, but the terminal stability gate for `N_2(B)/sqrt(B)` fails. Hence finite evidence does not identify exponent `1/2` and is not theorem proof.

The finite triple-face count `T=0` inside this particular census is not a perfect-cuboid nonexistence theorem.

## 9. Negative knowledge and OPEN_GATE

Checkpoint50 is frozen as

```text
OPEN_GATE=UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19
OPEN_GATE_STATUS=OPEN_GATE_AUDITED_PASS
OPEN_GATE_REENTRY_JUSTIFIED=NO
```

The following remain unproved:

- `N_2(B)->infinity`;
- an infinite primitive Stage19 construction;
- `N_2(B)>>B^delta` for any fixed `delta>0`;
- a matching `B^(1/2-o(1))` lower bound;
- an asymptotic `N_2(B)~C B^(1/2)`;
- sharpness or intrinsic status of exponent `1/2`;
- a strict sub-square-root upper theorem.

This negative ledger does not assert that no such family or theorem exists.

## 10. Causal and transition boundaries

Stage19 certifies the exact new arithmetic predicate and a same-measure mechanism proving zero density. It does not claim that the space-diagonal condition is probabilistically independent of the two prior face conditions.

The deeper comparative classification belongs to Stage24:

```text
STAGE24_OWNS=Stage18 -> Stage19 independence/correlation/interaction classification
INDEPENDENT_OF_PRIOR_CONDITIONS=UNRESOLVED_DEFER_STAGE24
```

Stage23 compares Stage17 to Stage19, Stage25 compares Stage16 to Stage19, and Stage28 performs the cross-transition synthesis.

## 11. External theorem boundary

Stage19 directly invokes no new published external theorem. Its theorem inputs are frozen project-internal interfaces from completed Stages14, 15 and 18. Any external literature used inside those completed stages belongs to their frozen proof contracts and is not re-adapted here.

```text
EXTERNAL_THEOREM_DEPENDENCIES=NONE_DIRECT_IN_STAGE19
UPSTREAM_INTERFACES_EXACT=true
```

## 12. Stage70 synthesis and stop rule

Stage19-70 adds no new theorem branch. It records the maximal safe synthesis:

- exact population and ratio interfaces;
- strongest certified upper theorem;
- exact squareclass predicate;
- independent local zero-density mechanism;
- exact finite evidence and constant floor;
- unresolved lower-bound and exponent questions;
- Stage24 interaction boundary.

Further progress requires genuinely new theorem/computation input or belongs to a downstream transition stage. The audited lower-bound OPEN_GATE is not reopened.

```text
SYNTHESIS_STOP_RULE_SATISFIED=YES
LOWER_STAGE_REINTERPRETATION_REQUIRES_REOPEN=NO
OPEN_GATE_REENTRY_JUSTIFIED=NO
```

## 13. Nonclaims

- no asymptotic for `N_2(B)`;
- no matching lower bound;
- no proof of unboundedness or infinitely many primitive Stage19 objects;
- no proof that exponent `1/2` is sharp or intrinsic;
- no independence or product-probability claim;
- no multiplication of the Stage14 upper saving by the Stage15 local-sieve saving;
- no directional limiting law;
- no perfect-cuboid existence or nonexistence conclusion;
- finite `T=0` is not global nonexistence.

## 14. Provenance ledger

Canonical Stage19 records:

- population: `stages/stage19/19-10/result.md`;
- finite baseline: `stages/stage19/19-20/result.md`;
- ratio: `stages/stage19/19-30/result.md`;
- upper bound: `stages/stage19/19-40/result.md`;
- lower/construction ledger: `stages/stage19/19-50/result.md`;
- causal decomposition: `stages/stage19/19-60/result.md`;
- bounded synthesis: `stages/stage19/19-70/result.md`;
- controller: `stages/stage19/19-controller.json`.

Frozen load-bearing upstream interfaces are printed above. Repository paths are provenance only.

## 15. Fresh hostile-review checklist

A fresh Stage19 audit verified:

1. exact population, cutoff and multiplicity locks;
2. literal Stage18 matched denominator interface;
3. Stage14 numerator theorem is upper-only and population matched;
4. both directions of the squareclass normal form, including primitive divisibility;
5. local density formula, fixed-finite-prime quantifier order and zero-density deduction;
6. no credit of half-power to the local sieve and no double charge;
7. finite B500m adapter and constant-floor deduction;
8. no finite-data asymptotic promotion;
9. checkpoint50 OPEN_GATE remains closed to re-excavation without new input;
10. Stage24 retains interaction/independence classification;
11. all Stage70 required fields and stop rule are present;
12. bundle/arsenal decisions are justified.

## 16. Machine-readable lock

```text
BUNDLE_ID=STAGE19-FINAL-SELF-CONTAINED-20260814-R01
STATUS=FROZEN_AUDIT_PASS
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STAGE=Stage19
CHECKPOINT_10=PROVED_AUDITED_PASS
CHECKPOINT_20=COMPUTED_AUDITED_PASS
CHECKPOINT_30=PROVED_AUDITED_PASS
CHECKPOINT_40=PROVED_AUDITED_PASS
CHECKPOINT_50=OPEN_GATE_AUDITED_PASS
CHECKPOINT_60=PROVED_AUDITED_PASS
CHECKPOINT_70=PROVED_AUDITED_PASS
UPSTREAM_INTERFACES_EXACT=true
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_DEPENDENCIES=NONE_DIRECT_IN_STAGE19
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO_FOR_STAGE18_RATIO
NUM_POPULATION_ADAPTER_REQUIRED=YES_AND_PROVED
FINITE_DATA_PROMOTED_TO_THEOREM=false
QUANTIFIER_ORDER_FIXED_S_THEN_B_LIMIT=YES
DOUBLE_CHARGE_CHECK=PASS
HALF_POWER_INTRINSIC=UNRESOLVED
MATCHING_LOWER_BOUND=false
UNBOUNDEDNESS_PROVED=false
INDEPENDENT_OF_PRIOR_CONDITIONS=UNRESOLVED_DEFER_STAGE24
OPEN_GATE=UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19
OPEN_GATE_REENTRY_JUSTIFIED=NO
PERFECT_CUBOID_CONCLUSION=NONE
SYNTHESIS_STOP_RULE_SATISFIED=YES
SELF_CONTAINED_BUNDLE_REQUIRED=YES
ARSENAL_PROMOTION_REQUIRED=NO
FRESH_AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
MERGE_ALLOWED=true
NEXT_STAGE=Stage20
```
