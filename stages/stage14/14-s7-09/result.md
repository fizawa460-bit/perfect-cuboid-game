# Stage14-s7-09 — adjacent two-cell mixed-character gate beyond 18/19

## Purpose

Merged Stage14-s7-08 proves the current whole-family bound

```text
V(B) << B^(18/19+o(1)).
```

Its thin branch uses the exact shared-`xi` four-cell factorisation

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j
```

and then varies one large cell at a time.  A one-cell quartic square sieve gives relative saving `T^(-1/2)`.  Because a large coefficient such as `a=r*s` only forces one cell of size at least `a^(1/2)`, this converts coefficient size `a` into only `a^(-1/4)` saving.  That loss is exactly what creates the `18/19` minimax barrier.

This stage asks whether the two cells comprising a large coefficient can be dispersed **jointly**.  It proves three structural facts:

1. every adjacent-cell detector is square-equivalent to one universal two-variable polynomial
   `H(R,S)=(1-R^2 S^2)(S^2-R^2)`;
2. for every inert prime `p=3 mod 4`, the complete two-variable quadratic-character trace of `H` is exactly zero;
3. if one can prove the uniform nonzero-frequency mixed-character estimate
   `|T_p(h,k)| << p` for this universal `H`, then two-cell square sieve gives relative saving `(RS)^(-1/3)` and the global threshold optimisation improves exactly to `16/17`.

The uniform mixed-frequency estimate is **not proved in this stage**.  Finite deterministic audits strongly support the `O(p)` scale, and Katz's work on nonsingular mixed character sums is the natural external theorem family to inspect next, but its exact hypotheses must be checked against this reducible normal-crossing divisor before it can be imported.

Therefore the current theorem exponent remains `18/19`.  Stage14-s7-10 is the geometry/sheaf gate for the universal adjacent-cell mixed transform.

---

## 1. Merged s7-08 input and the one-cell barrier

For one coefficient, say

```text
a=r*s,
```

s7-08 only uses

```text
max(r,s) >= a^(1/2).
```

One-cell square sieve on the larger cell gives relative saving

```text
max(r,s)^(-1/2) <= a^(-1/4).
```

This is the source of the numerator-thin exponent

```text
1-(theta-2*tau)/4.
```

Merely applying the one-cell estimate first in `r` and then separately in `s` does not multiply the two savings.  The same square condition is being detected twice, so the safe bound is only

```text
R*S / sqrt(max(R,S)),
```

which is again no better than `(RS)^(-1/4)` in the balanced worst case.

Thus any improvement below `18/19` requires a genuinely two-variable estimate.

---

## 2. Adjacent-cell detector

Write the two same-kernel factors as

```text
G1=(t*j*y^2)^2-(r*s*x^2)^2,
G2=(s*j*h^2)^2-(r*t*z^2)^2.
```

Fix `t,j,x,y,z,h` and vary the adjacent cells `(r,s)`.

Set

```text
A=t*j*y^2,
B=j*h^2,
C=t*z^2.
```

Then

```text
G1=A^2-r^2 s^2 x^4,
G2=B^2 s^2-C^2 r^2.
```

Define rational square scalings

```text
alpha = x*z/(j*y*h),
beta  = x*h/(t*z*y),
R=alpha*r,
S=beta*s.
```

They satisfy

```text
alpha*beta = x^2/A,
C/alpha = B/beta.
```

Hence

```text
G1 = A^2*(1-R^2*S^2),
G2 = K^2*(S^2-R^2),
K=C/alpha=B/beta.
```

Therefore

```text
boxed:
G1*G2 = (A*K)^2 * H(R,S),
H(R,S)=(1-R^2*S^2)(S^2-R^2).
```

So the squareclass detector for the adjacent pair `(r,s)` is universal.

The other three adjacent coefficient pairs `(t,j)`, `(r,t)`, `(s,j)` reduce by the same cell symmetries to `+H` or `-H` after rational square scalings.  A constant sign changes only the fixed quadratic-character phase and not the magnitude of any character sum.

---

## 3. Geometry of the universal detector

Over characteristic not equal to `2`,

```text
H(R,S)
=(1-R*S)(1+R*S)(S-R)(S+R).
```

Thus the zero divisor is the union of four smooth rational components:

```text
R*S=+1,
R*S=-1,
S=R,
S=-R.
```

Over the algebraic closure these meet only in transverse pairwise intersections; there is no repeated component.  In particular `H` is not a square in the rational function field.

For inert primes `p=3 mod 4`, the two line components meet the two hyperbola components in the expected conjugate pattern, and `-1` is nonsquare.  This produces an exact cancellation at zero additive frequency.

---

## 4. Exact inert complete trace

Let `chi` denote the quadratic character modulo an odd prime `p=3 mod 4`, extended by `chi(0)=0`.

Define

```text
S_p = sum_{R,S mod p} chi(H(R,S)).
```

### 4.1 Boundary axes

At `R=0`,

```text
H(0,S)=S^2,
```

so the nonzero `S` contribute `p-1`.

At `S=0`,

```text
H(R,0)=-R^2,
```

and `chi(-1)=-1`, so the nonzero `R` contribute `-(p-1)`.

The axis contributions cancel exactly.

### 4.2 Nonzero torus

For `R,S != 0`, put

```text
u=R*S,
v=R/S.
```

Then

```text
chi(H(R,S))=chi(1-u^2)*chi(1-v^2),
```

because the omitted factor `S^2` is a square.

The map `(R,S)->(u,v)` has two preimages exactly when

```text
chi(u)*chi(v)=1.
```

Therefore the torus sum is

```text
[sum_{u!=0} chi(1-u^2)]^2
+
[sum_{u!=0} chi(u)*chi(1-u^2)]^2.
```

For `p=3 mod 4`,

```text
sum_{u mod p} chi(1-u^2)=1,
```

and removing `u=0` gives zero.  The second sum is the inert trace already used in s7-07,

```text
sum_u chi(u*(1-u^2))=0.
```

Hence the torus contribution is also zero.

Combining axes and torus,

```text
boxed:
sum_{R,S mod p} chi((1-R^2*S^2)(S^2-R^2)) = 0.
```

This is stronger than a generic `O(p)` zero-frequency estimate.

---

## 5. The actual missing theorem: nonzero additive frequencies

For `(h,k) mod p`, define

```text
T_p(h,k)
 = sum_{R,S mod p}
   chi(H(R,S))*e_p(hR+kS).
```

Section 4 gives

```text
T_p(0,0)=0.
```

What is needed for genuine two-cell completion is the uniform mixed bound

```text
MIXED-2CELL(p):
|T_p(h,k)| << p
```

for every `(h,k)`, uniformly outside a finite good-prime set.

This is the natural two-dimensional square-root scale: the ambient complete box has `p^2` points.

Finite exact computations in the deterministic audit show `max_{h,k}|T_p(h,k)|/p` remains bounded for the tested inert primes and physical normalisations.  This is evidence only, not a theorem.

Relevant literature exists on nonsingular multiplicative and mixed character sums in several variables, notably Nicholas Katz, *Estimates for nonsingular multiplicative character sums* (IMRN 2002) and *Estimates for Nonsingular Mixed Character Sums* (IMRN 2007).  However `H=0` is reducible, though normal-crossing, so the exact mixed-sum theorem hypotheses must be checked before importing an `O(p)` estimate.

Thus:

```text
ADJACENT_TWO_CELL_ZERO_FREQUENCY_CLOSED=true
ADJACENT_TWO_CELL_NONZERO_FREQUENCY_OP_BOUND_PROVED=false
```

---

## 6. What MIXED-2CELL would imply locally

Assume `MIXED-2CELL(p)` uniformly for good inert primes.

By CRT, for a product `m=p*q` of two comparable good inert primes,

```text
|T_m(h,k)| << m*B^o(1).
```

Two-dimensional Fourier completion on a rectangle of side lengths `R,S` then gives

```text
sum_{r in I_R, s in I_S} chi_m(H(r,s))
 << m*B^o(1).
```

The zero mode is actually absent by the exact trace identity.

Let the auxiliary prime scale be `L`, so `m~L^2`.  A square sieve on the two-cell rectangle gives

```text
N_2cell(R,S)
 << B^o(1) * (R*S/L + L^2).
```

Optimising at

```text
L=(R*S)^(1/3)
```

gives

```text
boxed conditional:
N_2cell(R,S) << (R*S)^(2/3)*B^o(1).
```

Thus an adjacent coefficient

```text
a=r*s
```

would carry relative saving

```text
boxed conditional:
a^(-1/3),
```

instead of the current one-cell `a^(-1/4)`.

This is exactly the quantitative gain needed for the next exponent transition.

---

## 7. Conditional global optimisation

Retain the three threshold variables:

```text
lambda = small-denominator exponent,
tau    = square-part thickness exponent,
theta  = small-numerator exponent.
```

Under the conditional two-cell saving, the five active sector exponents become

```text
E1 = 2*lambda,
E2 = 1-tau/2,
E3 = 1+theta-lambda,
E4 = 1-(theta-2*tau)/3,
E5 = 1-(lambda-2*tau)/3.
```

The exact minimax point is

```text
lambda = 8/17,
tau    = 2/17,
theta  = 7/17.
```

At this point

```text
E1=E2=E3=E4=16/17,
E5=47/51 < 16/17.
```

Hence `MIXED-2CELL` would imply

```text
boxed conditional:
V(B) << B^(16/17+o(1)).
```

The potential improvement over the current `18/19` is

```text
18/19 - 16/17 = 2/323.
```

The corresponding remaining gap to square root would be

```text
16/17 - 1/2 = 15/34.
```

These are **conditional ledgers only**; they are not current theorem claims.

---

## 8. Why the current one-cell theorem cannot supply the gate

One might try to prove the two-cell bound by applying the s7-08 one-cell theorem twice.  That is invalid as a multiplicative saving.

Fixing `s` and sieving `r` gives at best

```text
R^(1/2)*S.
```

Fixing `r` and sieving `s` gives at best

```text
R*S^(1/2).
```

Taking the better of these gives

```text
R*S / sqrt(max(R,S)).
```

For fixed product `A=R*S`, the worst balanced case is

```text
A^(3/4),
```

exactly the one-cell coefficient saving already used in s7-08.

So the `2/3` exponent cannot be obtained by threshold retuning or repeated one-variable Weil bounds.  It genuinely requires a two-variable mixed-frequency theorem.

---

## 9. Stage boundary

Proved in s7-09:

- exact universal normalisation of every adjacent-cell detector to `+/-H`;
- exact factorisation `H=(1-RS)(1+RS)(S-R)(S+R)`;
- exact inert complete two-variable trace zero;
- exact identification of the missing uniform nonzero-frequency estimate;
- proof that sequential one-cell estimates cannot beat the `18/19` architecture;
- exact conditional square-sieve transfer from `MIXED-2CELL` to `(RS)^(2/3)`;
- exact conditional threshold optimum `16/17`.

Not proved in s7-09:

- the uniform `O(p)` bound for all additive frequencies;
- the two-cell `(RS)^(2/3)` theorem;
- any new whole-family exponent below `18/19`.

```text
STAGE14_S7_09=COMPLETE_ADJACENT_TWO_CELL_UNIVERSAL_TRACE_AND_MIXED_CHARACTER_GATE
MERGED_S7_08_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19
ADJACENT_TWO_CELL_UNIVERSAL_POLYNOMIAL=(1-R^2*S^2)(S^2-R^2)
ADJACENT_TWO_CELL_DIVISOR_NORMAL_CROSSING=true
INERT_ADJACENT_TWO_CELL_COMPLETE_TRACE_ZERO=true
SEQUENTIAL_ONE_CELL_SAVINGS_MULTIPLY=false
SEQUENTIAL_ONE_CELL_ARCHITECTURE_BEATS_18_19=false
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=false
CONDITIONAL_TWO_CELL_RECTANGLE_EXPONENT=2/3
CONDITIONAL_OPTIMAL_LAMBDA=8/17
CONDITIONAL_OPTIMAL_TAU=2/17
CONDITIONAL_OPTIMAL_THETA=7/17
CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-10
```
