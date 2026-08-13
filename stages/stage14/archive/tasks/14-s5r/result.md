# Stage14-s5r — root-sawtooth spacing theorem and closure of the local character average

## Purpose

Stage14-s5q reduced the complete finite local 2-descent character polynomial to one remaining scalar linear--`E` transition kernel.  On a regular Euclid box of linear scale `M`, the unresolved term had the form

```text
R(U,V)
 = sum_{v~V, split}
   sum_{r^2=-1 mod v}
   sum_{u~U}^*
   theta_{u,v,r}
   (u/v)
   sum_{a in I_{u,sigma}}
   psi((c_r*u*a+B)/v),
```

where `psi(t)={t}-1/2`, `|I_{u,sigma}| <= C M/U`, and the auxiliary state data `sigma` only partitions the `a`-sum into divisor-many intervals / coprime arithmetic progressions.  The s5m lattice second moment is neutral at the critical corner `U~M^(1/2), V~M`, so s5q left this as the final local analytic object.

This stage closes it.

The key point is elementary but strong: the signed root `r^2=-1 (mod v)` forces every small Fourier frequency of the sawtooth progression to be represented by one of four positive-definite binary quadratic forms.  Hence the apparently dangerous near-resonant frequencies are counted by divisors of a nonzero quadratic-form value.  A dyadic spacing argument then gives

```text
R(U,V) <<_epsilon B^epsilon U V
```

for the root-sawtooth part, uniformly in all auxiliary progression steps inherited from s5p.

A second exact simplification pairs the E-Walsh divisors `v` and `e/v`, so the analytic E-subset modulus may always be oriented to the side

```text
v < sqrt(e) <= sqrt(E) << M.
```

Thus `V` never needs to exceed the physical linear scale `M`.  The only sector where the `UV` spacing bound can approach the physical `M^2` scale is then the near-area sector `U,V~M`.  There the s5o graph escape says either another long linear edge is already available, or all other `u`-incident conductors are short.  In the latter case a squarefree mixed Gauss-completion bound closes the sector.

No new external theorem is used.

---

## 1. The four signed-root charts

Use the four linear columns

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

For each moving column choose an integral complementary coordinate `y`, after recording the fixed parity coset.  The signed E-root condition becomes

```text
y == c_r x (mod v),
r^2 == -1 (mod v).
```

The four possible coefficients `c_r` may be chosen as

```text
A: c_r = -r,
B: c_r =  r,
C: c_r = -(r+1)/2,
D: c_r =  (1-r)/2.
```

Therefore `c_r` satisfies one of the four quadratic congruences

```text
F_A(c,1)=c^2+1                  ==0 mod v,
F_B(c,1)=c^2+1                  ==0 mod v,
F_C(c,1)=2c^2+2c+1             ==0 mod v,
F_D(c,1)=2c^2-2c+1             ==0 mod v.
```

Homogenize:

```text
F_A(X,Y)=F_B(X,Y)=X^2+Y^2,
F_C(X,Y)=2X^2+2XY+Y^2,
F_D(X,Y)=2X^2-2XY+Y^2.
```

All four are positive definite, with discriminant `-4` or `-4` after the harmless factor normalization.  In particular

```text
F_i(X,Y)>0
```

for every nonzero integer pair `(X,Y)`.

This positivity is what rules out an exact nonzero resonance.

---

## 2. Exact discrete Fourier expansion of the sawtooth

For integer `k` modulo an odd modulus `v`, set

```text
psi_v(k)=psi(k/v).
```

Its exact finite Fourier expansion is

```text
psi_v(k)
 = -1/(2v)
   + sum_{h=1}^{v-1} gamma_v(h) e(hk/v),
```

with

```text
gamma_v(h) = -1/[v(1-e(-h/v))].
```

Hence, writing `|h|_v=min(h,v-h)`,

```text
|gamma_v(h)| << 1/|h|_v,
```

and after pairing `h` with `v-h`, the nonzero frequencies may be indexed by

```text
1 <= h <= v/2
```

with total Fourier `ell^1` cost `O(log v)`.

There is no truncation error in this step.

---

## 3. Frequency-to-quadratic-form divisibility

Fix one auxiliary arithmetic progression in the quotient variable,

```text
a=a_0+d n,
```

where the progression step `d` is coprime to `v`; this coprimality is supplied by the pairwise odd support and s5p transversality.

For a Fourier frequency `h`, put

```text
t = h*c_r*u*d (mod v).
```

Let `delta` be its centered residue,

```text
-v/2 < delta <= v/2.
```

Because `(u d,v)=1`,

```text
g=(h,v)=(delta,v),
```

and we may write

```text
h=g h_1,
v=g v_1,
delta=g delta_1,
(h_1,v_1)=1.
```

Modulo `v_1`,

```text
c_r == delta_1 * (h_1 u d)^(-1).
```

Homogeneity of the relevant chart polynomial therefore gives the exact divisibility

```text
v_1 | F_i(delta_1, h_1*u*d).
```

The integer on the right is nonzero by positive definiteness.

This is the central s5r observation.

---

## 4. Counting near-resonant root frequencies

Fix `h`, a dyadic `u`-range `u~U`, and `D>=1`.  Count triples

```text
(v,r,u)
```

with

```text
v~V,
r^2=-1 mod v,
|delta|<=D.
```

For fixed `g|h`, `u`, and `delta_1` with `|delta_1|<=D/g`, the previous section forces

```text
v_1 | F_i(delta_1,h_1*u*d).
```

The divisor bound gives only `B^epsilon` possible `v_1` in the dyadic range.  The roots above the primes contained in `g` contribute at most `2^omega(g)`, also `B^epsilon`.  Summing over `g|h` yields

```text
N_h(D)
 := #{(v,r,u): |delta|<=D}
 <<_epsilon
 B^epsilon U D.
```

Crucially, there is no factor `V` on the right.

Thus the Fourier frequencies for which the sawtooth progression moves unusually slowly are arithmetically sparse.

---

## 5. Root-sawtooth spacing theorem

Let one quotient progression have length `N`.  For a nonzero Fourier mode,

```text
|sum_{n in J} e(h*c_r*u*d*n/v)|
 << min(N, V/|delta|).
```

Use dyadic ranges `|delta|~D` and the bound from Section 4.  The contribution for fixed `h` is

```text
<< B^epsilon
   sum_D U D min(N,V/D).
```

Split at

```text
D_0=V/N.
```

For `D<=D_0`, the dyadic sum is `O(UV)`.  For `D>D_0`, every dyadic interval also contributes `O(UV)`, and the logarithmic number of intervals is absorbed into `B^epsilon`.  Therefore

```text
sum_{v~V}
 sum_{r^2=-1 mod v}
 sum_{u~U}
 |sum_{n in J} e(h*c_r*u*d*n/v)|
 <<_epsilon
 B^epsilon U V.
```

Now sum the exact sawtooth Fourier coefficients.  Their `ell^1` norm is logarithmic, so

```text
ROOT_SAWTOOTH_SPACING_BOUND:

sum_{v~V,split}
 sum_{r^2=-1 mod v}
 sum_{u~U}^*
 xi_{u,v,r}
 sum_{a in I_{u,sigma}}
 psi((c_r*u*a+B)/v)

<<_epsilon B^epsilon U V,
```

for every unit-modulus factor `xi_{u,v,r}` which is constant on each quotient progression.  Divisor-many progression pieces, Möbius dilations, parity classes, and the s5p auxiliary states are absorbed into `B^epsilon`.

The tiny constant Fourier coefficient contributes only boundary size and is smaller.

This theorem does not use cancellation in `(u/v)`; it remains valid after inserting that Jacobi factor.

---

## 6. Pair the E-Walsh divisor with its complement

Let

```text
e=ker_odd(E)
```

and let `d_1` be the odd first Kummer squareclass unit appearing in the E/H row.  From s5q,

```text
I_E(d_1;e)
 = 2^(-omega(e))
   sum_{v|e} (d_1/v).
```

For squarefree `e>1`, divisors pair without a fixed point:

```text
v <-> e/v.
```

Since

```text
(d_1/(e/v))=(d_1/e)(d_1/v),
```

we obtain the exact small-side identity

```text
I_E(d_1;e)
 = 2^(-omega(e))
   (1+(d_1/e))
   sum_{v|e, v<sqrt(e)} (d_1/v).
```

The paired coefficients still have total `ell^1` mass at most one and `ell^2` mass at most one.

Therefore every moving E-Walsh modulus used analytically may be chosen with

```text
v < sqrt(e) <= sqrt(E) << M
```

on a regular Euclid box.

So from this stage onward one may impose

```text
V <= C M.
```

There is no `V~M^2` transition endpoint.

---

## 7. The whole-E factor created by pairing is harmless

The extra factor

```text
(d_1/e)
```

does not reintroduce an E edge.

Primewise, for any odd squarefree divisor `q` of the four linear kernels,

```text
q | A or B  => (q/e)=1,
q | C or D  => (q/e)=(2/q).
```

Indeed every prime of `e` is `1 mod 4`, so reciprocity has no sign, and

```text
E == square mod A,B,
E == 2*square mod C,D.
```

Thus for an arbitrary state piece assembled from the four linear columns,

```text
(d_1/e)
```

is a product only of fixed one-variable mod-8 characters.  It belongs to the already closed s5o/s5q auxiliary Hilbert factor.

The complement pairing therefore genuinely removes the large E-modulus side rather than moving the problem elsewhere.

---

## 8. Far-from-area sector

The physical regular-box scale is `M^2`.  Choose

```text
Z=M^(3/20).
```

In the sector

```text
UV <= M^2/Z,
```

Section 5 gives immediately

```text
R(U,V)
 <<_epsilon
 B^epsilon M^2/Z
 = B^epsilon M^(37/20).
```

Hence this entire sector saves

```text
M^(-3/20+epsilon).
```

over the physical area scale.

In particular the old critical point

```text
U~M^(1/2), V~M
```

now satisfies

```text
R << B^epsilon M^(3/2),
```

which is far inside the power-saving region.

Thus the precise s5q critical corner is closed by the root-spacing theorem alone.

---

## 9. Near-area sector and the s5o graph escape

It remains to consider

```text
UV > M^2/Z.
```

Since Section 6 gives `U,V<<M`, both sides satisfy

```text
U,V >> M/Z = M^(17/20).
```

Now restore the other reciprocal factors attached to the same linear state vertex `u`.

Use the s5o threshold

```text
S=M^(1/100).
```

There are two cases.

### Case A: another long linear neighbor exists

If an additional reciprocal neighbor of `u` has modulus at least `S`, freeze the remaining variables and use the already proved s5o/s5p long--long linear edge escape.  Its conservative saving is

```text
M^(-1/200+epsilon).
```

No E-transition estimate is needed in this case.

### Case B: every other u-neighbor is short

The linear `K4` degree is at most three, so the product `q_0` of all other `u`-incident odd character conductors satisfies

```text
q_0 <= M^(3/100).
```

The u-dependent multiplicative factor is then one real squarefree character of conductor dividing

```text
v q_0
```

(up to the fixed mod-8 factor).

We next use a mixed squarefree Gauss-completion estimate.

---

## 10. Squarefree mixed character--additive completion

Let `chi_q` be a primitive real character of odd squarefree conductor `q`, and let

```text
e(t n/v)
```

be any additive twist whose denominator divides `q`.  For an interval `J` of length `T`,

```text
sum_{n in J} mu(n)^2 chi_q(n) e(t n/v)
 <<_epsilon
 B^epsilon T^(1/2) q^(1/4).
```

Proof: expand

```text
mu(n)^2=sum_{d^2|n}mu(d).
```

Terms with `(d,q)>1` vanish.  For the remaining terms, completion modulo `q` reduces every complete twisted sum to a product of ordinary quadratic Gauss sums (or zero), hence to `O(sqrt(q))`.  Splitting the squarefree-sieve variable at `D` gives

```text
D sqrt(q) + T/D,
```

and optimization yields the stated bound.  The same proof tolerates fixed coprime progressions and residue classes.

Using the exact sawtooth Fourier expansion costs only `B^epsilon`.  Therefore, in Case B, for fixed `v,r,a`,

```text
sum_{u~U}^*
 (u/v)
 (u/q_0)
 psi((c_r*u*a+B)/v)

<<_epsilon
 B^epsilon U^(1/2) (V q_0)^(1/4).
```

There are `O(M/U)` quotient values `a`, `O(V)` moduli `v`, and only `B^epsilon` roots per `v`.  Hence

```text
R(U,V)
 <<_epsilon
 B^epsilon
 M V^(5/4) q_0^(1/4) U^(-1/2).
```

In the near-area sector,

```text
U >= M^(17/20),
V <= M,
q_0 <= M^(3/100),
```

so

```text
R(U,V)
 <<_
 B^epsilon
 M^(733/400)
```

because

```text
1 + 5/4 - 17/40 + 3/400
 = 733/400
 = 1.8325.
```

Thus Case B saves more than `M^(-1/6)` from the physical `M^2` scale.  The weaker s5o Case-A saving `M^(-1/200)` remains the uniform global exponent budget for the assembled local polynomial.

---

## 11. Closure of the E transition wedge

Combine Sections 6--10.

Every E-Walsh term is first paired to a divisor `v<sqrt(e)`, so `V<<M`.

Then:

```text
UV <= M^2/Z
  => root-spacing bound gives M^(-3/20) saving;

UV > M^2/Z and another long linear edge exists
  => s5o long-edge escape gives M^(-1/200) saving;

UV > M^2/Z and all other u-neighbors are short
  => mixed Gauss completion gives >M^(-1/6) saving.
```

There is no unclassified dyadic sector.

Therefore

```text
E_LINEAR_TRANSITION_WEDGE_CLOSED=true.
```

In particular the original critical target

```text
U~M^(1/2), V~M
```

has the stronger direct bound

```text
R(U,V) <<_epsilon B^epsilon M^(3/2).
```

No genuine root-sawtooth resonance persists.

---

## 12. Consequence for the complete local character polynomial

Stage14-s5q already proved that

- the linear-only `K4` polynomial is fully assembled;
- all local Fourier coefficient tensors have bounded energy;
- the state-split E-star contracts to a single linear--E edge;
- auxiliary progressions and labels introduce no positive-power loss.

Section 11 now closes that final scalar edge.

Hence the complete finite local 2-descent character system from s5f has a power-saving average on every regular Stage14 dyadic Euclid box:

```text
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true.
```

The conservative assembled exponent inherited from the s5o graph escape is

```text
M^(-1/200+epsilon).
```

This is a theorem about the actual Stage14 local character system.  It is not promoted to the stronger arbitrary-coefficient prime-level large-sieve candidate formulated in s5g, so

```text
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
```

remains the correct boundary flag.

Also, local solubility of a 2-cover is not the same as existence of a global rational point.  The Sha / global-solubility step and the physical small-point window from s5a/s3 remain separate.

---

## 13. Deterministic audit

The accompanying audit checks:

- all four chart identities `F_i(c_r,1)==0 mod v`;
- positive definiteness of the four integer quadratic forms on a finite box;
- exact finite Fourier reconstruction of `psi(k/v)`;
- the frequency divisibility `v_1|F_i(delta_1,h_1ud)` including nontrivial `(h,v)`;
- finite near-resonance counts against the `U D B^epsilon` shape;
- exact E-Walsh complement pairing;
- divisor-level whole-E identities for arbitrary subpieces of `A,B,C,D`;
- sample mixed squarefree character--additive sums against the completion shape;
- the cutoff/exponent ledger for `Z=M^(3/20)` and the s5o threshold `M^(1/100)`.

Finite computation is regression evidence only.  The proof is carried by exact finite Fourier expansion, positive-definite quadratic-form divisibility, divisor bounds, E-Walsh complement pairing, Gauss completion, and the already-proved s5o/s5p graph escape.

---

## Boundary

```text
STAGE14_S5R=COMPLETE_ROOT_SAWTOOTH_SPACING_AND_FULL_LOCAL_CHARACTER_AVERAGE
ROOT_CHART_QUADRATIC_FORMS_EXACT=true
ROOT_SAWTOOTH_FINITE_FOURIER_EXACT=true
ROOT_FREQUENCY_QUADRATIC_FORM_DIVISIBILITY_PROVED=true
ROOT_NEAR_RESONANCE_DIVISOR_COUNT_PROVED=true
ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true
CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED=true
E_WALSH_SMALL_SIDE_PAIRING_EXACT=true
E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true
WHOLE_E_PAIRED_FACTOR_ONE_VARIABLE=true
MIXED_SQUAREFREE_GAUSS_COMPLETION_PROVED=true
E_LINEAR_TRANSITION_WEDGE_CLOSED=true
GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5s insert the Stage14-s3 physical small-point/height window into the now-closed local character average, quantify the locally soluble descent-class contribution, and isolate the remaining global rational-point/Sha gap
```
