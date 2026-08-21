# Stage29-02d — Beauville irregular cover Q-descent

```text
TASK=Stage29-02d
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ROLE=NEW_FOUNDATION_DEEPENING
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

The Beauville route survives arithmetic descent more strongly than the Stage29-02 Work intake established.

The published cuboid specialization is naturally written as a Q-model `Sigma_B` whose linear identification with the standard cuboid surface uses `i`. This is not a fatal field-of-definition mismatch. The Q(i)/Q descent cocycle is exactly the involution

```text
Y <-> Z
```

on Beauville's canonical quotient. That involution lifts to the smooth Beauville surface `X_B=(C0 x C0)/Gamma` as **factor exchange** on `C0 x C0`. Consequently the canonical degree-two cover itself descends, after twisting by this cocycle, to a Q-cover

```text
q_cub:X_cub -> S_cub
```

of the standard perfect-cuboid canonical model.

```text
BEAUVILLE_STANDARD_CUBOID_Q_FORM_ADAPTER=PASS_CANDIDATE
Q_FORM_COVER_EXISTS=PASS_CANDIDATE
DESCENT_COCYCLE=Y_Z_SWAP
COCYCLE_LIFT=FACTOR_SWAP
```

This is a new zero-loss field-of-definition adapter, subject to fresh audit.

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

For a standard Q-rational point, complex conjugation fixes all Beauville coordinates except that it exchanges `Y` and `Z`. Factor exchange on `C0 x C0` induces exactly that action on the seven canonical sections.

Full derivation: `q-form-adapter.md`.

## Rational-point descent is a twist family, not an untwisted lift

On the smooth positive nondegenerate physical open `U_phys`, the canonical double cover is finite etale of degree two. Therefore every

```text
P in U_phys(Q)
```

determines a fiber class

```text
delta(P) in H^1(Q,Z/2) ~= Q^*/Q^{*2}.
```

It lifts to a rational point on the corresponding quadratic twist `X^delta`, not necessarily on the untwisted `X_cub`.

Thus

```text
U_phys(Q)
 = union_delta image(X_U^delta(Q)).
```

No finite twist set is currently proved. The exact remaining lift receiver is to compute the generic squareclass function and its local ramification in physical coordinates.

Full ledger: `lift-twist-ledger.md`.

## Albanese target becomes explicit CM/twist arithmetic

Beauville's etale tower gives geometrically

```text
C0 x C0 -> X_B -> D x D,
D: s^2=t(t^4-1),
```

and an Albanese fourfold etale-isogenous to `J_D x J_D`. The Q(i)/Q cocycle exchanges the two factors, so the natural descended base target is the swap twist, i.e. the Weil-restriction form

```text
Res_{Q(i)/Q}(J_D,Q(i))
```

once the V4 isogeny-kernel equivariance is checked.

The genus-two curve `D` is the Bolza curve. Beauville 2014 gives the geometric CM-square structure

```text
End(J_D) tensor Q = M_2(Q(sqrt(-2))).
```

Fite--Sutherland 2014 provides the needed arithmetic firewall: the model `y^2=x^5-x` itself is not Q-isogenous to the square of a Q-elliptic curve, and its full endomorphism field is `Q(i,sqrt(-2))`; a different Q-twist has a Q-isogeny to the square of an explicit CM elliptic curve.

Therefore the route has genuinely narrowed to explicit twist/Selmer/Mordell-Weil arithmetic rather than vague use of an Albanese map.

Full target: `albanese-bolza-target.md`.

## Residual receivers

```text
R29-BEAU1A=BeauvilleCanonicalDoubleCoverStandardCuboidQFormAdapter
STATUS=PASS_CANDIDATE_THIS_PR

R29-BEAU1B=ExplicitGenericBeauvilleDoubleCoverSquareclassFunction
STATUS=OPEN

R29-BEAU1C=PhysicalEndpointLiftSquareclassLocalRamificationLedger
STATUS=OPEN

R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel
STATUS=OPEN_BOUNDED

R29-BEAU2=LocallySolubleBeauvilleTwistsToAlbaneseTorsors
STATUS=OPEN

R29-BEAU3=BolzaJacobianCMQCurveTwistDescentForBeauvilleEndpointCovers
STATUS=OPEN
```

## Applicability verdict

This route is **materially new and remains HIGH_VALUE**, because it replaces the initial geometric field-of-definition uncertainty by an explicit Q-descent adapter and identifies the remaining obstruction as a concrete quadratic-twist/Albanese/CM arithmetic problem.

It is not yet a perfect-cuboid obstruction:

```text
EVERY_Q_ENDPOINT_LIFTS_UNTWISTED=false
FINITE_TWIST_SET_PROVED=false
ALBANESE_RATIONAL_POINTS_CONTROLLED_UNIFORMLY=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Routing

After fresh audit, retain the Beauville receivers for later Stage29 endpoint routing and continue the independent suffix queue:

```text
NEXT_ITEM=29-02e
NEXT_EXPECTED_COMMAND=Stage29-audit
```

The open `29-02h*` namespace remains available for genuinely new foundations discovered later.
