# Stage14-4by — close the adjacent two-cell mixed transform and obtain 13/14

## Purpose

Merged Stage14-4bx gives the unconditional whole-family bound

```text
V(B) << B^(15/16+o(1)).
```

Merged Stage14-s7-09 isolates the next missing input.  For the universal adjacent-cell detector

```text
H(R,S)=(1-R^2*S^2)*(S^2-R^2)
      =(1-R*S)*(1+R*S)*(S-R)*(S+R),
```

it proves the complete inert-prime zero trace and shows that a uniform mixed additive Fourier estimate

```text
|T_p(h,k)| << p,
T_p(h,k)=sum_{R,S mod p} chi_p(H(R,S))*e_p(hR+kS),
```

would upgrade the one-cell coefficient saving to the two-cell saving `(RS)^(-1/3)`.

Stage14-4by proves this missing estimate.  The generic frequencies are handled by Lei Fu's toric twisted-exponential-sum theorem after an exact four-Kummer Gauss lift.  The only potentially degenerate frequencies are `h=+/-k`; for those frequencies the physical universal detector has an elementary line-by-line odd-pairing cancellation, giving exact zero.

Combining the now-proved two-cell receiver with the stronger thick-packet theorem from merged 4bx gives

```text
boxed:
V(B) << B^(13/14+o(1)).
```

No square-root bound is claimed.

---

## 1. Merged inputs

We use only merged repository inputs plus one explicitly contracted external character-sum theorem.

Merged inputs:

1. Stage14-s7-09:
   - universal adjacent two-cell detector `H(R,S)` above;
   - exact inert zero-frequency trace;
   - conditional transfer `|T_p(h,k)|<<p` -> two-cell rectangle count `(RS)^(2/3)B^o(1)`;
   - sequential one-cell savings do not multiply.
2. Stage14-4bx:
   - fixed product-square thick packet bound
     `N_packet << M*Hmin^(-4/5)B^o(1)`;
   - hence thick-sector exponent `1-4*tau/5`;
   - current whole-family exponent `15/16`.
3. Stage14-s7-08 / 4bw:
   - exact shared-`xi` four-cell parametrisation;
   - denominator/numerator sector decomposition;
   - fixed-coordinate partner multiplicity `B^o(1)`.

External theorem contract:

> Lei Fu, **Twisted Exponential Sums**, arXiv:math/0607164v2, Corollary 0.3.  If the Gauss-lifted Laurent polynomial associated to a finite collection of nontrivial multiplicative characters and one nontrivial additive character is non-degenerate with respect to its Newton polyhedron at infinity and has full dimension, then the original `n`-variable mixed sum is bounded by a fixed Newton-volume constant times `q^(n/2)`.

Here `n=2`, so the required scale is `O(p)`.  The stage verifies the non-degeneracy hypothesis directly for every non-exceptional additive frequency.

---

## 2. The mixed transform

Let `p=3 mod 4` be an inert odd prime and let `chi=chi_p` be the quadratic character, extended by `chi(0)=0`.

Define

```text
T_p(h,k)
 = sum_{R,S mod p}
   chi((1-R*S)*(1+R*S)*(S-R)*(S+R))
   e_p(hR+kS).                                      (2.1)
```

We prove

```text
boxed:
|T_p(h,k)| <= C*p                                  (2.2)
```

for an absolute constant `C`, uniformly in `p,h,k`.

The proof splits into generic frequencies `h != +/-k` and the two exceptional frequency lines.

---

## 3. Four-Kummer Gauss lift on the torus

First restrict to `R,S != 0`.  Put

```text
f1=1-R*S,
f2=1+R*S,
f3=S-R,
f4=S+R,
f0=h*R+k*S.
```

The torus part of (2.1) is

```text
sum_{R,S in F_p^*}
 chi(f1)*chi(f2)*chi(f3)*chi(f4)*e_p(f0).           (3.1)
```

Fu's Corollary 0.3 converts this to the non-degeneracy of the six-variable Laurent polynomial

```text
Phi_{h,k}(R,S,U,V,W,Z)
 = h*R+k*S
   +U*(1-R*S)
   +V*(1+R*S)
   +W*(S-R)
   +Z*(S+R).                                       (3.2)
```

All six variables are torus variables for the lifted sum.

The support of the four Kummer blocks alone already spans dimension six, so

```text
dim Delta_infty(Phi_{h,k})=6                       (3.3)
```

whether or not one of `h,k` vanishes.

---

## 4. Exact face non-degeneracy lemma

Take a face `tau` of `Delta_infty(Phi)` not containing the origin.  Let

```text
a = face weight of R,
b = face weight of S,
M = positive face level.
```

Suppose, for contradiction, that all six partial derivatives of `Phi_tau` vanish at a torus point.

### 4.1 Auxiliary blocks must occur in full pairs

Each auxiliary variable occurs in exactly two monomials:

```text
U: U, U*R*S,
V: V, V*R*S,
W: W*S, W*R,
Z: Z*S, Z*R.
```

If a face contains exactly one monomial from any one of these blocks, the derivative with respect to that auxiliary variable is a nonzero torus monomial.  Hence no critical point exists.

Therefore every auxiliary block appearing in a critical face must appear as its full two-term block.

A full hyperbola block (`U` or `V`) forces

```text
a+b=0.                                             (4.1)
```

A full line block (`W` or `Z`) forces

```text
a=b.                                               (4.2)
```

### 4.2 Two blocks of the same type are impossible

Both hyperbola blocks would impose simultaneously

```text
1-R*S=0,
1+R*S=0,
```

which is impossible for odd `p`.

Both line blocks would impose

```text
S-R=0,
S+R=0,
```

which is impossible on the torus.

Thus at most one hyperbola block and at most one line block may occur in a critical face.

### 4.3 One hyperbola plus one line is transverse

If one hyperbola and one line block both occur, (4.1)-(4.2) give

```text
a=b=0.
```

Because the face level is positive, the additive monomials `hR,kS` have weight zero and are absent from the face.

The four possible hyperbola/line intersections are transverse on the torus:

```text
1-RS=0 with S-R=0,
1-RS=0 with S+R=0,
1+RS=0 with S-R=0,
1+RS=0 with S+R=0.
```

Their two gradients are linearly independent.  The `R,S` derivative equations therefore force both auxiliary coefficients to vanish, contradicting that the auxiliary torus variables are nonzero.

### 4.4 A single hyperbola block cannot be critical

For a full hyperbola block, `a+b=0`.  At most one additive monomial can lie on the same positive face level.  The hyperbola `1+/-RS=0` is smooth on the torus and its gradient has both coordinates nonzero.

If no additive monomial occurs, the `R,S` derivatives force the auxiliary variable to be zero.  If exactly one additive monomial occurs, the derivative in the other coordinate remains a nonzero multiple of the auxiliary variable.  Both are impossible.

### 4.5 A single line block isolates exactly `h=+/-k`

For a full line block, `a=b`.

If the additive monomials are absent, smoothness again rules out a critical point.

If additive terms occur on the same positive face, the critical equations are:

For `S-R`:

```text
S-R=0,
h-W=0,
k+W=0,
```

which is possible exactly when

```text
k=-h.                                              (4.3)
```

For `S+R`:

```text
S+R=0,
h+Z=0,
k+Z=0,
```

which is possible exactly when

```text
k=h.                                               (4.4)
```

If only one of the additive coefficients is present, the other derivative prevents a critical point.

### 4.6 Generic conclusion

Faces with no complete Kummer block reduce to additive monomials and have nonzero gradient.

Therefore

```text
boxed:
Phi_{h,k} is Newton-nondegenerate whenever h != +/-k.  (4.5)
```

Fu's Corollary 0.3 now gives the torus estimate

```text
boxed:
|T_p^tor(h,k)| << p,
for h != +/-k.                                     (4.6)
```

The constant is absolute because the support/Newton polyhedron belongs to one fixed finite support family.

---

## 5. Coordinate axes cost only O(p)

Fu's theorem controls `R,S != 0`.  The axes are elementary.

At `R=0`,

```text
H(0,S)=S^2,
```

so the nonzero axis contributes

```text
sum_{S!=0} e_p(kS)
 = p-1 if k=0,
   -1  otherwise.                                  (5.1)
```

At `S=0`,

```text
H(R,0)=-R^2.
```

Since `p=3 mod 4`, `chi(-1)=-1`, so this axis contributes

```text
-sum_{R!=0} e_p(hR)
 = -(p-1) if h=0,
    +1    otherwise.                               (5.2)
```

Hence the total axis contribution is always `O(p)`.  Together with (4.6), this proves (2.2) for `h != +/-k`.

---

## 6. Exceptional frequencies vanish line by line

The two frequencies excluded by the Newton-face argument are even easier.

### 6.1 Frequency h=k

Put

```text
x=R+S,
y=S-R.
```

Then

```text
S^2-R^2=x*y,
R*S=(x^2-y^2)/4,
```

and therefore

```text
H(R,S)
 = x*y * (1-(x^2-y^2)^2/16).                      (6.1)
```

Fix `x`.

If `x=0`, then `H=0` identically on that line.

If `x!=0`, write `y=x*t`.  Up to the square factor `x^2`,

```text
H ~ t * [1 - x^4*(1-t^2)^2/16].                   (6.2)
```

The bracket is an even function of `t`.  Pairing `t` with `-t` gives

```text
chi(-t*E(t^2))
 = chi(-1)*chi(t*E(t^2))
 = -chi(t*E(t^2)),                                 (6.3)
```

because `chi(-1)=-1`.  The `t=0` term is zero.  Thus every line `R+S=x` has total character sum zero.

For `h=k`, the additive phase is constant on each such line:

```text
e_p(hR+hS)=e_p(hx).
```

Therefore

```text
boxed:
T_p(h,h)=0                                         (6.4)
```

for every `h`, including `h=0`.

### 6.2 Frequency h=-k

Now the phase depends only on `R-S`, equivalently on `y=S-R`.  Fix `y` and write `x=y*t` when `y!=0`.  The same odd pairing gives zero on each `S-R=y` line.  Hence

```text
boxed:
T_p(h,-h)=0.                                       (6.5)
```

### 6.3 Uniform mixed theorem

Combining Sections 4-6:

```text
boxed:
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true
|T_p(h,k)| << p
for every inert prime p and every h,k mod p.        (6.6)
```

The two would-be singular frequency lines are not losses; they are exact zeros.

---

## 7. CRT, rectangle completion, and two-cell square sieve

Let `m=p*q` with distinct good inert primes `p,q` of comparable scale `L`.  CRT factorisation and (6.6) give every complete additive Fourier mode modulo `m` the bound

```text
<< m*B^o(1).                                       (7.1)
```

The rational square scalings used in merged s7-09 are units at good primes, so they only permute additive frequencies.  Thus the bound is uniform in every physical adjacent-cell packet.

Two-dimensional Fourier completion on a rectangle of side lengths `R0,S0` gives

```text
sum_rectangle chi_m(H)
 << m*B^o(1).                                       (7.2)
```

Let

```text
A=R0*S0.
```

The standard square sieve then gives

```text
N_2cell(A)
 << B^o(1)*(A/L + L^2).                            (7.3)
```

Choose

```text
L=A^(1/3).
```

Then

```text
boxed:
N_2cell(R0,S0)
 << (R0*S0)^(2/3)*B^o(1).                          (7.4)
```

Equivalently a large adjacent coefficient `a=r*s` receives the relative saving

```text
boxed:
a^(-1/3+o(1)).                                    (7.5)
```

This upgrades the s7-09 conditional receiver to an unconditional theorem.

---

## 8. Global threshold ledger with the 4bx thick theorem

Use

```text
lambda : small-denominator threshold,
nu     : small-numerator threshold,
tau    : square-part threshold.
```

The exhaustive exponents are now

```text
E1 = 2*lambda,                                     (8.1)
E2 = 1+nu-lambda,                                  (8.2)
E3 = 1-4*tau/5,                                    (8.3)
E4 = 1-(nu-2*tau)/3,                               (8.4)
E5 = 1-(lambda-2*tau)/3.                           (8.5)
```

Here:

- `E3` is merged 4bx;
- `E4,E5` use the newly proved two-cell coefficient saving (7.5).

Because `nu<=lambda`, `E5<=E4`.

---

## 9. Exact minimax: 13/14

The optimum is

```text
boxed:
lambda = 13/28,
nu     = 11/28,
tau    = 5/56.                                     (9.1)
```

Indeed,

```text
2*lambda                  = 13/14,
1+nu-lambda              = 13/14,
1-4*tau/5                = 13/14,
1-(nu-2*tau)/3           = 13/14.                  (9.2)
```

The denominator-thin branch is smaller:

```text
1-(lambda-2*tau)/3
 = 19/21
 < 13/14.                                          (9.3)
```

### 9.1 Barrier certificate

If all active terms were at most `E`, then

```text
lambda <= E/2,
nu <= E-1+lambda <= 3E/2-1,
tau >= (5/4)*(1-E),
nu >= 2*tau+3*(1-E) >= (11/2)*(1-E).
```

Hence

```text
(11/2)*(1-E) <= 3E/2-1,
```

so

```text
boxed:
E>=13/14.                                          (9.4)
```

Thus `13/14` is the exact threshold-tuning barrier for the current **optimized thick + adjacent two-cell thin** architecture.

---

## 10. New whole-family upper bound

The sector split is exhaustive, hence

```text
boxed:
V(B) << B^(13/14+o(1)).                            (10.1)
```

The improvement over merged 4bx is

```text
15/16 - 13/14 = 1/112.                             (10.2)
```

The cumulative saving from the post-local baseline is especially simple:

```text
41/42 - 13/14 = 1/21.                              (10.3)
```

The remaining exponent gap to square root is

```text
13/14 - 1/2 = 3/7.                                 (10.4)
```

No square-root upper bound is proved.

---

## 11. Stage boundary

```text
STAGE14_4BY=FU_GAUSS_LIFT_TWO_CELL_MIXED_TRANSFORM_AND_13_14_BOUND
MERGED_4BX_IMPORTED=true
MERGED_S7_09_IMPORTED=true
FU_TWISTED_EXPONENTIAL_SUM_COROLLARY_0_3_IMPORTED=true
FOUR_KUMMER_GAUSS_LIFT_EXACT=true
GAUSS_LIFT_NEWTON_POLYHEDRON_FULL_DIMENSION=true
GENERIC_FREQUENCY_NEWTON_NONDEGENERACY_PROVED=true
ONLY_POTENTIAL_DEGENERATE_FREQUENCIES=h=+/-k
EXCEPTIONAL_FREQUENCY_LINE_SUMS_EXACT_ZERO=true
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true
ADJACENT_TWO_CELL_RECTANGLE_EXPONENT=2/3
ADJACENT_COEFFICIENT_RELATIVE_SAVING=(RS)^(-1/3)
OPTIMAL_DENOMINATOR_CUTOFF_EXPONENT=13/28
OPTIMAL_NUMERATOR_CUTOFF_EXPONENT=11/28
OPTIMAL_SQUAREPART_THRESHOLD_EXPONENT=5/56
TWO_CELL_OPTIMIZED_ARCHITECTURE_BARRIER=13/14
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14
IMPROVEMENT_OVER_15_16=1/112
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/21
CURRENT_GAP_TO_SQRT=3/7
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bz correlate the active 13/14 small-denominator/small-numerator/thick/two-cell sectors instead of retuning thresholds
```
