# Stage14-t3 — Humbert-Edge structure and universal five-elliptic splitting

> STATUS: `STAGE14_T3_COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING`

Stage14-t3 classifies the exceptional and low-degree geometry of the fixed-base triple/perfect-cuboid curve. The main conclusion is stronger than an exceptional-stratum statement: the low-degree elliptic structure is **universal on every genuine physical Pythagorean base**.

## 1. From the two quartics to three diagonal quadrics

Fix a genuine first-face slope `t` and put

\[
s=t^2,\qquad
A=\frac{1-s}{1+s},\qquad
C=\frac2s-1.
\]

The t1 triple fiber is

\[
W^2=q^4+2Aq^2+1,\qquad
R^2=q^4+2Cq^2+1.
\]

Homogenize `q=Q/P` and set

\[
U_0=P^2+Q^2,\qquad
U_1=P^2-Q^2,\qquad
U_2=2PQ.
\]

Then the smooth projective fiber is birational to, and hence identified with, the complete intersection in `P^4_[U0:U1:U2:W:R]`

\[
\boxed{U_0^2-U_1^2-U_2^2=0},
\]

\[
\boxed{2W^2-U_0^2-U_1^2-AU_2^2=0},
\]

\[
\boxed{2R^2-U_0^2-U_1^2-CU_2^2=0}.
\]

These are three **diagonal quadrics**. Therefore every genuine Stage14-t fiber is a Humbert--Edge curve of type `4`. The standard genus formula

\[
g_n=2^{n-2}(n-3)+1
\]

gives

\[
\boxed{g_4=5},
\]

recovering the t1 genus computation in a much more rigid form.

## 2. Exact five-point branch orbifold

The coordinate-sign group

\[
H\cong(\mathbf Z/2\mathbf Z)^4
\]

has quotient `P^1`. With

\[
x=U_1^2/U_0^2,
\]

the five branch values are

\[
\boxed{
\infty,\quad 0,\quad 1,\quad -\frac1s,\quad \frac1{1-s}.
}
\]

Equivalently, if

\[
\lambda=-1/s,
\]

then the fifth value is

\[
\mu=\frac{\lambda}{\lambda+1}.
\]

Branch collision occurs only at

```text
s = 0, 1, -1, infinity,
```

which corresponds to the already-known projective exceptional set

```text
t = 0, ±1, ±i, infinity.
```

No genuine positive rational Pythagorean base lies in this set. Hence the physical singular/lower-genus exceptional contribution is exactly zero for every height cutoff.

## 3. Five elliptic quotients on every physical fiber

There are five distinguished coordinate involutions

```text
sigma_U0, sigma_U1, sigma_U2, sigma_W, sigma_R.
```

Quotienting a type-4 Humbert--Edge curve by any one of them gives a type-3 Humbert--Edge curve, hence a genus-one curve. The five quotient models are explicit intersections of two diagonal quadrics.

For `sigma_R`:

\[
U_0^2-U_1^2-U_2^2=0,
\qquad
2W^2-U_0^2-U_1^2-AU_2^2=0.
\]

For `sigma_W`:

\[
U_0^2-U_1^2-U_2^2=0,
\qquad
2R^2-U_0^2-U_1^2-CU_2^2=0.
\]

For `sigma_U2`:

\[
2W^2=(1+A)U_0^2+(1-A)U_1^2,
\]

\[
2R^2=(1+C)U_0^2+(1-C)U_1^2.
\]

For `sigma_U1`:

\[
2W^2=2U_0^2+(A-1)U_2^2,
\]

\[
2R^2=2U_0^2+(C-1)U_2^2.
\]

For `sigma_U0`:

\[
2W^2=2U_1^2+(A+1)U_2^2,
\]

\[
2R^2=2U_1^2+(C+1)U_2^2.
\]

All five are smooth on every physical rational base because their four relevant branch values are distinct subsets of the five-point orbifold.

The refined Humbert--Edge Jacobian decomposition for type `4` has exactly

\[
\binom54=5
\]

one-dimensional factors. Since all five quotient maps above are defined over `Q` for rational `t`, the induced isogeny is defined over `Q`:

\[
\boxed{
J(C_t)\sim_{\mathbf Q}
E_{U_0,t}\times E_{U_1,t}\times E_{U_2,t}\times E_{W,t}\times E_{R,t}.
}
\]

Consequently

\[
\boxed{
\operatorname{rank}J(C_t)(\mathbf Q)
=\sum_{i=1}^{5}\operatorname{rank}E_{i,t}(\mathbf Q).
}
\]

This turns the moving genus-5 rank obstruction from t2 into an explicit five-elliptic-rank problem.

## 4. Extra-automorphism strata

For a type-4 generalized Humbert curve the Humbert group is unique. Therefore any extra automorphism must normalize `H` and descend to a Möbius symmetry of the five branch values.

The deterministic t3 audit checks all `120` permutations of

\[
\{\infty,0,1,-1/s,1/(1-s)\}
\]

and solves exactly for the parameter values at which the permutation is induced by a Möbius transformation. Besides the degenerate factors `s`, `s-1`, `s+1`, the only possible nondegenerate loci are

\[
s^2+1=0,
\]

\[
s^2+s+1=0,\qquad s^2-s+1=0,
\]

\[
s^2+s-1=0,\qquad s^2-s-1=0.
\]

Their discriminants are `-4,-3,-3,5,5`. None has a rational root. Thus for every genuine physical base `s=t^2 in Q_{>0}` there is no nontrivial branch symmetry, and hence

\[
\boxed{\operatorname{Aut}_{\overline{\mathbf Q}}(C_t)=H\cong(\mathbf Z/2\mathbf Z)^4.}
\]

In particular there is no hidden rational Pythagorean subfamily with enlarged automorphism group that can be split off as an accumulating exceptional stratum.

## 5. What this does and does not solve

The t2 concern that a small set of exceptional low-degree fibers might dominate `T(B)` is resolved:

```text
physical singular fibers                   0
physical lower-genus degenerations         0
physical rational extra-aut fibers         0
```

But the opposite phenomenon occurs: the elliptic structure is **not thin**. It is present on every fiber. Hence it cannot simply be discarded as a negligible exceptional contribution.

The square-root target remains open. The new exact bottleneck is to control, over moving Pythagorean bases, the Mordell--Weil ranks/torsion and the lift conditions from the five elliptic quotients back to `C_t` under the physical height.

This is directly compatible with recent perfect-cuboid work based on elliptic quotient and torsion-intersection obstructions: t3 now supplies the Stage14-native five-factor version of that strategy.

```text
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
TRIPLE_FIBER_HUMBERT_EDGE_TYPE4=true
TRIPLE_FIBER_JACOBIAN_COMPLETELY_ELLIPTIC=true
ELLIPTIC_FACTOR_COUNT=5
PHYSICAL_SINGULAR_EXCEPTIONAL_STRATUM_EMPTY=true
PHYSICAL_RATIONAL_EXTRA_AUTOMORPHISM_STRATUM_EMPTY=true
UNIVERSAL_LOW_DEGREE_STRUCTURE_NOT_THIN=true
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t4 elliptic-factor rank/torsion audit and Kummer-cover comparison
```
