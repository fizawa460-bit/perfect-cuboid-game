# Stage29-02d — Beauville / Bolza source lock

```text
TASK=Stage29-02d
ROLE=BEAUVILLE_IRREGULAR_COVER_Q_DESCENT
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## Primary geometric source

Arnaud Beauville, *A tale of two surfaces*, arXiv:1303.1910; published in *Higher Dimensional Algebraic Geometry — in honour of Yujiro Kawamata*, Adv. Stud. Pure Math. 74 (2017), 1–10, DOI 10.2969/aspm/07410001.

For genus-5 curves

```text
C: u^2=a(x,y), v^2=b(x,y), w^2=c(x,y)
```

with `Gamma ≅ (Z/2)^2` the even-sign subgroup, Proposition 1 constructs

```text
X=(C x C')/Gamma
q(X)=4, pg(X)=7, K_X^2=32,
```

and an involution `i_X` with 48 fixed points such that the canonical map has degree two and identifies `X/i_X` with a `(2,2,2,2)` complete intersection in `P^6` having 48 nodes.

For the cuboid specialization

```text
C0: u^2=xy, v^2=x^2-y^2, w^2=x^2+y^2,
```

the canonical quotient `Sigma_B` has coordinates `[X:Y:Z:T:U:V:W]` and equations

```text
XT = YZ = U^2,
V^2 = X^2-Y^2-Z^2+T^2,
W^2 = X^2+Y^2+Z^2+T^2.
```

Beauville then gives the linear change over `Q(i)`

```text
X=x+t,   T=t-x,
Y=y+i z, Z=y-i z,
U=u,     V=2v, W=2w,
```

which gives the standard cuboid equations

```text
t^2=x^2+y^2+z^2,
u^2=y^2+z^2,
v^2=x^2+z^2,
w^2=x^2+y^2.
```

Remark 2 gives the etale `(Z/2)^2` tower

```text
C x C' -> X -> D x D'
```

where `D=C/Gamma` has genus two, and identifies `X -> D x D'` as the pullback of an etale `(Z/2)^2` covering of `J_D x J_D'`; the resulting abelian fourfold is the Albanese variety geometrically.

For `C=C'=C0`, the genus-two quotient is

```text
D: s^2=t(t^4-1),
```

the Bolza curve.

## Primary geometric CM decomposition source

Arnaud Beauville, *Some surfaces with maximal Picard number*, J. École polytechnique Math. 1 (2014), 101–116, DOI 10.5802/jep.5, Proposition 8.

For the same `C0`, Proposition 8 proves geometrically

```text
J(C0) ~ E_i^3 x E_{sqrt(-2)}^2,
```

and its proof identifies the `Gamma`-invariant genus-two quotient `D=C0/Gamma` and gives

```text
End(J_D) tensor Q = M_2(Q(sqrt(-2))).
```

Thus `J_D` is geometrically isogenous to the square of a CM elliptic curve with CM field `Q(sqrt(-2))`.

## Arithmetic twist source

Francesc Fite and Andrew V. Sutherland, *Sato–Tate distributions of twists of y^2=x^5-x and y^2=x^6+1*, Algebra & Number Theory 8 (2014), 543–585, DOI 10.2140/ant.2014.8.543.

Section 4 treats the Bolza isomorphism class. It explicitly records that the model

```text
y^2=x^5-x
```

does **not** have Jacobian Q-isogenous to the square of an elliptic curve over Q. It also records that its full Jacobian endomorphism field is

```text
Q(i, sqrt(-2)).
```

The paper introduces the Q-twist

```text
C2^0: y^2=x^6-5x^4-5x^2+1
```

whose Jacobian is Q-isogenous to the square of

```text
E2^0: Y^2=X^3-5X^2-5X+1,
```

with CM by `Q(sqrt(-2))` (Lemma 4.1 and surrounding discussion).

## Scope firewall

```text
BEAUVILLE_GEOMETRIC_COVER_LOCKED=true
STANDARD_CUBOID_Q_FORM_IDENTICAL_WITHOUT_DESCENT=false
BOLZA_JACOBIAN_GEOMETRIC_CM_SQUARE=true
BOLZA_MODEL_Q_ISOGENOUS_TO_Q_ELLIPTIC_SQUARE=false
ARITHMETIC_TWIST_CONTROL_REQUIRED=true
ALBANESE_RATIONAL_POINT_FINITE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
