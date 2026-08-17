# Stage27-19-r5ac — three norm-support restrictions on `(p,q,g)`

```text
TASK_ID=Stage27-19-r5ac
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ab
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

This route extracts unconditional prime-support consequences from the exact r5aa/r5ab normalization. These are genuine survivor-support restrictions, but no fixed-power saving is promoted from them.

Retain

\[
M=m^2+n^2=ha,
\qquad
p=s_0^2a,
\qquad
g=d^2h,
\]

and

\[
J=ab h+d^2(p-q)=\kappa w^2,
\qquad
\kappa=\operatorname{sf}(p+q).
\]

## 1. The reduced numerator `p` and the common core `g` are sums of two squares

Because `(m,n)=1`, no odd prime `ell=3 mod 4` can divide

\[
M=m^2+n^2.
\]

Indeed, if such an `ell` divided `M`, then `ell` cannot divide `n` (otherwise it would divide `m`), so `(m n^{-1})^2=-1 mod ell`, contradicting the quadratic nonresiduacity of `-1` for `ell=3 mod 4`.

Therefore every odd prime `3 mod 4` occurs with exponent zero in both divisors `a` and `h` of `M`. Since

\[
p=s_0^2a,
\qquad
g=d^2h,
\]

all primes `3 mod 4` occur to even exponent in `p` and in `g`. By the two-squares criterion,

\[
\boxed{p\text{ is a sum of two integer squares}},
\]

and

\[
\boxed{g\text{ is a sum of two integer squares}}.
\]

Equivalently,

\[
\operatorname{sf}(p),\operatorname{sf}(g)
\]

contain no prime `3 mod 4`.

This restriction on `p` already belongs to the two-face toric arithmetic after reduction; the restriction on `g` is exposed by the r5aa core factorization.

## 2. Coprimality of the extracted square scale with the normalized squareclass variable

From

\[
M=ha,\qquad K=hb,
\]

and the primitive slope conditions,

\[
(d,M)=(d,K)=1.
\]

Hence

\[
\boxed{(d,a)=(d,b)=(d,h)=1}.
\]

Therefore

\[
J=ab h+d^2(p-q)
\]

satisfies

\[
\boxed{(d,J)=1}.
\]

Since `J=kappa w^2`,

\[
\boxed{(d,\kappa)=(d,w)=1}.
\]

This removes a possible fake local branch in which the common square scale `d` absorbs the squarefree coefficient of the space condition.

## 3. Every odd prime in `kappa=sf(p+q)` is split modulo four

Let an odd prime `ell` divide `kappa`. Then `ell|p+q`. Since `(p,q)=1`,

\[
ell\nmid pq.
\]

As `s_0^2|p`, `n_0^2|q`, `a|p`, and `b|q`, the prime `ell` divides none of

\[
a,b,s_0,n_0,p,q.
\]

Section 2 also gives `ell\nmid d` because `ell|J` and `(d,J)=1`.

Use the second diagonal equation from r5ab,

\[
\kappa w^2=ar^2-q d^2.
\]

Modulo `ell`, the left side vanishes, so

\[
ar^2\equiv qd^2\pmod\ell.
\]

But `a=p/s_0^2` and `p\equiv-q mod ell`. Therefore

\[
-\frac{q}{s_0^2}r^2\equiv qd^2\pmod\ell,
\]

and all denominators are invertible. Thus

\[
\boxed{\left(\frac{r}{s_0d}\right)^2\equiv-1\pmod\ell}.
\]

Hence `-1` is a quadratic residue modulo `ell`, forcing

\[
\boxed{\ell\equiv1\pmod4}.
\]

So the odd part of `kappa` is supported only on split primes.

## 4. The squarefree coefficient `kappa` is in fact odd

It remains to exclude `2|kappa`.

Assume `2|kappa`. Then `p+q` is even, so coprimality forces `p,q` odd. Hence `a,b,s_0,n_0` are all odd.

Because `J=kappa w^2` is even, the identity

\[
J=bm^2+p d^2
\]

shows first that `d` cannot be even: if `d` were even, `(m,d)=1` would make `m` odd and the right side would be odd. Thus `d` is odd. The same identity then forces `m` odd. Likewise

\[
J=ar^2-q d^2
\]

forces `r` odd.

Now reduce the normalized conic

\[
ar^2-bm^2=(p+q)d^2
\]

modulo `8`. Odd squares are `1 mod 8`, while `s_0^2=n_0^2=1 mod 8`, so

\[
a\equiv p\pmod8,
\qquad
b\equiv q\pmod8.
\]

Therefore the conic gives

\[
p-q\equiv p+q\pmod8,
\]

hence `2q=0 mod 8`, impossible for odd `q`.

Thus

\[
\boxed{2\nmid\kappa}.
\]

Combining with Section 3,

\[
\boxed{\kappa=\operatorname{sf}(p+q)\text{ is a product only of primes }1\pmod4}.
\]

In particular every prime `3 mod 4` occurs to even exponent in `p+q`, and its 2-adic valuation is also even. Hence

\[
\boxed{p+q\text{ is a sum of two integer squares}}.
\]

## 5. Three simultaneous support restrictions

Every Stage19 survivor therefore has the exact reduced-label restrictions

\[
\boxed{
p\in\mathcal S_2,
\qquad
g\in\mathcal S_2,
\qquad p+q\in\mathcal S_2,
}
\]

where `S_2` denotes the positive integers representable as a sum of two squares.

These conditions are simultaneous and same-measure. They are useful local sieves for the r5ab moving diagonal-quadrics receiver, especially because the difficult denominator `q` is now coupled to `p` by a second norm condition `p+q in S_2`.

However this route proves no fixed-power bound for the number of such labels in a dyadic tau band. No logarithmic-density heuristic or classical average theorem is promoted into the Stage27 exponent ledger. The half-power wall therefore remains intact.

The next mathematically honest step is no longer another algebraic normalization. It requires a uniform counting theorem for the moving diagonal intersection / simultaneous norm-support system, or a genuinely fixed-power square-sieve estimate on the realized `(p,q,g)` support. That is theorem-level new input and should be fresh-audited before being used to change the Stage27 upper exponent.

```text
P_SUM_TWO_SQUARES_PROVED=true
G_SUM_TWO_SQUARES_PROVED=true
D_J_COPRIME_PROVED=true
D_KAPPA_COPRIME_PROVED=true
D_W_COPRIME_PROVED=true
KAPPA_ODD_PROVED=true
KAPPA_ODD_PRIME_SUPPORT=1_mod_4_only
P_PLUS_Q_SUM_TWO_SQUARES_PROVED=true
THREE_SIMULTANEOUS_NORM_SUPPORT_RESTRICTIONS_PROVED=true
THREE_NORM_SUPPORT=p,g,p+q_are_sums_of_two_squares
FIXED_POWER_SUPPORT_SAVING_FROM_NORM_RESTRICTIONS_PROVED=false
UNIFORM_MOVING_DIAGONAL_QUADRICS_COUNT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
BATCH_STOP_REASON=NEXT_STEP_REQUIRES_FRESH_THEOREM_LEVEL_UNIFORM_COUNTING_INPUT
NEXT_DERIVED_ROUTE=27-19-r5ad
NEXT_EXPECTED_COMMAND=Stage27-19-r5aa-audit
```
