# Stage14-s7-10 — uniform adjacent-two-cell mixed Fourier theorem and the 13/14 bound

## Purpose

Merged Stage14-s7-09 reduced the next improvement to a single complete-sum question for the universal adjacent-two-cell polynomial

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2)
      =(1-RS)(1+RS)(S-R)(S+R).
```

For an odd inert prime `p=3 mod 4`, write

```text
T_p(h,k)
 = sum_{R,S mod p} chi_p(H(R,S)) e_p(hR+kS),
```

where `chi_p(0)=0`.

Stage14-s7-09 proved `T_p(0,0)=0` and finite evidence for `|T_p(h,k)|=O(p)`, but deliberately left the uniform theorem open.  This stage closes that theorem by splitting the Fourier plane into the generic stationary-phase chamber, two exact-cancellation diagonals, and the two coordinate axes.

During this stage the merged main track advanced independently: Stage14-4bx reoptimized the already-proved thick-packet inequality and improved the unconditional whole-family exponent from `18/19` to `15/16`.  The conditional two-cell target therefore also changed from the historical `16/17` ledger of s7-09 to the updated `13/14` ledger recorded in merged 4bx.

The result of the present stage is

```text
boxed:
|T_p(h,k)| << p
```

uniformly in every additive frequency `(h,k)` for all sufficiently large good inert primes `p=3 mod 4`; finitely many fixed bad primes are harmless in the square sieve.

Consequently the adjacent two-cell rectangle receiver becomes unconditional,

```text
N_2cell(A,B) << (A*B)^(2/3) B_global^o(1),
```

and combining it with the optimized thick-packet theorem of merged 4bx gives

```text
boxed:
V(B) << B^(13/14+o(1)).
```

No perfect-cuboid nonexistence statement is made.

---

## 1. Merged inputs and current ledger

### 1.1 Stage14-s7-09

The merged predecessor proves:

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2),
T_p(0,0)=0
```

for every inert odd prime, and shows that the desired all-frequency estimate

```text
|T_p(h,k)| << p                                      (1.1)
```

implies the two-cell square-sieve receiver

```text
N_2cell(A,B) << (A*B)^(2/3) B_global^o(1).           (1.2)
```

The factor `(A*B)^(-1/3)` is the improvement over the ambient two-cell coefficient volume.

### 1.2 Stage14-4bx

Merged 4bx independently strengthens the thick square-part packet estimate to

```text
N_packet << M*Hmin^(-4/5) B_global^o(1),             (1.3)
```

and therefore proves the current unconditional whole-family theorem

```text
V(B) << B^(15/16+o(1)).                              (1.4)
```

It also records the exact updated minimax if (1.2) is later made unconditional:

```text
lambda = 13/28,
nu     = 11/28,
tau    = 5/56,
E      = 13/14.                                      (1.5)
```

The present stage proves the missing hypothesis (1.1), so (1.5) becomes an unconditional ledger.

---

## 2. External theorem contract

The external input is the Fourier/stationary-phase package of Katz--Laumon, together with the usual one-dimensional Weil-II/Grothendieck--Ogg--Shafarevich consequence for a fixed-conductor lisse family.

Primary source:

- N. Katz and G. Laumon, *Transformation de Fourier et majoration de sommes exponentielles*, Publ. Math. IHES 62 (1985).
- N. Katz, *Estimates for Nonsingular Mixed Character Sums* (2007), used only as a comparison/check on the nonsingular Deligne-polynomial shortcut.

The precise contract used here is the following standard specialization of Fourier--Deligne stationary phase.

> **KL surface stationary-phase contract.**  Let `U` be the complement of a fixed simple-normal-crossing divisor in a smooth affine surface over `Z[1/N]`.  Let `L` be a rank-one tame Kummer local system with nontrivial local monodromy around every irreducible component.  For an additive linear form `ell`, assume that after the fixed normal-crossing compactification:
>
> 1. every finite stratified stationary point is isolated and nondegenerate;
> 2. every positive-dimensional stationary boundary stratum is removed or treated separately;
> 3. on every remaining infinity component the Artin--Schreier factor has a nonzero pole.
>
> Then the complete mixed trace on the two-dimensional affine surface is `O(q)`, with a constant depending only on the fixed divisor/stratification, not on the finite field or the additive frequency inside that chamber.

This is the dimension-two trace consequence of the Katz--Laumon facts that Fourier transform preserves perversity, preserves purity with the standard Fourier weight shift, and has uniformly bounded stalk complexity for a fixed stratification.

We do **not** invoke Katz 2007 Theorem 1.1 directly.  Its Deligne-polynomial hypothesis requires a smooth highest-degree projective hypersurface.  For the present `H`, the degree-six highest homogeneous part is

```text
-H_6 = R^2*S^2*(S^2-R^2),
```

which has repeated factors `R^2 S^2`; therefore the direct nonsingular-polynomial shortcut is invalid.

Likewise, the general Katz--Laumon finite-map theorem that allows a finite exceptional set of multiplicative-character orders is not by itself enough: our character has fixed order `2`.  Instead we audit the quadratic Kummer local monodromy and the stationary strata explicitly below.

---

## 3. The divisor is simple normal crossing

Over every field of characteristic different from `2`, write

```text
D1: 1-RS=0,
D2: 1+RS=0,
D3: S-R=0,
D4: S+R=0.
```

Then

```text
H=D1*D2*D3*D4.                                      (3.1)
```

Each component is smooth:

- `D1,D2` are smooth hyperbolas;
- `D3,D4` are smooth lines.

The two hyperbolas are disjoint, while the two lines meet transversely at `(0,0)`.  A line and a hyperbola meet only in transverse points.  No three components meet in odd characteristic.

Hence

```text
boxed:
D={H=0} is an SNC divisor on A^2 over Z[1/2].        (3.2)
```

Every component occurs with multiplicity one.  For the quadratic character, local Kummer monodromy around every component is therefore the nontrivial sign `-1`.  Thus there is no local order-two trivial-monodromy defect on the finite divisor.

This is precisely the local condition that is lost if one only looks at the singular highest homogeneous part of `H`.

---

## 4. Generic Fourier chamber

Let

```text
ell_{h,k}(R,S)=hR+kS.
```

Assume

```text
h*k*(h^2-k^2) != 0.                                 (4.1)
```

We check every finite divisor component.

### 4.1 Line components

On `D3: S=R`,

```text
ell=(h+k)R.
```

Because `h+k!=0`, there is no stationary point along this component.

On `D4: S=-R`,

```text
ell=(h-k)R,
```

and `h-k!=0` again gives no stationary point.

### 4.2 Hyperbola `RS=1`

Put `S=1/R`.  Then

```text
ell=hR+k/R,
d ell/dR = h-k/R^2.
```

The critical equation is

```text
R^2=k/h.                                            (4.2)
```

It has two geometric solutions.  At either solution,

```text
d^2 ell/dR^2 = 2k/R^3 != 0,                         (4.3)
```

so both are Morse.

### 4.3 Hyperbola `RS=-1`

Put `S=-1/R`.  Then

```text
ell=hR-k/R,
d ell/dR = h+k/R^2.
```

The critical equation

```text
R^2=-k/h                                             (4.4)
```

again gives two geometric points, with nonzero second derivative.

Thus every finite stratified stationary point in (4.1) is isolated and nondegenerate.

### 4.4 Infinity

Compactify in `P^1 x P^1`.  The Kummer divisor has even order along the two coordinate infinity divisors, so the quadratic Kummer factor itself creates no new odd-multiplicity ramification there.  The additive phase has a simple pole in the `R`-infinity direction when `h!=0` and a simple pole in the `S`-infinity direction when `k!=0`.

Hence in chamber (4.1) the Artin--Schreier factor is nontrivially wild on both infinity directions.  There is no positive-dimensional stationary infinity stratum.

All hypotheses of the KL surface stationary-phase contract are therefore satisfied, and

```text
boxed:
|T_p(h,k)| << p
for h*k*(h^2-k^2)!=0.                               (4.5)
```

The implied constant is absolute for this fixed polynomial.

---

## 5. The two diagonal frequencies cancel exactly

These are exactly the finite positive-dimensional stationary directions of the two line components, but they need no estimate.

### 5.1 `h=k`

Swapping the variables gives

```text
H(S,R)=-H(R,S).
```

For `p=3 mod 4`,

```text
chi_p(-1)=-1.
```

The additive phase `h(R+S)` is invariant under the swap, so

```text
T_p(h,h)=-T_p(h,h),
```

and therefore

```text
boxed:
T_p(h,h)=0.                                         (5.1)
```

### 5.2 `h=-k`

Use the involution

```text
(R,S) -> (-S,-R).
```

Again `H` changes sign, while `h(R-S)` is invariant.  Hence

```text
boxed:
T_p(h,-h)=0.                                        (5.2)
```

This includes every nonzero diagonal frequency.  The origin was already proved zero in s7-09.

---

## 6. Axis frequencies: genus-one family plus Artin--Schreier twist

The only frequencies not covered by Sections 4--5 are

```text
(h,0),  h!=0,
(0,k),  k!=0.                                       (6.1)
```

Here one additive coefficient vanishes, so the two-dimensional infinity argument should not be used blindly.  We reduce instead to a one-dimensional fixed-conductor family.

Define the row trace

```text
A(S)=sum_R chi_p(H(R,S)).                            (6.2)
```

As a polynomial in `R`,

```text
H(R,S)
 =(R-S)(R+S)(RS-1)(RS+1)
```

up to an irrelevant global sign/square convention.  Its discriminant in `R` is exactly

```text
boxed:
Disc_R H = 16*S^4*(S^4-1)^4.                       (6.3)
```

Therefore outside the fixed geometric parameter set

```text
S=0,
S^4=1,
infinity,                                           (6.4)
```

the double cover

```text
Y^2=H(R,S)                                          (6.5)
```

is a smooth genus-one curve.  Its first cohomology forms a rank-two lisse sheaf of weight one on the complement of the fixed set (6.4), with bounded conductor independent of `p`.

For `k!=0`, tensor this sheaf by the nontrivial Artin--Schreier sheaf `L_psi(kS)`.  The twist is wild at infinity, so it has no geometric invariant quotient there; consequently the compactly supported cohomology has no top-degree invariant term.  Grothendieck--Ogg--Shafarevich bounds the remaining first-cohomology dimension by an absolute constant, and Weil II gives weight at most two.

The finitely many singular parameters in (6.4) contribute only `O(1)` pointwise terms.  Hence

```text
boxed:
T_p(0,k) << p
for k!=0.                                           (6.6)
```

Finally the swap identity gives

```text
T_p(h,0)=-T_p(0,h),                                 (6.7)
```

so the same bound holds on the other axis.

---

## 7. Uniform all-frequency theorem

Sections 4--6 and merged s7-09 at the origin exhaust the Fourier plane.  Thus for every sufficiently large odd inert prime

```text
p == 3 (mod 4)
```

and every `(h,k) in F_p^2`,

```text
boxed:
|T_p(h,k)| <= C*p                                   (7.1)
```

for an absolute constant `C` depending only on the fixed polynomial `H`.

All finitely many primes excluded by the fixed SNC model, the external stationary-phase spreading-out integer, or the fixed genus-one conductor can be deleted from the auxiliary sieve-prime set at `B^o(1)` cost.

Therefore

```text
boxed:
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true. (7.2)
```

This upgrades the central false flag of merged s7-09.

---

## 8. Two-cell rectangle square sieve

With (7.1), CRT gives the same square-root-in-dimension-two Fourier bound for a squarefree product of two good inert auxiliary primes.  Fourier completion over a dyadic adjacent-cell rectangle and the square sieve now give the receiver already derived conditionally in s7-09:

```text
boxed:
N_2cell(A,B)
 << (A*B)^(2/3) * B_global^o(1).                   (8.1)
```

Thus a large adjacent coefficient `C=A*B` receives relative saving

```text
boxed:
C^(-1/3).                                           (8.2)
```

This is strictly stronger than the one-cell balanced saving `C^(-1/4)` used in s7-08/4bw/4bx.

---

## 9. Updated minimax after merged 4bx

Use the 4bx notation

```text
lambda : small-denominator threshold,
nu     : small-numerator threshold,
tau    : square-part threshold.
```

The five exhaustive sector exponents are now

```text
E1 = 2*lambda,
E2 = 1+nu-lambda,
E3 = 1-4*tau/5,
E4 = 1-(nu-2*tau)/3,
E5 = 1-(lambda-2*tau)/3.                            (9.1)
```

Because `nu<=lambda`, `E5<=E4`.

Take

```text
boxed:
lambda = 13/28,
nu     = 11/28,
tau    = 5/56.                                      (9.2)
```

Then

```text
E1 = 13/14,
E2 = 13/14,
E3 = 13/14,
E4 = 13/14,
E5 = 19/21 < 13/14.                                 (9.3)
```

This is the updated conditional ledger already recorded in merged 4bx; the present theorem makes its only conditional input unconditional.

Hence

```text
boxed:
V(B) << B^(13/14+o(1)).                             (9.4)
```

The improvement over the merged `15/16` theorem is

```text
15/16 - 13/14 = 1/112.                              (9.5)
```

The cumulative saving from the post-local `41/42` baseline is

```text
41/42 - 13/14 = 1/21.                               (9.6)
```

The remaining gap to the square-root exponent is

```text
13/14 - 1/2 = 3/7.                                  (9.7)
```

---

## 10. Boundary and next target

What is proved here:

- the direct Katz-2007 Deligne-polynomial shortcut is inapplicable to `H` because the top homogeneous part has repeated factors;
- the finite divisor `H=0` is an SNC union of four multiplicity-one components;
- quadratic Kummer monodromy is nontrivial on each finite component;
- for `hk(h^2-k^2)!=0`, all finite stationary points are isolated Morse and both infinity directions carry nontrivial Artin--Schreier poles;
- the two diagonal Fourier lines cancel exactly;
- the two coordinate axes reduce to a fixed genus-one family with discriminant `16*S^4*(S^4-1)^4`, and the nontrivial additive twist gives `O(p)` by one-dimensional Weil-II/GOS;
- therefore the adjacent-two-cell transform satisfies the uniform all-frequency bound `O(p)`;
- the two-cell rectangle receiver `(A*B)^(2/3)` is unconditional;
- after importing merged 4bx, the whole-family exponent is `13/14`.

What is not proved:

- any three-cell/four-cell analogue stronger than coefficient saving `C^(-1/3)`;
- a whole-family exponent below `13/14`;
- the square-root upper bound;
- perfect-cuboid nonexistence.

```text
STAGE14_S7_10=COMPLETE_UNIFORM_ADJACENT_TWO_CELL_MIXED_FOURIER_AND_13_14_BOUND
MERGED_S7_09_IMPORTED=true
MERGED_4BX_IMPORTED=true
DIRECT_KATZ_2007_DELIGNE_POLYNOMIAL_SHORTCUT_APPLICABLE=false
H_DIVISOR_SIMPLE_NORMAL_CROSSING=true
QUADRATIC_KUMMER_LOCAL_MONODROMY_NONTRIVIAL=true
GENERIC_TWO_CELL_STATIONARY_POINTS_ISOLATED_MORSE=true
NONZERO_DIAGONAL_FOURIER_TRACES_EXACT_ZERO=true
AXIS_GENUS_ONE_DISCRIMINANT=16*S^4*(S^4-1)^4
AXIS_FOURIER_BOUND=O(p)
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true
TWO_CELL_RECTANGLE_EXPONENT=2/3
TWO_CELL_COEFFICIENT_RELATIVE_SAVING=C^(-1/3)
OPTIMAL_DENOMINATOR_CUTOFF_EXPONENT=13/28
OPTIMAL_NUMERATOR_CUTOFF_EXPONENT=11/28
OPTIMAL_SQUAREPART_THRESHOLD_EXPONENT=5/56
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14
IMPROVEMENT_OVER_15_16=1/112
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/21
CURRENT_GAP_TO_SQRT=3/7
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-s7-11
```
