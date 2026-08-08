# Stage14-4aa — independent two-face parametrization and upstream-input audit

## Purpose

Stage14-4 begins the proof-level study of the true growth order of the primitive canonical exactly-two-face population. 14-4aa does **not** guess or prove a growth exponent. Its job is to replace the Stage14-3 finite-reconnaissance viewpoint by an exact structural parametrization and to lock which upstream Stage13 statement is provisionally allowed.

## Upstream assumption used in this restart

For current Stage14-4 work, the provisional external input is the **Stage13 R02 directional raw asymptotic candidate**

\[
A_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

as stated in `stages/stage13/13-12ac/current-proof.md`.

This is recorded as

```text
UPSTREAM_STAGE13_VERSION=R02
UPSTREAM_STAGE13_STATUS=ASSUMED_PROVISIONALLY
UPSTREAM_STAGE13_FINAL_EXTERNAL_FREEZE=false
```

The R02 pair-overlap and triple-overlap little-o statements are **not imported as proof inputs in 14-4aa**. They concern precisely the population Stage14 is now trying to understand more sharply. They may later be used as a provisional ceiling only if explicitly re-audited.

R03 is intentionally not used in this substage.

## 1. Direction-neutral structural coordinates

Let `e` denote the edge shared by the two integral faces, and let `x<y` denote the two nonshared edges. Introduce the two integral face diagonals `u<v` and the integer space diagonal `d`:

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
e^2+x^2+y^2=d^2.
\]

The three canonical Stage14 directions are then only the three possible positions of the shared edge among the ordered cuboid edges:

```text
a-direction: e < x < y
b-direction: x < e < y
c-direction: x < y < e
```

Thus the arithmetic equations are direction-neutral; the label `a/b/c` is a chamber condition on the same generic object.

The exactly-two condition is

\[
x^2+y^2\ne\square.
\]

If `x^2+y^2` is also a square, the object belongs to the triple population `T` and must not be discarded.

## 2. Four Pythagorean triangles attached to one raw pair object

From the defining equations,

\[
u^2+y^2=d^2,
\qquad
v^2+x^2=d^2.
\]

Hence every raw two-face object produces four integer right triangles:

```text
(e,x,u)
(e,y,v)
(u,y,d)
(v,x,d)
```

Only three of the four Pythagorean equations are independent. For example,

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
u^2+y^2=d^2
\]

already imply

\[
v^2+x^2=d^2.
\]

Conversely, any positive integer solution of these three equations, together with the required ordering and primitivity, gives a raw Stage14 pair object. The third-face square test then separates exactly-two from triple objects.

This is the first exact Stage14-4 structural reduction.

## 3. Euclid charts for the shared-face fiber product

For a primitive Euclid base `m>n>0`, `(m,n)=1`, `m-n` odd, define

\[
L_D(m,n)=m^2-n^2,
\qquad
L_P(m,n)=2mn,
\qquad
H(m,n)=m^2+n^2.
\]

Every positive integer Pythagorean triple can be written as

\[
(kL_\sigma(m,n),\ kL_{\bar\sigma}(m,n),\ kH(m,n)),
\qquad \sigma\in\{D,P\},
\]

for a positive scale `k`, with the two leg roles selectable by `sigma`.

Apply this independently to the two integral faces:

\[
(e,x,u)
=
\bigl(k_1L_{\sigma_1}(m,n),
      k_1L_{\bar\sigma_1}(m,n),
      k_1H(m,n)\bigr),
\]

\[
(e,y,v)
=
\bigl(k_2L_{\sigma_2}(r,s),
      k_2L_{\bar\sigma_2}(r,s),
      k_2H(r,s)\bigr).
\]

The shared-edge equation is therefore the exact fiber-product constraint

\[
\boxed{
 k_1L_{\sigma_1}(m,n)
 =k_2L_{\sigma_2}(r,s)
 =e.
}
\]

There are four representation-role charts

```text
DD, DP, PD, PP
```

for `(sigma_1,sigma_2)`. These chart labels record which Euclid leg realizes the shared edge; they are **not** the Stage13 OE/EE parity branches.

## 4. Third Pythagorean gluing: imposing the space diagonal intrinsically

The space-diagonal equation is equivalent to requiring `(u,y,d)` to be a Pythagorean triple. Introduce a third Euclid chart

\[
(u,y,d)
=
\bigl(k_3L_{\sigma_3}(p,q),
      k_3L_{\bar\sigma_3}(p,q),
      k_3H(p,q)\bigr).
\]

Then a raw Stage14 pair object is represented by three Pythagorean triples subject to the exact matching equations

\[
\boxed{
 k_1L_{\sigma_1}(m,n)
 =k_2L_{\sigma_2}(r,s)
}
\]

and

\[
\boxed{
 k_1H(m,n)
 =k_3L_{\sigma_3}(p,q),
\qquad
 k_2L_{\bar\sigma_2}(r,s)
 =k_3L_{\bar\sigma_3}(p,q).
}
\]

After these matches, `d=k_3H(p,q)` and the fourth triangle `(v,x,d)` is automatic.

This three-triple gluing is an exact, Stage14-native parametrization framework. It is not yet a uniqueness theorem and is not yet a counting asymptotic.

## 5. Global primitivity must be imposed after gluing

A crucial boundary is

\[
\gcd(e,x,y)=1.
\]

The Euclid bases `(m,n)`, `(r,s)`, `(p,q)` may each be primitive while the scales `k_1,k_2,k_3` still interact nontrivially. Therefore Stage14 must **not** replace global cuboid primitivity by the stronger and generally incorrect condition `k_1=k_2=k_3=1`.

Likewise, the canonical inequalities are imposed only after the generic triple-gluing object is formed:

```text
e<x<y  -> a-direction
x<e<y  -> b-direction
x<y<e  -> c-direction
```

This separates arithmetic support from chamber geometry.

## 6. Relation to Stage13 R02

Stage13 R02 parametrizes a raw one-face incidence by one integral face followed by an outer Pythagorean extension to the space diagonal. In the generic coordinates above, selecting `(e,x,u)` as the distinguished face gives exactly

```text
(e,x,u)  +  (u,y,d)
```

and the extra Stage14 condition is that

```text
(e,y,v)
```

is also Pythagorean.

Thus Stage13 R02 remains useful as an ambient one-face density statement, but Stage14-4 does not identify the second-face condition with an independent random event. The shared-edge matching equation creates genuine arithmetic correlation and must be analyzed directly.

In particular, 14-4aa does **not** infer

```text
N_2(B) ~ constant * A_q(B)
N_2(B) ~ B(log B)^alpha
N_2(B) ~ B^theta(log B)^beta
```

for any constants/exponents.

## 7. Dependency ledger

```text
INTRINSIC_STAGE14_FACTS:
  - locked primitive canonical counting convention
  - exact raw-pair / triple / exactly-two identities
  - finite census through B=2,000,000
  - direction-neutral (e,x,y) chamber decomposition
  - exact three-Pythagorean-triple gluing framework

PROVISIONAL_UPSTREAM_INPUT:
  - Stage13 R02 directional raw asymptotic A_q(B)

NOT_IMPORTED_IN_14_4AA:
  - Stage13 R02 pair-overlap little-o theorem
  - Stage13 R02 triple-overlap little-o theorem
  - Stage13 R03 statements
  - any Euler-side two-face asymptotic
  - any finite-ratio extrapolation
```

If the final external Stage13 review changes the directional asymptotic, only the provisional upstream section must be re-audited. The three-triple Stage14 parametrization survives unchanged.

## 8. What 14-4aa establishes and what it does not

Established:

```text
ONE_GENERIC_ARITHMETIC_OBJECT_FOR_ALL_THREE_DIRECTIONS=true
DIRECTION_LABEL_IS_CHAMBER_POSITION_OF_SHARED_EDGE=true
FOUR_RIGHT_TRIANGLES_PER_RAW_PAIR=true
THREE_INDEPENDENT_PYTHAGOREAN_RELATIONS_SUFFICE=true
EUCLID_SHARED_EDGE_FIBER_PRODUCT_LOCKED=true
THIRD_PYTHAGOREAN_GLUING_LOCKED=true
GLOBAL_PRIMITIVITY_APPLIED_AFTER_GLUING=true
```

Not established:

```text
UNIQUE_PARAMETERIZATION=false
BOUNDED_PARAMETER_MULTIPLICITY=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false
DIRECTIONAL_LIMIT_IDENTIFIED=false
STAGE13_R02_EXTERNALLY_FROZEN=false
```

## Next

Stage14-4ab should audit representation multiplicity and reduce the three-triple gluing to a counting problem with explicit matching/divisibility variables. The first target is not an asymptotic formula, but a clean countable parameter space without uncontrolled duplicate representations.
