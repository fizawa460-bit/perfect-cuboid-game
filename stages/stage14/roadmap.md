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
14-1b  connect to the existing pair-overlap notation and inherited checks  [complete]
14-1c  lock enumeration/output specification                               [complete]
```

Locked ambient population:

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Stage14-1 also retains the inherited ceiling

\[
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3),
\]

without treating it as the true two-face growth scale.

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

It imports no Stage13 counting code. It regenerates the population by exact Pythagorean-triple gluing, canonical deduplication by `(a,b,c,d)`, direct space-diagonal verification and exact recomputation of all three face-square flags.

All seven inherited finite rows reproduce exactly:

```text
B=1,000      (N_a,N_b,N_c)=(2,0,0)      N2=2   T=0
B=2,000      (N_a,N_b,N_c)=(2,2,1)      N2=5   T=0
B=5,000      (N_a,N_b,N_c)=(6,6,3)      N2=15  T=0
B=10,000     (N_a,N_b,N_c)=(9,11,5)     N2=25  T=0
B=20,000     (N_a,N_b,N_c)=(16,16,10)   N2=42  T=0
B=50,000     (N_a,N_b,N_c)=(24,24,14)   N2=62  T=0
B=100,000    (N_a,N_b,N_c)=(33,33,23)   N2=89  T=0
```

The historical reproduction gate therefore passes exactly.

Result:

```text
stages/stage14/data/14-2/historical_reproduction_report.json
```

No asymptotic inference is made from these seven rows.

### 14-2b — verified extension above B=100000

Status: [>] Next.

Use the locked Stage14 census to extend beyond the inherited ceiling. The first required target is at least one verified cutoff above `B=100000`; preferred ladder:

```text
200000 -> 500000 -> 1000000 -> 2000000
```

as performance allows.

Acceptance conditions for Stage14-2 as a whole remain:

1. historical reproduction gate passes exactly; [done in 14-2a]
2. optimized production path is cross-checked against a logically independent/literal method on feasible small bounds;
3. at least one verified `B>100000` row is produced;
4. all exact row identities pass;
5. any `T>0` witness is retained and independently checked.

## 14-3 — Finite directional-ratio evolution

Priority: required

Study

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and normalized proportions over the audited cutoff range. Test whether the directions share one apparent growth scale or separate already at finite size.

Status: not started.

## 14-4 — True total growth order

Priority: major analytic task

Determine the correct asymptotic order of

\[
N_2(B).
\]

Stage13 supplies only

\[
N_2(B)=o(B(\log B)^3),
\]

so Stage14 must determine the actual scale rather than presuppose one.

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

The fact that all currently verified rows have `T=0` is only a finite observation. No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is proved or numerically diagnosed.
