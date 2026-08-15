# Stage25-50 — deep lower/construction checkpoint

EVIDENCE_LEVEL=PROVED_AUDITED_PASS
CHECKPOINT=50
STATUS=PROVED_AUDITED_PASS
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Main audited result

The entering audited lower was

\[
N_2(B)\gg\sqrt{\log B}.
\]

Deep sublane `Stage25-r501` uses Meskhishvili's first one-rational-parameter nearly-perfect-cuboid family, homogenizes it into the exact primitive/canonical Stage19 population, and counts reduced rational parameters by height.

Hostile fresh audit accepts

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

Thus Stage19 now has a certified positive-power lower bound. Together with the audited whole-family upper,

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

No matching half-power lower or true exponent is claimed.

## 2. Stage25 endpoint ratio

The audited Stage21 source interface is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Therefore

\[
\boxed{
\frac{N_2(B)}{M_1(B)}
\gg B^{-7/4}(\log B)^{-1}.
}
\]

Together with the audited checkpoint40 upper,

\[
\boxed{
B^{-7/4}(\log B)^{-1}
\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
}
\]

The ratio still tends to zero while the target grows by a positive power.

## 3. Construction mechanism

For coprime positive `m,n`, define

\[
A=16m^2n^2(m^4-9n^4),
\]
\[
B=(m^4-10m^2n^2+9n^4)(m^4+2m^2n^2+9n^4),
\]
\[
C=4mn(m^2+3n^2)(m^4-10m^2n^2+9n^4),
\]

with integer diagonals

\[
D_{AC}=4mn(m^2+3n^2)(m^4-2m^2n^2+9n^4),
\]
\[
D_{BC}=(m^4-n^4)(m^4-81n^4),
\]
\[
D=m^8+46m^4n^4+81n^8.
\]

Exact identities are

\[
A^2+C^2=D_{AC}^2,
\quad B^2+C^2=D_{BC}^2,
\quad A^2+B^2+C^2=D^2.
\]

On

\[
7/2<m/n<4
\]

we have `0<B<C<A`. After primitive reduction by `g=gcd(A,B,C)`,

\[
(a,b,c)=(B/g,C/g,A/g).
\]

The two guaranteed canonical integral faces are therefore `ab` and `bc`, sharing edge `b`.

Primitive reduction preserves the required diagonals because `g` divides `DAC`, `DBC`, and `D` prime-by-prime.

## 4. Exactly-two mask

The remaining raw face satisfies

\[
A^2+B^2=n^{16}P(m/n),
\]

where

\[
P(t)=t^{16}-16t^{14}+316t^{12}-112t^{10}-3290t^8
-1008t^6+25596t^4-11664t^2+6561.
\]

Modulo 5 this is `P(t)=Q(t^2)` with

\[
Q(u)=u^8+4u^7+u^6+3u^5+2u^3+u^2+u+1.
\]

The hostile-audit hardening derives `Q` mechanically from the submitted `P` coefficients and verifies the committed Bezout certificate `gcd(Q,Q')=1`. Since `Q(0)=1`, this proves `P` squarefree mod 5 and hence over `Q`.

Thus

\[
w^2=P(t)
\]

has smooth projective genus 7. By Faltings, only finitely many rational `t` make the third face rational. Removing those finitely many parameters leaves exactly-two Stage19 objects.

Primitive reduction creates no new missing-face squares: the primitive missing face is square iff the raw missing face is square.

## 5. Counting and bounded multiplicity

Choose

\[
m=4n-k,\qquad 1\le k<n/2,\qquad (k,n)=1.
\]

For `n>2`, exactly `phi(n)/2` reduced residue classes lie below `n/2`. Taking `n<=floor(T/4)` therefore gives `gg T^2` reduced rational parameters with `m,n<=T` in the physical cone.

The space diagonal obeys

\[
D\le128T^8,
\]

and primitive reduction only decreases height.

The similarity invariant

\[
A/D=\frac{16t^2(t^4-9)}{t^8+46t^4+81}
\]

has fibers of size at most 8 because fixing its value gives a nonzero polynomial equation of degree at most 8 in `t`.

Hence

\[
N_2(B)\gg T^2\gg B^{1/4}.
\]

Full proof ledger: `r501-parametric-positive-power.md`.
Fresh hostile audit: `audit.md`.

## 6. Cross-stage backflow

The accepted numerator lower gives

\[
\boxed{N_2/M_2\gg B^{-3/4}(\log B)^{-5}},
\]

and

\[
\boxed{N_2/N_1\gg B^{-3/4}(\log B)^{-3}}.
\]

Since the ambient Stage16S space baseline satisfies `S0~B^-1`,

\[
\boxed{J_2\gg B^{1/4}(\log B)^{-5}\to\infty}.
\]

Thus Stage24's previously unresolved global interaction sign is now positive/divergent.

Since `S1=N1/M1~B^-1(log B)^2`,

\[
\boxed{I=(N_2/M_2)/(N_1/M_1)\gg B^{1/4}(\log B)^{-7}\to\infty}.
\]

Thus the previously unresolved second-order interaction sign is also positive/divergent.

Backflow records:

- `stages/stage19/post-stage25-50-supersession.md`;
- `stages/stage23/post-stage25-r01/result.md`;
- `stages/stage24/post-stage25-r01/result.md`.

## 7. New directional/channel deduction from hostile audit

Because canonical `(a,b,c)=(B/g,C/g,A/g)` and the guaranteed faces are `ab` and `bc`, the same counted family gives

\[
\boxed{N_{2,b}(B)\gg B^{1/4}},
\]

and the corresponding Stage17 raw pair-overlap channel satisfies

\[
\boxed{A_{ab,bc}(B)\gg B^{1/4}}.
\]

This is distinct from the earlier C17 shared-`c` lower.

Checkpoint30's missing source-channel denominator adapter remains open, so no Stage25 directional endpoint ratio is claimed.

## 8. Deep-search lane status

```text
LOWER_LANE_A=Meskhishvili_first_parametrization_positive_power:AUDITED_BREAKTHROUGH
LOWER_LANE_B=Meskhishvili_third_parametrization_same_degree8:IDENTIFIED_NO_EXPONENT_GAIN_YET
LOWER_LANE_C=Meskhishvili_second_parametrization_degree12:WEAKER_HEIGHT_EXPONENT
LOWER_LANE_D=Yoshida_face_cuboid_elliptic_surface:OPEN_FOR_POSSIBLE_HIGHER_DIMENSION_COUNT
LOWER_LANE_E=Stage24_symmetric_multiplier_k_family:OPEN_FOR_RANK_UNIFORMITY_OR_MULTI_K_AGGREGATION
LOWER_LANE_F=common_squarefree_core_slices:OPEN_NO_NEW_GLOBAL_COUNT_YET
```

The deeper lanes remain live for later work; they are not stacked into checkpoint50's certified theorem.

## 9. Numerical/reuse and literature boundaries

No census extension is used.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY_FOR_NEW_PARAMETRIC_FAMILY
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_EXACT_IDENTITY_AND_SQUAREFREE_CERTIFICATE_ONLY
FINITE_DATA_USED_AS_PROOF=false
```

Meskhishvili 2015 supplies formula provenance only; the Stage19 primitive/canonical/exactly-two/counting adapter is proved in-repo. No mathematical novelty claim is made for rational face-cuboid parametrization itself.

## 10. Exit

```text
DISCOVERY_CHECKPOINT=Stage25-50
DEEP_RESEARCH_MODE=true
HOSTILE_AUDIT=PASS
C17_LOWER_REUSED=true
OLD_LOWER=N2(B)>>sqrt(log B)
NEW_LOWER=N2(B)>>B^(1/4)
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_EXPONENT=1/4
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
STAGE25_RATIO_LOWER=B^(-7/4)(log B)^(-1)
STAGE24_RATIO_LOWER_BACKFLOW=B^(-3/4)(log B)^(-5)
STAGE23_RATIO_LOWER_BACKFLOW=B^(-3/4)(log B)^(-3)
AMBIENT_INTERACTION_SIGN=POSITIVE_DIVERGENT
CROSS_RATIO_SIGN=POSITIVE_DIVERGENT
N2_B_DIRECTION_LOWER=N2,b(B)>>B^(1/4)
A_AB_BC_OVERLAP_LOWER=A_ab,bc(B)>>B^(1/4)
STAGE25_DIRECTIONAL_RATIO_PROVED=false
HISTORY_SUPERSESSION_BACKFLOW_EXECUTED=true
FORMULA_SUBSTITUTION_ONLY=false
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
AUDIT_REQUIRED=false
AUDIT_STATUS=PASS
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEXT_EXPECTED_COMMAND=merge PR #984; then Stage25-main-batch
CODEX_REQUIRED=false
```
