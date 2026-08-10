# Stage14-t38 — moving canonical-prime elliptic packets and the critical sqrt-ell strip

## Purpose

Stage14-t37 proved that after fixing one canonical super-square-root prime `ell`, the entire norm-index problem has the uniform power-saving bound

\[
R_\ell(B)\ll (B/\ell)^{5/6}B^{o(1)}.
\]

The remaining obstruction was the summation over the moving canonical prime itself, especially the regime where `B/ell` is small.

Stage14-t38 changes the order of summation.  Instead of fixing `ell`, fix the **descended Gaussian cofactors** `U,V` and let the canonical Gaussian prime

\[
\pi\bar\pi=\ell
\]

move.  In this ordering the Stage14 target equation becomes a genus-one quartic in the slope of `pi`.  The same uniform bounded-height mechanism already used in t22, t36 and t37 then shows that one fixed descended packet admits only `B^{o(1)}` moving canonical primes.

This gives a global

\[
B^{1/2+o(1)}
\]

bound for the whole super-square-root packet family and, more importantly, a genuine fixed power saving whenever

\[
\ell\ge B^{1/2+\eta}
\]

for any fixed `eta>0`.

Thus the moving-prime problem is reduced to the **critical square-root strip**

\[
\ell=B^{1/2+o(1)}.
\]

The stage also corrects an important literature boundary.  Although the general Friedlander--Iwaniec--Mazur--Rubin spin theorem is not a degree-two theorem, a classical degree-two Gaussian spin theorem over `Z[i]` already exists in Friedlander--Iwaniec's 1998 work.  It is structurally relevant to the remaining critical strip.  However the Stage14 moving packet is not itself their Jacobi--Kubota spin, so their prime-spin theorem cannot yet be quoted as a direct solution.

No global `A_{1,1}` or `T=o(sqrt(B))` claim is made in t38.

## 1. Descended variables and the moving canonical prime

Write the actual direction Gaussian integer as

\[
A_c=a+ib=\pi U,
\qquad N(U)=m,
\qquad N(\pi)=\ell.
\]

For the cover complex number `P_c=p+iq`, the t32/t37 branches are

```text
visible same orientation:      P_c = pi * V
visible opposite orientation:  P_c = bar(pi) * V
invisible:                     P_c = V
```

up to one of the four Gaussian units, which can be absorbed into `V` at bounded cost.

Recall the exact identities

\[
A_c\overline{P_c}=g_4+i g_1,
\qquad
A_cP_c=-g_3+i g_2,
\]

and therefore

\[
\boxed{
F=g_1g_2g_3g_4
=-\Psi(A_c\overline{P_c})\Psi(A_cP_c),
}
\tag{38.1}
\]

where

\[
\Psi(z)=\Re(z)\Im(z).
\]

For a fixed Gaussian coefficient `c`, put

\[
\Psi_c(z)=\Re(cz)\Im(cz),
\qquad
\Phi_c(z)=\Re(cz^2)\Im(cz^2).
\tag{38.2}
\]

## 2. Exact moving-prime factorization: invisible branch

In the invisible branch `P_c=V`.  Hence

\[
A_c\overline{P_c}
=\pi U\bar V,
\qquad
A_cP_c=\pi UV.
\]

Set

\[
C_1=U\bar V,
\qquad C_2=UV.
\]

Then (38.1) becomes the exact identity

\[
\boxed{
F=-\Psi_{C_1}(\pi)\Psi_{C_2}(\pi).
}
\tag{38.3}
\]

If `pi=r+is` and `C=x+iy`, then

\[
\Psi_C(\pi)
=(xr-ys)(yr+xs).
\tag{38.4}
\]

Thus each factor is a product of two rational linear forms in `(r,s)`, and the moving target

\[
W^2=F
\]

is a binary quartic with four rational linear branch factors.

These four factors are distinct on every physical non-torsion invisible state.  Indeed, a common line between the factors attached to `C1` and `C2` would imply

\[
\frac{C_2}{C_1}
=\frac{V}{\bar V}\in \mathbf R\cup i\mathbf R.
\]

For `V=p+iq`, the real case forces `pq=0`, while the purely imaginary case forces `p^2=q^2`.  The physical interval has `p,q>0`, and the non-torsion branch has `p\ne q`, so neither is possible.

Consequently the projective curve in the slope `r/s` is a smooth genus-one curve with full rational `2`-torsion.

## 3. Exact moving-prime factorization: visible branches

Assume first that, after absorbing a Gaussian unit into `V`,

\[
P_c=\pi V.
\]

Then

\[
A_c\overline{P_c}=\ell U\bar V,
\qquad
A_cP_c=\pi^2UV.
\]

Therefore

\[
\boxed{
F
=-\ell^2\,\Psi(U\bar V)\,\Phi_{UV}(\pi).
}
\tag{38.5}
\]

Similarly, in the opposite orientation `P_c=bar(pi)V`,

\[
\boxed{
F
=-\ell^2\,\Psi(UV)\,\Phi_{U\bar V}(\pi).
}
\tag{38.6}
\]

The factor `ell^2` is a rational square and is irrelevant to the target squareclass.

For `c=u+iv`, the slope form of the moving quartic is exactly

\[
s^{-4}\Phi_c(r+is)
=
\bigl(u(x^2-1)-2vx\bigr)
\bigl(v(x^2-1)+2ux\bigr),
\qquad x=r/s.
\tag{38.7}
\]

The two rational quadratics are individually separable because both have discriminant

\[
4N(c)>0,
\]

and they cannot have a common projective root: simultaneous vanishing would say that both real and imaginary parts of `c(r+is)^2` vanish for a nonzero projective `(r,s)`.

Hence the visible moving-prime target is again a smooth genus-one quartic.  The rational factorization into the two quadratics supplies a rational `2`-torsion divisor.

## 4. Uniform moving-prime multiplicity for one descended packet

Fix `U,V`, the branch/orientation label, and all finite unit/local states.  Suppose the packet has at least one target moving prime `pi0`.  That target point supplies a rational point on the corresponding genus-one quartic, so the curve becomes an elliptic curve over `Q`.

Sections 2--3 provide rational `2`-torsion uniformly.  The coefficients are polynomial expressions in `U,V`, and in the super-square-root region all descended norms and all physical coordinates lie in a `B^{O(1)}` height window.  The moving prime itself satisfies `N(pi)=ell<=B^{O(1)}`.

Therefore the t22 uniform bounded-height theorem applies exactly as it did to the collision twists in t36/t37.  It yields

\[
\boxed{
\#\{\pi:\text{fixed descended packet is a Stage14 target}\}
\le B^{o(1)}.
}
\tag{38.8}
\]

A primitive Gaussian-prime slope determines the Gaussian prime up to only the bounded unit/conjugation choices, so no extra scale multiplicity is hidden in (38.8).

This estimate does not use primality analytically; it bounds all integral/rational points in the relevant height window and hence is valid a fortiori for Gaussian primes.

## 5. Count the descended packets before summing over ell

The super-square-root physical scale gives

\[
\frac{\varepsilon\ell m\delta}{2}\le B,
\qquad \ell>2\sqrt B.
\]

Hence

\[
\boxed{m\delta\ll \sqrt B.}
\tag{38.9}
\]

More generally, in a range `ell>=L`, put

\[
Y=\frac BL.
\]

Then every state in that range has

\[
m\delta\ll Y.
\]

For fixed `m,delta`, the divisor parameter `k` satisfies

\[
k\mid\varepsilon m,
\qquad n=k\delta.
\]

The number of possible primitive Gaussian representatives satisfies the standard soft bounds

\[
r_2(m),r_2(n),\tau(m)=B^{o(1)}.
\]

Therefore the number of descended packets is

\[
\begin{aligned}
\ll B^{o(1)}
\sum_{m\delta\ll Y}1
&\ll Y\log(2Y)B^{o(1)}\\
&=YB^{o(1)}.
\end{aligned}
\]

Combining this with (38.8),

\[
\boxed{
R_{\ell\ge L}^{\rm super}(B)
\ll \frac BL B^{o(1)}.
}
\tag{38.10}
\]

At the full super-square-root threshold `L=2sqrt(B)`, this gives

\[
\boxed{
R_{\rm super}(B)\ll B^{1/2+o(1)}.
}
\tag{38.11}
\]

This reaches the square-root exponent globally but does not yet give the required little-oh.

For every fixed `eta>0`, however,

\[
L=B^{1/2+\eta}
\]

gives the genuine power saving

\[
\boxed{
R_{\ell\ge B^{1/2+\eta}}^{\rm super}(B)
\ll B^{1/2-\eta+o(1)}.
}
\tag{38.12}
\]

Thus all canonical primes separated from `sqrt(B)` by a fixed power are closed.

## 6. The remaining critical strip

The only moving-prime region not closed by (38.12) is

\[
\boxed{
\ell=B^{1/2+o(1)}.
}
\tag{38.13}
\]

Equivalently, the descended cofactor budget is also of square-root size:

\[
B/\ell=B^{1/2+o(1)}.
\]

This is a balanced two-dimensional regime: the canonical Gaussian prime and the descended Gaussian cofactors have comparable polynomial size.  Pointwise elliptic-packet multiplicity reaches exactly the global `B^{1/2+o(1)}` barrier here, so a genuine **bilinear average across packets and primes** is needed.

## 7. Correct degree-two Gaussian-spin literature boundary

The relevant degree-two technology already exists in the classical paper

John Friedlander and Henryk Iwaniec,
*The polynomial X^2+Y^4 captures its primes*,
Annals of Mathematics 148 (1998), 945--1040; arXiv:math/9811185.

For a rational prime

\[
p=r^2+s^2
\]

with `r` odd, their Theorem 2 proves

\[
\boxed{
\sum_{r^2+s^2=p\le x}
\left(\frac{s}{r}\right)
\ll x^{76/77}.
}
\tag{38.14}
\]

They state that the same estimate survives restriction of the Gaussian prime `r+is` to a fixed sector and a fixed arithmetic progression.

More structurally, their Section 20 defines the Jacobi--Kubota symbol `[z]` and proves the twisted multiplier rule

\[
\boxed{
[wz]=\varepsilon[w][z]\left(\frac zw\right),
}
\tag{38.15}
\]

where the last factor is the real Dirichlet symbol in the Gaussian domain.  Section 21 then develops nontrivial bilinear estimates for sums

\[
\sum_w^*\sum_z
\alpha_w\beta_z
\left(\frac zw\right).
\tag{38.16}
\]

Thus t37's concern about the general degree-`>=3` spin theorem does **not** mean that degree two lacks a spin method.  The original Friedlander--Iwaniec Gaussian-spin machinery is exactly degree two.

## 8. Why Friedlander--Iwaniec does not yet close Stage14

The Stage14 moving packet is nevertheless not the single Jacobi--Kubota spin `[pi]`.

Equations (38.3), (38.5), and (38.6) show that the target is a squareclass condition on

```text
invisible:       Psi_C1(pi) * Psi_C2(pi)
visible:         constant * Phi_C(pi)
```

which is a quartic polynomial trace in the coordinates of `pi`.

After introducing an auxiliary square-sieve prime `lambda`, the local factor is of the form

\[
\chi_\lambda(G_{U,V}(\pi)),
\]

with fixed auxiliary modulus `lambda`.  By contrast, the Friedlander--Iwaniec spin is the internal Jacobi symbol whose modulus is a coordinate/norm attached to the moving Gaussian integer itself, and the bilinear kernel produced by their multiplier rule is the Gaussian Dirichlet symbol `(z/w)`.

Therefore

\[
\boxed{
\text{FI Gaussian spin is the right structural technology, but direct theorem substitution is not proved.}
}
\tag{38.17}
\]

The missing transfer is now precise: one must transform the critical-strip Stage14 quartic square-sieve correlation into a Type-I/Type-II sum with a Gaussian Dirichlet-symbol kernel of the form (38.16), or prove an equivalent bilinear prime-trace estimate directly.

## 9. Frozen finite audit

The t36 frozen population

```text
B=10000, a,b,p,q<=40
```

contains 1120 super-square-root states.  t38 reconstructs the canonical Gaussian prime from

\[
\pi=(a+ib)/U
\]

and checks the exact moving-prime formulas state by state.

The audit verifies:

```text
moving-prime exact factorization checks        1120
visible moving-quartic checks                   282
invisible four-distinct-linear-factor checks    838
```

For visible states the Gaussian unit relating the physical cover descent to `pi` or `bar(pi)` is absorbed before testing (38.5)--(38.6).

These are algebraic diagnostics.  The asymptotic multiplicity theorem is the bounded-height argument in Section 4.

## Boundary

```text
STAGE14_T38=COMPLETE_MOVING_PRIME_ELLIPTIC_PACKET_BOUND_AND_CRITICAL_STRIP_REDUCTION
CLASSICAL_QI_GAUSSIAN_SPIN_THEOREM_IDENTIFIED=true
GENERAL_DEGREE_GE3_SPIN_THEOREM_NEEDED=false
STAGE14_PACKET_EQUALS_FI_JACOBI_KUBOTA_SPIN=false
MOVING_PRIME_PACKET_FACTORIZATION_EXACT=true
MOVING_PRIME_TARGET_CURVE_GENUS_ONE=true
MOVING_PRIME_PACKET_MULTIPLICITY=B^o(1)
GLOBAL_SUPER_SQRT_PACKET_BOUND=B^(1/2+o(1))
LARGE_ELL_AWAY_FROM_SQRT_POWER_SAVING_PROVED=true
CRITICAL_SQRT_ELL_STRIP_REMAINS=true
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t39 treat the critical ell=B^(1/2+o(1)) strip by converting the Stage14 quartic square-sieve correlations into a genuine Gaussian Dirichlet-symbol Type-I/II bilinear form of the Friedlander-Iwaniec kind, or prove the exact obstruction to that transfer
```
