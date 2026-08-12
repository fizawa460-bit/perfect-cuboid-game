# Stage15-2b — third-face thin cover and the ambient `M_2(B)` asymptotic

Base: merged Stage15-2a (`PR #827`, main commit `2345d70`). Stage15-2a identified the shared-edge surface as a split toric singular quartic del Pezzo with smooth toric resolution

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad \rho(Y)=6,
\]

and left one exact gate open: prove that the third-face-square locus is negligible before transferring the toric main term to the exactly-two count `M_2(B)`.

## 1. Result

That subtraction gate closes.

Let `M_3(B)` denote primitive canonical Euler bricks, i.e. triples with all three integral face diagonals and the common Stage15 geometric cutoff

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}\le B.
\]

Then

\[
M_3(B)=o\!\left(B(\log B)^5\right).
\]

Moreover there is a constant `C_M2>0` such that

\[
\boxed{M_2(B)\sim C_{M_2}\,B(\log B)^5.}
\]

Thus the logarithmic exponent left open in Stage15-2 and Stage15-2a is exactly five. The constant is a positive toric/Tamagawa chamber constant; Stage15-2b does not evaluate it numerically.

The same argument gives directional asymptotics. If `M_{2,a}`, `M_{2,b}`, `M_{2,c}` denote exactly-two boxes whose unique shared edge is respectively the smallest, middle, or largest canonical edge, then

\[
M_{2,j}(B)\sim C_j B(\log B)^5\qquad (j=a,b,c)
\]

with `C_j>0`, and `C_M2=C_a+C_b+C_c`.

```text
THIRD_FACE_COVER_IDENTIFIED=true
THIRD_FACE_COVER_DEGREE=2
THIRD_FACE_COVER_GEOMETRICALLY_INTEGRAL=true
THIRD_FACE_COVER_MINIMAL_RESOLUTION=K3
THIRD_FACE_IMAGE_THIN_TYPE_II=true
M3_MAIN_TERM_NEGLIGIBLE=true
M3_BOUND=o(B(log B)^5)
STAGE15_R_IS_ANTICANONICAL_HEIGHT=true
M2_ASYMPTOTIC_PROVED=true
M2_LOG_POWER_PROVED=true
M2_LOG_POWER=5
M2_ASYMPTOTIC_CONSTANT_POSITIVE=true
M2_ASYMPTOTIC_CONSTANT_EXPLICIT=false
M2_DIRECTIONAL_ASYMPTOTICS_PROVED=true
DIRECT_M2_TORIC_TRANSFER=true
STAGE15_2B_EXIT=M2_ASYMPTOTIC_PROVED
```

## 2. Exact shared-edge counting space

Use the Stage15-2a projective shared-edge model

\[
X:\quad u^2=e^2+x^2,\qquad v^2=e^2+y^2
\]

in `P^4_[e:x:y:u:v]`. Its minimal desingularization `Y` is the smooth split toric surface `Bl_4(P1 x P1)` and the morphism `Y -> X` is anticanonical.

Let `T subset Y` be the dense torus. A rational point in the physical real chamber is represented uniquely by primitive integral projective coordinates after imposing

```text
e>0, x>0, y>0, u>0, v>0, x<y.
```

The two displayed quadrics then say that the two faces through the distinguished edge `e` have integral diagonals `u,v`.

Projective primitiveness matches the Stage15 primitive convention. Indeed

\[
\gcd(e,x,y)=1
\]

if and only if the primitive integral projective representative has no common divisor in all five coordinates: any common divisor of `e,x,y` also divides `u,v` by the two Pythagorean equations.

## 3. The Stage15 height is an anticanonical height, not only a comparable one

Stage15-2a proved comparison with the standard projective sup height. For the transfer theorem one can sharpen the statement.

For a primitive integral representative define

\[
H_R([e:x:y:u:v])=\sqrt{e^2+x^2+y^2}.
\]

This is homogeneous of degree one in the projective coordinates. On `X(R)` it is everywhere positive: `e=x=y=0` would force `u=v=0`, which is not a projective point. Hence the Euclidean norm above defines a continuous archimedean metric on `O_X(1)`; at finite places take the standard integral projective metric.

Because Stage15-2a proved

\[
\pi^*O_X(1)\cong -K_Y,
\]

`H_R` is an anticanonical adelic height on `Y`. For primitive integral coordinates its value is exactly the Stage15 cutoff `R`, not merely a constant-factor substitute.

Therefore external anticanonical toric counting theorems may be applied without changing the Stage15 denominator.

## 4. Full physical shared-edge asymptotic

Batyrev--Tschinkel prove Manin's anticanonical asymptotic for arbitrary smooth projective toric varieties. Huang proves the corresponding Manin--Peyre equidistribution for smooth proper split toric varieties, including asymptotic counting in adelic neighbourhoods.

Apply these results to the smooth split toric surface `Y` with `rho(Y)=6` and the anticanonical height `H_R`. On the dense torus,

\[
N_T(B)\sim c_T B(\log B)^{\rho(Y)-1}=c_T B(\log B)^5.
\]

Now impose the physical real-place inequalities

\[
e,x,y,u,v>0,\qquad x<y.
\]

Their boundary is contained in finitely many real algebraic hypersurfaces and has Tamagawa measure zero. By archimedean equidistribution, the restricted count has

\[
A(B)\sim C_A B(\log B)^5
\]

for a positive constant `C_A`: positivity follows because the chamber is a nonempty open subset of the real torus.

Here `A(B)` counts primitive physical shared-edge incidences with at least the two faces through `e` integral; it does not yet exclude a square third face.

## 5. Exact incidence identity

Every exactly-two box has one unique shared edge. After assigning that edge to `e` and ordering the other two legs by `x<y`, it contributes exactly one point to `A(B)`.

Every Euler brick has all three edges as possible shared edges. For each choice of `e`, ordering the two remaining legs by `x<y` gives exactly one point. Therefore

\[
\boxed{A(B)=M_2(B)+3M_3(B).}
\]

Direction by direction, if `A_a,A_b,A_c` are the three subchambers

```text
C_a: e<x<y
C_b: x<e<y
C_c: x<y<e,
```

then

\[
A_j(B)=M_{2,j}(B)+M_3(B),\qquad j=a,b,c.
\]

Each chamber is nonempty already at the elementary level:

```text
shared smallest: (e,x,y;u,v)=(12,16,35;20,37)
shared middle:   (20,15,21;25,29)
shared largest:  (60,11,25;61,65)
```

and in each case `x^2+y^2` is nonsquare. Hence each chamber has positive archimedean measure and a positive toric leading constant.

## 6. Third-face-square cover

The forbidden third face is square precisely when

\[
z^2=x^2+y^2.
\]

Adjoin `z` and form

\[
W_0\subset \mathbf P^5_{[e:x:y:u:v:z]}
\]

with equations

\[
\begin{aligned}
u^2&=e^2+x^2,\\
v^2&=e^2+y^2,\\
z^2&=x^2+y^2.
\end{aligned}
\]

Forgetting `z` gives a generically degree-two map

\[
\varpi:W_0\longrightarrow X.
\]

Over the dense torus, pull this cover back through the resolution `Y -> X`.

### 6.1 Geometric integrality

The cover is not split over the geometric function field. Over `Qbar`,

\[
x^2+y^2=(x+i y)(x-i y).
\]

At the generic point of the divisor `x+i y=0` on the torus, the other factor is nonzero and the valuation of `x^2+y^2` is one. Hence `x^2+y^2` is not a square in `\overline{\mathbf Q}(Y)`.

Therefore the cover is geometrically integral and generically finite of degree two. Its rational image in `T(Q)` is consequently a type-II thin subset in the sense of Serre.

A concrete exact-two witness also shows nontriviality over `Q`:

\[
(e,x,y;u,v)=(60,11,91;61,109),
\]

for which

\[
x^2+y^2=8402
\]

is not a square.

### 6.2 K3 geometry of the cover

The projective model `W_0` is a complete intersection of three quadrics in `P^5`, of degree eight. Adjunction gives

\[
K_{W_0}=O_{W_0}(-6+2+2+2)=O_{W_0}
\]

on the smooth locus.

The Jacobian has rank drop at the twelve rational points obtained from

```text
(e,x,y)=(0,0,1), with v,z=+-1 and u=0;
(e,x,y)=(0,1,0), with u,z=+-1 and v=0;
(e,x,y)=(1,0,0), with u,v=+-1 and z=0.
```

At each such point two equations solve linearly for two coordinates and the remaining local equation is a nondegenerate quadratic cone, so these are `A1` rational double points. Resolving them preserves the trivial canonical class; the resulting smooth minimal surface is a K3 surface.

This geometry explains why direct counting on the cover is not the easiest route. The thin-set theorem avoids needing an independent K3 rational-point asymptotic.

## 7. Thin-set zero-density theorem

Use Browning--Loughran, *Sieving rational points on varieties*, Theorem 1.2:

> On an almost Fano variety with equidistributed anticanonical rational points on a dense open subset, every thin subset has zero density in the bounded-height count.

The hypotheses hold for `Y`:

- `Y` is smooth, projective, split toric;
- `H^1(Y,O_Y)=H^2(Y,O_Y)=0`;
- `Pic(Y)` is torsion free;
- `-K_Y` is big (`K_Y^2=4`);
- toric anticanonical rational points are equidistributed on the dense torus.

Let `Theta` be the image in `T(Q)` of the geometrically integral degree-two cover above. Then

\[
\#\{P\in\Theta:H_R(P)\le B\}
=o\!\left(N_T(B)\right)
=o\!\left(B(\log B)^5\right).
\]

Every physical Euler-brick incidence lies in `Theta`. Hence

\[
3M_3(B)\le \#\{P\in\Theta:H_R(P)\le B\}
=o\!\left(B(\log B)^5\right),
\]

so

\[
\boxed{M_3(B)=o(B(\log B)^5).}
\]

No unproved K3 counting conjecture is used.

## 8. Transfer to `M_2(B)`

Combine

\[
A(B)\sim C_A B(\log B)^5
\]

with

\[
A(B)=M_2(B)+3M_3(B)
\]

and the thin estimate for `M_3`. Then

\[
M_2(B)=C_A B(\log B)^5+o(B(\log B)^5).
\]

Thus `C_M2=C_A>0`, proving

\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5.}
\]

Likewise, in each directional chamber

\[
A_j(B)\sim C_jB(\log B)^5,
\qquad
A_j(B)=M_{2,j}(B)+M_3(B),
\]

so

\[
M_{2,j}(B)\sim C_jB(\log B)^5
\]

with `C_j>0`.

## 9. What is and is not proved

Proved in Stage15-2b:

- exact logarithmic exponent `5` for `M_2(B)`;
- a positive leading constant exists;
- triple-face/Euler-brick subtraction is lower order;
- each shared-edge direction has the same `B(log B)^5` scale with its own positive constant.

Not proved here:

- a closed numerical formula for `C_M2` or the directional constants;
- an effective power/log saving for `M_3(B)` beyond little-`o`;
- any asymptotic for Euler bricks themselves;
- any statement about existence or nonexistence of perfect cuboids.

The Stage15-3 finite A/B comparison can now use a proved ambient denominator rather than only the polynomial-exponent bound from Stage15-2.

## 10. Literature contract

The transfer uses the following external results only at their stated interfaces.

1. V. Batyrev and Y. Tschinkel, *Manin's conjecture for toric varieties*, arXiv:alg-geom/9510014. Anticanonical bounded-height asymptotic for arbitrary smooth projective toric varieties.
2. T. Browning and D. Loughran, *Sieving rational points on varieties*, arXiv:1705.01999, Theorem 1.2. Thin subsets have zero density under the stated almost-Fano/equidistribution hypotheses.
3. Z. Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509, current v3. Manin--Peyre equidistribution for smooth proper split toric varieties and counting in adelic neighbourhoods.

The K3 identification and the physical-incidence identities are proved directly above and are not imported from the literature.

## 11. Exit

Stage15-2 has now answered all six questions in its roadmap at the level needed for the comparison project:

```text
M2_INFINITE=true
M2_COMPLETE_SHARED_EDGE_MODEL=true
M2_GROWTH_SCALE=B(log B)^5
M2_MATCHING_ORDER_PROVED=true
M2_ASYMPTOTIC_PROVED=true
M2_DIRECTIONAL_ASYMPTOTICS_PROVED=true
```

Next primary roadmap target: `Stage15-3`, the matched numerical A/B comparison under the now-proved ambient denominator.
