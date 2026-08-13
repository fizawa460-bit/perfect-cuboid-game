# Stage14-t27 — trivial-kernel target compression and cover-conditioned friability split

## Purpose

Stage14-t20 identified the trivial missing-face squareclass exactly with triple objects:

\[
n_1(B)=3T(B).
\]

Stages t21--t26 then built a stronger partition-resolved second-moment route. That route remains valid, but for the **primary t-track target** it is stronger than necessary. Stage14-t27 compresses the target to the unique trivial split partition and then audits the large-prime/smooth-exception architecture on that single dangerous fiber.

The key conclusion is:

\[
\boxed{N_{1,1}(B)=3T(B)}
\]

and, using the uniform fixed-direction multiplicity bound from t22,

\[
\boxed{3T(B)\le B^{o(1)}A_{1,1}(B)}.
\]

Therefore a fixed power saving

\[
\boxed{A_{1,1}(B)=O(B^{1/2-\delta})}
\qquad(\delta>0)
\]

already implies

\[
T(B)=o(\sqrt B).
\]

A power saving for the full rank-active second moment is still a sufficient stronger theorem, but it is no longer required for the primary triple correction.

## 1. Why the trivial class is exactly `(alpha,beta)=(1,1)`

For a raw-pair edge t20 writes

\[
D-C=h\alpha r^2,
\qquad
D+C=h\beta u^2,
\]

with `alpha,beta` positive, squarefree and coprime, and

\[
\kappa=\alpha\beta.
\]

The trivial squareclass is `kappa=1`. Positivity and squarefreeness therefore force

\[
\boxed{\alpha=\beta=1}.
\]

Conversely `(alpha,beta)=(1,1)` gives `kappa=1`, hence the missing third face is integral. Thus its raw-pair edge belongs to a triple object. Since every triple object contributes exactly three raw-pair edges,

\[
\boxed{N_{1,1}(B)=n_1(B)=3T(B)}.
\]

This is exact; no Cauchy--Schwarz or partition majorant is needed on the trivial class.

## 2. The dangerous fiber is a primitive Pythagorean direction

On `(alpha,beta)=(1,1)`,

\[
D-C=hr^2,
\qquad
D+C=hu^2,
\]

where `(r,u)=1`, `u>r`, and

\[
h=1\iff r,u\text{ are both odd},
\qquad
h=2\text{ otherwise}.
\]

Hence

\[
\boxed{D=\frac h2(r^2+u^2)},
\qquad
\boxed{C=\frac h2(u^2-r^2)}.
\]

Put

\[
L=hru.
\]

Then

\[
\boxed{C^2+L^2=D^2}.
\]

Thus the unique dangerous partition is exactly the primitive Pythagorean direction family. The t23 elliptic quotient has full rational `2`-torsion on this fiber because `D^2-C^2=L^2` is already a square.

## 3. Fixed-direction multiplicity converts the edge count to an active-direction count

Let `A_{1,1}(B)` be the number of reduced `(1,1)` directions that carry at least one physical simultaneous completion with `d<=B`.

Stage14-t22 proves uniformly in `(D,C)` that all physical completions over one fixed reduced direction contribute only

\[
B^{o(1)}
\]

raw edges up to height `B`. Therefore

\[
N_{1,1}(B)\le B^{o(1)}A_{1,1}(B).
\]

Combining with `N_{1,1}=3T` gives

\[
\boxed{T(B)\le B^{o(1)}A_{1,1}(B)}.
\]

Accordingly, a fixed exponent saving for `A_{1,1}` is sufficient for the primary theorem target. This avoids having to prove a power saving simultaneously for all nontrivial split kernels.

## 4. Dyadic large-prime / smooth split on the single dangerous fiber

Work on a dyadic direction shell

\[
X<D\le2X.
\]

For `(1,1)` define the four moving columns

\[
r,\qquad u,\qquad C=u\text{-}r\text{ quadratic column},\qquad D=u\text{+}r\text{ quadratic column}
\]

more precisely by the formulas in Section 2, and define the canonical odd largest-prime statistic

\[
P_*(r,u):=P^+(r\,u\,C\,D)_{\rm odd}.
\]

For fixed `eta>0`, split active directions into

\[
\mathcal L_\eta(X)
=\{X<D\le2X:\ P_*(r,u)>X^\eta\},
\]

and

\[
\mathcal S_\eta(X)
=\{X<D\le2X:\ P_*(r,u)\le X^\eta\}.
\]

Then

\[
A_{1,1}(B)
\ll
\sum_{X\ \mathrm{dyadic}\le B}
\left(
\#\mathcal L_\eta(X)+\#\mathcal S_\eta(X)
\right).
\]

Thus it is enough to find fixed `eta,delta>0` such that both branches satisfy

\[
\#\mathcal L_\eta(X),\ \#\mathcal S_\eta(X)
=O(X^{1/2-\delta}).
\]

The split itself is exact. The two required power savings are not proved in t27.

## 5. The large branch is now fully routed by t26

Choose the **largest odd prime** `ell=P_*(r,u)` canonically on `mathcal L_eta(X)`. Since `ell>X^eta`, the t26 routing theorem places `ell` into one of finitely many cover-side states.

With

\[
S=p^2+q^2,
\qquad
T_0=p^2-q^2,
\]

the possibilities are:

- `ell|D`: `ell|S`, or a Gaussian congruence `W +/- rho C S = 0` modulo the appropriate prime power;
- `ell|r u`, `ell=3 mod 4`: the t25 inert-prime forcing puts the required power of `ell` into `T_0`;
- `ell|r u`, `ell=1 mod 4`: `ell|T_0`, or a Gaussian congruence `W +/- rho C T_0 = 0`;
- `ell|C`: `ell|pq`, or the dual-isogeny linear factor `2Dpq +/- W = 0` modulo the required prime power.

The sign/root allocation loss over all split primes is at most `2^omega=B^{o(1)}`. Therefore the large branch is reduced to a finite union of **cover-conditioned congruence incidences with a canonical modulus `ell>X^eta`**.

Define `I_eta(X)` to be the number of such routed physical incidences after the canonical largest-prime choice. Then t26 gives schematically

\[
\boxed{\#\mathcal L_\eta(X)\le X^{o(1)}I_\eta(X)}.
\]

The next analytic problem on this branch is a genuine incidence count, not further local algebra.

## 6. Why Le Boudec's large-prime subset does not by itself control the complement

Pierre Le Boudec's congruent-number argument deliberately starts by restricting to squarefree parameters with a large prime factor, then exploits that factor by complete `2`-descent. The paper proves that this restricted family has positive proportion; it does not show that the complement is power-saving small.

That distinction is decisive here. The Stage14 task is an **upper bound for every active direction**, so selecting a positive-proportion large-prime subfamily cannot discard the remaining directions.

Reference: Pierre Le Boudec, *Height of rational points on congruent number elliptic curves*, arXiv:1802.07136, especially the introduction and Lemma 1 construction of the large-prime subset.

## 7. Ambient friability blocks a one-column availability shortcut

There is also a genuine smooth-value barrier to a naive argument using only one quadratic column.

Balog--Blomer--Dartyge--Tenenbaum study

\[
\Psi_F(R,y)=\#\{1\le a,b\le R:P^+(F(a,b))\le y\}
\]

for integral binary forms. For degree `2`, their general theorem already permits `y=R^epsilon` while retaining order `R^2` many friable values. Thus a quadratic form such as the Pythagorean hypotenuse form can take polynomially smooth values on an ambient set of positive order of magnitude.

Therefore t27 does **not** assert that `D` alone, or `C` alone, contains a polynomially large prime outside a power-saving exceptional set.

This does not prove that the simultaneous four-column set

\[
P^+(r u C D)\le X^\eta
\]

is large, and it says even less after imposing the physical elliptic-cover condition. It does show that the smooth branch must be counted **with the physical cover condition present** rather than thrown away by a generic largest-prime-factor heuristic.

Reference: A. Balog, V. Blomer, C. Dartyge, G. Tenenbaum, *Friable values of binary forms*, Comment. Math. Helv. 87 (2012), 639--667.

## 8. Exact next counting problem

The primary t-track can now ignore all nontrivial `(alpha,beta)` packets if the goal is only `T(B)=o(sqrt B)`.

For the single `(1,1)` fiber, the next theorem must count physical solutions to

\[
W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4),
\]

with

\[
D=\frac h2(r^2+u^2),
\qquad
C=\frac h2(u^2-r^2),
\qquad
(r,u)=1,
\]

in two regimes:

1. **large branch:** canonical `ell=P^+(ruCD)>X^eta`, with one of the t26 routed congruence states;
2. **smooth branch:** `P^+(ruCD)<=X^eta`, but still satisfying the physical cover equation.

A fixed power saving

\[
\boxed{
\#\mathcal L_\eta(X)+\#\mathcal S_\eta(X)
=O(X^{1/2-\delta})
}
\]

uniformly on dyadic shells closes `T(B)=o(sqrt B)` after the t22 `B^{o(1)}` fixed-direction multiplicity.

## 9. Frozen finite diagnostics

The t27 audit performs two independent checks through `B=2,000,000`.

First, it regenerates the actual Stage14 raw-pair graph and verifies that the frozen range contains no `(alpha,beta)=(1,1)` edge, equivalently no triple object.

Second, independently of physical activation, it enumerates the entire primitive `(1,1)` **candidate direction** universe through `D<=2,000,000` and records, on every standard cutoff and on the top dyadic shell, how many candidate directions satisfy

\[
P^+(r u C D)\le B^\eta
\]

for several fixed `eta`. These are ambient candidate diagnostics only. They are not promoted to an asymptotic estimate for active directions.

## Boundary

```text
STAGE14_T27=COMPLETE_TRIVIAL_KERNEL_TARGET_COMPRESSION_AND_COVER_CONDITIONED_FRIABILITY_SPLIT
TRIVIAL_KERNEL_PARTITION_ONLY_1_1=true
N_11_EQUALS_3T=true
DANGER_FIBER_PRIMITIVE_PYTHAGOREAN=true
FIXED_DIRECTION_TRANSFER_TO_A11=true
GLOBAL_SECOND_MOMENT_REQUIRED_FOR_PRIMARY_T_TARGET=false
PRIMARY_SUFFICIENT_TARGET=A_11(B)=O(B^(1/2-delta))
DYADIC_LARGE_SMOOTH_SPLIT_EXPLICIT=true
ODD_LARGE_BRANCH_ROUTING_COMPLETE_FROM_T26=true
LE_BOUDEC_POSITIVE_PROPORTION_LARGE_PRIME_SUBSET_NOT_EXHAUSTIVE=true
ONE_QUADRATIC_COLUMN_SMOOTH_EXCEPTION_POWER_SAVING_AVAILABLE=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
ROUTED_LARGE_BRANCH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t28 cover-conditioned (1,1) dyadic incidence count: canonical largest-prime routed branch plus physical smooth branch
```
