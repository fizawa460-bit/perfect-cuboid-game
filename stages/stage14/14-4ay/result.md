# Stage14-4ay — linear-edge slicing dispersion and upper-endpoint boundary

## Result

Stage14-4ax imported the sparse six-linear discrepancy theorem from s5j and left three local objects:

```text
MEDIUM_DETERMINANT_DISPERSION
+ MICROSCOPIC_SMALL_SIDE_INDUCTION
+ NORM_MIXED_SIGN_D_TIMES_S_DISPERSION.
```

Stage14-4ay closes the **medium discrepancy problem for all six reciprocal edges among the four linear Euclid columns** by a more direct argument than determinant averaging. The key is to use the two edge forms themselves as coordinates, refine the frozen auxiliary norm state by root signs, and count the resulting projective congruence by lattice slicing plus Möbius inversion.

This does not yet close the complete local indicator. The bulk modes at exact/small reciprocal side, the upper complementary-divisor endpoint, and reciprocal edges involving state-split `m^2+n^2` pieces remain separate.

## 1. Six linear edges admit primitive coordinates

Write

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

For every unordered pair `Li,Lj` from `{A,B,C,D}`, put

```text
x=Li(m,n),
y=Lj(m,n).
```

The coefficient determinant is `+/-1` for five of the six pairs and `+/-2` for the pair `(C,D)`.

For primitive opposite-parity Euclid pairs,

```text
gcd(x,y)=1
```

for all six pairs. Conversely, within the corresponding parity class, `gcd(x,y)=1` is equivalent to `gcd(m,n)=1`.

For `(C,D)` this uses that `C,D` are odd and

```text
gcd(m-n,m+n) | 2,
```

so their gcd is exactly `1` in the primitive opposite-parity family.

Thus each linear reciprocal edge has a coordinate system in which the primitive condition is again the ordinary visible-lattice condition.

## 2. Frozen full local state becomes one projective congruence

Fix one Fourier/support state from 14-4au and one reciprocal edge between `Li,Lj`. Split the squarefree endpoint support as

```text
Li : a0 * u,
Lj : b0 * v,
```

where `u~U`, `v~V` are the two moving reciprocal pieces and `a0,b0` contain all frozen pieces on those two columns. Odd support disjointness gives

```text
gcd(a0*u,b0*v)=1.
```

Write

```text
x=a0*u*r,
y=b0*v*s.
```

Every frozen odd prime on either of the other two linear columns imposes a projective root different from the `x=0` and `y=0` roots. Therefore in `(x,y)` coordinates it has both coefficients nonzero modulo that prime.

For the norm column `E=m^2+n^2`, refine each split prime `p=1 mod 4` by choosing one of the two roots `+i_p,-i_p`. This root-sign refinement costs at most

```text
2^omega(q_E)=B^o(1)
```

across a Stage14 polynomial-height box. Each refined norm branch is again a projective root distinct from the two endpoint roots.

Chinese remaindering over every frozen auxiliary odd prime therefore produces one congruence

```text
r == c*s (mod R),
```

with

```text
gcd(c,R)=1,
gcd(R,a0*b0*u*v)=1.
```

The exact Q2 state contributes only finitely many parity/residue branches and does not create a growing odd modulus.

So, after freezing the full structural state and refining norm signs, the incidence coefficient is reduced to a visible-lattice count in a transformed convex box with one projective congruence.

## 3. Uniform slicing lemma

Let the original `(m,n)` rectangle have side lengths `X,Y` with

```text
X~Y~L.
```

Under a fixed linear-edge change of variables its image is a convex polygon with `O(1)` sides and diameter/perimeter `O(L)`. After dividing by `a0*u` and `b0*v`, the effective coordinate scales are

```text
A_* ~ L/(a0*u),
B_* ~ L/(b0*v).
```

Consider first the count without the visible-lattice condition. For one congruence

```text
r == c*s (mod R),  (c,R)=1,
```

slice the polygon by integer `s`. On each horizontal slice the admissible `r` form one residue class modulo `R`; hence the count on that slice is its length divided by `R` plus `O(1)`. Summing the slice lengths differs from polygonal area by `O(A_*+B_*+1)`. Repeating with vertical slices if desired gives the uniform estimate

```text
#(congruence points)
 = area/R + O(A_*+B_*+1),
```

with an implied constant depending only on the fixed edge geometry, not on `R`.

This independence from the frozen auxiliary modulus is the crucial point.

## 4. Möbius and endpoint-coprimality completion

Because

```text
x=a0*u*r,
y=b0*v*s,
```

and the endpoint moduli are coprime, primitiveness is equivalent to

```text
gcd(r,s)=1,
gcd(r,b0*v)=1,
gcd(s,a0*u)=1.
```

Insert

```text
1_{gcd(r,s)=1} = sum_{d|r,s} mu(d)
```

and the two finite divisor inclusions for the endpoint coprimality conditions. Every contributing `d` is coprime to the frozen projective modulus `R`, so after dividing by `d` the congruence remains a single invertible projective congruence.

Applying the slicing lemma termwise gives the exact s5i rank-one density as the main term. The total error is bounded by the harmonic sum over `d` and the subpower number of squarefree endpoint divisors:

```text
Delta_state(u,v)
 <<_epsilon B^epsilon
    ( L/(a0*u) + L/(b0*v) + 1 ).
```

Dropping the helpful frozen factors `a0,b0>=1`,

```text
boxed:
|Delta_state(u,v)|
 <<_epsilon B^epsilon (L/u + L/v + 1).
```

The bound is uniform in the frozen auxiliary odd modulus `R`; root-sign refinement and Q2 branching cost only `B^o(1)`.

This is a theorem for the six linear reciprocal edges. It does not assert the analogous statement when one of the reciprocal variables itself is a state-split norm-column piece.

## 5. Dyadic L2 dispersion for the six linear edges

Sum over odd squarefree

```text
u~U,
v~V.
```

Using the pointwise bound and `#u=O(U), #v=O(V)` gives

```text
D_lin(U,V)
:= sum_{u~U} sum_{v~V} |Delta_state(u,v)|^2

<<_epsilon B^epsilon
   [ L^2(V/U + U/V + 1) + UV ].
```

The harmless `+1` may be absorbed into the displayed terms for `U,V>=1`.

Hence

```text
boxed:
D_lin(U,V)
 <<_epsilon B^epsilon
    ( L^2(V/U + U/V) + UV + L^2 ).
```

This is the missing medium-range second-moment estimate for the six linear edges.

It is stronger than the raw determinant-divisor reduction from s5j because the special Euclid linear forms permit a direct coordinate normalization before the second moment is taken.

## 6. Transfer to the reciprocal error

For the discrepancy character block,

```text
E_Delta(U,V)
 = sum_{u~U} sum_{v~V}
   Delta_state(u,v) (u/v),
```

Cauchy-Schwarz and `|(u/v)|<=1` give

```text
|E_Delta(U,V)|
 <= (UV)^(1/2) D_lin(U,V)^(1/2)

<<_epsilon B^epsilon
   [ L(U+V) + UV + L*sqrt(UV) ].
```

In particular, for any fixed `kappa>0`, if

```text
max(U,V) <= L^(1-kappa),
```

then

```text
boxed:
E_Delta(U,V)
 <<_epsilon L^(2-kappa+epsilon).
```

There is **no lower bound required on `min(U,V)`** for this discrepancy estimate. Thus the finite-box/Möbius discrepancy is power-saving even when one reciprocal side is microscopic, provided the other side is not at the full linear-factor scale.

This closes the `Delta` part of the medium/microscopic six-linear problem.

## 7. What remains at a microscopic side

The previous statement concerns the discrepancy only. If `u=1`, then

```text
(1/v)=1.
```

The corresponding **rank-one bulk Fourier mode** therefore loses one reciprocal edge entirely. It must be reclassified as a lower-dimensional character mode, as already identified in 14-4ax.

More generally, bounded `u` produces a finite collection of lower-complexity character modes. Stage14-4ay organizes these by edge deletion:

```text
edge complexity k
 -> bounded-side modes of complexity <= k-1.
```

Because the reciprocity graph has finitely many edges, this gives a finite induction scheme. What is still missing is a quantitative theorem showing that every terminal lower-dimensional bulk mode either belongs to the diagonal density or retains another character edge with a fixed-power saving.

Therefore

```text
MICROSCOPIC_DISCREPANCY_CLOSED=true
FULL_MICROSCOPIC_BULK_INDUCTION_CLOSED=false.
```

## 8. Upper endpoint and complementary divisors

The L2 transfer loses its fixed power when

```text
max(U,V) ~ L.
```

This is the genuine upper endpoint. If, for example, a squarefree state piece `v` occupies almost the whole kernel of a linear factor `F_j(P)=O(L)`, then its complementary kernel piece has size

```text
v_comp << L/v.
```

For

```text
v > L^(1-kappa)
```

this complementary piece is `< L^kappa`.

Thus the next endpoint mechanism is a complementary-divisor/state switch. However the local Fourier coefficient and Jacobi edge must be rewritten together with the complementary state piece; merely replacing `v` by `F_j/v` would be invalid. Stage14-4ay records the switch interface but does not claim the bookkeeping theorem.

## 9. Norm-column boundary is now cleaner

For a **linear-linear reciprocal edge**, state-split norm primes only occur inside the frozen auxiliary state. Root-sign refinement converts them to the single congruence `r=c s mod R`, so the s5j mixed-sign `D*S` collision is not an obstruction to the six-linear first-moment discrepancy theorem above.

The mixed-sign obstruction survives precisely when a reciprocal variable itself belongs to a split `E=m^2+n^2` state piece. Then two-copy dispersion sees

```text
q_same | D(P,P'),
q_opp  | S(P,P')=m*n'+m'*n,
```

and the six-linear coordinate argument no longer supplies two independent linear endpoint coordinates.

Hence the remaining norm problem is isolated to

```text
RECIPROCAL_MODES_INVOLVING_STATE_SPLIT_E_PIECES.
```

## 10. Main-track consequence

The local analytic ledger is now

```text
six linear reciprocal edges:
  rank-one bulk interior saving         proved (14-4av/4aw)
  sparse natural-diagonal L2            proved (s5j/4ax)
  frozen-state discrepancy medium L2    proved (14-4ay)
  microscopic discrepancy               proved (14-4ay)
  bounded-side bulk modes               finite edge-deletion induction, not closed
  upper full-factor endpoint            complementary-state switch not closed

norm reciprocal modes:
  whole-kernel collapse                 proved (s5h)
  state-split E mixed-sign modes        not closed.
```

So the previous frontier

```text
MEDIUM_DETERMINANT_DISPERSION
+ MICROSCOPIC_SMALL_SIDE_INDUCTION
+ NORM_MIXED_SIGN_D_TIMES_S_DISPERSION
```

is sharpened to

```text
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION
+ UPPER_COMPLEMENTARY_STATE_SWITCH
+ STATE_SPLIT_E_RECIPROCAL_DISPERSION.
```

The six-linear discrepancy is no longer the first local obstruction.

## Boundary

```text
STAGE14_4AY=SIX_LINEAR_FROZEN_STATE_DISCREPANCY_L2_POWER_SAVING_PROVED
SIX_LINEAR_EDGE_PRIMITIVE_COORDINATES=true
AUXILIARY_NORM_ROOT_SIGN_REFINEMENT_SUBPOWER=true
FROZEN_AUXILIARY_STATE_SINGLE_PROJECTIVE_CONGRUENCE=true
SLICING_ERROR_UNIFORM_IN_AUXILIARY_MODULUS=true
SIX_LINEAR_POINTWISE_DISCREPANCY_BOUND_PROVED=true
SIX_LINEAR_DYADIC_L2_DISPERSION_PROVED=true
SIX_LINEAR_MEDIUM_DISCREPANCY_POWER_SAVING_PROVED=true
MICROSCOPIC_DISCREPANCY_CLOSED=true
FULL_MICROSCOPIC_BULK_INDUCTION_CLOSED=false
UPPER_COMPLEMENTARY_STATE_SWITCH_CLOSED=false
STATE_SPLIT_E_RECIPROCAL_DISPERSION_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No determinant-distribution theorem beyond the six-linear coordinate structure is claimed. No complementary-divisor Fourier rewrite and no state-split norm reciprocal theorem is silently imported.

```text
NEXT=Stage14-4az close the finite lower-dimensional bulk-mode induction and formulate/prove the upper complementary-state switch for linear columns; in parallel isolate the state-split E reciprocal modes for the s5 norm-dispersion track
```
