# Stage14-t26 — complete odd-prime routing via Gaussian allocation and the dual 2-isogeny

## Purpose

Stage14-t25 proved odd local minimality for the rank-branch curve and routed the `3 mod 4` part of the square variables `r,u` into the physical `[-1]` covering variables. The unresolved columns were:

- split primes `ell = 1 mod 4` in `D` and in the square parts `r,u`;
- odd primes in `C`.

Stage14-t26 completes the **local routing problem at every odd prime**. The output is not yet a rank-energy power saving: it says that once a usable large odd prime is present in any of the four moving columns

\[
r,\qquad u,\qquad C,\qquad D,
\]

that prime is forced into one of finitely many explicit covering congruence states. The remaining analytic problem is then large-prime availability / smooth exceptions and the resulting same-partition incidence count.

## 1. Starting point

For a reduced direction `(D,C)` and a primitive physical covering parameter `(p,q)=1`, write

\[
S=p^2+q^2,\qquad T=p^2-q^2,
\]

and let `W` be the integer from the t24/t25 `[-1]` cover:

\[
\boxed{
W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4).
}
\]

The two exact norm identities are

\[
\boxed{W^2+C^2S^2=(2Dpq)^2}
\tag{26.1}
\]

and

\[
\boxed{W^2+C^2T^2=4(D^2-C^2)p^2q^2.}
\tag{26.2}
\]

Recall also

\[
D-C=h\alpha r^2,\qquad D+C=h\beta u^2,
\]

so

\[
D^2-C^2=h^2\alpha\beta r^2u^2.
\]

## 2. The dual curve is a full-rational-2-torsion model

The rank curve is

\[
E: Y^2=X(X^2+aX+C^4),
\qquad a=4D^2-2C^2.
\]

For a model `y^2=x(x^2+a x+b)` with kernel `(0,0)`, the standard 2-isogenous curve is

\[
E': y^2=x(x^2-2ax+(a^2-4b)).
\]

Here

\[
a^2-4C^4=16D^2(D^2-C^2),
\]

and the quadratic factor splits completely. Therefore

\[
\boxed{
E'_{D,C}:\quad y^2=x(x-4D^2)(x-4(D^2-C^2)).
}
\]

Thus the dual side has full rational 2-torsion.

For the physical point, the isogeny has

\[
x'=\frac{Y^2}{X^2}=\left(\frac{W}{pq}\right)^2.
\]

Using (26.1)--(26.2),

\[
\boxed{
x'-4D^2=-\left(\frac{CS}{pq}\right)^2,}
\]

\[
\boxed{
x'-4(D^2-C^2)=-\left(\frac{CT}{pq}\right)^2.}
\]

Hence the complete full-2-torsion descent signature of every physical image is

\[
\boxed{[x',\ x'-4D^2,\ x'-4(D^2-C^2)]=[1,-1,-1].}
\]

This is the dual-descent state that was missing in t25.

## 3. Split-prime Gaussian allocation for the D-column

Let `ell = 1 mod 4` be an odd prime and `e=v_ell(D)`. Let `rho` be a square root of `-1` modulo `ell^{2e}`.

From (26.1), modulo `ell^{2e}`,

\[
(W-\rho CS)(W+\rho CS)\equiv0\pmod{\ell^{2e}}.
\]

There are two cases.

1. `ell | S`. Then the large prime is already routed into the explicit quadratic form `p^2+q^2`.
2. `ell \nmid S`. Since `ell\nmid C`, the two Gaussian linear factors are coprime modulo `ell`; consequently exactly one sign `epsilon in {+1,-1}` satisfies

\[
\boxed{
ell^{2e}\mid W+\epsilon\rho CS.}
\]

Thus every odd prime power in the `D` column is routed either to `S` or to one of two Gaussian congruence states. By t25, all odd primes of `D` are already `1 mod 4`, so this is complete for `D`.

## 4. Complete routing for the r/u columns

Let `ell` be an odd prime dividing `ru`, with `f=v_ell(ru)`.

### 4.1 Inert primes

If `ell = 3 mod 4`, t25 gives the exact valuation forcing

\[
\boxed{\ell^f\mid W,\qquad \ell^f\mid T.}
\]

Hence the prime is routed into exactly one of `p-q` and `p+q` at the `ell`-adic level.

### 4.2 Split primes

If `ell = 1 mod 4`, take a square root `rho^2=-1 mod ell^{2f}`. From (26.2),

\[
(W-\rho CT)(W+\rho CT)\equiv0\pmod{\ell^{2f}}.
\]

Again there are two cases.

1. `ell | T`, which is already an explicit rational divisor condition.
2. `ell \nmid T`. Then exactly one sign satisfies

\[
\boxed{\ell^{2f}\mid W+\epsilon\rho CT.}
\]

The exponent `2f` is the entire moving-square contribution from `r,u`; any additional odd exponent belonging to the fixed kernel `alpha beta` only strengthens the congruence.

Therefore every odd prime in either `r` or `u` is routed into a rational `T` state or one of two Gaussian states.

## 5. The C-column from the dual descent

Factor (26.1) over the integers:

\[
\boxed{
(2Dpq-W)(2Dpq+W)=C^2S^2.
}
\tag{26.3}
\]

Let `ell` be an odd prime with `e=v_ell(C)`. Since `(D,C)=1`:

- if `ell|pq`, the prime is already routed into the primitive cover denominator/numerator product `pq`;
- if `ell\nmid pq`, then the two factors on the left of (26.3) cannot both be divisible by `ell`, because their sum is `4Dpq`.

Hence exactly one sign absorbs the full `C^2` contribution:

\[
\boxed{
ell^{2e}\mid 2Dpq+\epsilon W}
\]

for a unique sign modulo `ell`.

This is the missing C-column routing. It is the integral valuation form of the dual full-2-torsion descent signature above.

## 6. Complete odd-prime routing theorem

For every physical rank-active direction and every odd prime occurring in one of

\[
r,\quad u,\quad C,\quad D,
\]

there is an explicit covering-side state of one of the following forms:

```text
D-column:
  ell | p^2+q^2
  or ell^(2e) | W ± rho*C*(p^2+q^2)

r/u-column, ell=3 mod 4:
  ell^f | W and ell^f | p^2-q^2

r/u-column, ell=1 mod 4:
  ell | p^2-q^2
  or ell^(2f) | W ± rho*C*(p^2-q^2)

C-column:
  ell | p*q
  or ell^(2e) | 2D*p*q ± W
```

Here `rho^2=-1` modulo the required split-prime power. Each split prime introduces only a bounded sign choice; over all prime factors this costs at most `2^{omega}=B^{o(1)}` states.

Thus the local routing portion of the Le Boudec transfer is complete at all odd primes.

## 7. Exact same-partition pair-count handoff

Fix `(alpha,beta)`. A rank-energy collision consists of two distinct reduced directions

\[
(r_1,u_1),\qquad(r_2,u_2)
\]

with their physical primitive cover triples `(p_j,q_j,W_j)`.

Choose, for each direction, a usable large odd prime from one of the four moving columns. Stage14-t26 maps it into one of the finite states in Section 6. Therefore, after a `B^{o(1)}` state decomposition, `Q_rank(B)` is bounded by a sum of explicit pair-incidence counts with:

- one large prime divisor/congruence condition on each physical cover;
- the same fixed split kernel `(alpha,beta)`;
- the original height bounds `D_j<=B` and physical cover bounds.

No spectral or polynomial-sieve estimate is invoked here. The next analytic task is to prove that almost all relevant directions possess a sufficiently large odd prime in at least one moving column, control the smooth exceptional set, and count the routed pair incidences with a fixed power saving.

## 8. What is and is not proved

Proved in t26:

- explicit dual curve with full rational 2-torsion;
- exact physical dual-descent signature `[1,-1,-1]`;
- complete local routing for every odd prime in `r,u,C,D`;
- only a `B^{o(1)}` finite-state loss from Gaussian sign allocation.

Not proved:

- existence of a large odd prime of prescribed size for every or almost every active direction;
- a power-saving bound for the smooth/no-large-prime exceptional set;
- the final routed pair-incidence estimate;
- `Q_rank(B)=O(B^{1-delta})`.

## Boundary

```text
STAGE14_T26=COMPLETE_ODD_PRIME_GAUSSIAN_AND_DUAL_ROUTING
DUAL_CURVE_FULL_RATIONAL_2_TORSION=true
PHYSICAL_DUAL_DESCENT_SIGNATURE=1,-1,-1
D_COLUMN_ODD_PRIME_ROUTING_COMPLETE=true
RU_COLUMN_ODD_PRIME_ROUTING_COMPLETE=true
C_COLUMN_ODD_PRIME_ROUTING_COMPLETE=true
ODD_LARGE_PRIME_LOCAL_ROUTING_COMPLETE=true
GAUSSIAN_STATE_LOSS=B^o(1)
LARGE_PRIME_AVAILABILITY_POWER_SAVING_PROVED=false
ROUTED_PAIR_INCIDENCE_POWER_SAVING_PROVED=false
RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t27 large-prime availability / smooth-exception split and routed same-partition pair-incidence count
```
