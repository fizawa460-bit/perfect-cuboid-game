# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AA_COMPLETE_R02_PROVISIONAL_UPSTREAM_14_4AB_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. Stage14-1 through Stage14-3 are complete. Stage14-4 restarts at proof level with an independent two-face parametrization; only a narrowly stated Stage13 R02 directional asymptotic is admitted provisionally as upstream input.

## §1. Locked counting convention

For `B>=1`, count positive integers satisfying

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

The raw pair populations are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

The exactly-two populations are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

with

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. Any `T>0` object is retained with its exact witness.

## §2. Frozen finite census and reconnaissance

Two materially different exact enumeration routes agree at all 11 audited cutoffs through `B=2,000,000`. At the verified ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

Stage14-3 established only finite facts. In particular:

- the coarse sampled equality `N_a/N_c=7/4` is not stable under a 50k grid and is not retained as a limit candidate;
- the final `a/b` crossing in the verified event stream occurs at `d=1,148,545`;
- after that crossing `a>b` persists only through the verified finite ceiling `B=2,000,000`;
- no growth law or limiting directional vector was inferred.

Canonical finite synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

## §3. Stage14-4 upstream-input boundary

The current provisional upstream assumption is the Stage13 **R02** directional raw asymptotic candidate from

```text
stages/stage13/13-12ac/current-proof.md
```

namely

\[
\boxed{
A_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

This is recorded as

```text
UPSTREAM_STAGE13_VERSION=R02
UPSTREAM_STAGE13_STATUS=ASSUMED_PROVISIONALLY
UPSTREAM_STAGE13_FINAL_EXTERNAL_FREEZE=false
STAGE13_R03_USED=false
```

The R02 pair-overlap and triple-overlap little-o statements are **not imported in Stage14-4aa**. Stage14 is now trying to understand the true two-face scale intrinsically, so using those conclusions as hidden proof inputs would blur the dependency boundary.

Stage12 is not directly imported in Stage14-4aa; any Stage12 dependence is contained inside the provisional Stage13 R02 statement above.

If the eventual external Stage13 freeze changes that directional theorem, the upstream-input section must be re-audited. The Stage14-native parametrization below is unaffected.

## §4. Stage14-4aa — independent two-face parametrization

### §4.1 One generic arithmetic object for all three directions

Let `e` be the edge shared by the two integral faces. Let the two nonshared edges be `x<y`, and let the corresponding face diagonals be `u<v`. Then a raw two-face object satisfies

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
e^2+x^2+y^2=d^2.
\]

The three canonical directions are exactly the three possible chamber positions of `e`:

```text
a-direction: e < x < y
b-direction: x < e < y
c-direction: x < y < e
```

Therefore the arithmetic core is direction-neutral. The direction label is a chamber inequality, not a different Diophantine system.

The exactly-two condition is

\[
x^2+y^2\ne\square.
\]

If `x^2+y^2` is square, the object belongs to `T` and remains in the raw-pair ledger.

### §4.2 Four attached right triangles

From the three defining equations,

\[
u^2+y^2=d^2,
\qquad
v^2+x^2=d^2.
\]

Thus every raw pair object carries four integer right triangles:

```text
(e,x,u)
(e,y,v)
(u,y,d)
(v,x,d)
```

Only three Pythagorean equations are independent. For example,

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
u^2+y^2=d^2
\]

imply the fourth equation `v^2+x^2=d^2` automatically.

Conversely, any positive integer solution of those three equations, followed by the global primitivity and chamber conditions, gives a raw Stage14 pair object.

### §4.3 Euclid shared-edge fiber product

For a primitive Euclid base `m>n>0`, `(m,n)=1`, `m-n` odd, define

\[
L_D(m,n)=m^2-n^2,
\qquad
L_P(m,n)=2mn,
\qquad
H(m,n)=m^2+n^2.
\]

Every positive integer Pythagorean triple is

\[
(kL_\sigma(m,n),
 kL_{\bar\sigma}(m,n),
 kH(m,n)),
\qquad \sigma\in\{D,P\},
\]

for a positive scale `k`.

Write the two integral faces as

\[
(e,x,u)=
\bigl(k_1L_{\sigma_1}(m,n),
      k_1L_{\bar\sigma_1}(m,n),
      k_1H(m,n)\bigr),
\]

\[
(e,y,v)=
\bigl(k_2L_{\sigma_2}(r,s),
      k_2L_{\bar\sigma_2}(r,s),
      k_2H(r,s)\bigr).
\]

The common edge is therefore governed by the exact fiber-product equation

\[
\boxed{
 k_1L_{\sigma_1}(m,n)
 =k_2L_{\sigma_2}(r,s)
 =e.
}
\]

There are four shared-edge role charts

```text
DD, DP, PD, PP.
```

These are Euclid-leg roles and must not be confused with the historical Stage13 OE/EE branches.

### §4.4 Third Pythagorean gluing for the space diagonal

Impose the space diagonal intrinsically by writing

\[
(u,y,d)
=
\bigl(k_3L_{\sigma_3}(p,q),
      k_3L_{\bar\sigma_3}(p,q),
      k_3H(p,q)\bigr).
\]

Then the three-triple system is controlled by

\[
\boxed{
 k_1L_{\sigma_1}(m,n)
 =k_2L_{\sigma_2}(r,s)
}
\]

and

\[
\boxed{
 k_1H(m,n)=k_3L_{\sigma_3}(p,q),
\qquad
 k_2L_{\bar\sigma_2}(r,s)
 =k_3L_{\bar\sigma_3}(p,q).
}
\]

After these matches,

\[
d=k_3H(p,q)
\]

and the fourth right triangle `(v,x,d)` is automatic.

This is an exact Stage14-native parametrization framework. It is not yet a uniqueness theorem and it does not yet identify an asymptotic order.

### §4.5 Global primitivity comes after gluing

The cuboid condition is

\[
\gcd(e,x,y)=1.
\]

The three Euclid bases can each be primitive while the scales `k_1,k_2,k_3` still interact. Consequently Stage14 must not replace global cuboid primitivity by the stronger condition

```text
k_1=k_2=k_3=1.
```

The correct order is:

```text
build primitive Euclid bases
allow positive scales
solve the matching equations
glue the three triangles
apply gcd(e,x,y)=1
apply one of the three chamber inequalities
retain T separately from exactly-two
```

### §4.6 Relation to Stage13 R02

Selecting `(e,x,u)` as the distinguished face turns the Stage14 object into the Stage13 one-face nested pair

```text
(e,x,u) + (u,y,d)
```

plus the extra condition that `(e,y,v)` is Pythagorean.

Thus the Stage13 R02 directional raw asymptotic supplies an ambient one-face scale, but the second-face event is **not** assumed independent. The shared-edge fiber-product equation is an arithmetic correlation that must be analyzed directly.

No claim of the form

```text
N_2(B) ~ constant * A_q(B)
N_2(B) ~ B(log B)^alpha
N_2(B) ~ B^theta(log B)^beta
```

is made in 14-4aa.

### §4.7 14-4aa decision

Artifacts:

```text
stages/stage14/archive/stage14-4aa-parametrization-input-audit.md
stages/stage14/data/14-4/proof_input_audit.json
```

Locked state:

```text
STAGE14_4AA=COMPLETE
ONE_GENERIC_ARITHMETIC_OBJECT_FOR_ALL_THREE_DIRECTIONS=true
DIRECTION_LABEL_IS_CHAMBER_POSITION_OF_SHARED_EDGE=true
FOUR_RIGHT_TRIANGLES_PER_RAW_PAIR=true
THREE_INDEPENDENT_PYTHAGOREAN_RELATIONS_SUFFICE=true
EUCLID_SHARED_EDGE_FIBER_PRODUCT_LOCKED=true
THIRD_PYTHAGOREAN_GLUING_LOCKED=true
GLOBAL_PRIMITIVITY_APPLIED_AFTER_GLUING=true
UNIQUE_PARAMETERIZATION=false
BOUNDED_PARAMETER_MULTIPLICITY=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false
DIRECTIONAL_LIMIT_IDENTIFIED=false
```

## §5. Next — Stage14-4ab

Stage14-4ab will audit representation multiplicity and reduce the three-triple gluing to an explicit countable matching/divisibility parameter space.

The immediate targets are:

```text
identify duplicate symmetries
solve the shared-edge scale equation in gcd/lcm variables
separate arithmetic multiplicity from chamber multiplicity
rewrite the remaining gluing equations as explicit divisibility constraints
retain global primitivity after gluing
avoid guessing a growth exponent before the parameter multiplicity is controlled
```

```text
NEXT=Stage14-4ab representation multiplicity and explicit matching-variable reduction
```