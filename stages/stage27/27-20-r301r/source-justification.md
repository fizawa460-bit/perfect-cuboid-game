# Stage27-20-r301r — source justification for the uniform elliptic point-count theorem

SOURCE_KIND=PRIMARY_RESEARCH
SOURCE_TITLE=Counting rational points on elliptic curves with a rational 2-torsion point
SOURCE_AUTHOR=Francesco Naccarato
SOURCE_ARXIV=2105.04032
SOURCE_THEOREM=Theorem_1.1
SOURCE_URL=https://arxiv.org/abs/2105.04032

## The theorem actually used

Naccarato, Theorem 1.1, states that there exist **absolute computable constants** `C,c0` such that for every elliptic curve `E/Q` in Weierstrass form with a rational `2`-torsion point,

\[
N_E(T)\le T^{C/\log\log T}
\]

for every

\[
T\ge \max\{e^e,(eH(E))^{c_0}\},
\]

where `H(E)` is the naive Weil height of the Weierstrass coefficient vector and `N_E(T)` counts rational points whose `x`-coordinate Weil height is at most `T`.

The key feature needed by Stage27 is that `C` and `c0` are absolute; they do not depend on the individual elliptic curve.

## Match to the Stage27 receiver

Stage27-20-r301q produces, for every fixed reduced physical `x=a/b`, the `delta`-independent curve

\[
\mathcal E_{a,b}:\quad
W^2=U(U-(a^2+b^2)^2)(U-(a^2-b^2)^2).
\]

It has full rational `2`-torsion, hence certainly at least one rational `2`-torsion point, so it lies inside the theorem's family.

R301q also proves

\[
H(\mathcal E_{a,b})\ll B^8
\]

and every physical point from any compatible `delta`-fiber maps with bounded multiplicity to a target point satisfying

\[
H(U)\le B^{K_0}
\]

for one absolute `K0`.

Since `c0` is absolute, enlarge the target cutoff to

\[
T_B=B^K
\]

for one absolute `K` chosen larger than `K0` and large enough that

\[
T_B\ge (eH(\mathcal E_{a,b}))^{c_0}
\]

for all sufficiently large `B`.  Then Naccarato gives uniformly in moving `a,b`

\[
N_{\mathcal E_{a,b}}(T_B)
\le T_B^{C/\log\log T_B}
=B^{O(1/\log\log B)}
=B^{o(1)}.
\]

Finite small `B` can be absorbed into an absolute initial range and is irrelevant to the asymptotic exponent gate.

## Scope firewall

This use does **not** claim a new theorem about elliptic curves.  It imports exactly the stated primary-source theorem after r301q verifies its moving-curve height threshold uniformly.

It also does not by itself prove a strict sub-square-root bound for `N2(B)`; the independent support count in the moving first coordinate remains separate.

```text
NACCARATO_PRIMARY_SOURCE_VERIFIED=true
NACCARATO_THEOREM_1_1_ABSOLUTE_CONSTANTS=true
NACCARATO_REQUIRES_RATIONAL_2_TORSION=true
R301Q_TARGET_SATISFIES_2_TORSION_HYPOTHESIS=true
R301Q_CURVE_HEIGHT_THRESHOLD_POLYNOMIAL_UNIFORM=true
R301Q_POINT_HEIGHT_THRESHOLD_POLYNOMIAL_UNIFORM=true
THEOREM_APPLICATION_UNIFORM_IN_MOVING_X=true
STRICT_SUB_SQRT_UPPER_PROVED=false
```
