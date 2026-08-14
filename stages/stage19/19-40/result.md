# Stage19-40 — upper-bound ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## 1. Strongest certified whole-family upper bound

Because Stage19 is literally the Stage14/15 physical exactly-two population with integral space diagonal and the exact cutoff adapter `d=R`, the strongest frozen whole-family ceiling transfers without modification:

\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}
\]

for every `epsilon>0`. Equivalently,

\[
\boxed{N_2(B)\ll B^{1/2+o(1)}}.
\]

This bound ranges over the complete primitive canonical Stage19 family. It is not a fixed-direction, fixed-fiber, or averaged statement.

## 2. What pays for the half-power

The half-power is inherited from the frozen Stage14 whole-family theorem. Its proof chain is a global counting mechanism, not the Stage15 local squareclass sieve. In compressed form:

1. exact two-face gluing gives a raw pair graph with `N_2(B)<=E(B)`;
2. every active face has uniformly only `B^{o(1)}` bounded-height neighbors on the associated elliptic fiber;
3. complete balanced-packet reductions and host/reconstruction bounds cover every physical chamber;
4. the resulting whole-family exponent is `1/2`, with only `B^{o(1)}` losses.

Thus the ledger assigns the fixed-power saving to the **Stage14 global graph / elliptic-fiber / complete-host proof chain**.

The Stage15 Gaussian-squareclass mechanism proves zero density independently but does not pay for this fixed half-power ceiling.

## 3. Sharpness status

The bound is currently one-sided. Stage14 explicitly did not prove

\[
N_2(B)\asymp B^{1/2}
\]

or any matching lower bound. It also did not prove a strict improvement

\[
N_2(B)\ll B^{1/2-\delta}
\]

for a fixed `delta>0`.

Therefore checkpoint40 records the strongest certified upper ledger but **does not classify exponent `1/2` as intrinsic or sharp**. That question remains one of the central Stage19 tasks and must be resolved, if possible, by checkpoint50/60/70 or else closed as an explicit open gate.

## 4. Relation to checkpoint30

Combining this ceiling with the frozen Stage18 denominator

\[
M_2(B)\sim C_{M_2}B(\log B)^5
\]

gives exactly the Stage19-30 quantitative survival ceiling

\[
\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

No extra saving is double charged.

## 5. Non-claims

- no matching lower bound;
- no `N_2(B)~C sqrt(B)` asymptotic;
- no proof that `1/2` is the true exponent;
- no strict sub-square-root theorem;
- no claim that Stage15 local parity filters yield the half-power;
- no perfect-cuboid conclusion.

```text
EVIDENCE_LEVEL=PROVED
UPPER_BOUND=N_2(B) <<_epsilon B^(1/2+epsilon)
EQUIVALENT_FORM=N_2(B) << B^(1/2+o(1))
BOUND_SOURCE=Stage14 whole-family theorem
PAYING_MECHANISM=global pair graph + uniform elliptic-fiber multiplicity + complete balanced-host reconstruction
STAGE15_LOCAL_SIEVE_PAYS_HALF_POWER=false
MATCHING_LOWER_BOUND=false
HALF_POWER_SHARP=false
HALF_POWER_INTRINSIC=UNRESOLVED
STRICT_SUB_SQRT_BOUND=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=50
CODEX_REQUIRED=false
```
