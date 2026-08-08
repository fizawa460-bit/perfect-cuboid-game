# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
FINITE_RECONNAISSANCE_COMPLETE=true
MAX_VERIFIED_B=2000000
UPSTREAM_STAGE13_VERSION=R02
UPSTREAM_STAGE13_STATUS=ASSUMED_PROVISIONALLY
UPSTREAM_STAGE13_FINAL_EXTERNAL_FREEZE=false
STAGE13_R03_USED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
NEXT=Stage14-4ab representation multiplicity and explicit matching-variable reduction
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

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),\qquad N_2=356,\qquad T=0.
\]

No triple object was found through this finite ceiling; this is not a nonexistence proof.

## Stage14-3 finite reconnaissance

The coarse `a/c=7/4` pattern failed under 50k-grid densification and is not treated as an invariant or limit candidate. The last verified `a/b` crossing in the event stream occurs at

\[
d=1,148,545,
\]

after which `a>b` persists only through the verified finite ceiling `B=2,000,000`.

Final finite synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

## Stage14-4aa — independent structural restart

Stage14-4 now restarts under one deliberately narrow provisional upstream input: the Stage13 **R02** directional raw asymptotic candidate

\[
A_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

R02 is not yet treated as externally frozen. R03 is intentionally not used in 14-4aa. The R02 pair-overlap and triple-overlap little-o statements are also not imported in this substage, because Stage14 is trying to understand that two-face population intrinsically.

For a raw two-face object, let `e` be the shared edge and let `x<y` be the nonshared edges. Then

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,
\qquad u^2+y^2=d^2,
\qquad v^2+x^2=d^2.
\]

Only three equations are independent. The three Stage14 directions are simply the three chamber positions of `e`:

```text
a-direction: e<x<y
b-direction: x<e<y
c-direction: x<y<e
```

Thus all directions share one arithmetic object; direction is a chamber condition.

Using Euclid legs

\[
L_D(m,n)=m^2-n^2,\qquad L_P(m,n)=2mn,
\qquad H(m,n)=m^2+n^2,
\]

the two integral faces form a shared-edge fiber product

\[
k_1L_{\sigma_1}(m,n)=k_2L_{\sigma_2}(r,s),
\]

and the space diagonal is imposed by a third Pythagorean gluing. Global cuboid primitivity remains

\[
\gcd(e,x,y)=1
\]

and must be applied after gluing; the scales must not be incorrectly forced to one.

Artifacts:

```text
stages/stage14/archive/stage14-4aa-parametrization-input-audit.md
stages/stage14/data/14-4/proof_input_audit.json
```

## What remains unknown

Stage14-4aa does not identify the true growth order, a leading constant, a bounded/unique parameter multiplicity, a limiting directional vector, or an eventual directional leader.

Next:

```text
14-4ab  audit representation multiplicity and reduce the three-triple gluing
        to an explicit countable matching/divisibility parameter space
```
