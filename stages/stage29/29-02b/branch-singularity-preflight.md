# Stage29-02b — branch/singularity preflight

```text
ROLE=BRANCH_INTERSECTION_AND_LOCAL_SINGULARITY_PREFLIGHT
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

This note does not attempt the full global resolution table reserved for roadmap item 29-07.  It checks the concrete local mechanisms that could invalidate the canonical-class preflight.

## 1. Exact affine factors

On the Stage28 affine chart `v1=v2=1`, write the toric parameters as `x=u1`, `y=u2`.  The two third-face branch components are

\[
F_\pm=y(x^2-1)\pm i x(y^2-1),
\]

and the four space branch components are

\[
S_1=xy-i,\quad S_2=xy+i,\quad S_3=x-iy,\quad S_4=x+iy.
\]

These are exactly the Stage28 factorisations, merely dehomogenized.

## 2. Same-colour crossings

The two face components intersect where

```text
y(x^2-1)=0,
x(y^2-1)=0.
```

Away from the toric corner this gives `(x,y)=(±1,±1)`.  At each such point the gradients of the two underlying summands are independent, so `F_+` and `F_-` cross transversally.  Locally the face double cover has the standard form

```text
u^2=rs,
```

hence an `A1` rational double point.  The joint cover is the same `A1` times an unramified quadratic coordinate locally.

Likewise the non-boundary intersections among distinct `S_j` are transverse; for example `S_1=S_3=0` has points `(i,1),(-i,-1)` and the Jacobian determinant of `(S_1,S_3)` is nonzero.  These produce the same `A1` local mechanism for the space marginal and the joint cover.

Thus the ordinary same-colour branch crossings are canonical/crepant singularities.

## 3. Different-colour transverse crossings

If a smooth face branch and a smooth space branch meet transversally, choose local base coordinates so they are `r=0` and `s=0`.  The joint cover is

```text
u^2=r,
v^2=s,
```

which is smooth with local coordinates `(u,v)`.

Therefore a transverse intersection of the two *different* branch colours is not a singularity of the total `V4` cover, even though it is a node of the cross-quotient branch union.

The cross quotient there is

```text
w^2=rs,
```

an `A1` rational double point, again crepant.

## 4. Boundary tangency at a toric corner

The blow-up in `Y=Bl_4(P1xP1)` matters.  At the representative corner `(x,y)=(0,0)`, use the blow-up chart `y=xz`.

For the matching pair `F_+` and `S_3`, after removing the common exceptional factor their strict transforms are

\[
\widetilde F_+=-(z+i)+x^2(z+iz^2),
\]

\[
\widetilde S_3=1-iz.
\]

They meet on the exceptional divisor at `z=-i`.  Put `w=z+i`.  Then

```text
F_tilde = -w - 2 i x^2 + higher terms,
S_tilde = -i w.
```

Hence the two smooth branch curves are tangent with intersection multiplicity two.

For the total joint cover, eliminate `w` using `v^2=S_tilde`.  The remaining local equation has nondegenerate quadratic leading form

```text
u^2 + unit*v^2 + unit*x^2 + higher = 0,
```

so the joint cover has an ordinary double point (`A1`) at this representative tangency.

For the cross quotient the local branch equation is the product of two smooth tangent branches of contact order two; the double cover has the standard `A3` rational-double-point type after analytic coordinate change.

The conjugate/symmetric corner pairs have the same local mechanism.  A complete global count of all such boundary singularities is deliberately left to 29-07; the point of this preflight is that the visible tangency corrections are ADE and therefore crepant, not a source of hidden canonical loss.

## 5. What is certified at preflight level

```text
SAME_COLOUR_TRANSVERSE_CROSSING_TYPE=A1
DIFFERENT_COLOUR_TRANSVERSE_JOINT_COVER=SMOOTH
DIFFERENT_COLOUR_TRANSVERSE_CROSS_QUOTIENT=A1
REPRESENTATIVE_BOUNDARY_TANGENCY_JOINT_TYPE=A1
REPRESENTATIVE_BOUNDARY_TANGENCY_CROSS_TYPE=A3
VISIBLE_LOCAL_CORRECTIONS_CREPANT=true
FULL_GLOBAL_SINGULARITY_ENUMERATION_COMPLETE=false
```

Thus no local model found in the exact Stage28 factorisation contradicts the canonical `K^2=16` joint-cover signal or the `K^2=8` cross-quotient signal.  The full global singularity inventory remains a later refinement rather than an unresolved conceptual blocker.
