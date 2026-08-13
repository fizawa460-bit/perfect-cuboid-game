# Stage14-tH15 — Shared-U bipartite squareclass-energy receiver

## Purpose

Merged Stage14-t54 proves that fixing the primitive Gaussian cofactor `U` does **not** reduce the live principal-incidence problem to a one-variable moving-canonical-prime sum.

The exact fixed-`U` skeleton is

\[
N(U)=m,
\qquad N(V)=n=k\delta,
\qquad k\mid \varepsilon m,
\qquad hk=\varepsilon m.
\tag{H15.1}
\]

After fixing `U` and the finite state `epsilon`, the divisor fan `(k,h)` has only `B^{o(1)}` possibilities, but `delta`, the primitive Gaussian cover cofactor `V`, and the canonical Gaussian prime `pi` all continue to move.

For one fixed-`U` physical fiber, let

\[
r_U(\kappa)
 =\#\{s:[\widetilde F_s]=\kappa\},
\qquad
R_U=\sum_\kappa r_U(\kappa),
\]

and

\[
E_U=\sum_\kappa r_U(\kappa)^2.
\tag{H15.2}
\]

The desired live theorem is

\[
\boxed{E_U\ll R_U B^{o(1)}}.
\tag{H15.3}
\]

Stage14-tH15 builds the exact non-circular receiver for (H15.3), proves every one-dimensional / non-transverse part that can legally be imported from t36/t38, writes the remaining two-dimensional trace explicitly in projective coordinates, and isolates the new theorem that Stage14-t55 must prove if no stronger existing theorem can be certified.

The merged t54 boundary

```text
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
```

is treated as an input guard.  No t54 power saving is assumed.

The prohibited operation remains prohibited:

```text
ordered state pair
  -> cross-kernel tau
  -> coefficient-energy E4
```

before the fixed-`U` bipartite cancellation.

---

## 1. Mandatory fixed-U packet

A legal tH15 packet retains

```text
fixed primitive U
fixed epsilon
k | epsilon*N(U)
h*k = epsilon*N(U)
moving canonical Gaussian prime pi
moving primitive Gaussian V
N(V)=k*delta
delta
visible/invisible branch
visible orientation
interval selector
reconstruction conditions
canonical-prime selector
sharp hyperbola/divisor coupling
common-refinement sign/weight
```

The divisor fan `(k,h)` may be refined because

\[
\#\{k:k\mid\varepsilon m\}=B^{o(1)}.
\tag{H15.4}
\]

The branch/orientation split is finite.  These refinements cost only `B^{o(1)}`.

By contrast, `delta`, `V`, and `pi` must **not** be frozen cell-by-cell and then recombined by Cauchy.  They are the live bipartite variables.

Thus the canonical tH15 state is

\[
s=(U,\varepsilon,k,h;\pi,V,\delta;\mathfrak b,\mathfrak m),
\tag{H15.5}
\]

where `mathfrak b` is the finite branch/orientation datum and `mathfrak m` contains the physical masks and common-refinement provenance.

---

## 2. Cauchy-free principal-energy partition

Inside one fixed-`U` packet, view the physical states as edges of a bipartite graph

```text
left vertex  = canonical Gaussian prime/orientation pi
right vertex = primitive descended cover packet V (including delta when needed)
edge color   = squareclass [Ftilde(pi,V)]
```

The ordered equal-squareclass pairs counted by `E_U` split disjointly into

1. exact state diagonal;
2. same-`pi`, distinct-`V` collisions;
3. same-`V`, distinct-`pi` collisions;
4. transverse collisions with both `pi!=pi'` and `V!=V'`.

Write these contributions as

\[
E_U
=R_U+I_U^{(\pi)}+I_U^{(V)}+I_U^{\rm tr}.
\tag{H15.6}
\]

No Cauchy inequality has been used in (H15.6).  In particular there is no factor equal to the number of `delta`, common-core, or canonical-prime cells.

### Same-pi slice

For fixed `pi`, the actual direction Gaussian integer `A_c=pi U` is fixed.  The t36 fixed-direction squareclass-collision theorem gives

\[
I_U^{(\pi)}\ll R_U B^{o(1)}
\tag{H15.7}
\]

after summing the disjoint fixed-`pi` fibers.

### Same-V slice

For fixed descended `V` and fixed finite branch data, t38 gives a smooth genus-one moving-`pi` quartic with bounded-height multiplicity `B^{o(1)}`.  Applying the same collision twist to a fixed target state gives

\[
I_U^{(V)}\ll R_U B^{o(1)}.
\tag{H15.8}
\]

Hence

\[
\boxed{
E_U\ll R_U B^{o(1)}+I_U^{\rm tr}.
}
\tag{H15.9}
\]

This is the first proved tH15 receiver.  It makes the Latin-square obstruction exact: **only the genuinely bipartite transverse principal incidence remains.**

The t54 Latin-square model has `I_tr` of polynomial size even when both (H15.7) and (H15.8) are optimal, so no row/column shortcut is permitted.

---

## 3. Projective reduction of the t38 factorization

The squareclass is invariant under rational rescaling of `pi` and `V`, because all relevant formulas are even in the rational scales.

Write

\[
U=a+ib,
\qquad
\pi=s(x+i),
\qquad
V=q(y+i),
\tag{H15.10}
\]

with rational projective slopes

\[
x=\frac{\Re\pi}{\Im\pi},
\qquad
y=\frac{\Re V}{\Im V}.
\]

All factors `s^4 q^4` are rational squares and disappear in the squareclass.  Therefore each fixed-`U` branch has an exact bivariate projective squareclass polynomial.

Define

\[
A_+(y)=ay+b,\qquad B_+(y)=by-a,
\]

\[
A_-(y)=ay-b,\qquad B_-(y)=by+a,
\tag{H15.11}
\]

and

\[
L(A,B;x)=(Ax-B)(Bx+A).
\tag{H15.12}
\]

### Invisible branch

Merged t38 gives

\[
F=-\Psi_{U\bar V}(\pi)\Psi_{UV}(\pi).
\]

After removing the square scale `s^4q^4`, the exact projective trace is

\[
\boxed{
P_U^{\rm inv}(x,y)
=-L(A_+(y),B_+(y);x)
 L(A_-(y),B_-(y);x).
}
\tag{H15.13}
\]

Equivalently it factors into four explicit bilinear forms in `(x,y)`.

### Visible same orientation

Merged t38 gives

\[
F/\ell^2
=-\Psi(U\bar V)\Phi_{UV}(\pi).
\]

Thus

\[
\boxed{
\begin{aligned}
P_U^{\rm vis,+}(x,y)
={}&-A_+(y)B_+(y)\\
&\times\bigl(A_-(y)(x^2-1)-2B_-(y)x\bigr)\\
&\times\bigl(B_-(y)(x^2-1)+2A_-(y)x\bigr).
\end{aligned}
}
\tag{H15.14}
\]

### Visible opposite orientation

The opposite branch interchanges `U\bar V` and `UV`:

\[
\boxed{
\begin{aligned}
P_U^{\rm vis,-}(x,y)
={}&-A_-(y)B_-(y)\\
&\times\bigl(A_+(y)(x^2-1)-2B_+(y)x\bigr)\\
&\times\bigl(B_+(y)(x^2-1)+2A_+(y)x\bigr).
\end{aligned}
}
\tag{H15.15}
\]

All three projective traces have bidegree at most `(4,4)` and are exact identities, not asymptotic models.

The tH15 deterministic audit checks (H15.13)--(H15.15) against direct Gaussian multiplication on integer samples.

---

## 4. Geometry: why the two one-variable elliptic theorems do not globalize

For a fixed rational squareclass `kappa`, the projective principal fiber has the form

\[
Z^2=\kappa P_U^{\mathfrak b}(x,y).
\tag{H15.16}
\]

The branch divisor has total class `(4,4)` on

\[
\mathbf P^1_x\times\mathbf P^1_y.
\]

Consequently, after the usual smoothness / reduced-branch certification, (H15.16) is a **K3-type double-cover surface**.  Its two natural projections are genus-one fibrations; these are precisely the one-variable t36/t38 slices.

This explains the t54 Latin-square obstruction geometrically:

- t36 controls rational points along one elliptic fibration;
- t38 controls rational points along the other;
- neither theorem bounds the total rational-point incidence on the two-dimensional surface.

No uniform `B^{o(1)}` rational-point theorem for the physical subset of (H15.16) is imported here.

The K3 label is used as a theorem-shape diagnostic, not as a claim that every physical specialization has already passed a smooth minimal-resolution classification.  Exceptional reducible/singular parameter loci must be routed separately if a future geometric proof uses this route.

---

## 5. Exact transverse external-prime Frobenius receiver

The non-circular way to attack `I_U^tr` is to retain the physical state sum and average auxiliary characters **before** any cross-kernel collapse.

Let `Pcal` be a family of odd split auxiliary primes, and for a physical state `s` define

\[
c_s(p)=\chi_p(\widetilde F_s),
\]

with the t50 bad-prime mask retained.  Put

\[
b_s=\#\{p\in\mathcal P:p\mid\widetilde F_s\},
\qquad b=\max_s b_s=B^{o(1)}.
\tag{H15.17}
\]

For two states write

\[
\langle c_s,c_t\rangle
=\sum_{p\in\mathcal P}c_s(p)c_t(p).
\]

Define the **transverse Frobenius energy**

\[
\boxed{
\mathfrak F_U^{\rm tr}
=\sum_{\substack{s,t\in S_U\\
\pi_s\ne\pi_t\\V_s\ne V_t}}
|\langle c_s,c_t\rangle|^2.
}
\tag{H15.18}
\]

This is nonnegative and does not aggregate ordered pairs by a cross-kernel.

If `[Ftilde_s]=[Ftilde_t]`, then on every auxiliary prime good for both states

\[
c_s(p)c_t(p)=1.
\]

Hence each transverse principal pair contributes at least `(P-2b)^2`, where `P=#Pcal`, and therefore

\[
\boxed{
I_U^{\rm tr}(P-2b)^2
\le \mathfrak F_U^{\rm tr}.
}
\tag{H15.19}
\]

This is the exact positive receiver required by t55.

### Matrix form without pair-kernel collapse

For one auxiliary pair `(p,q)` define the full fixed-`U` trace

\[
G_U(p,q)=\sum_{s\in S_U}c_s(p)c_s(q).
\tag{H15.20}
\]

For each left vertex `pi` and right vertex `V`, define

\[
G_{U,\pi}(p,q)=\sum_{s:\pi_s=\pi}c_s(p)c_s(q),
\]

\[
G_{U,V}(p,q)=\sum_{s:V_s=V}c_s(p)c_s(q),
\]

and

\[
D_U(p,q)=\sum_{s\in S_U}c_s(p)^2c_s(q)^2.
\]

Exact inclusion-exclusion gives

\[
\boxed{
\mathfrak F_U^{\rm tr}
=\sum_{p,q\in\mathcal P}
\left(
G_U(p,q)^2
-\sum_\pi G_{U,\pi}(p,q)^2
-\sum_V G_{U,V}(p,q)^2
+D_U(p,q)
\right).
}
\tag{H15.21}
\]

Equation (H15.21) is an identity.  The expression inside parentheses need not be positive modulus-by-modulus; positivity exists only after the pair-space interpretation (H15.18).

This is why absolute-valuing each `pi`, `V`, `delta`, or common-core cell before global aggregation is forbidden.

---

## 6. The sufficient genuinely bipartite theorem

Combining (H15.9) and (H15.19), a sufficient theorem for Stage14-t55 is now exact.

### SharedUPhysicalBipartiteDispersion (SUBD)

For every fixed primitive `U`, finite `epsilon`, and legal `B^{o(1)}` divisor-fan/branch refinement, let `S_U` be the full physical set retaining `delta`, primitive `V`, canonical `pi`, interval/reconstruction masks and the hyperbola cutoff.

Let `Pcal` be a split auxiliary-prime family with

\[
b=o(P).
\tag{H15.22}
\]

The required estimate is

\[
\boxed{
\mathfrak F_U^{\rm tr}
\ll P^2 R_U B^{o(1)}.
}
\tag{H15.23}
\]

Then (H15.19) gives

\[
I_U^{\rm tr}\ll R_U B^{o(1)},
\]

and (H15.9) gives

\[
\boxed{E_U\ll R_U B^{o(1)}}.
\tag{H15.24}
\]

No `E4` coefficient appears anywhere in this implication.

For an uncentered/random-character proof strategy, the natural nonprincipal baseline of (H15.18) is roughly `R_U^2 P`; therefore the scale

\[
P\ge R_U B^{-o(1)}
\tag{H15.25}
\]

is the natural amplifier regime unless a future argument subtracts and controls that baseline in a genuinely signed way.  This is the fixed-`U` analogue of the t49 amplifier condition.

---

## 7. t38 factorization inside the auxiliary trace

For one external squarefree split modulus

\[
M=pq,
\]

the fixed-`U` physical trace in (H15.20) is exactly

\[
G_U(p,q)
=\sum_{(\pi,V)\in S_U}
\chi_M\bigl(P_U^{\mathfrak b}(x_\pi,y_V)\bigr),
\tag{H15.26}
\]

with (H15.13)--(H15.15) chosen by branch.

The important structural facts are:

1. both variables are retained;
2. the character modulus is shared by `pi` and `V`;
3. the physical coefficient is the actual bipartite incidence selector, not an arbitrary Cartesian product;
4. `delta` remains encoded through `N(V)=k delta` and the sharp `ell*m*delta` hyperbola;
5. canonical and reconstruction masks remain inside the sum.

On complete split norm circles t32 changes angular variables to ratio/product coordinates and obtains exact one-variable factorization plus square-root complete cancellation.  That local completion may be inserted **before** any state-pair collapse.

However, the physical set in (H15.26) is a sparse integral subset of the complete torus.  As t50/tH14 already record, complete finite-field cancellation does not automatically imply cancellation on this selector.

Thus t32 supplies the local trace geometry required by SUBD, but does not by itself prove (H15.23).

---

## 8. Gaussian reciprocity / Hecke routes: exact applicability audit

Three standard analytic routes were checked against the fixed-`U` object.

### 8.1 Friedlander--Iwaniec Gaussian Dirichlet-symbol bilinear form

The classical FI kernel is a separated Gaussian Dirichlet symbol

\[
\left(\frac zw\right)
\]

with coefficients factored between the two variables.  Merged t39 already proves that for the Stage14 `Psi/Phi` trace:

- using the natural moving Gaussian modulus makes the trace constant or zero on good states;
- keeping an external auxiliary modulus preserves a nontrivial trace but destroys multiplicativity;
- the modulus-dependent coordinate rotation needed to identify a FI symbol destroys coefficient separation.

Fixing `U` does not remove the moving `V` from (H15.13)--(H15.15).  Therefore no new exact identity

\[
\chi_M(P_U(x_\pi,y_V))
=\alpha_\pi\beta_V\left(\frac V\pi\right)
\]

has been proved.

```text
DIRECT_FI_GAUSSIAN_DIRICHLET_SYMBOL_TRANSFER_VALID=false
```

### 8.2 Quadratic Hecke / quadratic large sieve after squareclass collapse

One may always collapse states by `[Ftilde]` and apply a quadratic large sieve to the resulting character family.  But its coefficient energy is exactly

\[
\sum_\kappa r_U(\kappa)^2=E_U,
\]

the quantity being proved.

Hence this route is circular for tH15.

```text
QUADRATIC_LARGE_SIEVE_AFTER_SQUARECLASS_COLLAPSE_NONCIRCULAR=false
```

### 8.3 Finite-field arbitrary-set trace bilinear theorems

Modern arbitrary-set bilinear trace estimates work for certified one-field trace-sheaf kernels under quantitative support/energy hypotheses.  The physical tH15 object instead has:

- a bivariate `(4,4)` trace rather than a certified `K(xy)` kernel;
- two external primes in the square-sieve/Frobenius receiver;
- a divisor-coupled integral hyperbola rather than arbitrary independent finite-field supports;
- canonical/interval/reconstruction masks that need a uniform transfer theorem.

No existing theorem is imported until those hypotheses are mapped exactly.

```text
KNOWN_ARBITRARY_SET_TRACE_THEOREM_DIRECTLY_CERTIFIED=false
```

The literature remains useful orientation, not a proof of SUBD.

---

## 9. Strong impossibility guards

### Guard A — Latin square

A bipartite `N x N` array can have each color once per row and once per column while each color occurs `N` times globally.  Then

\[
R=N^2,
\qquad
E=N^3.
\]

Thus optimal t36/t38 row/column multiplicity alone misses the target by `N`.

### Guard B — arbitrary physical-looking selector

Even with the explicit trace polynomial, an arbitrary selector can choose only points carrying one squareclass.  Then

\[
E_U=R_U^2.
\]

SUBD must therefore use the actual arithmetic selector; it cannot be stated for arbitrary bipartite masks.

### Guard C — cellwise Cauchy

Fixing each `delta`, common-core, or `(k,delta)` cell, applying a local bound, and finally Cauchy-summing the cells can introduce the number of cells as a polynomial loss.  Only the divisor fan `(k,h)` and finite branch states are known a priori to be `B^{o(1)}` refinements.

### Guard D — pair-to-tau precollapse

Expanding pair identities is legal.  Replacing the ordered pair family first by coefficients indexed by

\[
\tau=\operatorname{sqf}(\widetilde F_s\widetilde F_t)
\]

and then applying a coefficient-energy theorem is forbidden because the coefficient energy returns the unresolved fourth energy.

### Guard E — K3 slice theorem is not a global theorem

Uniform `B^{o(1)}` bounds on every fixed-`x` or fixed-`y` genus-one fiber do not imply a `B^{o(1)}` bound on the total `(4,4)` double-cover incidence.

---

## 10. Critical sqrt-ell exponent ledger

On the critical strip

\[
\ell=B^{1/2+o(1)}.
\tag{H15.27}
\]

From the physical scale

\[
\varepsilon\ell m\delta/2\le B
\]

we obtain

\[
m\delta\le B^{1/2+o(1)}.
\tag{H15.28}
\]

Write

\[
m=B^{u+o(1)}.
\]

Then

\[
\delta\le B^{1/2-u+o(1)},
\qquad
N(V)=k\delta\le B^{1/2+o(1)},
\tag{H15.29}
\]

because `k<=epsilon*m`.

Therefore both moving Gaussian coordinates have the balanced critical height

\[
|\pi|=B^{1/4+o(1)},
\qquad
|V|\le B^{1/4+o(1)}.
\tag{H15.30}
\]

This is the geometric reason the endpoint is genuinely bipartite.

Let

\[
R_U=B^{r+o(1)},
\qquad P=B^{\rho+o(1)}.
\]

The desired energy exponent is `r` while the trivial energy exponent is `2r`.

The positive Frobenius receiver (H15.19) plus SUBD loses no fixed power:

\[
\operatorname{exp}(I_U^{tr})\le r.
\]

For the uncentered natural-scale strategy, (H15.25) becomes

\[
\boxed{\rho\ge r.}
\tag{H15.31}
\]

Any theorem of the weaker shape

\[
\mathfrak F_U^{tr}
\ll P^2R_U B^{\omega+o(1)}
\]

gives

\[
E_U\ll R_U B^{\omega+o(1)}.
\]

Thus the fixed-power target requires

\[
\boxed{\omega=0.}
\tag{H15.32}
\]

No positive fixed loss may be hidden in `B^{o(1)}`.

---

## 11. What is proved and what remains

### Proved in tH15

1. exact Cauchy-free partition (H15.6);
2. same-`pi` slice routed to t36;
3. same-`V` slice routed to t38;
4. reduction (H15.9) to transverse bipartite principal incidence;
5. exact projective bivariate formulas (H15.13)--(H15.15);
6. `(4,4)` / K3-type theorem-shape identification;
7. positive transverse Frobenius receiver (H15.19);
8. exact matrix inclusion-exclusion identity (H15.21);
9. exact sufficient theorem contract SUBD (H15.23);
10. critical exponent and coordinate-height ledger.

### Not proved

1. SUBD itself;
2. a direct FI Gaussian-symbol reduction;
3. a non-circular Hecke large-sieve proof;
4. a physical K3 rational-point bound;
5. the full SharedUBipartiteSquareclassEnergy theorem;
6. the global principal/fourth-energy or critical-strip power saving.

The residual is therefore **strictly smaller** than t54's original problem: all row, column, diagonal and divisor-fan losses are removed; only transverse two-dimensional physical character dispersion remains.

---

## 12. Direct handoff contract for Stage14-t55

Stage14-t55 may import the following record.

```text
SharedUBipartiteSquareclassEnergy:
  fixed:
    primitive_U = true
    epsilon = true
    divisor_fan_(k,h) = B^o(1)

  live_variables:
    canonical_Gaussian_prime_pi = moving
    primitive_Gaussian_V = moving
    delta = moving

  physical_constraints:
    N(V)=k*delta
    k|epsilon*N(U)
    interval_selector = retained
    reconstruction = retained
    branch_orientation = retained
    hyperbola = retained
    canonical_selector = retained

  energy_partition:
    E_U = R_U + I_same_pi + I_same_V + I_transverse
    I_same_pi <= R_U*B^o(1)       # t36
    I_same_V  <= R_U*B^o(1)       # t38

  projective_trace:
    invisible = H15.13
    visible_same = H15.14
    visible_opposite = H15.15
    bidegree <= (4,4)

  transverse_receiver:
    I_transverse*(P-2b)^2 <= Frob_transverse
    required_SUBD:
      Frob_transverse <= P^2*R_U*B^o(1)

  forbidden:
    row_column_bounds_imply_global = false
    freeze_delta_then_power_Cauchy = false
    pair_to_tau_before_cancellation = false
    E4_as_coefficient_energy = false
    complete_trace_implies_sparse_selector = false

  status:
    SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED = false
    MINIMAL_REMAINING_OBSTRUCTION = SharedUPhysicalBipartiteDispersion
```

If Stage14-t55 proves SUBD uniformly on the critical fixed-`U` family, then (H15.24) immediately closes the requested fixed-`U` energy theorem with no new roadworks stage.

---

## Literature orientation

No external result is promoted to a Stage14 proof input here.

- Friedlander--Iwaniec, *The polynomial X^2+Y^4 captures its primes*: Gaussian spin / Dirichlet-symbol bilinear machinery; merged t39 records the exact separation failure for the raw Stage14 trace.
- Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*: valid quadratic Hecke-family large sieve, but collapsing tH15 states by squareclass feeds the unknown `E_U` back as coefficient energy.
- Ping Xi, *Bilinear forms with trace functions over arbitrary sets, and applications to Sato--Tate*: demonstrates genuinely two-variable arbitrary-support trace technology over one finite field under sheaf/support hypotheses, but no direct certificate for the present `(4,4)` two-prime divisor-coupled Gaussian selector.
- Cameron Wilson, *General Bilinear Forms In The Jacobi Symbol Over Hyperbolic Regions*: shows that hyperbolic support can coexist with Jacobi-symbol cancellation once the kernel is genuinely a Jacobi symbol; tH15 has no exact reduction of (H15.13)--(H15.15) to that kernel.

---

## Proof boundary

```text
STAGE14_TH15=COMPLETE_SHARED_U_BIPARTITE_RECEIVER_AND_TRANSVERSE_DISPERSION_BOUNDARY
MERGED_T54_IMPORTED=true
FIXED_U_DIVISOR_FAN_PRESERVED=true
MOVING_PI_PRESERVED=true
MOVING_PRIMITIVE_V_PRESERVED=true
DELTA_PRESERVED=true
INTERVAL_RECONSTRUCTION_BRANCH_MASKS_PRESERVED=true
HYPERBOLA_DIVISOR_COUPLING_PRESERVED=true
ONE_VARIABLE_FIBER_BOUNDS_GLOBALIZE=false
CAUCHY_FREE_ROW_COLUMN_TRANSVERSE_PARTITION_PROVED=true
SAME_PI_PRINCIPAL_ENERGY_NEAR_LINEAR=true
SAME_V_PRINCIPAL_ENERGY_NEAR_LINEAR=true
T38_PROJECTIVE_BIPARTITE_FACTORIZATION_PROVED=true
PROJECTIVE_TRACE_BIDEGREE_AT_MOST_4_4=true
K3_TYPE_DOUBLE_COVER_THEOREM_SHAPE_IDENTIFIED=true
TRANSVERSE_POSITIVE_FROBENIUS_RECEIVER_PROVED=true
TRANSVERSE_MATRIX_INCLUSION_EXCLUSION_IDENTITY_PROVED=true
SHARED_U_PHYSICAL_BIPARTITE_DISPERSION_DEFINED=true
SHARED_U_PHYSICAL_BIPARTITE_DISPERSION_PROVED=false
DIRECT_FI_GAUSSIAN_DIRICHLET_SYMBOL_TRANSFER_VALID=false
QUADRATIC_LARGE_SIEVE_AFTER_SQUARECLASS_COLLAPSE_NONCIRCULAR=false
KNOWN_ARBITRARY_SET_TRACE_THEOREM_DIRECTLY_CERTIFIED=false
PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED=false
E4_COEFFICIENT_ENERGY_USED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
MINIMAL_REMAINING_OBSTRUCTION=SharedUPhysicalBipartiteDispersion
NEXT=Stage14-t55 prove SUBD on the physical fixed-U (pi,V,delta) family, or certify a theorem import after exact kernel/sheaf/support mapping
```
