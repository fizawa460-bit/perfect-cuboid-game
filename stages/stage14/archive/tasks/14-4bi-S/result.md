# Stage14-4bi-S — full edge-radical modulus and canonical-witness small-D core

## Purpose

Merged Stage14-4bi-L closes the large edge-kernel route, while merged Stage14-s6-03 independently proves a centered-quartic fixed-packet saving and reduces every coordinate-level complement to small denominator.

This stage performs the S-side main-track cleanup.  Its new observation is that the packet equations carry not merely the selected edge kernels `a,b,c`, but the **entire odd radicals of the three Pythagorean legs** as usable congruence moduli.

Consequences:

1. `small kernel` is removed from the intrinsic obstruction list;
2. hypotenuses with genuinely small radical form a globally power-sparse base family;
3. radical-rich packets have a full-radical witness-lattice restriction, independent of kernel size;
4. if the corresponding witness pair is short, the exact packet equation forces a small denominator;
5. after importing s6-03, the sole unresolved quantitative issue is the conversion of these coordinate-level restrictions into an unweighted base/class existence saving.

No full positive `delta_post` is claimed.

---

## 1. Imported packet and centered-sieve boundary

From merged s6-01,

\[
d_0=\tau_0ab,\qquad d_1=\tau_1ac,\qquad d_2=\tau_2bc,
\]

with

\[
a\mid\operatorname{rad}_{\rm odd}(S),\quad
b\mid\operatorname{rad}_{\rm odd}(X),\quad
c\mid\operatorname{rad}_{\rm odd}(H),
\]

and

\[
\tau_0ab u_0^2-\tau_1ac u_1^2=S^2D^2,
\]

\[
\tau_2bc u_2^2-\tau_0ab u_0^2=X^2D^2,
\]

\[
\tau_2bc u_2^2-\tau_1ac u_1^2=H^2D^2.
\]

Merged 4bi-L divides by the common edge kernel:

\[
\tau_0b u_0^2-\tau_1c u_1^2=a(S/a)^2D^2,
\tag{1S}
\]

\[
\tau_2c u_2^2-\tau_0a u_0^2=b(X/b)^2D^2,
\tag{1X}
\]

\[
\tau_2b u_2^2-\tau_1a u_1^2=c(H/c)^2D^2.
\tag{1H}
\]

Merged s6-03 proves, independently of kernel size, the fixed-packet centered-quartic rectangle saving

\[
\min(U,D)^{-1/3+\epsilon},
\]

and the exact forcing

\[
D\le2\max(|u_1|,|u_2|).
\]

It also correctly isolates the remaining quantifier gap: coordinate-density savings cannot simply be multiplied by the unweighted `B^(41/42)` local class count.

---

## 2. Full odd radicals are exact congruence moduli

Define

\[
R_S=\operatorname{rad}_{\rm odd}(S),\qquad
R_X=\operatorname{rad}_{\rm odd}(X),\qquad
R_H=\operatorname{rad}_{\rm odd}(H).
\]

Write `R_S=a q_S`.  Since every prime in `q_S` divides `S/a`,

\[
R_S=a q_S\mid a(S/a)^2.
\]

Likewise,

\[
R_X\mid b(X/b)^2,
\qquad
R_H\mid c(H/c)^2.
\]

Therefore (1S)--(1H) give

\[
\boxed{\tau_0b u_0^2\equiv\tau_1c u_1^2\pmod{R_S}},
\]

\[
\boxed{\tau_2c u_2^2\equiv\tau_0a u_0^2\pmod{R_X}},
\]

\[
\boxed{\tau_2b u_2^2\equiv\tau_1a u_1^2\pmod{R_H}}.
\]

The coefficients are units modulo the corresponding odd radical because the three primitive Pythagorean legs are pairwise coprime and the `tau_i` only add sign and a factor of `2`.

Hence the usable modulus survives even when

```text
a=b=c=1.
```

So

```text
SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false.
```

---

## 3. Full-radical rectangle theorem

The composite squarefree line-cover lemma from 4bi-L applies directly.  For example, on the H-edge the congruence solutions lie in at most

\[
2^{\omega(R_H)}=B^{o(1)}
\]

projective lines modulo `R_H`, each giving a rank-two lattice of index `R_H`.

Thus for `u_1~U_1`, `u_2~U_2`,

\[
\boxed{
N_H(U_1,U_2)
\ll_\epsilon
B^\epsilon
\left(
\frac{U_1U_2}{R_H}+\min(U_1,U_2)+1
\right).
}
\tag{2}
\]

The same bound holds on the S and X edges with `R_S,R_X`.

If

\[
R_H\ge B^\rho,
\qquad
U_*:=\max(U_1,U_2)\ge B^\nu,
\]

then the H-edge witness layer has relative saving

\[
\boxed{B^{-\min(\rho,\nu)+\epsilon}}.
\tag{3}
\]

This is a coordinate/witness-layer theorem, not yet an unweighted class-count theorem.

---

## 4. Radical-poor integers are globally sparse

For fixed `rho>0` and `epsilon>0`,

\[
\boxed{
\#\{n\le B:\operatorname{rad}(n)\le B^\rho\}
\ll_{\rho,\epsilon}B^{\rho+\epsilon}.
}
\tag{4}
\]

Proof: for squarefree `r`,

\[
\sum_{\operatorname{rad}(n)=r}n^{-s}
=r^{-s}\prod_{p\mid r}(1-p^{-s})^{-1}.
\]

Rankin's trick gives

\[
\#\{n\le B:\operatorname{rad}(n)=r\}
\le B^s r^{-s}\prod_{p\mid r}(1-p^{-s})^{-1}.
\]

For fixed `s>0`, the Euler-factor product is `O_{s,eta}(r^eta)` for every `eta>0`.  Taking `s=epsilon/2`, `eta=s/2`, and summing `r<=B^rho` proves (4).

For each odd hypotenuse `H`, the number of oriented primitive Pythagorean representations is at most `2^{omega(H)+O(1)}=H^{o(1)}`.  The closed local/descent packet multiplicity is also `B^epsilon`.

Hence

\[
\boxed{
\#\{\text{supported base/classes}:H\le B,\ R_H\le B^\rho\}
\ll_\epsilon B^{\rho+\epsilon}.
}
\tag{5}
\]

This is a genuine global base/class saving, unlike the relative coordinate-box gains.

---

## 5. Radical-rich short witness forces small denominator

From (1H),

\[
\frac{H^2}{c}D^2
=
|\tau_2b u_2^2-\tau_1a u_1^2|.
\]

Since `a,b,c<=H` and `|tau_i|<=2`,

\[
\frac{H^2}{c}D^2\le4HU_*^2.
\]

Because `c<=H`,

\[
HD^2\le4HU_*^2,
\]

so

\[
\boxed{D\le2U_*}.
\tag{6}
\]

Therefore

\[
R_H\ge B^\rho,\quad U_*<B^\nu
\quad\Longrightarrow\quad
\boxed{D<2B^\nu}.
\tag{7}
\]

This agrees with and sharpens the interpretation of merged s6-03: after all coordinate-level tools are applied, the only residual coordinate sector is small denominator.

---

## 6. Exact S-side partition

For fixed positive `rho,nu`, every S-side packet lies in one of:

### A. Radical-poor hypotenuse

\[
R_H<B^\rho.
\]

By (5), this contributes only

\[
B^{\rho+\epsilon}
\]

supported base/classes.

### B. Radical-rich, long canonical witness

\[
R_H\ge B^\rho,\qquad U_*\ge B^\nu.
\]

The full-radical lattice gives (3), and s6-03 simultaneously supplies a centered-quartic fixed-packet saving whenever `D` is long.

### C. Radical-rich short core

\[
R_H\ge B^\rho,\qquad U_*<B^\nu,
\]

which by (7) lies inside

\[
D<2B^\nu.
\]

Thus `small kernel` no longer appears anywhere in the final S-side partition.

---

## 7. Why no global delta_S is declared

The current physical/local theorem is

\[
N_{\rm local}(B)\ll B^{41/42+\epsilon}.
\]

It counts each admissible base/state packet once.

By contrast, (2), (3), and the s6-03 square sieve count the density of possible witness coordinates within a fixed packet box.  A packet contributes one to the existence count as soon as it has a single global point.  Therefore there is no valid multiplication

\[
B^{41/42}\times B^{-\delta_{coord}}
\]

without a theorem that sums the witness restrictions **after** the moving packet family has been assembled.

The s6-01 height transfer only gives a polynomial coordinate box

\[
|A|\le B^{K_C},\qquad D^2\le B^{K_C}
\]

with an unspecified fixed `K_C`; brute-force absolute counting of that box is not competitive.

The exact unresolved theorem is therefore:

```text
RADICAL_RICH_CANONICAL_WITNESS_OCCUPANCY
```

or equivalently the moving-packet weighted correlation requested by s6-03, with the small-D core treated anisotropically rather than by the generic polynomial box.

A deterministic canonical witness can be selected per soluble class (minimal canonical height, then naive height, then lexicographic tie-break), so multiplicity is not conceptually ambiguous.  What remains is its uniform moving-family count.

---

## 8. Main-track handoff

4bi-L and 4bi-S should now be recombined immediately; no further parallel branch is needed.

The combined obstruction list is reduced to one item:

```text
RADICAL_RICH_CANONICAL_WITNESS_OCCUPANCY / SMALL-D MOVING-PACKET CORRELATION.
```

The local exponent remains

\[
41/42,
\]

and reaching a square-root upper bound still requires

\[
\boxed{10/21}
\]

of post-local saving.

No positive full-family post-local exponent is asserted at this stage.

---

## Boundary

```text
STAGE14_4BI_S=FULL_EDGE_RADICAL_MODULUS_AND_CANONICAL_WITNESS_SMALL_D_CORE_ISOLATED
STAGE14_4BI_L_IMPORTED=true
STAGE14_S6_03_IMPORTED=true
FULL_ODD_EDGE_RADICAL_CONGRUENCES_PROVED=true
FULL_ODD_EDGE_RADICAL_RECTANGLE_BOUND_PROVED=true
SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false
RADICAL_POOR_INTEGER_COUNT_BOUND=B^(rho+epsilon)
RADICAL_POOR_HYPOTENUSE_SECTOR_GLOBALLY_SPARSE=true
RADICAL_RICH_LONG_WITNESS_LAYER_SAVING=B^(-min(rho,nu)+epsilon)
RADICAL_RICH_SHORT_WITNESS_IMPLIES_D_LE_2_USTAR=true
ONLY_COORDINATE_LEVEL_COMPLEMENT=SMALL_DENOMINATOR
CANONICAL_WITNESS_SELECTION_AVAILABLE=true
SMALL_DENOMINATOR_ALONE_POWER_SAVING_PROVED=false
EXISTENTIAL_PROJECTION_TO_CLASS_SAVING_PROVED=false
CANONICAL_WITNESS_OCCUPANCY_POWER_SAVING_PROVED=false
S_ROUTE_GLOBAL_POSITIVE_SAVING_PROVED=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bj immediately recombine 4bi-L and 4bi-S, delete small-kernel from the obstruction ledger, and freeze the radical-rich canonical-witness occupancy / small-D moving-packet correlation as the unique quantitative gate
```
