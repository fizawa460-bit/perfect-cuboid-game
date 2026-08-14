# Stage19-60 — causal decomposition

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 is the primitive canonical exactly-two-face population after imposing an integral space diagonal. Checkpoints30/40/50 have already separated the certified thinning law, one-sided half-power upper bound, and the still-open lower-bound problem. Checkpoint60 identifies the arithmetic mechanism without reopening those ledgers.

## 1. Source geometry already present before Stage19

The Stage18 source population has exactly two integral faces. After choosing their unique shared edge `e` and the two non-shared edges `x,y`, the source geometry is the double Pythagorean system

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,\qquad x^2+y^2\notin\square.
\]

Stage19 adds only the condition that the space diagonal

\[
R^2=e^2+x^2+y^2
\]

is integral. The population, primitivity, canonical ordering, physical-object measure and cutoff `R<=B` do not change.

## 2. Exact new arithmetic restriction

Use the frozen Stage15 positive shared-edge toric coordinates `(m:n),(r:s)` and define

\[
A=m^2r^2+n^2s^2=N(mr+i\,ns),
\qquad
B=m^2s^2+n^2r^2=N(ms+i\,nr).
\]

Stage15-4 proved the exact identity

\[
G^2R^2=4AB,
\]

where `G` is the primitive gcd removed from the raw shared-edge incidence. Hence

\[
\boxed{R\in\mathbf Z
\iff AB\in\mathbf Z^2
\iff \operatorname{sf}(A)=\operatorname{sf}(B).}
\]

Equivalently, uniquely,

\[
A=kP^2,\qquad B=kQ^2
\]

for one squarefree core `k>0`.

Therefore the **exact Stage18-to-Stage19 restriction** is not a generic random-square test. It is equality of the squareclasses of two coupled Gaussian norms built from the same toric parameters.

## 3. Certified causal zero-density mechanism

For the exact survivor condition, every prime must satisfy

\[
v_p(A)\equiv v_p(B)\pmod2.
\]

For inert odd primes `p=3 mod 4`, Gaussian norm valuations are automatically even, so there is no local loss there.

For every good split prime `p=1 mod 4`, Stage15-6 proved on the same charged physical toric measure the exact local acceptance density

\[
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)},
\]

with

\[
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
\]

For every fixed finite split-prime set `S`, the refined same-measure asymptotic is

\[
M_{2,S}(B)=C_{M_2}
\left(\prod_{p\in S}\rho_p\right)
B(\log B)^5+o_S(B(\log B)^5).
\]

Every Stage19 survivor belongs to every local acceptance set. Taking `B->infinity` first and then enlarging `S` gives

\[
\prod_{p\in S}\rho_p\to0
\]

and therefore

\[
\boxed{\frac{N_2(B)}{M_2(B)}\to0.}
\]

This is the certified **mechanism-level explanation** for zero density: infinitely many split-prime valuation-parity constraints on a paired Gaussian-norm squareclass coincidence.

## 4. What the causal mechanism does not yet explain quantitatively

Checkpoint30 also has the stronger theorem

\[
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5},
\]

coming from the Stage14 whole-family numerator bound

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

The fixed half-power is **not** derived from the split-prime squareclass sieve. The local product itself naturally has logarithmic profile

\[
\prod_{\substack{p\le z\\p\equiv1\,(4)}}\rho_p
=(\log z)^{-2+o(1)}.
\]

Thus Stage19 keeps two layers separate:

1. exact arithmetic / causal zero-density mechanism: paired Gaussian-norm squareclass equality plus split-prime parity rejection;
2. strongest certified fixed-power ceiling: Stage14 global graph / elliptic-fiber / complete-host upper-bound machinery.

They are compatible, but they are not multiplied together and the half-power is not declared intrinsic.

## 5. Numerical weapon: diagnostic consistency only

The Stage14 numerical observatory is directly reusable after selecting the exactly-two face mask and using `d=R`.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

The exact finite census reaches

\[
N_2(500{,}000{,}000)=3495,
\qquad
(N_a,N_b,N_c)=(1374,1371,750).
\]

The sample-size gate is passed, but the predeclared stability gate for `N_2(B)/sqrt(B)` remains FAIL. This is consistent with refusing to identify `1/2` as the true exponent. It neither proves the local mechanism nor supplies a lower-bound theorem.

The finite `T=0` record remains unrelated to any perfect-cuboid nonexistence claim.

## 6. Lower-bound OPEN_GATE is not reopened

Checkpoint50 is already `OPEN_GATE_AUDITED_PASS` for

```text
UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19
```

No new theorem or construction input appears at checkpoint60. The causal decomposition therefore does not re-run that route. In particular it still does not prove

\[
N_2(B)\to\infty,
\qquad
N_2(B)\gg B^\delta,
\qquad
N_2(B)\asymp B^{1/2}.
\]

## 7. Stage24 boundary

Stage19 can identify the exact new predicate and a same-measure zero-density mechanism. It does **not** decide whether the quantitative cost of imposing the space diagonal after two faces is integral is independent of, correlated with, or interaction-dependent on the already imposed face conditions.

That comparative classification belongs to Stage24, where Stage18 is the matched source population and other control/transition lanes can be used. No probabilistic independence claim is made here.

## 8. Causal verdict

At current certified resolution:

- source structure before Stage19: two Pythagorean faces sharing one edge;
- exact new Stage19 predicate: paired Gaussian-norm squareclass coincidence;
- local causal thinning: split primes `p=1 mod 4` impose valuation-parity acceptance with loss `4/p+O(p^-2)`;
- consequence: same-measure survivor density tends to zero;
- fixed `B^(1/2+o(1))` ceiling: certified globally but not attributed to the local squareclass sieve;
- lower-bound / true-exponent question: remains the audited checkpoint50 OPEN_GATE;
- independence / interaction classification: reserved for Stage24;
- no perfect-cuboid conclusion.

```text
EVIDENCE_LEVEL=PROVED
CHECKPOINT=60
SOURCE_STRUCTURE=DOUBLE_PYTHAGOREAN_FACES_SHARING_ONE_EDGE
NEW_ARITHMETIC_MECHANISM=PAIRED_GAUSSIAN_NORM_SQUARECLASS_COINCIDENCE
EXACT_SURVIVOR_CONDITION=sf(A)=sf(B)
LOCAL_ZERO_DENSITY_MECHANISM=SPLIT_PRIME_VALUATION_PARITY_SIEVE
LOCAL_ACCEPTANCE_LOSS=1-rho_p=4/p+O(p^-2) for good p=1 mod 4
CAUSAL_ZERO_DENSITY_PROVED=true
FIXED_POWER_UPPER_BOUND=N_2(B)<<_epsilon B^(1/2+epsilon)
FIXED_POWER_SOURCE=Stage14 global whole-family theorem
LOCAL_SIEVE_PAYS_HALF_POWER=false
HALF_POWER_INTRINSIC=UNRESOLVED
INDEPENDENT_OF_PRIOR_CONDITIONS=UNRESOLVED_DEFER_STAGE24
DOUBLE_CHARGE_CHECK=PASS
LOWER_OPEN_GATE_REOPENED=false
OPEN_GATE_REENTRY_JUSTIFIED=NO
PERFECT_CUBOID_CONCLUSION=NONE
DEPENDS_ON=Stage18-60,Stage15-4,Stage15-6,Stage19-30,Stage19-40,Stage19-50,AR-040
FINITE_DATA_USED_AS_PROOF=false
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=70
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint60 is a synthesis of audited exact interfaces; no bounded implementation or external theorem search is required.
```