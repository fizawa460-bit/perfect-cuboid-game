# Stage14-t2 — quantitative literature audit

## Browning--Heath-Brown--Salberger

T. D. Browning, D. R. Heath-Brown, P. Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117.

Classification:

```text
REUSABLE_METHOD — UNIFORM_FIXED_DEGREE_DETERMINANT_METHOD
```

The paper gives rational-point bounds uniform in projective varieties of fixed degree and dimension. This is directly relevant to any fixed-degree projective model of the Stage14-t genus-5 fibers. It does not by itself perform the required summation over the moving Pythagorean base with the physical lcm/Euclidean height.

## de la Bretèche--Tenenbaum

Régis de la Bretèche, Gérald Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.

Classification:

```text
REUSABLE_METHOD — MULTIPLICATIVE_PARTIAL_SUM_ASYMPTOTIC
```

Stage14-t2 uses the classical Selberg--Delange mechanism after establishing the exact factorization

```text
F(s)=zeta(s)^6 L(s,chi4)^3 G(s)
```

with an Euler product `G` absolutely convergent near `s=1`. This supplies the fixed logarithmic order `B(log B)^5` for the independent Pythagorean-chain majorant.

## Bonolis--Browning

Dante Bonolis, Tim Browning, *Uniform bounds for rational points on hyperelliptic fibrations*, arXiv:2007.14182.

Classification:

```text
ADJACENT_RESULT / REUSABLE_METHOD — FAMILY_SPECIFIC_UNIFORM_SQUARE_SIEVE
```

Their work demonstrates that strong coefficient-uniform bounds can be obtained for special fibrations by combining a square sieve with exponential-sum estimates. The Stage14-t fiber is instead a simultaneous biquadratic/fiber-product condition; no theorem from this paper is imported directly.

## Dimitrov--Gao--Habegger

Vesselin Dimitrov, Ziyang Gao, Philipp Habegger, *Uniform bound for the number of rational points on a pencil of curves*, arXiv:1904.07268.

Classification:

```text
ADJACENT_RESULT — FAMILY UNIFORMITY WITH MORDELL--WEIL RANK DEPENDENCE
```

This gives a family-level uniformity mechanism for genus at least two, but the bound depends on the Mordell--Weil rank of the fiber Jacobian. Stage14-t has no uniform rank control for its moving genus-5 Jacobians, so it does not imply the desired global `T(B)` estimate.

## Boundary

The t2 search found no primary theorem that can currently be inserted into the exact Stage14 physical-height sum to prove

```text
T(B)=o(sqrt(B))
```

or a fixed `B^(1/2-delta)` upper bound.

```text
DIRECT_STAGE14_T2_SQRT_BOUND=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```
