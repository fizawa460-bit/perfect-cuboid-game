# Stage29-02d — explicit Q-form adapter for the Beauville canonical double cover

```text
STATUS=AUDITED_PASS
BASE_FIELD_Q=true
SPLITTING_FIELD=Q(i)
```

## 1. Two Q-models over `Q(i)`

Let `Sigma_B/Q` be Beauville's canonical quotient model with coordinates

```text
[X:Y:Z:T:U:V:W]
```

and equations

```text
XT=YZ=U^2,
V^2=X^2-Y^2-Z^2+T^2,
W^2=X^2+Y^2+Z^2+T^2.
```

Let `S_cub/Q` be the standard perfect-cuboid canonical model with coordinates

```text
[x:y:z:t:u:v:w]
```

and equations

```text
t^2=x^2+y^2+z^2,
u^2=y^2+z^2,
v^2=x^2+z^2,
w^2=x^2+y^2.
```

Beauville's linear map over `K=Q(i)` is

```text
phi:S_cub,K -> Sigma_B,K
X=x+t, T=t-x,
Y=y+i z, Z=y-i z,
U=u, V=2v, W=2w.
```

Direct substitution verifies all four equations.

## 2. The descent cocycle is explicit

Let `sigma` be complex conjugation in `Gal(K/Q)`. For a point of the standard Q-form,

```text
sigma(X)=X,
sigma(T)=T,
sigma(U)=U,
sigma(V)=V,
sigma(W)=W,
sigma(Y)=Z,
sigma(Z)=Y.
```

Hence the discrepancy between the native Q-structure of `Sigma_B` and the standard cuboid Q-structure is the Q-automorphism

```text
tau_Sigma:[X:Y:Z:T:U:V:W] -> [X:Z:Y:T:U:V:W].
```

Equivalently, `S_cub` is the `Q(i)/Q` twist of `Sigma_B` by the cocycle sending the nontrivial Galois element to `tau_Sigma`.

## 3. The cocycle lifts to Beauville's smooth surface

For the cuboid specialization take

```text
C0: u^2=xy, v^2=x^2-y^2, w^2=x^2+y^2
X_B=(C0 x C0)/Gamma,
```

with diagonal `Gamma=(Z/2)^2` the even-sign subgroup.

On `C0 x C0`, factor exchange

```text
kappa:(p,q) -> (q,p)
```

is defined over Q and commutes with the diagonal `Gamma`, hence descends to a Q-involution `tau_X` of `X_B`.

For Beauville's canonical sections

```text
X=x x', Y=x y', Z=y x', T=y y',
U=u u', V=v v', W=w w',
```

factor exchange fixes `X,T,U,V,W` and exchanges `Y,Z`. Therefore

```text
q_B o tau_X = tau_Sigma o q_B,
```

where `q_B:X_B->Sigma_B` is the canonical degree-two quotient.

Thus the descent cocycle on `Sigma_B` lifts to the cover. Galois descent therefore produces a Q-form

```text
q_cub:X_cub -> S_cub
```

whose base change to `Q(i)` is Beauville's canonical double cover.

This resolves the first field-of-definition obstruction at the level of the cover itself.

## 4. Deck involution also descends

The canonical deck involution `i_X` is induced by the diagonal action of the nontrivial class in `Gamma_+/Gamma`; factor exchange commutes with every diagonal action on `C0 x C0`. Hence

```text
tau_X o i_X = i_X o tau_X.
```

Therefore the twist/descent above carries the deck involution with it. On the descended smooth free locus, the deck group is the constant Q-group `Z/2`, not merely a geometric involution after base change. This is the precise input needed for the rational fiber classes in `H^1(Q,Z/2)` used by `lift-twist-ledger.md`.

## 5. Audited verdict and retained receivers

```text
R29-BEAU1A=BeauvilleCanonicalDoubleCoverStandardCuboidQFormAdapter
Q_FORM_COVER_EXISTS=PASS_AUDITED
DESCENT_COCYCLE=Y_Z_SWAP
COCYCLE_LIFT=FACTOR_SWAP_ON_C0xC0
DECK_INVOLUTION_DESCENDS=true
DESCENDED_DECK_GROUP=CONSTANT_Z_OVER_2
```

Not supplied here:

- an explicit projective equation for `X_cub/Q` independent of descent notation;
- an explicit rational function whose squareclass represents the generic double cover;
- a complete boundary model on the minimal resolution;
- any claim that every Q-point lifts to the untwisted `X_cub(Q)`.

```text
EVERY_RATIONAL_ENDPOINT_LIFTS_UNTWISTED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
