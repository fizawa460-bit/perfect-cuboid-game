# Stage32 MB104 — `000707000f0f` e=2 split Hodge/conductor bound

Status: **RETAINED QUADRATIC CONDUCTOR-ALLOCATION CONSTRAINT / e=2 NOT CLOSED / e=4 OPEN / NO CREDIT**

## Scope

Continue the dangerous equality packet on `000707000f0f` and use the retained half-branch class

```text
2L_abs ~ B_abs,
B_abs = sum of the 16 absent-type exceptional curves.
```

Let

```text
pi:Y->S
```

be the double cover defined by `L_abs`, branched along `B_abs`.  The branch curves are disjoint smooth `(-2)`-curves, so `Y` is smooth.  The candidate carrier `C in |D_l|` is disjoint from `B_abs`; therefore `pi` is etale in a neighborhood of `C` and

```text
Ctilde := pi^{-1}(C) -> C
```

is a finite etale double cover of the singular carrier.

On the normalization `E` of `C`, the pullback is the residual cover classified by

```text
eta=L_abs|_E in Pic^0(E)[2].
```

Thus the retained case split says

```text
e=2 <=> eta=0,
e=4 <=> eta!=0.
```

## 1. What eta=0 means on the singular preimage

Assume `e=2`, hence `eta=0`.  The normalization of `Ctilde` is then

```text
E disjoint-union E.
```

The singular curve `Ctilde` need not itself be disconnected: conductor identifications at singular points of `C` can glue the two normalization sheets crosswise.  Therefore one must not infer two disjoint global curves from `eta=0`.

Nevertheless `Ctilde` has exactly two irreducible components

```text
C_1, C_2
```

exchanged by the deck involution, each with normalization `E`.  Write

```text
y := C_1.C_2 >= 0.
```

The number `y` measures cross-sheet conductor intersection on the smooth ambient surface `Y`.

## 2. Self-intersections of the two components

Because

```text
pi^* C = C_1 + C_2
```

and `pi|_(C_j)` has generic degree one, projection formula gives

```text
(pi^*C).C_1 = C^2.
```

By symmetry `C_1^2=C_2^2`, hence

```text
C_1^2 + y = C^2,
C_1^2=C_2^2=C^2-y.
```

For the uniform ray,

```text
C^2=D_l^2=336l^2.
```

## 3. Hodge-index lower bound on cross-sheet gluing

Choose any ample divisor `A` on `S`.  Its pullback `pi^*A` is ample on `Y`.  Since `C_1` and `C_2` have the same pushforward class,

```text
(C_1-C_2).pi^*A=0.
```

Hodge index on the smooth projective surface `Y` therefore gives

```text
(C_1-C_2)^2 <= 0.
```

But

```text
(C_1-C_2)^2
 = C_1^2+C_2^2-2C_1.C_2
 = 2(C^2-y)-2y
 = 2C^2-4y.
```

Hence

```text
y >= C^2/2 = 168l^2.                       (H)
```

This is a genuinely quadratic constraint forced only in the split-normalization case `e=2`.

## 4. Relation to the total conductor budget

Adjunction on `S` gives

```text
p_a(C)=1+(D_l^2+K.D_l)/2
      =168l^2+56l+1.
```

The normalization genus is one, so the total delta invariant is

```text
Delta(C)=p_a(C)-1=168l^2+56l.
```

Since `Ctilde->C` is etale of degree two, its total normalization defect is twice that amount.  If `delta_same` is the normalization defect carried internally by either component (the two are exchanged by the involution), then

```text
2 Delta(C) = 2 delta_same + y,
```

so

```text
Delta(C)=delta_same+y/2.
```

Combining with `(H)` gives

```text
y/2 >= 84l^2,
delta_same <= 84l^2+56l.
```

Thus `e=2` requires at least `84l^2` of the downstairs delta budget, measured in this normalized cross-sheet sense, to participate in nontrivial sheet gluing.

## 5. What this does and does not prove

This does **not** contradict the known total delta budget: the budget is itself quadratic.  It does, however, give a new target for the global singularity/conductor route.  Any independent upper bound

```text
y < 168l^2
```

on cross-sheet conductor intersection would exclude `e=2` and force the nonzero residual character `e=4`.

The previously retained Lu--Miyaoka lower bound is only linear in `l` and therefore does not by itself provide such an upper bound.

## Next lever

Combine `(H)` with explicit singularity/conductor information for a degree-`112l` carrier.  Useful inputs would be:

- a local bound of cross-sheet intersection in terms of delta/conductor type, together with a global restriction on those singularity types;
- a global upper bound for conductor supported on the nontrivial residual sheet character;
- an exact modular/commensurator monodromy computation that determines the sheet gluing directly.

## Firewalls

- `e=2` is not excluded.
- `e=4` is not excluded.
- No claim is made that `eta=0` makes the singular preimage disconnected; conductor gluing is explicitly retained.
- No conversion of ordinary-node/triple lower bounds into a quadratic contradiction is claimed.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
