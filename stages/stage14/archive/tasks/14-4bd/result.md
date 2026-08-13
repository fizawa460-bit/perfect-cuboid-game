# Stage14-4bd — import s5r root-spacing closure and freeze the complete reciprocal exponent

## Result

Merged Stage14-4bc left exactly one nonconstant local obstruction: the single linear--`E` root-sawtooth kernel on the handoff band

```text
R_E(alpha,beta)>-1/200.
```

Merged Stage14-s5r now closes that kernel and, with it, the actual complete finite local 2-descent character polynomial on every regular Stage14 dyadic Euclid box.

The main-track consequence is unconditional:

```text
E_rec(M) <<_epsilon M^(2-1/200+epsilon).
```

Equivalently, on the Stage14 height scale `B~M^2`,

```text
E_rec(B) << B^(399/400+o(1)).
```

Thus the complete **nonconstant reciprocal/local Fourier contribution** now has a positive power-saving exponent.

This does not yet identify the final local retainer `rho_loc`.  The constant/diagonal local-density term `D_loc` is a separate contribution in

```text
S_W <= D_loc + E_rec
```

and must still be compared with `A_W`.

---

## 1. Imported s5r root-spacing theorem

For the final scalar linear--`E` edge, s5q/4bc wrote the discrepancy as a finite combination of

```text
R(U,V)
 = sum_{v~V,split}
   sum_{r^2=-1 mod v}
   sum_{u~U}^*
   xi_{u,v,r}
   sum_{a in I_{u,sigma}}
   psi((c_r*u*a+B)/v),
```

where `psi(t)={t}-1/2`, the quotient intervals/progressions satisfy `|I_{u,sigma}|<<M/U`, and all frozen local data are carried with the s5p auxiliary-uniform energy bounds.

For the four linear charts `A,B,C,D`, s5r identifies positive-definite binary quadratic forms

```text
F_A(X,Y)=F_B(X,Y)=X^2+Y^2,
F_C(X,Y)=2X^2+2XY+Y^2,
F_D(X,Y)=2X^2-2XY+Y^2.
```

The signed-root coefficient `c_r` satisfies

```text
F_i(c_r,1)=0 mod v.
```

After the exact finite Fourier expansion of the sawtooth, a frequency `h` with centered residue `delta` satisfies the divisibility

```text
v/g | F_i(delta/g,(h/g)u d),
g=(h,v).
```

Positive definiteness makes the integer on the right nonzero.  Divisor counting therefore gives the near-resonance estimate

```text
N_h(D) <<_epsilon M^epsilon U D.
```

Dyadic spacing in `delta`, followed by the exact sawtooth Fourier sum, yields

```text
R(U,V) <<_epsilon M^epsilon U V.
```

The estimate is uniform in the coprime auxiliary progressions inherited from s5p and remains valid after inserting the Jacobi factor `(u/v)`.

Hence the former critical point

```text
U~M^(1/2), V~M
```

satisfies directly

```text
R(U,V) << M^(3/2+o(1)),
```

rather than the neutral `M^2` bound from the earlier lattice-Cauchy estimate.

---

## 2. Exact E-Walsh small-side pairing

From s5q the complete odd `E` column is

```text
I_E(d1;e)
 = 2^(-omega(e)) sum_{v|e} (d1/v),
```

where `e=ker_odd(E)`.

Merged s5r pairs complementary divisors `v <-> e/v` exactly and obtains

```text
I_E(d1;e)
 = 2^(-omega(e))
   (1+(d1/e))
   sum_{v|e, v<sqrt(e)} (d1/v).
```

The extra whole-`E` factor is harmless:

```text
q|A or B => (q/e)=1,
q|C or D => (q/e)=(2/q).
```

Thus it is only a product of one-variable mod-8 characters and does not restore a moving `E` conductor.

Consequently the analytically active E-Walsh modulus may always be taken with

```text
v<sqrt(e)<=sqrt(E)<<M,
```

so `V<<M`.

---

## 3. Complete dyadic sector split

Set

```text
Z=M^(3/20).
```

### Far-from-area sector

If

```text
UV <= M^2/Z,
```

then the root-spacing theorem gives

```text
R(U,V)
 << M^epsilon U V
 << M^(2-3/20+epsilon).
```

So this sector saves `3/20` on the M-scale.

### Near-area sector

If

```text
UV > M^2/Z,
```

then `U,V>>M^(17/20)` because both are `O(M)` after the E-Walsh pairing.

Restore the remaining reciprocal neighbors of the linear state variable `u` and use the s5o threshold `M^(1/100)`.

There are exactly two cases.

#### Case A — another long linear neighbor exists

The already-proved s5o/s5p long--long quadratic-large-sieve escape applies and gives

```text
M^(-1/200+epsilon)
```

relative saving.

#### Case B — every other u-neighbor is short

The linear K4 degree is at most three, so their product conductor satisfies

```text
q0 <= M^(3/100).
```

Merged s5r proves the elementary squarefree mixed character--additive completion

```text
sum_{n in J} mu(n)^2 chi_q(n)e(tn/v)
 <<_epsilon M^epsilon |J|^(1/2) q^(1/4),
```

by square-divisor expansion plus quadratic Gauss completion.

After summing the quotient variable, E moduli and root choices, s5r obtains

```text
R(U,V)
 << M^(733/400+epsilon).
```

Since

```text
2-733/400 = 67/400 > 1/6,
```

this case is far stronger than the conservative `1/200` main-track budget.

There is no unclassified dyadic sector and no surviving root-sawtooth resonance.

---

## 4. Freeze the complete reciprocal exponent

The three relevant saving margins are

```text
root-spacing far sector:      3/20,
near-area Case A:             1/200,
near-area Case B:             67/400.
```

Therefore their minimum is exactly

```text
delta_rec = 1/200.
```

Hence

```text
E_rec(M) << M^(2-1/200+o(1))
         = M^(399/200+o(1)).
```

With `B~M^2`, this becomes

```text
E_rec(B) << B^(399/400+o(1)).
```

This is the first complete positive exponent for all nonconstant local Fourier modes of the actual Stage14 local 2-descent character system.

In particular,

```text
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true.
```

The stronger arbitrary-coefficient prime-level family large-sieve candidate from s5g is still not claimed; it is no longer needed for this actual local polynomial closure.

---

## 5. What remains: the diagonal/local-density term

The 14-4au decomposition remains

```text
S_W <= D_loc + E_rec.
```

Stage14-4bd has now closed `E_rec` with a quantitative positive exponent.  But `D_loc` is the constant/diagonal local-density contribution, not an oscillatory reciprocal error.

Therefore it would still be incorrect to write

```text
rho_loc=M^(-1/200).
```

The next main-track task is to evaluate `D_loc/A_W` on regular dyadic boxes, including all fixed `Q_2` branches and odd local-density coefficients, and decide whether it supplies a genuine retainer factor or only a constant density.

Only after that step can the first complete pair

```text
S_W <= rho_loc A_W + E_loc
```

be frozen and propagated into the 14-4as local/global/height ledger.

---

## Boundary

```text
STAGE14_4BD=S5R_ROOT_SAWTOOTH_IMPORTED_AND_COMPLETE_RECIPROCAL_EXPONENT_FROZEN
S5R_ROOT_SPACING_THEOREM_IMPORTED=true
ROOT_CHART_QUADRATIC_FORMS_EXACT=true
ROOT_NEAR_RESONANCE_DIVISOR_COUNT_PROVED=true
ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true
CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED=true
E_WALSH_SMALL_SIDE_PAIRING_EXACT=true
E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true
WHOLE_E_PAIRED_FACTOR_ONE_VARIABLE=true
E_LINEAR_TRANSITION_WEDGE_CLOSED=true
GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true
ROOT_SPACING_FAR_SECTOR_SAVING_M_SCALE=3/20
NEAR_AREA_LONG_EDGE_SAVING_M_SCALE=1/200
NEAR_AREA_MIXED_COMPLETION_SAVING_M_SCALE=67/400
COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true
COMPLETE_RECIPROCAL_SAVING_EXPONENT_M_SCALE=1/200
COMPLETE_RECIPROCAL_ERROR_M_SCALE=M^(399/200+o(1))
COMPLETE_RECIPROCAL_ERROR_B_SCALE=B^(399/400+o(1))
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_COMPLETE_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4be evaluate the diagonal/local-density term D_loc against A_W on regular dyadic boxes, freeze the first explicit rho_loc/E_loc pair if possible, and propagate it into the 14-4as local-global-height exponent ledger
```
