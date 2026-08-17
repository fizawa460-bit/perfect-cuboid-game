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

**Lemma.** Let positive integers \(A,B,N\) and \(H\ge2\) be given. The number of positive integer solutions

\[
A x^2-B y^2=N,\qquad x,y\le H,
\]

is

\[
\ll_\epsilon (ABNH)^\epsilon
\]

uniformly in \(A,B,N,H\).

### Proof

Multiply by \(A\), and put

\[
X=Ax,\qquad D=AB,\qquad M=AN.
\]

Then

\[
X^2-Dy^2=M.
\]

#### Square case

If \(D=t^2\) is a square, then

\[
(X-ty)(X+ty)=M.
\]

Every positive solution gives a factor pair of \(M\). Hence the number of solutions is at most \(\tau(M)\), which is \(M^{o(1)}\). The congruence and positivity conditions needed to recover \((X,y)\), and the divisibility condition \(A\mid X\), only remove factor pairs.

#### Nonsquare case: pass to the maximal order

Suppose \(D\) is not a square. Write

\[
D=t^2d
\]

with \(d>1\) squarefree, and let

\[
K=\mathbf Q(\sqrt d),\qquad \mathcal O_K
\]

be its maximal order. For a positive solution define

\[
\alpha=X+y\sqrt D=X+ty\sqrt d\in\mathcal O_K.
\]

Its field norm is

\[
N_{K/\mathbf Q}(\alpha)=M.
\]

Because \(X>0\), \(y>0\), and \(M=X^2-Dy^2>0\), one has

\[
X>y\sqrt D,
\]

so both real embeddings of \(\alpha\) are positive.

As ideals in the Dedekind domain \(\mathcal O_K\),

\[
(\alpha)(\bar\alpha)=(M).
\]

Therefore \((\alpha)\) is an integral ideal divisor of \((M)\).

Now write \(p^e\Vert M\). The number of possible local exponents in an ideal divisor of \((M)\) is bounded uniformly in the splitting type of \(p\):

- if \(p\) splits, at most \((e+1)^2\);
- if \(p\) is inert, at most \(e+1\);
- if \(p\) ramifies, at most \(2e+1\).

Hence the total number of integral ideal divisors of \((M)\) is bounded by

\[
\prod_{p^e\Vert M}(2e+1)^2
\le \tau(M^2)^2
= M^{o(1)},
\]

uniformly in the quadratic field \(K\). In particular no separate conductor-prime estimate is needed.

Fix one principal ideal \(I=(\alpha_0)\) occurring this way. Any other generator of \(I\) with norm \(M\) differs from \(\alpha_0\) by a norm-one unit, up to the harmless sign torsion. Since the desired generators are positive in both real embeddings, they lie in one orbit under the totally positive norm-one unit group.

Let \(\varepsilon_K>1\) generate that positive unit group. Its trace is an integer and, for a nontrivial norm-one real quadratic unit,

\[
\varepsilon_K+\varepsilon_K^{-1}\ge3.
\]

Thus uniformly

\[
\varepsilon_K\ge\frac{3+\sqrt5}{2}>1.
\]

For our bounded solutions,

\[
0<\alpha=X+y\sqrt D\le H(A+\sqrt{AB}).
\]

Also \(\alpha\bar\alpha=M\) and \(\alpha\ge\bar\alpha>0\), so \(\alpha\ge\sqrt M\). Consequently, inside one unit orbit the number of admissible generators is

\[
O\!\left(1+
\frac{\log\!\big(H(A+\sqrt{AB})/\sqrt M\big)_+}{\log\varepsilon_K}
\right)
=O(\log(ABNH)),
\]

with an absolute implied constant.

Multiplying the \(M^{o(1)}\) possible ideal divisors by this logarithmic number of unit translates gives

\[
\#\{(x,y):Ax^2-By^2=N,\ x,y\le H\}
\ll_\epsilon (ABNH)^\epsilon.
\]

Finally, the requirement \(A\mid X\) only removes solutions. This proves the lemma. \(\square\)

The important repair is that the nonsquare argument is carried out in the maximal order \(\mathcal O_K\); the earlier informal appeal to ideal divisors inside \(\mathbf Z[\sqrt D]\) at conductor primes is not used.

Only the subpower conclusion is used below.

## 3. Eight-variable completion compression

Fix

\[
(a,b,\delta,c_0,c_s,c_n,\nu,\sigma).
\]

Then \(Q_1\) is fixed. If a Stage19 completion exists, r5al forces uniquely

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

All coefficients and all physical variables have polynomial height in the Stage19 cutoff parameter \(B\): r402a gives \(m,n,r,s\ll B^{1/2}\), while \(a,b,\kappa\ll B^{O(1)}\), and the exact diagonal product gives \(w'\le B\). Therefore the repaired uniform Pell lemma gives

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

The remaining outer support is still moving in \((a:b)\) and in the residual scale variables. The Pell compression removes one free completion direction but does not yet count the number of eight-variable outer cells with a fixed-power saving.

In particular it does **not** prove

\[
N_2(B)\ll B^{1/2-\eta}.
\]

The next useful receiver is to exploit the common squarefree kernel \(\kappa\) as a growing modulus on the original slopes, rather than treating it only as a coefficient in the norm equation.

```text
UNIFORM_PELL_COUNT_LEMMA_PROVED=true
UNIFORM_PELL_PROOF_MAXIMAL_ORDER_REPAIRED=true
NONMAXIMAL_ORDER_CONDUCTOR_ARGUMENT_USED=false
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
