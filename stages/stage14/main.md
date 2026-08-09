# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AK_COMPLETE_SPLIT_ROOT_COSET_VOID_14_4AL_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 counts primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with exactly two integral face diagonals. No perfect-cuboid nonexistence assumption is made.

This file is the current canonical resynthesis through Stage14-4ak. Detailed historical derivations remain in the stage archive files.

## §1. Exact ledger and finite ceiling

Let `T(B)` count all-three-face objects and let `E(B)=O_pair_raw(B)` be the sum of the three raw face-pair incidences. Then

\[
\boxed{E(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, two independent exact enumerators give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

This is finite evidence only. Frozen Stage13 `R03 + Stage13-12ag` gives

\[
N_2(B)=o(B(\log B)^3)
\]

but no `B`-dependent power saving.

## §2. Exact two-face coordinates and elliptic reduction

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L_0=\operatorname{lcm}(S_1,S_2),\qquad t_i=X_i/S_i.
\]

Primitive gluing has multiplicity one and

\[
\boxed{(e,x,y)=L_0(1,t_1,t_2)},
\qquad
\boxed{d=L_0\sqrt{1+t_1^2+t_2^2}}.
\]

The space-square condition is equivalent to

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

Fixing the first face gives the elliptic curve

\[
\boxed{E_t:Y^2=X(X-1)(X+t^2).}
\]

For the actual Pythagorean base

\[
r=\frac{X_1}{H_1+S_1},\qquad t=\frac{2r}{1-r^2},
\]

the pulled-back elliptic surface has six `I4` fibers and geometric generic Mordell--Weil rank zero. Rational torsion on genuine physical fibers is nonphysical, so every physical raw pair lies on a positive-rank specialization.

## §3. Level-4 Kummer geometry and exact physical height

Stage14-4ag identifies the Pythagorean-base K3 over `Q(i)` with the classical level-4 modular surface; over `C` it is `Km(E_i x E_i)`. In symmetric half-angle variables,

\[
\boxed{Z^2=F(r,s):=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

The toric control surface is

\[
Y=\operatorname{Bl}_4(\mathbf P^1_r\times\mathbf P^1_s),
\]

with

\[
\boxed{L=2H_r+2H_s-E_{++}-E_{+-}-E_{-+}-E_{--}=-K_Y},
\qquad L^2=4.
\]

The branch has strict class `2L`. For the resolved double cover

\[
\pi:X\to Y,
\]

Stage14-4ah proves

\[
\boxed{M=\pi^*L},
\qquad
\boxed{M^2=8},
\qquad
\boxed{H_M=d}.
\]

Thus the original space-diagonal cutoff is the actual Kummer `M`-height.

## §4. Active rank-jump graph

Let `V(B)` count active oriented first-face states and `E(B)` raw pair edges. Then

\[
\boxed{E(B)=\frac12V(B)\bar d(B)=N_2(B)+3T(B).}
\]

A uniform bounded-height estimate on each elliptic fiber gives

\[
\max_F\deg_B(F)=B^{o(1)},
\]

so raw edges and active vertices have identical limsup and liminf polynomial growth exponents.

Finite data give

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

with effective exponent `0.4998643818582221` on `200k -> 2m`. This remains a finite diagnostic.

## §5. Fixed rational curves: the extremal degree target

For a physical rational curve `C/Q`, put

\[
n=\deg(C\to\mathbf P^1_r).
\]

Because `t(r)` has degree two and `t=x/e` is a quotient of `M`-sections,

\[
M\cdot C\ge2n.
\]

There are no physical sections, hence

\[
\boxed{n\ge2},\qquad \boxed{M\cdot C\ge4}.
\]

For `C\simeq\mathbf P^1`, a fixed `M`-degree `m` curve contributes bounded-height polynomial exponent `2/m`. Therefore a fixed curve can reach exponent `1/2` only if

\[
\boxed{M\cdot C=4,\qquad \deg(C\to\mathbf P^1_r)=2.}
\]

The second physical coordinate also gives

\[
\boxed{\deg(C\to\mathbf P^1_s)\le2.}
\]

This finite degree pattern is the object classified in Stage14-4ai through 4ak.

## §6. Stage14-4ai — all but one minimal mechanism eliminated

Let

\[
D=\pi(C),\qquad \delta_0=\deg(C\to D)\in\{1,2\}.
\]

Stage14-4ai proves:

1. `delta_0=2`: after boundary reduction only constant sections and opposite-corner `(1,1)` pencils remain; exact branch discriminants eliminate every physical rational inverse image.
2. `delta_0=1`, arithmetic genus zero: every `(1,2)` contact core and every `(2,2)` genus-zero ancestor is eliminated by exact resultant/discriminant identities.
3. The sole unresolved class is
   \[
   \boxed{D=L=-K_Y},\qquad D^2=4,\qquad p_a(D)=1.
   \]
   A singular member can have normalization `P1`; if the Kummer branch restricts evenly, its pullback can split into an `M`-degree-four rational bisection.

Thus at the end of 14-4ai the entire fixed-curve question had been reduced to a split singular anticanonical curve.

## §7. Symmetric Kummer coordinates

Stage14-4ai introduces

\[
\lambda=\frac{1-rs}{r-s},
\qquad
\mu=\frac{1+rs}{r+s}.
\]

Then

\[
(\lambda^2-1)(\mu^2-1)=\square
\]

encodes rational recovery of `r,s`, while the space-square condition is

\[
(\lambda^2+1)(\mu^2+1)=\square.
\]

Hence

\[
\boxed{(\lambda^4-1)(\mu^4-1)=\square.}
\]

These coordinates identify the same Gaussian-CM/Kummer structure used by the Shimada lattice computation.

## §8. Stage14-4aj — exact Shimada/deck interface

On the elliptic model

\[
E_t:y^2=x(x-1)(x+t^2),
\]

the physical inverse coordinate has the form `q=x/(s_0y)`. The raw Kummer deck involution fixing `q` is

\[
\boxed{\delta(x,y)=\left(-\frac{t^2}{x},-\frac{t^2y}{x^2}\right)}.
\]

In the group law,

\[
\boxed{\delta(P)=(0,0)-P}. 
\]

Therefore, in Shimada's fixed NS basis, the Stage14 deck matrix is a nonzero 2-torsion translation composed with elliptic inversion, not bare inversion.

For a split anticanonical survivor,

\[
\pi^{-1}(D)=C+\delta(C),
\qquad
\pi^*D=M,
\]

so

\[
\boxed{M=C+\delta(C)},
\qquad
\boxed{C^2=-2},
\qquad
\boxed{M\cdot C=4},
\qquad
C\cdot\delta(C)=6.
\]

This is the exact lattice contract consumed in 14-4ak.

## §9. Stage14-4ak — published Shimada data and physical labeling

Stage14-4ak directly consumes Shimada's published level-4 computation objects

```text
GramS0
L40vs
SixFs
fsigma
AutX0h0
AutX0f
MWtorsigmaz
Tsigma
iotasigmaz
```

using the published row-vector/right-action convention.

The `AutX0h0` orbit of `fsigma` has size five. Intrinsic Stage14 fiber/corner constraints leave four candidates for the symmetric second fiber class `f_s`. Requiring the actual coordinate swap `r<->s` to exchange the two fibrations and the corresponding boundary systems leaves two complete labelings.

Those two are equivalent: 64 elements of `AutX0f` map one full labeling to the other, including `f_s`, `M`, corner classes, and deck involution. Hence there is one physical labeling up to the relevant symmetry.

One representative is

```text
f_s = [0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
M   = [1,-1,1,-1,0,0,0,2,0,2,2,2,0,2,2,0,0,0,0,0]
deck 2-torsion label = [0,2]
```

## §10. Complete split-root reduction

For a hypothetical split root put

\[
\boxed{x=2C-M}.
\]

Since `delta(M)=M` and `delta(C)=M-C`,

\[
\boxed{\delta(x)=-x}.
\]

Also

\[
x^2=(2C-M)^2=4(-2)-4(4)+8=-16.
\]

Finally `C=(M+x)/2` is an integral NS class exactly when

\[
\boxed{x\equiv M\pmod2}.
\]

Thus the unique remaining Stage14-4ai mechanism is equivalent to finding a vector satisfying

```text
delta(x) = -x
x^2 = -16
x = M mod 2.
```

This reduction is exhaustive: any split `M.C=4` component gives such an `x`, and conversely such an `x` gives an integral root class `C` with the required numerical split identities.

## §11. Anti-invariant lattice and exact enumeration

Let `K` be a saturated integer basis of

\[
\ker(\delta+1)\cap NS(X).
\]

The computation gives

```text
anti-invariant rank = 6
```

and for the positive definite form

\[
Q=-K^T\operatorname{GramS0}K
\]

one has

```text
det Q = 256.
```

The exact vector census through norm 16 is

```text
norm 0   :    1
norm 4   :   60
norm 8   :  252
norm 12  :  544
norm 16  : 1020
```

So the anti-invariant lattice has many norm-16 vectors. The decisive Stage14 obstruction is the parity coset.

Two independent exact enumeration routes agree:

```text
PARI qfminim nonzero vectors norm <=16 = 1876
PARI norm-16 +/- representatives        = 510
independent exact LDL norm-16 vectors    = 1020
parity-compatible norm-16 vectors       = 0
parity-compatible split-root pairs      = 0
```

The PARI route uses the saturated integer kernel and Fincke--Pohst enumeration. The independent route uses exact rational LDL decomposition and recursive integer enumeration. Their cross-check passes.

An earlier implementation diagnostic accidentally extracted the PARI norm incorrectly and temporarily printed zero norm-16 vectors. The independent enumerator exposed that bug. The corrected promoted result is **not** a norm-16 void; it is the required Stage14 parity-coset void.

## §12. Fixed-curve conclusion

Every hypothetical split singular-anticanonical `M`-degree-four component would give an integral anti-invariant norm-16 vector in the coset `M mod 2`. That coset contains none.

Therefore

\[
\boxed{\text{no split singular-anticanonical }M\text{-degree-four bisection exists}.}
\]

Combined with the complete 14-4ai classification,

\[
\boxed{\text{there is no physical rational }M\text{-degree-four bisection}.}
\]

Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

This is a geometric lattice obstruction before any `Q`-descent, `Galmu`, effectivity, or physical-open filter is needed.

## §13. Meaning for the finite sqrt(B) signal

The stable finite values of `V(B)/sqrt(B)` cannot be explained by a finite collection of fixed extremal rational curves. If a `sqrt(B)` law exists, it must be collective: a moving positive-rank specialization phenomenon together with the first-small-point height gate.

This reconnects the main track directly to Stage14-s, which has already isolated:

```text
positive rank
+ moving bad-prime/Selmer structure
+ first non-torsion point in a logarithmic canonical-height window
```

No square-root asymptotic is promoted by 14-4ak itself.

## §14. Triple gate

The exact relation remains

\[
N_2(B)=E(B)-3T(B).
\]

The independent Stage14-t track must still prove sufficiently strong moving-base control, ideally

\[
T(B)=o(\sqrt B),
\]

before any future raw-pair square-root law can be transferred to exactly-two.

## §15. Locked decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
STAGE14_4AJ=COMPLETE_SHIMADA_LATTICE_INTERFACE
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID

PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8

DEGREE_TWO_IMAGE_M4_MECHANISM_ELIMINATED=true
GENUS_ZERO_SPLIT_M4_MECHANISM_ELIMINATED=true
SINGULAR_ANTICANONICAL_SPLIT_M4_MECHANISM_ELIMINATED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true

SHIMADA_PHYSICAL_LABELINGS_UP_TO_AUTX0F=1
ANTI_INVARIANT_LATTICE_RANK=6
ANTI_INVARIANT_POSITIVE_FORM_DETERMINANT=256
NORM16_VECTOR_COUNT=1020
PARITY_COMPATIBLE_NORM16_VECTOR_COUNT=0
ENUMERATOR_CROSSCHECK=PASS

RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false

TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4al collective rank-jump / first-small-point mechanism
```

## §16. Primary artifacts

```text
stages/stage14/archive/stage14-4ai-degree4-bisections.md
stages/stage14/archive/stage14-4aj-shimada-lattice-interface.md
stages/stage14/archive/stage14-4ak-shimada-split-root-void.md
stages/stage14/data/14-4/shimada_stage14_4ak_result.json
stages/stage14/scripts/14-4/shimada_stage14_identify.py
stages/stage14/scripts/14-4/shimada_stage14_refine.py
stages/stage14/scripts/14-4/shimada_stage14_equiv.py
stages/stage14/scripts/14-4/shimada_stage14_roots.py
stages/stage14/scripts/14-4/shimada_stage14_verify.py
.github/workflows/stage14-4ak-shimada-probe.yml
```
