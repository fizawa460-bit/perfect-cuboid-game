# Stage15-6aq - global norm-core aggregation audit and causal boundary

Base: Stage15-6ap in the current cycle. Stage15-6ap closed the coordinate-core dichotomy at fixed norm core `k` and proved, on every dyadic block,

\[
N_k(Z,W)
\ll_\varepsilon
B^\varepsilon k^{1/8}(ZW)^{5/8}
\le
B^{5/8+\varepsilon}k^{-1/2},
\]

using the exact physical height `kZW<=2B`.

Stage15-6aq audits the remaining sum over the common Gaussian norm core `k`. It does not hide this sum in `B^o(1)` and does not recharge the norm-core congruences already consumed in 6aa--6ac.

## 1. The kappa obstruction is closed, the k obstruction is not

The current mechanism has two distinct squarefree cores:

```text
k      = common Gaussian norm core
kappa  = common coordinate-product core
```

Stage15-6al proved `(k,kappa)=1`. The coordinate core therefore supplied genuinely new information, and 6am--6ap used it legally.

For fixed `k`, the full coordinate-core population is now covered by:

```text
large kappa:
  root-line square-root collapse                          [6am]

small kappa:
  j=1728 degree-4 quartic
  -> uniform Heath-Brown count per kappa fiber           [6an/6ao]
  -> diagonal kappa coupling without #kappa factor       [6ap]
```

Thus there is no longer an uncounted `kappa=1` or small-coordinate-core branch at fixed `k`.

```text
STAGE15_6AQ_COORDINATE_CORE_OBSTRUCTION_CLOSED_AT_FIXED_k=true
```

## 2. Why the norm-core sum is not B^o(1)

The common norm core `k` is squarefree, supported on `2` and primes `1 mod 4`, and polynomially bounded by the physical product-height identity.

For one fixed `k`, the Gaussian orientations cost only `r_2(k)^2=B^o(1)`. This does **not** imply that the number of possible values of `k` is `B^o(1)`.

Indeed the set of squarefree integers supported on split primes is still polynomially large as a function of its upper cutoff. Therefore the formal sum

\[
B^{5/8+\varepsilon}\sum_{k\le K} k^{-1/2}
\]

has polynomial growth in `K`; it cannot be absorbed into `B^o(1)`.

The uniqueness of `k` per physical point prevents duplicate representation, but uniqueness alone supplies no upper bound for the total diagonal mass over different `k`.

```text
STAGE15_6AQ_NORM_CORE_VALUE_COUNT_SUBPOLYNOMIAL=false
STAGE15_6AQ_NAIVE_SUM_k_MINUS_HALF_LEGAL_THINNING_PROOF=false
```

## 3. 6ac high-core spacing cannot simply be fired again

Stage15-6ac used the odd norm core

\[
q=k/2^\eta
\]

as a root-line modulus **inside a fixed physical outer-pair fiber** and split by

\[
q^2\ge R_0S_0
\quad\text{versus}\quad
q^2<R_0S_0.
\]

The present 6ad--6ap route is precisely the descendant of the second, low-core branch. Its Gaussian-square and quartic equations were obtained only after the original norm-core charge and orientation data were consumed.

Therefore it is invalid to say:

```text
k is now visible again
-> charge k as a fresh modulus
-> apply AR-009 a second time
```

That would count the same norm-core information twice. AR-028 forbids it.

Moreover the 6ac threshold is tied to the original conditioned physical inner rectangle. It is not a theorem that an unrestricted global Gaussian block with large numerical `k` automatically lies in the old high-core branch.

```text
STAGE15_6AQ_AR009_NORM_CORE_RECHARGE_ALLOWED=false
STAGE15_6AQ_6AC_HIGH_CORE_CROSS_PROMOTION_TO_GLOBAL_k_SUM=false
```

## 4. Global Gaussian reformulation of the remaining correlation

Write the two primitive Gaussian square values

\[
\alpha_0=x+iy=K_\alpha z^2,
\qquad
\beta_0=p+iq=K_\beta w^2.
\]

Then

\[
\operatorname{sf}(x^2+y^2)
=
\operatorname{sf}(p^2+q^2)
=k,
\]

and

\[
\operatorname{sf}(xy)
=
\operatorname{sf}(pq)
=\kappa.
\]

Stage15-6aj also gives

\[
\boxed{
R=\frac{2}{\gamma}
\sqrt{(x^2+y^2)(p^2+q^2)},
\qquad \gamma\in\{2,4\}.
}
\]

So after all exact reductions, the unresolved causal aggregation is a **same-pair double-squareclass correlation**:

```text
primitive coordinate pair (x,y)
primitive coordinate pair (p,q)

same norm squareclass          k
same coordinate-product class  kappa
product norm height            <= B
physical masks                 retained as postfilters
```

The `kappa` direction now has a uniform degree-four count. What is missing is a theorem that aggregates the simultaneously moving norm squareclass without paying a polynomial number of `k` values.

## 5. Stage14 Gaussian coordinate-product research is guidance, not a reusable saving

Stage14-s7-48 and its auxiliary audit sH48 studied a related one-Gaussian-state correlation between a sum-of-two-squares norm and a rotated coordinate product. The frozen sH48 verdict was

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
FIXED_POWER_SAVING_PROVED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```

for its exact balanced Stage14 packet measure.

That result is not a theorem that the present Stage15 correlation has no saving. But it is an Arsenal-style warning that one-sided norm or product marginals do not create a fixed-power gain by themselves and that a genuine same-point cross-correlation theorem is required.

The Stage14 measure, balanced cells, reciprocal masks and target exponent differ from the Stage15 product-height measure, so no Stage14 exponent is transferred.

```text
STAGE15_6AQ_STAGE14_SH48_DIRECT_REUSE=false
STAGE15_6AQ_STAGE14_SH48_STRUCTURAL_GUIDANCE=true
```

## 6. A j=1728 twist-height route exists as a future adapter, but is not proved here

Stage15-6an proved that every small-`kappa` quartic is geometrically `j=1728`. This makes twist-specific arithmetic a legitimate future route rather than a generic elliptic-family search.

Nara's work on quadratic twists gives lower bounds of canonical height growing like a positive multiple of `log|D|` for non-2-torsion points on a fixed quadratic-twist family. Such a theorem could become relevant only after Stage15 supplies all of the following exact adapters:

1. the rational twist parameter `D` of `C_{K,kappa}` in terms of `k,kappa` and the 2-primary data;
2. an explicit map from the Stage15 quartic point to the chosen Weierstrass twist;
3. a bound comparing the Stage15 projective/product height with canonical height;
4. a pointwise Mordell--Weil rank or lattice-point bound strong enough to count **every** twist, not merely average twists;
5. a final aggregation preserving the original common-`k` coupling.

None of these five items is proved in 6aq. Therefore Nara is recorded only as a targeted future theorem candidate, not as a current saving.

```text
STAGE15_6AQ_J1728_TWIST_HEIGHT_ROUTE_IDENTIFIED=true
STAGE15_6AQ_J1728_TWIST_HEIGHT_ADAPTER_PROVED=false
STAGE15_6AQ_TWIST_RANK_POINTWISE_BOUND_PROVED=false
```

## 7. Exact theorem gate after 6aq

The remaining theorem/adapter species can now be stated narrowly as

```text
Stage15PrimitiveGaussianNormAndCoordinateProduct
CommonSquareclassDiagonalCorrelationUnderProductHeight
```

or, through the isotrivial model,

```text
UniformJ1728TwistPointCountWithCommonNormCoreAggregation
```

A successful theorem must beat the polynomial cost of summing norm cores and preserve an every-fiber / whole-physical-family upper bound. Average Selmer, average rank, almost-all twists, or a theorem on one fixed `k` does not close this gate without an exceptional-set contribution strong enough for the Stage15 measure.

## 8. Causal exponent status

The cycle has obtained a genuine new fixed-`k` estimate, but it has **not** independently recovered the Stage15-5 whole-family half-power upper thinning.

In particular:

```text
k=1 small-kappa branch from 6ap:
  certified fixed-k exponent = 5/8 + epsilon

Stage15-5 whole numerator theorem:
  exponent = 1/2 + epsilon
```

The former is a causal-mechanism bound on the normalized receiver; the latter remains the stronger whole-family theorem supplied by the Stage14 direct numerator bridge. They must not be conflated.

```text
STAGE15_6AQ_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6AQ_STAGE15_5_REPROVED=false
```

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6aq
STAGE15_6AQ_STARTING_GATE=GLOBAL_NORM_CORE_AGGREGATION
STAGE15_6AQ_COORDINATE_CORE_OBSTRUCTION_CLOSED_AT_FIXED_k=true
STAGE15_6AQ_NORM_CORE_VALUE_COUNT_SUBPOLYNOMIAL=false
STAGE15_6AQ_NAIVE_SUM_k_MINUS_HALF_LEGAL_THINNING_PROOF=false
STAGE15_6AQ_AR009_NORM_CORE_RECHARGE_ALLOWED=false
STAGE15_6AQ_6AC_HIGH_CORE_CROSS_PROMOTION_TO_GLOBAL_k_SUM=false
STAGE15_6AQ_STAGE14_SH48_DIRECT_REUSE=false
STAGE15_6AQ_STAGE14_SH48_STRUCTURAL_GUIDANCE=true
STAGE15_6AQ_J1728_TWIST_HEIGHT_ROUTE_IDENTIFIED=true
STAGE15_6AQ_J1728_TWIST_HEIGHT_ADAPTER_PROVED=false
STAGE15_6AQ_NORM_CORE_GLOBAL_SUM_PROVED=false
STAGE15_6AQ_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6AQ_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AQ_EXIT=J1728_TWIST_HEIGHT_OR_NORM_CORE_CORRELATION_THEOREM_GATE
```

This is the natural cycle stop: the remaining work is no longer unused exact algebra or an unclassified genus-one family. It is a precise new arithmetic theorem/adapter gate.