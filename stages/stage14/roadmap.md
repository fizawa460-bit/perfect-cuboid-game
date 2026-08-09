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
- `14-4am`: exact three-gate factorization `V/A=(Sigma/A)(R/Sigma)(V/R)` and complete rank/Selmer census of every primitive oriented base through `H<=20,000`.

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

The late finite profile gives effective exponent `0.4998644` for `V` on `200k -> 2m`, and `sqrt(B)V/A` has coefficient of variation about `1.54%` on the four late cutoffs. These are finite diagnostics only.

## 14-4am — Selmer / MW-rank / first-small-point factorization

Status: [x] Complete.

Define nested base sets

```text
A(B)      = all primitive oriented Pythagorean bases with H<=B
Sigma(B)  = bases with dim Sel_2(E_F)>2
R(B)      = bases with rank E_F(Q)>0
V(B)      = bases with mu(F)<=B
```

Merged Stage14 gives

\[
\boxed{V(B)\subset R(B)\subset\Sigma(B)\subset A(B)}
\]

and therefore the exact density identity

\[
\boxed{\frac{V}{A}=\frac{\Sigma}{A}\frac{R}{\Sigma}\frac{V}{R}}.
\]

If `A(B)=B^{1+o(1)}` and an eventual `V(B)=B^{1/2+o(1)}` law holds, the Selmer, MW-rank-given-Selmer, and first-hit-given-rank thinning exponents must sum to `1/2`.

Stage14-4am replaces the old s1 matched sample by a complete PARI `ellrank(E,0)` census of every primitive oriented Pythagorean base through `H<=20,000`. The exact full-2-torsion Selmer dimension is read from the merged s1 interface; the true positive-rank count is bracketed by unconditional PARI rank bounds.

Exact finite counts:

```text
B        A       Sigma      R interval       V
2,000      638      476       371..385         7
5,000     1584     1234       916..989        25
10,000    3186     2553      1875..2057       39
20,000    6372     5209      3784..4239       54
```

At `B=20,000`:

```text
Sigma/A          = 0.8174827369742624
R/A              in [0.5938480853735091, 0.6652542372881356]
V/R              in [0.012738853503184714, 0.01427061310782241]
V/A              = 0.00847457627118644
```

The finite thinning-exponent budget is

```text
gamma(total)                   = 0.4817176373
alpha_Selmer                   = 0.02034894195
alpha_MW | Selmer              in [0.02080686276, 0.03227209060]
beta_first-hit | MW            in [0.4290966047, 0.4405618326]
```

These exponents are finite diagnostics, and the interval endpoints are correlated through the unknown exact `R(B)`. They must not be combined independently.

The robust finite conclusion is that neither nontrivial 2-Selmer nor positive MW rank is rare on the complete audited base family, whereas physical activation conditional on positive rank is only about `1.3–1.4%` at `20k`. Thus the observed finite thinning budget is overwhelmingly located in the height-sensitive `R -> V` first-small-point gate.

This does **not** prove positive-rank density, a first-small-point lower-tail law, or a square-root asymptotic.

Artifacts:

```text
stages/stage14/archive/stage14-4am-rank-smallpoint-factorization.md
stages/stage14/scripts/14-4/rank_smallpoint_factor_audit.py
stages/stage14/data/14-4/rank_smallpoint_factor_summary.json
.github/workflows/stage14-4am-rank-smallpoint.yml
```

## 14-4an — Euclid-factor reciprocity matrix coupled to height

Status: [>] Next.

Stage14-s5a expresses the moving 2-descent support in primitive opposite-parity Euclid parameters as

```text
m, n, m-n, m+n, m^2+n^2
```

plus the fixed prime `2`.

Stage14-4an must now:

1. derive the explicit local quadratic-character / Hilbert-symbol conditions between squarefree pieces of those five moving factors;
2. organize them as a reciprocity matrix suitable for a family average / large-sieve argument;
3. state precisely which part controls `A -> Sigma`, which part can reach `Sigma -> R`, and where Sha/global representability remains;
4. because 4am shows the finite dominant thinning lies in `R -> V`, couple the character analysis to the physical logarithmic height window rather than stop at a Selmer-density bound;
5. seek any unconditional family-level power saving for the joint activation set before attempting the square-root endpoint.

## 14-5 — directionwise asymptotic structure

Status: pending Stage14-4.

## Parallel arithmetic small-point track

Stage14-s is now a direct input to the main line. In particular s5a has already fixed the Euclid-parameter descent support and theorem target; 4am clarifies that a purely local/Selmer sieve is unlikely to explain the observed finite thinning unless it is coupled to global representability and the small-point height window.

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
NEXT=Stage14-4an Euclid-factor reciprocity matrix coupled to height-sensitive activation
```
