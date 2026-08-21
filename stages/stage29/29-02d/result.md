# Stage29-02d — Beauville irregular cover Q-descent

```text
TASK=Stage29-02d
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
ROLE=NEW_FOUNDATION_DEEPENING
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

The Beauville route survives arithmetic descent. The cuboid specialization is naturally written as Beauville's Q-model `Sigma_B`; its linear identification with the standard cuboid surface uses `i`, but the resulting `Q(i)/Q` descent cocycle is explicit and lifts to the smooth Beauville surface.

The standard cuboid Q-form is obtained from the cocycle

```text
Y <-> Z
```

on Beauville's canonical quotient. On

```text
X_B=(C0 x C0)/Gamma,
C0: u^2=xy, v^2=x^2-y^2, w^2=x^2+y^2,
```

factor exchange `(p,q)<->(q,p)` is Q-defined, commutes with the diagonal `Gamma`, and induces exactly the `Y<->Z` action on canonical sections. Therefore Galois descent produces

```text
q_cub:X_cub -> S_cub
```

over Q whose base change to `Q(i)` is Beauville's canonical degree-two cover.

The audit further checks that factor exchange commutes with the canonical deck involution induced by `Gamma_+/Gamma`. Hence the descended free smooth-locus cover has constant deck group `Z/2` over Q.

```text
R29-BEAU1A=BeauvilleCanonicalDoubleCoverStandardCuboidQFormAdapter
STATUS=DISCHARGED_BY_PR1297_AUDIT
Q_FORM_COVER_EXISTS=PASS_AUDITED
DESCENT_COCYCLE=Y_Z_SWAP
COCYCLE_LIFT=FACTOR_SWAP
DECK_INVOLUTION_DESCENDS=true
```

## Exact Q(i) coordinate bridge

Beauville's quotient coordinates satisfy

```text
XT=YZ=U^2,
V^2=X^2-Y^2-Z^2+T^2,
W^2=X^2+Y^2+Z^2+T^2.
```

The standard cuboid coordinates are obtained over `Q(i)` by

```text
X=x+t, T=t-x,
Y=y+i z, Z=y-i z,
U=u, V=2v, W=2w.
```

For a standard Q-rational point, complex conjugation fixes all transported Beauville coordinates except that it exchanges `Y` and `Z`.

## Rational-point descent is a twist family

On the positive nondegenerate smooth physical open `U_phys`, the descended canonical cover is finite etale degree two with constant deck group `Z/2`. Therefore every

```text
P in U_phys(Q)
```

determines a torsor class

```text
delta(P) in H^1(Q,Z/2) ~= Q^*/Q^{*2}.
```

It lifts to a rational point on the corresponding quadratic twist `X^delta`, not necessarily on the untwisted `X_cub`. Thus

```text
U_phys(Q)
 = union_delta image(X_U^delta(Q) -> U_phys(Q)).
```

No finite twist set is proved. The remaining lift receivers are

```text
R29-BEAU1B=ExplicitGenericBeauvilleDoubleCoverSquareclassFunction
R29-BEAU1C=PhysicalEndpointLiftSquareclassLocalRamificationLedger
```

## Albanese / Bolza arithmetic target

Beauville's **Remark 1** gives geometrically

```text
C0 x C0 -> X_B -> D x D,
D: s^2=t(t^4-1),
```

and an Albanese fourfold with an etale `(Z/2)^2` isogeny to `J_D x J_D`. Factor exchange swaps the two factors, so the natural descended target is the swap twist / Weil restriction

```text
Res_{Q(i)/Q}(J_D,Q(i)).
```

The exact swap-equivariance of the V4 isogeny kernel is not promoted here and remains

```text
R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel.
```

The genus-two curve `D` is the Bolza curve. Beauville 2014 Proposition 8 and its proof give

```text
End(J_D) tensor Q = M_2(Q(sqrt(-2)))
```

geometrically. Fite--Sutherland 2014 supplies the arithmetic firewall: `y^2=x^5-x` itself does not have Jacobian Q-isogenous to a square of a Q-elliptic curve and its full endomorphism field is `Q(i,sqrt(-2))`; the Q-twist

```text
y^2=x^6-5x^4-5x^2+1
```

has Jacobian Q-isogenous to the square of

```text
Y^2=X^3-5X^2-5X+1
```

with CM by `Q(sqrt(-2))`.

The route therefore narrows to explicit twist/Selmer/Mordell-Weil arithmetic rather than a generic Albanese argument.

## Residual receivers

```text
R29-BEAU1B=OPEN
R29-BEAU1C=OPEN
R29-BEAU2A=OPEN_BOUNDED
R29-BEAU2=LocallySolubleBeauvilleTwistsToAlbaneseTorsors
R29-BEAU3=BolzaJacobianCMQCurveTwistDescentForBeauvilleEndpointCovers
```

## Bounded audit repairs

1. Beauville's etale tower/Albanese statement is in `Remark 1`, not `Remark 2`.
2. The deck involution descent was made explicit so the `H^1(Q,Z/2)` fiber classification is fully justified over Q.

No main route conclusion changes.

## Applicability / routing verdict

This route remains materially new and HIGH_VALUE, but it is not yet an endpoint obstruction.

```text
EVERY_Q_ENDPOINT_LIFTS_UNTWISTED=false
FINITE_TWIST_SET_PROVED=false
V4_KERNEL_SWAP_EQUIVARIANCE_AUDITED=false
ALBANESE_RATIONAL_POINTS_CONTROLLED_UNIFORMLY=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02e
NEXT_EXPECTED_COMMAND=Stage29-main-batch
```
