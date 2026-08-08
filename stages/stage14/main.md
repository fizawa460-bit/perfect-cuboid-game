# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AB_COMPLETE_R03_FULL_ACCESS_14_4AC_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals. Stage14-1 through Stage14-3 are complete. Stage14-4 is active at proof level. The reviewed Stage13 R03 map is now fully available as upstream machinery, while the Stage14 two-face parametrization remains independently derived.

## §1. Locked counting convention

For `B>=1`, count positive integers satisfying

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
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

The exactly-two directional populations are

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

No perfect-cuboid nonexistence assumption is made. Any `T>0` object remains an exact perfect-cuboid candidate and must be retained.

## §2. Frozen finite facts

Two materially different exact cuboid-generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the verified ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

Stage14-3 established only finite directional geography. In particular, the coarse `a/c=7/4` pattern failed under densification, and no limiting directional vector was inferred.

Canonical finite synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

## §3. Stage13 R03 upstream map — fully available

Stage14 may now use the reviewed R03 proof map and the post-review Stage13-12ag supplement:

```text
stages/stage13/13-12af/current-proof.md
stages/stage13/13-12ag/result.md
```

Current repository review record:

```text
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
UPSTREAM_STAGE13_REVIEWED_SNAPSHOT=STAGE13-FINAL-SELF-CONTAINED-20260809-R03
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_CLAUDE_VERDICT=NOT_RECORDED_AT_CURRENT_REPO_CHECKPOINT
R03_FULL_ACCESS_AUTHORIZED=true
UPSTREAM_STAGE13_FINAL_REPOSITORY_FREEZE=false
```

The final repository freeze flag is bookkeeping. The mathematical R03 map is available to Stage14.

The imported raw directional theorem candidate is

\[
\boxed{
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

R03 also supplies

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}
\]

for every raw pair direction and

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

Hence Stage14 may record the inherited ceiling

\[
\boxed{
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3).
}
\]

This does not determine the true two-face order. Stage14-4 seeks a sharper intrinsic law.

## §4. Stage14-4aa — one arithmetic object for all directions

Let `e` be the edge shared by the two integral faces, and let `x<y` be the nonshared edges. Let the face diagonals be `u,v`. Then a raw pair object satisfies

\[
e^2+x^2=u^2,
\qquad e^2+y^2=v^2,
\qquad u^2+y^2=d^2,
\qquad v^2+x^2=d^2.
\]

Only three Pythagorean equations are independent.

The three directions are exactly the three chamber positions of the shared edge:

```text
a-direction: e<x<y
b-direction: x<e<y
c-direction: x<y<e
```

Thus all directions share one arithmetic object; direction is a chamber inequality.

The exactly-two / triple split is

```text
x^2+y^2 nonsquare  -> exactly two
x^2+y^2 square     -> triple T
```

For a primitive Euclid base define

\[
L_D=m^2-n^2,\qquad L_P=2mn,\qquad H=m^2+n^2.
\]

Stage14-4aa writes the two face triples with arbitrary positive scales and matches them along the shared edge. A third Euclid triple imposes `(u,y,d)`. Stage14-4ab now removes the redundant scale and third-triple variables exactly.

## §5. Stage14-4ab — exact shared-edge matching reduction

### §5.1 Oriented primitive face data

An oriented primitive face datum is

\[
F=(S,X,H),
\]

where `S` is the primitive Pythagorean leg designated to become the shared edge and `X` is the other leg. Thus

\[
S=L_\sigma(m,n),\qquad X=L_{\bar\sigma}(m,n),\qquad H=m^2+n^2
\]

for one unique primitive Euclid base and one leg role `sigma`.

For each datum,

\[
\gcd(S,X)=\gcd(S,H)=\gcd(X,H)=1.
\]

Every positive integer Pythagorean triangle with a distinguished leg has a unique form

\[
(kS,kX,kH).
\]

### §5.2 Solve the shared-edge scale equation

Take

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2)
\]

and write

\[
(e,x,u)=k_1(S_1,X_1,H_1),
\]

\[
(e,y,v)=k_2(S_2,X_2,H_2).
\]

The shared-edge equation is

\[
k_1S_1=k_2S_2.
\]

Put

\[
g=\gcd(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

Then `(alpha,beta)=1`, and the complete positive solution is

\[
\boxed{k_1=t\beta,\qquad k_2=t\alpha,\qquad t\ge1.}
\]

Therefore

\[
\begin{aligned}
e&=tg\alpha\beta,\\
x&=t\beta X_1,\\
y&=t\alpha X_2,\\
u&=t\beta H_1,\\
v&=t\alpha H_2.
\end{aligned}
\]

### §5.3 Primitive cuboids force exactly `t=1`

Define the minimal glued edges

\[
e_0=g\alpha\beta,
\qquad x_0=\beta X_1,
\qquad y_0=\alpha X_2.
\]

Stage14-4ab proves

\[
\boxed{\gcd(e_0,x_0,y_0)=1.}
\]

Indeed a prime dividing `alpha` cannot divide `x_0`; a prime dividing `beta` cannot divide `y_0`; and a prime dividing only the common factor `g` of `S_1,S_2` divides neither primitive complementary leg.

Since

\[
(e,x,y)=t(e_0,x_0,y_0),
\]

we have the exact identity

\[
\boxed{\gcd(e,x,y)=t.}
\]

Thus global primitive cuboids force

\[
\boxed{t=1.}
\]

This is not the incorrect condition `k_1=k_2=1`. The actual primitive face scales are

\[
\boxed{k_1=\beta=S_2/g,\qquad k_2=\alpha=S_1/g,}
\]

which may be large.

Hence the primitive minimal gluing is

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
u&=\beta H_1,\\
v&=\alpha H_2.
\end{aligned}}
\]

No free global scale remains.

### §5.4 Representation multiplicity is exactly one

The convention `x<y` removes the swap of the two nonshared faces.

For a fixed raw pair incidence:

1. `(e,x,u)` and `(e,y,v)` are fixed physical triangles;
2. each has a unique scale-times-primitive-Euclid decomposition with the shared leg distinguished;
3. primitivity forces the common matching scalar `t=1`;
4. `x<y` fixes the order of the two face data.

Therefore

\[
\boxed{\text{parameter-fiber multiplicity}=1.}
\]

A triple object contributes three intended raw pair incidences, one per shared edge; this is the genuine `T` incidence structure, not duplicate parametrization of one incidence.

### §5.5 The third Euclid triple is not independent

After minimal gluing,

\[
u=\beta H_1,\qquad y=\alpha X_2.
\]

Thus the space-diagonal condition is exactly

\[
\boxed{(\beta H_1)^2+(\alpha X_2)^2=d^2.}
\]

Equivalently,

\[
(\alpha H_2)^2+(\beta X_1)^2=d^2.
\]

Let

\[
h=\gcd(\beta H_1,\alpha X_2).
\]

Using the primitive face coprimalities and `(alpha,beta)=1`,

\[
\boxed{h=\gcd(H_1,X_2).}
\]

If the square condition holds, dividing `(u,y,d)` by `h` gives a primitive Pythagorean triple, whose Euclid parameters are unique. Therefore the third triple introduced in 14-4aa is recovered uniquely with

\[
\boxed{k_3=\gcd(H_1,X_2).}
\]

It contributes no independent parameter sum.

### §5.6 Exact bijective parameter space

Stage14 raw pair incidences are now parametrized bijectively by two oriented primitive face data.

Choose

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2),
\]

put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g,
\]

and form

\[
\boxed{
\begin{aligned}
e&=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

Then impose exactly

```text
x<y
d^2 is a perfect square
d<=B
```

for a raw pair incidence.

The resulting glued cuboid is automatically primitive; no extra gcd filter remains.

Finally classify

```text
x^2+y^2 nonsquare -> exactly two
x^2+y^2 square    -> T
```

and apply the chamber test for `a/b/c`.

Thus the 14-4aa three-triple fiber product has reduced to

```text
two oriented primitive Euclid face data
+ gcd(S1,S2)
+ one exact diagonal-square condition
+ x<y
+ one shared-edge chamber test
```

with exact fiber multiplicity one.

## §6. Independent finite audit of the bijection

A new Stage14-4ab enumerator uses only the two-face primitive parameter space above. It does not use the Stage14-2 cuboid-edge-first production route.

It reproduces the locked exactly-two counts

```text
B=1000   (2,0,0)
B=2000   (2,2,1)
B=5000   (6,6,3)
B=10000  (9,11,5)
```

with `T=0` at all four cutoffs.

Artifacts:

```text
stages/stage14/archive/stage14-4ab-matching-reduction.md
stages/stage14/scripts/14-4/bijection_audit.py
stages/stage14/data/14-4/bijection_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

The finite agreement validates the new coordinates but is not an asymptotic proof.

## §7. Locked Stage14-4ab decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
R03_FULL_ACCESS_AUTHORIZED=true
R03_PAIR_OVERLAP_LITTLE_O_IMPORTED=true
R03_TRIPLE_OVERLAP_LITTLE_O_IMPORTED=true
SHARED_EDGE_SCALE_SOLUTION_EXACT=true
GLOBAL_COMMON_SCALE_EQUALS_CUBOID_GCD=true
PRIMITIVE_COMMON_SCALE_T=1=true
MINIMAL_GLUING_AUTOMATICALLY_PRIMITIVE=true
FIXED_RAW_PAIR_PARAMETER_FIBER_MULTIPLICITY=1
THIRD_EUCLID_TRIPLE_INDEPENDENT=false
THIRD_TRIPLE_SCALE_K3=gcd(H1,X2)
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
BIJECTION_FINITE_AUDIT_PASS=true
INHERITED_TWO_FACE_CEILING=o(B(log B)^3)
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false
DIRECTIONAL_LIMIT_IDENTIFIED=false
```

## §8. Next — Stage14-4ac

The next task is to convert the exact bijection into a height/divisibility counting envelope.

Immediate targets:

```text
rewrite d<=B explicitly in primitive face parameters
track g=gcd(S1,S2), alpha, beta and gcd(H1,X2)
identify divisor/logarithmic multiplicities
use R03 fixed-local and harmonic tools where genuinely applicable
seek a rigorous bound sharper than o(B(log B)^3)
only then test candidate true growth orders
```

```text
NEXT=Stage14-4ac height inequality and arithmetic counting envelope
```
