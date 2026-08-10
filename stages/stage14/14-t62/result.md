# Stage14-t62 — matched orthogonal-rectangle Kummer frame reduction

## Purpose

Merged Stage14-t61 shows that the t60 polar/SVD shortcut is not zero-loss: taking the positive polar operator `|C_r|` creates unavoidable fixed-power leverage.  The live receiver is therefore the signed t59 rectangle sum

\[
\sum_{p\ne q}
\left|
\sum_j
\sum_{\pi\in A_j}
\sum_{V\in B_j}
K_{pq}(t(\pi),x(V))
\right|^2
\ll
P^2\sum_j |A_j||B_j|\,B^{o(1)}.
\tag{62.1}
\]

Stage14-t62 does not take an absolute value of the Kummer coefficient matrix and does not enlarge the physical support.  Instead it uses the exact orthogonality already proved in t59 to compress each Cartesian block to one normalized Hilbert--Schmidt basis vector.  This identifies the precise TT*/dual object that tH17 should test.

No analytic large-sieve estimate is proved here.  The gain is a strict reduction from an arbitrary operator-valued bilinear theorem to a matched block-average frame/Rayleigh bound.

---

## 1. Exact orthonormal basis carried by a t59 rectangle family

Fix one t59 family

\[
\mathcal R=\{A_j\times B_j\}_{j\in J},
\]

with pairwise-disjoint row projections `A_j` and pairwise-disjoint column projections `B_j`.  Put

\[
a_j=|A_j|,\qquad b_j=|B_j|,
\qquad m_j=a_jb_j.
\]

Define normalized row/column indicators

\[
u_j=\frac{1_{A_j}}{\sqrt{a_j}},
\qquad
v_j=\frac{1_{B_j}}{\sqrt{b_j}},
\tag{62.2}
\]

and the rank-one matrix

\[
E_j=u_jv_j^*.
\tag{62.3}
\]

Because the row sets are disjoint and the column sets are disjoint,

\[
\langle u_j,u_k\rangle=\delta_{jk},
\qquad
\langle v_j,v_k\rangle=\delta_{jk}.
\]

Therefore

\[
\boxed{
\langle E_j,E_k\rangle_{HS}=\delta_{jk}.
}
\tag{62.4}
\]

Thus every t59 family carries an exact Hilbert--Schmidt orthonormal basis indexed only by its rectangles.  No residue-class completion or spectral transform is involved.

The physical selector matrix of the family is

\[
W_{\mathcal R}
=\sum_j 1_{A_j}1_{B_j}^*
=\sum_j \sqrt{m_j}\,E_j.
\tag{62.5}
\]

Moreover

\[
W_{\mathcal R}v_j=\sqrt{m_j}\,u_j,
\qquad
W_{\mathcal R}^*u_j=\sqrt{m_j}\,v_j.
\tag{62.6}
\]

Hence (62.5) is already an exact singular-value decomposition of the selector matrix, with singular values

\[
\boxed{s_j=\sqrt{m_j}.}
\tag{62.7}
\]

In particular

\[
\boxed{
\|W_{\mathcal R}\|_{HS}^2
=\sum_j m_j
=:R_{\mathcal R},
}
\tag{62.8}
\]

which is exactly the selected physical mass.  There is no factor equal to the number of rectangles.

```text
T59_RECTANGLE_INDICATORS_HS_ORTHONORMAL=true
T59_SELECTOR_EXACT_SVD_PROVED=true
T59_SELECTOR_HS2_EQUALS_PHYSICAL_MASS=true
```

---

## 2. Normalize the signed Kummer trace rectangle-by-rectangle

For one ordered auxiliary pair `(p,q)`, let `K_{pq}` denote the signed physical Kummer matrix

\[
K_{pq}(\pi,V)=K_{pq}(t(\pi),x(V)).
\]

Define one scalar per rectangle:

\[
\boxed{
\kappa_{pq,j}
:=\langle E_j,K_{pq}\rangle_{HS}
=\frac1{\sqrt{m_j}}
\sum_{\pi\in A_j}
\sum_{V\in B_j}
K_{pq}(t(\pi),x(V)).
}
\tag{62.9}
\]

and the physical-mass vector

\[
z_j:=\sqrt{m_j}.
\tag{62.10}
\]

Then the complete family trace in (62.1) is exactly

\[
\boxed{
T_{\mathcal R}(p,q)
=\sum_j z_j\kappa_{pq,j}.
}
\tag{62.11}
\]

Also

\[
\boxed{\|z\|_2^2=R_{\mathcal R}.}
\tag{62.12}
\]

Thus all internal `(pi,V)` combinatorics of a t59 rectangle family have been compressed to one signed scalar `kappa_{pq,j}` per block and one canonical positive coefficient `z_j=sqrt(m_j)`.

The t61 signed rectangle receiver is therefore exactly the Rayleigh estimate

\[
\boxed{
\sum_{p\ne q}
|\langle z,\kappa_{pq}\rangle|^2
\ll
P^2\|z\|_2^2 B^{o(1)}.
}
\tag{62.13}
\]

No polar operator occurs anywhere in (62.9)--(62.13).

---

## 3. Exact TT* Gram formulation

Define the rectangle Gram matrix

\[
G_{jk}
:=\sum_{p\ne q}
\kappa_{pq,j}\overline{\kappa_{pq,k}}.
\tag{62.14}
\]

Then

\[
\sum_{p\ne q}|T_{\mathcal R}(p,q)|^2
=z^*Gz.
\tag{62.15}
\]

Therefore the exact current theorem is

```text
PhysicalMassVectorKummerRayleighBound
```

namely

\[
\boxed{
z^*Gz\ll P^2\,z^*z\,B^{o(1)},
\qquad z_j=\sqrt{|A_j||B_j|}.
}
\tag{62.16}
\]

This is strictly weaker than proving the full frame/operator bound

\[
\|G\|_{op}\ll P^2B^{o(1)}.
\tag{62.17}
\]

Stage14-t62 records this quantifier distinction explicitly: **the physical receiver needs one canonical positive mass vector, not arbitrary rectangle coefficients.**

```text
PHYSICAL_RECEIVER_EQUALS_MASS_VECTOR_RAYLEIGH_BOUND=true
FULL_RECTANGLE_FRAME_OPERATOR_BOUND_REQUIRED=false
```

A theorem proving (62.17) is legal and sufficient, but stronger than the exact demand.

---

## 4. Convenient sufficient dual theorem

For comparison with standard large-sieve/TT* technology, define the stronger frame inequality

\[
\sum_{p\ne q}
\left|\sum_j c_j\kappa_{pq,j}\right|^2
\ll P^2B^{o(1)}\sum_j|c_j|^2
\tag{62.18}
\]

for arbitrary coefficients `c_j`.

By Hilbert-space duality, (62.18) is equivalent to

\[
\boxed{
\sum_j
\left|
\sum_{p\ne q}d_{pq}\kappa_{pq,j}
\right|^2
\ll
P^2B^{o(1)}
\sum_{p\ne q}|d_{pq}|^2.
}
\tag{62.19}
\]

Substituting (62.9) gives the exact block-average form

\[
\boxed{
\sum_j
\frac1{m_j}
\left|
\sum_{\pi\in A_j}
\sum_{V\in B_j}
\sum_{p\ne q}
 d_{pq}K_{pq}(t(\pi),x(V))
\right|^2
\ll
P^2B^{o(1)}\sum_{p\ne q}|d_{pq}|^2.
}
\tag{62.20}
\]

Call (62.20)

```text
MatchedRectangleProjectedKummerDualLargeSieve.
```

It is the natural theorem-shaped sufficient contract for tH17.  It only asks for the block-constant projection generated by the actual t59 matched rectangles.  It does **not** ask for a bound on every state-level coefficient vector or every operator-valued matrix packet.

---

## 5. The block projection itself is zero-loss

For an arbitrary function `F(pi,V)` on the union of the rectangles, orthonormality of `E_j` gives Bessel exactly:

\[
\boxed{
\sum_j
\frac1{m_j}
\left|
\sum_{(\pi,V)\in A_j\times B_j}F(\pi,V)
\right|^2
\le
\sum_j
\sum_{(\pi,V)\in A_j\times B_j}|F(\pi,V)|^2.
}
\tag{62.21}
\]

So the passage

```text
state function -> matched rectangle block averages
```

costs exactly zero fixed power.  The unresolved cancellation is entirely in the auxiliary family

\[
F_d(\pi,V)=\sum_{p\ne q}d_{pq}K_{pq}(t(\pi),x(V)).
\]

This matters for theorem matching: any ambient state-space dual large sieve would imply (62.20) immediately by (62.21), but tH16/t61 show that such broad ambient estimates are not presently available at zero loss.  Conversely, tH17 does not need to prove that stronger ambient theorem.

```text
MATCHED_BLOCK_PROJECTION_BESSEL_ZERO_LOSS=true
AMBIENT_STATE_SPACE_LARGE_SIEVE_REQUIRED=false
```

---

## 6. Why the t61 polar obstruction disappears from the statement

The t61 loss came from replacing the signed coefficient matrix by its positive polar absolute value before the outer auxiliary average.

Stage14-t62 never performs that operation.  The scalars

\[
\kappa_{pq,j}=\langle E_j,K_{pq}\rangle
\]

retain the full sign/phase of the original Kummer kernel for each `(p,q)` and each matched physical block.  TT* is taken only after these signed block traces are formed.

Hence the lower bound

\[
a_t^*|C_r|a_t=\Omega(r^{1/4})
\]

from t61 does not insert any factor into (62.13) or (62.20).

This does not prove cancellation; it merely ensures that the known polar fixed-power loss is absent from the new contract.

```text
POLAR_ABSOLUTE_VALUE_USED=false
T61_POLAR_FIXED_POWER_LOSS_INSERTED=false
SIGNED_KUMMER_PHASE_PRESERVED=true
```

---

## 7. Frozen t59 compatibility

The merged frozen t59 family has

```text
invisible states                    419
fixed (U,eps,k) packets               8
exact rectangles                    127
energy-balanced families            109
max rectangles per family             4
```

The t62 audit reconstructs the same physical rectangle families from the merged t59 machinery and checks, family by family:

- row projections are disjoint;
- column projections are disjoint;
- normalized rectangle matrices are Hilbert--Schmidt orthonormal;
- selector SVD singular values are exactly `sqrt(a_j*b_j)`;
- selector Hilbert--Schmidt mass is exactly the physical edge count;
- block-average Bessel inequality is exact for deterministic integer test functions.

No finite injectivity claim is promoted to an asymptotic theorem; the asymptotic identities follow directly from t59 orthogonality.

---

## 8. Updated minimal analytic hierarchy

The current hierarchy is now

```text
exact physical demand:
  PhysicalMassVectorKummerRayleighBound

stronger convenient sufficient theorem:
  MatchedRectangleProjectedKummerDualLargeSieve

still stronger, not required:
  full rectangle frame/operator norm bound
  ambient arbitrary-state same-modulus Kummer large sieve
```

This is a strict sharpening of t61's broad

```text
SignedOrthogonalRectangleKummerBilinearLargeSieve.
```

The physical route should not silently replace the first line by the stronger later lines unless a theorem naturally supplies them.

---

## 9. tH decision

`tH17` remains needed and is not yet consumed.

Its target should be sharpened from the broad signed-rectangle phrase to the pair

```text
PhysicalMassVectorKummerRayleighBound
MatchedRectangleProjectedKummerDualLargeSieve
```

with priority on the second because it matches standard TT*/dual large-sieve language.

The independent audit should test whether same-modulus bilinear/trace large sieve, TT*/dual large sieve, operator-valued large sieve, or a trace-function frame theorem can prove (62.20) **after the exact matched block projection**, without:

- replacing `K_{pq}` by `|C_{pq}|`;
- paying for the number of rectangles;
- promoting to the full ambient state space unnecessarily;
- separating the common `(p,q)` modulus between the two physical coordinates;
- pre-collapsing to squareclass coefficient energy.

No tH18 is needed at this stage.  The t main route remains unblocked.

```text
TH17_NEEDED=true
TH17_REQUESTED_OBJECT=MatchedRectangleProjectedKummerDualLargeSieve
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH17=false
```

---

## Locked boundary

```text
STAGE14_T62=COMPLETE_MATCHED_RECTANGLE_FRAME_AND_DUAL_PROJECTION_REDUCTION
MERGED_T61_IMPORTED=true
T59_RECTANGLE_INDICATORS_HS_ORTHONORMAL=true
T59_SELECTOR_EXACT_SVD_PROVED=true
T59_SELECTOR_HS2_EQUALS_PHYSICAL_MASS=true
SIGNED_RECTANGLE_TRACE_COMPRESSES_TO_ONE_SCALAR_PER_BLOCK=true
PHYSICAL_RECEIVER_EQUALS_MASS_VECTOR_RAYLEIGH_BOUND=true
FULL_RECTANGLE_FRAME_OPERATOR_BOUND_REQUIRED=false
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_PROVED=false
MATCHED_BLOCK_PROJECTION_BESSEL_ZERO_LOSS=true
AMBIENT_STATE_SPACE_LARGE_SIEVE_REQUIRED=false
POLAR_ABSOLUTE_VALUE_USED=false
T61_POLAR_FIXED_POWER_LOSS_INSERTED=false
SIGNED_KUMMER_PHASE_PRESERVED=true
PHYSICAL_MASS_VECTOR_KUMMER_RAYLEIGH_BOUND_PROVED=false
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH17_NEEDED=true
TH17_REQUESTED_OBJECT=MatchedRectangleProjectedKummerDualLargeSieve
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH17=false
NEXT=Stage14-t63 attack the matched block-average dual inequality directly; consume tH17 if available
```
