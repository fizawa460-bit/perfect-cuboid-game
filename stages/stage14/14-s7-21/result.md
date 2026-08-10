# Stage14-s7-21 — primewise orientation linearization and dual CRT short-vector obstruction

## Status

`COMPLETE_PRIMEWISE_ORIENTATION_LINEARIZATION_AND_DUAL_CRT_SHORT_VECTOR_REDUCTION`

Merged Stage14-s7-20 localizes every collision capable of saturating the current `7/8` endpoint to the balanced eight-cell system

```text
k cells:  alpha,beta,gamma,delta,
          each exponent in [3/16,5/16],

xi cells: R,S,T,J,
          each exponent in [1/8,1/4],
```

with four difference-square divisibilities and four positive sum-of-two-squares divisibilities.

Stage14-s7-21 audits how many genuinely independent arithmetic conditions these eight divisibilities contain.

The key conclusion is structural:

1. after a `B^o(1)` primewise sign/Gaussian-orientation refinement, the four `xi`-cell divisibilities become a homogeneous rank-four linear CRT lattice on the actual squarepart roots `(x1,y1,x2,y2)` with exact determinant `xi^2`;
2. the four `k`-cell divisibilities become a homogeneous rank-two linear CRT lattice on `(z1,z2)` with exact determinant `k^2`;
3. on the endpoint root boxes, the short vectors of the first lattice have rank at most `3`, while those of the second have rank at most `1`;
4. rank one on the `k` side fixes the rational ratio `z1:z2`, hence fixes the exact product ratio `x1*y1 : x2*y2`;
5. this recovers only a `B^o(1)` partner bound for a fixed first state, not an average scarcity theorem.

Therefore the eight divisibilities must **not** be multiplied as eight independent local savings.  The current whole-family exponent remains `7/8`.

The new live receiver is the average existence of compatible short vectors in these two large-determinant lattices:

```text
BalancedDualCRTShortVectorEnergy.
```

---

## 1. Imported endpoint packet

Take two distinct reduced physical states with the same squarefree labels

```text
xi=ker(P_1 Q_1)=ker(P_2 Q_2),
k =ker(Q_1^2-P_1^2)=ker(Q_2^2-P_2^2).
```

At the merged 4cd endpoint,

```text
P_i,Q_i,Q_i-P_i,Q_i+P_i ~ B^(1/2),
xi ~ B^(3/4),
k  = B^(1-o(1)).
```

Write

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2,
R*S*T*J=xi,
```

and

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
alpha*beta*gamma*delta=k.
```

Inside each four-cell family the cells are pairwise coprime and squarefree.

The endpoint sizes are

```text
x_i,y_i ~ B^(1/16),
r_i,s_i=B^o(1),
z_i~B^(1/8),
omega_i=B^o(1),
```

where

```text
Q_i^2-P_i^2=k*omega_i^2,

z_i = 2*x_i*y_i/g_i,
g_i=gcd(Q_i-P_i,Q_i+P_i) in {1,2}.
```

Merged s7-20 supplies the eight exact square-divisibilities.

Merged 4ce additionally supplies the exact odd-prime residue lock on switching cells.  No density multiplication is imported from 4ce.

---

## 2. Primewise linearization of a difference-square cell

Consider a typical agreement-cell congruence

```text
c^2 | U^2-V^2,
```

where `c` is squarefree and every odd prime `p|c` is coprime to `UV`.

For an odd `p|c`,

```text
p^2 | (U-V)(U+V).
```

Since `p` cannot divide both `U-V` and `U+V`, exactly one of the two factors carries the full `p^2` divisibility.  Thus every prime chooses a sign

```text
U == epsilon_p V (mod p^2),
epsilon_p in {+1,-1}.
```

The signs may vary from prime to prime.  Consequently one must **not** assert globally that `c^2|(U-V)` or `c^2|(U+V)` without refining the prime support.

After refining by the primewise signs, CRT gives one unit relation modulo `c^2`.

In the `xi` system, `U,V` are themselves unit multiples of squares such as `y_1^2,y_2^2`.  Because an actual physical solution exists, the resulting unit ratio is a square modulo every `p^2`.  Taking the square root gives at most two additional branches per odd prime.

Therefore a difference-square cell produces at most

```text
4^omega(c)=B^o(1)
```

linear root branches.

The 2-primary convention contributes only `O(1)` cases.

---

## 3. Primewise linearization of a positive switch cell

For a switching cell the typical congruence is

```text
c^2 | U^2+V^2.
```

Merged 4ce proves that every odd switching prime is `1 mod 4`.  Hence for each odd `p|c` there are exactly two lifts modulo `p^2` of a square root of `-1`.

Thus

```text
U == iota_p V (mod p^2),
iota_p^2 == -1 (mod p^2),
```

for one of the two Gaussian orientations.

Again, when `U,V` are unit multiples of root squares, the existence of the actual physical root pair guarantees the required ratio has a square root.  Refining by that root gives at most another factor `2` per odd prime.

Therefore the positive switch cell also decomposes into only

```text
B^o(1)
```

linear root branches.

This is an exact primewise orientation refinement, not a claim of cancellation.

---

## 4. The xi-side four-dimensional CRT lattice

Fix

```text
R,S,T,J,
omega_1,omega_2,
```

together with one legal primewise sign/Gaussian-root branch in each cell.

After absorbing the fixed unit coefficients into branch parameters, the four `xi` divisibilities become linear root congruences of the form

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2),
x_2 == lambda_S*y_1 (mod S^2),
y_2 == lambda_T*x_1 (mod T^2),                     (4.1)
```

where every `lambda_*` is a unit modulo its indicated modulus.

Let

```text
Lambda_xi subset Z^4
```

be the homogeneous lattice of vectors

```text
(x_1,y_1,x_2,y_2)
```

satisfying (4.1).

Each individual congruence has index equal to its modulus because one coefficient is a unit.  The four moduli

```text
R^2,S^2,T^2,J^2
```

are pairwise coprime.  Therefore the four congruence sublattices have coprime indices and

```text
boxed:
[Z^4:Lambda_xi]
 =R^2*S^2*T^2*J^2
 =xi^2.                                             (4.2)
```

Equivalently,

```text
boxed:
det Lambda_xi=xi^2.                                (4.3)
```

At the endpoint,

```text
det Lambda_xi = B^(3/2+o(1)).                      (4.4)
```

This determinant is exact; no probabilistic independence is used.

---

## 5. The k-side two-dimensional CRT lattice

Fix

```text
alpha,beta,gamma,delta,
r_i,s_i,
```

and one legal primewise orientation branch in every `k` cell.

The four `k` divisibilities become relations

```text
z_1 == mu_alpha*z_2 (mod alpha^2),
z_1 == mu_beta *z_2 (mod beta^2),
z_1 == mu_gamma*z_2 (mod gamma^2),
z_1 == mu_delta*z_2 (mod delta^2),                 (5.1)
```

with unit `mu_*`.

Let

```text
Lambda_k subset Z^2
```

be the lattice of `(z_1,z_2)` satisfying (5.1).  As above, the cell-square moduli are pairwise coprime and each row has exact index its modulus.  Hence

```text
boxed:
[Z^2:Lambda_k]
 =alpha^2*beta^2*gamma^2*delta^2
 =k^2,                                              (5.2)
```

so

```text
boxed:
det Lambda_k=k^2=B^(2-o(1)).                       (5.3)
```

Again this is an exact CRT determinant, not a large-sieve estimate.

---

## 6. Endpoint short-rank collapse

Put

```text
L=B^(1/16+o(1)),
Z=B^(1/8+o(1)).
```

The physical root vectors satisfy

```text
|x_i|,|y_i| <= B^(1/16+o(1)),
|z_i| <= B^(1/8+o(1)).
```

### 6.1 xi lattice

If four linearly independent vectors of `Lambda_xi` all had sup norm `O(L)`, the absolute determinant of those four vectors would be

```text
O(L^4)=B^(1/4+o(1)).
```

But four independent lattice vectors generate a sublattice whose determinant is an integer multiple of `det Lambda_xi`, hence at least

```text
B^(3/2-o(1)).
```

This is impossible.  Therefore

```text
boxed:
rank(span(Lambda_xi cap [-CL,CL]^4)) <= 3.          (6.1)
```

for every fixed constant `C` and every endpoint packet.

The determinant-to-root-box exponent gap is

```text
3/2-4*(1/16)=5/4.                                   (6.2)
```

### 6.2 k lattice

Similarly, two independent vectors of `Lambda_k` of size `O(Z)` would have determinant

```text
O(Z^2)=B^(1/4+o(1)),
```

contradicting

```text
det Lambda_k=B^(2-o(1)).
```

Hence

```text
boxed:
rank(span(Lambda_k cap [-CZ,CZ]^2)) <= 1.           (6.3)
```

The determinant-to-`z`-box exponent gap is

```text
2-2*(1/8)=7/4.                                      (6.4)
```

Thus every fixed oriented `k` packet has at most one rational short direction.

---

## 7. Rank one fixes the physical product ratio

If an oriented `k` packet contains a physical collision, its small `z` vectors lie on one rational line.  Let the primitive positive direction be

```text
(u,v),
gcd(u,v)=1,
```

so every physical pair in that packet satisfies

```text
(z_1,z_2)=t*(u,v)                                   (7.1)
```

for some positive integer `t`.

Therefore

```text
v*z_1=u*z_2.                                        (7.2)
```

Using the exact identity

```text
z_i=2*x_i*y_i/g_i,
```

we obtain

```text
boxed:
v*g_2*x_1*y_1
 =u*g_1*x_2*y_2.                                    (7.3)
```

So the enormous determinant `k^2` does not produce an additional independent density factor after a short vector exists.  It rigidifies the collision to a fixed multiplicative product ratio.

For a fixed first state and fixed oriented packet, (7.3) leaves only divisor-many possibilities for `(x_2,y_2)`:

```text
B^o(1).
```

This is useful pointwise rigidity, but it is not average sparsity.

---

## 8. Why the eight divisibilities do not yet beat 7/8

The tempting but invalid argument would be

```text
8 large square moduli
-> multiply 8 independent local densities
-> fixed-power saving.
```

Sections 4--7 show why this is wrong.

After the legal primewise orientation refinement:

- the four `xi` conditions are one four-dimensional CRT lattice;
- the four `k` conditions are one two-dimensional CRT lattice;
- inside the physical boxes, the `k` lattice collapses to one rational product direction;
- after fixing a first state, the remaining second-state factorizations are only `B^o(1)`, but they need not be zero.

This recovers the already-known pointwise recurrence scale

```text
partner multiplicity <= B^o(1),
```

and therefore still permits an abstract matching in which a positive proportion of the `B^(7/8+o(1))` first states has one partner.

Thus

```text
boxed:
RAW_DUAL_CRT_RANK_REDUCTION_BEATS_7_8=false.         (8.1)
```

No whole-family exponent improvement is promoted.

---

## 9. The exact remaining average theorem

For one balanced endpoint orientation packet `Pi`, write

```text
Lambda_xi(Pi),
Lambda_k(Pi)
```

for the two lattices above and define the compatible short-vector set

```text
C(Pi)
 = {
     (x_1,y_1,x_2,y_2):
       physical masks hold,
       root vector in Lambda_xi(Pi),
       (2*x_1*y_1/g_1, 2*x_2*y_2/g_2) in Lambda_k(Pi)
   }.
```

The new receiver is

```text
BalancedDualCRTShortVectorEnergy:

sum over balanced physical endpoint packets Pi
of the off-diagonal compatible short-vector mass #C(Pi),
with each physical pair charged once.
```

The required theorem is

```text
boxed target:
BalancedDualCRTShortVectorEnergy
 << B^(7/8-delta+o(1))                              (9.1)
```

for some fixed `delta>0`.

Equivalently, one must prove that the simultaneous existence of

```text
- an xi-lattice short root vector at scale B^(1/16), and
- a compatible k-lattice short product vector at scale B^(1/8)
```

is power-sparse **on average over the physical packets**.

Pointwise geometry of numbers alone cannot supply this average scarcity.

---

## 10. Relation to quadratic large sieve / toolbox / tH

Merged tH14 R2 proves a quadratic-large-sieve product-row adapter, but it does not prove physical squareclass anti-coherence.  Merged toolbox-aq/ar forbids promoting that adapter into a different positive collision receiver without an exact coefficient-space bridge.

The current s7-21 object is already an exact positive physical-pair CRT object.  Replacing it by a Jacobi-symbol density would discard the squared-modulus short-vector information and would not yield a fixed-power saving.

Accordingly no new tH/supervisor line is required at this stage:

```text
TH16_NEEDED_BY_S7_21=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

A future auxiliary theorem is justified only if it estimates `BalancedDualCRTShortVectorEnergy` on this exact packet space rather than an analogous Gaussian coefficient space.

---

## 11. Quantitative ledger

Endpoint labels:

```text
xi exponent = 3/4,
k exponent  = 1.
```

Root scales:

```text
x_i,y_i exponent = 1/16,
z_i exponent     = 1/8.
```

Exact lattice determinants:

```text
det Lambda_xi exponent = 2*(3/4)=3/2,
det Lambda_k  exponent = 2.
```

Physical box determinant ceilings:

```text
four x/y roots: 4*(1/16)=1/4,
two z roots:    2*(1/8)=1/4.
```

Gaps:

```text
xi CRT determinant gap = 3/2-1/4=5/4,
k  CRT determinant gap = 2-1/4=7/4.
```

Short-rank conclusions:

```text
xi root short rank <=3,
k z short rank <=1.
```

No new unconditional exponent:

```text
V(B) << B^(7/8+o(1)).
```

---

## 12. Next receiver

Stage14-s7-22 should attack

```text
BalancedDualCRTShortVectorEnergy
```

as an **average short-vector existence problem**, not as eight independent congruence densities.

The preferred first attempt is to charge a short `k` direction to its primitive product ratio `(u:v)` and then count which balanced `xi` orientation lattices admit a physical root vector on the bilinear surface

```text
v*g_2*x_1*y_1=u*g_1*x_2*y_2.
```

The rank-3/tangent-resonance case of the `xi` lattice should be separated explicitly from the generic rank-2-or-less case before any Cauchy or auxiliary-prime average.

---

## Stage boundary

```text
STAGE14_S7_21=COMPLETE_PRIMEWISE_ORIENTATION_LINEARIZATION_AND_DUAL_CRT_SHORT_VECTOR_REDUCTION
MERGED_S7_20_IMPORTED=true
MERGED_S7_19_IMPORTED=true
MERGED_4CE_PRIMEWISE_RESIDUE_LOCK_IMPORTED=true
EIGHT_SQUARE_DIVISIBILITIES_INDEPENDENT_DENSITIES=false
PRIMEWISE_ORIENTATION_REFINEMENT_COST=B^o(1)
XI_ROOT_LINEAR_CRT_LATTICE_DEFINED=true
XI_ROOT_CRT_LATTICE_DETERMINANT=xi^2
K_Z_LINEAR_CRT_LATTICE_DEFINED=true
K_Z_CRT_LATTICE_DETERMINANT=k^2
FOUR_CD_ENDPOINT_XI_CRT_DETERMINANT_EXPONENT=3/2
FOUR_CD_ENDPOINT_K_CRT_DETERMINANT_EXPONENT=2
FOUR_CD_ENDPOINT_XI_ROOT_BOX_EXPONENT=1/4
FOUR_CD_ENDPOINT_K_Z_BOX_EXPONENT=1/4
XI_CRT_DETERMINANT_GAP_EXPONENT=5/4
K_CRT_DETERMINANT_GAP_EXPONENT=7/4
XI_ROOT_SHORT_VECTOR_RANK_MAX=3
K_Z_SHORT_VECTOR_RANK_MAX=1
K_RANK_ONE_FIXES_Z_RATIO=true
Z_TO_CANONICAL_PRODUCT_IDENTITY=z_i=2*x_i*y_i/g_i
FIXED_Z_RATIO_GIVES_BILINEAR_PRODUCT_EQUATION=true
RAW_DUAL_CRT_RANK_REDUCTION_BEATS_7_8=false
BALANCED_DUAL_CRT_SHORT_VECTOR_ENERGY_REQUIRED=true
BALANCED_DUAL_CRT_SHORT_VECTOR_ENERGY_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH16_NEEDED_BY_S7_21=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-s7-22
```
