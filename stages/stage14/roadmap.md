# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

The three canonical directions are indexed by their shared edge:

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Priority: required

```text
14-1a  lock ambient object, exactly-two categories, raw-pair/triple ledger   [complete]
14-1b  connect to the historical pair-overlap notation and checksums         [complete]
14-1c  lock enumeration/output specification                                [complete]
```

Locked ambient population:

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

### Stage13-review isolation

Stage13 is under independent proof review. Any inherited Stage13 asymptotic statement, including the previously recorded ceiling

\[
N_2(B)=o(B(\log B)^3),
\]

is **not used as an input to current Stage14 work while that review is unresolved**. Stage14-2 and Stage14-3 proceed from direct exact enumeration only. Stage14-4 is planned to attack the growth scale independently rather than rely on the inherited ceiling.

The historical finite rows remain useful only because Stage14-2a independently reproduced them exactly with a standalone enumerator.

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Priority: required

Required outputs:

```text
O_ab_ac, O_ab_bc, O_ac_bc
T
N_a^(2), N_b^(2), N_c^(2)
N_2
normalized directional diagnostics
candidate/dedup diagnostics
validation flags and any triple witnesses
```

### 14-2a — standalone historical reproduction

Status: [x] Complete.

A standalone Stage14 implementation was added at

```text
stages/stage14/scripts/14-2/two_face_census.py
```

It imports no Stage13 counting code. All seven historical finite rows reproduce exactly:

```text
B=1,000      (N_a,N_b,N_c)=(2,0,0)      N2=2   T=0
B=2,000      (N_a,N_b,N_c)=(2,2,1)      N2=5   T=0
B=5,000      (N_a,N_b,N_c)=(6,6,3)      N2=15  T=0
B=10,000     (N_a,N_b,N_c)=(9,11,5)     N2=25  T=0
B=20,000     (N_a,N_b,N_c)=(16,16,10)   N2=42  T=0
B=50,000     (N_a,N_b,N_c)=(24,24,14)   N2=62  T=0
B=100,000    (N_a,N_b,N_c)=(33,33,23)   N2=89  T=0
```

Result:

```text
stages/stage14/data/14-2/historical_reproduction_report.json
```

### 14-2b — verified extension above B=100000

Status: [x] Complete.

The standalone Stage14 enumerator reaches the full preferred ladder:

```text
B=200,000      (42,50,24)    N2=116   T=0
B=500,000      (70,78,40)    N2=188   T=0
B=1,000,000    (98,101,56)   N2=255   T=0
B=2,000,000    (142,134,80)  N2=356   T=0
```

c-normalized exactly-two ratios:

```text
200k   1.7500 : 2.083333 : 1
500k   1.7500 : 1.950000 : 1
1m     1.7500 : 1.803571 : 1
2m     1.7750 : 1.675000 : 1
```

The finite leader is `b` through `B=1m`, then `a` at `B=2m`. This reversal is a finite diagnostic and forbids assuming monotone directional convergence without further evidence.

No triple object is found through `B=2m`; this is a finite search result only.

Results:

```text
stages/stage14/data/14-2/extended_census_report.json
stages/stage14/archive/stage14-2b-extended-census.md
```

No Stage13 analytic result was used to obtain these rows.

### 14-2c — finite-census closure / audit

Status: [>] Next.

Close Stage14-2 before ratio analysis by checking:

1. historical reproduction remains exact;
2. the four extended rows satisfy all pair/triple/exactly-two identities;
3. the implementation/output metadata are internally consistent;
4. the Stage14 canonical summary is synchronized through `B=2m`;
5. Stage13 analytic dependencies are explicitly quarantined while external review is unresolved;
6. no asymptotic or monotonicity statement has leaked into the finite census layer.

After this audit, freeze the finite table and move to Stage14-3.

## 14-3 — Finite directional-ratio evolution

Priority: required

Study

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and normalized proportions over the audited cutoff range. In particular, account for the observed finite leader reversal rather than presupposing monotone convergence.

Status: not started.

## 14-4 — True total growth order

Priority: major analytic task

Determine the correct asymptotic order of

\[
N_2(B).
\]

Current policy: proceed independently of unresolved Stage13 analytic claims. Any repaired Stage13 bound may later be used only as a cross-check after its review status is settled.

Fine-grained substages for this task may begin at `14-4aa`.

Status: not started.

## 14-5 — Directionwise asymptotic structure

Priority: major analytic task

After the total scale is understood, determine whether

\[
N_a^{(2)},\quad N_b^{(2)},\quad N_c^{(2)}
\]

share the same exponent/logarithmic scale, whether direction constants exist, and what geometric/arithmetic mechanism controls their ratios.

A later comparison with the face-diagonal-first / Euler-side two-face layer is natural, but equality of the two directional laws is not assumed.

Fine-grained substages for this task may begin at `14-5aa`.

Status: not started.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. The triple population `T(B)` is retained explicitly and removed from each raw pair count when forming the exactly-two populations.

The fact that all currently verified rows through `B=2,000,000` have `T=0` is only a finite observation. No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is independently established.
