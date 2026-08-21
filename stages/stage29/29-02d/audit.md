# Stage29-02d fresh audit

```text
AUDITED_PR=1297
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=593c2d663c1986e37e11d6d70a059cde36cf4bb4
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## Scope

Fresh audit covered the Beauville cuboid specialization, the `Q(i)` linear adapter to the standard cuboid model, the Galois cocycle, lift of that cocycle to the smooth irregular cover, descent of the canonical deck involution, rational fiber/twist semantics on the physical smooth open, the Albanese/Bolza target, CM/twist source claims, Stage29 routing, and controller state.

## Primary-source lock

Beauville, *A tale of two surfaces*, Proposition 1 verifies the surface

```text
X=(C x C')/Gamma
q=4, pg=7, K^2=32
```

and the canonical degree-two quotient onto a complete intersection of four quadrics in `P^6` with 48 nodes. Its cuboid example gives the exact linear change

```text
X=x+t, T=t-x,
Y=y+i z, Z=y-i z,
U=u, V=2v, W=2w.
```

The etale `(Z/2)^2` tower and Albanese pullback statement are in **Remark 1**, not Remark 2. The submission locator was repaired accordingly.

Beauville, *Some surfaces with maximal Picard number*, Proposition 8 and its proof give the Bolza quotient and the geometric endomorphism algebra

```text
End(J_D) tensor Q = M_2(Q(sqrt(-2))).
```

Fite--Sutherland Section 4 confirms that the model `y^2=x^5-x` does not itself have Jacobian Q-isogenous to a square of a Q-elliptic curve, has full endomorphism field `Q(i,sqrt(-2))`, while the Q-twist

```text
y^2=x^6-5x^4-5x^2+1
```

has Jacobian Q-isogenous to the square of

```text
Y^2=X^3-5X^2-5X+1
```

with CM by `Q(sqrt(-2))`.

```text
SOURCE_LOCK_AUDIT=PASS
BEAUVILLE_TOWER_LOCATOR_AUDIT=PASS_AFTER_REMARK_1_REPAIR
BOLZA_CM_SOURCE_AUDIT=PASS
FITE_SUTHERLAND_TWIST_FIREWALL_AUDIT=PASS
```

## Q-form descent

Under complex conjugation, the standard-Q cuboid coordinates transported to Beauville's quotient satisfy

```text
Y <-> Z
```

with the other canonical coordinates fixed. Thus the `Q(i)/Q` cocycle on the Beauville quotient is the involution `tau_Sigma` swapping `Y,Z`.

On `C0 x C0`, factor exchange is Q-defined, commutes with the diagonal `Gamma`, and on the canonical sections fixes `X,T,U,V,W` while swapping `Y,Z`. Hence it supplies a lift `tau_X` with

```text
q_B o tau_X = tau_Sigma o q_B.
```

The cocycle condition holds because factor exchange is an involution. Galois descent therefore gives the Q-form

```text
q_cub:X_cub -> S_cub.
```

### Deck-group repair

The submitted twist ledger used `H^1(Q,Z/2)` but did not explicitly record that the canonical deck involution survives the Q-form descent. The canonical involution `i_X` is induced by a diagonal odd-sign class in `Gamma_+/Gamma`, while factor exchange commutes with all diagonal actions. Therefore

```text
tau_X i_X = i_X tau_X,
```

so `i_X` descends and the free smooth-locus cover has constant deck group `Z/2` over Q.

```text
Q_FORM_COVER_ADAPTER_AUDIT=PASS
R29_BEAU1A=DISCHARGED
DECK_INVOLUTION_DESCENT_AUDIT=PASS
DESCENDED_DECK_GROUP=CONSTANT_Z_OVER_2
```

## Rational lift / twists

After removing the 48 branch/fixed points and restricting to the positive nondegenerate smooth physical open,

```text
q_U:X_U -> U_phys
```

is finite etale of degree two with constant deck group `Z/2`. Each `P in U_phys(Q)` therefore defines an exact torsor class

```text
delta(P) in H^1(Q,Z/2) ~= Q^*/Q^{*2}.
```

Twisting by that class gives a rational lift. The union-over-twists identity is correct, but no finite set of possible squareclasses is proved.

```text
FIBER_TORSOR_CLASS_AUDIT=PASS
FINITE_TWIST_SET_PROVED=false
UNTWISTED_LIFT_SUFFICES=false
R29_BEAU1B=OPEN
R29_BEAU1C=OPEN
```

## Albanese / Bolza target

Factor exchange descends through the `D x D` tower and swaps the two Jacobian factors. The corresponding swap descent target is the Weil restriction form

```text
Res_{Q(i)/Q}(J_D,Q(i)).
```

This target is valid. However, the exact equivariance of the `(Z/2)^2` isogeny kernel `A_B -> J_D x J_D` under the swap cocycle is not proved in this suffix and remains correctly isolated as

```text
R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel.
```

No Albanese finiteness or endpoint obstruction follows merely from the geometric CM decomposition.

```text
SWAP_WEIL_RESTRICTION_TARGET_AUDIT=PASS
V4_KERNEL_SWAP_EQUIVARIANCE_AUDITED=false
R29_BEAU2A=OPEN_BOUNDED
R29_BEAU2=OPEN
R29_BEAU3=OPEN
```

## Controller / routing

PR #1293 is already merged as `8adb7deb9daf80282974bbee7a2b497ecf5bf9a2`, while the inherited controller still recorded it as pending merge. This audit mechanically synchronizes that state.

Stage29-02d remains a materially distinct Stage29-native route. No Stage16--28 backflow is triggered. The independent suffix queue advances to `29-02e`, while the Beauville residual receivers remain live for later routing.

## Verdict

```text
CHECKPOINT29_02D_AUDIT=PASS
SOURCE_LOCK_AUDIT=PASS_AFTER_LOCATOR_REPAIR
Q_FORM_COVER_ADAPTER_AUDIT=PASS
R29_BEAU1A=DISCHARGED
DECK_INVOLUTION_DESCENT_AUDIT=PASS
FIBER_TORSOR_CLASS_AUDIT=PASS
SWAP_WEIL_RESTRICTION_TARGET_AUDIT=PASS
V4_KERNEL_SWAP_EQUIVARIANCE_AUDITED=false
FINITE_TWIST_SET_PROVED=false
ALBANESE_UNIFORM_CONTROL_PROVED=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_STATUS=29-02e_EXISTING_V4_CHARACTER_NEWFORM_ROUTE
NEXT_ITEM=29-02e
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
