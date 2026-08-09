# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed foundation

- `14-1`: definition/counting interface.
- `14-2`: two independent exact finite enumerators through `B=2,000,000`.
- `14-3`: finite directional reconnaissance.
- `14-4aa`: common shared-edge parametrization.
- `14-4ab`: exact face-pair bijection, multiplicity one.
- `14-4ac`: rational slope/lcm height envelope.
- `14-4ad`: elliptic reduction `E_t:Y^2=X(X-1)(X+t^2)`.
- `14-4ae`: physical fiber height and generic rank zero.
- `14-4af`: six-`I4` Pythagorean-base K3; torsion nonphysical; fixed-base triple genus 5.
- `14-4ag`: level-4/Kummer identification; active rank-jump graph; raw-edge and active-vertex polynomial exponents equal.
- `14-4ah`: exact physical Kummer polarization `M=pi^*(-K_Y)`, `M^2=8`, `H_M=d`; fixed physical rational curves have `M.C>=4`.
- `14-4ai`: all minimal `M`-degree-4 mechanisms reduced to one split singular-anticanonical target.
- `14-4aj`: exact Shimada lattice/deck/polarization interface.
- `14-4ak`: published Shimada data ingested; the final split-root parity coset is empty by two independent exact enumerators; all fixed `M.C=4` rational-bisection mechanisms are closed.
- `14-4al`: exact collective first-hit activation measure `V(B)=#{F:mu(F)<=B}`; ambient primitive oriented Pythagorean base count is linear; the finite sqrt signal is reformulated as inverse-square-root activation density.

Frozen Stage13 upstream remains `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3),
\]

with no imported growing-modulus power saving.

## 14-4ai through 14-4ak — close the fixed-curve path

Status: [x] Complete.

A fixed physical rational curve capable of exponent `1/2` must satisfy

\[
M\cdot C=4,\qquad \deg(C\to\mathbf P^1_r)=2,
\qquad \deg(C\to\mathbf P^1_s)\le2.
\]

Stage14-4ai eliminates every connected degree-two image mechanism and every arithmetic-genus-zero split/contact mechanism. The sole survivor was a singular rational member of the anticanonical class `D=L=-K_Y` whose K3 pullback could split.

Stage14-4aj identifies the raw Kummer deck involution as

\[
\delta(P)=(0,0)-P
\]

on `E_t:y^2=x(x-1)(x+t^2)`. For a split component,

\[
M=C+\delta(C),\qquad C^2=-2,\qquad M\cdot C=4.
\]

Putting `x=2C-M` reduces the last case to

\[
\delta(x)=-x,\qquad x^2=-16,\qquad x\equiv M\pmod2.
\]

Stage14-4ak consumes Shimada's official level-4 computation data. Up to the relevant automorphism group there is one physical labeling. Its deck anti-invariant NS lattice has rank `6`, positive-form determinant `256`, and `1020` norm-16 vectors; nevertheless none lies in the required parity coset. PARI/Fincke--Pohst and an independent exact rational-LDL enumerator agree.

Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

## 14-4al — collective rank-jump / first-small-point activation

Status: [x] Complete.

For each primitive oriented Pythagorean first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

define `mu(F)` as the least physical Stage14 space-diagonal height among all partners of `F`, and `mu(F)=infinity` if no physical partner exists. Then exactly

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}}.
\]

Let `A(B)` be the number of primitive oriented Pythagorean bases with `H<=B`. Euclid-parameter lattice counting gives

\[
\boxed{A(B)=\frac{B}{\pi}+O(\sqrt B\log B)}.
\]

Thus, whenever either asymptotic exists,

\[
\boxed{V(B)\sim c\sqrt B
\iff
V(B)/A(B)\sim \pi c/\sqrt B.}
\]

This turns the post-4ak question into a moving-base activation/lower-tail problem rather than another accumulating-curve search.

The exact finite audit gives

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

and on `200k -> 2m`

```text
A effective exponent                1.0001773995
V effective exponent                0.4998643819
(V/A) effective exponent           -0.5003130177
mean sqrt(B)*V/A                    1.0990995462
CV   sqrt(B)*V/A                    0.0154166485
```

These numbers are finite diagnostics only. No square-root asymptotic is promoted.

The active population is not a single rank or descent class. At `B=2m`, exact PARI ranks include `254` rank-1 and `188` rank-2 fibers; their `200k -> 2m` effective exponents are about `0.4554` and `0.5033`. Stage14-s4a/b independently finds `483/490` distinct exact Kummer square-class triples and `393` coarse arithmetic signatures, with largest coarse cluster only `4`.

The first-small-point gate also remains substantial: at `B=2m`, `mu(F)/H(F)` has median `21.03`, 75th percentile `98.23`, and maximum about `1.15e4`. Positive-rank specialization therefore cannot simply be identified with physical activation near the base height.

Locked boundary:

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
```

Artifacts:

```text
stages/stage14/archive/stage14-4al-collective-first-hit.md
stages/stage14/scripts/14-4/collective_first_hit_audit.py
stages/stage14/data/14-4/collective_first_hit_summary.json
.github/workflows/stage14-4al-collective-first-hit.yml
```

## 14-4am — uniform arithmetic lower tail for first activation

Status: [>] Next.

The remaining main-track count has the conceptual form

\[
V(B)=\sum_{\substack{F\text{ primitive oriented}\\H(F)\le B}}
1_{\{\operatorname{rank}E_F(\mathbf Q)>0\}}
1_{\{\mu(F)\le B\}}.
\]

Stage14-4am must separate and control the two moving gates:

1. frequency of positive-rank specialization on the primitive Pythagorean base;
2. conditional lower tail of the first physical non-torsion point `mu(F)` on positive-rank fibers;
3. dependence on the moving bad-prime / 2-descent support already exposed by Stage14-s2/s4;
4. a uniform upper or lower exponent for the joint activation probability, without assuming rank equals Selmer rank or first hit equals a Mordell--Weil generator;
5. only after that, decide whether the finite inverse-square-root activation density can be promoted, rejected, or narrowed.

## 14-5 — directionwise asymptotic structure

Status: pending Stage14-4.

## Parallel arithmetic small-point track

Stage14-s is now a direct input to the main line: s1/s2 isolate rank/Selmer and moving bad-prime support, s3 isolates the canonical-height small-point gate, and s4a/b show that active arithmetic fingerprints are highly dispersed.

## Parallel triple gate

The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

A future raw-pair law cannot be transferred to exactly-two until the triple track proves sufficiently strong control, ideally

\[
T(B)=o(\sqrt B).
\]

## Scope boundary

No true Stage14 growth exponent, leading constant, limiting directional vector, perfect-cuboid existence/nonexistence theorem, or `T=o(sqrt(B))` theorem is established yet.

```text
NEXT=Stage14-4am uniform arithmetic lower-tail statement for mu(F)
```
