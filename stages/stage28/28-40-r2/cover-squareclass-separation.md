# Stage28-40-r2 — quadratic-cover squareclass separation

```text
ROUTE=U13_COVER_SQUARECLASS_SEPARATION
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Let `K=Qbar(Y)` for the common two-face base.  The two completion covers have function fields

\[
K_{\rm face}=K\left(\sqrt{t_1^2+t_2^2}\right),
\qquad
K_{\rm sp}=K\left(\sqrt{1+t_1^2+t_2^2}\right).
\]

Two quadratic extensions of `K` are equal if and only if the quotient of their radicands is a square in `K^*`.

The r2 branch decomposition proves that the odd branch divisor of the space radicand has four geometric rational components, while the odd branch divisor of the third-face radicand has two geometric genus-one components.  In particular the mod-2 divisor supports are not equal.

If

\[
\frac{1+t_1^2+t_2^2}{t_1^2+t_2^2}
\]

were a square in `K`, every divisorial valuation of the quotient would be even, so the two branch divisors would agree modulo `2`.  They do not.  Hence

\[
\boxed{
\frac{1+t_1^2+t_2^2}{t_1^2+t_2^2}
\notin K^{*2}.
}
\]

Therefore

\[
\boxed{K_{\rm sp}\neq K_{\rm face}}
\]

as quadratic extensions of the fixed base function field.

Combined with the component-profile invariant, no automorphism of `Y_Qbar` can conjugate one branch divisor to the other.  Thus the Stage19 and Stage20 covers are genuinely distinct degree-two cover structures, not two presentations related by a base automorphism or by a hidden square rescaling of the radicand.

```text
RADICAND_RATIO_SQUARE=false
SAME_QUADRATIC_EXTENSION_OVER_FIXED_BASE=false
BASE_PRESERVING_BIRATIONAL_EQUIVALENCE=false
BASE_AUTOMORPHISM_CONJUGACY=false
```

Firewall: this is a statement about the two cover structures over `Y`.  It does not prove that the resolved K3 surfaces are abstractly non-isomorphic or non-birational after forgetting their maps to `Y`.

```text
ABSTRACT_K3_NONISOMORPHISM_PROVED=false
ABSTRACT_K3_NONBIRATIONALITY_PROVED=false
COUNTING_ORDERING_PROVED=false
```
