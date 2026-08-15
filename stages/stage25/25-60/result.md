# Stage25-60 — causal decomposition after the positive-power breakthrough

EVIDENCE_LEVEL=PROVED_FROM_AUDITED_INTERFACES_PLUS_NEW_R507
CHECKPOINT=60
STATUS=PROVED_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Entering audited theorem

Checkpoint50 established

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

Therefore the Stage25 endpoint ratio is currently

\[
\boxed{
B^{-7/4}(\log B)^{-1}
\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
}
\]

Checkpoint60 asks what this means causally, whether the two legal paths agree without double charging, and whether the remaining lower lanes can already improve the exponent `1/4`.

## 2. Exact two-path causal decomposition

Put

\[
F=M_2/M_1,\quad S=N_1/M_1,\quad A=N_2/M_2,\quad T=N_2/N_1.
\]

The legal path identities are

\[
N_2/M_1=F A=S T.
\]

Define

\[
I=\frac{A}{S}=\frac{T}{F}=\frac{N_2M_1}{M_2N_1}.
\]

Then the formerly-invalid naive product receives an exact interaction correction:

\[
\boxed{N_2/M_1=F S I.}
\]

Since

\[
F\asymp B^{-1}(\log B)^4,\qquad
S\asymp B^{-1}(\log B)^2,
\]

and checkpoint50 gives

\[
A\gg B^{-3/4}(\log B)^{-5},\qquad
T\gg B^{-3/4}(\log B)^{-3},
\]

we get

\[
\boxed{I(B)\gg B^{1/4}(\log B)^{-7}\to\infty.}
\]

The matching inherited upper is

\[
I(B)\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7}.
\]

Thus the second-face and space-diagonal requirements have a rigorously **positive divergent population-ratio interaction**. The combined population is asymptotically much larger than the raw product `F*S`; `I` is the exact correction factor. No stochastic independence claim is made.

## 3. Ambient-control hierarchy

Stage16S gives the ambient space ratio

\[
S_0\asymp B^{-1}.
\]

Stage21 gives

\[
J_1=\frac{S}{S_0}\asymp(\log B)^2.
\]

Stage24 after checkpoint50 gives

\[
J_2=\frac{A}{S_0}
\gg B^{1/4}(\log B)^{-5}\to\infty.
\]

Moreover

\[
\boxed{J_2/J_1=I\to\infty.}
\]

So prior one-face conditioning enhances space integrality only logarithmically, while prior two-face conditioning enhances it by at least a positive polynomial factor divided by logs. The second face changes the interaction class.

```text
AMBIENT_SPACE_COST=B^-1
ONE_FACE_SPACE_INTERACTION=POSITIVE_LOG_SQUARED
TWO_FACE_SPACE_INTERACTION=POSITIVE_DIVERGENT_AT_LEAST_B^1/4_LOG^-5
SECOND_FACE_INCREMENTAL_INTERACTION=POSITIVE_DIVERGENT
```

## 4. Order-of-conditions classification

The same cross-ratio appears in both orders:

\[
\frac{N_2/M_2}{N_1/M_1}=I
\]
compares space integrality after two faces versus after one face, while

\[
\frac{N_2/N_1}{M_2/M_1}=I
\]
compares the second-face ratio after space integrality versus before space integrality.

Hence the order-of-conditions interaction is **symmetric and positive at the exact population cross-ratio level**. This does not mean the strata are literal nested subsets.

## 5. r501 lane saturation: new theorem

Checkpoint60 proves an exact primitive gcd theorem for the checkpoint50 parametric family:

\[
\gcd(A,B,C)=2^{7\epsilon_2}3^{4\epsilon_3}\le10368,
\]
where `epsilon_2=1` iff `m,n` are both odd and `epsilon_3=1` iff `3|m`.

Since raw space height

\[
D=m^8+46m^4n^4+81n^8\ge m^8,
\]
primitive height satisfies

\[
D_{prim}\ge m^8/10368.
\]

Together with the checkpoint50 lower count, this gives the exact internal family order

\[
\boxed{N_{r501}(B)=\Theta(B^{1/4}).}
\]

Thus the audited r501 lane itself is exhausted at exponent `1/4`: hidden gcd cancellation cannot improve it.

## 6. Deeper lower search

All checkpoint50 open lanes were reopened.

- `R502` Meskhishvili third family: same degree-eight mechanism, so no exponent improvement from degree count alone.
- `R503` Yoshida elliptic surface: remains the highest-value route; the `32:1` structural map and infinitely many positive-rank fibers are known, but no uniform bounded-height count over varying fibers is currently certified.
- `R504` symmetric-k aggregation: new structural progress. The degenerate section `(t,z)=(k,1)` is generically non-torsion because its `k=2` specialization is the audited infinite-order point. An explicit `3P` rational section is recorded, but its available height degree is worse than r501 and yields no stronger lower theorem.
- `R505/R506` common-core/common-leg receivers: remain open without a closed dimension/height count.

Therefore

```text
HIGHER_THAN_ONE_QUARTER_SEARCH=EXECUTED
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
BEST_OPEN_ROUTE=R503_YOSHIDA_UNIFORM_VARYING_FIBER_HEIGHT
```

This is a bounded stop: further progress now requires a genuinely new uniform height/count theorem or another higher-dimensional polynomial-height family.

## 7. Double-charge firewall

The following remain forbidden:

- multiplying `F` and `S` and calling the result `N2/M1` without the interaction correction `I`;
- multiplying Path A and Path B estimates;
- reusing Stage21's `(log B)^2` enhancement as an extra factor after it has already entered `S`;
- multiplying Stage24 thin-cover/local-sieve savings onto the half-power upper;
- interpreting `I->infinity` as probabilistic dependence or an objectwise conditional probability.

The legal corrected decomposition is exactly

\[
\boxed{N_2/M_1=(M_2/M_1)(N_1/M_1)I.}
\]

## 8. Exit / audit decision

Checkpoint60 contains two genuinely new theorem-level statements:

1. the exact positive-divergent corrected-product causal decomposition after the quarter-power backflow;
2. the r501 primitive-gcd rigidity and exact family growth `Theta(B^(1/4))`.

It also adds the generic non-torsion symmetric-k section as structural progress. For that reason a fresh audit is required before Stage70 closeout.

```text
TWO_PATH_CAUSAL_DECOMPOSITION=PASS
DOUBLE_CHARGE_AUDIT=PASS
ORDER_OF_CONDITIONS_INTERACTION=POSITIVE_DIVERGENT_SYMMETRIC_CROSS_RATIO
STAGE16S_STAGE21_STAGE22_STAGE23_STAGE24_COMPARISON=PASS
R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R504_GENERIC_NONTORSION_SECTION_PROVED=true
GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
FORMULA_SUBSTITUTION_ONLY=false
EXPLORATION_EVIDENCE_COMPLETE=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
```
