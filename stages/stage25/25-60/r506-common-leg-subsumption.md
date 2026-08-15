# Stage25-60 R506 — common-leg + space is the R505 toric receiver

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R506
ROLE=ITERATIVE_CHECKPOINT60_ROUTE_SUBSUMPTION_CERTIFICATE

## 1. Start from the Stage19 toric variables

Use the same primitive positive toric parameters `m,n,r,s` as in R505 and set

\[
u=mr,\qquad v=ns,\qquad w=ms,\qquad z=nr.
\]

Then

\[
\boxed{uv=wz}.
\]

Equivalently

\[
\det\begin{pmatrix}u&w\\z&v\end{pmatrix}=0.
\]

So the four apparent common-leg coordinates lie on a rank-one determinantal variety; they do not supply four independent parameters.

The two Stage19 norm factors become

\[
\boxed{A=u^2+v^2},
\qquad
\boxed{B=w^2+z^2}.
\]

Therefore the space condition is exactly the R505 common-core condition

\[
\operatorname{sf}(u^2+v^2)=\operatorname{sf}(w^2+z^2),
\]

or equivalently

\[
u^2+v^2=kP^2,\qquad w^2+z^2=kQ^2.
\]

## 2. Converse reconstruction

The rank-one relation is not merely necessary. For positive rational `u,v,w,z` with

\[
uv=wz,
\]

the toric ratios are reconstructed by

\[
\boxed{m:n=u:z=w:v},
\]

\[
\boxed{r:s=u:w=z:v}.
\]

Indeed `uv=wz` is precisely the consistency relation needed for these ratio equalities. Choosing positive rational representatives for the two projective ratios and clearing denominators recovers a toric quadruple `(m,n,r,s)`; the ordinary primitive/canonical normalization then returns to the existing Stage19 population contract.

Thus the common-leg coordinates and the original toric coordinates are birational/projectively equivalent on the positive dense locus, up to the already present finite scaling/normalization choices.

```text
R506_U=mr
R506_V=ns
R506_W=ms
R506_Z=nr
R506_RANK_ONE_IDENTITY=uv=wz
R506_A=u^2+v^2
R506_B=w^2+z^2
R506_TORIC_RECONSTRUCTION_PROJECTIVE_UNIQUE=true
```

## 3. Consequence for route independence

R506 was retained as a possible separate construction lane because a “common leg + space norm” factorization can look like an extra degree of freedom. The determinant identity shows that this is coordinate illusion: the common-leg data remain on the same rank-one toric incidence space, and the additional space requirement is exactly R505's common squarefree-core receiver.

Therefore R506 does not provide an independent parameter dimension, an independent target equation, or an independent population measure.

Any future **specific** common-leg formula that produces a new low-height subfamily is still valuable, but mathematically it is a new subfamily inside the R505/Stage19 exact receiver. Such a discovery would reopen the construction search and, if genuinely distinct, may be assigned R508+; it does not justify keeping R506 as an independent unresolved lane today.

## 4. Boundary

```text
R506_INDEPENDENT_PARAMETER_DIMENSION=false
R506_INDEPENDENT_TARGET_RECEIVER=false
R506_SUBSUMED_BY_R505_EXACT_TORIC_RECEIVER=true
R506_STATUS=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R506_REOPEN_CONDITION=NEW_EXPLICIT_COMMON_LEG_SUBFAMILY_WITH_NEW_HEIGHT_GEOMETRY
GLOBAL_STAGE25_LOWER_CHANGED=false
FINITE_DATA_USED_AS_PROOF=false
```

This closes only the claim that R506 is a separate research route. It does not forbid future explicit common-leg constructions inside the common-core receiver.
