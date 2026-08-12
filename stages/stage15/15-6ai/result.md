# Stage15-6ai — exact projective classification of the small-support one-point receiver

Base: Stage15-6ah head `81befe1b` (`PR #840`, still open when this substage was started). This is a stacked continuation: 6ai changes only new 6ai files and assumes the 6ah reduction as predecessor input.

Stage15-6ah exhausted all large **total** two-point common support. The residual population has small full good common support `J`, including `J=1`, so no useful pair modulus is forced. Stage15-6ai therefore returns to the exact one-point receiver from 6ad/6ae and classifies its projective geometry before any genus-one/conic counting theorem is considered.

No counting theorem is applied in this substage.

## 1. Exact homogeneous receiver in P^3

Fix one legally charged low-core physical fiber. Thus

```text
m>n>0
h_alpha,h_beta>0
K_alpha=A+iB
K_beta=C+iD
N(K_alpha)=N(K_beta)=k>0
```

are fixed, while

```text
z=a+ib,
w=u+iv
```

vary. Put

\[
X=A(a^2-b^2)-2Bab,
\qquad
Y=B(a^2-b^2)+2Aab.
\]

Merged Stage15-6ae gives the exact complex equation

\[
mn h_\beta K_\beta w^2
=h_\alpha\left(m^2Y+i n^2X\right).
\]

Writing `M=mn h_beta` and `H=h_alpha`, this is exactly the pair of homogeneous quadrics

\[
\boxed{
Q_1:=M\{C(u^2-v^2)-2Duv\}-Hm^2Y=0,
}
\]

\[
\boxed{
Q_2:=M\{D(u^2-v^2)+2Cuv\}-Hn^2X=0.
}
\]

Hence the exact low-core one-point receiver is a degree-`(2,2)` complete-intersection candidate

\[
\mathcal C_{m,n,\mathrm{dec}}:=V(Q_1,Q_2)\subset \mathbf P^3_{a:b:u:v}.
\]

This is the **exact** Gaussian-square target, not the norm-quartic projection from 6ae. The norm quartic remains only a necessary projection and is not substituted for `C_{m,n,dec}`.

## 2. Universal diagonal form over Qbar

Let

\[
s=m^2+n^2,\qquad d=m^2-n^2.
\]

Over `Qbar`, all nonzero fixed core/cross-gcd coefficients can be absorbed by invertible linear scalings. Use complex linear coordinates built from

\[
p=a+ib,\quad q=a-ib,\quad x=u+iv,\quad y=u-iv,
\]

and absorb square roots of the fixed nonzero constants `K_alpha`, `K_beta`, `M`, `H`, and `i`. The two quadrics become

\[
\boxed{
R^2=sQ^2-dP^2,
\qquad
S^2=dQ^2-sP^2.
}
\]

Equivalently,

\[
F_1:=R^2+dP^2-sQ^2=0,
\qquad
F_2:=S^2+sP^2-dQ^2=0.
\]

Therefore the Gaussian cores and cross-gcd decorations are **twist data** for the projective curve. Geometric smoothness is controlled by the physical outer pair `(m,n)`.

```text
STAGE15_6AI_QBAR_UNIVERSAL_DIAGONAL_FORM=true
STAGE15_6AI_CORE_DATA_ARE_PROJECTIVE_TWISTS=true
```

## 3. Pencil discriminant and exact smoothness

The pencil `lambda F_1+mu F_2` is diagonal in `(P,Q,R,S)`. Its determinant is, up to a fixed nonzero scalar,

\[
\boxed{
-\lambda\mu(d\lambda+s\mu)(s\lambda+d\mu).
}
\]

Thus the four singular members of the pencil occur at

\[
[\lambda:\mu]
=
[0:1],\ [1:0],\ [-s:d],\ [-d:s].
\]

For the physical toric chamber `m>n>0`,

\[
d>0,\qquad s>0,
\]

and

\[
s^2-d^2=4m^2n^2>0.
\]

Hence all four pencil parameters are distinct.

A direct Jacobian check now proves smoothness without an external counting theorem. If a point of `V(F_1,F_2)` were singular, some nonzero pencil member would have zero gradient at that point. Since the pencil is diagonal, every nonzero coordinate of the point would force the corresponding diagonal coefficient to vanish. A projective point on both quadrics cannot have only one nonzero coordinate, so at least two diagonal coefficients would need to vanish for the same `[lambda:mu]`. Distinctness of the four pencil roots forbids this.

Therefore

\[
\boxed{\mathcal C_{m,n,\mathrm{dec}}\text{ is geometrically smooth for every physical }m>n>0.}
\]

The affine cubic part of the pencil discriminant has marker

\[
\boxed{
d^2s^2(s^2-d^2)^2\ne0.}
\]

The only algebraic degeneration conditions are outside the physical chamber: `d=0` (`m=n`), `s=0`, or `s^2=d^2` (forcing `mn=0` over the rational outer parameters).

```text
STAGE15_6AI_PHYSICAL_PENCIL_ROOTS_DISTINCT=true
STAGE15_6AI_PHYSICAL_CURVE_SMOOTH=true
STAGE15_6AI_PHYSICAL_SINGULAR_CONIC_BRANCH=false
```

## 4. Geometric integrality and genus

On the `Q!=0` chart of the universal form, put `t=P/Q`. Then

\[
(R/Q)^2=s-dt^2,
\qquad
(S/Q)^2=d-st^2.
\]

The two quadratic polynomials on the right have simple, disjoint root sets because `d s (s^2-d^2)!=0`. Their squareclasses are independent in `Qbar(t)^*/Qbar(t)^{*2}`: neither polynomial is a square, and their product has four simple roots and is not a square. Thus adjoining both square roots gives a degree-four field extension of `Qbar(t)`. The projective complete intersection is therefore geometrically integral.

A smooth complete intersection of two quadrics in `P^3` has degree `4`. Its canonical class is

\[
K_{\mathcal C}
=(K_{\mathbf P^3}+2H+2H)|_{\mathcal C}
=\mathcal O_{\mathcal C},
\]

so `deg K_C=0=2g-2`. Therefore

\[
\boxed{g(\mathcal C_{m,n,\mathrm{dec}})=1.}
\]

So the exact one-point low-core receiver is not generically genus one with exceptional physical conics: it is **always a smooth geometrically integral genus-one curve in the physical chamber**.

For a populated physical fiber, the survivor itself supplies a rational point `[a:b:u:v]`, so that particular curve may be viewed as an elliptic curve after choosing an origin. This does not give a uniform counting theorem and is not used as a saving.

```text
STAGE15_6AI_GEOMETRICALLY_INTEGRAL=true
STAGE15_6AI_COMPLETE_INTERSECTION_DEGREE=4
STAGE15_6AI_GEOMETRIC_GENUS=1
STAGE15_6AI_POPULATED_FIBER_HAS_RATIONAL_POINT=true
```

## 5. The family moves with the outer ratio

The four pencil roots retain nontrivial outer-pair information. For example, with the ordering `(infinity,0,-s/d,-d/s)`, one cross-ratio is

\[
\boxed{\rho=\left(\frac d s\right)^2
=\left(\frac{m^2-n^2}{m^2+n^2}\right)^2,}
\]

up to the usual six cross-ratio transforms from reordering the four points.

Thus the projective pencil is not a single fixed genus-one curve with harmless coefficient scaling. As `(m,n)` moves, the pencil moduli move. The core/cross-gcd data are twists, but the outer ratio changes the geometric pencil itself.

This is crucial for the next counting gate: a theorem for one fixed elliptic curve, one fixed rank, or one fixed discriminant cannot be silently promoted to the whole Stage15 physical outer measure.

```text
STAGE15_6AI_PENCIL_CROSS_RATIO=(d/s)^2_UP_TO_S3
STAGE15_6AI_MOVING_OUTER_GEOMETRY=true
STAGE15_6AI_SINGLE_FIXED_ELLIPTIC_CURVE_REDUCTION=false
```

## 6. Relation to the small-total-support branch

The condition `J<L` from 6ah is a **two-point support condition**. It does not alter the exact one-point equations above. Once the pair-overlap mechanism is exhausted, each remaining point is still hosted by the same fixed-fiber genus-one curve `C_{m,n,dec}`.

Therefore 6ai does not claim that small `J` itself cuts out a subcurve. Rather, it identifies the arithmetic object that must now be counted when no useful shared modulus is available.

The one-point problem is now:

```text
fixed physical outer/core/gcd/orientation fiber
-> smooth genus-one (2,2) curve C in P^3
-> count primitive integral/rational representatives satisfying the original divisibility,
   positivity, dyadic-height, canonical and exactly-two masks
-> sum uniformly over the original physical outer measure
```

## 7. Arsenal / theorem-species audit

The Stage14 Arsenal contains no direct theorem that counts this exact moving genus-one family in the Stage15 physical outer-pair measure.

```text
ARSENAL_DIRECT_GENUS_ONE_COUNT_MATCH=false
AR-016=FINITE_TWIST_AND_RECONSTRUCTION_DECORATIONS_ONLY
AR-023=OUTER_PAIR_MEASURE_MUST_NOT_BE_SCALARIZED
AR-024=COMMON_KERNEL_DOES_NOT_TRANSFER_A_DIFFERENT_MEASURE_THEOREM
AR-027=AVERAGED_CURVE_FAMILY_THEOREM_REQUIRES_EXCEPTIONAL_SET_BRIDGE
AR-028=NO_RECHARGE_OF_CORE_OR_PAIR_SUPPORT
AR-030=PHYSICAL_MASKS_RETAINED_AS_MONOTONE_POSTFILTERS_FOR_UPPER_BOUNDS
```

No genus-one/elliptic counting result is imported in 6ai. In particular, no rank bound, integral-point theorem, determinant-method estimate, average Selmer theorem, or almost-all-curve statement is invoked.

Before any such theorem can be used, Stage15 must first normalize:

1. the integral genus-one model and coefficient size/discriminant;
2. the relation between projective/elliptic height and the original physical `R<=B` / dyadic fiber;
3. twist multiplicity already charged in 6ab--6ad;
4. quantifiers over every fixed outer fiber versus averages over `(m,n)`;
5. the retained physical post-filters.

```text
STAGE15_6AI_GENUS_ONE_COUNTING_THEOREM_APPLIED=false
STAGE15_6AI_HEIGHT_MEASURE_ADAPTER_PROVED=false
STAGE15_6AI_EXTERNAL_THEOREM_SEARCH_OPENED=false
```

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ai
STAGE15_6AI_STARTING_GATE=CLASSIFY_SMALL_SUPPORT_ONE_POINT_PROJECTIVE_MODEL
STAGE15_6AI_EXACT_MODEL=TWO_QUADRICS_IN_P3
STAGE15_6AI_QBAR_UNIVERSAL_DIAGONAL_FORM=true
STAGE15_6AI_PENCIL_DETERMINANT=-lambda*mu*(d*lambda+s*mu)*(s*lambda+d*mu)
STAGE15_6AI_PHYSICAL_PENCIL_ROOTS_DISTINCT=true
STAGE15_6AI_PHYSICAL_CURVE_SMOOTH=true
STAGE15_6AI_GEOMETRICALLY_INTEGRAL=true
STAGE15_6AI_GEOMETRIC_GENUS=1
STAGE15_6AI_PHYSICAL_SINGULAR_CONIC_BRANCH=false
STAGE15_6AI_MOVING_OUTER_GEOMETRY=true
STAGE15_6AI_ARSENAL_DIRECT_COUNT_MATCH=false
STAGE15_6AI_GENUS_ONE_COUNTING_THEOREM_APPLIED=false
STAGE15_6AI_HEIGHT_MEASURE_ADAPTER_PROVED=false
STAGE15_6AI_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AI_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AI_EXIT=SMOOTH_MOVING_GENUS_ONE_FAMILY_HEIGHT_AUDIT_READY
```

## 9. Next narrow gate

Stage15-6aj should **not** jump directly to an elliptic-curve theorem. It should first build the height/coefficient bridge for this exact `(2,2)` family:

```text
physical R<=B and fixed dyadic fiber
<-> bounds for (a,b,u,v)
<-> coefficient/discriminant size of C_{m,n,dec}
<-> projective / genus-one height receiver
```

Only after that audit can Stage15 state the exact uniform theorem species needed for the small-support branch.