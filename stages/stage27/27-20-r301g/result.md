# Stage27-20-r301g — integral squareclass kernel and common-gcd localization

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301f
SOURCE_STAGE=Stage20

## 1. Clear the torus denominators exactly

Start from the audited r301f receiver

\[
(q_1^2+q_2^2)(q_1^2q_2^2+1)\in(\mathbf Q^*)^2.
\]

Write the two positive torus coordinates in lowest terms as

\[
q_1=\frac ab,\qquad q_2=\frac ce,
\qquad (a,b)=(c,e)=1.
\]

Put

\[
F:=a^2e^2+b^2c^2,
\qquad
G:=a^2c^2+b^2e^2.
\]

Then

\[
q_1^2+q_2^2=\frac{F}{b^2e^2},
\qquad
q_1^2q_2^2+1=\frac{G}{b^2e^2}.
\]

The common denominator in the product is already a square, so the space-diagonal condition is exactly

\[
\boxed{FG\text{ is an integer square}.}
\]

## 2. The common squareclass is the squarefree kernel of gcd(F,G)

Let

\[
h:=\gcd(F,G),\qquad F=hu,\qquad G=hv,
\qquad (u,v)=1.
\]

If `FG` is a square, then `uv` is a square.  Since `u` and `v` are coprime, both are squares:

\[
u=r^2,\qquad v=s^2.
\]

Write

\[
h=\delta t^2
\]

with `delta>0` squarefree.  Then

\[
\boxed{F=\delta (tr)^2,\qquad G=\delta (ts)^2.}
\]

Thus the varying rational squareclass in r301f is not an extra free parameter: after clearing denominators it is exactly

\[
\boxed{\delta=\operatorname{sqf}(\gcd(F,G)).}
\]

## 3. No common prime can come from a torus numerator or denominator

Let `p` be a prime dividing `gcd(F,G)`.  Then

\[
\boxed{p\nmid abce.}
\]

For example, if `p|a`, then `(a,b)=1` gives `p\nmid b`.  From `p|F` one would obtain `p|c`, while from `p|G` one would obtain `p|e`, contradicting `(c,e)=1`.  The other three variables are symmetric.

Hence every common prime is a unit prime for both rational torus coordinates.

## 4. Exact odd-prime localization

Let `p` be odd and divide `gcd(F,G)`.  In `F_p` put

\[
x=a/b,\qquad y=c/e.
\]

Because `p\nmid abce`, both are units, and the two congruences become

\[
x^2+y^2=0,
\qquad
x^2y^2+1=0.
\]

Substituting `y^2=-x^2` into the second equation gives

\[
x^4=1.
\]

For odd `p`, therefore `x^2=1` or `x^2=-1`.  Correspondingly,

\[
\begin{array}{ll}
x^2=1:&y^2=-1,\\
x^2=-1:&y^2=1.
\end{array}
\]

In either case `-1` is a quadratic residue modulo `p`, so

\[
\boxed{p\equiv1\pmod4.}
\]

Moreover every such common prime lies in exactly one of the two cross-gcd channels

\[
\boxed{
 p\mid\gcd(a^2-b^2,c^2+e^2)
 \quad\text{or}\quad
 p\mid\gcd(a^2+b^2,c^2-e^2).
}
\]

The two alternatives cannot both occur for the same odd prime, because that would force `p|2a^2` and `p|2b^2`.

Therefore, writing `delta_odd` for the odd part of the squarefree kernel,

\[
\boxed{
\delta_{\rm odd}
\mid
\operatorname{rad}\gcd(a^2-b^2,c^2+e^2)
\;\operatorname{rad}\gcd(a^2+b^2,c^2-e^2).
}
\]

In particular every odd prime of `delta` is `1 mod 4`.  The prime `2` is retained separately and no stronger 2-adic statement is promoted here.

## 5. Scope firewall

This route proves an exact localization of the common squareclass.  It does **not** yet prove that the global set of squareclasses up to physical height `B` has fixed-power sparsity, because the cross-gcd values move with the torus point.

```text
STAGE27_20_R301G_STATUS=AUDITED_PASS_MERGED
INTEGRAL_F_G_RECEIVER_PROVED=true
COMMON_SQUARECLASS_EQUALS_SQFREE_GCD_KERNEL=true
COMMON_PRIME_AVOIDS_ABCE=true
ODD_COMMON_PRIME_ONE_MOD_FOUR=true
ODD_COMMON_PRIME_CROSS_GCD_LOCALIZATION_PROVED=true
GLOBAL_SQUARECLASS_FIXED_POWER_SUPPORT_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301h
```
