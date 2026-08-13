# Stage14-s5u — projective all-short refinement and s5 method closure

## Purpose

Stage14-s5t optimized the original s5o three-case graph escape and improved the conservative Euclid-scale saving from `1/200` to `1/41`. The only remaining quantitative bottleneck inside that proof was the all-short sector, where s5o had used the generic centered-periodic estimate

```text
P q + q^2
```

for each complete short modulus tuple and then summed those tuple bounds absolutely.

s5u revisits exactly that step using structural information proved later in s5p and s5q.

The result has two parts.

1. A complete fixed all-short state tuple is not an arbitrary periodic row. After its projective root data are fixed, it is one rank-two projective lattice of index equal to the product state modulus. Geometry of numbers therefore removes the positive `q`-power from the fixed-tuple boundary error: on a regular Stage14 box it is `O_epsilon(M B^epsilon)`, uniformly in the short tuple modulus.
2. The stronger hope that the s5p/s5q Hilbert `ell^2` bounds would also remove the **number of different modulus tuples** is not a valid formal consequence. Those `ell^2` bounds are conditional on a fixed physical support / fixed moving cell. They do not give one global `ell^2`-normalized coefficient vector over all modulus tuples occurring for different physical points.

With the valid projective-lattice refinement, the three-case threshold optimization improves once more:

```text
Euclid-scale saving: M^(-1/21+epsilon)
physical B-scale upper bound: B^(41/42+epsilon).
```

This is extremely close to the pre-existing single-edge boundary exponent `1/20`. Further optimization of the same s5 machinery can improve the Euclid exponent by at most the small gap from `1/21` to `1/20` unless one proves a new single-edge boundary theorem or a genuinely new cross-tuple periodic large sieve. Neither changes the qualitative distance to the desired `B^(1/2)` scale.

Accordingly s5u closes the s5 local-2-descent / reciprocity-sieve method and hands the remaining square-root-scale problem to Stage14-s6.

No new external theorem is used.

---

## 1. Recall the s5t threshold ledger

Let

```text
S=M^sigma
L=M^lambda
```

be the long and very-long thresholds in the linear `K4` reciprocity graph.

The first two s5o escape mechanisms remain unchanged:

```text
Case A, long-long QLS:
  delta_A = sigma/2.

Case B, very-long vertex with only short neighbors:
  delta_B = lambda/2 - 3 sigma/4.
```

The only term to improve is the all-short Case C.

---

## 2. A fixed full linear state tuple is one projective lattice

Fix pairwise odd-coprime squarefree moduli

```text
q_A,q_B,q_C,q_D
```

on the four linear columns

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

Put

```text
Q=q_A q_B q_C q_D.
```

At each odd prime dividing `Q`, exactly one of the four distinct projective roots

```text
0, infinity, +1, -1
```

is imposed. CRT combines all prime conditions into one projective line modulo `Q`.

Equivalently, the integer solutions form one rank-two sublattice

```text
Lambda_sigma subset Z^2
```

with

```text
[Z^2:Lambda_sigma]=det(Lambda_sigma)=Q.
```

This is the full-tuple projective-lattice statement already established geometrically in s5p. In the purely linear all-short `K4` sector there is no extra state-split `E` variable: s5q contracts the `E` star separately to one linear--E edge, and s5r closes that edge.

---

## 3. Fixed-tuple centered discrepancy has no positive Q-power

Let `Omega` be a regular convex Stage14 Euclid box with

```text
area(Omega) asymp M^2,
perimeter(Omega) asymp M.
```

For one fixed full state tuple `sigma`, after the exact local mean has been separated as in s5g, the tuple contribution is a finite bounded linear combination of projective lattice counts and their local-density main terms.

For any rank-two lattice `Lambda` of determinant `Q`, the standard planar lattice count gives

```text
#(Omega intersect Lambda)
 = area(Omega)/Q
   + O(1 + perimeter(Omega)/lambda_1(Lambda)).
```

Every nonzero integer lattice vector has Euclidean length at least `1`, so uniformly

```text
lambda_1(Lambda_sigma) >= 1.
```

Hence the fixed-tuple discrepancy satisfies

```text
|Delta_sigma(Omega)|
 <<_epsilon B^epsilon M.
```

The Möbius inversion for primitiveness contributes only divisor/harmonic factors already absorbed into `B^epsilon`. Fixed mod-4/mod-8 and `Q_2` cases are finite.

This improves the generic microscopic estimate

```text
B^epsilon(M Q + Q^2)
```

used in s5o. The old estimate treated the row as an arbitrary period-`Q` function and ignored that the state support itself is one index-`Q` projective lattice.

Thus

```text
ALL_SHORT_GENERIC_PERIODIC_Q_LOSS_REMOVED=true.
```

---

## 4. Summing the all-short tuples

In Case C every graph-active linear state modulus is below

```text
M^lambda.
```

There are at most four active linear vertices, so the number of possible dyadic integer modulus tuples is bounded crudely by

```text
#Sigma_short << M^(4 lambda).
```

The exact local Fourier coefficients are bounded, and the finite local state/root multiplicities cost only `B^epsilon`. Absolute summation of the valid fixed-tuple projective-lattice discrepancy therefore gives

```text
|S_short|
 <<_epsilon
 B^epsilon M * M^(4 lambda)
 = B^epsilon M^(1+4 lambda).
```

Relative to the physical `M^2` scale, Case C now saves

```text
delta_C = 1 - 4 lambda.
```

No `2-8lambda` or `2-12lambda` term is needed: the `Q^2` boundary-cell artifact disappeared when the projective lattice was used directly.

---

## 5. Why Hilbert energy does not remove the tuple cardinality for free

It is tempting to take the s5q statement

```text
sum_sigma |c_P(sigma)|^2 << 1
```

and conclude that the factor `#Sigma_short` can be deleted by one global Cauchy--Schwarz inequality. That step is not valid.

The quantifiers are different.

The s5q coefficient-energy statement is pointwise in a **fixed physical Euclid point `P`** (or after fixing a moving edge, in its compatible auxiliary state fiber):

```text
for each P:
  ||c_P||_ell2 <= C.
```

Different physical points have different moving prime support and hence different sets of admissible modulus tuples. Embedding all those supports into one universal tuple space does not imply

```text
||c_global||_ell2 <= C.
```

A minimal abstract example makes the issue explicit. Let physical points `P_1,...,P_N` have coefficient vectors

```text
c_{P_j}=e_j
```

in mutually orthogonal tuple coordinates. Then every point individually has norm one, but the union/support vector has norm `sqrt(N)`.

Likewise, the s5p collision-energy theorem is strong after a moving base cell is fixed:

```text
sum_sigma W_sigma(u,v)^2
 << B^epsilon W_base(u,v)^2.
```

If there is no selected moving edge and the base cell is the whole physical box, the right side is already of area scale `M^4` after squaring. It does not by itself supply a power-saving global all-short estimate.

Therefore

```text
HILBERT_GLOBAL_TUPLE_CARDINALITY_ELIMINATION_JUSTIFIED=false.
```

A true removal of the remaining tuple count would require a new cross-tuple periodic/projective large-sieve theorem, not merely reusing the already-proved conditional Hilbert contraction.

This distinction prevents an overclaim while retaining the valid projective-lattice improvement of Sections 2--4.

---

## 6. Exact re-optimization

The valid uniform saving is now

```text
delta(sigma,lambda)
 = min(
     sigma/2,
     lambda/2 - 3 sigma/4,
     1 - 4 lambda
   ).
```

At the optimum, the three terms balance.

First,

```text
sigma/2 = lambda/2 - 3 sigma/4
```

gives

```text
lambda = 5 sigma/2.
```

Write

```text
delta=sigma/2.
```

Then balancing Case C gives

```text
delta = 1 - 4 lambda
      = 1 - 10 sigma
      = 1 - 20 delta.
```

Hence

```text
boxed: delta = 1/21,
boxed: sigma = 2/21,
boxed: lambda = 5/21.
```

At these values,

```text
delta_A=1/21,
delta_B=1/21,
delta_C=1/21.
```

Thus the actual complete local system now satisfies

```text
N_local(M)
 <<_epsilon M^(2-1/21+epsilon).
```

---

## 7. Compatibility with previously closed sectors

The worst previously proved single-linear-edge boundary saving from s5n is

```text
1/20.
```

Since

```text
1/21 < 1/20,
```

that sector remains safely stronger than the new global graph budget.

The s5r near-area `E` mixed-completion exponent with the new short-neighbor threshold `sigma=2/21` is

```text
73/40 + 3 sigma/4
 = 73/40 + 1/14
 = 531/280.
```

Its saving from `M^2` is

```text
2 - 531/280
 = 29/280
 > 1/21.
```

The root-spacing and other central/boundary sectors recorded in s5n/s5r are also stronger than `1/21`.

Therefore no previously closed sector reopens.

---

## 8. Physical-cutoff exponent

Stage14-s5s gives

```text
physical hit below B
 => locally soluble supported descent class
```

and

```text
M <= B^(1/2).
```

Therefore

```text
#Q_B^phys
 <<_epsilon
 (B^(1/2))^(2-1/21+epsilon)
 = B^(41/42+epsilon).
```

So the improved physical upper-bound exponent is

```text
41/42.
```

This supersedes the s5t `81/82` bookkeeping exponent.

---

## 9. Quantitative ceiling of the currently proved s5 modules

After the all-short projective refinement, the global saving is `1/21`.

The nearest already-proved independent bottleneck is the s5n switched-large single-edge boundary saving

```text
1/20.
```

Even if a new cross-tuple theorem eliminated the all-short loss completely, the currently proved module collection could not claim a global exponent larger than `1/20` without reopening that single-edge boundary analysis.

On the physical `B` scale, `1/20` would correspond only to

```text
B^((2-1/20)/2)
 = B^(39/40).
```

Thus continuing to micro-optimize the existing s5 architecture can at best move the present exponent

```text
41/42 = 0.976190...
```

toward

```text
39/40 = 0.975
```

before a new analytic input is required.

That is quantitatively negligible compared with the unresolved gap to the desired/observed `B^(1/2)` scale.

This does **not** prove that `1/20` is an arithmetic barrier. It is only the ceiling of the currently proved s5 module set without proving a new single-edge theorem.

---

## 10. Stage-method decision

The s5 sequence has now accomplished its coherent purpose:

- exact moving-prime full-2-descent local character system;
- reciprocal graph reduction and elimination of fake product-conductor resonances;
- auxiliary progression uniformity;
- state-split `E` tensor collapse;
- root-sawtooth transition closure;
- complete actual local-system power-saving average;
- insertion of the physical logarithmic small-point window as a one-sided majorant;
- first unconditional physical-base power-saving upper bound;
- optimization of all internal bookkeeping losses to the point where the next available gain is tiny and requires a genuinely new theorem.

No unresolved **internal logical gap** remains in the s5 upper-bound chain. What remains is a strength gap: `B^(41/42+epsilon)` is far from `B^(1/2)`.

That strength gap should not be hidden by proliferating `s5v,s5w,...` substages. It requires a new amplification/counting mechanism and therefore belongs in Stage14-s6.

Accordingly:

```text
S5_METHOD_CLOSED=true
NEXT=Stage14-s6
```

---

## Boundary

```text
STAGE14_S5U=COMPLETE_PROJECTIVE_ALL_SHORT_REFINEMENT_AND_S5_METHOD_CLOSURE
FULL_SHORT_STATE_TUPLE_IS_PROJECTIVE_LATTICE=true
FIXED_TUPLE_PROJECTIVE_LATTICE_INDEX_PRODUCT=true
FIXED_TUPLE_CENTERED_DISCREPANCY_O_M=true
ALL_SHORT_GENERIC_PERIODIC_Q_LOSS_REMOVED=true
ALL_SHORT_TUPLEWISE_BOUND=M^(1+4lambda+epsilon)
HILBERT_POINTWISE_COEFFICIENT_ENERGY_RETAINED=true
HILBERT_GLOBAL_TUPLE_CARDINALITY_ELIMINATION_JUSTIFIED=false
HILBERT_QUANTIFIER_MISMATCH_ISOLATED=true
GRAPH_ESCAPE_OPTIMAL_SIGMA=2/21
GRAPH_ESCAPE_OPTIMAL_LAMBDA=5/21
ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/21
ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=41/42
S5R_E_TRANSITION_COMPATIBLE_WITH_S5U_THRESHOLDS=true
CURRENT_PROVED_SINGLE_EDGE_CEILING=1/20
NEW_ARITHMETIC_RESONANCE_FOUND=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_DISTRIBUTION_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
S5_METHOD_CLOSED=true
S5_SUBSTAGE_SPLIT_REQUIRED=false
NEXT=Stage14-s6
```
