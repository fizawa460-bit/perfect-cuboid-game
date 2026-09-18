# Stage32 MB104 — SOFT-PARK second-depth screening Round 5 / portfolio freeze — 2026-09-18

Status: **ROUND 5 COMPLETE / SECOND-DEPTH PORTFOLIO FROZEN / NO NEW THIRD-DEPTH ADVANCE / NO MATHEMATICAL CREDIT**

## Scope

This is the fifth and final user-directed second-depth pass over the 26 broader SOFT-PARK directions.

Round 5 screens

```
W3   Aut(S)-norm / representation-theoretic invariant section
W7   cyclic/abelian-cover BMY amplification
W9   finite-characteristic specialization
W12  receiver-preserving explicit degeneration
W25  Lefschetz / monodromy / slope refinement
```

The active ray remains

```
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
D_l^2=336l^2,
K.D_l=112l,
Delta=168l^2+56l.
```

A direction advances only if it has a source-complete forward adapter and an explicit path to all-`l` or large-`l` exclusion.

## W3 — invariant-section vanishing is impossible on an infinite large-l subsequence

The wide scan found that the `Aut(S)`-norm of a hypothetical active-ray section has class

```
896l A,
A=6H-sum_(all 48 nodes)E,
A^2=480,
K.A=96.
```

Riemann--Roch gives

```
chi(O(A))
 =8+(A^2-K.A)/2
 =200.
```

Also

```
H.(K-A)=16-96=-80<0,
```

so `K-A` is not effective and `h2(A)=0`. Hence

```
h0(A)>=200>0.
```

Choose any nonzero effective divisor `D in |A|`. The exact automorphism group has order

```
|Aut(S)|=1536.
```

The orbit-sum divisor

```
N_G(D)=sum_(g in Aut(S)) g(D)
```

is `Aut(S)`-invariant and has class

```
1536 A.
```

Now

```
896*(12k) =1536*(7k).
```

Therefore, for every `k>=1`, taking `7k` copies of `N_G(D)` gives an invariant effective divisor of **exactly** the W3 norm class

```
896*(12k) A.
```

So invariant-section nonexistence cannot possibly exclude all sufficiently large `l`: invariant sections exist for the unbounded subsequence

```
l=12,24,36,...
```

This is stronger than the original positivity heuristic.

A more delicate representation-theoretic condition on the *specific norm section* would be a different theorem, but W3 as an invariant-section vanishing route is exhausted.

**Disposition: PARK_EXACT_INFINITE_SUBSEQUENCE_COUNTERWITNESS.**

## W7 — cyclic/abelian-cover BMY is absorbed by H8 log/orbifold BMY

The shallow cyclic-cover computation gave

```
3c2(Y)-K_Y^2
 =224n
  +112(n-1)l
  +336 (n-1)(2n+1)/n * l^2 >0
```

for every smooth cyclic cover order `n>=2`.

The stronger retained H8 gate already tested the corresponding log/orbifold architecture with arbitrary boundary coefficients

```
0<=a,b_i<=1,
```

including the cyclic-cover coefficients `a=1-1/n`.  For a retained-data-compatible ordinary-node/transverse witness, H8 proved the uniform slack

```
3 e_orb(S,B) - (K+B)^2 >=147
```

for every `l>=1` and every coefficient choice in the full cube.

Thus optimizing the cover degree `n`, or merely passing from smooth cover BMY to the standard orbifold correction, cannot close MB104.

A W7 revival would need a **new analytic theorem** forcing the off-exceptional singularities into a class whose local orbifold corrections are substantially worse than the retained nodal witness.  That input is no longer a cover-order phenomenon; it belongs to the singularity/contact directions W23/W24.

**Disposition: PARK_ABSORBED_BY_H8.**

## W9 — finite-characteristic specialization

The shallow objection was that normalization-genus-one / integral / multibranch receiver data are not preserved under naive reduction.

There is a genuine compactification repair in principle.  Modern genus-one stable-map theory provides proper compactifications of the main component of the genus-one stable-map space.  In particular Ranganathan--Santos-Parker--Wise construct a smooth proper moduli space dominating the main component of Kontsevich's genus-one stable maps to projective space.

However, the proper boundary is strictly larger than the original receiver.  Genus-one stable-map spaces contain ghost boundary phenomena, including contracted genus-one components attached to positive-degree genus-zero pieces.  Coates--Manolache explicitly separate the main and ghost components in genus one.

Consequently a characteristic-`p` exclusion would have to prove nonexistence not merely of an integral genus-one carrier with the original branch packet, but of every special-fiber point in the closure of the relevant main-component locus, including admissible boundary/ghost degenerations.

No prime, no finite-field compactified receiver, and no source-complete special-fiber exclusion theorem of that strength are presently available in the MB104 archive.

Compared with W12, finite characteristic also adds inseparability/Frobenius and Picard-jump behavior without providing a designed simpler special fiber.

**Disposition: PARK_DOMINATED_BY_W12.**

External references:
- D. Ranganathan, K. Santos-Parker, J. Wise, *Moduli of stable maps in genus one and logarithmic geometry I*, arXiv:1708.02359.
- T. Coates, C. Manolache, *A splitting of the virtual class for genus one stable maps*, arXiv:1809.04162.

## W12 — explicit degeneration: receiver compactification exists, but no useful special fiber yet

W12 improves relative to its shallow status.

The same proper genus-one main-component compactification gives a credible **forward receiver adapter** for a projective degeneration: a smooth-domain genus-one map on the generic fiber has a limit in a proper compactification after base change.

This removes the shallow statement that "there is no compactified receiver" as the fundamental blocker.

The real blocker is now the special fiber.

The compactified boundary can contain reducible maps and ghost elliptic components.  Therefore it is not enough to produce a degeneration where the special fiber has no integral genus-one curve of the original shape.  One must exclude the entire limiting main-component locus in the specialized class.

The logarithmic genus-one theory is relevant here: Ranganathan--Santos-Parker--Wise provide proper logarithmic models and a genus-one tropical realizability framework for toric targets.  This suggests a concrete future architecture:

```
construct a source-locked toroidal/semistable degeneration of the cuboid surface
 -> transport D_l and the fourteen contact packets
 -> describe the principal/main-component tropical genus-one maps
 -> prove no realizable tropical type for all l (or all l>L).
```

But the repository currently has **no** explicit receiver-preserving toroidal degeneration of the cuboid surface and no tropical image of the exact MB104 packet.  Building that is substantial new work.

**Disposition: RESERVE.**

This is not promoted to third-depth yet because the first load-bearing object—the explicit degeneration with tracked packet/class—does not exist.

External reference:
- D. Ranganathan, K. Santos-Parker, J. Wise, *Moduli of stable maps in genus one and logarithmic geometry I/II*, arXiv:1708.02359 and arXiv:1709.00490.

## W25 — slope/monodromy refinement of a pencil

Take a generic pencil in `|D_l|`.  Its base locus has

```
N=D_l^2=336l^2
```

points.  Blow them up to obtain

```
f:X' -> P1.
```

A general smooth fiber has genus

```
g
 =1+(D_l^2+K.D_l)/2
 =1+168l^2+56l.
```

The relative invariants are exactly

```
K_f^2
 =16+3D_l^2+4K.D_l
 =1008l^2+448l+16,

chi_f
 =chi(O_S)+g-1
 =168l^2+56l+8.
```

Hence the slope tends to

```
K_f^2/chi_f ->6.
```

The standard Cornalba--Harris--Xiao lower slope bound is asymptotically `4`, so the pencil lies comfortably on the allowed side.  Exact substitution gives

```
K_f^2 * g - 4(g-1)chi_f
 =16(3528l^4+3528l^3+679l^2-28l+1)>0
```

for every `l>=1`.

The total semistable Euler/singularity budget is

```
e_f
 =12chi_f-K_f^2
 =1008l^2+224l+80.
```

The hypothetical genus-one normalization carrier would have defect

```
Delta=g-1=168l^2+56l,
```

so one such singular fiber consumes only about one sixth of the total pencil budget.  Exact difference:

```
e_f-Delta
 =840l^2+168l+80>0.
```

Thus neither the slope inequality nor the total semistable singularity budget approaches a contradiction.

A monodromy refinement would need packet-specific restrictions on the vanishing cycles of the special carrier; no such source-complete relation is presently available.

**Disposition: PARK_SLOPE_COMPATIBLE.**

External reference:
- L. Stoppino, *Slope inequalities for fibred surfaces via GIT*, arXiv:math/0411639.

## Round-5 selection

```
ADVANCE_FOR_THIRD_DEPTH:
  none

RESERVE:
  W12  proper receiver compactification exists in principle, but explicit
       packet-preserving degeneration is missing

PARK:
  W3   invariant-section vanishing has exact unbounded counterwitness l=12k
  W7   absorbed by stronger H8 log/orbifold BMY compatibility witness
  W9   same compactification burden as W12 with less controlled special fiber
  W25  exact fibration slope and singularity budgets are compatible
```

## Complete second-depth portfolio freeze

All 26 broader SOFT-PARK directions have now received one second-depth pass.

```
THIRD-DEPTH CANDIDATES
  W4   exact rank-20 K3 (-2)-root wall
  W16  canonical non-split O(l)-size Cayley--Bacharach subcluster
  W20  finite Pic^0(E)[2] Abel/conductor bridge

HIGH RESERVE
  W5   higher symmetric differentials with 2025 exact A_n local-Euler machinery

RESERVE
  W12  receiver-preserving log/toroidal degeneration
  W13  rank-64 stable-base/effective-cone route
  W17  support-stabilizer fixed-locus singularity localization
  W23  exact special-grid tangency evaluator / quadratic collision target

PARK / ABSORBED
  W1,W3,W6,W7,W9,W11,W18,W19,
  W21,W22,W24,W25,W26,W27,W28,W29,W30,W31
```

The five broader HARD-DROP directions remain

```
W2,W8,W10,W14,W15.
```

No W32+ label is needed at this stage.

## Third-depth execution order

The second-depth portfolio now supports a concrete next phase.

### Pass A — W4 exact K3 root wall

This is the most bounded next experiment.  The external Stoll verification already constructs the rank-20 quotient Picard lattice, intersection pairing, known curves and automorphisms.  Compute the seven primitive pushdown rays and test them against a source-complete effective `(-2)`-root wall.

Possible outcomes are decisive:

```
negative root found
 -> corresponding quotient gives all-l fixed-component contradiction;

all seven primitive rays nef against the complete effective root wall
 -> W4 closes negatively and is removed.
```

### Pass B — W20 finite torsion bridge

Compute the explicit class

```
delta_fac=O_E(D_z^+-D_w^+) in E[2]
```

and relate it to `eta` / ambient conductor character.  This is finite but initially closes only the `e=2` branch.

### Pass C — W16 proper CB construction

Search for an intrinsic proper lci Cayley--Bacharach scheme of length `O(l)` that is forced by every carrier and yields a non-split Serre extension.  If length `<=112l`, the numerical package would exclude every `l>=2`, leaving only `l=1`.

This order is research routing only, not mathematical ranking or credit.

## Firewalls

- MB104 is not complete.
- No finite degree window is proved.
- No receiver/effectivity/theorem/endpoint credit.
- No Perfect Cuboid existence or nonexistence claim.
- No merge authorization.
