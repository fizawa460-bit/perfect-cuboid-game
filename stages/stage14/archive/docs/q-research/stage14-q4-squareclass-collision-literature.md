# Stage14-q4 — Global squareclass / collision literature pass

## Status

```text
STAGE14_Q4=COMPLETE_GLOBAL_SQUARECLASS_COLLISION_LITERATURE_PASS
CHECKED_AT=2026-08-09
TRIGGER_STAGE=Stage14-t20 draft PR #261
EXACT_OBSTRUCTION=partition-resolved missing-face squareclass collision energy Q_split(B)
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
HIGH_PRIORITY_NEAR_WEAPONS=3
PRIMARY_RECOMMENDATION=square/polynomial-sieve reformulation before generic Selmer machinery
Q3_STATUS=NOT_EXECUTED_BY_THIS_PR
Q2_STATUS=SEPARATE_PR_260
HANDOFF=Stage14-t21 after t20 merge
```

## 1. Trigger and exact current target

Stage14-t19 identified the missing-face squareclass as the conditioned discriminant squareclass. Draft Stage14-t20 then corrects the asymptotic population from exactly-two objects to raw-pair edges and writes, for an edge with shared side `s` and space diagonal `d`,

```text
m(e) = d^2 - s^2 = g^2 h^2 A B,
A = alpha r^2,
B = beta u^2,
gcd(alpha,beta)=1,
kappa(e) = [m(e)] = alpha beta in Q*/Q*2.
```

The corrected collision energy is

```text
Q_edge(B) = sum_k n_k(B)^2,
3 T(B) = n_1(B),
9 T(B)^2 <= Q_edge(B).
```

Draft t20 further resolves the squarefree kernel into coprime pieces and obtains

```text
Q_edge(B) <= B^o(1) Q_split(B),
Q_split(B) = sum_{alpha,beta} N_{alpha,beta}(B)^2.
```

Thus any fixed power saving

```text
Q_split(B) = O(B^(1-delta))
```

would imply the t-track target `T(B)=o(sqrt(B))`.

This q4 pass asks whether the literature already contains a theorem or proof architecture that controls this kind of moving squareclass collision energy.

## 2. Key reformulation found by q4

For nonzero integers `x,y`, equality of squareclasses is equivalent to their product being a square:

```text
[x] = [y] in Q*/Q*2
iff
xy is a rational square.
```

Hence the Stage14 collision count can be rewritten exactly as a square-value count on **pairs of raw edges**:

```text
kappa(e1)=kappa(e2)
iff
m(e1)m(e2) is a square.
```

After t20's square-factor removal, equivalently

```text
(alpha1 beta1)(alpha2 beta2) is a square.
```

Because the factors are squarefree, this is precisely the same kernel-collision condition, not a relaxation.

This changes the literature priority. The closest human technology is no longer generic Selmer-distribution theory. It is first:

1. Heath-Brown type **square sieve**;
2. Browning/Bonolis/Pierce **polynomial sieve / thin-set sieve**;
3. square-sieve methods on **families/fibrations**;

with Selmer/Kummer machinery retained only when the raw-edge parameterization naturally organizes into a genuine elliptic twist or descent family.

## 3. René Peschmann 2026 — exact perfect-cuboid square-value framework

### 3.1 Quartic reductions and elliptic obstructions for perfect Euler bricks

**Primary source:** René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328, submitted 2026-04-10.

**Verified statements relevant to q4:**

- the perfect cuboid problem is reduced to simultaneous square conditions in two Euclid pairs;
- these conditions are packaged into a one-parameter genus-3 hyperelliptic family
  `C_A: w^2=lambda^8+A lambda^4+1`;
- the distinguished elliptic quotient is
  `E_A: y^2=(x+A)(x-2)(x+2)`;
- Corollary 5.2 turns non-degenerate rational points on `C_A` into a **square-value problem** for a rational function `f(P)` on `E_A`;
- the Kummer character is nontrivial on 4-torsion and 2-descent excludes specified squareclass families;
- the paper explicitly states that these obstructions do not cover all descent classes and do not prove global nonexistence.

**Fit to Stage14:** `NEAR / strong structural corroboration`.

This is unusually close in philosophy to t17--t20: Euclid parametrization -> higher-genus cover -> elliptic quotient -> Kummer/squareclass -> 2-descent -> square-value obstruction.

**Why it does not close q4:** Peschmann studies existence/nonexistence of square lifts on individual parameter fibers. Stage14 now needs an **average collision-energy bound across the whole raw-edge family under physical height**. The paper does not supply an estimate of the form `Q_split(B)=o(B)` or a family second moment for squareclass multiplicities.

**Handoff value:** use Peschmann as a coordinate/geometry cross-check whenever t21 derives an explicit rational-function square condition. Do not treat the fiberwise Kummer obstruction as an averaged collision theorem.

### 3.2 Torsion-intersection proof on 1,072 fibers

**Primary source:** René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072, submitted 2026-04-30.

**Verified content:** for 1,072 explicit master-tuple fibers, rank-zero certificates plus torsion-intersection arguments exclude non-degenerate perfect-cuboid points unconditionally.

**Fit:** `NEAR / finite-fiber weapon`.

**Mismatch:** a strong exact result on finitely many fibers is not a uniform positive-density or power-saving theorem over Stage14's moving physical-height family. It is therefore excellent for diagnostics and exceptional-fiber elimination, but not the present `Q_split` asymptotic.

## 4. Browning polynomial sieve — closest second-moment architecture

**Primary source:** T. D. Browning, *The polynomial sieve and equal sums of like polynomials*, arXiv:1306.6767.

### 4.1 Why this is highly relevant

Browning formulates a general polynomial sieve extending Heath-Brown's square sieve. The special case `f(x;y)=x^2-y` recovers the square sieve exactly.

More importantly for the present Stage14 target, the application is explicitly a **collision second moment**: for a polynomial `f`, Browning studies nontrivial solutions of

```text
f(y1)+f(y2)=f(y3)+f(y4)
```

and targets a fixed power saving over the natural diagonal scale. For quartic `f`, Theorem 1.3 proves

```text
E_f(B) << B^(2-1/6+epsilon).
```

The exact equation differs from Stage14, but the proof architecture is conceptually aligned with `Q_split`: isolate the unavoidable diagonal, transform the nontrivial collision relation, expose common factors, then apply a polynomial/square sieve to the residual family.

**Fit:** `NEAR / high priority proof architecture`.

### 4.2 Concrete Stage14 transfer test

After t20 is merged, t21 should try to parameterize each raw-edge chart by integer variables `theta` such that, after removing forced square factors,

```text
m(e(theta)) = square(theta) * K(theta),
```

with `K(theta)` an integral polynomial or controlled rational form.

A collision then becomes

```text
Y^2 = K(theta) K(theta').
```

This is a direct square-sieve target on the pair parameter `(theta,theta')`.

The transfer test is not complete until all of the following are checked:

1. finitely many parameter charts cover the raw-edge family with `B^o(1)` multiplicity;
2. denominators can be cleared without introducing a moving squareclass ambiguity;
3. fixed square factors and gcd strata are separated explicitly;
4. the remaining product polynomial is not identically a square on a positive-dimensional component;
5. diagonal/automorphism components are isolated before applying the sieve;
6. the sieve variable-height box converts back to physical `B` with enough exponent saving.

If these checks pass, the square/polynomial sieve is the most direct existing human weapon found in q4.

## 5. Bonolis--Pierce — polynomial sieve beyond separation of variables

**Primary source:** Dante Bonolis and Lillian B. Pierce, *Application of a polynomial sieve: beyond separation of variables*, arXiv:2209.02494; published in *Algebra & Number Theory* 18 (2024).

**Verified content:** they give the first application of a polynomial sieve producing a nontrivial point-count bound for a polynomial relation `F(Y,X)=0` that does **not** exhibit separation of variables. Their framework interprets the solvability set as a type-II thin set and proves nontrivial upper bounds under a nonsingularity hypothesis for the associated weighted projective hypersurface.

**Fit:** `NEAR / highest-priority modern transfer candidate`.

This matters because Stage14's collision cover may not simplify to `Y^2-G(theta,theta')=0` in one globally separated chart after primitive/gcd/order constraints are retained. Bonolis--Pierce shows that nonseparability is not automatically fatal.

**Critical unverified hypotheses for Stage14:**

- dimension of the final free parameter vector;
- weighted homogeneity after physical-height normalization;
- irreducibility and nonsingularity of the collision cover away from known diagonal/gcd components;
- whether the theorem's ambient-box saving survives restriction to the thin raw-pair subfamily;
- conversion from parameter height to cuboid physical height.

No theorem is promoted to `DIRECT` until t21 writes the actual collision polynomial and checks these hypotheses.

## 6. Heath-Brown--Pierce / Bonolis--Browning — square sieve on covers and fibrations

### 6.1 Heath-Brown--Pierce

**Primary source:** D. R. Heath-Brown and Lillian B. Pierce, *Counting rational points on smooth cyclic covers*, arXiv:1109.1455.

**Verified content:** the paper obtains bounds for perfect `r`-th power values of multivariable polynomials via an `r`-th power sieve combined with a `q`-analogue of van der Corput, in the setting of smooth cyclic covers.

**Fit:** `NEAR` if t21's pair-collision cover becomes a smooth double cover of a sufficiently large-dimensional parameter space.

**Mismatch:** Stage14's raw-pair family has strong Pythagorean/gcd/order constraints and may be low-dimensional or singular along arithmetic diagonals. The smooth high-dimensional theorem cannot be imported before those geometric conditions are audited.

### 6.2 Bonolis--Browning

**Primary source:** Dante Bonolis and Tim Browning, *Uniform bounds for rational points on hyperelliptic fibrations*, arXiv:2007.14182.

**Verified content:** a square-sieve variant gives uniform bounded-height point estimates on families of surfaces fibred by hyperelliptic curves.

**Fit:** `NEAR / secondary geometry route`.

If fixing part of the t21 Euclid data turns the squareclass-collision condition into a hyperelliptic fiber, this is a more natural architecture than forcing a global Selmer model.

## 7. Thin-set / Hilbert-irreducibility benchmark

Bonolis--Pierce review the quantitative Hilbert-irreducibility benchmark: for a type-II thin set in affine `n`-space, classical results give a saving of roughly one half-power relative to the ambient `B^n` count, while stronger Serre-type bounds seek codimension-one strength under good geometry.

**Fit:** `BACKGROUND / benchmark`.

This is useful conceptually because a square-lift condition is naturally a degree-2 cover. However Stage14's needed statement is not merely "the liftable set is thin". The physical raw-edge population itself is already arithmetic and sparse, so an ambient thin-set theorem must be reweighted/restricted before it says anything about `Q_split(B)`.

## 8. Krumm — squarefree parts of polynomial values

**Primary source:** David Krumm, *Squarefree parts of polynomial values*, arXiv:1407.4890.

**Verified content:** studies which squarefree parts occur among rational polynomial values and their behavior modulo primes, including local/global questions.

**Fit:** `BACKGROUND`.

This confirms that the squarefree-kernel map itself is a standard arithmetic object, but the paper does not give the Stage14 quantitative second moment

```text
sum_k n_k(B)^2
```

or a power-saving collision bound. Do not cite it as a solution to t21.

## 9. 2-Selmer distribution literature — important but presently not first-line

**Representative primary source:** Jinzhao Pan and Ye Tian, *On the Distribution of 2-Selmer ranks of Quadratic Twists of Elliptic Curves over Q*, arXiv:2503.21462.

**Verified content:** establishes distribution/moment results for 2-Selmer ranks in quadratic-twist families with full rational 2-torsion.

**Fit to current t20/t21 target:** `BLOCKED for direct import / secondary if a twist model reappears`.

Reason: after t20's factorization, the target is a collision count of squarefree kernels attached to raw-pair edges. It is not currently parameterized as the 2-Selmer rank distribution of a fixed elliptic curve under quadratic twisting. Generic Selmer moments therefore do not imply that the map

```text
edge -> alpha beta
```

has small collision energy.

Reopen this literature only if t21 constructs a genuine fixed-curve twist parameter whose Selmer/Kummer class equals the missing-face kernel.

## 10. Decision table

| Weapon | q4 status | Exact use | Present blocker |
|---|---|---|---|
| Peschmann genus-3/Kummer/2-descent | NEAR | exact perfect-cuboid square-value geometry; independent cross-check | fiberwise, no family collision energy |
| Peschmann 1,072-fiber torsion intersection | NEAR | eliminate/certify explicit fibers | finite list, no asymptotic |
| Heath-Brown square sieve via Browning polynomial sieve | NEAR, high priority | count pairs for which product of kernel forms is a square | must write Stage14 collision polynomial/charts |
| Bonolis--Pierce nonseparable polynomial sieve | NEAR, highest priority modern route | handle nonseparated square-lift cover | nonsingularity/dimension/height hypotheses unverified |
| Heath-Brown--Pierce cyclic-cover power sieve | NEAR | smooth multivariable square-cover counting | Stage14 cover may be low-dimensional/singular |
| Bonolis--Browning hyperelliptic fibration square sieve | NEAR | fiberwise family counting after partial fixing | correct fibration not yet derived |
| Krumm squarefree parts | BACKGROUND | language/local behavior of squarefree kernels | no second-moment bound |
| generic 2-Selmer twist distribution | BLOCKED direct | possible later if a fixed twist model emerges | wrong family/statistic at t20 |

## 11. Recommended t21 proof order

The q4 literature pass changes the recommended order for the t-route.

### Step A — parameterize collision pairs before doing more descent

Write a finite set of raw-edge parameter charts and an explicit squarefree-kernel representative `K(theta)` after removing forced squares and gcd strata.

### Step B — turn collision energy into a square-lift cover

Use

```text
kappa(theta)=kappa(theta')
iff
Y^2 = K(theta) K(theta').
```

The diagonal `theta=theta'` and any symmetry-induced identical-edge components must be split off explicitly.

### Step C — audit square/polynomial-sieve hypotheses

For every chart record:

```text
PARAMETER_DIMENSION=
COLLISION_POLYNOMIAL=
IRREDUCIBLE_AFTER_DIAGONAL_REMOVAL=
GENERICALLY_NONSQUARE=
COVER_SMOOTHNESS_STATUS=
PARAMETER_TO_PHYSICAL_HEIGHT_EXPONENT=
EXPECTED_SIEVE_SAVING=
```

### Step D — choose the human weapon by geometry

- separated square polynomial -> Heath-Brown/Browning square sieve;
- nonseparated but nonsingular weighted cover -> Bonolis--Pierce;
- hyperelliptic fibration after fixing variables -> Bonolis--Browning;
- smooth higher-dimensional cyclic cover -> Heath-Brown--Pierce;
- elliptic twist/Kummer model genuinely appears -> reopen Selmer literature;
- special explicit fibers -> Peschmann torsion-intersection/rank-zero route.

### Step E — convert the resulting exponent to the exact t20 budget

A generic "power saving" is not enough until it is compared to the physical target

```text
Q_split(B)=O(B^(1-delta)).
```

The parameter-height exponent and chart multiplicity must be propagated explicitly.

## 12. Final q4 conclusion

No literature theorem found in this pass can be imported unchanged to prove

```text
Q_split(B)=o(B).
```

However q4 does find a materially better human-tool match than the previous generic "Selmer/squareclass collision" label:

> **After t20, the global collision problem is exactly a perfect-square value problem on pairs of raw-edge parameters. The primary literature weapon should therefore be a square/polynomial sieve on the pair cover, with Peschmann's Kummer/2-descent work as a close perfect-cuboid-specific structural cross-check and fallback fiberwise obstruction.**

The next useful proof-stage experiment is not another abstract squareclass formalism. It is to write the explicit t21 pair-collision polynomial, remove its diagonal/square components, and test the hypotheses of Browning / Bonolis--Pierce.

```text
NEXT_T_HANDOFF=Stage14-t21 explicit pair-collision cover + square/polynomial-sieve hypothesis audit
Q4_DIRECT_CLOSE=false
Q4_PRIMARY_WEAPON_SHIFT=SELMER_FIRST_TO_SQUARE_POLYNOMIAL_SIEVE_FIRST
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```
