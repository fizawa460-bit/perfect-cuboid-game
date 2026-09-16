# Stage32 MB104 — `000707000f0f` factor-character pair square wall

Status: **RETAINED EXACT ALGEBRAIC IDENTITY / ETA1=ETA2 AUTOMATIC / JOINT-CHARACTER-COMPARISON ROUTE EXHAUSTED / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the dangerous equality packet on

```text
Sigma=000707000f0f,
node-type counts=(7,7,0).
```

The absent singular type is `b3=0`.  The preceding residual-character/Picard leaves attach to the two product-induced factor fibrations two classes

```text
eta_1,eta_2 in Pic^0(E)[2]
```

and require `eta_1=eta_2` because they describe the same residual double cover.

This leaf proves that equality directly from the cuboid equations and shows that it gives no additional obstruction.

## 1. Complementary factor coordinates

On the canonical quadric

```text
a1^2+a2^2+a3^2=c^2
```

we have

```text
(c+a1)(c-a1)=(a2+i*a3)(a2-i*a3).
```

The two rulings can be written

```text
t=(c+a1)/(a2+i*a3)=(a2-i*a3)/(c-a1),

u=(c+a1)/(a2-i*a3)=(a2+i*a3)/(c-a1).
```

These are the two product-factor genus-five fibration coordinates retained in the Stoll--Testa adapter.

For either ruling the two bad values belonging to the absent `b3=0` singular type are

```text
+i and -i.
```

For example, setting `t=i` or `t=-i` in the ruling equations forces one of the two `b3=0` elliptic-quartic components; the two values give the two absent-type reduced bad fibers for that ruling.  The same holds for `u`.

## 2. Character representatives

For a double cover of the factor line whose two branch values are `+i,-i`, a square-class representative is

```text
f_t=(t-i)/(t+i),
f_u=(u-i)/(u+i).
```

Pulling these functions to the normalization `E` gives the two residual two-torsion classes `eta_1,eta_2` from the preceding leaf.

Substitution of the ruling coordinates gives

```text
f_t=(c+a1+a3-i*a2)/(c+a1-a3+i*a2),

f_u=(c+a1-a3-i*a2)/(c+a1+a3+i*a2).
```

## 3. Exact square identity

Using only

```text
c^2=a1^2+a2^2+a3^2
```

one obtains

```text
f_t/f_u=(c+a3)/(c-a3).
```

The cuboid equation

```text
b3^2=a1^2+a2^2=c^2-a3^2=(c+a3)(c-a3)
```

then gives

```text
f_t/f_u
  = (c+a3)/(c-a3)
  = ((c+a3)/b3)^2.
```

Thus the ratio of the two factor-character representatives is already a square in the function field of the cuboid surface.

Equivalently,

```text
[f_t]=[f_u]
```

in the function-field square-class group before restriction to any candidate carrier.

The same identity can also be written with the equivalent square-class representative

```text
(c+a3)/(c-a3) ~ (a1-i*a2)/(a1+i*a2)
```

because their ratio is itself a square by the same canonical-quadric relation.

## 4. Consequence for the residual character

A dangerous-packet carrier has degree `112l` and cannot be an irreducible component of `b3=0`, whose components are degree-four `G2` curves.  Hence the displayed rational functions restrict normally to its function field.

Therefore

```text
eta_1=eta_2
```

is automatic for every hypothetical carrier in the current scope.  It is not an extra incidence condition capable of distinguishing `e=2` from `e=4`.

The common class may be computed from either factor alone:

```text
eta := eta_1=eta_2.
```

The retained case classification remains

```text
e=2  <=> eta=0,
e=4  <=> eta!=0.
```

## Route consequence

The following route is now exhausted:

```text
try to contradict 000707 by proving eta_1 != eta_2.
```

The cuboid quadratic identities force equality identically.

The genuinely missing datum is one-factor square/non-square status:

```text
is f_t|_E a square in k(E)^* ?
```

or equivalently, in the surface-Picard form,

```text
is O_E((Q_a-Q_b)|_E) trivial or the nonzero two-torsion class?
```

Any next useful lever must decide that single class from the carrier geometry rather than compare the two factors.

## Firewalls

- The identity does not prove `f_t|_E` is itself a square.
- It does not close `e=2` or `e=4`.
- It does not close `000707000f0f`.
- No arbitrary-branch closure is obtained.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104, span5, receiver, theorem, endpoint, and Perfect-Cuboid credit remain zero.
- No merge authorization.
