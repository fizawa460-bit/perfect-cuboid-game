# Stage14-s roadmap — Selmer / rank-jump arithmetic track

## Purpose

Stage14-s studies the arithmetic bottlenecks behind active Pythagorean first-face states. For a genuine base state `F`, merged Stage14 gives

\[
\mu(F)<\infty\iff \operatorname{rank}E_F(\mathbf Q)>0,
\]

with

\[
E_t:Y^2=X(X-1)(X+t^2),\qquad t=\frac{2r}{1-r^2}.
\]

The unresolved finite signal is

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

Stage14-s separates two gates:

1. how often the Pythagorean-base fiber has positive Mordell--Weil rank;
2. how often the first non-torsion point is small enough to satisfy `mu(F)<=B`.

No square-root law, parity conjecture, BSD statement, or Selmer=rank equality is assumed.

## 14-s1 — exact descent interface and finite Selmer/rank audit

Status: [x] Complete.

For a primitive oriented Pythagorean face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

s1 locks

\[
\boxed{E_F:Y^2=Z(Z-S^2)(Z+X^2)},
\qquad
\boxed{\Delta=16S^4X^4H^4}.
\]

The split full-2-torsion Kummer interface is

\[
d_1u_1^2-d_2u_2^2=S^2,
\qquad
d_3u_3^2-d_1u_1^2=X^2,
\]

with `d1*d2*d3` square.

A deterministic PARI/GP audit compares 96 active and 96 inactive-control fibers through `B=2m`. The key finite finding is that 54/96 inactive controls already have certified positive Mordell--Weil rank and 80/96 have nontrivial 2-Selmer beyond torsion. Thus positive rank alone does not explain physical activity at the verified scale.

```text
STAGE14_S1=COMPLETE_EXACT_DESCENT_INTERFACE_AND_FINITE_PARIRANK_AUDIT
FINITE_SELMER_ONLY_GATE_SEPARATES_ACTIVITY=false
FINITE_POSITIVE_RANK_INACTIVE_CONTROLS=54_OF_96
FINITE_SMALL_POINT_GATE_PRIORITY=HIGH
```

## 14-s2 — Pythagorean-base local Selmer support and sieve boundary

Status: [x] Complete.

The nontrivial finite local support is the moving set

\[
\Sigma_F=\{p:p\mid2SXH\}.
\]

For an odd prime `p`, write the primitive Euclid base as `[m:n] in P^1(F_p)`. The bad-prime event `p|SXH` occurs at

```text
0, infinity, +1, -1
```

and additionally at the two roots of `r^2+1=0` when `p=1 mod 4`. Therefore

\[
\boxed{\delta_p=4/(p+1)\quad(p\equiv3\pmod4)},
\]

\[
\boxed{\delta_p=6/(p+1)\quad(p\equiv1\pmod4)}.
\]

At odd `p` not dividing `SXH`, the curve has good reduction and the 2-descent local condition is unramified; no new base-dependent bad-prime coordinate is created there.

If

\[
k=\omega(2SXH),
\]

then the ambient split Kummer square-class space after the product-square constraint has `F2`-dimension at most

\[
\boxed{2(k+1)},
\]

hence at most

\[
\boxed{4^{k+1}}
\]

candidate covering classes before local solubility. Maximal order of `omega` gives

\[
4^{\omega(2SXH)+1}=H^{o(1)}.
\]

Thus local 2-cover complexity is subpolynomial **per base**, but this does not thin the base population by a fixed power.

The Stage13 fixed-auxiliary-prime product sieve does not transfer: positive-rank candidacy is a global `F2` compatibility problem among the moving bad primes dividing `2SXH`, while a fixed good prime supplies only the unramified condition.

Finite audit through `H<=200000`:

```text
primitive Pythagorean triples = 31,819
oriented face states          = 63,638
mean omega(2SXH)              = 8.7472893554
max omega(2SXH)               = 12
max log2 ambient cover cap    = 26
```

The audited prime frequencies match the exact projective laws closely; `p=3` and `p=5` have density one.

Quadratic-twist average-Selmer theorems are not imported: Stage14 has nonconstant `j`, is not a fixed-curve twist family, and genuine fibers have rational `Z/2 x Z/4` torsion. No matching average theorem for the exact Pythagorean base change has been established here.

```text
STAGE14_S2=COMPLETE_LOCAL_SUPPORT_ARCHITECTURE_AND_FIXED_PRIME_SIEVE_BOUNDARY
PYTHAGOREAN_BAD_PRIME_DENSITIES_LOCKED=true
SELMER_SQUARECLASS_SUBPOLYNOMIAL_PER_BASE_ENVELOPE=true
FIXED_AUXILIARY_PRIME_PRODUCT_SIEVE_PROVES_POWER_SAVING=false
AVERAGE_SELMER_THEOREM_IMPORTED=false
POSITIVE_RANK_DENSITY_PROVED=false
LOCAL_CONDITIONS_POWER_SAVING_PROVED=false
```

Artifacts:

```text
stages/stage14/14-s2/result.md
stages/stage14/14-s2/literature-local-selmer-audit.md
stages/stage14/scripts/14-s2/local_selmer_sieve_audit.py
stages/stage14/data/14-s2/local_selmer_sieve_audit.json
.github/workflows/stage14-s2-local-selmer.yml
```

## 14-s3 — first-small-point / regulator gate

Status: [>] Next.

The s1+s2 evidence moves the main arithmetic bottleneck here. Translate

\[
\mu(F)\le B
\]

into elliptic/descent height data.

Targets:

- derive uniform inequalities between physical `q`-height and canonical height on `E_F`;
- record first non-torsion generator heights for active and certified-positive-rank inactive controls;
- quantify the gap between positive rank and a physical point below the Stage14 cutoff;
- determine whether the finite `sqrt(B)` signal is primarily a small-generator-height phenomenon;
- prove the strongest unconditional upper/lower envelope for `V(B)` obtainable without assuming a rank-distribution conjecture.

## 14-s4 — compare with the M-degree-4 bisection mechanism

Status: [ ] Pending relevant merged `14-4ai+` and s3.

Identify the descent/Selmer classes traced by physical `M`-degree-4 bisections from the main Kummer track. Determine whether finitely many bisection classes account for the dominant first-hit population or whether equal-order rank-jump fibers remain outside them.

## 14-s5 — rank-jump counting synthesis

Status: [ ] Pending s4.

Combine arithmetic and geometry into the strongest theorem-level statement for

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

Possible outcomes remain a proved `B^{1/2+o(1)}` order, a sharper accumulating-class asymptotic, a different exponent, or a rigorous envelope explaining why the square-root signal remains unresolved.

## Proof discipline and scope

Stage14-s does not duplicate `14-t` (genus-5 triple correction) or main `14-4` (Kummer rational-curve classification). Root number is never silently converted to Mordell--Weil parity, Selmer dimension is never identified with rank without controlling Sha, and average-family results are imported only after verifying the exact family hypotheses.

```text
STAGE14_S_TRACK=ACTIVE
STAGE14_S1=COMPLETE_EXACT_DESCENT_INTERFACE_AND_FINITE_PARIRANK_AUDIT
STAGE14_S2=COMPLETE_LOCAL_SUPPORT_ARCHITECTURE_AND_FIXED_PRIME_SIEVE_BOUNDARY
PRIMARY_OBJECT=ACTIVE_PYTHAGOREAN_BASES
PRIMARY_COUNT=V(B)
S3_TARGET=FIRST_SMALL_POINT_GATE
S4_TARGET=BISECTION_SELMER_CLASS_COMPARISON
S5_TARGET=RANK_JUMP_COUNTING_SYNTHESIS
NEXT=Stage14-s3 first-small-point / regulator gate
```
