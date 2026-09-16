# Stage32 MB104 — `000707000f0f` e=2 square-root factor base-change semantics

Status: **RETAINED SEMANTIC CORRECTION / SQRT SIGN TRANSPORT FACTORS THROUGH RESIDUAL BASE COVER / NO CONDUCTOR SIGN COUNT / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the explicit Kummer representative

```text
f_t=(t-i)/(t+i)
```

on

```text
R=C8/H ~= P1.
```

The residual quotient

```text
q:R -> S=R/(G/H)=C8/G ~= P1
```

is the degree-two cover branched at the two absent-type points. The retained residual-sheet leaf constructs, in both surviving cases, a degree-`56l` map

```text
phi:E -> S
```

from the normalization of the hypothetical carrier.

This note fixes the semantic level of the square-root transport problem: the relevant residual character is the pullback of the **base-cover class of q**, not an independently chosen rational function on `E`.

## 1. Base-cover function

Choose a rational function

```text
h in k(S)^*
```

whose square root generates the quadratic extension

```text
k(R)=k(S)(sqrt(h)).
```

Equivalently, after choosing coordinates on `S~=P1`, `h` has odd valuation at the two branch values of `q` and even valuation elsewhere.

The normalized residual base change is

```text
T=Norm(E x_(S,phi) R),
```

and therefore its function-field class is

```text
[h o phi] in k(E)^*/k(E)^{*2}.                (BASE)
```

The retained half-fiber calculation gives

```text
div(h o phi)=2A-2B
```

up to adding the divisor of a square, and the corresponding etale double cover is classified by

```text
eta=O_E(A-B) in Pic^0(E)[2].
```

Thus

```text
e=2 <=> [h o phi]=1,
e=4 <=> [h o phi]!=1.                         (CASE)
```

## 2. Relation with the factor representative f_t

The previous explicit-function leaf proves on the surface complement that the ambient half-branch torsor is represented by

```text
[f_t],  f_t=(t-i)/(t+i).
```

The residual modular cover `q:R->S` is the same degree-two quotient encoded by the absent stabilizer type. Consequently, after pulling through the actual factor/modular map, the two descriptions must agree as square classes:

```text
[f_t|_E]=[h o phi] in k(E)^*/k(E)^{*2}.        (MATCH)
```

Statement `(MATCH)` is a square-class identity. It does **not** identify the rational functions literally, and it does not permit replacing the residual base-cover class by an arbitrary function on `E`.

## 3. Correct e=2 square root

Assume `e=2`. By `(CASE)`, choose

```text
w in k(E)^*,
w^2=h o phi.
```

By `(MATCH)`, after multiplying by a rational square one may equivalently work with a square root of `f_t|_E`. The conductor sign attached to an identification pair is the descent sign of this **pulled-back residual-cover square root**.

Hence the active transport object is

```text
sqrt(h o phi)
```

or any explicitly verified square-equivalent lift such as `sqrt(f_t|_E)`.

This preserves the residual-sheet semantics:

```text
R=C8/H --q--> S=C8/G,
E --phi--> S,
T=Norm(E x_S R).
```

## 4. What is still missing

The current repository data determine the square class and its zero/nonzero status for `e=2/e=4`, but do not yet provide an explicit formula assigning the two limiting values of `w` to every pair of normalization branches identified in the singular carrier.

Therefore no count of opposite-sign conductor intersections follows yet.

The next load-bearing input must be an explicit modular/product-cover lift that maps a conductor branch preimage to a point of `R=C8/H` above `phi(x)in S`, so that the two lifts can be compared under the deck involution of `q`.

## 5. Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP
```

Target: construct the branch-preimage-to-`R` lift map at conductor identifications and determine whether the two preimages land on the same or opposite sheets of `q`. Only after this map is explicit may the weighted opposite-sheet sum be compared with `84l^2`.

## Firewalls

- No literal equality `f_t|_E=h o phi` is claimed; only square-class equality.
- No arbitrary choice of a base function on `E` is allowed.
- No conductor pair is assigned a sign here.
- No upper bound for `y` is proved.
- `e=2` and `e=4` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
