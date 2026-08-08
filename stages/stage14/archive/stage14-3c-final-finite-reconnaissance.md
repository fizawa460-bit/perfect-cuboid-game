# Stage14-3c — final finite reconnaissance synthesis

## Purpose

Stage14-3c closes the currently allowed Stage14 work. It does not fit an asymptotic model and does not import any Stage13 analytic theorem. Its role is to separate verified finite facts from sampling artifacts and from questions that must remain open until the one-face proof review provides a trustworthy proof-level map.

## Verified finite base

The ambient convention remains

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

Stage14-2 used two materially different exact generation routes. They agree on all 11 audited cutoffs through `B=2,000,000`.

At the verified ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

No triple object is found through this finite ceiling. This is not a proof that perfect cuboids do not exist.

## What Stage14-3 learned

Stage14-3a showed that coarse directional samples move enough to make naive extrapolation unsafe. Stage14-3b then replaced the sparse late grid by a 50,000-step grid from `100k` to `2m`, together with the exact exactly-two event stream near the `a/b` crossing.

The apparent coarse equality

\[
N_a^{(2)}/N_c^{(2)}=7/4
\]

at `200k`, `500k`, and `1m` is not stable under densification. Between those points the ratio moves substantially. The repeated coarse equality is therefore recorded as a sparse-grid finite artifact, not as an invariant or limiting value.

The cumulative `a/b` crossing is localized exactly after `1m`:

```text
d=1,083,121   a-b: -1 ->  0
d=1,096,685   a-b:  0 -> -1
d=1,127,185   a-b: -1 ->  0
d=1,148,545   a-b:  0 -> +1
```

Immediately after the final crossing,

```text
(N_a,N_b,N_c)=(107,106,60).
```

From `d=1,148,545` through `B=2,000,000`, every subsequent exactly-two event state keeps `a>b`. This is only a finite-range persistence statement; eventual or asymptotic `a` dominance is not inferred.

## Robust finite conclusions

The following are retained as the final finite reconnaissance facts.

1. The finite exactly-two census is independently cross-checked through `B=2,000,000` at the locked audited cutoffs.
2. The dense `100k..2m` directional trajectory is not monotone in any simple sense.
3. The sampled `a/c=7/4` pattern is not stable and is rejected as a finite invariant candidate.
4. The late finite `b -> a` crossing can be localized to the exact event `d=1,148,545`, with finite `a>b` persistence through `2m`.
5. No triple object occurs in the verified range, but no perfect-cuboid nonexistence statement follows.
6. All current Stage14 finite conclusions are independent of Stage13 code and Stage13 asymptotic claims.

## What remains unknown

Stage14-3 does not identify

```text
the growth order of N_2(B)
a limiting directional vector
a monotonicity theorem
an eventual directional leader
an asymptotic meaning for 7/4
an Euler-side two-face equality or inequality
whether T(B) ever becomes positive
```

The finite data are therefore a map of phenomena a later proof must explain, not a substitute for that proof.

## Restart gate

Stage14 now stops deliberately. Stage14-4 and Stage14-5 remain paused until the one-face / Stage13 review identifies which structural tools are genuinely reliable.

When Stage14 resumes, the first analytic substage should not simply import an old Stage13 theorem. A suitable restart is

```text
14-4aa  independent two-face parametrization and proof-input audit
```

with every Stage13 dependency explicitly re-audited before use.

## Decision

```text
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
STAGE14_3C=COMPLETE
STAGE14_3=COMPLETE
FINITE_RECONNAISSANCE_COMPLETE=true
STOP_LINE_ACTIVE=true
ASYMPTOTIC_FIT_PERFORMED=false
FINITE_RATIO_LIMIT_IDENTIFIED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
NEXT=WAIT_FOR_ONE_FACE_REVIEW_BEFORE_STAGE14_4
```
