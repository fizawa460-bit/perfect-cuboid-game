# Stage14-s5 — uniform small-point / activation theorem boundary

## Purpose

After Stage14-4ak closed every fixed physical Q-rational M-degree-4 curve mechanism and Stage14-s4c converted any higher-degree explanation into a required proliferation exponent, Stage14-s5 asks which existing elliptic-curve small-point theorems can actually control

\[
V(B)=\#\{F=(S,X,H):\mu(F)\le B\}
\]

over the moving primitive Pythagorean base family.

## Existing single-fiber inputs

For

\[
E_F: W^2=Z(Z-S^2)(Z+X^2),
\]

every fiber has full rational 2-torsion. The literature therefore supplies strong **single-curve** tools:

1. Petsche gives an effective lower bound for the canonical height of a non-torsion rational point in terms of the minimal discriminant and Szpiro ratio.
2. Naccarato gives, for elliptic curves over Q with rational 2-torsion, a subpolynomial-in-height upper bound for the number of rational points of bounded Weil height; in the full-2-torsion case this is compatible with the Bombieri--Zannier framework.
3. Newer uniform torsion-family bounds preserve the same qualitative conclusion: one fixed fiber contains only `B^{o(1)}` rational points up to exponential height `B`.

These inputs are useful for controlling multiplicity **inside one active fiber**.

## Why this does not bound V(B)

Stage14-4al counts eligible primitive oriented Pythagorean bases with

\[
A(B)=B/\pi+O(\sqrt B\log B).
\]

A uniform per-fiber estimate of the shape

\[
\#\{P\in E_F(\mathbf Q):H(P)\le B^C\}\le B^{o(1)}
\]

only yields the trivial family sum

\[
\sum_{H(F)\le B}\#\{P\text{ small on }E_F\}\le B^{1+o(1)}.
\]

It does **not** imply a power saving for the number of fibers possessing at least one physical small point. In particular it cannot by itself prove

\[
V(B)\ll B^{1/2+o(1)}.
\]

The obstruction is logical rather than quantitative: point-counting on each fiber controls multiplicity conditional on activation, whereas Stage14 needs a theorem controlling the **activation probability/density across fibers**.

## Required theorem shape

A Stage14-closing arithmetic theorem must contain genuine averaging over the primitive Pythagorean family. Any one of the following would be structurally sufficient:

### A. direct activation-density estimate

For every `epsilon>0`,

\[
\#\{F:H(F)\le B,\ \exists\ P\in E_F(\mathbf Q)_{nt}\text{ in the physical height window}\}
\ll_\epsilon B^{1/2+\epsilon}.
\]

### B. averaged least-height tail

A uniform tail bound for the least physical/non-torsion height `lambda(F)` strong enough that

\[
\sum_{H(F)\le B} 1_{\lambda(F)\le C\log B}
\ll B^{1/2+o(1)}.
\]

### C. descent-class large sieve

Using Stage14-s2/s4b, the relevant Kummer square classes are supported on primes dividing `2SXH` and are highly dispersed. A large-sieve/character-sum theorem over Euclid parameters `(m,n)` that shows physical-soluble descent classes occur on at most `B^{1/2+o(1)}` bases would directly attack `V(B)`.

### D. average-rank plus uniform least-point theorem

An average-rank statement alone is insufficient. It becomes useful only if combined with a uniform theorem forcing a positive-rank Pythagorean fiber to have a physical point below the Stage14 window with sufficiently small probability.

## Most promising Stage14-specific route

The strongest current route is **C**, not a direct application of a generic single-curve height theorem.

Stage14 already has the needed structural reductions:

- full rational 2-torsion on every `E_F`;
- Kummer classes supported inside the moving bad-prime set `p|2SXH`;
- exact-class dispersion: `483/490` distinct among active fibers;
- coarse dispersion: `393/490` signatures, `326` singleton signatures;
- fixed M-degree-4 accumulating curves eliminated by Stage14-4ak.

Thus the remaining target is an averaged local-solubility/descent problem over primitive Euclid parameters, with the small-point height window imposed after descent.

## Boundary

```text
STAGE14_S5=COMPLETE_UNIFORM_SMALL_POINT_THEOREM_BOUNDARY
PETSche_SINGLE_FIBER_HEIGHT_LOWER_BOUND_RELEVANT=true
NACCARATO_SINGLE_FIBER_BOUNDED_HEIGHT_COUNT_RELEVANT=true
SINGLE_FIBER_POINT_COUNT_SUFFICIENT_FOR_VB_POWER_SAVING=false
AVERAGE_RANK_ALONE_SUFFICIENT=false
FAMILY_LEVEL_ACTIVATION_THEOREM_REQUIRED=true
PREFERRED_NEXT_ROUTE=PYTHAGOREAN_2_DESCENT_LARGE_SIEVE_WITH_SMALL_POINT_WINDOW
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5a formulate the explicit Euclid-parameter descent-class sieve target
```

## References

- Clayton Petsche, *Small rational points on elliptic curves over number fields*, New York J. Math. 12 (2006), arXiv:math/0508160.
- Francesco Naccarato, *Counting rational points on elliptic curves with a rational 2-torsion point*, arXiv:2105.04032 (2021).
- Marta Dujella, *Uniform bounds for the number of rational points of bounded height on certain elliptic curves*, Acta Arith. 217 (2025), 309--332.
