# Stage14-e2 — finite ambient reconnaissance + literature refresh

> STATUS: `STAGE14_E2_COMPLETE_FINITE_AMBIENT_RECONNAISSANCE`
>
> TRACK: front-side two-face ambient control population
>
> INPUT: Stage14-e1 definition/bijection and its edge-first = face-pair-first lock through `B=2000`
>
> SPACE-DIAGONAL RULE: `D_R` is a real Euclidean height only; no rational/integer condition

## 1. Purpose

Stage14-e1 established the exact ambient object

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,
\qquad \gcd(e,x,y)=1,\qquad x<y,
\]

with real height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B.
\]

The exactly-two ambient population further requires

\[
x^2+y^2\ne\square.
\]

Stage14-e2 has two tasks:

1. push the finite census far beyond the e1 bijection audit;
2. refresh the literature collision search before any growth interpretation is promoted.

No asymptotic theorem is claimed in this stage.

## 2. Large finite census

For the large cutoffs e2 uses the edge-first Pythagorean-neighbor enumerator. This is legitimate because e1 already independently proved and audited equality with the oriented-face-pair parameterization through `B=2000`; e2 is reconnaissance rather than a new bijection proof.

The exact census is:

| `B` | `E_a` | `E_b` | `E_c` | `E_2` | raw ambient | Euler-brick objects |
|---:|---:|---:|---:|---:|---:|---:|
| 2,000 | 1,342 | 2,136 | 1,334 | 4,812 | 4,833 | 7 |
| 10,000 | 12,464 | 18,198 | 11,004 | 41,666 | 41,720 | 18 |
| 50,000 | 103,892 | 142,403 | 85,436 | 331,731 | 331,857 | 42 |
| 200,000 | 612,678 | 805,875 | 477,952 | 1,896,505 | 1,896,751 | 82 |
| 1,000,000 | 4,592,536 | 5,816,786 | 3,408,403 | 13,817,725 | 13,818,382 | 219 |

Every all-three-face Euler brick contributes three raw shared-edge incidences, so

\[
E_{\rm raw}(B)-E_2(B)=3\,\#\{\text{primitive Euler bricks with }D_{\mathbf R}\le B\}.
\]

At `B=1,000,000` this is

\[
13{,}818{,}382-13{,}817{,}725=657=3\cdot219.
\]

Thus the third-face-square filter is already extremely sparse inside the two-face ambient family at this scale.

## 3. Independent external subpopulation cross-check

The e2 code also changes cutoff convention deliberately and counts primitive Euler bricks with

\[
a<b<c<X,
\]

which is the convention of OEIS A239618. It reproduces

```text
X = 10^3   -> 5
X = 10^4   -> 19
X = 10^5   -> 65
```

exactly.

This is not evidence for the Stage14-e asymptotic because the height is different. It is an external computational cross-check of the all-three-face subpopulation and of the square-testing logic.

## 4. Finite growth diagnostics

The raw values of `E_2/B` increase strongly:

```text
B=2,000       2.406
B=10,000      4.1666
B=50,000      6.63462
B=200,000     9.482525
B=1,000,000  13.817725
```

The normalizations by `B log B` and `B(log B)^2` also drift substantially upward over this interval. By contrast,

\[
R_3(B):=\frac{E_2(B)}{B(\log B)^3}
\]

is

```text
B=2,000       0.005478985421608477
B=10,000      0.005332793530354440
B=50,000      0.005237945426592706
B=200,000     0.005214301572383136
B=1,000,000   0.005240053581957176
```

This is strikingly stable finite behavior. Therefore

\[
\boxed{B(\log B)^3}
\]

is promoted only to a **high-priority e3 candidate scale**.

Stage14-e2 does **not** claim

\[
E_2(B)\sim C B(\log B)^3.
\]

The purpose of e3 is precisely to determine whether this finite stability has a structural explanation or is transient.

## 5. Directional finite geography

At `B=1,000,000`,

\[
\frac{(E_a,E_b,E_c)}{E_2}
\approx
(0.3323655667,\ 0.4209655352,\ 0.2466688981).
\]

Across the audited range:

- the `b` chamber remains the largest;
- the `a` share increases;
- the `c` share decreases;
- no limiting vector is inferred.

This is deliberately kept separate from Stage14-5 and from any future e4 directional theorem.

## 6. Third-face-square thinning

The raw-incidence fraction removed by the third-face-square condition is

\[
\frac{E_{\rm raw}(B)-E_2(B)}{E_{\rm raw}(B)}.
\]

It falls from about

```text
4.35e-3 at B=2,000
```

to

```text
4.75e-5 at B=1,000,000.
```

This is a useful empirical separation:

```text
two shared-edge Pythagorean faces     abundant
third face also Pythagorean           very sparse inside that ambient family
integer space diagonal                an additional main-Stage14 filter beyond e-track
```

No thinning exponent is claimed.

## 7. Literature refresh — what is already known

The detailed classification is in `14-e2/literature-refresh.md`.

The main conclusions are:

```text
Leech 1977                 ADJACENT_RESULT + REUSABLE_METHOD
van Luijk 2000             ADJACENT_RESULT + REUSABLE_METHOD
Ramsden–Sharipov 2012      ADJACENT_RESULT + REUSABLE_METHOD
Meskhishvili 2012/2015     ADJACENT_RESULT (especially close to main Stage14)
Rathbun tables / OEIS       ADJACENT_RESULT + COMPUTATIONAL CROSSCHECK
De Grey–Gibbs–Helm 2024    ADJACENT_RESULT + REUSABLE_METHOD
Himane 2024                ADJACENT_RESULT
Peschmann 2026 trilogy      ADJACENT_RESULT + REUSABLE_METHOD
```

The important boundary is that Euler bricks themselves are extensively parametrized, searched and tabulated. In particular recent 2026 work uses two coprime Pythagorean pairs, quartics and elliptic fibrations and reports more than one million Master-Hits. The e-track must not rediscover that machinery under new names.

What this refreshed search did **not** locate is a theorem counting the larger primitive two-face ambient population by

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}
\]

with or without shared-edge chamber separation.

The correct status is therefore

```text
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

—not a novelty certificate.

## 8. Decision for e3

The e3 task is now sharpened.

Before attempting the candidate `B(log B)^3` law, e3 must search specifically for existing results on:

1. simultaneous Pythagorean pairs sharing one leg;
2. rational Pythagorean slopes with lcm/shared-denominator height;
3. lcm-weighted Euclid-parameter sums;
4. height zeta functions / rational-point counts on the associated arithmetic variety;
5. any Manin-type or toric interpretation that would predict a `B(log B)^k` law.

Only after that collision audit should e3 build the analytic count.

```text
STAGE14_E2=COMPLETE_FINITE_AMBIENT_RECONNAISSANCE
MAX_RECON_B=1000000
OEIS_A239618_CROSSCHECK_PASS=true
B_LOG3_FINITE_CANDIDATE_PRIORITY=HIGH
ASYMPTOTIC_CLAIM_MADE=false
DIRECTIONAL_LIMIT_CLAIM_MADE=false
LITERATURE_REFRESH_RECORDED=true
NEXT_E_TASK=Stage14-e3 total ambient growth with literature-first asymptotic collision audit
```
