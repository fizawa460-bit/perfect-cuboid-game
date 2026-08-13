# Stage14-4bj — L/S reunification and least-denominator post-local gate

## Purpose

Stage14-4bi was temporarily split into `L` and `S` lanes. Both are now merged, and the split ends here.

This stage formally imports merged:

- `14-4bi-L`: composite edge-kernel incidence and large-kernel `incidence OR small-D` dichotomy;
- `14-4bi-S`: full-leg-radical incidence, radical-poor base sparsity, and reduction to a radical-rich/small-D core;
- `14-s6-03`: centered-quartic coordinate sieve and `D<=2 max(|u1|,|u2|)`;
- `14-s6-04`: exact-witness auxiliary-character resonance, exact modulus `D^2`, and the least-denominator packet statistic.

The objective is to collapse these results into one main-track contract, choose the critical exponents forced by the existing `41/42` bound, and identify the unique remaining packet-level quantitative gate.

No positive full-family post-local exponent is claimed in 4bj.

---

## 1. Exact exponent budget

The physical upper bound remains

\[
V(B)\ll_\epsilon B^{41/42+\epsilon}.
\]

The square-root target is `B^(1/2+epsilon)`, so the missing exponent is

\[
\boxed{\frac{41}{42}-\frac12=\frac{10}{21}.}
\tag{BJ.1}
\]

Any positive packet-level `delta_post` is genuine progress; `delta_post>=10/21` reaches the square-root upper-bound scale.

---

## 2. Reunified exact witness system

For a primitive Pythagorean base

\[
S^2+X^2=H^2,
\]

the integral witness packet has

\[
d_0u_0^2-d_1u_1^2=S^2D^2,
\qquad
 d_2u_2^2-d_0u_0^2=X^2D^2,
\]

hence

\[
\boxed{d_2u_2^2-d_1u_1^2=H^2D^2.}
\tag{BJ.2}
\]

The odd squarefree kernel factorization is

```text
d0=tau0*a*b,
d1=tau1*a*c,
d2=tau2*b*c,
```

with

```text
a | rad_odd(S),
b | rad_odd(X),
c | rad_odd(H).
```

Merged `14-4bi-S` proves the stronger full-radical congruence

\[
\tau_2b u_2^2\equiv\tau_1a u_1^2
\pmod{R_H},
\qquad
R_H:=\operatorname{rad}_{odd}(H).
\tag{BJ.3}
\]

Thus neither a tiny selected kernel nor a large-but-smooth kernel is an intrinsic obstruction.

---

## 3. Reunified structural partition

For thresholds `rho,nu>0`, every supported exact witness lies in one of three sectors.

### A. Radical-poor base/class sector

If

\[
R_H\le B^\rho,
\]

merged `14-4bi-S` gives the genuine base/class estimate

\[
\boxed{
\#\{\text{supported base/classes}:R_H\le B^\rho\}
\ll_\epsilon B^{\rho+\epsilon}.
}
\tag{BJ.4}
\]

This is already at packet level.

### B. Radical-rich, long witness sector

If

\[
R_H>B^\rho,
\qquad
U_*:=\max(|u_1|,|u_2|)\ge B^\nu,
\]

the full-radical CRT lattice bound gives

\[
N_H(U_1,U_2)
\ll_\epsilon B^\epsilon
\left(
\frac{U_1U_2}{R_H}+\min(U_1,U_2)+1
\right),
\]

so the fixed witness-coordinate layer gains

\[
B^{-\min(\rho,\nu)+\epsilon}.
\tag{BJ.5}
\]

This is a coordinate-density theorem, not yet an unweighted packet-existence theorem.

### C. Radical-rich, short witness sector

If `R_H>B^rho` but `U_*<B^nu`, then merged s6-03 / 4bi-S gives

\[
\boxed{D\le2U_*<2B^\nu.}
\tag{BJ.6}
\]

Hence every coordinate-level complement lands in the small-denominator sector.

There is no residual large-prime, smooth-kernel, tiny-kernel, or independent short-variable sector.

---

## 4. Critical threshold choice

Take

\[
\boxed{\rho=\frac12.}
\tag{BJ.7}
\]

Then (BJ.4) gives

\[
R_H\le B^{1/2}
\quad\Longrightarrow\quad
O(B^{1/2+\epsilon})
\]

supported base/classes. The radical-poor family is therefore already harmless at square-root scale.

Only

\[
\boxed{R_H>B^{1/2}}
\tag{BJ.8}
\]

can still contribute above the target.

Now take

\[
\boxed{\nu=\frac{10}{21}.}
\tag{BJ.9}
\]

On the radical-rich family, if `U_*>=B^(10/21)`, then

\[
\min\left(\frac12,\frac{10}{21}\right)=\frac{10}{21},
\]

so the full-radical coordinate modulus supplies exactly the entire missing coordinate exponent.

If instead `U_*<B^(10/21)`, then

\[
\boxed{D<2B^{10/21}.}
\tag{BJ.10}
\]

Thus `1/2` and `10/21` are the natural critical thresholds for the reunified ledger.

This still does not prove the square-root upper bound because coordinate density cannot be multiplied blindly by the unweighted local packet count.

---

## 5. Exact-witness auxiliary-character route is closed

Merged s6-03 has centered quartics satisfying on every exact witness

```text
Phi0(u0,D)=(k*u1*u2)^2,
Phi1(u1,D)=(k*u0*u2)^2,
Phi2(u2,D)=(k*u0*u1)^2.
```

Merged s6-04 observes that for every good auxiliary prime not dividing the square root,

\[
\chi(\Phi_i)=+1.
\]

Therefore a moving auxiliary-character sum whose weight already retains the exact witness equations is resonant rather than oscillatory. Choosing one canonical exact witness per packet does not change this: its centered quartic is still a square.

Hence

```text
EXACT_WITNESS_AUXILIARY_CHARACTER_RESONANCE=true
MOVING_EXACT_WITNESS_CHARACTER_CANCELLATION_TARGET_VALID=false
CANONICAL_SELECTOR_ALONE_CREATES_AUXILIARY_CANCELLATION=false.
```

The fixed-packet square sieve from s6-03 remains correct before conditioning on exact witness support; only the proposed transfer mechanism is rejected.

---

## 6. Denominator-square incidence

From (BJ.2), merged s6-04 gives the exact modulus

\[
\boxed{d_2u_2^2\equiv d_1u_1^2\pmod{D^2}.}
\tag{BJ.11}
\]

Primitive denominator coprimality implies the coefficients and `u1,u2` are units at primes dividing `D`.

For each odd prime power in `D^2`, the unit quadratic ratio has at most two roots; the 2-primary part contributes at most four. Thus `(u1,u2)` lies on at most

\[
4\,2^{\omega(D_{odd})}=D^{o(1)}
\]

projective lines modulo `D^2`, and

\[
\boxed{
N_D(U_1,U_2)
\ll_\epsilon
D^\epsilon
\left(
\frac{U_1U_2}{D^2}+\min(U_1,U_2)+1
\right).
}
\tag{BJ.12}
\]

Using `D<=2U_*`, a dyadic layer with `D>=B^eta` has relative coordinate saving at least

\[
B^{-\eta+\epsilon}.
\tag{BJ.13}
\]

At `eta=10/21`, the denominator modulus independently reaches the full missing coordinate exponent.

Again, this is not itself an unweighted packet-count theorem.

---

## 7. Unique packet-level statistic

For a locally admissible supported packet `pi=(F,sigma)` in the fixed bounded-height window inherited from Stage14-s3, define

\[
D_{\min}(\pi;B)
=
\min\{D(Q):Q\text{ is an admissible bounded-height non-torsion global witness in }\pi\},
\]

and `D_min=+infinity` if the packet has no such witness.

The physical count is majorized by the number of packets with finite `D_min`.

After all L/S and s6-04 reductions, the unique unresolved quantitative problem is therefore:

> count radical-rich locally-admissible packets with finite `D_min` directly at packet level.

The natural critical split is

```text
R_H > B^(1/2),
D_min <  B^(10/21)   : small least-denominator tail,
D_min >= B^(10/21)   : large least-denominator tail.
```

The large tail carries enough coordinate congruence strength, but a packet-occupancy theorem is still needed to convert that structure into an unweighted packet saving. The small tail must be counted using the bounded denominator itself.

A sufficient packet-level target is

\[
\#\{\pi:R_H>B^{1/2},\ D_{\min}(\pi;B)<\infty\}
\ll B^{41/42-\delta+\epsilon}.
\tag{BJ.14}
\]

Any `delta>0` is the first genuine direct post-local packet saving. The square-root upper-bound scale requires

\[
\boxed{\delta\ge\frac{10}{21}.}
\tag{BJ.15}
\]

---

## 8. Reunification decision

The temporary parallelization is now retired permanently for the `14-4` main track.

Closed:

- L/S branch split;
- largest-prime dependence;
- large-but-smooth kernel obstruction;
- tiny selected-kernel obstruction;
- radical-poor family above square-root relevance;
- independent short-variable complement;
- moving exact-witness auxiliary-character cancellation as a candidate mechanism;
- denominator-square incidence geometry.

Open:

- radical-rich `D_min` packet distribution / canonical-witness occupancy;
- any positive full-family `delta_post`;
- the square-root upper bound and asymptotic.

The next main-track stage attacks `D_min` directly. Do not reopen L/S lanes.

---

## Boundary flags

```text
STAGE14_4BJ=LS_REUNIFIED_AND_LEAST_DENOMINATOR_GATE_FROZEN
TEMPORARY_LS_PARALLELIZATION_CLOSED=true
L_ROUTE_COMPOSITE_KERNEL_IMPORTED=true
S_ROUTE_FULL_RADICAL_IMPORTED=true
S6_04_RESONANCE_AND_D2_MODULUS_IMPORTED=true
RADICAL_POOR_THRESHOLD_FOR_SQRT_SCALE=1/2
RADICAL_POOR_HYPOTENUSE_SECTOR_SQRT_SCALE_CONTROLLED=true
REQUIRED_POST_LOCAL_SAVING=10/21
CRITICAL_WITNESS_SCALE=10/21
RADICAL_RICH_LONG_WITNESS_COORDINATE_SAVING_REACHES_10_21=true
SMALL_DENOMINATOR_CRITICAL_THRESHOLD=10/21
EXACT_WITNESS_AUXILIARY_CHARACTER_RESONANCE=true
EXACT_WITNESS_AUXILIARY_CHARACTER_CANCELLATION_TARGET_VALID=false
DENOMINATOR_SQUARE_MODULUS_EXACT=true
DENOMINATOR_SQUARE_LINE_MULTIPLICITY_SUBPOLYNOMIAL=true
DENOMINATOR_SQUARE_RECTANGLE_BOUND_PROVED=true
LEAST_DENOMINATOR_PACKET_STATISTIC_DEFINED=true
UNIQUE_POST_LOCAL_QUANTITATIVE_GATE=RADICAL_RICH_LEAST_DENOMINATOR_PACKET_DISTRIBUTION
EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bk attack the radical-rich D_min distribution directly with the critical split D_min<B^(10/21) versus D_min>=B^(10/21), and prove the first packet-level post-local exponent if possible
```
