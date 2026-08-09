# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t controls the triple/perfect-cuboid correction term in

\[
E(B)=N_2(B)+3T(B).
\]

It is separate from the main `14-4` raw-pair/Kummer track and the `14-e` ambient track.

## 14-t1 — baseline and theorem gap
Status: [x] Complete.

## 14-t2 — quantitative boundary
Status: [x] Complete.

## 14-t3 — Humbert-Edge splitting
Status: [x] Complete.

## 14-t4 — elliptic compression and Kummer restriction
Status: [x] Complete.

## 14-t5 / t5a — fixed minimal-curve transfer gate
Status: [x] Complete. Stage14-4ak eliminates the final fixed physical `M`-degree-4 mechanism.

## 14-t6 — reflected moving double-small-point gate
Status: [x] Complete. Triple points require compatible logarithmic small points on the reflected quotient pair `E_+(s), E_+(-s)`.

## 14-t7 — shared-q conic and fixed-prime boundary
Status: [x] Complete. The exact conic relation is useful structurally but the naive fixed-prime square-class sieve is vacuous on physical bases.

## 14-t8 — reflected moving-prime local boundary
Status: [x] Complete. At new reflected primes the local square condition is automatic unless the easy unit argument degenerates at `q^2=-1 mod p`.

## 14-t9 — Euclid sparse-residue formulation
Status: [x] Complete, with interpretation corrected by t10.

## 14-t10 — character-sieve direction audit
Status: [x] Complete. The sparse reflected residue support is an exceptional regime where automatic local solubility stops, not a necessary thinning condition for every triple.

## 14-t11 — compatible paired small-point activation
Status: [x] Complete. Define `V_pair(B)` and object-level `P(B)` for compatible shared-`q` points; simultaneous rank or unrelated small points are insufficient.

## 14-t12 — point-conditioned reflected-square parameter gate
Status: [x] Complete.

Conditioning on a raw point and parametrizing the auxiliary right triangle by `r` gives

\[
y^2+B_{t,r}y+1=0,\qquad y=q^2,
\]

with

\[
B_{t,r}=2\frac{1-t^2}{1+t^2}-\frac{(1-r^2)^2}{t^2(1+t^2)r^2}.
\]

Compatibility requires both `D_{t,r}=B_{t,r}^2-4` square and the selected root `y` itself square in the physical height window.

## 14-t13 — discriminant-cover geometry
Status: [x] Complete.

The discriminant cover is genus 3 on every genuine physical rational base:

\[
Z^2=(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1).
\]

There are no physical branch-collision fibers of genus 0, 1, or 2.

## 14-t14 — bielliptic quotient and second-square decomposition
Status: [x] Complete.

With `x=r^2`, the full discriminant-square plus `y=q^2` gate separates as

\[
U^2=(x-1)^2-4t^2x,
\]

\[
V^2=x^2+(4t^4-2)x+1,
\]

with `x` itself required to be a rational square and with the physical height cutoff retained.

## 14-t15 — simultaneous two-conic plus x-square fiber product
Status: [x] Complete.

Let

\[
A_t(x)=(x-1)^2-4t^2x,
\qquad
B_t(x)=x^2+(4t^4-2)x+1.
\]

The x-level fiber product

\[
C_{0,t}:\quad U^2=A_t(x),\qquad V^2=B_t(x)
\]

has genus one for every genuine physical rational base. Indeed

\[
\operatorname{disc}(A_t)=16t^2(t^2+1),
\]

\[
\operatorname{disc}(B_t)=16t^4(t-1)(t+1)(t^2+1),
\]

\[
\operatorname{Res}(A_t,B_t)=16t^4(t^2+1)^2,
\]

so its four quadratic branch points are distinct on every physical fiber.

Reimposing `x=r^2` gives a double cover `C_t -> C_{0,t}` branched at the four points above `x=0` and four points above `x=infinity`. Hence

\[
\boxed{g(C_t)=5}.
\]

Over the r-line the `(Z/2)^2` sign quotients have genus pattern

```text
U-only quotient        1
V-only quotient        1
UV quotient            3
```

and therefore

\[
J(C_t)\sim E_{A,t}\times E_{B,t}\times J(G_t).
\]

No physical low-genus degeneration or component splitting occurs. The reduction has reconstructed the original genus-five triple fiber as an eight-branch square lift of a moving elliptic curve.

## 14-t16 — square-x lift on the moving elliptic family
Status: [x] Complete.

Treat

\[
C_{0,t}: U^2=A_t(x),\quad V^2=B_t(x)
\]

as the base elliptic family and count rational points for which

\[
x\in(\mathbf Q^\times)^2.
\]

The divisor is `div(x)=D_0-D_infinity`, with both divisors reduced of degree four. Thus `r^2=x` is ramified at eight points and is not an ordinary etale elliptic `2`-cover/E[2] Kummer torsor. It is a branched quadratic-cover/Prym interface, and ordinary Mordell--Weil modulo 2 is insufficient by itself.

## 14-t17 — square-value sieve on the branched cover
Status: [>] Next.

Formulate a square-value/branched-cover sieve on `C_{0,t}` using the Prym or generalized-Jacobian interface, averaged over physical rational Pythagorean `t`, while retaining the physical height window.

Primary target remains

\[
T(B)=o(\sqrt B).
\]

## Scope boundary

Stage14-t is a population-counting track, not a finite-search proof of perfect-cuboid nonexistence.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
STAGE14_T4=COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION
STAGE14_T5=COMPLETE_FIXED_M4_TRANSFER_GATE_ZERO_CASES
STAGE14_T6=COMPLETE_MIRROR_DOUBLE_SMALL_POINT_GATE
STAGE14_T7=COMPLETE_SHARED_Q_CONIC_AND_LOCAL_SIEVE_BOUNDARY
STAGE14_T8=COMPLETE_REFLECTED_MOVING_PRIME_LOCAL_BOUNDARY
STAGE14_T9=COMPLETE_EUCLID_SPARSE_RESIDUE_SIEVE_FORMULATION
STAGE14_T10=COMPLETE_CHARACTER_SIEVE_DIRECTION_AUDIT
STAGE14_T11=COMPLETE_COMPATIBLE_PAIRED_ACTIVATION_FORMULATION
STAGE14_T12=COMPLETE_CONDITIONAL_REFLECTED_SQUARE_PARAMETER_GATE
STAGE14_T13=COMPLETE_DISCRIMINANT_COVER_GENUS_CLASSIFICATION
STAGE14_T14=COMPLETE_BIELLIPTIC_QUOTIENT_AND_SECOND_SQUARE_DECOMPOSITION
STAGE14_T15=COMPLETE_THREE_SQUARE_FIBER_PRODUCT_CLASSIFICATION
STAGE14_T16=COMPLETE_SQUARE_X_DIVISOR_AND_RAMIFIED_COVER_BOUNDARY
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t17 square-value/branched-cover sieve with Prym or generalized-Jacobian and physical height
```
