# Stage14-t roadmap — triple-gate side track

## Canonical batch entry point

The permanent execution entry point for advancing this route is:

```text
Stage14-t-batch
```

Before deriving a concrete successor, first read
[`stages/stage14/archive/docs/operations/stage14-batch-common-contract.md`](../../stages/stage14/archive/docs/operations/stage14-batch-common-contract.md)
and then
[`stages/stage14/archive/docs/operations/stage14-t-batch-task-contract.md`](../../stages/stage14/archive/docs/operations/stage14-t-batch-task-contract.md)
from latest merged `main`. The entry point advances the existing t ledger; it
does not create a parallel numbering system. A normal run follows the unique
merged `NEXT` chain for 3--5 substantive work units on one branch and publishes one
Draft PR at the batch boundary.

The batch stops early when the fixed-`U` receiver changes, an integrated tH audit
leaves an unresolved external gate, or a rigorous counterexample is obtained.
It also stops at five work units. Every internal stage records the tH decision
and, when needed, the exact frozen request and target. A new tH is normally run
inside the same branch and Draft PR, counts as one of the 3--5 substantive work
units, and remains a clean-room frozen-snapshot audit. Existing tH work is never
rewritten to chase the batch.

```text
STAGE14_T_CANONICAL_EXECUTION_ENTRY=Stage14-t-batch
STAGE14_T_BATCH_MINIMUM_TARGET_WORK_UNITS=3
STAGE14_T_BATCH_MAXIMUM_WORK_UNITS=5
STAGE14_T_BATCH_MINIMUM_TARGET_STAGES=3
STAGE14_T_BATCH_MAXIMUM_STAGES=5
STAGE14_T_BATCH_ONE_BRANCH_ONE_PR=true
STAGE14_T_BATCH_EARLY_STOP=receiver_change|unresolved_external_gate|rigorous_counterexample
STAGE14_T_BATCH_EVERY_STAGE_RECORDS_TH_DECISION=true
STAGE14_T_BATCH_INTEGRATES_NEW_TH=true
STAGE14_T_BATCH_H_COUNTS_AS_WORK_UNIT=true
STAGE14_T_BATCH_REWRITES_EXISTING_TH_TARGET=false
```

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
C_{0,t}:\quad U^2=A_t(x),\quad V^2=B_t(x)
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

Reimposing `x=r^2` gives a double cover `C_t -> C_{0,t}` branched at the four points above `x=0` and four above `x=infinity`. Hence

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

## 14-t17 — generalized-Jacobian square-value sieve
Status: [x] Complete.

Let `m_t=D_0+D_infinity`. The cover has Prym dimension `5-1=4`. Since the eight branch points are rational, the generalized Jacobian of `C_{0,t}` with modulus `m_t` is an extension of the elliptic Jacobian by the split torus

\[
\operatorname{Res}_{m_t}\mathbf G_m/\mathbf G_m\cong\mathbf G_m^7.
\]

For `P` away from the branch modulus the lift condition is exactly

\[
\delta_t(P)=[x(P)]=1\in\mathbf Q^\times/\mathbf Q^{\times2}.
\]

At any finite place set `S`, the local squareclass condition has an exact finite-character projector. Thus the triple gate is reduced to a branch-sensitive moving character-sum average over physical points on `C_{0,t}` with the original cuboid-height cutoff. A fixed universal prime set is not asserted to thin the family.

## 14-t18 — selected branch local image and packet Fourier bound
Status: [x] Complete.

The eight branch points have a seven-dimensional quadratic branch-character space, and the Stage14 cover `r^2=x` selects the all-ones monodromy vector.

For this selected character the local squareclass map is surjective at every completion. Thus there is no local-image density saving; the required thinning must come from global distribution of squareclass signatures.

On a packet with `r` selected quadratic characters, total candidate count `M`, and signature collision count `Q=sum_a n_a^2`, finite Fourier orthogonality and Parseval give

\[
E_{\ne0}=2^rQ-M^2,
\]

and Cauchy--Schwarz gives

\[
N_\square\le\frac{M}{2^r}+\sqrt{(1-2^{-r})\left(Q-\frac{M^2}{2^r}\right)}.
\]

## 14-t19 — conditioned discriminant identity and finite collision ledger
Status: [x] Complete, with the asymptotic collision population corrected by t20.

Instantiating the t12--t18 variables on the actual raw Stage14 ledger gives

\[
\Delta_x=\left(\frac{t(1+t^2)(1-q^2)R}{q^2}\right)^2(t^2+u^2),
\]

so `[Delta_x]=[t^2+u^2]`, exactly the missing third-face squareclass after shared-edge scaling. Thus the conditioned discriminant is not a new independent gate.

The exact finite ledger through `B=2,000,000` has 356 exactly-two objects, all with distinct missing-face squareclasses. Because `T(B)=0` throughout the frozen range, this ledger is also the raw-pair-edge ledger there. The finite computation remains valid; only the earlier asymptotic statement for an exactly-two-only collision population is superseded by t20.

## 14-t20 — raw-edge collision correction and coprime factor reduction
Status: [x] Complete.

Use the raw-pair edge population: one edge for an exactly-two object and three edges for a triple object. For an edge with shared side `s` and space diagonal `d`, define

\[
m=d^2-s^2,\qquad \kappa=[m].
\]

Then

\[
E(B)=N_2(B)+3T(B),\qquad n_1(B)=3T(B),
\]

and therefore

\[
9T(B)^2\le Q_{edge}(B),\qquad Q_{edge}(B)=\sum_k n_k(B)^2.
\]

Hence `Q_edge(B)=o(B)` is a valid sufficient target for `T(B)=o(sqrt(B))`.

The edge squareclass admits the coprime factorization

\[
g=(d,s),\quad D=d/g,\quad C=s/g,\quad h=(D-C,D+C)\in\{1,2\},
\]

\[
A=(D-C)/h=\alpha r^2,\qquad B=(D+C)/h=\beta u^2,
\]

with squarefree coprime `alpha,beta` and `kappa=alpha beta`. The missing-face kernel uses only `2` and primes `1 mod 4`.

For the partition-resolved counts `N_{alpha,beta}(B)`, one has

\[
Q_{edge}(B)\le B^{o(1)}Q_{split}(B),
\qquad
Q_{split}(B)=\sum_{\alpha,\beta}N_{\alpha,\beta}(B)^2.
\]

Thus any fixed power saving `Q_split(B)=O(B^{1-delta})` would close the t-track target.

## 14-t21 — partition-resolved direction/scale reduction
Status: [x] Complete.

For a fixed split partition, put

\[
a=\alpha r^2,\qquad b=\beta u^2,
\qquad (a,b)=1,\quad b>a.
\]

The parity factor is uniquely determined by

\[
h=1\iff a,b\text{ both odd};\qquad h=2\text{ otherwise},
\]

and the reduced direction is exactly

\[
\boxed{D=\frac h2(a+b),\qquad C=\frac h2(b-a).}
\]

Conversely these formulas recover the t20 factorization, giving a bijection between admissible `(alpha,beta,r,u)` and normalized directions `(D,C)`.

The remaining scale satisfies `d=gD`, `s=gC`. Primitivity forces every prime divisor of `g` to satisfy `p=1 mod 4`; in particular `g` is odd. For fixed `(alpha,beta,r,u,g)`, the two integral-face equations give at most `tau(s^2)^2=B^o(1)` possible ordered face completions. Therefore

\[
N_{\alpha,\beta}(B)
\le B^{o(1)}
\sum_{(r,u)\in\mathcal R_{\alpha,\beta}(B)}
\left\lfloor\frac{B}{D_{\alpha,\beta}(r,u)}\right\rfloor
\]

and the coarse harmonic estimate gives

\[
N_{\alpha,\beta}(B)\ll\frac{B^{1+o(1)}}{\sqrt{\alpha\beta}}.
\]

This bound is not strong enough to give a power saving for `Q_split`: small-kernel fibers, including `(1,1)`, remain too large in the majorant. The missing input is now isolated as a simultaneous face-completion correlation over scales and generalized-Pell directions.

At `B=2m`, all 356 observed reduced directions and all 356 split partitions remain distinct; 317 edges have `g=1`, and the 39 nontrivial-scale edges use observed scales `5,13,17,29,37,41`. This is finite diagnostic evidence only.

## 14-t22 — uniform fixed-direction simultaneous-completion bound
Status: [x] Complete.

For fixed reduced `(D,C)`, normalize a raw edge by

\[
X=x/g,\quad Y=y/g,\quad P=H_1/g,\quad Q=H_2/g.
\]

All scales in that direction lie on

\[
P^2=C^2+X^2,\qquad Q^2=C^2+Y^2,\qquad X^2+Y^2=D^2-C^2.
\]

The bounded-degree elliptic quotient is

\[
R^2=(D^2-C^2-X^2)(D^2-X^2),\qquad R=YQ.
\]

With

\[
U=\frac{2D}{D-X},\qquad V=\frac{2DR}{(D-X)^2},
\]

this becomes

\[
V^2=(U-1)(-C^2U^2+4D^2U-4D^2).
\]

Equivalently, `x_E=-U`, `y_E=V/C` gives a monic Weierstrass equation with the nonzero rational 2-torsion point `(-1,0)`. Primitivity also makes the physical scale canonical:

\[
\boxed{g=\operatorname{lcm}(\operatorname{den}X,\operatorname{den}Y).}
\]

Physical height transfers polynomially: `H(U)<=2d` and a crude `H(V)<=2d^3`. The quotient equation height is polynomial in `D,C`. Dujella's uniform bounded-height theorem for elliptic curves with rational prime-order torsion therefore gives, uniformly over all reduced directions,

\[
\boxed{M_{D,C}(B/D)=B^{o(1)}.}
\]

Thus scale reuse is closed at the polynomial-exponent level. If `A_{alpha,beta}(B)` counts active reduced directions in a fixed split partition, then

\[
N_{\alpha,\beta}(B)\le B^{o(1)}A_{\alpha,\beta}(B),
\]

and hence

\[
Q_{split}(B)\le B^{o(1)}Q_{active-dir}(B),
\qquad
Q_{active-dir}(B)=\sum_{\alpha,\beta}A_{\alpha,\beta}(B)^2.
\]

Any fixed power saving for this active-direction second moment now closes the t-track target. At `B=2m` the 356 frozen edges still occupy 356 distinct active directions and 356 distinct partitions, so the finite `Q_active-dir` equals 356; this is diagnostic only.

## 14-t23 — torsion / positive-rank dichotomy and order-8 packet
Status: [x] Complete.

Shift the t22 quotient by `z=1-U`. Then

\[
E_{D,C}: y^2=z\left(z^2+\left(4D^2/C^2-2\right)z+1\right)
\]

contains the rational order-four point `(1,2D/C)`. Every physical point satisfies

\[
z=-\left(\frac{D+X}{Q}\right)^2<-1,
\]

so its rational 2-isogeny Kummer class is `[-1]`. Combining this with Mazur's torsion classification and the exact duplication formula shows that a physical quotient point can be torsion only with exact order eight.

For a physical point

\[
x(2P)=\left(\frac{CX}{QY}\right)^2,
\]

and order eight forces `x(2P)=1`, equivalently

\[
X^2=D(D-C).
\]

The physical equations then give `Q^2=CD` and `Y^2=C(D-C)`. Since `(D,C)=1`, this implies

\[
D=a^2,\qquad C=b^2,\qquad D-C=c^2,
\qquad a^2=b^2+c^2.
\]

Hence torsion-active reduced directions have first moment `O(B^{1/2+o(1)})` under `D<=B`. Moreover their split partitions lie in two explicit quartic squarefree-kernel packets:

\[
\alpha=1,\quad \beta=\operatorname{core}(m^4+6m^2n^2+n^4),
\]

or

\[
\alpha=2,\quad \beta=\operatorname{core}(m^4+n^4).
\]

Thus the active-direction second moment splits into a positive-rank branch and an explicit quartic torsion branch:

\[
Q_{active-dir}\le2Q_{rank}+2Q_{tor}.
\]

At `B=2m` there are zero order-eight necessary hits, so all 356 frozen active edges are certified to map to non-torsion quotient points and hence positive-rank direction quotients. This remains finite evidence for the family distribution.

## 14-t24 — split second-moment attack
Status: [>] Next.

Attack the two residual energies separately:

1. `Q_tor(B)`: squarefree-kernel collisions of the explicit quartics `m^4+n^4` and `m^4+6m^2n^2+n^4`, now eligible for the q4/q6 polynomial-square-sieve route;
2. `Q_rank(B)`: positive-rank generalized-Pell direction activation in the physical small-height window, with q3 height-frequency tools as the natural comparison route.

A fixed power saving for both implies one for `Q_active-dir`, then `Q_split`, then `Q_edge=o(B)`, and finally

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
STAGE14_T17=COMPLETE_GENERALIZED_JACOBIAN_SQUARECLASS_SIEVE_INTERFACE
STAGE14_T18=COMPLETE_SELECTED_BRANCH_LOCAL_IMAGE_AND_PACKET_FOURIER_BOUND
STAGE14_T19=COMPLETE_CONDITIONED_DISCRIMINANT_IDENTITY_AND_FINITE_COLLISION_LEDGER
STAGE14_T20=COMPLETE_RAW_EDGE_COLLISION_CORRECTION_AND_COPRIME_FACTOR_REDUCTION
STAGE14_T21=COMPLETE_PARTITION_DIRECTION_SCALE_REDUCTION
STAGE14_T22=COMPLETE_UNIFORM_FIXED_DIRECTION_ELLIPTIC_QUOTIENT_BOUND
STAGE14_T23=COMPLETE_TORSION_POSITIVE_RANK_DICHOTOMY_AND_ORDER8_PACKET_REDUCTION
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t24 split second-moment attack / quartic torsion packet plus rank-active height frequency
```
