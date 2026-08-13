# Stage14-4bh — two-quadric genus-one geometry and the first direct incidence split

## Result

Merged Stage14-4bg reduced the selected post-local global-small-point route to the exact bounded witness system

\[
Y^2=A(A-S^2D^2)(A+X^2D^2),\qquad S^2+X^2=H^2,
\]

and, after fixing a signed squarefree kernel state,

\[
d_0u_0^2-d_1u_1^2=S^2D^2,
\]
\[
d_2u_2^2-d_0u_0^2=X^2D^2.
\]

Stage14-4bh determines the exact geometry of this fixed-state incidence and proves the first genuinely post-local congruence saving on the large-kernel-prime sector.

The main conclusions are:

1. the fixed-state projective incidence is a smooth complete intersection of two quadrics in `P^3`, hence a geometrically smooth genus-one curve;
2. torsion and coordinate-boundary loci are finite, not positive-dimensional accumulating components;
3. eliminating `u0` gives one smooth ternary conic plus one square-lift condition, equivalently a double cover of the conic branched at four geometric points;
4. every odd kernel prime belongs to exactly one of the three factor-pair edges `(01),(02),(12)`, supported respectively on `S,X,H`;
5. after dividing the corresponding difference equation by such a kernel prime `ell`, every witness lies on at most two linear congruence classes in the incident square-variable pair;
6. on a dyadic box this gives an exact lattice-count gain

```text
# incident pairs
  << U_i U_j / ell + min(U_i,U_j) + 1.
```

Thus whenever

```text
ell >= B^eta
and
max(U_i,U_j) >= B^eta,
```

the incident pair sector gains `B^(-eta)` relative to the unrestricted pair box, up to constants.

This is the first direct post-local **sectoral** power saving proved on the 14-4 main route. It is not yet a complete bound for `J_C(B)`: classes whose odd kernel has no large prime, and boxes in which every square variable incident to the available large kernel prime is too short, remain open. In addition, the generic polynomial coordinate bound from 4bg is not exponent-sharp enough to turn a fixed-curve determinant estimate into a uniform `delta_post>0` for the full moving family.

Accordingly

```text
DIRECT_POST_LOCAL_LARGE_KERNEL_SECTOR_SAVING_PROVED=true
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
```

for the full family.

---

## 1. Fixed packet equations

Write

\[
Q_1=d_0u_0^2-d_1u_1^2-S^2D^2,
\]
\[
Q_2=d_2u_2^2-d_0u_0^2-X^2D^2.
\]

Here `d0,d1,d2` are nonzero signed squarefree integers and `S,X,H` are the nonzero legs/hypotenuse of a primitive Pythagorean base.

The projective fixed-packet curve is

\[
C_{F,d}: Q_1=Q_2=0\subset \mathbf P^3_{[u_0:u_1:u_2:D]}.
\]

For a non-torsion witness in primitive affine coordinates we have

```text
D>0,
u0*u1*u2 != 0.
```

Indeed `u_i=0` means one of

```text
A=0,
A-S^2D^2=0,
A+X^2D^2=0,
```

which is exactly an `x`-coordinate of rational 2-torsion on

\[
W^2=Z(Z-S^2)(Z+X^2).
\]

The maximal-halving construction used upstream chooses a non-torsion nonzero mod-2 class, so these points are excluded from the counted post-local witness set.

---

## 2. Exact pencil determinant

Consider the pencil

\[
\lambda Q_1+\mu Q_2.
\]

In coordinates `(u0,u1,u2,D)` its diagonal matrix has coefficients

\[
d_0(\lambda-\mu),\quad
-\lambda d_1,\quad
\mu d_2,\quad
-(\lambda S^2+\mu X^2).
\]

Therefore

\[
\boxed{
\det(\lambda Q_1+\mu Q_2)
=d_0d_1d_2\,\lambda\mu(\lambda-\mu)(\lambda S^2+\mu X^2).
}
\]

The four singular pencil parameters are

\[
[0:1],\quad[1:0],\quad[1:1],\quad[-X^2:S^2].
\]

They are pairwise distinct over characteristic zero because `S,X` are nonzero and

\[
S^2+X^2=H^2\ne0.
\]

Equivalently, the binary quartic root discriminant is nonzero; up to a nonzero scalar its square of pairwise determinants contains

\[
S^4X^4H^4.
\]

The standard pencil criterion for an intersection of two quadrics in `P^3` therefore gives

\[
\boxed{C_{F,d}\text{ is a smooth genus-one complete intersection}.}
\]

So the post-local witness variety does **not** hide a line, rational component, or singular conic component that could account for a large exceptional population.

---

## 3. Boundary loci are zero-dimensional

Each coordinate hyperplane cuts the smooth curve in finitely many geometric points.

For example, on `u0=0`,

\[
-d_1u_1^2=S^2D^2,
\qquad
d_2u_2^2=X^2D^2.
\]

Since `D=0` would force all coordinates to vanish, `D!=0` on this hyperplane section, and the two ratios `u1/D`, `u2/D` each have at most two geometric choices. Thus `u0=0` contributes at most four geometric points. The same argument applies to `u1=0`, `u2=0`, and the projective boundary `D=0`.

Hence

```text
POSITIVE_DIMENSIONAL_TORSION_OR_COORDINATE_BOUNDARY=false.
```

Any determinant/square-sieve argument may remove these loci explicitly without losing a positive-dimensional component.

---

## 4. Eliminate one square variable exactly

Adding the two equations eliminates `u0`:

\[
\boxed{
d_2u_2^2-d_1u_1^2=H^2D^2.
}
\]

Call this ternary conic `K_{F,d}`. Since `d1,d2,H` are nonzero, it is a smooth conic over `Qbar`.

The forgotten variable is recovered from

\[
\boxed{
d_0u_0^2=d_1u_1^2+S^2D^2.
}
\]

Thus `C_{F,d}` is a degree-two cover of `K_{F,d}`. The branch divisor is obtained by setting `u0=0`, hence

\[
d_1u_1^2=-S^2D^2,
\qquad
d_2u_2^2=X^2D^2,
\]

which consists of four geometric points. This gives a second exact genus-one description: a double cover of a conic branched at four points.

If the conic is rationally soluble, one may parameterize it and the remaining square-lift becomes a binary quartic square equation. However, choosing such a rational parameterization uniformly is itself a global-solubility issue; using an unknown witness as the base point would be circular. Therefore 4bh does not claim a uniform quartic parameterization before the global point is counted.

---

## 5. Odd kernel primes form three exact edges

Let

\[
G_0=A,
\quad G_1=A-S^2D^2,
\quad G_2=A+X^2D^2.
\]

Because `G0*G1*G2` is a square, for every odd prime the parity vector

\[
(v_p(G_0),v_p(G_1),v_p(G_2))\pmod2
\]

has even Hamming weight. Hence a prime entering the signed squarefree kernel occurs in exactly two of `d0,d1,d2`.

Merged 4bg proved the pairwise odd gcd supports

```text
(0,1) -> S,
(0,2) -> X,
(1,2) -> H.
```

Therefore the odd kernel parts factor exactly as

\[
\boxed{
d_0^{(odd)}=ab,\qquad
d_1^{(odd)}=ac,\qquad d_2^{(odd)}=bc,}
\]

with

\[
a\mid\operatorname{rad}_{odd}(S),\qquad
b\mid\operatorname{rad}_{odd}(X),\qquad
c\mid\operatorname{rad}_{odd}(H).
\]

For a primitive Pythagorean triple the odd supports of `S,X,H` are pairwise disjoint, so `a,b,c` are pairwise coprime.

The sign and 2-adic factors may be retained in fixed bounded packets and do not affect the odd-prime argument below.

---

## 6. A kernel edge prime gives at most two congruence lines

Let `ell` be an odd prime appearing in one of the three edge kernels.

### S-edge: `ell|a`

Then `ell|d0,d1,S`, with `v_ell(d0)=v_ell(d1)=1`. Write

\[
d_0=\ell d_0',\qquad d_1=\ell d_1'.
\]

Divide `Q1=0` by `ell`. Since `ell^2|S^2`, reduction modulo `ell` gives

\[
\boxed{d_0'u_0^2\equiv d_1'u_1^2\pmod\ell.}
\]

Both coefficients are units modulo `ell`. The solution set is either only the common zero residue or the union of at most two lines

\[
u_0\equiv \pm r u_1\pmod\ell.
\]

### X-edge: `ell|b`

Likewise, dividing the second difference equation by `ell` gives

\[
\boxed{d_2'u_2^2\equiv d_0'u_0^2\pmod\ell,}
\]

again at most two lines in `(u2,u0)`.

### H-edge: `ell|c`

Use the eliminated equation. Dividing by `ell` gives

\[
\boxed{d_2'u_2^2\equiv d_1'u_1^2\pmod\ell,}
\]

again at most two lines in `(u2,u1)`.

This conclusion includes the residue `(0,0)` and therefore does not require a separate shallow/deep valuation assumption.

---

## 7. Dyadic lattice count: first post-local sectoral saving

Let an incident square-variable pair lie in a rectangular dyadic box

```text
|u_i| <= U_i,
|u_j| <= U_j.
```

For one nonzero line

\[
u_i\equiv r u_j\pmod\ell,
\]

counting `u_i` after fixing `u_j` gives

\[
O\left(\frac{U_iU_j}{\ell}+U_j+1\right).
\]

Counting in the opposite order and taking the better estimate gives, for the union of at most two lines,

\[
\boxed{
N_{ij}(U_i,U_j;\ell)
\ll
\frac{U_iU_j}{\ell}+\min(U_i,U_j)+1.
}
\]

Relative to the unrestricted pair volume `U_iU_j`, the retained fraction is

\[
\ll \ell^{-1}+\max(U_i,U_j)^{-1}+ (U_iU_j)^{-1}.
\]

Consequently, for any fixed `eta>0`, every dyadic sector satisfying

\[
\ell\ge B^\eta,
\qquad
\max(U_i,U_j)\ge B^\eta
\]

has an incident-pair saving

\[
\boxed{B^{-\eta}}
\]

up to constants/subpolynomial factors.

This is a theorem about the actual global witness variables, not a reuse of the s5 local character cancellation.

It proves

```text
LARGE_KERNEL_PRIME_PROJECTIVE_INCIDENCE_SAVING=true.
```

It does **not** yet prove a global `delta_post`, because one must still sum the complementary sectors and compare the full anisotropic witness volume to the already-proved local-class count.

---

## 8. Exact remaining obstruction

After 4bh the direct post-local count has no unresolved fixed-packet geometric singularity. The remaining obstruction is quantitative and lies in the complement of the large-prime/long-incident-variable sector.

### A. Smooth or tiny odd kernel

The nonzero Kummer class may have no odd kernel prime above `B^eta`; in particular, a class can have very small odd support even when `SXH` itself has large prime factors. A smoothness theorem for the base alone is therefore insufficient.

### B. Short incident square variables

Even with a large kernel prime, the congruence-line estimate only becomes a power saving relative to the pair box when an incident square-variable range is itself sufficiently long. The generic 4bg canonical-height transfer gives only

```text
|A|, D^2 <= B^K_C
```

for a fixed but non-optimized `K_C`; it does not yet provide the sharp anisotropic dyadic distribution needed to show that the short-variable complement is negligible.

### C. Determinant method cannot yet be imported as a black box

The fixed packet curve is now proved smooth degree four/genus one, so the **geometric** prerequisites are favorable. But a per-curve rational-point estimate in a box of size `B^K_C`, multiplied over the moving base/kernel family, does not automatically improve the class exponent `41/42`. A quantitative theorem must exploit either the moving large-prime incidence, sharper physical height coordinates, or an averaged square-sieve/determinant estimate across packets.

Thus

```text
DETERMINANT_METHOD_GEOMETRY_READY=true
DETERMINANT_METHOD_BLACK_BOX_SUFFICIENT_FOR_DELTA_POST=false.
```

---

## 9. Current exponent ledger

Merged s5u/4bg still give

\[
J_C(B)\ll B^{41/42+\varepsilon}.
\]

A full-family theorem

\[
J_C(B)\ll B^{41/42-\delta_{post}+\varepsilon}
\]

with any fixed `delta_post>0` remains open. Reaching the square-root upper-bound scale still requires

\[
\delta_{post}\ge\frac{10}{21}.
\]

4bh supplies a genuine `B^{-eta}` gain on every sector carrying an edge-kernel prime and incident square-variable range both at least `B^eta`; it does not yet prove that these sectors dominate the full witness count.

---

## Boundary

```text
STAGE14_4BH=TWO_QUADRIC_GENUS_ONE_GEOMETRY_AND_LARGE_KERNEL_INCIDENCE_SPLIT
FIXED_PACKET_PENCIL_DETERMINANT_EXACT=true
FIXED_PACKET_PENCIL_HAS_FOUR_DISTINCT_SINGULAR_PARAMETERS=true
FIXED_PACKET_CURVE_SMOOTH_GENUS_ONE=true
POSITIVE_DIMENSIONAL_TORSION_OR_COORDINATE_BOUNDARY=false
ONE_SQUARE_VARIABLE_ELIMINATION_EXACT=true
CONIC_PLUS_SQUARE_LIFT_EXACT=true
CONIC_DOUBLE_COVER_BRANCH_COUNT=4
ODD_KERNEL_EDGE_PACKET_FACTORIZATION_REPROVED=true
LARGE_KERNEL_EDGE_PRIME_TWO_LINE_CONGRUENCE=true
DYADIC_LARGE_PRIME_INCIDENCE_BOUND_PROVED=true
DIRECT_POST_LOCAL_LARGE_KERNEL_SECTOR_SAVING_PROVED=true
DETERMINANT_METHOD_GEOMETRY_READY=true
SMOOTH_OR_TINY_KERNEL_COMPLEMENT_OPEN=true
SHORT_INCIDENT_SQUARE_VARIABLE_COMPLEMENT_OPEN=true
DETERMINANT_METHOD_BLACK_BOX_SUFFICIENT_FOR_DELTA_POST=false
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bi quantify the complementary smooth/tiny-kernel and short-incident-variable sectors using the exact edge-packet decomposition and a sharper anisotropic height ledger; combine with the 4bh congruence-line gain if a positive global delta_post emerges
```
