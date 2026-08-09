# Stage14-t28 — four-linear cover packet and torsion-diagonal removal

## Purpose

Stage14-t27 compressed the primary triple target to the unique trivial split partition

\[
(\alpha,\beta)=(1,1),
\qquad
N_{1,1}(B)=3T(B),
\]

so it is enough to power-save the number \(A_{1,1}(B)\) of active reduced directions.

The immediate counting problem is not yet the raw `[-1]` cover by itself: on the trivial-kernel fibre that cover contains a universal rational order-four section. Counting cover points without removing this section would therefore count **every** candidate direction and create a false density signal.

Stage14-t28 removes that torsion diagonal and rewrites the remaining cover condition as a four-linear square packet with completely controlled common-prime support.

## 1. Reparametrise the primitive Pythagorean direction

On the `(1,1)` fibre write

\[
D-C=hr^2,\qquad D+C=hu^2,\qquad L=hru,
\qquad C^2+L^2=D^2,
\]

with \((r,u)=1\), \(u>r>0\), and \(h\in\{1,2\}\).

Introduce coprime \(0<a<b\) and \(\varepsilon\in\{1,2\}\) by

```text
if r,u have opposite parity:
    epsilon = 1
    a = u-r
    b = u+r

if r,u are both odd:
    epsilon = 2
    a = (u-r)/2
    b = (u+r)/2
```

Then exactly

\[
\boxed{D-L=\varepsilon a^2,\qquad D+L=\varepsilon b^2,}
\]

\[
\boxed{C=\varepsilon ab,\qquad
D=\frac{\varepsilon}{2}(a^2+b^2),\qquad
L=\frac{\varepsilon}{2}(b^2-a^2).}
\]

Conversely every coprime pair \(0<a<b\) occurs in exactly one of these parity cases.

Define

\[
\Delta(a,b)=2ab(b^2-a^2)(a^2+b^2).
\]

The relation to the t27 moving support is exact:

\[
\boxed{
\Delta=
\begin{cases}
16\,r u C D,&\varepsilon=1,\\
r u C D,&\varepsilon=2.
\end{cases}}
\]

Hence the odd prime support of \(\Delta\) is **exactly** the odd prime support of the canonical t27 statistic \(ruCD\).

## 2. The physical `[-1]` cover factors into four linear forms

From t24 the trivial-kernel rank cover is

\[
W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4),
\qquad (p,q)=1.
\]

Since \(D^2-C^2=L^2\),

\[
4D^2-2C^2=(D-L)^2+(D+L)^2.
\]

Substituting the \(a,b,\varepsilon\) parametrisation gives

\[
W^2
=
-\varepsilon^2
(a^2q^2-b^2p^2)(b^2q^2-a^2p^2).
\]

For a non-degenerate positive cover point, positivity is equivalent to

\[
\boxed{\frac ab<\frac pq<\frac ba.}
\]

Define the four positive linear forms

\[
g_1=bp-aq,\qquad
g_2=aq+bp,
\]

\[
g_3=bq-ap,\qquad
g_4=bq+ap.
\]

Then the cover equation is exactly

\[
\boxed{W^2=\varepsilon^2 g_1g_2g_3g_4.}
\]

Thus, with \(Z=W/\varepsilon\),

\[
\boxed{Z^2=g_1g_2g_3g_4.}
\]

This is an equivalence at the integral-cover level, not merely a congruence consequence.

## 3. Universal torsion diagonal

Take \(p=q=1\). Then

\[
g_1=g_3=b-a,\qquad g_2=g_4=a+b,
\]

so the product is automatically a square on **every** direction.

On the integral elliptic model

\[
E_{D,C}:Y^2=X(X^2+(4D^2-2C^2)X+C^4)
\]

this point is

\[
\boxed{P_4=(-C^2,\,2C^2L).}
\]

For a curve \(y^2=x(x^2+Ax+C^4)\), the duplication formula has

\[
x(2P)=\frac{(x^2-C^4)^2}{4y^2}.
\]

At \(P_4\),

\[
x(P_4)^2=C^4,\qquad y(P_4)\neq0,
\]

so

\[
2P_4=(0,0).
\]

Therefore \(P_4\) has exact order four.

This is the universal section already anticipated by the t23 torsion analysis. It is **not** a physical non-torsion activation. In the four-linear coordinates,

\[
\boxed{p=q
\iff
g_1=g_3\ \text{and}\ g_2=g_4.}
\]

Because \((p,q)=1\), the positive diagonal is exactly \(p=q=1\).

Hence any asymptotic cover count that fails to remove this diagonal is unusable for \(A_{1,1}\).

## 4. Pairwise gcd support is exactly the direction support

For primitive \((p,q)\), the gcd of two distinct linear forms divides the determinant of their coefficient vectors. The six determinants are

\[
2ab,\quad b^2-a^2,\quad a^2+b^2,\quad
a^2+b^2,\quad b^2-a^2,\quad 2ab.
\]

Consequently every pairwise gcd satisfies

\[
\boxed{\gcd(g_i,g_j)\mid\Delta(a,b).}
\]

In particular, if a prime \(\ell\nmid\Delta\), then \(\ell\) divides at most one \(g_i\).

If \(g_1g_2g_3g_4\) is a square, every such outside prime occurs to even valuation in its unique factor.

Therefore each factor has a canonical decomposition

\[
\boxed{g_i=d_i z_i^2}
\]

with \(d_i\) positive squarefree and

\[
\boxed{d_i\mid\operatorname{rad}\Delta.}
\]

Moreover

\[
\boxed{d_1d_2d_3d_4\in\mathbb Z^2.}
\]

For each prime dividing \(\Delta\), its membership among the four squarefree kernels must have even cardinality. There are at most eight choices per prime, so the packet-state loss is

\[
\boxed{8^{\omega(\Delta)}=X^{o(1)}}
\]

on a dyadic direction shell \(X<D\le2X\).

This is a stronger structural statement than merely knowing that a large direction prime is locally routable.

## 5. Weighted diagonal biquadrate equation

The four linear forms satisfy

\[
g_1+g_2=2bp,\qquad g_2-g_1=2aq,
\]

\[
g_3+g_4=2bq,\qquad g_4-g_3=2ap.
\]

Eliminating \(a/b\) after substituting \(g_i=d_i z_i^2\) gives

\[
(g_1+g_2)(g_2-g_1)
=
(g_3+g_4)(g_4-g_3),
\]

hence

\[
\boxed{
d_1^2z_1^4+d_4^2z_4^4
=
d_2^2z_2^4+d_3^2z_3^4.
}
\]

The direction ratio is recoverable from the same packet:

\[
\frac ab
=
\frac{g_4-g_3}{g_1+g_2}
=
\frac{g_2-g_1}{g_3+g_4}.
\]

Thus the non-torsion trivial-kernel cover is reduced to a finite-state family of **weighted equal-sums-of-biquadrates** with the additional support condition \(d_i\mid\operatorname{rad}\Delta(a,b)\).

The universal order-four section is the diagonal subfamily

\[
g_1=g_3,\qquad g_2=g_4.
\]

The Stage14 counting problem concerns the off-diagonal part.

## 6. What happens to the t27 canonical largest prime

Let

\[
P_*=P^+(ruCD)_{\rm odd}=P^+(\Delta)_{\rm odd}.
\]

A tempting next step would be to assume that \(P_*\) enters at least one squarefree coefficient \(d_i\). This is false.

The t28 synthetic audit contains explicit non-diagonal square-cover points for which the largest odd prime in \(ruCD\) divides none of

\[
d_1,d_2,d_3,d_4.
\]

Therefore the large-prime branch splits further:

1. **kernel-visible:** \(P_*\mid d_i\) for at least one \(i\);
2. **kernel-invisible:** \(P_*\nmid d_1d_2d_3d_4\).

The second branch is exactly why the Gaussian/dual routing from t26 remains necessary. The four-linear kernel packet does not supersede t26.

No claim is made that the finite visible/invisible proportions are asymptotic densities.

## 7. Sieve applicability boundary

The packet now supplies a concrete polynomial object for the q6/q8 square/polynomial-sieve route.

However, two shortcuts are not justified.

First, the universal order-four diagonal must be removed before any point-counting theorem is interpreted as activation thinning.

Second, the Bonolis--Browning hyperelliptic-fibration theorem is not a direct black-box fit: its main square-sieve theorem assumes an odd exponent \(n\), while the present fibre is an even quartic. Their paper explicitly identifies the oddness assumption as essential to the relevant complete character-sum lemma.

Pierce--Xu type character bounds remain plausible on fixed admissible packets, but t28 does not yet supply the moving-coefficient and existential-projection bookkeeping needed to turn those bounds into an \(A_{1,1}\) power saving.

As a consistency check, the 2026 preprint of Peschmann independently reduces the perfect-cuboid problem to quartic/genus-three square-value conditions and explicitly leaves the global non-existence problem open. The Stage14 four-linear packet is therefore treated as a reduction object, not as an accidental proof of non-existence.

## 8. Frozen diagnostics

The deterministic t28 audit has two parts.

### Full `(1,1)` direction universe through `D<=2,000,000`

\[
636640
\]

primitive directions are recovered, with

\[
318362
\]

in the top shell \(1,000,000<D\le2,000,000\), matching t27 exactly.

### Synthetic cover identity audit

For all coprime \(0<a<b\le40\), and all primitive \(1\le p,q\le40\) in the physical interval:

```text
(a,b) directions                         489
primitive interval (p,q) tuples       239121
square-cover hits                         587
universal p=q=1 order-4 hits              489
non-diagonal square-cover hits             98
kernel-support checks                     587
weighted-biquadrate checks                587

non-diagonal P_* kernel-visible             32
non-diagonal P_* kernel-invisible           66
```

These are algebraic/synthetic diagnostics only. The 98 non-diagonal cover points are **not** asserted to be actual perfect-cuboid completions.

## Boundary

```text
STAGE14_T28=COMPLETE_FOUR_LINEAR_COVER_PACKET_AND_TORSION_DIAGONAL_REMOVAL
TRIVIAL_KERNEL_COVER_FULL_2_TORSION=true
UNIVERSAL_P_EQ_Q_POINT_EXACT_ORDER4=true
FOUR_LINEAR_COVER_FACTORISATION=true
PAIRWISE_GCD_SUPPORT_EQUALS_DIRECTION_ODD_SUPPORT=true
FOUR_FACTOR_SQUAREFREE_KERNEL_PACKET=true
FOUR_FACTOR_KERNEL_STATE_LOSS=X^o(1)
WEIGHTED_DIAGONAL_BIQUADRATE_REDUCTION=true
CANONICAL_LARGE_PRIME_ALWAYS_KERNEL_VISIBLE=false
COVER_ONLY_COUNTING_WITHOUT_TORSION_REMOVAL_VALID=false
ROUTED_LARGE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t29 split non-torsion packets into largest-prime kernel-visible versus Gaussian/dual-invisible states and test square/polynomial-sieve incidence on the visible weighted biquadrate family
```
