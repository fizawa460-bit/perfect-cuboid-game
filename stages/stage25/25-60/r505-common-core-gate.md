# Stage25-60 R505 — common squarefree-core receiver boundary

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R505
ROLE=ITERATIVE_CHECKPOINT60_DEEP_RESEARCH

## 1. R505 is the exact Stage19 target receiver

Use the primitive toric Stage19 coordinates

\[
E=4mnrs,
\qquad
X=2rs(m^2-n^2),
\qquad
Y=2mn(r^2-s^2).
\]

Put

\[
A=m^2r^2+n^2s^2,
\qquad
B=m^2s^2+n^2r^2.
\]

The two guaranteed face identities are

\[
E^2+X^2=\bigl(2rs(m^2+n^2)\bigr)^2,
\]

\[
E^2+Y^2=\bigl(2mn(r^2+s^2)\bigr)^2,
\]

and the space identity is

\[
E^2+X^2+Y^2=4AB.
\]

After the primitive physical gcd normalization used by Stage19, the space diagonal is integral exactly when `AB` is a rational square. Because `A,B` are positive integers, this is equivalent to equality of their squarefree parts:

\[
\boxed{\operatorname{sf}(A)=\operatorname{sf}(B).}
\]

Equivalently there is a unique positive squarefree `k` and positive integers `P,Q` such that

\[
\boxed{A=kP^2,\qquad B=kQ^2.}
\]

Thus the common-core condition is not an additional construction ansatz. It is an exact reformulation of the Stage19 space condition inside the two-face toric population.

```text
R505_EXACT_TARGET_RECEIVER=true
R505_A=m^2r^2+n^2s^2
R505_B=m^2s^2+n^2r^2
R505_SPACE_CONDITION=sf(A)=sf(B)
R505_COMMON_CORE=A=kP^2,B=kQ^2
R505_RECEIVER_IS_NOT_CONSTRUCTION_BY_ITSELF=true
```

## 2. Fixed-core slices do not explain the global quarter-power lower

Fixing the squarefree core and the finite local/cell decorations reduces the remaining rational-point problem to degree-four genus-one / elliptic receivers already isolated in the Stage15 deep cycle. A fixed finite collection of such curves has fixed Mordell-Weil rank and ordinary fixed-curve height growth; it can contribute only polylogarithmically many multiples under a polynomial physical-height cutoff unless a separate rational parametrization is present.

This statement is only about a **fixed finite collection of core/cell genus-one slices**. It is not a global upper bound for Stage19 and does not exclude special explicit families such as audited R501/R502, whose parameter geometry gives the stronger `B^(1/4)` lower.

Hence an exponent improvement from R505 cannot come merely from choosing one more fixed core and walking along one elliptic orbit. It must exploit the moving-core family quantitatively or exhibit genuinely new parameter geometry.

## 3. Repository reuse — the moving-core problem was already attacked deeply

The Stage15 cycle did not stop at the phrase “moving genus-one family”. The following exact reductions are already available and are reused here rather than rediscovered:

- `15-6ai` to `15-6ao`: smooth degree-four genus-one receiver, exact physical/product height, explicit quartic/Jacobian structure, and uniform pointwise fixed-cell counting;
- `15-6ap` to `15-6az`: fixed-core quantitative control, explicit 2-covering/non-torsion image, complete 2-descent dictionary, and a negative certificate showing that the physical product height does not imply the almost-minimal canonical-height window needed for the direct Petit route;
- `15-6ba` to `15-6bb`: the apparent divisor-many extra variable collapses back to the same degree-four quartic receiver;
- `15-6bd` to `15-6be`: the explicit global core sum is eliminated by the physical diagonal-product receiver, and each fixed physical diagonal fiber has only `B^o(1)` multiplicity;
- `15-6bf` to `15-6bg`: direct integral-point / second-moment literature cannot be substituted because the retained points have moving rational denominators; the remaining object becomes the support of admissible physical diagonal values;
- `15-6bh` to `15-6bk`: support relabeling, equal-hypotenuse and endpoint repackagings are audited as circular/equivalent and return to the same global two-channel charge;
- `15-6bl` to `15-6bs`: the actual squarefree core gives an exact codimension-two congruence lattice of index `q^2`; fixed-level toric equidistribution, Huang-level, geometric-sieve, and general large-sieve imports do not provide the required polynomial uniformity in the point-generated growing core;
- `15-6bw` to `15-6ce`: the moving-core condition is reduced further to a physical first moment for the explicit channel gcd product, with blind rediscovery confirming no new non-equivalent repo-native route in that normal form and pointwise domination explicitly tested and blocked;
- `15-6cf` onward: an exact physical-height-aware complementary-divisor switch separates small-modulus root-line error from a large complementary-cofactor average, but a polynomial overlap window remains unavailable without new quantitative input.

The reusable structural endpoint is narrower than the original R505 description. In one equivalent channel notation,

\[
G_S=\gcd(m^2+n^2,\,r^2-s^2),
\qquad
G_O=\gcd(m^2-n^2,\,r^2+s^2),
\]

and the old actual core is controlled by `G_S G_O`. The remaining whole-family problem requires a genuinely physical-height-aware average/uniformity theorem after primitive normalization; the formal fixed-modulus density alone cannot be recharged as an independent saving.

## 4. Exact remaining input species

For Stage25 **lower-bound** purposes, the useful new input would have to be one of:

1. a genuinely new explicit multi-parameter Stage19 family with bounded physical height and bounded multiplicity;
2. a uniform moving-core small-point theorem producing polynomially many core/fiber points in the exact physical measure;
3. another theorem that supplies a polynomially large admissible support set together with the primitive/canonical/exactly-two adapter.

The existing repo-native common-core manipulations do not produce such a lower family. Continuing to rename the same squareclass, diagonal-support, equal-hypotenuse, elliptic or channel-gcd receiver is explicitly blocked by the prior equivalence/double-charge audits.

A bounded reuse/rediscovery pass at Stage25 found no new non-equivalent executable mutation beyond those already recorded. This is a repository-state statement, not an impossibility theorem.

## 5. R505 classification

The proposed checkpoint60 boundary is

```text
R505_STAGE15_INTERNAL_ROUTE_SEARCH_REUSED=true
R505_FIXED_FINITE_CORE_CELL_COLLECTION_POSITIVE_POWER_UPGRADE=false
R505_MOVING_CORE_UNIFORM_SMALL_POINT_THEOREM_PROVED=false
R505_NEW_MULTI_PARAMETER_PARAMETRIC_FAMILY_FOUND=false
R505_REMAINING_GATE=WHOLE_FAMILY_PHYSICAL_HEIGHT_UNIFORMITY_OR_GENUINELY_NEW_PARAMETRIC_FAMILY
R505_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505_REOPEN_CONDITION=NEW_UNIFORM_PHYSICAL_HEIGHT_THEOREM_OR_NEW_EXPLICIT_PARAMETRIC_FAMILY
GLOBAL_STAGE25_LOWER_CHANGED=false
FINITE_DATA_USED_AS_PROOF=false
```

`EXTERNAL_THEOREM_GATE` means that the current exact common-core normal form has no remaining unexecuted repo-native mutation certified to generate a stronger lower. It does **not** assert that the moving-core arithmetic has no future solution.
