# Stage25-60 R504 exceptional base-change search

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

The general degree-two search is normalized, modulo source PGL2, by
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1},\qquad a\ne b.
\]
The target coordinate is fixed by `k^4+1`, so the generic branch-value space is two-dimensional, not one-dimensional. The earlier one-dimensional wording is superseded.

The pullback twist cover is
\[
C_{a,b}: y^2=(a u^2+b)^4+(u^2+1)^4.
\]
Its involution `u->-u` gives the inherited quotient birational to `s^2=k^4+1` and hence the inherited `E0` factor.

Writing
\[
Q_{a,b}(x)=(ax+b)^4+(x+1)^4=A x^4+B x^3+C x^2+D x+E,
\]
with
\[
A=a^4+1,\ B=4(a^3b+1),\ C=6(a^2b^2+1),\ D=4(ab^3+1),\ E=b^4+1,
\]
a second Q-rational reciprocal involution `u->lambda/u` requires
\[
D=L B,\qquad E=L^2A,\qquad L=\lambda^2.
\]
Elimination gives the exact condition
\[
\boxed{E B^2-A D^2=16(a-b)^3(a+b)(ab-1)(ab+1).}
\]
Thus the extra-involution locus is completely explicit. `a=b` is the constant-map degeneration. For a Q-rational involution, the nondegenerate loci are `a=-b` and `ab=1`; the factor `ab=-1` has `L=-a^{-2}` and does not define a Q-rational reciprocal involution.

On `a=-b`, the complementary elliptic quotient has
\[
I=64a^4(4a^4+3),\qquad J=-1024a^8(8a^4+9),
\]
so no nonzero rational `a` gives `J=0` and hence no complementary `j=1728` factor.

On `ab=1`, with `b=1/a`, the complementary quotient has
\[
I=8(a-1)^4(5a^4+4a^3+6a^2+4a+5)/a^2,
\]
\[
J=-64(a-1)^8(a^2+a+1)(7a^2+10a+7)/a^3.
\]
The two quadratic factors have negative discriminant, while `a=1` is the constant-map degeneration. Again there is no nondegenerate rational `J=0` point.

Therefore the entire Q-rational extra-involution / bielliptic quotient locus of the normalized generic degree-two family is closed symbolically:

```text
R504_GENERAL_DEGREE2_NORMAL_FORM=phi_(a,b)(u)=(a*u^2+b)/(u^2+1)
R504_GENERAL_DEGREE2_PARAMETER_DIMENSION=2
R504_PREVIOUS_ONE_DIMENSION_BRANCH_CLAIM=SUPERSEDED
R504_GENERAL_EXTRA_INVOLUTION_LOCUS=(a-b)^3*(a+b)*(ab-1)*(ab+1)=0
R504_Q_RATIONAL_EXTRA_INVOLUTION_NONDEGENERATE_LOCI=a_plus_b_zero;ab_equal_1
R504_EXTRA_INVOLUTION_DEGREE2_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
```

This does not classify all possible elliptic factors of `J(C_(a,b))`: an additional factor Q-isogenous to `E0` could arise through a higher-degree map without a second curve involution. The remaining live object is therefore the two-dimensional Prym/isogeny locus, not another unexecuted involution ansatz:

```text
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_PRYM_ISOGENY_LOCUS
R504_RESIDUAL=NON_BIELLIPTIC_E0_ISOGENY_FACTOR_LOCUS_IN_PRYM_SURFACE
R504_GENERAL_DEGREE2_FULL_RANK_JUMP_CLASSIFICATION_PROVED=false
R504_NEW_RANK_JUMP_PROVED=false
R504_NEW_STAGE19_FAMILY_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

Previously closed candidates remain frozen: BC1/BC2 audited no-rank-jump, BC3/BC4 exact `J=+-1024*a*(8*a^2+9)`, BC5 complementary `j=8000,8000`, and growing multiples audited `o(B^(1/4))`.

NEXT_ATTACK=PRYM_HUMBERT_E0_ISOGENY_FACTOR_LOCUS
