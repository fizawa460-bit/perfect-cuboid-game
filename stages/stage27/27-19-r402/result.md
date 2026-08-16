# Stage27-19-r402 — tau-pushforward upper reentry

```text
TASK_ID=Stage27-19-r402
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
ROUTE_LABEL=STAGE19_TAU_PUSHFORWARD_UPPER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_UPPER_EXPONENT=1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Purpose

The bounded lower reentry `Stage27-19-r401` through `r401d` has reached an audited stopping boundary. PR #1036 passed fresh hostile re-audit and merged at

```text
b37bc86e045175238bf2520518b059574addc52b
```

This route returns to checkpoint40 from the Stage19 exact toric receiver, but uses the natural `tau` coordinate as an **upper-side pushforward label**, not as a lower-family parametrization.

The target remains

\[
N_2(B)\ll_\varepsilon B^{\mu+\varepsilon},\qquad \mu<\frac12.
\]

No population, cutoff, or multiplicity adapter is changed.

## 2. Exact tau identity on the Stage19 survivor surface

For a Stage19 survivor write

\[
x=m/n,\qquad y=r/s,
\]

and use the audited master receiver

\[
x^2y^2+1=z^2(x^2+y^2).
\]

Thus

\[
z^2=\frac{x^2y^2+1}{x^2+y^2}.
\]

The r401a fibration coordinate is

\[
\tau=\frac{x^2-z^2}{z^2-1}.
\]

Direct substitution gives

\[
x^2-z^2
=\frac{x^4-1}{x^2+y^2}
=\frac{(x^2-1)(x^2+1)}{x^2+y^2},
\]

and

\[
z^2-1
=\frac{(x^2-1)(y^2-1)}{x^2+y^2}.
\]

On the positive physical chart `x^2!=1`, `y^2!=1`, hence

\[
\boxed{\tau=\frac{x^2+1}{y^2-1}}.
\]

Returning to homogeneous toric variables,

\[
\boxed{
\tau=\frac{s^2(m^2+n^2)}{n^2(r^2-s^2)}.
}
\]

This second formula is important on the upper side: it is a rational function of the two-face toric host variables **before** imposing the integral-space condition. Thus `tau` can be used as an outer physical pushforward label on the ambient two-face host; a Stage19 survivor simply lands on a `tau` fiber that also contains a rational `z` point of the genus-one receiver.

The label is invariant under independent homogeneous rescaling `(m,n)->lambda(m,n)` and `(r,s)->mu(r,s)` and is positive on the frozen positive chart `m>n>0`, `r>s>0`.

```text
TAU_SURVIVOR_IDENTITY_PROVED=true
TAU_TORIC_FORMULA_PROVED=true
TAU_DEFINED_BEFORE_SPACE_FILTER=true
TAU_IS_OUTER_PHYSICAL_RATIONAL_LABEL=true
```

## 3. Exact tau-collision receiver

Two toric points `(m_i,n_i,r_i,s_i)`, `i=1,2`, have the same `tau` exactly when

\[
\boxed{
 s_1^2(m_1^2+n_1^2)n_2^2(r_2^2-s_2^2)
 =s_2^2(m_2^2+n_2^2)n_1^2(r_1^2-s_1^2).
}
\]

This is the exact collision equation for any future `tau`-energy or weighted-pushforward theorem. No independence, equidistribution, or sparsity is assumed here.

## 4. Polynomial physical support is genuinely present

The audited lower calibration now gives more than a lower-family stopping rule. R501 and R502 each have

\[
N_{R50i}(B)=\Theta(B^{1/4})
\]

and r401d proves that their reduced maps to the `tau`-line have degree eight.

A nonconstant rational map of degree eight has at most eight preimages of a generic `tau` value over the parameter line, with only finitely many exceptional branch/denominator points. Together with the already-audited bounded physical parameter multiplicity, R501 alone therefore forces

\[
\boxed{\#\operatorname{Supp}_\tau(N_2(B))\gg B^{1/4}.}
\]

The same conclusion is available from R502.

This matters for checkpoint40 routing: `tau` is not another fixed-`U` residue-class universe of size `B^{o(1)}`. It is an actual outer physical rational label with polynomially many values already realized by certified Stage19 objects. Consequently the Stage27-40ad obstruction to averaging over a subpolynomial fixed-`U` class family does **not automatically close** `tau`-pushforward averaging.

This is not an upper saving. Polynomial cardinality by itself is not charged as a deficit.

```text
R501_TAU_PROJECTION_DEGREE_USED=8
R502_TAU_PROJECTION_DEGREE_USED=8
TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true
TAU_SUPPORT_LOWER_EXPONENT=1/4
FIXED_U_SUBPOLY_CLASS_OBSTRUCTION_AUTOMATICALLY_APPLIES_TO_TAU=false
TAU_CARDINALITY_ALONE_GIVES_UPPER_SAVING=false
```

## 5. Upper exponent calculus for the tau pushforward

Let

\[
\mathcal T(B)=\{\tau(Q):Q\in\mathcal A_2(B)\}
\]

and define the physical survivor weight

\[
w_B(t)=\#\{Q\in\mathcal A_2(B):\tau(Q)=t\}.
\]

Then exactly

\[
\boxed{N_2(B)=\sum_{t\in\mathcal T(B)}w_B(t).}
\]

Suppose a future theorem proves

\[
\#\mathcal T(B)\ll B^{\sigma+o(1)}
\]

and

\[
\max_t w_B(t)\ll B^{\phi+o(1)}.
\]

Then

\[
\boxed{N_2(B)\ll B^{\sigma+\phi+o(1)}}.
\]

Therefore the exact max-fiber progress gate is

\[
\boxed{\sigma+\phi<\frac12.}
\]

The audited lower families imply only `sigma>=1/4` for the realized global support in the weak limsup/exponent sense; they do not determine the true support exponent. In particular, a route with `sigma=1/4` would need `phi<1/4`, while a subpolynomial fiber theorem `phi=0` would still require a strict support theorem `sigma<1/2`.

A second-moment version is also exact. Put

\[
E_\tau(B)=\sum_{t\in\mathcal T(B)}w_B(t)^2.
\]

By Cauchy,

\[
N_2(B)^2\le \#\mathcal T(B)\,E_\tau(B).
\]

Hence bounds

\[
\#\mathcal T(B)\ll B^{\sigma+o(1)},\qquad E_\tau(B)\ll B^{\eta+o(1)}
\]

give

\[
\boxed{N_2(B)\ll B^{(\sigma+\eta)/2+o(1)}}
\]

and strict sub-half follows from

\[
\boxed{\sigma+\eta<1.}
\]

These are sufficient theorem interfaces, not claims that the required support/fiber/energy bounds are already known.

```text
TAU_MAX_FIBER_UPPER_GATE=sigma+phi<1/2
TAU_SECOND_MOMENT_UPPER_GATE=sigma+eta<1
TAU_SUPPORT_STRICT_SUBHALF_THEOREM_PROVED=false
TAU_UNIFORM_FIBER_SUBPOWER_THEOREM_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_THEOREM_PROVED=false
```

## 6. Relation to checkpoint40 routes

This route is distinct from the already-closed shortcuts:

- it does not improve the `B^o(1)` elliptic multiplicity and call that a fixed-power gain;
- it does not reuse fixed-prime squareclass density as a polynomial sieve;
- it does not average only over the fixed-`U` Gaussian residue classes from 40ad;
- it does not recharge raw outer-cardinality already paid in the Stage14 complete host.

Instead it creates an exact Stage19-native outer pushforward whose collision equation is explicit. To become a strict upper theorem, a future `r402a+` task must prove a **same-physical-measure** support/fiber or weighted-energy deficit satisfying one of the gates above. The most direct next tests are:

1. determine the physical height of reduced `tau=p/q` uniformly on `R<=B` and obtain a nontrivial support upper bound;
2. bound fixed-`tau` physical fibers using the genus-one receiver with all toric/primitivity adapters retained;
3. attack the exact collision equation by a weighted second moment across the actual physical population.

No one of these is claimed solved in r402.

## 7. Verdict

`r402` does not yet improve `mu=1/2`. Its concrete advance is to turn the previously lower-side `tau` fibration into a legal checkpoint40 outer physical averaging variable, prove the exact host formula and collision receiver, and show from the audited R501/R502 degree-eight calibration that the realized `tau` universe is genuinely polynomial rather than `B^{o(1)}`.

The remaining obstacle is now quantitative and explicit: obtain enough support/fiber anti-concentration to satisfy `sigma+phi<1/2`, or enough collision-energy control to satisfy `sigma+eta<1`.

```text
TAU_PUSHFORWARD_UPPER_REENTRY_EXECUTED=true
TAU_OUTER_PHYSICAL_LABEL_MATERIALIZED=true
TAU_COLLISION_RECEIVER_DERIVED=true
TAU_POLYNOMIAL_SUPPORT_CERTIFIED_FROM_KNOWN_FAMILIES=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```