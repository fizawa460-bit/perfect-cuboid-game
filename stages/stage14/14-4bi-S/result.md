# Stage14-4bi-S — full edge-radical modulus and small-denominator core

## Purpose

Stage14-4bi-L closes the large edge-kernel route.  With

\[
d_0=\tau_0ab,\qquad d_1=\tau_1ac,\qquad d_2=\tau_2bc,
\]

where

\[
a\mid\operatorname{rad}_{\rm odd}(S),\quad
b\mid\operatorname{rad}_{\rm odd}(X),\quad
c\mid\operatorname{rad}_{\rm odd}(H),
\]

it proves that a large kernel gives either a composite-modulus incidence gain or a transfer to small denominator.  The nominal S-side input is therefore

```text
K=max(a,b,c) < B^kappa
OR
D < 2 B^upsilon.
```

The first point of this stage is that **small kernel is not actually the correct residual modulus obstruction**.  The same normalized packet equations used by 4bi-L imply congruences modulo the **entire odd radical of each Pythagorean leg**, independently of how the radical is split between the edge kernel and its complement.

The second point is that hypotenuses with genuinely small odd radical form a power-sparse set.  Hence the only serious S-side remainder is a radical-rich family in which the canonical global witness nevertheless occupies a short/small-denominator box.  Existing Stage14 inputs do not yet turn the resulting witness-layer lattice gain into a class-count power saving, because the post-local count is existential and the only available canonical-to-naive height transfer gives an unspecified polynomial box exponent `K_C`.

Thus 4bi-S removes `small kernel` as an intrinsic arithmetic obstruction and replaces it by one explicit analytic gate:

> **canonical-witness occupancy in radical-rich, small-denominator/short-variable boxes.**

No full `delta_post>0` is claimed here.

---

## 1. Imported exact packet

From merged s6-01 / 4bg,

\[
\tau_0ab u_0^2-\tau_1ac u_1^2=S^2D^2,
\tag{S.1}
\]

\[
\tau_2bc u_2^2-\tau_0ab u_0^2=X^2D^2,
\tag{S.2}
\]

and therefore

\[
\tau_2bc u_2^2-\tau_1ac u_1^2=H^2D^2.
\tag{S.3}
\]

The odd edge packets are pairwise coprime and supported on the three pairwise-coprime Pythagorean legs.

Stage14-4bi-L divides by the shared edge kernel and obtains

\[
\tau_0b u_0^2-\tau_1c u_1^2
 =a\left(\frac Sa\right)^2D^2,
\tag{S.a}
\]

\[
\tau_2c u_2^2-\tau_0a u_0^2
 =b\left(\frac Xb\right)^2D^2,
\tag{S.b}
\]

\[
\tau_2b u_2^2-\tau_1a u_1^2
 =c\left(\frac Hc\right)^2D^2.
\tag{S.c}
\]

These three identities are the only algebra needed below.

---

## 2. Full odd radical divides the normalized right-hand side

Put

\[
R_S=\operatorname{rad}_{\rm odd}(S),\qquad
R_X=\operatorname{rad}_{\rm odd}(X),\qquad
R_H=\operatorname{rad}_{\rm odd}(H).
\]

Because `a` is squarefree and `a|R_S`, write

\[
R_S=a q_S,
\qquad q_S=R_S/a.
\]

Every prime of `q_S` divides `S/a`, so

\[
q_S\mid S/a.
\]

Therefore

\[
R_S=a q_S\mid a(S/a)^2.
\]

The same argument gives

\[
R_X\mid b(X/b)^2,
\qquad
R_H\mid c(H/c)^2.
\]

Consequently (S.a)--(S.c) imply the exact full-radical congruences

\[
\boxed{
\tau_0b u_0^2\equiv\tau_1c u_1^2\pmod{R_S},
}
\tag{S.RS}
\]

\[
\boxed{
\tau_2c u_2^2\equiv\tau_0a u_0^2\pmod{R_X},
}
\tag{S.RX}
\]

\[
\boxed{
\tau_2b u_2^2\equiv\tau_1a u_1^2\pmod{R_H}.
}
\tag{S.RH}
\]

All coefficients are units modulo the relevant radical.  For example `a,b` are supported on `S,X`, hence are coprime to the odd radical of `H`; the powers of two in the `tau_i` are also units modulo `R_H`.

This proves:

```text
SMALL_KERNEL_IS_NOT_AN_INTRINSIC_SMALL_MODULUS_OBSTRUCTION.
```

Even if `c=1`, the H-edge still carries the full modulus `rad_odd(H)`.

---

## 3. Full-radical rectangle bound

Apply the composite squarefree line-cover lemma from 4bi-L to (S.RH).  Since `R_H` is odd and squarefree, the solution set modulo `R_H` is covered by at most

\[
2^{\omega(R_H)}
\]

projective congruence lines, each of lattice index `R_H`.  Hence for a dyadic rectangle

\[
u_1\asymp U_1,\qquad u_2\asymp U_2,
\]

we have

\[
\boxed{
N_H(U_1,U_2)
\ll_\epsilon
B^\epsilon
\left(
\frac{U_1U_2}{R_H}
+\min(U_1,U_2)+1
\right).
}
\tag{S.4}
\]

The analogous estimates hold with `(R_S,U_0,U_1)` and `(R_X,U_0,U_2)`.

Thus every packet has three canonical global-witness incidence moduli

```text
rad_odd(S), rad_odd(X), rad_odd(H),
```

not merely the selected edge kernels `a,b,c` or their largest prime factors.

In particular, the L/S split should no longer be interpreted as

```text
large kernel versus small kernel.
```

The genuine split is

```text
large usable leg radical / long witness variables
versus
radical-poor base or short canonical witness.
```

---

## 4. Radical-poor integers are power sparse

We record an elementary uniform lemma because it gives an actual **base-count** saving, unlike a packet-layer relative density.

### Lemma

For every fixed `rho>0` and `epsilon>0`,

\[
\#\{n\le B:\operatorname{rad}(n)\le B^\rho\}
\ll_{\rho,\epsilon}
B^{\rho+\epsilon}.
\tag{S.5}
\]

### Proof

For a squarefree integer `r`, integers with `rad(n)=r` have Dirichlet series

\[
\sum_{\operatorname{rad}(n)=r} n^{-s}
=
 r^{-s}\prod_{p\mid r}(1-p^{-s})^{-1}.
\]

For fixed `s>0`, Rankin's trick gives

\[
\#\{n\le B:\operatorname{rad}(n)=r\}
\le
B^s r^{-s}
\prod_{p\mid r}(1-p^{-s})^{-1}.
\]

For every fixed `s` and every `eta>0`, the standard bound

\[
C_s^{\omega(r)}\ll_{s,\eta}r^\eta
\]

absorbs the Euler factors.  Take `s=epsilon/2` and `eta=s/2`.  After summing over squarefree `r<=B^rho`, the remaining negative power of `r` can be discarded, giving

\[
\ll B^{\epsilon/2}B^\rho
\ll B^{\rho+\epsilon}.
\]

This proves (S.5).

### Pythagorean consequence

For a fixed odd hypotenuse `H`, the number of oriented primitive representations

\[
S^2+X^2=H^2
\]

is at most `2^{omega(H)+O(1)}=H^{o(1)}`.  The supported local/descent packet multiplicity is also `B^epsilon` by the closed s5/s6 state ledger.

Therefore

\[
\boxed{
\#\{\text{supported base/classes}:H\le B,\ R_H\le B^\rho\}
\ll_\epsilon B^{\rho+\epsilon}.
}
\tag{S.6}
\]

This is a genuine global counting statement.  For any fixed

\[
\rho<41/42,
\]

the radical-poor hypotenuse sector is already power-smaller than the current `B^(41/42+epsilon)` local majorant.

```text
RADICAL_POOR_HYPOTENUSE_SECTOR_GLOBALLY_SPARSE=true.
```

---

## 5. Radical-rich packets: the witness-layer gain

Assume now

\[
R_H\ge B^\rho.
\]

Let

\[
U_*=\max(U_1,U_2).
\]

From (S.4), relative to an unconstrained `U_1 U_2` rectangle, the H-edge witness layer gains

\[
\ll_\epsilon B^\epsilon
\left(
B^{-\rho}+U_*^{-1}+(U_1U_2)^{-1}
\right).
\]

Thus whenever

\[
U_*\ge B^\nu,
\]

the square-variable layer has a genuine factor

\[
\boxed{
B^{-\min(\rho,\nu)+\epsilon}.
}
\tag{S.7}
\]

This statement is stronger than the kernel-size split: it applies even to `a=b=c=1` provided the hypotenuse radical is large.

However, exactly as 4bi-L correctly warns, a relative lattice density in the auxiliary witness variables does **not** automatically multiply the already-proved `B^(41/42)` class count.  Stage14 currently counts whether a class possesses at least one global witness; it does not count an ambient uniform rectangle of witness variables with one point per cell.

Therefore (S.7) is a valid incidence theorem but not yet a theorem

\[
J_C(B)\ll B^{41/42-\delta}.
\]

---

## 6. Short radical-rich witness implies small denominator

There is nevertheless an exact transfer analogous to 4bi-L which makes the residual core smaller.

From (S.c),

\[
\frac{H^2}{c}D^2
=
\left|\tau_2b u_2^2-\tau_1a u_1^2\right|.
\]

Because

\[
a,b,c\le H,
\qquad |\tau_i|\le2,
\]

we obtain

\[
\frac{H^2}{c}D^2
\le4H U_*^2.
\]

Since `c<=H`, the left side is at least `H D^2`, hence

\[
\boxed{D\le2U_*.}
\tag{S.8}
\]

Consequently, if the radical-rich H-edge does not enter a long witness range and instead

\[
U_*<B^\nu,
\]

then automatically

\[
\boxed{D<2B^\nu.}
\tag{S.9}
\]

Thus the S-side complement may be reduced to

```text
(A) radical-poor H: R_H < B^rho, already globally sparse;
(B) radical-rich and long witness: R_H >= B^rho, U_* >= B^nu,
    with a proved witness-layer B^(-min(rho,nu)+eps) incidence gain;
(C) radical-rich short core: R_H >= B^rho, U_* < B^nu, D < 2B^nu.
```

The same construction is available on the S and X edges.

---

## 7. Why small denominator alone is not yet a power-saving theorem

The denominator `D` in s6-01 is the denominator of the **maximally 2-halved nonzero Kummer representative**, not the physical space diagonal.  The physical point supplied by s3 has explicit bounded coordinates, but repeated halving is used to reach a nonzero class in `E_F(Q)/2E_F(Q)`.

Canonical height decreases under halving, but the available canonical/naive comparison only yields

\[
|A|\le B^{K_C},\qquad D^2\le B^{K_C}
\]

for some fixed, unspecified family exponent `K_C`.

Therefore there is currently no valid deduction of the form

```text
D < B^nu
=>
class density < B^(-delta).
```

Likewise, simply counting all integral `(u_0,u_1,u_2,D)` in the generic `B^(K_C)` box is far too wasteful and can be much larger than the ambient base count.

This identifies the exact missing analytic bridge:

> one needs an **anisotropic canonical-witness occupancy theorem** which counts existence of a bounded-height global point on the moving two-quadric packet, uniformly in the radical congruence lattice and with a cost compatible with the physical `41/42` base exponent.

This is different from another local sieve theorem and different from a per-fixed-curve determinant-method bound.

---

## 8. Canonical representative removes multiplicity ambiguity but not the count

For bookkeeping, each globally soluble class counted by `J_C(B)` may be assigned one canonical witness by the deterministic rule:

1. minimize canonical height among non-torsion representatives in the class;
2. then minimize naive `Z` height;
3. then use a fixed lexicographic sign/coordinate tie-break.

Northcott finiteness makes this selection well-defined inside the fixed height window.

This converts the existential projection into an injection

\[
(F,\xi)\hookrightarrow
(F,\xi,u_0,u_1,u_2,D).
\]

But it does not by itself prove a power saving: a theorem is still required to count these canonical selected points inside the radical congruence lattices.

Accordingly

```text
CANONICAL_WITNESS_SELECTION_AVAILABLE=true
CANONICAL_WITNESS_OCCUPANCY_POWER_SAVING_PROVED=false.
```

---

## 9. S-side conclusion and handoff to 4bj

The nominal `small kernel` branch has been structurally eliminated as a modulus issue.  The exact new picture is:

1. **radical-poor hypotenuses** are globally sparse by (S.6);
2. **radical-rich, long-witness packets** satisfy a full-radical CRT lattice restriction with the sectoral gain (S.7);
3. **radical-rich, short-witness packets** lie in the explicit small-denominator core (S.9).

What is *not* yet proved is the conversion of item 2 or item 3 into a uniform class-count power saving after the existential/canonical-witness projection.

Therefore the S-side exponent remains

```text
delta_S > 0 : NOT YET PROVED.
```

The correct 14-4bj task is no longer to combine a large-kernel estimate with a vague smooth-kernel estimate.  It should combine L and S into one radical-based decomposition, delete `small kernel` from the obstruction list, and freeze the single remaining post-local theorem target:

```text
RADICAL_RICH_CANONICAL_WITNESS_OCCUPANCY
with explicit small-D/short-variable core.
```

---

## Boundary

```text
STAGE14_4BI_S=FULL_EDGE_RADICAL_MODULUS_AND_SMALL_DENOMINATOR_CORE_ISOLATED
STAGE14_4BI_L_IMPORTED=true
FULL_ODD_EDGE_RADICAL_CONGRUENCES_PROVED=true
FULL_ODD_EDGE_RADICAL_RECTANGLE_BOUND_PROVED=true
SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false
RADICAL_POOR_INTEGER_COUNT_BOUND=B^(rho+epsilon)
RADICAL_POOR_HYPOTENUSE_SECTOR_GLOBALLY_SPARSE=true
RADICAL_RICH_LONG_WITNESS_LAYER_SAVING=B^(-min(rho,nu)+epsilon)
RADICAL_RICH_SHORT_WITNESS_IMPLIES_D_LE_2_USTAR=true
RADICAL_RICH_SHORT_CORE=D<2B^nu
CANONICAL_WITNESS_SELECTION_AVAILABLE=true
SMALL_DENOMINATOR_ALONE_POWER_SAVING_PROVED=false
EXISTENTIAL_PROJECTION_TO_CLASS_SAVING_PROVED=false
SHARP_ANISOTROPIC_CANONICAL_WITNESS_BOX_PROVED=false
CANONICAL_WITNESS_OCCUPANCY_POWER_SAVING_PROVED=false
S_ROUTE_GLOBAL_POSITIVE_SAVING_PROVED=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bj assemble 4bi-L and 4bi-S into a single radical-based post-local decomposition, remove small-kernel from the obstruction list, and freeze the radical-rich canonical-witness occupancy theorem as the unique remaining quantitative gate
```
