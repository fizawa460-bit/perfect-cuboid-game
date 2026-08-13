# Stage14-X13 addendum — merged s7-41 quantifier bridge closure

This addendum is canonical with `stages/stage14/14-X13/result.md` after synchronizing merged `Stage14-s7-41` into the X13 branch.

Merged s7-41 correctly proves that

```text
first residual support  <-> twin-short support
```

is only a `B^o(1)`-finite change of coordinates at the old `23/44` endpoint, and therefore the two descriptions cannot be multiplied as independent savings.  It also records

```text
REVERSE_ROOT_LINE_REUSE_WITHOUT_QUANTIFIER_BRIDGE_ALLOWED=false
```

and opens an s-specific H gate because no merged bridge was then available.

X13 does **not** reuse the common-core root-line spacing in reverse.  It supplies a different exact bridge after the legal forward quantifier order has already fixed the primitive pair `(U,V)` and the endpoint-linear column has reconstructed `M`.

With endpoint-small/2-primary decoration fixed,

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k
```

fixes `X*Y`.  The second exact reciprocal equation becomes

```text
(c*p)^2-(d*q)^2
 = 4*X*Y*epsilon_x*U*V =: W_2.
```

Since `cp=Q+P`, `dq=Q-P`, `Q>P>0`,

```text
(cp-dq)(cp+dq)=W_2.
```

A fixed `W_2` has divisor-many positive factor pairs; those recover `cp,dq`, and divisor factorization recovers `(c,p,d,q)` with `B^o(1)` multiplicity.

Then the first reciprocal equation becomes

```text
(a*U)^2-(b*V)^2
 = 4*r*s*epsilon_k*p*q =: W_1,
```

so

```text
(aU-bV)(aU+bV)=W_1.
```

Again divisor factorization recovers `(a,b)` with `B^o(1)` multiplicity because `(U,V)` is already fixed.

Therefore

```text
fixed (U,V,M)
=> # {(a,b,c,d,p,q)} = B^o(1)
=> # {N=a*b*c*d} = B^o(1).
```

The Cayley row congruence is consequently only a filter on these divisor-many `N` candidates.  No second root-line density is invoked, and the s7-41 no-double-saving rule is respected.

This is precisely the quantifier bridge absent at the s7-41 snapshot:

```text
S7_41_NO_DOUBLE_SAVING_RULE_RESPECTED=true
S7_41_REVERSE_ROOT_LINE_REUSED=false
X13_DISTINCT_REVERSE_RECIPROCAL_QUANTIFIER_BRIDGE_PROVED=true
S7_41_MISSING_QUANTIFIER_BRIDGE_CLOSED_ON_X_ROUTE=true
S7_41_H_GATE_REQUIRED_FOR_X13_SQRT_BOUND=false
```

Consequently the X13 complete count remains

```text
E_RRF <= 2*phi + 1/4 - chi = 1 - 2*theta,
```

and the whole-family theorem remains

```text
V(B) << B^(1/2+o(1)).
```

The s7-41 auxiliary H may still be studied as an independent route toward a strict sub-square-root saving, but it is no longer required to reach the square-root upper bound once X13 is merged.
