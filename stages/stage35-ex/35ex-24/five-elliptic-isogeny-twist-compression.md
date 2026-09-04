# Stage35-EX 35EX-24 — exact five-elliptic isogeny/twist compression

## Scope and authority

This leaf starts only after hostile-audit PASS of 35EX-23 at exact head

```text
77ff0a6cf51679bd64525a0be843fcd1eed77d8e
review 5111910947
merged main c20ee71d91af850103fd7406f9b1072448a11fcf
```

and after the required fresh breadth audit

```text
stages/stage35-ex/35ex-23/post-five-elliptic-breadth-audit.json
```

selected exactly one LIVE route:

```text
E1-FIVE-ELLIPTIC-ISOGENY-TWIST-COMPRESSION.
```

No E1/R29/FIB2/J12/Stage35/perfect-cuboid credit is granted here.

Work over the audited first-source function field

```text
K = Q(B1),   B1: p^2=1+x^2,
a=x^2,
p^2=1+a.
```

## 1. A general symmetric pair-quartic adapter

Let `r,s in K^*`, put

```text
d=r*s,
c=r^2+s^2,
r^2 != s^2,
```

and consider the smooth genus-one quartic

```text
C(r,s): V^2=(y^2+r^2)(y^2+s^2)
       =y^4+c*y^2+d^2.
```

On the dense open `y!=0`, define

```text
U = 2*d*(V+d)/y^2,
T = U+c,
Y = y*(U^2-4*d^2)/(2*d).
```

Then direct elimination gives

```text
Q(r,s): Y^2=T*(T-(r+s)^2)*(T-(r-s)^2).
```

The inverse on the open where

```text
D=(T-(r+s)^2)*(T-(r-s)^2) != 0
```

is

```text
y = 2*d*Y/D,
U = T-c,
V = U*y^2/(2*d)-d.
```

Exact substitution gives both round trips on these opens.

The exceptional genus-one points are also controlled. With the quartic point `(0,+d)` chosen as origin,

```text
(0,+d) -> O_Q,
(0,-d) -> (0,0),
I_+     -> ((r+s)^2,0),
I_-     -> ((r-s)^2,0),
```

where `I_+/-` are the two quartic points at infinity with `V/y^2 -> +/-1`.

Thus this is an exact genus-one quartic-to-Weierstrass adapter, including the excluded dense-open loci; it is not an inference from matching j-invariants.

Formal Arsenal `S31-W01` is used only for this adapter discipline. Its exact card remains:

```text
docs/arsenal/cards/formal/S31-W01.md
blob_sha=122a6c1c5c871c1c7b797017e854de8ec55e7c50
```

## 2. The same cubic is a kernel-(0,0) degree-2 quotient

Define

```text
L(r,s): W^2=Z*(Z+r^2)*(Z+s^2)
             =Z^3+c*Z^2+d^2*Z.
```

The rational 2-torsion point is `T0=(0,0)`. Translation by `T0` on the affine open `Z!=0` is

```text
tau(Z,W)=(d^2/Z, -d^2*W/Z^2).
```

The two rational functions

```text
T = W^2/Z^2 = Z+c+d^2/Z,
Y = W*(d^2-Z^2)/Z^2
```

are exactly invariant under `tau`. Direct substitution gives

```text
Y^2=T^3-2*c*T^2+(c^2-4*d^2)*T
   =T*(T-(r+s)^2)*(T-(r-s)^2).
```

Hence they give the standard degree-2 quotient

```text
phi(r,s): L(r,s) -> Q(r,s)
```

with kernel `{O,T0}`. Combining with the exact quartic adapter above proves:

```text
C(r,s) is K-2-isogenous to L(r,s).
```

This is proved by the displayed quotient invariants and equations; no j-only isogeny inference is used.

## 3. Apply the lemma to the three pair-character factors

The 35EX-23 pair quotients are exactly

```text
E12 = C(1,x),
E13 = C(1,p),
E23 = C(x,p).
```

Therefore

```text
E12 ~_2 L12,   L12: R^2=Z*(Z+1)*(Z+a),
E13 ~_2 F,     F:   R^2=Z*(Z+1)*(Z+p^2),
E23 ~_2 L23,   L23: R^2=Z*(Z+a)*(Z+p^2).
```

All three degree-2 isogenies are defined over `K`.

## 4. Exact fixed `-1` twist relation for the E12/Eplus channel

The 35EX-23 `Eplus` model is

```text
Eplus: Yplus^2=(X+1)*(X+a)*(X+1+a).
```

Translate

```text
t=X+1+a.
```

Then

```text
Eplus: Yplus^2=t*(t-1)*(t-a).
```

Define the constant quadratic twist

```text
Eplus^(-1): R^2=-t*(t-1)*(t-a).
```

Setting `Z=-t` gives exactly

```text
R^2=Z*(Z+1)*(Z+a)=L12.
```

Consequently

```text
E12 is K-2-isogenous to Eplus^(-1).
```

The `-1` twist is essential over `K`; this leaf does **not** claim `E12` is K-isogenous to `Eplus` merely because the j-pair lies on the degree-2 modular relation geometrically.

After the constant quadratic extension `K(i)/K`, the twist disappears, so

```text
E12_(K(i)) ~_2 Eplus_(K(i)).
```

## 5. Exact fixed `-1` twist relation for the E13/E23 channel

Keep

```text
F: R^2=Z*(Z+1)*(Z+p^2),   p^2=1+a.
```

The general lemma already gives

```text
E13 ~_2 F
```

over `K`.

Let

```text
F^(-1): R^2=-Z*(Z+1)*(Z+p^2).
```

On `Z!=-1`, define

```text
U = -a*Z/(Z+1),
W =  a*R/(Z+1)^2.
```

Using `p^2=1+a`, exact substitution gives

```text
W^2=U*(U+a)*(U+p^2)=L23.
```

The inverse is rational on the corresponding open, so `F^(-1)` and `L23` are K-isomorphic as elliptic curves after the exceptional points are restored. Hence

```text
E23 is K-2-isogenous to F^(-1).
```

Again the fixed twist is not discarded. Over `K(i)`:

```text
E13_(K(i)) ~_2 F_(K(i)),
E23_(K(i)) ~_2 F_(K(i)).
```

## 6. Exact compression of the five-factor Jacobian package

35EX-23 proved generically

```text
Jac(C) ~ E12 * E13 * E23 * Eplus * Eminus
```

(up to isogeny over `K`). Replacing the three pair factors by the exact K-isogenous models above yields the sharper K-level package

```text
Jac(C)
 ~_K
 Eplus * Eplus^(-1) * F * F^(-1) * Eminus.
```

After adjoining `i`, the fixed twist pairs coalesce:

```text
Jac(C)_(K(i))
 ~
 Eplus^2 * F^2 * Eminus.
```

Thus the five displayed nonisotrivial quotient factors have only three underlying variation shapes after the proved fixed-twist/base-extension compression, with multiplicities `2,2,1` over `K(i)`.

This does **not** prove that the three retained shapes are pairwise non-isogenous by every possible degree. The exact statement is only that the displayed five-factor package admits the three-representative compression above; no further compression is claimed.

## 7. The three retained variation shapes still move

The representative j-functions are

```text
j(Eplus)
 =256*(a^2-a+1)^3/(a^2*(a-1)^2),

j(F)
 =256*(a^2+a+1)^3/(a^2*(a+1)^2),

j(Eminus)
 =256*(a^4-a^2+1)^3/(a^4*(a-1)^2*(a+1)^2).
```

All are nonconstant in `a`. Therefore the exact compression does not unlock one fixed elliptic curve or one fixed finite constant list.

The gain is structural: any future simultaneous Kummer/Selmer/height/receiver-intersection argument should be organized around

```text
(Eplus, Eplus^(-1)),
(F, F^(-1)),
Eminus,
```

rather than treating `E12,E13,E23,Eplus,Eminus` as five unrelated families.

## 8. Arsenal routing after compression

The required fresh breadth audit compared the generated routes against the Arsenal only after blind generation.

- `S31-W01` certifies the quartic/cubic rational adapter discipline used above; it gives no arithmetic closure.
- `S34-W03` is a strong future router for the preserved simultaneous Kummer-lift candidate because only the exact quotient-plus-receiver intersection would need to be killed.
- `S34-W02` remains locked because no full Mordell-Weil group valid for every moving receiver-relevant fiber has been certified.
- `S31-WF01` remains only the full-MW certification workflow if such data become load-bearing later.

No formal Arsenal card was found that already supplies the exact fixed-twist isogeny compression or a uniform moving-family closure theorem.

## 9. What is proved and what is not

Proved here:

```text
PAIR_QUARTIC_EXACT_WEIERSTRASS_ADAPTER=true
PAIR_QUARTIC_STANDARD_KERNEL_2_ISOGENY=true
E12_K_2_ISOGENOUS_TO_MINUS1_TWIST_EPLUS=true
E13_K_2_ISOGENOUS_TO_F=true
E23_K_2_ISOGENOUS_TO_MINUS1_TWIST_F=true
JACOBIAN_K_TWIST_PAIR_COMPRESSION=true
JACOBIAN_KI_THREE_REPRESENTATIVE_COMPRESSION=true
KI_MULTIPLICITY_PATTERN=2,2,1
ALL_THREE_REPRESENTATIVE_J_FUNCTIONS_NONCONSTANT=true
FIXED_ELLIPTIC_CURVE_REDUCTION_UNLOCKED=false
UNIFORM_MW_CLOSURE_UNLOCKED=false
```

Not proved:

- `E12` is K-isogenous to untwisted `Eplus`;
- `E23` is K-isogenous to untwisted `F`;
- the three retained representative families are pairwise non-isogenous in every degree;
- any full Mordell-Weil group over all rational fibers;
- a simultaneous Kummer-lift contradiction;
- a uniform specialization/height theorem;
- a new Brauer obstruction;
- rational-point classification of the normalized surface;
- E1 or any parent/endpoint closure.

Therefore this leaf is an exact compression, not a closure theorem.

## 10. Cycle consequence

The K-level fixed-twist decomposition and the `K(i)` multiplicity pattern are a new exact structural invariant of the 35EX-23 package. Under the Cycle Exploration Safety Protocol this material change requires another fresh breadth audit after hostile-audit PASS before choosing the arithmetic successor.

```text
CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_NEW_GATE=TWO_FIXED_MINUS1_TWIST_PAIRS_PLUS_EMINUS
FRESH_BREADTH_AUDIT_REQUIRED_AFTER_HOSTILE_PASS=true
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
