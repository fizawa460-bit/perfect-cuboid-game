# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed foundation

- `14-1`: definition/counting interface.
- `14-2`: two independent exact finite enumerators through `B=2,000,000`.
- `14-3`: finite directional reconnaissance only.
- `14-4aa`: common shared-edge parametrization.
- `14-4ab`: exact face-pair bijection, multiplicity one.
- `14-4ac`: rational slope/lcm height envelope.
- `14-4ad`: elliptic reduction `E_t:Y^2=X(X-1)(X+t^2)`.
- `14-4ae`: physical fiber height `v asymp sqrt(Bg/S1)` and generic rank zero.
- `14-4af`: actual Pythagorean base is a six-`I4` K3; torsion is nonphysical; physical pair implies positive rank; fixed-base triple genus 5.
- `14-4ag`: exact level-4/Kummer identification; active rank-jump graph; raw-edge and active-vertex polynomial exponents are equal.

Frozen Stage13 upstream remains `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3),
\]

with no imported growing-modulus power saving.

## 14-4ah — physical Kummer height and minimum accumulating bisection

Status: [x] Complete.

### Exact physical polarization

The independent e3 toric compactification is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_1+2H_2-\sum E_j=-K_Y,
\qquad L^2=4.
\]

With

\[
t_1=\frac{2r}{1-r^2},
\qquad
t_2=\frac{2s}{1-s^2},
\]

the space-square branch is

\[
F=(1+r^2)^2(1+s^2)^2-16r^2s^2.
\]

It has bidegree `(4,4)` and multiplicity two at each of the four toric corners `(+-1,+-1)`, so its strict transform has class

\[
\boxed{2L=-2K_Y}.
\]

For the resolved K3 double cover `pi:X->Y`,

\[
\boxed{M=\pi^*L=\Phi^*O_{P2}(1)},
\qquad
\boxed{M^2=8}.
\]

On the Stage14 arithmetic open set the corresponding height is exactly

\[
\boxed{H_M=d}.
\]

Thus Stage14 now knows the divisor class of the **actual** physical cutoff.

### Big and nef boundary

`M` is big and nef but not ample. The four toric `L`-null boundary curves lift geometrically to eight `M`-null `(-2)`-curves, all outside the primitive positive Stage14 open set.

Because McKinnon's product-Kummer counting theorem uses an ample height, its asymptotic is not imported directly for Stage14 `M`.

### Minimum physical rational-curve degree

Let `C` be a physical rational curve and

\[
n=\deg(C\to P^1_r).
\]

The slope map `t(r)=2r/(1-r^2)` has degree two and `t=x/e` is a quotient of two `M`-sections, hence

\[
\boxed{M\cdot C\ge2n.}
\]

A physical `n=1` curve would be a section. Generic Mordell--Weil rank is zero and all torsion sections are nonphysical, so

\[
\boxed{n\ge2},
\qquad
\boxed{M\cdot C\ge4}.
\]

A rational curve of `M`-degree `m` has bounded-height polynomial exponent `2/m`. Therefore no fixed physical rational curve can exceed exponent `1/2`, and the extremal square-root target is exactly

\[
\boxed{\text{a Q-rational M-degree-4 bisection}.}
\]

Existence/classification/dominance of such bisections is not yet proved.

### Interior finite diagnostic

The active-vertex `sqrt(B)` signal survives fixed cusp deletion:

```text
B          all V    0.1<=r<=0.9    0.2<=r<=0.8    0.25<=r<=0.75
200k         155          134             105                92
500k         254          227             174               147
1m           347          307             238               197
2m           490          426             338               283
```

The `200k -> 2m` effective exponents are

```text
0.49986438, 0.50230480, 0.50772740, 0.48799861.
```

This is finite evidence only.

### Relative triple cover

The third-face-square numerator

\[
G=r^2(1-s^2)^2+s^2(1-r^2)^2
\]

also has strict class `2L` on `Y`. Hence the relative degree-two cover of the raw K3 has branch class

\[
\boxed{2M}.
\]

Its rational image is type-II thin, but no thin-set zero-density theorem for the raw K3 under the big-and-nef `M`-height is currently imported or proved. Therefore

\[
T(B)=o(\sqrt B)
\]

remains open.

Decision:

```text
STAGE14_4AH=COMPLETE
PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
PHYSICAL_POLARIZATION_BIG_NEF_NOT_AMPLE=true
PHYSICAL_RATIONAL_CURVE_M_DEGREE_LOWER_BOUND=4
SQRTB_MINIMAL_RATIONAL_CURVE_TARGET=M-degree-4 rational bisection
MCKINNON_DIRECT_ASYMPTOTIC_IMPORTED=false
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
TRIPLE_TYPE_II_THIN=true
T_O_SQRT_B_PROVED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

Artifacts:

```text
stages/stage14/archive/stage14-4ah-kummer-height.md
stages/stage14/scripts/14-4/kummer_height_audit.py
stages/stage14/data/14-4/kummer_height_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## 14-4ai — classify the extremal bisections

Status: [>] Next.

Purpose:

- classify `Q`-rational bisections `C` with `M.C=4` on the level-4/Kummer model;
- determine which such curves meet the primitive positive Stage14 open set;
- derive the exact physical height on their rational parameters and count first-hit vertices contributed by them;
- test whether the degree-four bisections account for `V(B)=B^(1/2+o(1))` or only a subpopulation;
- restrict the relative triple cover to each candidate bisection and determine whether triple points are finite / lower-order on the same curves;
- only after this promote, reject, or refine the square-root growth candidate.

## 14-5 — directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true Stage14 growth exponent, leading constant, limiting directional vector, perfect-cuboid existence/nonexistence theorem, or `T=o(sqrt(B))` theorem is established yet.

```text
NEXT=Stage14-4ai classify Q-rational M-degree-4 bisections and count their first-hit height
```
