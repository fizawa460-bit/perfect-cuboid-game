# Stage14-t24 — torsion-energy closure and rank-branch -1 descent cover

## Purpose

Stage14-t23 split the active-direction collision energy into

\[
Q_{\rm active}(B)\le 2Q_{\rm rank}(B)+2Q_{\rm tor}(B),
\]

where the torsion branch is forced onto the exact order-8 locus and the remaining branch carries a physical non-torsion point on the t22 elliptic quotient.

Stage14-t24 does two things.

1. It closes the torsion second moment at theorem scale by viewing the two t23 quartic packets as soluble binary-quartic 2-coverings and applying the uniform bounded-height theorem to their Jacobians.
2. It writes the rank branch as an explicit fixed `[-1]` 2-descent covering family and identifies the split partition `(alpha,beta)` as the exact squareclass of the displayed elliptic discriminant.

The remaining t-track obstruction after this stage is only the rank-active direction second moment.

## 1. Torsion packet recalled

On the possible order-8 branch, primitive Euclid parameters satisfy

\[
(m,n)=1,\qquad m>n>0,\qquad m\not\equiv n\pmod2,
\]

and

\[
D=(m^2+n^2)^2\le B.
\]

The two split-partition packets from t23 are

\[
F_+(m,n)=m^4+6m^2n^2+n^4,
\qquad \alpha=1,
\]

and

\[
F_-(m,n)=m^4+n^4,
\qquad \alpha=2.
\]

If `beta=core(F_\pm(m,n))`, then

\[
F_\pm(m,n)=\beta v^2
\]

for an integer `v`.

For each sign and squarefree `beta`, define the full potential-packet multiplicity

\[
M_{\pm,\beta}(B)
=
\#\{(m,n):D\le B,\ \operatorname{core}(F_\pm(m,n))=\beta\}.
\]

The actual torsion-active directions form a subset of this potential packet, so

\[
Q_{\rm tor}(B)
\le
\widetilde Q_{\rm tor}(B)
:=
\sum_\beta M_{+,\beta}(B)^2
+
\sum_\beta M_{-,\beta}(B)^2.
\]

## 2. Each fixed squarefree kernel is a soluble binary-quartic 2-cover

For `A in {0,6}`, put

\[
F_A(M,N)=M^4+A M^2N^2+N^4.
\]

For fixed squarefree `beta`, consider the degree-2 genus-one model

\[
\boxed{
C_{A,\beta}:\quad W^2=\beta F_A(M,N).
}
\]

A packet solution `F_A(m,n)=beta v^2` gives the rational point

\[
[M:N:W]=[m:n:\beta v]
\]

on `C_{A,beta}`. Thus every nonempty packet is a soluble binary quartic.

The underlying quartics are smooth. Their ordinary polynomial discriminants are

```text
disc(x^4+1)             = 2^8,
disc(x^4+6x^2+1)       = 2^14.
```

Hence multiplying by nonzero `beta` does not create a repeated geometric root.

## 3. The Jacobians have uniform rational 2-torsion

For the binary quartic

\[
\beta(x^4+A x^2z^2+z^4),
\]

the classical invariants are

\[
I=(A^2+12)\beta^2,
\qquad
J=2A(36-A^2)\beta^3.
\]

For both `A=0` and `A=6`,

\[
J=0.
\]

With the standard binary-quartic normalization `c4=16I`, `c6=32J`, the Jacobian may be written

\[
E_{A,\beta}:\quad
Y^2=X^3-\frac{I}{3}X-\frac{J}{27}.
\]

Therefore the two families are explicitly

\[
\boxed{
E_{-,\beta}:Y^2=X^3-4\beta^2X,
}
\]

and

\[
\boxed{
E_{+,\beta}:Y^2=X^3-16\beta^2X.
}
\]

In particular both have nonzero rational 2-torsion for every positive squarefree `beta`:

```text
E_- : (0,0), (2 beta,0), (-2 beta,0),
E_+ : (0,0), (4 beta,0), (-4 beta,0).
```

This is exactly the hypothesis needed for the uniform bounded-height theorem used earlier in t22.

Reference for degree-2 genus-one models, binary-quartic invariants, and their Jacobians: Cremona--Fisher--Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves*, Algebra & Number Theory 4 (2010), arXiv:0908.1741.

## 4. Fixed-beta packet multiplicity is subpolynomial

A degree-2 genus-one model is a 2-covering of its Jacobian. The covering map has bounded degree (degree four), and its covariants have fixed algebraic degree.

Under the torsion-direction cutoff

\[
(m^2+n^2)^2\le B,
\]

we have

\[
|m|,|n|\le B^{1/4},
\]

and

\[
F_-(m,n)\le B,
\qquad
F_+(m,n)\le 2B.
\]

Thus `beta<=2B`, and the packet point on `C_{A,beta}` has projective height `B^{O(1)}`. The bounded-degree covering map sends it to a point of height `B^{O(1)}` on `E_{A,beta}`; the curve coefficients themselves also have height `B^{O(1)}`.

Marta Dujella's uniform theorem for elliptic curves over `Q` with a rational point of exact prime order, applied with prime order `2`, gives

\[
\#\{P\in E_{A,\beta}(\mathbf Q):H(P)\le B^K\}
\le
\exp\!\left(C\frac{\log B}{\log\log B}\right)
=B^{o(1)}
\]

uniformly in `beta` and in the two packet families.

Since the covering degree is fixed and primitive positive `(m,n)` give distinct rational parameter points up to bounded symmetry,

\[
\boxed{
M_{\pm,\beta}(B)=B^{o(1)}
}
\]

uniformly in `beta`.

Reference: Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves*, Acta Arith. 217 (2025), arXiv:2312.03655.

## 5. Torsion second moment is now power-saved

The number of primitive Euclid pairs in the disk

\[
m^2+n^2\le B^{1/2}
\]

is `O(B^{1/2})`. Hence

\[
\sum_\beta M_{+,\beta}(B)
+
\sum_\beta M_{-,\beta}(B)
=O(B^{1/2}).
\]

Combining this first moment with the uniform fixed-kernel multiplicity,

\[
\widetilde Q_{\rm tor}(B)
\le
\left(\max_{\pm,\beta}M_{\pm,\beta}(B)\right)
\left(
\sum_\beta M_{+,\beta}(B)+\sum_\beta M_{-,\beta}(B)
\right),
\]

so

\[
\boxed{
Q_{\rm tor}(B)
\le
\widetilde Q_{\rm tor}(B)
=O(B^{1/2+o(1)}).
}
\]

Thus the entire torsion branch is no longer a blocker for `Q_active=o(B)`.

This is stronger than the q8 square-sieve handoff was required to produce. The q8 route remains valid as an independent analytic route, but is not needed for the theorem-level torsion-energy bound once the binary-quartic Jacobian structure is used.

## 6. q8 Pierce--Xu admissibility audit

For completeness, the q8 transfer hypothesis can be checked exactly.

Pierce--Xu's theorem applies to quadratic characters evaluated at `(2,p)`-admissible homogeneous forms. For every odd prime `p`, both `F_+` and `F_-` remain squarefree modulo `p`, because their discriminants are powers of `2` only.

A squarefree binary quartic cannot become a function of only one coordinate after a `GL_2(F_p)` change of variables: such a homogeneous one-coordinate quartic would be a fourth power of a linear form and hence not squarefree.

Therefore

\[
\boxed{
F_+,F_-\text{ are }(2,p)\text{-admissible for every odd prime }p.
}
\]

So the q8 classification `PIERCE_XU_BINARY_QUARTIC_TRANSFER=NEAR_HIGH_PRIORITY` passes its algebraic admissibility check. The Pierce--Xu theorem is nontrivial for two-dimensional boxes beyond its `p^{1/3+epsilon}` threshold. The remaining square-sieve composite-modulus/prime-averaging bookkeeping is bypassed here by the genus-one argument above.

Reference: Lillian B. Pierce and Junyan Xu, *Burgess bounds for short character sums evaluated at forms*, Algebra & Number Theory 14 (2020), arXiv:1907.03108.

## 7. Integral 4-torsion model for the rank branch

Now return to a general active reduced direction `(D,C)` outside the order-8 locus.

The shifted t22 quotient

\[
y^2=z\left(z^2+\left(4D^2/C^2-2\right)z+1\right)
\]

has the integral model

\[
\boxed{
\mathcal E_{D,C}:\quad
Y^2=X\left(X^2+(4D^2-2C^2)X+C^4\right),
}
\]

obtained from `X=C^2 z`, `Y=C^3 y`.

It contains

\[
(0,0)\in\mathcal E_{D,C}[2](\mathbf Q)
\]

and the built-in order-four point

\[
(C^2,2DC^2).
\]

Its displayed discriminant is

\[
\boxed{
\Delta_{D,C}=256\,C^8D^2(D^2-C^2).
}
\]

Using the t20/t21 partition equations

\[
D-C=h\alpha r^2,
\qquad
D+C=h\beta u^2,
\]

we get

\[
D^2-C^2=h^2\alpha\beta r^2u^2,
\]

and therefore

\[
\boxed{
\Delta_{D,C}
=\alpha\beta\,(16hC^4Dru)^2.
}
\]

Hence the split partition kernel is exactly the squareclass of the displayed discriminant:

\[
\boxed{[\Delta_{D,C}]=[\alpha\beta].}
\]

This does not assert that the displayed equation is globally minimal at every prime. It is a squareclass identity on the explicit Stage14 model and is the correct input for the next local/minimal-discriminant transfer audit.

## 8. Physical rank activation lies on one explicit `[-1]` 2-cover

For

\[
y^2=z(z^2+Az+1),
\qquad A=4D^2/C^2-2,
\]

t23 proved that every physical point has

\[
[z]=[-1]\in\mathbf Q^\times/\mathbf Q^{\times2}.
\]

Writing

\[
z=-\left(\frac{p}{q}\right)^2
\]

in lowest rational form and substituting into the elliptic equation gives the standard `[-1]` 2-cover

\[
\boxed{
\omega^2=-p^4+A p^2q^2-q^4.
}
\]

After clearing the fixed direction denominator `C^2`, this is

\[
\boxed{
(C\omega)^2
=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4).
}
\]

Equivalently,

\[
\boxed{
(C\omega)^2+C^2(p^2+q^2)^2=(2Dpq)^2.
}
\]

For an actual physical orientation from t23 one can take

\[
p=D+X,
\qquad
q=Q,
\]

because

\[
z=-((D+X)/Q)^2.
\]

Outside the t23 order-8 locus, this point is non-torsion. Thus every rank-active direction produces a bounded-height rational point on this single explicit `[-1]` covering family.

## 9. Exact remaining second-moment target

Define

\[
A^{\rm rank}_{\alpha,\beta}(B)
\]

as the number of reduced directions in split partition `(alpha,beta)` that carry a physical non-torsion point. Then

\[
Q_{\rm rank}(B)
=
\sum_{\alpha,\beta}
\left(A^{\rm rank}_{\alpha,\beta}(B)\right)^2.
\]

From t22--t24,

\[
Q_{\rm split}(B)
\le B^{o(1)}Q_{\rm active}(B)
\le
B^{o(1)}\left(2Q_{\rm rank}(B)+O(B^{1/2+o(1)})\right).
\]

Therefore the whole t-track is now reduced to one theorem:

\[
\boxed{
Q_{\rm rank}(B)=O(B^{1-\delta})
\quad\text{for some fixed }\delta>0.
}
\]

Any such estimate implies

\[
Q_{\rm split}(B)=o(B),
\qquad
Q_{\rm edge}(B)=o(B),
\qquad
T(B)=o(\sqrt B).
\]

## 10. Rank-side handoff to the q3 architecture

The displayed discriminant and the explicit `[-1]` cover make the q3 Le-Boudec-style transfer test concrete.

For a fixed partition `(alpha,beta)`, directions are

\[
D=\frac h2(\alpha r^2+\beta u^2),
\qquad
C=\frac h2(\beta u^2-\alpha r^2).
\]

Ignoring fixed powers of `2` and the fixed kernel `alpha beta`, the moving support of the displayed discriminant is contained in

\[
r\,u\,C\,D,
\]

that is in the explicit factors

\[
\boxed{
r,\quad u,\quad \beta u^2-\alpha r^2,\quad \beta u^2+\alpha r^2.}
\]

The next stage should audit local minimality and the exact 2-descent effect of a large prime in one of these moving factors, then count pairs of directions in the same `(alpha,beta)` packet for which the `[-1]` cover has a physical small point.

No minimal-discriminant, conductor, or large-prime power saving is claimed in t24.

## 11. Frozen finite diagnostics

The standard-library t24 audit regenerates the exact Stage14 graph through `B=2,000,000` and checks:

- all 356 actual raw-pair edges remain on the positive-rank branch from t23;
- all 356 displayed discriminants have squarefree core exactly `alpha*beta`;
- both physical orientations of every edge satisfy the explicit `[-1]` covering equation;
- the potential order-8 Euclid universe through `D<=2,000,000` contains 225 primitive `(m,n)` pairs, hence 450 oriented torsion directions before the physical simultaneous-completion gate;
- for `F_+`, all 225 observed squarefree kernels are distinct;
- for `F_-`, the finite packet energy is 229, with maximum kernel multiplicity 2;
- the only repeated `F_-` kernels in this frozen potential universe are `17` and `113`.

At the frozen endpoint:

```text
potential primitive Euclid parameters        225
potential oriented torsion directions        450
F_plus packet energy                          225
F_minus packet energy                         229
combined potential torsion packet energy      454
max F_plus kernel multiplicity                  1
max F_minus kernel multiplicity                 2
repeated F_minus kernels                   17,113
actual physical torsion-active directions        0
actual rank-active raw edges                   356
rank discriminant-squareclass checks            356
rank [-1]-cover orientation checks               712
```

These finite collision values are diagnostics only. The theorem-level torsion energy bound comes from the binary-quartic/Jacobian argument, not from finite injectivity.

## Locked boundary

```text
STAGE14_T24=COMPLETE_TORSION_SECOND_MOMENT_AND_RANK_MINUS_ONE_COVER_REDUCTION
TORSION_PACKET_BINARY_QUARTIC_2_COVER=true
TORSION_PACKET_JACOBIAN_RATIONAL_2_TORSION=true
FIXED_TORSION_KERNEL_MULTIPLICITY=B^o(1)
TORSION_SECOND_MOMENT=O(B^(1/2+o(1)))
TORSION_SECOND_MOMENT_POWER_SAVING_PROVED=true
PIERCE_XU_ODD_PRIME_ADMISSIBILITY=true
RANK_INTEGRAL_4_TORSION_MODEL_EXPLICIT=true
RANK_DISPLAYED_DISCRIMINANT_SQUARECLASS=alpha*beta
RANK_PHYSICAL_MINUS_ONE_2_COVER_EXPLICIT=true
Q_ACTIVE_REDUCED_TO_RANK_ENERGY=true
RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED=false
Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED=false
Q_SPLIT_POWER_SAVING_PROVED=false
Q_EDGE_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t25 rank-active Le-Boudec transfer test: minimal discriminant/local large-prime forcing on the explicit [-1] cover and same-partition collision pairs
```
