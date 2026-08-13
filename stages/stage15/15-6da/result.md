# Stage15-6da — divisor-many fourth-variable completion via a Pell norm

Base: Stage15-6cz. Fix one legal cross-gcd cell package `(a,b,c,d)`, fix three residual variables `(M,N,U)`, and retain all legal local channel orientations. We prove that the remaining positive residual variable `V` has only `B^{o(1)}` exact-survivor completions.

Stage15-6cz reduces the possible common squarefree cores to a divisor-many set
\[
k^\circ\mid |X^4-Y^4|,
\qquad X=abM,\quad Y=cdN,
\]
with only bounded 2-primary choices. Fix one such `k`.

The first exact survivor equation is
\[
a^4M^2U^2+d^4N^2V^2=kP^2.
\]
Put
\[
C=a^2MU,\qquad L=d^2NV.
\]
Then
\[
\boxed{L^2-kP^2=-C^2.}
\]
This is a binary norm equation.

## 1. The case k=1

Here
\[
(P-L)(P+L)=C^2.
\]
Every solution is determined by a factor pair of `C^2`, hence there are
\[
\ll \tau(C^2)=B^{o(1)}
\]
possible values of `L`, and therefore of `V`.

## 2. The case k>1 squarefree

Work in the maximal order of `K=Q(sqrt(k))`. For
\[
\xi=L+P\sqrt{k}
\]
we have
\[
N_{K/Q}(\xi)=-C^2.
\]
Consequently
\[
(\xi)(\bar\xi)=(C)^2.
\]
Thus the principal ideal `(xi)` is an integral ideal divisor of `(C)^2`. The number of ideal divisors of `(C)^2` is at most divisor-like: each rational prime contributes at most two prime ideals and polynomially bounded exponents, so
\[
\#\{I:I\mid(C)^2\}=B^{o(1)}.
\]
For each principal ideal divisor, all generators differ by a unit. The real quadratic unit group has rank one; under the physical bounds `m,r<=2B`, `n,s<=B`, both `L` and `P` are polynomially bounded in `B`. Hence only `O(log B)` powers of a fundamental unit can occur for one ideal divisor. Therefore
\[
\boxed{\#\{(L,P):L^2-kP^2=-C^2,\ |L|,|P|\le B^{O(1)}\}=B^{o(1)}.}
\]
The divisibility `L=d^2NV` and positivity merely select a subset, so the same bound holds for `V`.

The second norm equation
\[
b^4M^2V^2+c^4N^2U^2=kQ^2,
\]
all local root/sign orientations, `(q,H)=1`, primitiveness, positivity, exactly-two, canonical ordering and the physical cutoff are postfilters. None can enlarge the completion fiber.

Summing over the `B^{o(1)}` possible cores from 6cz proves
\[
\boxed{\#\{V:\text{exact physical survivor completion}\}=B^{o(1)}}
\]
for fixed cells and fixed `(M,N,U)`.

The statement is symmetric. If a different residual variable is left free, use the fixed opposite toric pair to place `k^circ` in the corresponding fixed fourth-power difference and use the analogous norm equation. Thus any three residual variables determine the fourth up to divisor-many/Pell-unit multiplicity.

This is an exact Stage15 reconstruction theorem. It does not import a Stage14 counting exponent and it does not charge the common core twice.

A concrete check is the S-channel witness `(m,n,r,s)=(13,1,9,1)`, for which all cells are `1`, `(M,N,U,V)=(13,1,9,1)`, `k=10`, and
\[
1^2-10\cdot37^2=-117^2,
\]
exactly matching the displayed norm equation.

```text
STAGE15_6_SUBSTAGE=6da
STAGE15_6DA_FIXED_THREE_RESIDUALS_COMPLETION=B^o(1)
STAGE15_6DA_CORE_LIST_MULTIPLICITY=B^o(1)
STAGE15_6DA_FIXED_CORE_COMPLETION=PELL_NORM_EQUATION
STAGE15_6DA_PELL_COMPLETION_MULTIPLICITY=B^o(1)
STAGE15_6DA_SECOND_NORM_AND_PHYSICAL_MASKS=POSTFILTERS
STAGE15_6DA_AR010_STYLE_RECONSTRUCTION_POSITIVE=true
STAGE15_6DA_NO_STAGE14_EXPONENT_TRANSFER=true
STAGE15_6DA_EXIT=RECONSTRUCTION_TO_DELTA_SIGMA_LEDGER_READY
```