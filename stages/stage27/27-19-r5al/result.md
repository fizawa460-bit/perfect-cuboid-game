# Stage27-19-r5al proposal — residual completion rigidity and the remaining uniform counting gate

```text
TASK_ID=Stage27-19-r5al
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PROPOSAL
PARENT_ROUTE=Stage27-19-r5aj-r5ak
STATUS=PROPOSED_INCONCLUSIVE_PENDING_FRESH_AUDIT
VERDICT=INCONCLUSIVE
```

## 1. Plain-language conclusion

The three residual equations do contain useful rigidity: after fixing nine outer
variables, all remaining variables are forced, if they exist at all.  Thus this
completion step does not need a uniform Mordell--Weil rank theorem.

This does **not** yet improve

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

The unresolved problem is now an outer-support problem.  The primitive
coefficient ratio \(a:b\) moves with the object, and the exact edge budget does
not by itself provide a uniform supply of good sieve primes for all coefficient
cells.  No strict-subhalf exponent is promoted in this route.

## 2. Inputs retained exactly

Use the r5aj residual chart

\[
m=c_0c_s\mu,\quad r=c_0c_n\rho,
\quad s_0=c_s\sigma,\quad n_0=c_n\nu,
\quad C=c_0c_sc_n,
\]

and retain the exact physical edge budget

\[
\boxed{\delta C\mu\rho\nu\sigma\le B.}
\]

On a Stage19 survivor, r5ak gives

\[
a c_s^2\sigma^2+b c_n^2\nu^2
 =\kappa c_0^2c'^2, \tag{S1}
\]

\[
b c_0^2\mu^2+a\delta^2\sigma^2
 =\kappa c_n^2w'^2, \tag{S2}
\]

\[
a c_0^2\rho^2-b\delta^2\nu^2
 =\kappa c_s^2w'^2. \tag{S3}
\]

Here \(\kappa\) is squarefree and \(L=c'w'\).  The actual r5ak survivor with
\(L=1\) remains in scope; this route makes no pointwise lower-bound claim for
\(L\).

## 3. Proved residual-completion rigidity lemma

**Lemma.** Fix positive integers

\[
(a,b,\delta,c_0,c_s,c_n,\mu,\nu,\sigma),
\qquad (a,b)=1.
\]

There is at most one positive-integer completion

\[
(\kappa,c',w',\rho)
\]

satisfying (S1)--(S3) with \(\kappa\) squarefree.

**Proof.** Put

\[
Q_1=a c_s^2\sigma^2+b c_n^2\nu^2.
\]

Equation (S1) says

\[
Q_1=\kappa(c_0c')^2.
\]

Since \(\kappa\) is squarefree, necessarily

\[
\boxed{\kappa=\operatorname{sf}(Q_1)},
\qquad
\boxed{c'=\frac1{c_0}\sqrt{Q_1/\kappa}}.
\]

Thus \(\kappa,c'\) are unique, or no integral completion exists.  Next put

\[
Q_2=b c_0^2\mu^2+a\delta^2\sigma^2.
\]

Equation (S2) forces

\[
\boxed{w'=\frac1{c_n}\sqrt{Q_2/\kappa}},
\]

again uniquely if the displayed value is integral.  Finally (S3) forces

\[
\boxed{
\rho^2=
\frac{\kappa c_s^2w'^2+b\delta^2\nu^2}{a c_0^2}.
}
\]

There is at most one positive value of \(\rho\).  This proves the lemma. \(\square\)

The physical budget can then only reject the unique completion; it cannot
create additional completions.

## 4. What the lemma does and does not buy

The lemma replaces a moving-fiber point-count question, in this completion
direction, by three exact arithmetic tests:

1. the squarefree kernel and divisibility test for \(Q_1\);
2. the square test for \(Q_2/\kappa\);
3. the final square test defining \(\rho\), followed by the exact edge budget.

This gives fiber multiplicity at most one.  It does not bound the number of
outer tuples.  In particular, the edge budget controls

\[
\delta c_0c_sc_n\mu\rho\nu\sigma,
\]

whereas the square tests contain the moving primitive coefficients \(a,b\).
Crude reconstruction only gives heights as large as the ambient quadratic
scale and loses the power one is trying to save.

For a square sieve, primes dividing

\[
2ab\delta c_0c_sc_n
\]

or the relevant discriminants/resultants are bad.  No existing r5 result proves
that every physical-budget cell has a fixed-power-sized collection of good
primes.  This is the exact missing uniformity.  A fixed-coefficient estimate is
not sufficient because \(a:b\) moves over the Stage19 population.

## 5. Proposed uniform small-L lemma

Let \(I(B,T)\) count admissible residual charts satisfying all exact
coprimality, chamber, reconstruction, (S1)--(S3), and physical-cutoff
conditions, with

\[
L=c'w'\le T.
\]

The useful target is: there exist constants \(\eta>0\) and \(A<\infty\) such
that, uniformly in an explicit power range of \(T\),

\[
\boxed{
I(B,T)\ll_\epsilon B^{1/2-\eta+\epsilon}T^A.
}
\tag{R5AL-SLI}
\]

The proposed proof architecture is:

1. apply the completion-rigidity lemma;
2. stratify by \(\gcd(Q_1,Q_2)\), \(ab\), \(\delta C\), and dyadic variable boxes;
3. apply a two-stage square sieve on good-prime-rich strata;
4. count bad-prime-rich strata by a gcd/resultant determinant estimate while
   retaining the exact edge product.

This lemma is not proved here.  Moreover the large-\(L\) side still needs a
companion estimate, for example

\[
\#\{R\le B:L>T\}
 \ll_\epsilon B^{1/2+\epsilon}T^{-\lambda}
\]

for some \(\lambda>0\).  Only after both estimates are proved and their
\(T\)-exponents are optimized may the project promote a strict-subhalf bound.

## 6. Safe experiment contract

A useful diagnostic experiment should enumerate exact primitive slope charts
and bucket them by dyadic \((L,C,\delta,\kappa)\).  Each bucket should record

\[
\gcd(Q_1,Q_2),\qquad
\operatorname{rad}(2ab\delta C),
\]

and the number of usable sieve primes up to a declared cutoff.  Its purpose is
to locate bad-prime-rich strata and formulate the missing theorem.  Numerical
output must not be promoted to an asymptotic exponent.

```text
RESIDUAL_COMPLETION_RIGIDITY_PROVED=true
RESIDUAL_COMPLETION_MULTIPLICITY_AT_MOST_ONE=true
UNIFORM_MORDELL_WEIL_RANK_ASSUMED=false
ACTUAL_L_EQ_1_WITNESS_RETAINED=true
MOVING_COEFFICIENT_UNIFORMITY_OBSTACLE_IDENTIFIED=true
UNIFORM_SMALL_L_FIXED_POWER_BOUND_PROVED=false
LARGE_L_COMPANION_DECAY_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
EXPONENT_PROMOTION_PROPOSED=false
VERDICT=INCONCLUSIVE
NEXT_TARGET=GOOD_PRIME_RICH_SQUARE_SIEVE_PLUS_BAD_PRIME_RICH_GCD_DETERMINANT_STRATIFICATION
```
