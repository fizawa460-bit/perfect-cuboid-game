# Stage29-02b — exact finite-field V4 point-count identity

```text
ROLE=JOINT_LOCAL_POINT_COUNT_DECOMPOSITION
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Let `q` be an odd good prime power for the common base and covers, and let `chi` be the quadratic character extended by `chi(0)=0`.  In a local trivialization of the two square-root line bundles, the number of solutions of

```text
u^2=f(P)
```

above a base point `P` is exactly `1+chi(f(P))`, including branch points.  Likewise for `g`.

Therefore the joint fiber size is

\[
(1+\chi(f(P)))(1+\chi(g(P)))
=1+\chi(f(P))+\chi(g(P))+\chi(f(P)g(P)).
\]

The three quadratic quotient fiber sizes are respectively

```text
1+chi(f),
1+chi(g),
1+chi(fg).
```

Summing over the common base gives the exact good-reduction identity

\[
\boxed{
\#X_{joint}(\mathbf F_q)
=
\#X_{face}(\mathbf F_q)
+
\#X_{sp}(\mathbf F_q)
+
\#X_{cross}(\mathbf F_q)
-2\#Y(\mathbf F_q),
}
\]

for compatible normal cover models (and equivalently on the common unramified/branch-compatible open before boundary corrections are reattached).

This is the finite-field shadow of the `V4` character decomposition: the three nontrivial characters of the deck group are carried by the three quadratic quotients.

## Covariance interpretation

Writing

```text
S_f(q)=sum_P chi(f(P)),
S_g(q)=sum_P chi(g(P)),
S_fg(q)=sum_P chi(f(P)g(P)),
```

one has

```text
#X_face  = #Y + S_f,
#X_sp    = #Y + S_g,
#X_cross = #Y + S_fg,
#X_joint = #Y + S_f + S_g + S_fg.
```

Thus the **entire new joint local term** beyond the two marginals is the cross-quotient trace `S_fg`.

This upgrades the 29-02 screening observation from a pointwise indicator identity to an exact global finite-field cover identity.

## New bridge to endpoint L-functions

Because `X_joint` is birational to the full perfect-cuboid endpoint and the two marginal quotients are K3 surfaces, the identity suggests a cohomological receiver:

```text
R29-L2=V4CohomologyDecompositionAndCrossQuotientLFunctionAdapter
```

The later 29-02e / 29-09 work should compare:

1. Horie--Yamauchi's computed `H^2` / L-function of the full cuboid surface;
2. the Euler-K3 quotient contribution;
3. the space-K3 quotient contribution;
4. the residual cross-quotient representation.

If all model/bad-prime/Tate corrections are aligned, the cross quotient may be recoverable cohomologically by subtraction rather than by a new broad point-count search.

## Firewalls

```text
FINITE_FIELD_V4_IDENTITY_EXACT=true
CROSS_TRACE_IS_JOINT_COVARIANCE_TERM=true
GLOBAL_RATIONAL_POINT_COUNT_FROM_LOCAL_TRACES=false
EULER_PRODUCT_TO_PHYSICAL_PERFECT_CUBOID_COUNT=false
BAD_PRIME_AND_MODEL_CORRECTIONS_STILL_REQUIRED=true
```
