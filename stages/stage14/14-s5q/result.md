# Stage14-s5q — Fourier-energy tensor contraction and final E-linear transition kernel

## Purpose

Stage14-s5p removed every positive-power loss coming from frozen auxiliary progression moduli and supplied auxiliary-uniform discrepancy estimates, auxiliary `ell^2` energy transfer, and a Hilbert-space lift of the quadratic large sieve.

This stage addresses the remaining **multi-edge discrepancy tensor contraction**. The result is that the tensor problem itself is not an additional obstruction.

The exact odd local rows from s5c/s5d have Fourier coefficient `ell^2` norm at most one at every prime. Their tensor product therefore has a uniform Fourier-energy budget. All other Jacobi factors in a monomial act by diagonal unitary multipliers on the auxiliary Hilbert coordinates. Hence a finite multi-edge local character monomial cannot enlarge the edgewise discrepancy energy supplied by s5p.

For the norm column

```text
E=m^2+n^2,
```

there is an additional exact simplification: selected and unselected `H`-prime rows coincide. Consequently the whole odd `E` column is one normalized Walsh subset expansion. The feared state-split `E` multiplicity is therefore contractive in `ell^2`.

After these reductions, the only unresolved local analytic problem is already present on a **single linear--E signed-root edge**. The s5m lattice second moment is power-saving in a large region, but becomes neutral in an explicit transition wedge. This stage derives the exact root-sawtooth boundary kernel which remains to be estimated there.

No new external theorem is used.

---

## 1. Primewise Fourier coefficient energy

After the product-square relation, s5h gives

```text
selected S or H   : (1+x)/2
selected X        : (1+s)(1+x)/4
unselected S or H : (1+x)/2
unselected X      : (3+x-s+s*x)/4,
```

where `x in {+1,-1}` is the relevant reciprocity bit and `s=chi_p(-1)`.

Write a row as `c0+c1*x`. Its coefficient energy is `|c0|^2+|c1|^2`.

The exact cases are

```text
selected S/H:       (1/2,1/2), energy 1/2
selected X, s=+1:   (1/2,1/2), energy 1/2
selected X, s=-1:   (0,0),     energy 0
unselected S/H:     (1/2,1/2), energy 1/2
unselected X, s=+1: (1/2,1/2), energy 1/2
unselected X, s=-1: (1,0),     energy 1.
```

Thus

```text
FOURIER_ROW_L2_ENERGY <= 1
```

at every odd prime.

The prime-2 contribution is the fixed eight-state table of s5f. It contributes only an absolute finite constant and no moving odd modulus.

---

## 2. Global Fourier-energy budget

For one physical Euclid point `P`, expand all odd local rows and let

```text
c_P(sigma)
```

be the coefficient of the complete local Fourier/state label `sigma`.

Primewise expansions tensor independently, so Hilbert tensor-product norms multiply. Therefore

```text
sum_sigma |c_P(sigma)|^2 <= C_2,
```

where `C_2` is an absolute constant from the finite `Q_2` table. We absorb it into Stage14 constants and write

```text
||c_P||_2 << 1.
```

For two physical points `P,P'`,

```text
|sum_sigma c_P(sigma) conjugate(c_P'(sigma))|
 <= ||c_P||_2 ||c_P'||_2
 << 1.
```

Hence the s5p collision-energy transfer remains valid with the **actual local-polynomial Fourier coefficients**, without a state-label cardinality loss.

---

## 3. Tensor contraction lemma

Fix one dyadic moving edge `(i,j)`. Carry every remaining local-state label in a Hilbert space `H`, and let

```text
Delta_ij(u,v) in H
```

be the auxiliary discrepancy vector supplied by s5p.

Every other reciprocal edge in the same monomial multiplies each auxiliary coordinate by a Jacobi symbol of absolute value one. Thus it defines a diagonal unitary operator

```text
U_{u,v}: H -> H.
```

Let `c in H` be the local Fourier coefficient vector. Section 2 gives `||c||_H << 1`. Therefore

```text
|<Delta_ij(u,v), U_{u,v} c>|
 <= ||Delta_ij(u,v)||_H ||c||_H
 << ||Delta_ij(u,v)||_H.
```

Squaring and summing the moving cells,

```text
sum_{u,v}
 |<Delta_ij(u,v),U_{u,v}c>|^2
 <<
 sum_{u,v} ||Delta_ij(u,v)||_H^2.
```

So finite multi-edge character assembly cannot enlarge an edgewise discrepancy `L^2` norm, apart from the harmless `B^epsilon` divisor/Mobius factors already present in s5p.

This proves

```text
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true.
```

---

## 4. Compatibility with the s5o graph escape

The same Hilbert space carries the separable/rank-one bulk pieces. By s5p the quadratic-large-sieve operator has the same norm after tensoring with `Id_H`.

Hence the three s5o graph cases remain valid after inserting the complete finite local Fourier coefficients:

1. a long--long edge is handled by the Hilbert-valued quadratic large sieve;
2. a very-long vertex with only short neighbors is handled by the auxiliary-progression squarefree completion;
3. an all-short active graph is handled by exact centering and periodic completion before the finite Hilbert contraction.

Together with the single-edge boundary work of s5n, the purely linear `K4` sector is now fully assembled:

```text
LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true.
```

The conservative saving is the one already recorded in s5o.

---

## 5. Exact simplification of the E/H column

At an odd prime `p|E`, the prime is an `H`-column prime.

From s5c, a selected `H` prime has label `23` and local conditions

```text
chi_p(a2*a3)=+1,
chi_p(a1)=+1.
```

Because `chi_p(a1*a2*a3)=+1`, the first condition follows from the second.

From s5d, an unselected `H` prime has exactly

```text
chi_p(d1)=+1.
```

For label `23`, `p` does not divide `d1`, so `a1` is exactly the `p`-unit part of `d1`. Therefore the selected and unselected rows are identical:

```text
p|E  =>  chi_p(d1)=+1.
```

Every odd `E` prime contributes

```text
(1+chi_p(d1))/2.
```

Let

```text
e=ker_odd(E).
```

Then the complete odd `E` column is exactly

```text
I_E(d1;e)
 = product_{p|e} (1+chi_p(d1))/2
 = 2^(-omega(e)) sum_{v|e} (d1/v).
```

Thus there is only **one Walsh subset variable `v|e`**. In any one Fourier monomial, all reciprocal edges incident to the state-split `E` column form one star centered at this same `v`.

---

## 6. E-Walsh weights are contractive

For fixed `e`, define

```text
w_e(v)=2^(-omega(e)) 1_{v|e}.
```

Then

```text
sum_{v|e} w_e(v)=1,
sum_{v|e} w_e(v)^2=2^(-omega(e))<=1.
```

So the E-subset expansion is normalized in `ell^1` and contractive in `ell^2`.

Combined with Section 2 and s5p auxiliary energy transfer, this proves

```text
STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS=false.
```

The remaining E-star Jacobi factors are diagonal unitaries on the auxiliary Hilbert coordinates. Therefore, for norm purposes, a full multi-edge monomial containing the E-star reduces to a **single moving linear--E edge discrepancy estimate**.

Hence

```text
STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true.
```

This statement concerns tensor multiplicity and contraction. It does not claim that the scalar linear--E edge is power-saving on every dyadic scale.

---

## 7. Reduction to one scalar E-linear edge

Let `u~U` be an odd squarefree state modulus on one linear column and let `v~V` be the E-Walsh subset modulus. Refine `v` to one of the signed root patterns of s5l/s5m.

All remaining linear graph variables, support labels, E-complement data, mod-4/mod-8 factors, and `Q_2` cases may be carried in the auxiliary Hilbert coordinate. Sections 2--6 show that they introduce no new exponent loss.

Thus the unresolved local analytic task is the scalar edge

```text
T_{i,E}(U,V)
 = sum_{u~U}
   sum_{v~V, split}
   sum_{r^2=-1 mod v}
   Delta_{i,E,r}(u,v)
   theta_{u,v,r}
   (u/v),
```

with `|theta_{u,v,r}|<=1` representing already-controlled auxiliary phases.

On a regular box of perimeter scale `M`, s5m gives

```text
sum_{u,v,r} |Delta_{i,E,r}(u,v)|^2
 <<_epsilon B^epsilon UV
 [1+M^2/K(U,V)^2],

K(U,V)=max(V^(1/2),min(U,V)).
```

Cauchy--Schwarz therefore gives

```text
|T_{i,E}(U,V)|
 <<_epsilon B^epsilon UV
 [1+M/K(U,V)].
```

The complete local-polynomial tensor contraction contributes no factor beyond this scalar bound.

---

## 8. Exact exponent atlas

Write

```text
U=M^alpha,
V=M^beta,
0<=alpha<=1,
0<=beta<=2.
```

Put

```text
kappa(alpha,beta)
 = max(beta/2,min(alpha,beta)).
```

Relative to the physical `M^2` scale, the current s5m/Cauchy discrepancy exponent is

```text
R_E(alpha,beta)
 = alpha+beta
   + max(0,1-kappa(alpha,beta))
   - 2.
```

Therefore

```text
R_E<0 : current signed-root L2 estimate is power-saving;
R_E=0 : transition/critical scale;
R_E>0 : current L2+Cauchy route is insufficient.
```

The zero boundary contains the three elementary pieces

```text
beta<1:  alpha=1;

beta=1:  1/2<=alpha<=1;

beta>1:  alpha+beta/2=1
         in the branch alpha<beta/2.
```

The central corner is

```text
(alpha,beta)=(1/2,1),
U~M^(1/2),
V~M.
```

There

```text
K~M^(1/2),
UV~M^(3/2),
UV*(M/K)~M^2,
```

so the current lattice second moment is exactly neutral.

The s5l sparse diagonal estimate is useful for geometry but also becomes non-saving for scalar reciprocal contraction once `UV` reaches the physical `M^2` scale. It therefore does not remove this transition wedge.

---

## 9. Exact root-sawtooth boundary kernel

The remaining scalar obstruction has an explicit form.

Fix one linear column `L_i` and choose an integral complementary linear coordinate `Y_i` so that the coordinate determinant is `±1` or `±2`. After recording the fixed parity coset, put

```text
x=L_i(m,n),
y=Y_i(m,n).
```

For a signed E root `r^2=-1 (mod v)`, transversality gives one congruence

```text
y == c_r x (mod v),
```

where `c_r` is a unit modulo `v`.

Write

```text
x=u*a.
```

On each polygonal piece of the transformed Stage14 box, the admissible integer y-values form an interval

```text
L(x) <= y <= R(x),
```

with affine endpoints. For an integer residue `b`, the exact counting identity is

```text
#{y in [L,R] : y==b (mod v)}
 = (R-L+1)/v
   + psi((L-1-b)/v)
   - psi((R-b)/v),
```

where

```text
psi(t)={t}-1/2.
```

Taking `b=c_r*u*a`, the length term produces the local-density main term already handled by the separable bulk. The unresolved discrepancy is therefore a finite linear combination of sums

```text
R(U,V)
 = sum_{v~V, split}
   sum_{r^2=-1 mod v}
   sum_{u~U}^*
   (u/v)
   sum_{a in I_u}
   b_{u,v,r,a}
   psi((A_r*u*a+B)/v),
```

where

```text
|b_{u,v,r,a}| <= B^epsilon,
|I_u| ~ M/U.
```

Auxiliary progressions from s5p only shorten the quotient intervals or place them in coprime residue classes. Mobius inversion for primitiveness gives divisor-many dilated copies of the same kernel.

Fourier expansion of the sawtooth reduces the problem to hybrid sums of the schematic form

```text
sum_u (u/v) e(h*A_r*a*u/v),
```

averaged simultaneously over

```text
u,
v,
r^2=-1 mod v,
a~M/U.
```

At `U~M^(1/2), V~M`, one-variable completion sits exactly at square-root conductor length and gives no power saving. A genuinely bilinear/hybrid estimate is therefore required.

This root-sawtooth reciprocal sum is the final local analytic object isolated by s5q.

---

## 10. Status after s5q

The following are now closed:

```text
multi-edge state-label cardinality loss,
auxiliary Hilbert tensor multiplicity,
K4 degree-2/degree-3 conductor pile-up,
state-split E label multiplicity,
E-star multi-edge tensor-norm loss,
linear-only full local-polynomial assembly.
```

The remaining failure is **not tensorial**. It is the scalar signed-root E-linear transition estimate of Sections 8--9.

Accordingly s5q does not set `FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true`.

---

## Deterministic audit

The accompanying audit checks:

- the exact Fourier `ell^2` energy of every odd local row for both values of `s`;
- multiplicativity of tensor-product Fourier energy;
- equality of selected and unselected H-prime conditions under the product-square constraint;
- the exact E-column Walsh identity;
- `ell^1` and `ell^2` norms of the E-Walsh weights;
- invariance of finite auxiliary vector norms under Jacobi phase multiplication;
- the exponent atlas `R_E(alpha,beta)` and the three critical boundary pieces;
- signed-root transversality in all four linear coordinate charts;
- the exact floor/sawtooth residue-count identity.

The finite audit is regression evidence only. The tensor theorem is carried by the exact local character-polynomial identities, Hilbert-space Cauchy--Schwarz, s5p energy transfer, and unitary Jacobi multipliers.

---

## Boundary

```text
STAGE14_S5Q=COMPLETE_FOURIER_ENERGY_TENSOR_CONTRACTION_AND_FINAL_E_TRANSITION_KERNEL
ODD_LOCAL_ROW_FOURIER_L2_ENERGY_LE_1=true
GLOBAL_LOCAL_FOURIER_ENERGY_BOUNDED=true
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true
LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
E_SELECTED_UNSELECTED_H_ROW_IDENTICAL=true
E_COLUMN_SINGLE_WALSH_SUBSET_EXACT=true
E_WALSH_L1_NORMALIZED=true
E_WALSH_L2_CONTRACTIVE=true
STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS=false
STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true
FULL_LOCAL_CHARACTER_POLYNOMIAL_REDUCED_TO_SINGLE_E_LINEAR_EDGE=true
E_LINEAR_EXISTING_L2_POWER_SAVING_REGION_CLASSIFIED=true
E_LINEAR_TRANSITION_WEDGE_PERSISTS=true
FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5r prove a hybrid bilinear estimate for the root-sawtooth reciprocal kernel, with the critical target U~M^(1/2), V~M, or exhibit a genuine resonance preventing power saving
```
