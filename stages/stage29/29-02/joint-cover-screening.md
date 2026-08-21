# Stage29-02 — joint cover and cross quotient screening note

```text
ROLE=EXACT_FUNCTION_FIELD_SCREENING
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## Common-base input

Use the audited Stage28 common two-face base

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad K=\overline{\mathbf Q}(Y).
\]

The two completion covers are

\[
K_{face}=K(\sqrt{f}),\qquad f=t_1^2+t_2^2,
\]
\[
K_{sp}=K(\sqrt{g}),\qquad g=1+t_1^2+t_2^2.
\]

Stage28 proves that `f/g` is not a square in `K`, hence the two quadratic extensions are distinct.

## Degree-four compositum

Because both extensions are quadratic and distinct,

\[
[K(\sqrt f,\sqrt g):K]=4.
\]

The compositum has the three nontrivial quadratic subfields

\[
K(\sqrt f),\qquad K(\sqrt g),\qquad K(\sqrt{fg}).
\]

The third one is the cross quotient

\[
K_{cross}=K\!\left(\sqrt{(t_1^2+t_2^2)(1+t_1^2+t_2^2)}\right).
\]

This field is forced by the algebra of two independent quadratic completion predicates; it is not an extra conjectural family.

## Endpoint semantics

Over the common two-face host, the joint cover records simultaneous choices

\[
u^2=f,\qquad v^2=g.
\]

Thus a base point lifts to the joint cover precisely when both completion predicates are satisfied over the same base point.  This is the direct Stage29 endpoint semantics.  Primitivity, canonical physical chamber and `R<=B` remain separate physical adapters and are not erased by the function-field construction.

## Cross branch support

Stage28 certifies

```text
D_sp   : 4 geometric genus-0 components, total class -2K_Y
D_face : 2 geometric genus-1 components, total class -2K_Y
```

No irreducible component can be common to the two reduced branch supports because a single geometric irreducible curve cannot simultaneously have genus zero and genus one.  Therefore the odd divisor support of `fg` is the union of the two supports and has

```text
D_cross components = 6
D_cross genus multiset = {0,0,0,0,1,1}
D_cross class = -4K_Y
```

The standard double-cover line bundle corresponding to the cross radicand is therefore expected to be `-2K_Y`.  The formal canonical expression on the normal double cover is

\[
K_{X_{cross}}\sim \pi^*(K_Y-2K_Y)=\pi^*(-K_Y).
\]

However, Stage29-02 does **not** certify the minimal-resolution Kodaira type or invariants.  Branch intersections, normalization and resolution corrections must be audited in 29-07 before any `GENERAL_TYPE=true` statement is allowed.

```text
CROSS_CANONICAL_SIGNAL=pi^*(-K_Y)_BEFORE_RESOLUTION_AUDIT
CROSS_GENERAL_TYPE_PROVED=false
JOINT_COVER_GENERAL_TYPE_PROVED=false
```

## Local character identity

For every good odd prime and every base point away from zeros/poles of `f,g`, with quadratic character `chi`,

\[
\mathbf 1_{f\in(\mathbf F_p^*)^2,\ g\in(\mathbf F_p^*)^2}
=\frac14(1+\chi(f))(1+\chi(g)).
\]

Expanding,

\[
\mathbf 1_{both}
=\frac14\{1+\chi(f)+\chi(g)+\chi(fg)\}.
\]

Hence the third character `chi(fg)` is the exact extra datum needed to pass from two marginal square tests to their simultaneous correlation.  Geometrically it is the character attached to the cross quotient.

This identity is local and exact.  It does not justify an Euler product for the global perfect-cuboid count.

```text
JOINT_LOCAL_CROSS_TERM_EXACT=true
GLOBAL_PRODUCT_INFERENCE_ALLOWED=false
```
