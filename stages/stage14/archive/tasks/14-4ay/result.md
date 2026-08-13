# Stage14-4ay — frozen-state stability and full six-linear interior summation

## Result

Merged Stage14-s5k proves the six-edge linear medium-dispersion theorem for the four linear Euclid columns

```text
m, n, m-n, m+n.
```

For each reciprocal edge `(L_i,L_j)` and odd squarefree coprime `u~U`, `v~V`, s5k gives

```text
|Delta_ij(u,v)|
 <<_epsilon B^epsilon (1 + H_i/u + H_j/v),
```

and hence

```text
sum |Delta_ij|^2
 <<_epsilon B^epsilon
    (UV + H_i^2 V/U + H_j^2 U/V).
```

It also gives the reciprocal discrepancy corollary

```text
|sum Delta_ij(u,v) (u/v)|
 <<_epsilon B^epsilon (UV + H_i V + H_j U).
```

Stage14-4ay performs the next main-track step:

1. prove that the s5k slicing theorem is stable after **all remaining local state pieces are frozen**, including a root-sign refinement of the state-split norm column;
2. combine this frozen-state discrepancy bound with the s5h/4av rank-one quadratic-large-sieve bulk;
3. sum the complete six-linear **interior** dyadic mode family with a fixed power saving;
4. isolate the only remaining linear-column endpoints: bounded-side lower-dimensional bulk modes and full-factor complementary-state switching.

The state-split norm reciprocal modes themselves remain a separate obstruction.

## 1. Import from s5k: primitive edge coordinates

For every unordered pair from

```text
A=m,
B=n,
C=m-n,
D=m+n,
```

the change of variables

```text
x=L_i(m,n),
y=L_j(m,n)
```

has determinant `+/-1` except `(C,D)`, whose determinant is `+/-2`.

Within the opposite-parity Euclid family,

```text
gcd(x,y)=gcd(m,n).
```

Thus all six reciprocal edges preserve the visible-lattice primitive condition. This is the structural reason the elementary polygon/Möbius argument of s5k works.

Stage14-4ay does not re-prove the bare s5k theorem; it proves the stability statement needed by the full local character expansion.

## 2. Freeze the complete local state

Fix one support/Fourier state from 14-4au and one reciprocal edge `(L_i,L_j)`. Split the squarefree endpoint support as

```text
L_i : a0 * u,
L_j : b0 * v,
```

where `u~U`, `v~V` are the moving reciprocal pieces and `a0,b0` contain every frozen piece on the two endpoint columns. Odd support disjointness gives

```text
gcd(a0*u,b0*v)=1.
```

Write

```text
x=a0*u*r,
y=b0*v*s.
```

Every frozen prime on either of the other two linear columns is a projective root distinct from the two endpoint roots. In `(x,y)` coordinates its equation therefore has two nonzero coefficients modulo that prime.

For the norm column

```text
E=m^2+n^2,
```

refine every split prime `p=1 mod 4` by choosing one root sign `+i_p` or `-i_p`. The number of root-sign refinements is

```text
2^omega(q_E)=B^o(1)
```

on the Stage14 polynomial-height family. Each refined norm root is also distinct from every linear endpoint root.

Chinese remaindering over all frozen auxiliary odd primes therefore reduces their joint condition to one projective congruence

```text
r == c*s (mod R),
```

with

```text
(c,R)=1,
(R,a0*b0*u*v)=1.
```

The exact Q2 table contributes only `O(1)` parity/residue branches.

This is the full-state normal form missing from the bare s5k statement.

## 3. Frozen auxiliary modulus does not worsen the slicing error

Under a fixed edge-coordinate change, a balanced Euclid box maps to a convex polygon with `O(1)` sides and coordinate scales

```text
H_i/(a0*u),
H_j/(b0*v).
```

For a single congruence

```text
r == c*s (mod R),
```

horizontal or vertical slicing gives

```text
# lattice points
 = area/R
 + O(1 + H_i/(a0*u) + H_j/(b0*v)),
```

with an implied constant independent of `R`.

Insert Möbius inversion for `gcd(r,s)=1` and the finite divisor inclusions for

```text
(r,b0*v)=1,
(s,a0*u)=1.
```

All contributing divisors are coprime to `R`, so after division the same one-projective-congruence structure persists. Harmonic summation and the divisor bound cost only `B^o(1)`.

Consequently the **full frozen-state discrepancy** satisfies

```text
boxed:
|Delta_state(u,v)|
 <<_epsilon B^epsilon
    (1 + H_i/(a0*u) + H_j/(b0*v)).
```

In particular,

```text
boxed:
|Delta_state(u,v)|
 <<_epsilon B^epsilon
    (1 + H_i/u + H_j/v).
```

Thus the s5k pointwise theorem is stable under the complete frozen local state. The growing auxiliary modulus does not reappear in the error term.

## 4. Frozen-state L2 theorem

Summing the preceding bound over `u~U`, `v~V` gives

```text
D_state(U,V)
:= sum |Delta_state(u,v)|^2

<<_epsilon B^epsilon
   (UV + H_i^2 V/U + H_j^2 U/V).
```

This is exactly the s5k L2 shape, now with all complementary local state pieces frozen.

By Cauchy-Schwarz,

```text
E_Delta(U,V)
:= sum Delta_state(u,v) (u/v)

<<_epsilon B^epsilon
   (UV + H_i V + H_j U).
```

For balanced geometric scales `H_i,H_j~L`, if

```text
max(U,V) <= L^(1-kappa),
```

then

```text
E_Delta(U,V)
 << L^(2-kappa+epsilon).
```

No lower bound on `min(U,V)` is required for the discrepancy term.

Therefore the six-linear **discrepancy** is now power-saving throughout the medium and microscopic-side ranges, except only at the full-factor upper endpoint.

## 5. Combine with the rank-one quadratic-large-sieve bulk

For the same frozen state, s5i gives a separable rank-one bulk. The s5h/4av quadratic-large-sieve estimate yields schematically on a balanced box

```text
E_bulk(U,V)
 << L^(2+epsilon) sqrt(1/U + 1/V).
```

If the reciprocal block is in the true interior corridor

```text
L^kappa <= U,V <= L^(1-kappa),
```

then

```text
E_bulk(U,V)
 << L^(2-kappa/2+epsilon),
```

while the frozen-state discrepancy satisfies the stronger

```text
E_Delta(U,V)
 << L^(2-kappa+epsilon).
```

Hence the complete frozen six-linear reciprocal mode obeys

```text
boxed:
E_mode(U,V)
 << L^(2-kappa/2+epsilon).
```

There are only `O((log L)^2)` dyadic `(U,V)` boxes, and the support/root-sign/Q2 refinements cost `B^o(1)`. Therefore the full six-linear **interior mode family** sums to

```text
boxed:
E_linear,int(L;kappa)
 << L^(2-kappa/2+o(1)).
```

This closes the combination requested by the s5k boundary for the interior six-linear sector.

## 6. Microscopic discrepancy is closed, microscopic bulk is not

The frozen-state discrepancy theorem remains power-saving when one side is bounded and the other is at most `L^(1-kappa)`.

However, if `u=1`, then

```text
(1/v)=1.
```

The **bulk Fourier mode** loses that reciprocal edge. It must be reclassified as a lower-dimensional character mode.

More generally, bounded-side modes form a finite edge-deletion induction:

```text
reciprocity complexity k
 -> bounded-side mode of complexity <= k-1.
```

Since the reciprocity graph has finitely many edges, the induction terminates. But the quantitative terminal statement is not yet proved: one must show that every terminal mode is either absorbed into the diagonal/local-density main term or still contains another power-saving character edge.

Thus

```text
MICROSCOPIC_DISCREPANCY_CLOSED=true
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_FORMULATED=true
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=false.
```

## 7. Upper endpoint requires a complementary-state switch

The full-mode saving also fails when one moving state piece is almost the whole linear factor:

```text
max(U,V) ~ L.
```

If, for example,

```text
v > L^(1-kappa)
```

and `v` is a squarefree piece of a linear kernel of size `O(L)`, then the complementary kernel piece is `< L^kappa`.

This suggests a divisor/state switch. But the Jacobi/Fourier coefficient must be transformed together with the complementary support piece. Replacing `v` by the complementary divisor inside `(u/v)` without this bookkeeping would be invalid.

Stage14-4ay therefore isolates the exact remaining linear endpoint as

```text
UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH.
```

It is not claimed closed here.

## 8. State-split norm reciprocal modes remain separate

For a linear-linear reciprocal edge, norm primes occur only in the frozen auxiliary state. Root-sign refinement absorbs them into `r=c s mod R`, so they do not spoil the six-linear frozen-state slicing theorem.

The remaining norm obstruction occurs when a reciprocal variable itself is a state-split piece of `E=m^2+n^2`. In two-copy dispersion, s5j gives

```text
q_same | D(P,P'),
q_opp  | S(P,P')=m*n'+m'*n.
```

That mixed `D*S` kernel is not reduced by the six-linear edge coordinates.

Hence the norm frontier is now precisely

```text
STATE_SPLIT_E_RECIPROCAL_DISPERSION.
```

## 9. Main-track consequence

The local six-linear ledger is now

```text
rank-one bulk separability                    proved
bare six-linear pointwise/L2 discrepancy     proved (s5k)
frozen-full-state stability                   proved (14-4ay)
interior bulk + discrepancy mode bound        proved
interior dyadic/support-state summation       proved
microscopic discrepancy                       proved
lower-dimensional microscopic bulk induction formulated, not closed
upper complementary-state Fourier switch      not closed
```

So the first remaining local obstacles are reduced to

```text
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION
+ UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH
+ STATE_SPLIT_E_RECIPROCAL_DISPERSION.
```

No explicit nontrivial `(rho_loc,E_loc)` for the complete local indicator is claimed until those sectors are closed.

## Boundary

```text
STAGE14_4AY=FROZEN_STATE_LINEAR_DISPERSION_STABLE_AND_INTERIOR_FULL_MODE_SUMMED
S5K_SIX_LINEAR_MEDIUM_DISPERSION_IMPORTED=true
FROZEN_AUXILIARY_STATE_SINGLE_PROJECTIVE_CONGRUENCE=true
FROZEN_AUXILIARY_MODULUS_DOES_NOT_WORSEN_SLICING_ERROR=true
FROZEN_STATE_POINTWISE_DISCREPANCY_BOUND_PROVED=true
FROZEN_STATE_L2_DISPERSION_PROVED=true
SIX_LINEAR_MEDIUM_DISCREPANCY_POWER_SAVING_PROVED=true
SIX_LINEAR_INTERIOR_FULL_MODE_POWER_SAVING_PROVED=true
SIX_LINEAR_INTERIOR_DYADIC_STATE_SUMMATION_PROVED=true
MICROSCOPIC_DISCREPANCY_CLOSED=true
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_FORMULATED=true
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=false
UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_CLOSED=false
STATE_SPLIT_E_RECIPROCAL_DISPERSION_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No auxiliary-modulus independence beyond the projective slicing lemma is assumed. No endpoint divisor switch or state-split norm theorem is imported without proof.

```text
NEXT=Stage14-4az close the finite lower-dimensional bulk-mode induction and prove the upper complementary-state Fourier switch for the linear columns, while the s-track attacks the state-split E mixed-sign reciprocal sector
```
