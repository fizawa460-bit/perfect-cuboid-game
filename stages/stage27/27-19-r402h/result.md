# Stage27-19-r402h — primitive `(A,D)` support reformulation and route verdict

```text
TASK_ID=Stage27-19-r402h
PARENT_ROUTE=Stage27-19-r402g
ROUTE_KIND=UPPER_SUPPORT_REFORMULATION
CURRENT_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

For every realized reduced tau/core pair

\[
t=p/q,\qquad g\in\mathcal G_t(B),
\]

the unreduced pair is exactly

\[
\boxed{(A,D)=(pg,qg)},
\]

with

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2),\qquad A,D<2B^2.
\]

Conversely `(A,D)` uniquely determines

\[
g=\gcd(A,D),\qquad (p,q)=(A/g,D/g).
\]

Therefore the realized `(tau,g)` incidence set is in exact bijection with the realized integer-pair support

\[
\mathcal P(B)=\{(A,D):\exists\text{ physical Stage19 object with these }A,D\}.
\]

In a dyadic tau-height band this bijection simply imposes

\[
T\le \max(A/g,D/g)<2T.
\]

Hence the r402g first-moment target is equivalently

\[
\boxed{\#\mathcal P_T(B)\ll B^{1/2-\delta+o(1)}}
\]

uniformly in `T`, where `\mathcal P_T` is the corresponding primitive-direction slice of realized `(A,D)` pairs.

This reformulation matters because it shows that gcd/core manipulations alone cannot create an additional saving: `(tau,g)` is merely the canonical gcd decomposition of `(A,D)`.  Any future fixed-power theorem must use a genuinely new arithmetic restriction coupling the two forms

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2)
\]

under the same physical variables and masks.  Counting possible gcds, possible reduced slopes, or possible divisors separately only reparameterizes the same support.

The most promising remaining upper mechanisms are therefore external/nontrivial ones: a same-measure bilinear/incidence estimate for the coupled forms, a determinant-method bound for the realized `(A,D)` image, or a sieve theorem that exploits the simultaneous sum-of-two-squares / difference-of-squares structure without charging conditions already used in Stage14/15.

No such theorem is currently present in the repository.  Thus the r402 reentry has made genuine progress (fixed-core multiplicity is removed) but has now reached a clean **support theorem wall** rather than another elementary factorization problem.

Per the route policy, do not create r402i by merely renaming this support wall.  After fresh audit, either:

1. reopen an upper route only with a genuinely new coupled-form incidence/determinant/sieve input; or
2. if no such input is available, return to the audited lower route rather than looping elementary support decompositions.

```text
REALIZED_TAU_CORE_TO_AD_SUPPORT_BIJECTION_PROVED=true
GCD_CORE_REPARAMETRIZATION_GIVES_NO_NEW_SAVING=true
ELEMENTARY_R402_CONTINUATION_VIABILITY=NO_GO
R402_REENTRY_PROGRESS=FIXED_CORE_MULTIPLICITY_GATE_DISCHARGED
R402_CURRENT_WALL=COUPLED_FORM_REALIZED_AD_SUPPORT_THEOREM
R402I_AUTOMATIC_CONTINUATION_FORBIDDEN=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
ROUTE_DECISION_AFTER_AUDIT=NEW_UPPER_INPUT_OR_LOWER_ROUTE
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```
