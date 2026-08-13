# Stage14-t17 — generalized-Jacobian square-value sieve interface

## Purpose

Stage14-t16 identifies the remaining lift

\[
\pi_t:C_t\longrightarrow C_{0,t},\qquad r^2=x,
\]

as a quadratic cover of the elliptic curve

\[
C_{0,t}:\quad U^2=A_t(x),\qquad V^2=B_t(x)
\]

ramified at the reduced degree-eight divisor

\[
\mathfrak m_t=D_0+D_\infty.
\]

The purpose of t17 is to formulate the correct arithmetic sieve interface for the square-value condition while retaining the physical Stage14 height window. No estimate for `T(B)` is promoted here.

## 1. Prym geometry is four-dimensional

Let

\[
P_t=\ker\!\left(\operatorname{Nm}_{\pi_t}:J(C_t)\to J(C_{0,t})\right)^0.
\]

Since `g(C_t)=5` and `g(C_{0,t})=1`,

\[
\dim P_t=4.
\]

Thus the ramified double cover has a genuine four-dimensional Prym contribution. The usual pullback/norm relation gives the standard isogeny-level decomposition

\[
J(C_t)\sim J(C_{0,t})\times P_t.
\]

This is useful geometry, but by itself it does not turn the square-value condition into a Mordell--Weil-mod-2 condition on the elliptic quotient.

## 2. The branch modulus gives the correct generalized Jacobian

The eight branch points are rational on every physical fiber: above `x=0` they are the four points `(0,\pm1,\pm1)` and above `x=\infty` the monic leading terms give the four independent sign choices `U/x=\pm1`, `V/x=\pm1`.

For the reduced split modulus

\[
\mathfrak m_t=D_0+D_\infty,
\qquad \deg \mathfrak m_t=8,
\]

let `J_{\mathfrak m_t}` be the generalized Jacobian of `C_{0,t}`. Its toric extension is

\[
1\to T_{\mathfrak m_t}\to J_{\mathfrak m_t}\to J(C_{0,t})\to0,
\]

with

\[
T_{\mathfrak m_t}
=\operatorname{Res}_{\mathfrak m_t}\mathbf G_m/\mathbf G_m
\cong \mathbf G_m^7,
\]

so

\[
\dim J_{\mathfrak m_t}=1+7=8.
\]

This is precisely the type of modulus setup in generalized-Jacobian explicit descent: `n=2` divides `deg(\mathfrak m_t)=8`, and exponent-two coverings ramified only at the prescribed modulus are handled through the associated semiabelian descent isogeny. The Stage14 cover `r^2=x` therefore belongs in this branch-sensitive framework rather than ordinary elliptic `E[2]` descent.

Primary literature interface:

- Brendan Creutz, *Generalized Jacobians and explicit descents*, arXiv:1601.06445.
- Valeria Ornella Marcucci and Juan Carlos Naranjo, *Prym varieties of double coverings of elliptic curves*, arXiv:1111.3340.
- Nils Bruin, Bjorn Poonen and Michael Stoll, *Generalized explicit descent and its application to curves of genus 3*, arXiv:1205.4456.

These references supply the descent/Prym framework only. They do not supply the Stage14 family average or the physical-height estimate required below.

## 3. Exact squareclass detector

For

\[
P\in C_{0,t}(\mathbf Q)\setminus |\mathfrak m_t|,
\]

define

\[
\delta_t(P)=[x(P)]\in \mathbf Q^\times/\mathbf Q^{\times2}.
\]

Then the branched lift has a rational point above `P` exactly when

\[
\boxed{\delta_t(P)=1}.
\]

For a finite set of places `S`, define the truncated local detector

\[
\delta_{t,S}(P)=([x(P)]_v)_{v\in S}
\in H_S:=\prod_{v\in S}\mathbf Q_v^\times/\mathbf Q_v^{\times2}.
\]

A global square necessarily has trivial image in `H_S`, hence every finite local sieve gives a valid upper bound. Character orthogonality gives the exact identity

\[
1_{\delta_{t,S}(P)=1}
=
\frac1{|H_S|}\sum_{\chi\in\widehat H_S}
\chi(\delta_{t,S}(P)).
\]

This is the t17 conversion from a branched square-value condition to a character-sum problem.

## 4. Physical-height family average

Let `\mathcal W_t(B)` denote the rational points on `C_{0,t}` that lie in the physical Stage14 open set, reconstruct the t12--t15 configuration, and have physical cuboid height at most `B`. Define the square-lift incidence count

\[
\mathcal P_{\square}(B)
=
\sum_{t\ \mathrm{physical}}
\sum_{P\in\mathcal W_t(B)}
1_{\delta_t(P)=1}.
\]

The fixed Stage14 orientation/sign bookkeeping has bounded multiplicity, so controlling `\mathcal P_{\square}(B)` controls the triple-object count. In particular, a bound

\[
\mathcal P_{\square}(B)=o(\sqrt B)
\]

is sufficient for the primary t-track target `T(B)=o(\sqrt B)`.

For any chosen finite place set `S=S(t,B)` one has

\[
\mathcal P_{\square}(B)
\le
\sum_t\sum_{P\in\mathcal W_t(B)}
1_{\delta_{t,S}(P)=1}.
\]

Applying character orthogonality turns the right side into a trivial-character term plus nontrivial character sums over the moving elliptic family.

## 5. The place set must be branch-sensitive and moving

Stages t7--t10 already show that a naive fixed-prime sieve can be vacuous on the physical family. Therefore t17 does **not** select one universal finite set of primes and claim thinning.

The next analytic step must choose places from the moving arithmetic support, including primes exposed by the Euclid parameter and by the numerator/denominator of the physical point, while respecting the branch modulus `\mathfrak m_t`. The desired estimate has the form

\[
\frac1{|H_{S(t,B)}|}
\left(
M(B)
+
\sum_{\chi\ne1}
\left|
\sum_t\sum_{P\in\mathcal W_t(B)}
\chi(\delta_{t,S(t,B)}(P))
\right|
\right)
=o(\sqrt B),
\]

where `M(B)=\sum_t|\mathcal W_t(B)|` is the unsieved x-level candidate count. This formula is a theorem target, not a theorem proved in t17.

The generalized-Jacobian formulation is important because it keeps the eight branch points in the descent object instead of erasing them in the ordinary elliptic quotient.

## 6. What t17 closes

The remaining triple gate is now expressed as one exact global squareclass condition, one exact finite-place character projector, and one moving physical-height family average. This removes the ambiguity left by t16 about what a valid `2`-descent/sieve must remember.

It does **not** prove:

- cancellation for any nontrivial character family;
- a growing useful local-image rank;
- an average multiplicity bound on `\mathcal W_t(B)`;
- `T(B)=o(\sqrt B)`;
- perfect-cuboid nonexistence.

## Locked boundary

```text
STAGE14_T17=COMPLETE_GENERALIZED_JACOBIAN_SQUARECLASS_SIEVE_INTERFACE
BRANCH_MODULUS_DEGREE=8
BRANCH_MODULUS_SPLIT_RATIONAL=true
PRYM_DIMENSION=4
GENERALIZED_JACOBIAN_TORUS_RANK=7
GENERALIZED_JACOBIAN_DIMENSION=8
SQUARE_LIFT_IFF_GLOBAL_X_SQUARECLASS_TRIVIAL=true
FINITE_LOCAL_CHARACTER_PROJECTOR_EXACT=true
FIXED_UNIVERSAL_PRIME_SIEVE_CLAIMED=false
MOVING_BRANCH_SENSITIVE_PLACE_SET_REQUIRED=true
PHYSICAL_HEIGHT_WINDOW_RETAINED=true
CHARACTER_CANCELLATION_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t18 derive the explicit branch-modulus 2-descent/local image and first moving character-sum inequality
```
