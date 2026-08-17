# Stage27-19-r5ak — residual squareclass incidence system and small-L witness

```text
TASK_ID=Stage27-19-r5ak
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5aj
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

Stage27-19-r5ah-r5ai reduced the exact physical height to

\[
R=\frac{h}{\varepsilon}\kappa L,
\qquad
L=\frac{wc}{C}=w'c',
\]

and r5aj introduced

\[
m=c_0c_s\mu,\quad r=c_0c_n\rho,
\quad s_0=c_s\sigma,\quad n_0=c_n\nu.
\]

On a Stage19 survivor write

\[
p+q=\kappa c^2,\qquad J=\kappa w^2,
\]

with

\[
c=c_0c',\qquad w=c_sc_nw'.
\]

This route records the exact quadratic incidence system satisfied by the residual factors \(c',w'\).

## 1. First residual squareclass equation

Since

\[
p=s_0^2a=a c_s^2\sigma^2,
\qquad
q=n_0^2b=b c_n^2\nu^2,
\]

and \(p+q=\kappa c_0^2c'^2\),

\[
\boxed{
a c_s^2\sigma^2+b c_n^2\nu^2
 =\kappa c_0^2c'^2.
}
\tag{S1}
\]

## 2. Second and third residual squareclass equations

Using

\[
J=bm^2+p\delta^2
\]

and \(m=c_0c_s\mu\), factor out \(c_s^2\):

\[
J=c_s^2\left(bc_0^2\mu^2+a\delta^2\sigma^2\right).
\]

Since \(J=\kappa c_s^2c_n^2w'^2\),

\[
\boxed{
bc_0^2\mu^2+a\delta^2\sigma^2
 =\kappa c_n^2w'^2.
}
\tag{S2}
\]

Likewise from

\[
J=ar^2-q\delta^2
\]

and \(r=c_0c_n\rho\), factor out \(c_n^2\):

\[
\boxed{
a c_0^2\rho^2-b\delta^2\nu^2
 =\kappa c_s^2w'^2.
}
\tag{S3}
\]

Thus the small-residual population \(L=w'c'\le T\) is not an unstructured gcd event: it lies on three coupled integral quadratic equations with \(c',w'\le T\), together with the r5aj physical budget

\[
\delta C\mu\rho\nu\sigma\le B.
\]

This is the next uniform incidence-counting receiver.

## 3. Actual Stage19 survivor with L=1

A pointwise argument cannot assume that every Stage19 survivor leaves a nontrivial residual factor. Consider

\[
(m,n,r,s)=(21,16,27,14).
\]

Then

\[
\delta=2,\quad n_0=8,\quad s_0=7,
\]

\[
c_0=3,\quad c_s=7,\quad c_n=1,
\quad C=21,\quad \varepsilon=1.
\]

Moreover

\[
M=21^2+16^2=697=41\cdot17,
\]

\[
K=27^2-14^2=533=41\cdot13,
\]

so

\[
h=41,\quad a=17,\quad b=13.
\]

Hence

\[
p=7^2\cdot17=833,
\qquad q=8^2\cdot13=832,
\]

\[
p+q=1665=185\cdot3^2,
\]

and

\[
J=abh+\delta^2(p-q)=9065=185\cdot7^2.
\]

Therefore

\[
\kappa=185,\qquad c=3,\qquad w=7,
\]

so

\[
\boxed{L=\frac{wc}{C}=1.}
\]

The exact primitive scale is \(\Gamma=84\), giving physical edges

\[
(e,x,y)=(6048,1665,4264).
\]

The two required face diagonals are

\[
\sqrt{e^2+x^2}=6273,
\qquad
\sqrt{e^2+y^2}=7400,
\]

while

\[
x^2+y^2=20{,}953{,}921
\]

is not a square. The space diagonal is

\[
R=7585=41\cdot185.
\]

Thus this is an actual exactly-two-face Stage19 survivor with \(L=1\).

This witness closes only the **unconditional pointwise** shortcut `L>1 for every survivor`. A single finite witness does not rule out a height-dependent lower bound on all sufficiently large survivors, so no asymptotic negative theorem is claimed.

## 4. Next counting target

The exact-height strategy is now reduced to a uniform count for the solutions of (S1)-(S3), stratified by small \(L=w'c'\), together with the edge budget from r5aj. A fixed-power saving for the small-L stratum, combined with the r5ai large-L side, would be enough to improve the half-power wall. That theorem is not yet proved here.

```text
RESIDUAL_SQUARECLASS_SYSTEM_PROVED=true
RESIDUAL_S1=a*cs^2*sigma^2+b*cn^2*nu^2=kappa*c0^2*cprime^2
RESIDUAL_S2=b*c0^2*mu^2+a*delta^2*sigma^2=kappa*cn^2*wprime^2
RESIDUAL_S3=a*c0^2*rho^2-b*delta^2*nu^2=kappa*cs^2*wprime^2
ACTUAL_STAGE19_L_EQ_1_WITNESS_PROVED=true
ACTUAL_STAGE19_L_EQ_1_WITNESS=(21,16,27,14)
ACTUAL_STAGE19_L_EQ_1_SPACE_DIAGONAL=7585
UNCONDITIONAL_POINTWISE_L_GT_1_PROVED=false
UNCONDITIONAL_POINTWISE_L_GT_1_CLOSED_BY_WITNESS=true
HEIGHT_DEPENDENT_L_LOWER_BOUND_DISPROVED=false
SMALL_L_SURVIVOR_COUNT_FIXED_POWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5al
NEXT_TARGET=UNIFORM_SMALL_L_INCIDENCE_COUNT_USING_RESIDUAL_QUADRATIC_SYSTEM_AND_EDGE_BUDGET
```