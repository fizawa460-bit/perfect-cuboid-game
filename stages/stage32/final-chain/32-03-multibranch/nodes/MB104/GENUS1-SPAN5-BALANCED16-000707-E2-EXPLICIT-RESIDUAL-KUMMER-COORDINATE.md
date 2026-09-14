# Stage32 MB104 — `000707000f0f` e=2 explicit residual Kummer coordinate

Status: **RETAINED RESIDUAL-COVER COORDINATE REFINEMENT / ABSTRACT `q:R->S` KUMMER CLASS MADE EXPLICIT / CONDUCTOR PREIMAGE EVALUATION STILL MISSING / e=2 OPEN / NO CREDIT**

## Scope

Continue the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained boundary has

```text
R=C8/H,
S=C8/G,
q:R->S,
G~= (Z/2)^3,
H=<s1,s2>,
```

where the support uses the `b1=0` and `b2=0` singular types and the absent type is `b3=0`.

The previous retained square-root note knew only that the residual cover could be written abstractly as `sqrt(h)` and that its pullback class on the normalization agrees with `[f_t]`. This refinement makes the one-factor residual extension itself explicit.

## 1. Identify the active subgroup in the theta sign basis

Use the source-locked generator basis `(T,T',R)` of `G=Gamma[4]/Gamma[8]`.

From the theta sign matrices:

```text
b3=Z3=0  <->  T,
b1=Z1=0  <->  T',
b2=Z2=0  <->  TT'R.
```

Hence, for the active `000707` support,

```text
s1=T',
s2=TT'R,
s3=T,
H=<T',TT'R>.
```

The residual nontrivial class in `G/H` is represented by `T H`.

## 2. The retained factor character is a base function

For the second factor write

```text
X=theta00(2w),
Y=theta10(2w).
```

The retained factor coordinate is

```text
t=(C+W1)/(W2+i*W3).
```

Substituting the exact theta parametrization gives

```text
C+W1=(x+y)(X+Y),
W2+i*W3=i*(x+y)(X-Y),
t=-i*(X+Y)/(X-Y).
```

Therefore

```text
f_t=(t-i)/(t+i)=X/Y.                           (FT)
```

By the theta sign action, both `X` and `Y` are fixed by `T,T'` and both are negated by `R`. Thus their ratio is fixed by all of `G`. Consequently `f_t` is literally a rational function on the base

```text
S=C8/G,
```

not merely a square class after pullback to a carrier.

## 3. A semi-invariant square root generates `k(R)/k(S)`

Put

```text
E10=theta10(w),
r0=E10/Y.
```

The theta identity gives

```text
E10^2=2XY,
```

hence

```text
r0^2=2*X/Y=2*f_t.                              (KUM)
```

Its sign character on `(T,T',R)` is

```text
chi(r0)=(-,+,-).
```

Therefore

```text
chi(T')=+1,
chi(TT'R)=(-)*(+)*(-)=+1,
chi(T)=-1.
```

So `r0` is invariant under `H=<T',TT'R>` but not under `G`. Since `[G:H]=2`, it generates the residual quadratic extension:

```text
k(R)=k(S)(r0),
r0^2=2*f_t,
T H : r0 -> -r0.                               (RES)
```

Equivalently, over the complex field one may normalize

```text
rho=r0/sqrt(2)
```

and write

```text
rho^2=f_t,
T H : rho -> -rho.
```

The exact algebraic equation `(RES)` is retained without needing this scalar normalization.

## 4. Consequence for the active e=2 conductor problem

In the `e=2` case the retained map

```text
psi:E->R
```

has degree `28l`. The residual sheet coordinate at a normalization point `x in E` can therefore be represented explicitly by

```text
r0(psi(x)),
```

whose square is

```text
2*f_t(phi(x)).
```

For a conductor-identified pair `(x_i,x_j)`, the fixed residual character is now exactly the relative sign under

```text
r0(psi(x_i))  versus  r0(psi(x_j)).
```

Thus one of the three forms of the previous information wall has been sharpened:

```text
abstract sqrt(h o phi)
    -> explicit theta semi-invariant r0=theta10(w)/theta10(2w)
       with r0^2=2*f_t and residual deck action r0->-r0.
```

What remains missing is not the equation of the residual double cover. It is the source-locked evaluation of `psi` (equivalently `r0 o psi`) on the two normalization preimages participating in each conductor identification.

## 5. No conductor sign follows yet

The boundary-fiber saturation still gives, for each used zero quartic in the `e=2` case, two full reduced `R`-fibres of size `28l`, but it does not say which branch at a given supported node occupies which `r0` value.

Therefore this refinement does **not** assign a conductor sign and does not provide an upper bound for

```text
sum_p sum_(i<j) I_p(beta_i,beta_j)*alpha_abs(lambda_(p;i,j)).
```

The retained Hodge threshold `>=84*l^2` is unchanged.

## Firewalls

- No conductor normalization preimage is assigned an `r0` value.
- No identity or deck-twisted conductor gluing is asserted.
- No weighted-cut upper bound is claimed.
- The scalar normalization by `sqrt(2)` is used only over `C`; no `Q(i)` square claim for `2` is made.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
