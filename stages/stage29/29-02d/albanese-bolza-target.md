# Stage29-02d — Albanese / Bolza arithmetic target

```text
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Geometric tower

For the cuboid specialization `C=C'=C0`, Beauville's Remark 2 gives

```text
C0 x C0 -> X_B -> D x D,
```

where

```text
D: s^2=t(t^4-1)
```

is the genus-two Bolza curve and the second map is an etale `(Z/2)^2` cover. It is the pullback of an etale `(Z/2)^2` cover

```text
A_B -> J_D x J_D,
```

with `A_B` the geometric Albanese fourfold of `X_B`.

## 2. Descent action

The Q(i)/Q cocycle from the standard cuboid Q-form is induced by factor exchange on `C0 x C0`. On the quotient tower it therefore exchanges the two `D` factors and the two `J_D` factors.

The swap-twist of `D x D` by `Gal(Q(i)/Q)` is the standard descent object

```text
Res_{Q(i)/Q}(D_{Q(i)}),
```

and the corresponding swap-twist of `J_D x J_D` is

```text
Res_{Q(i)/Q}(J_D,Q(i)).
```

For the V4 isogeny `A_B -> J_D x J_D`, the exact equivariance of the kernel under the swap cocycle should be checked before promoting the twisted isogeny over Q. This is retained as a bounded receiver rather than assumed.

```text
R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel
```

If it passes, the descended/twisted Albanese fourfold is Q-isogenous to the above Weil restriction.

## 3. The Bolza Jacobian is arithmetically special

Beauville 2014 Proposition 8 identifies geometrically

```text
End(J_D) tensor Q = M_2(Q(sqrt(-2))),
```

so `J_D` is geometrically a square of a CM elliptic curve.

But the arithmetic field matters. Fite--Sutherland 2014 Section 4 explicitly records that the Bolza model

```text
y^2=x^5-x
```

does not have Jacobian Q-isogenous to the square of an elliptic curve over Q, and that the full endomorphism field is

```text
Q(i,sqrt(-2)).
```

They also exhibit the Q-twist

```text
C2^0: y^2=x^6-5x^4-5x^2+1
```

with

```text
Jac(C2^0) ~_Q (E2^0)^2,
E2^0: Y^2=X^3-5X^2-5X+1,
CM field Q(sqrt(-2)).
```

Therefore the Beauville route reaches a highly structured CM/twist arithmetic target, but not a single fixed elliptic curve over Q without further descent.

## 4. New exact arithmetic receiver

The route now separates into two stages:

```text
surface lift squareclass delta
    -> Beauville twist X^delta
    -> descended Albanese torsor / fourfold A^delta
    -> Bolza-Jacobian / CM-elliptic twist arithmetic.
```

This is materially different from the Stage29 joint-V4 branch-profile route.

The next theorem-level receiver is

```text
R29-BEAU3=BolzaJacobianCMQCurveTwistDescentForBeauvilleEndpointCovers
```

It must answer:

1. Which genus-two/Jacobian twist is induced by a given Beauville cover class `delta`?
2. Over which minimal field does the induced Jacobian split as a CM elliptic square?
3. Can local solubility or Selmer conditions eliminate all but a controlled set of `delta`?
4. Can the Albanese image of `X^delta(Q)` be reduced to explicit Mordell-Weil/Selmer data?
5. Is the resulting control uniform in the physical height, rather than family-specific?

## Firewalls

```text
GEOMETRIC_CM_DECOMPOSITION_IMPLIES_Q_SPLITTING=false
ALBANESE_MAP_IMPLIES_RATIONAL_POINT_FINITE=false
FINITE_NUMBER_OF_TWISTS_PROVED=false
CM_IMPLIES_ENDPOINT_OBSTRUCTION=false
OLD_STAGE_REPLAY=false
PERFECT_CUBOID_CONCLUSION=NONE
```
