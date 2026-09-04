# Stage35-EX 35EX-25 — single elliptic full-square receiver and exact Kummer lift dictionary

## Scope and authority

This leaf starts only after hostile re-audit PASS of 35EX-24 at exact head

```text
529c550c742e75025cdcc1a6b9666582f26697a1
review 5112867152
merged main 81569110952b348692e688c5e1d7148dca10b163
```

and after the required fresh post-35EX-24 breadth audit

```text
stages/stage35-ex/35ex-24/post-isogeny-compression-breadth-audit.json
```

selected exactly one LIVE route:

```text
E1-SIMULTANEOUS-ELLIPTIC-KUMMER-LIFT-COMPATIBILITY.
```

No E1/R29/FIB2/J12/Stage35/perfect-cuboid credit is granted here.

Work over the first-source field

```text
K = Q(B1),   B1: p^2=1+x^2,
a=x^2,
```

and, for rational receiver fibers, over the corresponding rational specialization field. On the positive Stage35-EX source chamber the relevant smooth fibers have `a != 0,1,-1`.

## 1. The genus-5 receiver already has one distinguished elliptic quotient

The audited generic fiber is

```text
C_a:
q^2 = y^2+1,
z^2 = y^2+a,
w^2 = y^2+1+a.
```

The 35EX-23 genus-two character quotient has the elliptic quotient

```text
Eplus_a:
Y^2=(X+1)(X+a)(X+1+a),
```

with the exact map

```text
pi_plus: C_a -> Eplus_a,
X = y^2,
Y = q*z*w.
```

Therefore every receiver point satisfies

```text
X       = y^2,
X+1     = q^2,
X+a     = z^2,
X+1+a   = w^2.
```

All four displayed linear factors are squares in the ground field.

## 2. Converse: the four-square elliptic locus reconstructs C exactly

Let `F` be any characteristic-zero field containing `a`, and let

```text
P=(X,Y) in Eplus_a(F)
```

satisfy

```text
X       in F^2,
X+1     in F^2,
X+a     in F^2,
X+1+a   in F^2.
```

Choose square roots

```text
y^2=X,
q^2=X+1,
z^2=X+a,
w^2=X+1+a.
```

Since `P` lies on `Eplus_a`,

```text
Y^2=(q*z*w)^2.
```

Thus `Y=+qzw` or `Y=-qzw`. Changing the sign of one of `q,z,w` if necessary gives

```text
Y=q*z*w.
```

Then `(y,q,z,w)` is an `F`-point of `C_a`, and `pi_plus` sends it back to `P`.

Hence, set-theoretically and with all sign fibers retained,

```text
pi_plus(C_a(F))
 = { P=(X,Y) in Eplus_a(F) :
     X, X+1, X+a, X+1+a are all squares in F }.
```

This is an iff receiver dictionary. It does not classify `Eplus_a(F)`; it identifies exactly the much smaller receiver-restricted intersection that matters.

At zero factors the same reconstruction remains literal: a zero square root is allowed and the sign choice is immaterial. For the Stage35-EX positive receiver chamber the geometric boundary `y*q*z*w=0` is excluded by the inherited open conditions, so the active arithmetic receiver is the nonzero part of this four-square locus.

## 3. Pair-character 2-isogeny image criterion

35EX-24 proved the general pair-quartic adapter. Keep

```text
C(r,s): V^2=(y^2+r^2)(y^2+s^2),
d=r*s,
c=r^2+s^2,

Q(r,s): Y^2=T*((T-c)^2-4*d^2),

L(r,s): W^2=Z^3+c*Z^2+d^2*Z,
```

with the degree-2 quotient

```text
phi: L(r,s) -> Q(r,s),
T = W^2/Z^2,
Y = W*(d^2-Z^2)/Z^2.
```

On `T != 0`, an `F`-point `(T,Y)` of `Q(r,s)` lies in `phi(L(r,s)(F))` if and only if `T` is a square in `F`.

The forward implication is immediate from `T=(W/Z)^2`.

For the converse, write `T=t^2` and define

```text
Z = (T-c-Y/t)/2,
W = t*Z.
```

The `Q` equation gives

```text
(Y/t)^2=(T-c)^2-4*d^2,
```

so direct substitution yields

```text
Z^2+(c-T)Z+d^2=0.
```

Equivalently

```text
T=Z+c+d^2/Z,
```

and therefore

```text
W^2=T*Z^2=Z^3+c*Z^2+d^2*Z.
```

Moreover

```text
W*(d^2-Z^2)/Z^2
 = t*(d^2/Z-Z)
 = Y,
```

by the chosen sign in `Z`. Thus `(Z,W)` is an exact `F`-rational lift through `phi`.

This is the exact 2-isogeny/Kummer image test needed below; no global Mordell-Weil computation is used.

## 4. Receiver points satisfy the three pair lift tests automatically

Suppose an actual `C_a` point supplies `y,q,z,w`. For the general pair with

```text
q_r^2=y^2+r^2,
q_s^2=y^2+s^2,
V=q_r*q_s,
```

35EX-24 has

```text
T=c+2*d*(V+d)/y^2.
```

But direct expansion gives the stronger identity

```text
T = ((r*q_s+s*q_r)/y)^2.
```

Indeed the numerator difference is

```text
(r*q_s+s*q_r)^2
 - c*y^2 - 2*d*(q_r*q_s+d)
 = r^2*(q_s^2-y^2-s^2)
   +s^2*(q_r^2-y^2-r^2)
 =0.
```

Therefore the three pair-character quotients satisfy exact rational 2-isogeny lift conditions:

```text
E12=C(1,x):
  T12=((z+x*q)/y)^2,

E13=C(1,p):
  T13=((w+p*q)/y)^2,

E23=C(x,p):
  T23=((x*w+p*z)/y)^2.
```

By the criterion of section 3, all three corresponding `Q` points lie in the images of their kernel-`(0,0)` degree-2 source isogenies.

## 5. The five-factor simultaneous compatibility collapses to one elliptic receiver

The key point is that the three pair lift tests and the `Eminus` image do not need to be imposed as independent arithmetic conditions once the `Eplus` four-square receiver is retained.

From an `Eplus` point satisfying

```text
X=y^2,
X+1=q^2,
X+a=z^2,
X+1+a=w^2,
```

we reconstruct `C_a` exactly by section 2. The same reconstructed `y,q,z,w` then produces

```text
E12: V12=q*z,
E13: V13=q*w,
E23: V23=z*w,
Eminus: Xminus=y^2, Yminus=y*q*z*w,
```

and the three square `T12,T13,T23` coordinates above.

Conversely every `C_a` point maps to that four-square `Eplus` locus.

Thus the exact simultaneous quotient compatibility problem has the smaller receiver

```text
R_plus(a):
P=(X,Y) in Eplus_a(F),
X, X+1, X+a, X+1+a in F^2,
```

and

```text
C_a(F) nonempty  <=>  R_plus(a) nonempty.
```

For the positive nondegenerate Stage35-EX chamber, the same equivalence holds after imposing the inherited nonzero/positivity conditions on the chosen square roots.

This is a receiver reduction, not a proof that `R_plus(a)` is empty.

## 6. Arsenal routing

Formal Arsenal card

```text
docs/arsenal/cards/formal/S34-W03.md
blob_sha=1d5275321f42768a6414d4610ac912c63be43f96
```

now matches exactly as a router: the larger auxiliary object is the moving elliptic curve `Eplus_a`, while the true receiver imposes the four simultaneous square conditions defining `R_plus(a)`.

Therefore a future leaf may legally close a fiber/branch by proving the exact intersection empty or receiver-degenerate without classifying all of `Eplus_a(F)`.

This leaf does **not** claim that S34-W03 itself supplies such an exclusion. No local prime, full Mordell-Weil group, Selmer computation, or uniform specialization theorem has yet been proved for all receiver-relevant `a`.

`S34-W02` remains locked because a full Mordell-Weil group uniformly controlling the moving family has not been certified.

## 7. What is proved and what is not

Proved here:

```text
EPLUS_FOUR_SQUARE_RECEIVER_IFF_C_LIFT=true
SINGLE_ELLIPTIC_RECEIVER_REDUCTION=true
PAIR_2ISOGENY_IMAGE_IFF_T_SQUARE_ON_T_NONZERO=true
THREE_PAIR_RECEIVER_T_COORDINATES_SQUARE=true
FIVE_FACTOR_SIMULTANEOUS_COMPATIBILITY_RECONSTRUCTED_FROM_EPLUS_FULL_SQUARE_LOCUS=true
S34_W03_SINGLE_ELLIPTIC_RECEIVER_ROUTING_MATCH=true
```

Not proved:

- `R_plus(a)` is empty for every admissible rational source `a`;
- the full rational point set of `Eplus_a`;
- a uniform full Mordell-Weil group;
- a uniform Selmer or specialization theorem;
- a fixed finite squareclass family over all `a`;
- a new Brauer obstruction;
- E1 or any parent/endpoint closure.

Accordingly this is a strict receiver compression and exact Kummer dictionary, not an arithmetic closure theorem.

## 8. Cycle consequence

The active object is no longer a five-factor compatibility problem. It is one moving elliptic curve together with four exact square conditions. This is a materially stronger receiver and therefore triggers another fresh breadth audit after hostile-audit PASS before selecting the next arithmetic leaf.

```text
CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_NEW_GATE=SINGLE_MOVING_EPLUS_FOUR_SQUARE_RECEIVER
FRESH_BREADTH_AUDIT_REQUIRED_AFTER_HOSTILE_PASS=true
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
