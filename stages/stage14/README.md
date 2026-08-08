# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
MAX_VERIFIED_B=2000000
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_FULL_ACCESS_AUTHORIZED=true
R03_PAIR_OVERLAP_LITTLE_O_IMPORTED=true
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
NEXT=Stage14-4ac height inequality and arithmetic counting envelope
```

Canonical source: `stages/stage14/main.md`.

## Counting convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

with

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

## Frozen finite census

Two materially different exact cuboid-generation routes agree through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),\qquad N_2=356,\qquad T=0.
\]

No triple object was found through this finite ceiling; this is not a nonexistence proof.

## Stage13 R03 upstream map — fully available

Stage14 may now use the reviewed R03 proof map and the Stage13-12ag explicitness supplement:

```text
stages/stage13/13-12af/current-proof.md
stages/stage13/13-12ag/result.md
```

The repository currently records Grok `CLOSED` and Qwen `CLOSED` on the R03 snapshot. The final repository freeze remains bookkeeping; the mathematical R03 map is available to Stage14.

Imported results now include

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3).
\]

Hence Stage14 inherits the ceiling

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

This is not the true two-face order; Stage14-4 is trying to sharpen it.

## Stage14-4aa — structural restart

For a raw pair object, let `e` be the shared edge and `x<y` the nonshared edges. Then

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,
\qquad u^2+y^2=d^2,
\qquad v^2+x^2=d^2.
\]

The three directions are only the chamber positions of `e`:

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

Thus all directions share one arithmetic object.

## Stage14-4ab — exact matching reduction

Let two oriented primitive Pythagorean face data be

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2),
\]

where `S_i` is the leg designated to become the shared edge. Put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

The complete shared-edge scale solution is

\[
k_1=t\beta,\qquad k_2=t\alpha.
\]

The minimal glued edges are

\[
e_0=g\alpha\beta,\qquad x_0=\beta X_1,\qquad y_0=\alpha X_2,
\]

and Stage14-4ab proves

\[
\gcd(e_0,x_0,y_0)=1.
\]

Therefore

\[
\boxed{\gcd(e,x,y)=t},
\]

so global cuboid primitivity forces exactly

\[
\boxed{t=1.}
\]

The actual face scales need not be one:

\[
k_1=\beta,\qquad k_2=\alpha.
\]

Thus a primitive raw pair incidence is obtained bijectively from two oriented primitive face data by

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2,
\end{aligned}}
\]

with

```text
x<y
d^2 square
d<=B
```

and then the third-face test separates exactly-two from `T`.

The third Euclid triple from 14-4aa is not independent. If

\[
h=\gcd(H_1,X_2),
\]

then its scale is exactly

\[
\boxed{k_3=h}.
\]

For a fixed raw pair incidence the parameter-fiber multiplicity is exactly

\[
\boxed{1}.
\]

## Independent bijection audit

A new face-pair-first enumerator reproduces the locked counts without using the Stage14-2 cuboid-edge-first route:

```text
B=1000   (2,0,0)
B=2000   (2,2,1)
B=5000   (6,6,3)
B=10000  (9,11,5)
```

with `T=0` at all four audit cutoffs.

Artifacts:

```text
stages/stage14/archive/stage14-4ab-matching-reduction.md
stages/stage14/scripts/14-4/bijection_audit.py
stages/stage14/data/14-4/bijection_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## What remains unknown

Stage14 still has not identified the true growth order, leading constant, limiting directional vector, eventual leader, or whether `T(B)` ever becomes positive.

Next:

```text
14-4ac  convert the bijection into an explicit height/divisibility counting envelope
        and begin testing candidate true orders using the full R03 machinery
```
