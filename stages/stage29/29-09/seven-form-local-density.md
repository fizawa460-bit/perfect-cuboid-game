# Stage29-09 — exact seven-linear-form local density at odd primes

```text
ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
RECEIVER=R29-KUM-LOC1
STATUS=SUBMISSION_PENDING_AUDIT
BASE=P2
BRANCH_DIVISOR=xyz(x+y)(x+z)(y+z)(x+y+z)=0
ODD_PRIMES=EXACT
P2_BAD_PRIME=SEPARATE_RECEIVER
```

Write

\[
L=(x,y,z,x+y,x+z,y+z,x+y+z).
\]

For an odd prime `p`, let `chi` be the quadratic character of `F_p`, with `chi(0)=0`, and put

\[
\epsilon=\chi(-1),\qquad \eta=\chi(2),\qquad \theta=\chi(-2)=\epsilon\eta.
\]

A reduction point of `P^2(F_p)` is called **eligible** when all nonzero members of `L` have one common quadratic character. If exactly `k` branch lines vanish there, let `A_k(p)` be the number of eligible points. The seven-line incidence has only `k=0,1,2,3` for odd `p`.

## 1. Exact branch-stratum counts

The off-branch host has the already-audited size

\[
\#(P^2\setminus D)(F_p)=(p-3)^2.
\]

Let

\[
E:y^2=x^3-x,
\qquad a_E(p)=p+1-\#E(F_p).
\]

Direct character sums on the seven branch lines give

\[
\boxed{
A_1(p)=
\frac34(p-4-\epsilon)
+\frac{1+\epsilon}{8}(p-5)
+\frac{3(1+\epsilon)}{16}(p-11-4\eta-a_E(p)).
}
\]

The three terms are respectively the three coordinate lines, the line `x+y+z=0`, and the three pair-sum lines. On a pair-sum line the simultaneous square condition is the degree-eight Kummer curve whose genus-one quotient is exactly `E:y^2=x^3-x`; this is why `a_E(p)` occurs.

At the three ordinary double points,

\[
\boxed{A_2(p)=\frac34(1+\epsilon)(1+\eta).}
\]

Thus all three double points are eligible exactly for `p=1 mod 8`.

At the six triple points,

\[
\boxed{A_3(p)=\frac32(3+\epsilon).}
\]

The three coordinate triple points are always eligible; the other three are eligible exactly when `-1` is a square.

## 2. Exact off-branch count from the endpoint Frobenius package

At an eligible reduction point with `k` vanishing branch values, the normal sign cover has exactly

```text
k=0 : 64 F_p-points in the fiber
k=1 : 32
k=2 : 16
k=3 : 8
```

and an ineligible point has no `F_p`-point in the fiber. Therefore

\[
\boxed{
\#\bar S(F_p)=64A_0(p)+32A_1(p)+16A_2(p)+8A_3(p).
}
\]

Reuse the audited Stage29-02e endpoint Frobenius identity

\[
\#\bar S(F_p)=1+p^2+3a_p(h_{16})+a_p(h_{32})+3a_p(h_8)
+p(10+2\epsilon+\theta+3\eta).
\]

Substitution gives the exact closed formula

\[
\boxed{
\begin{aligned}
64A_0(p)= {}&p^2+p(-24-8\epsilon+3\eta+\epsilon\eta)\\
&+(135+86\epsilon+12\eta+12\epsilon\eta)\\
&+3a_p(h_{16})+a_p(h_{32})+3a_p(h_8)\\
&+6(1+\epsilon)a_E(p).
\end{aligned}}
\]

This is the exact seven-form common-squareclass count on the nonbranch finite-field host. It is not a heuristic `1/64` independence model.

By Deligne for the weight-three newforms and Hasse for `E`,

\[
A_0(p)=\frac{p^2}{64}+O(p),
\qquad
\frac{A_0(p)}{(p-3)^2}=\frac1{64}+O(1/p).
\]

The `1/64` is therefore the leading local geometric density on this `P^2` host, not a physical population survival factor.

## 3. Exact regression

`local_density_check.py` independently enumerates `P^2(F_p)`, classifies the branch depth, tests the common character condition, evaluates the elliptic trace directly, and verifies the formulas for all odd primes below 100 by default.

The check also reconstructs the normal endpoint point count from the exact fiber sizes. No floating arithmetic is used.

## 4. Deduplication against Stage19/20

The Stage19 same-measure space-diagonal law on the matched two-face host has, at good split primes,

\[
1-\rho_p=4/p+O(p^{-2}),
\]

while Stage20's third-face blocker on its matched two-face toric host has

\[
\delta_p=2/p+O(p^{-2}).
\]

Those are conditional laws on already-selected physical/two-face hosts. The present `A_0/(p-3)^2` law is on the full seven-line `P^2` base and is therefore a different measure. It must **not** be multiplied by the Stage19/20 savings as an independent factor.

```text
SAME_PREDICATE_DIFFERENT_COORDINATES_IS_NEW_SAVING=false
STAGE19_STAGE20_LOCAL_LAWS_RECREDITED=false
PHYSICAL_HEIGHT_MEASURE_ADAPTER_REQUIRED_FOR_GLOBAL_SIEVE=true
LOCAL_DENSITY_IS_GLOBAL_NONEXISTENCE=false
```

## 5. Receiver state

```text
R29-KUM-LOC1-ODD=DISCHARGED_CANDIDATE_EXACT_FINITE_FIELD_FORMULA
R29-KUM-LOC1=PARTIAL_DISCHARGE_ODD_PRIMES_EXACT_BAD_PRIME_2_SEPARATE
ATTACK_CREDIT=false
AUDIT_REQUIRED=true
```
