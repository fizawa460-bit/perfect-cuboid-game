# Stage14-4bd — close the root-sawtooth handoff band and freeze the reciprocal exponent

## Result

Merged Stage14-4bc reduced the complete nonconstant local problem to the explicit linear--`E` root-sawtooth kernel on

```text
W_{1/200}={ (alpha,beta): R_E(alpha,beta)>-1/200 }.
```

Stage14-4bd closes that remaining handoff band.

The proof has two ingredients.

1. **Exact E-Walsh complementary-side normalization.**  For fixed odd `E` squareclass kernel `e`, the Walsh divisor `v|e` can be replaced by its complement `w=e/v`.  The multiplier `(d1/e)` introduced by this replacement is a product of fixed one-variable mod-8 characters, because every odd prime of `e` is `1 mod 4` and the divisor-level whole-`E` identities are

```text
q|m       => (q/e)=1,
q|n       => (q/e)=1,
q|m-n     => (q/e)=(2/q),
q|m+n     => (q/e)=(2/q).
```

Hence the analytic `E` subset modulus may always be chosen on the small side

```text
v <= sqrt(e) <= sqrt(E) << M.
```

Thus throughout the remaining handoff band we may assume `beta<=1`.

2. **Squarefree mixed Burgess on the long linear modulus.**  Once `beta<=1`, the 4bc exponent atlas itself forces

```text
alpha > 99/200.
```

The sawtooth Fourier modes are linear additive twists in `u`.  After the already-closed K4 graph escape is removed, every residual reciprocal twist incident to `u` has product conductor at most `M^(3/100)`.  The combined quadratic character therefore has squarefree conductor

```text
Q <= V M^(3/100).
```

Specializing Bryce Kerr's squarefree mixed-character theorem (arXiv:1410.3587, Theorem 1) to degree `d=1` and moment parameter `r=3` gives, for a primitive quadratic character modulo squarefree `Q`,

```text
sum_{n in J} chi_Q(n) exp(2*pi*i(theta*n))
 << Q^epsilon |J|^(2/3) Q^(2/15)
```

whenever `|J|<=Q^(3/5)`.  For longer intervals ordinary completion gives `Q^(1/2+epsilon)`.

After inserting the squarefree state condition by

```text
mu^2(n)=sum_{d^2|n} mu(d),
```

and allowing an arbitrary coprime auxiliary progression of modulus `A`, one obtains the uniform mixed squarefree progression estimate

```text
S(T;A,Q)
 << M^epsilon [
      (T/A)^(2/3) Q^(2/15)
      + (T/A)^(1/2) Q^(1/5)
    ].
```

The progression only helps.  Finite mod-8 classes and fixed root/sign cases cost `M^o(1)`.

At the worst point of the normalized handoff band,

```text
alpha=99/200,
beta=1,
log_M Q <= 1+3/100=103/100.
```

The two relative saving margins are exactly

```text
alpha/3 - (2/15)*(103/100) = 83/3000,
alpha/2 - (1/5)*(103/100)  = 83/2000.
```

Both are strictly larger than `1/100`.  Therefore, uniformly on the whole normalized handoff band,

```text
squarefree mixed u-sum
 << U M^(-1/100+o(1)).
```

Vaaler/Fourier expansion of the sawtooth costs only `M^o(1)` because the mixed estimate is uniform in the linear additive frequency.  Summing the quotient variable `a` (`|I_u|~M/U`), split moduli `v~V<=M`, signed roots, Mobius copies, and auxiliary Hilbert coordinates gives

```text
R(U,V)
 << M V M^(-1/100+o(1))
 << M^(2-1/100+o(1)).
```

Thus

```text
ROOT_SAWTOOTH_HANDOFF_BAND_CLOSED=true
ROOT_SAWTOOTH_SAVING_EXPONENT=1/100.
```

Outside the handoff band Stage14-4bc already gives `M^(-1/200)` from the signed-root lattice `L^2` theorem.  Consequently the complete nonconstant reciprocal error now satisfies

```text
E_rec(M) << M^(2-1/200+o(1)).
```

Since the Stage14 physical height scale has `B~M^2`, equivalently

```text
E_rec(B) << B^(399/400+o(1)).
```

This is the first unconditional positive exponent for the **complete nonconstant local reciprocal contribution**.

The diagonal/local-density term `D_loc` is still separate.  Stage14-4bd therefore does **not** set `rho_loc=M^(-1/200)` and does not yet claim a complete local retainer inequality.

---

## 1. Imported 4bc endpoint

Stage14-4bc proved

```text
S_W <= D_loc + E_rec,
```

with all nonconstant modes outside `W_{1/200}` already bounded by

```text
M^(2-1/200+o(1)).
```

Inside the band the only unresolved term was the exact sawtooth kernel

```text
R(U,V)
 = sum_{v~V,split}
   sum_{r^2=-1 mod v}
   sum_{u~U}^*
   (u/v)
   sum_{a in I_u}
   b_{u,v,r,a}
   psi((A_r*u*a+B)/v).
```

The `b` notation is an envelope for already-structured local coefficients, not an arbitrary adversarial matrix.  The only `u`-dependent unit-modulus factors are Jacobi/mod-8 characters coming from reciprocal edges; auxiliary incidence constraints are coprime progressions handled by s5p.

---

## 2. Exact E-Walsh complement switch

From s5q,

```text
I_E(d1;e)=2^(-omega(e)) sum_{v|e} (d1/v).
```

For `w=e/v`, squarefreeness and `gcd(d1,e)=1` give

```text
(d1/v)=(d1/e)(d1/w).
```

The Walsh weight is symmetric under `v<->w`, so the Fourier expansion may be analytically oriented toward the smaller of `v,w`; the larger complementary `E` piece is retained as an auxiliary signed-root/incidence coordinate, for which s5p is uniform.

To control `(d1/e)`, decompose `d1` into odd state pieces lying in the four linear Euclid columns.  No `E` prime occurs in `d1`: selected `H=E` primes have label `23=(0,1,1)`, and unselected `H` primes lie in none of `d1,d2,d3`.

For every odd divisor `q` of a linear column the congruence `E=e*t^2` gives the divisor-level identities

```text
q|m or q|n       => (q/e)=1,
q|m-n or q|m+n   => (q/e)=(2/q).
```

Quadratic reciprocity has no sign because every prime of `e` is `1 mod 4`.  Therefore `(d1/e)` contains no moving `E` conductor; it is a product of one-variable mod-8 factors and is absorbed into the already-bounded coefficient Hilbert space.

Hence

```text
E_WALSH_SMALL_SIDE_ORIENTATION_EXACT=true,
E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true.
```

On a regular box `E<<M^2`, so the active modulus has `V<<M` and therefore `beta<=1` at exponent level.

---

## 3. Handoff band forces a long linear variable

For `beta<=1`,

```text
kappa=max(beta/2,min(alpha,beta))
```

satisfies `kappa>=beta/2` and `kappa<=1`.  Thus

```text
R_E(alpha,beta)
 = alpha+beta+1-kappa-2
 <= alpha+beta/2-1
 <= alpha-1/2.
```

If `R_E>-1/200`, then necessarily

```text
alpha>1/2-1/200=99/200.
```

So every still-unresolved normalized sawtooth block has

```text
U > M^(99/200).
```

This is far above the Burgess `Q^(1/4+delta)` transition for the conductors below.

---

## 4. Residual reciprocal conductor at u

Use the s5o graph threshold

```text
eta=1/100.
```

If a second long-long linear reciprocal edge exists, that monomial is already bounded by the closed K4 quadratic-large-sieve escape with saving `1/200`; it does not enter the 4bd sawtooth remainder.

Therefore, in the remainder, every reciprocal neighbor of the very-long `u` vertex has state size `<M^eta`.  A K4 linear vertex has degree at most three, so the product of all remaining odd reciprocal conductors incident to `u` is

```text
q0 <= M^(3 eta)=M^(3/100).
```

Multiplying those Jacobi factors with `(u/v)` yields one primitive quadratic character on the coprime squarefree conductor

```text
Q=v*q0,
Q <= M^(beta+3/100).
```

Finite mod-4/mod-8 factors are handled by residue-class splitting.

---

## 5. Squarefree mixed Burgess in a coprime progression

Let `chi_Q` be the quadratic character on the odd squarefree conductor `Q`, `(A,Q)=1`, and let `J` be an interval of physical length `T`.  For one residue class `n=c (mod A)` define

```text
S=sum mu^2(n) chi_Q(n) exp(2*pi*i theta n).
```

Expand `mu^2` by square divisors.  If `(d,A)>1` there is no compatible solution in a primitive residue class; if `(d,Q)>1` the character contribution vanishes.  Otherwise CRT writes the surviving terms as one interval in a new integer variable of length

```text
N_d << T/(A d^2)+1,
```

and the character becomes `chi_Q(linear variable)` with invertible leading coefficient.  Translation/scaling modulo `Q` reduces this to the standard mixed interval form, while the additive phase remains linear.

For `N_d<=Q^(3/5)`, Kerr Theorem 1 with `d=1,r=3` gives

```text
N_d^(2/3) Q^(2/15+o(1)).
```

For `N_d>Q^(3/5)`, completion of the primitive character times a linear additive character gives

```text
Q^(1/2+o(1)).
```

Summing the square-divisor variable gives

```text
S
 << M^epsilon [
      (T/A)^(2/3) Q^(2/15)
      + (T/A)^(1/2) Q^(1/5)
    ].
```

The exponents come from

```text
sum d^(-4/3)<infinity
```

for the Kerr range and at most

```text
sqrt((T/A)/Q^(3/5))
```

square divisors in the completion range.

---

## 6. Exact exponent margin

Put `T=U=M^alpha`.  The worst normalized handoff values are

```text
alpha=99/200,
beta=1,
gamma=log_M Q <= 103/100.
```

For the Kerr term the relative saving is

```text
delta_1
 = alpha/3-(2/15)gamma
 >= 83/3000
 > 1/100.
```

For the completion term,

```text
delta_2
 = alpha/2-(1/5)gamma
 >= 83/2000
 > 1/100.
```

Any smaller `beta`, larger `alpha`, or nontrivial auxiliary progression only improves these inequalities.

Thus the uniform conservative contract is

```text
DELTA_SAW=1/100.
```

---

## 7. Sawtooth Fourier summation

Use a Vaaler finite Fourier approximation to

```text
psi(t)={t}-1/2.
```

Choose a polynomial truncation height.  Its Fourier coefficient `ell^1` norm is logarithmic and the positive approximation error contributes a negative power after choosing the height sufficiently large.  The mixed Burgess estimate above is uniform in the real linear phase, so every nonzero Fourier mode receives the same `M^(-1/100+o(1))` saving.

The signed-root multiplicity is `2^omega(v)=M^o(1)`, and Mobius/auxiliary state multiplicities are `M^o(1)` by s5p.  Summing `a` costs `M/U` and summing `v~V` costs at most `V`.  Hence

```text
R(U,V)
 << (M/U)*V*U*M^(-1/100+o(1))
 = M V M^(-1/100+o(1))
 <= M^(2-1/100+o(1)).
```

This closes all of `W_{1/200}`.

---

## 8. Complete reciprocal exponent

Combine

```text
outside W_{1/200}: delta >= 1/200   (4bc),
inside  W_{1/200}: delta >= 1/100   (4bd).
```

Therefore

```text
E_rec(M) << M^(2-1/200+o(1)).
```

Equivalently, because `B~M^2`,

```text
E_rec(B) << B^(399/400+o(1)).
```

The nonconstant local character modes are now fully power-saving.

What remains on the local side is not another reciprocal-character estimate.  It is the diagonal/local-density assignment

```text
D_loc <= rho_loc A_W + E_diag.
```

Only after that calculation may the complete local retainer `rho_loc` be stated.

---

## External analytic input

The new external input used at this stage is:

- Bryce Kerr, *Some mixed character sums*, arXiv:1410.3587, Theorem 1.  We use the squarefree-modulus theorem with polynomial degree `d=1`, `D=d(d+1)/2=1`, and `r=3`, which specializes to `N^(2/3)Q^(2/15+o(1))` for `N<=Q^(3/5)`.

No Gaussian/Hecke large sieve is needed for the 4bd closure.

---

## Boundary

```text
STAGE14_4BD=ROOT_SAWTOOTH_HANDOFF_CLOSED_AND_COMPLETE_RECIPROCAL_EXPONENT_FROZEN
E_WALSH_SMALL_SIDE_ORIENTATION_EXACT=true
E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true
WHOLE_E_COMPLEMENT_FACTOR_ONE_VARIABLE=true
NORMALIZED_HANDOFF_BETA_LE_1=true
HANDOFF_FORCES_ALPHA_GT_99_OVER_200=true
RESIDUAL_U_CHARACTER_CONDUCTOR_EXPONENT_LE_BETA_PLUS_3_OVER_100=true
KERR_SQUAREFREE_MIXED_THEOREM_IMPORTED=true
KERR_D1_R3_SPECIALIZATION=N^(2/3)*Q^(2/15+o(1))
SQUAREFREE_MIXED_AP_BOUND_PROVED=true
ROOT_SAWTOOTH_HANDOFF_BAND_CLOSED=true
ROOT_SAWTOOTH_SAVING_EXPONENT=1/100
COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true
COMPLETE_RECIPROCAL_SAVING_EXPONENT_M_SCALE=1/200
COMPLETE_RECIPROCAL_ERROR_M_SCALE=M^(2-1/200+o(1))
COMPLETE_RECIPROCAL_ERROR_B_SCALE=B^(399/400+o(1))
FULL_NONCONSTANT_LOCAL_FOURIER_MODES_AVERAGED=true
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_COMPLETE_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4be evaluate the diagonal/local-density term D_loc against A_W on regular dyadic boxes, freeze the first explicit rho_loc/E_loc pair if possible, and then propagate that pair into the 14-4as local-global-height exponent ledger
```
