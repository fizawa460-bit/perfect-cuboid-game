# Stage27-19-r5am — uniform Pell compression of the residual completion fiber

```text
TASK_ID=Stage27-19-r5am
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5al
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Input retained from r5al

Use

\[
Q_1=a c_s^2\sigma^2+b c_n^2\nu^2=\kappa c_0^2c'^2,
\]

\[
Q_2=b c_0^2\mu^2+a\delta^2\sigma^2=\kappa c_n^2w'^2,
\]

\[
Q_3=a c_0^2\rho^2-b\delta^2\nu^2=\kappa c_s^2w'^2.
\]

The exact physical budget remains

\[
\delta c_0c_sc_n\mu\rho\nu\sigma\le B.
\]

No coarse toric replacement is made.

## 2. Uniform Pell-count lemma

**Lemma.** Let positive integers \(A,B,N\) and \(H\ge2\) be given.  The number of positive integer solutions

\[
A x^2-B y^2=N,\qquad x,y\le H,
\]

is

\[
\ll_\epsilon (ABNH)^\epsilon
\]

uniformly in \(A,B,N,H\).

**Proof.** Multiply by \(A\) and set \(X=Ax\), \(D=AB\).  Then

\[
X^2-Dy^2=AN.
\]

If \(D\) is a square, the left side factors over \(\mathbf Z\), so the number of solutions is bounded by a divisor function of \(AN\).

If \(D\) is not a square, a solution \(X+y\sqrt D\) has norm \(AN\) in the quadratic order \(\mathbf Z[\sqrt D]\).  Principal solution ideals lie among ideal divisors of \((AN)\); the number of such local divisor choices is \((DAN)^\epsilon\) by the divisor bound, including primes meeting the order conductor.  Within each ideal class of solutions, multiplication by norm-one units produces one Pell orbit.  The number of orbit points of height at most a fixed polynomial in \(H\) is \(O(\log H)\), uniformly, because every real quadratic fundamental unit is bounded away from 1.  Hence the total number is \((ABNH)^\epsilon\).  The additional divisibility condition \(A\mid X\) can only remove solutions.  \(\square\)

Only the subpower conclusion is used below.

## 3. Eight-variable completion compression

Fix

\[
(a,b,\delta,c_0,c_s,c_n,\nu,\sigma).
\]

Then \(Q_1\) is fixed.  If a Stage19 completion exists, r5al forces uniquely

\[
\kappa=\operatorname{sf}(Q_1),\qquad
c'=\frac1{c_0}\sqrt{Q_1/\kappa}.
\]

Thus only \((\mu,w',\rho)\) remain.

Equation \(Q_2=\kappa c_n^2w'^2\) is

\[
\kappa c_n^2w'^2-bc_0^2\mu^2=a\delta^2\sigma^2.
\]

Put

\[
X=c_nw',\qquad Y=c_0\mu.
\]

Then

\[
\kappa X^2-bY^2=a\delta^2\sigma^2.
\]

After multiplying by \(\kappa\), this is the Pell/norm equation

\[
(\kappa X)^2-\kappa bY^2
=\kappa a\delta^2\sigma^2.
\]

All coefficients and all physical variables have polynomial height in \(B\): r402a gives \(m,n,r,s\ll B^{1/2}\), while \(a,b,\kappa\ll B^{O(1)}\), and the exact diagonal product gives \(w'\le B\).  Therefore the uniform Pell lemma gives

\[
\#\{(\mu,w')\text{ compatible with the fixed eight outer variables}\}
\ll_\epsilon B^\epsilon.
\]

For each such \((\mu,w')\), equation \(Q_3=\kappa c_s^2w'^2\) determines at most one positive \(\rho\):

\[
\rho^2=
\frac{\kappa c_s^2w'^2+b\delta^2\nu^2}{a c_0^2}.
\]

The chamber, primitive-slope, reconstruction, exactly-two-face and exact physical-cutoff tests only remove candidates.

Hence:

\[
\boxed{
\text{for fixed }(a,b,\delta,c_0,c_s,c_n,\nu,\sigma),
\text{ the Stage19 completion multiplicity is }B^{o(1)}.
}
\]

This strictly strengthens the r5al statement that multiplicity is at most one only after also fixing \(\mu\).

## 4. What this does not prove

The remaining outer support is still moving in \((a:b)\) and in the residual scale variables.  The Pell compression removes one free completion direction but does not yet count the number of eight-variable outer cells with a fixed-power saving.

In particular it does **not** prove

\[
N_2(B)\ll B^{1/2-\eta}.
\]

The next useful receiver is to exploit the common squarefree kernel \(\kappa\) as a growing modulus on the original slopes, rather than treating it only as a coefficient in the norm equation.

```text
UNIFORM_PELL_COUNT_LEMMA_PROVED=true
EIGHT_OUTER_VARIABLE_COMPLETION_MULTIPLICITY=B^o(1)
R5AL_NINE_VARIABLE_UNIQUENESS_STRENGTHENED=true
UNIFORM_MORDELL_WEIL_RANK_ASSUMED=false
EXACT_PHYSICAL_CUTOFF_RETAINED=true
OUTER_CELL_FIXED_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5an
```
