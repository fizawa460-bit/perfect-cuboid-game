# Stage14-4al — collective rank-jump / first-small-point activation measure

## Purpose

Stage14-4ak eliminated the complete fixed physical `M`-degree-four rational-bisection mechanism. Stage14-4al therefore returns the main track to the moving elliptic-specialization problem and makes the remaining count exact at the level of first-face bases.

For a primitive oriented Pythagorean first face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

define `mu(F)` to be the least physical Stage14 space-diagonal height `d` among all physical partners of `F`, and put `mu(F)=infinity` if no physical partner exists. Then the active-vertex count is exactly

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}}.
\]

This identity is the post-4ak collective counting object.

## Ambient primitive-base count

Let

\[
A(B)=\#\{F=(S,X,H)\text{ primitive oriented Pythagorean}:H\le B\}.
\]

Euclid parameters `m>n`, `gcd(m,n)=1`, `m-n` odd and `m^2+n^2<=B` give one primitive triangle and two oriented choices of distinguished leg. Standard sector lattice-point counting with coprimality and opposite parity gives

\[
\boxed{A(B)=\frac{B}{\pi}+O(\sqrt B\log B)}.
\]

Therefore, whenever either asymptotic exists,

\[
V(B)\sim c\sqrt B
\quad\Longleftrightarrow\quad
\frac{V(B)}{A(B)}\sim \frac{\pi c}{\sqrt B}.
\]

So the finite square-root signal can be reformulated as an inverse-square-root **activation density** among a linear-size Pythagorean base population. This is an equivalence/reframing, not a proof of the square-root law.

## Exact finite profile

The deterministic audit regenerates the full Stage14 graph and the complete Stage14-s4a PARI arithmetic census. At the late frozen cutoffs:

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

Across `200k -> 2m`:

```text
A effective exponent                1.0001773995
V effective exponent                0.4998643819
(V/A) effective exponent           -0.5003130177
mean sqrt(B)*V/A                    1.0990995462
CV   sqrt(B)*V/A                    0.0154166485
```

This is a striking finite match to inverse-square-root activation density, but it remains finite evidence only.

## Rank strata are not a single exceptional type

At `B=2,000,000`, the 490 active fibers have unconditional PARI rank intervals

```text
exact rank 1      254
exact rank 2      188
exact rank 3       22
exact rank 4        1
interval 0..2      15
interval 1..3      10
```

The two dominant exact-rank strata both grow substantially over `200k -> 2m`:

```text
exact rank 1 effective exponent   0.4554437100
exact rank 2 effective exponent   0.5033058376
```

Thus the finite signal is not carried only by one special exact-rank type. Stage14-s4a/b already gives the stronger arithmetic-dispersion diagnostics

```text
exact Kummer square-class triples distinct   483 / 490
coarse arithmetic signatures                 393 / 490
largest coarse signature cluster               4
```

so no bounded collection of observed arithmetic fingerprints accounts for the active population.

## The first-small-point gate is quantitatively real

At `B=2,000,000`, among active first hits,

```text
mu/H min       1.0084504563
mu/H q25       5.9293664156
mu/H median   21.0312461990
mu/H q75      98.2251521298
mu/H max   11483.1313868613
```

and

```text
log(mu)/log(H) q25      1.1766954421
log(mu)/log(H) median   1.3256609166
log(mu)/log(H) q75      1.5584093372
```

Thus active fibers need not acquire their first physical point at height comparable to the base hypotenuse. The first-small-point gate cannot be collapsed into the rank-jump/base-count gate.

The actual first-hit canonical heights remain logarithmic in the physical height, consistent with Stage14-s3:

```text
hhat/log(mu) q25      0.2497840927
hhat/log(mu) median   0.3116647403
hhat/log(mu) q75      0.3700583881
```

Again, these constants are finite diagnostics, not a uniform generator-height theorem.

## Exact post-4ak decomposition

The remaining main-track count can now be stated conceptually as

\[
V(B)=\sum_{\substack{F\text{ primitive oriented}\\H(F)\le B}}
1_{\{\operatorname{rank}E_F(\mathbf Q)>0\}}
1_{\{\mu(F)\le B\}},
\]

where the first indicator is the moving rank-jump gate and the second is the physical first-small-point gate. A physical hit implies positive rank, but Stage14-s1/s3 already show that positive rank alone does not imply a hit below the current ceiling.

The next theorem must therefore control a **joint lower tail** over the moving Pythagorean base; it cannot come from reopening fixed accumulating curves.

## Boundary

```text
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED=true
ORIENTED_PRIMITIVE_PYTHAGOREAN_BASE_ASYMPTOTIC_LINEAR=true
SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY=true
FIXED_CURVE_MECHANISM_REOPENED=false
POSITIVE_RANK_DENSITY_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4am isolate a uniform arithmetic lower-tail statement for mu(F), separating positive-rank frequency from first-small-point frequency
```

## Artifacts

```text
stages/stage14/scripts/14-4/collective_first_hit_audit.py
stages/stage14/data/14-4/collective_first_hit_summary.json
.github/workflows/stage14-4al-collective-first-hit.yml
```

CI regenerates the complete 490-row Stage14-s4a census, the full `collective_first_hit_audit.json`, and cross-checks the frozen compact summary.
