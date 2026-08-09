# Stage14-4bj — L/S reunification and least-denominator post-local gate

## Purpose

Stage14-4bi was temporarily split into two implementation lanes.

- `14-4bi-L` closed the large edge-kernel route by replacing a largest-prime modulus with the whole squarefree edge kernel and proving the large-kernel dichotomy
  `incidence saving OR small denominator`.
- `14-4bi-S` strengthened the usable modulus further to the full odd radical of each Pythagorean leg, proved the radical-poor hypotenuse family is globally sparse, and reduced every coordinate-level complement to small denominator.

Both lanes are now merged. Stage14-4bj terminates the temporary parallelization and returns the `14-4` main track to a single sequence.

The stage has four jobs:

1. combine the L/S ledgers without double counting;
2. freeze the exact critical thresholds forced by the current `41/42` local exponent;
3. remove an invalid candidate transfer mechanism: exact-witness auxiliary-character cancellation is resonant, not oscillatory;
4. replace the vague moving-packet correlation target by one packet-level statistic, the least denominator of a bounded-height global witness.

No positive full-family post-local exponent is claimed here.

---

## 1. Merged inputs

The current physical upper bound remains

\[
V(B)\ll_\epsilon B^{41/42+\epsilon}.
\]

The square-root target is `B^(1/2+epsilon)`, so the missing saving is exactly

\[
\boxed{
\frac{41}{42}-\frac12=\frac{10}{21}.
}
\tag{BJ.1}
\]

The global witness packet has

\[
d_0u_0^2-d_1u_1^2=S^2D^2,
\qquad
 d_2u_2^2-d_0u_0^2=X^2D^2,
\]

and hence

\[
\boxed{d_2u_2^2-d_1u_1^2=H^2D^2.}
\tag{BJ.2}
\]

The signed squarefree kernels satisfy the merged s6-01 factorization

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

Merged `14-4bi-S` additionally gives the full-radical congruences, in particular

\[
\tau_2b u_2^2\equiv \tau_1a u_1^2
\pmod{\operatorname{rad}_{odd}(H)}.
\tag{BJ.3}
\]

Thus neither `small selected kernel` nor `large-but-smooth kernel` is an intrinsic obstruction.

---

## 2. Exact reunified structural partition

Put

\[
R_H=\operatorname{rad}_{odd}(H).
\]

For any `rho,nu>0`, every supported witness belongs to one of three structural sectors.

### A. Radical-poor hypotenuse

\[
R_H\le B^\rho.
\]

Merged `14-4bi-S` proves, by the elementary radical Rankin bound plus the primitive Pythagorean representation multiplicity,

\[
\#\{\text{supported base/classes with }R_H\le B^\rho\}
\ll_\epsilon B^{\rho+\epsilon}.
\tag{BJ.4}
\]

This is already a genuine packet/base-count estimate, not a coordinate-density estimate.

### B. Radical-rich and long incident witness coordinate

\[
R_H>B^\rho,
\qquad
U_*=\max(|u_1|,|u_2|)\ge B^\nu.
\]

The full-radical CRT lattice bound gives, inside each fixed witness packet rectangle,

\[
N_H(U_1,U_2)
\ll_\epsilon
B^\epsilon
\left(
\frac{U_1U_2}{R_H}
+\min(U_1,U_2)+1
\right),
\]

hence the witness-coordinate layer has relative gain

\[
B^{-\min(\rho,\nu)+\epsilon}.
\tag{BJ.5}
\]

This remains a coordinate-layer theorem; it cannot be multiplied blindly by the unweighted `B^(41/42)` packet count.

### C. Short incident witness coordinate

If `R_H>B^rho` but `U_*<B^nu`, the exact H-edge equation and the kernel coefficient bounds give

\[
\boxed{D\le 2U_*<2B^\nu.}
\tag{BJ.6}
\]

Thus all coordinate-level complements transfer to small denominator.

The temporary L/S split is therefore completely recombined:

```text
radical-poor base/classes
OR
radical-rich coordinate-saved witnesses
OR
small denominator.
```

There is no fourth large-kernel, smooth-kernel, tiny-kernel, or short-variable remainder.

---

## 3. Critical threshold choice

The radical-poor estimate (BJ.4) allows the exact square-root threshold

\[
\boxed{\rho=\frac12.}
\tag{BJ.7}
\]

Indeed

\[
R_H\le B^{1/2}
\quad\Longrightarrow\quad
\#\text{base/classes}\ll B^{1/2+\epsilon}.
\]

Hence the only family still capable of exceeding square-root scale has

\[
\boxed{R_H>B^{1/2}.}
\tag{BJ.8}
\]

On this radical-rich family the missing saving from (BJ.1) is `10/21`. Therefore choose

\[
\boxed{\nu=\frac{10}{21}.}
\tag{BJ.9}
\]

If `U_*>=B^(10/21)`, then the coordinate-layer radical modulus gain satisfies

\[
\min\left(\frac12,\frac{10}{21}\right)=\frac{10}{21},
\]

which is exactly the full missing exponent budget.

If `U_*<B^(10/21)`, then

\[
\boxed{D<2B^{10/21}.}
\tag{BJ.10}
\]

Thus the current arithmetic/geometric machinery reaches the exact required power at coordinate level everywhere except the small-denominator branch.

This does **not** yet prove the square-root bound because of the packet-existence quantifier gap.

---

## 4. Exact-witness auxiliary-character resonance

Merged s6-03 introduced the three centered quartic projections

```text
Phi0(u0,D)=(k*u1*u2)^2,
Phi1(u1,D)=(k*u0*u2)^2,
Phi2(u2,D)=(k*u0*u1)^2
```

on every exact witness.

Therefore for every good auxiliary odd prime `lambda` not dividing the displayed nonzero square,

\[
\chi_\lambda(\Phi_i)=+1.
\]

Consequently, a proposed moving-packet sum which **retains the exact witness indicator** and hopes for cancellation from

\[
\chi_q(\Phi_i)
\]

is tautologically resonant on its support. Selecting one canonical exact witness per packet does not create oscillation: the selected value is still a square.

Hence

```text
EXACT_WITNESS_AUXILIARY_CHARACTER_CANCELLATION_TARGET_VALID=false.
```

The fixed-packet square-sieve theorem from s6-03 remains valid as a coordinate-density statement before conditioning on being an exact witness. What fails is only the attempted direct transfer to packet existence by reusing the same character on exact witness support.

This removes one misleading candidate for the next stage.

---

## 5. Denominator-square incidence

Equation (BJ.2) gives the exact congruence

\[
\boxed{
d_2u_2^2\equiv d_1u_1^2\pmod{D^2}.
}
\tag{BJ.11}
\]

From the primitive denominator representation `Z=A/D^2` with `gcd(A,D)=1`, every prime dividing `D` is coprime to each exact factor

```text
Gi=di*ui^2.
```

Thus the relevant coefficients and square variables are units modulo every prime power dividing `D`.

For an odd prime power `p^(2e)||D^2`, a unit quadratic congruence for the ratio `u2/u1` has at most two roots. The 2-adic factor contributes at most four roots. CRT therefore puts `(u1,u2)` into at most

\[
4\,2^{\omega(D_{odd})}=D^{o(1)}
\]

projective congruence lines modulo `D^2`.

Hence a dyadic rectangle satisfies

\[
\boxed{
N_D(U_1,U_2)
\ll_\epsilon
D^\epsilon
\left(
\frac{U_1U_2}{D^2}
+\min(U_1,U_2)+1
\right).
}
\tag{BJ.12}
\]

Together with `D<=2U_*`, a layer with `D>=B^eta` has at least

\[
B^{-\eta+\epsilon}
\]

relative coordinate saving. At the critical choice `eta=10/21`, the denominator-square modulus independently reaches the full missing coordinate exponent.

Again, this is not yet an unweighted packet-count theorem.

---

## 6. The packet-level statistic that survives all reductions

For a locally admissible supported packet `pi=(F,sigma)` and the fixed bounded-height window inherited from Stage14-s3, define

\[
D_{\min}(\pi;B)
=
\min\{D(Q): Q\text{ is an admissible bounded-height non-torsion global witness in }\pi\},
\]

with `D_min=+infinity` if no such witness exists.

The physical count is majorized by the number of packets with finite `D_min`.

After the L/S reunion, the only unresolved packet-level quantitative question is the distribution of this statistic on the radical-rich family

\[
R_H>B^{1/2}.
\]

The critical split is

```text
D_min <  B^(10/21)   : small-denominator packet sector,
D_min >= B^(10/21)   : large-denominator packet sector.
```

Coordinate incidence is strong enough in the second sector, but a theorem is still needed that converts the existence of one selected witness into a count of packets without paying uncontrolled coordinate volume.

The next theorem must therefore be formulated directly at packet level. A sufficient target is: prove some fixed `delta>0` in

\[
\#\{\pi:R_H>B^{1/2},\ D_{\min}(\pi;B)<\infty\}
\ll B^{41/42-\delta+\epsilon}.
\tag{BJ.13}
\]

Any `delta>0` is genuine post-local progress. The square-root upper-bound scale is reached once

\[
\boxed{\delta\ge\frac{10}{21}.}
\tag{BJ.14}
\]

A sharper two-tail version may estimate the `D_min<B^eta` and `D_min>=B^eta` sectors separately.

---

## 7. What is now closed and what remains open

Closed:

- the temporary L/S branch split;
- largest-prime dependence;
- large-but-smooth kernel obstruction;
- tiny selected-kernel obstruction;
- radical-poor hypotenuse family above square-root relevance;
- all coordinate-level short-variable complements;
- the idea that exact-witness auxiliary characters themselves can provide moving-family cancellation;
- exact denominator-square projective-line incidence.

Open:

- a packet-level distribution theorem for `D_min` / canonical global-witness occupancy on the radical-rich family;
- any positive full-family `delta_post`;
- the `B^(1/2+epsilon)` upper bound;
- a square-root asymptotic.

The next main-track stage should attack `D_min` directly rather than reopening L/S branches or another local-character sieve.

---

## Boundary flags

```text
STAGE14_4BJ=LS_REUNIFIED_AND_LEAST_DENOMINATOR_GATE_FROZEN
TEMPORARY_LS_PARALLELIZATION_CLOSED=true
L_ROUTE_COMPOSITE_KERNEL_IMPORTED=true
S_ROUTE_FULL_RADICAL_IMPORTED=true
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
NEXT=Stage14-4bk attack the radical-rich D_min distribution directly, with the critical split D_min<B^(10/21) versus D_min>=B^(10/21), and prove the first packet-level post-local exponent if possible
```
