# Stage14-t11 — compatible paired small-point activation

## Purpose

Stage14-t10 corrected the direction of the reflected local sieve: the sparse residues where the easy local square argument fails are an exceptional error regime, not the main source of thinning. The triple correction must therefore be attacked globally.

This stage defines the exact population that must be counted after raw activation.

No estimate `T(B)=o(sqrt(B))` is claimed here.

## Fixed-base triple fiber as a shared-q fiber product

For a physical Pythagorean base `s=t^2` put

\[
A=\frac{1-s}{1+s},\qquad C=\frac2s-1.
\]

The two relevant quartics are

\[
W^2=q^4+2Aq^2+1,
\]

\[
R^2=q^4+2Cq^2+1.
\]

The raw quotient `E_R` and reflected/third-face quotient `E_W` are not independent point conditions: a triple point requires the **same rational q** to satisfy both quartics. Equivalently it is a rational point on the genus-5 Humbert--Edge fiber product

\[
\mathcal C_s:\quad
W^2=q^4+2Aq^2+1,\qquad
R^2=q^4+2Cq^2+1.
\]

Thus simultaneous positive rank on the two elliptic quotients is only a necessary relaxation. It is not the t-side counting object.

## First-hit functions

For a primitive oriented physical base `F`, define

```text
mu_R(F)    = least physical cuboid height of a raw-pair point on F,
mu_pair(F) = least physical cuboid height of a compatible shared-q point on C_F,
             with infinity if no such point exists.
```

Then tautologically

\[
\mu_R(F)\le \mu_{pair}(F),
\]

because every compatible pair projects to a raw point.

Define the activation populations

\[
V_R(B)=\#\{F:\mu_R(F)\le B\},
\]

\[
V_{pair}(B)=\#\{F:\mu_{pair}(F)\le B\}.
\]

Hence

\[
\boxed{V_{pair}(B)\le V_R(B)}.
\]

The t-side missing quantity is the conditional paired-lift density

\[
\theta_{pair}(B)=\frac{V_{pair}(B)}{V_R(B)}
\]

when `V_R(B)>0`.

A proof that

\[
\theta_{pair}(B)\to0
\]

would show that compatible triple bases are sparse **relative to raw active bases**. To derive the absolute target `T(B)=o(sqrt(B))`, this must be combined with a sufficiently sharp raw activation/multiplicity bound; relative sparsity alone is not automatically enough.

## Object count versus base count

`V_pair(B)` counts activated bases, whereas `T(B)` counts primitive triple objects. A single base may in principle support multiple compatible physical shared-q points below height `B`.

Therefore the exact object-level quantity is

\[
P(B)=\#\{(F,q): q\text{ is a compatible physical shared-q point with height }\le B\}.
\]

Every primitive triple object gives such a pair, up to the fixed finite orientation/symmetry bookkeeping already present in Stage14. Thus the theorem-scale route must control either `P(B)` directly or combine

1. a bound for `V_pair(B)`, and
2. a uniform/average multiplicity bound for compatible points per activated base.

The single-fiber bounded-height results discussed in Stage14-s5 may help only with item 2; they do not supply the family thinning in item 1.

## Relation to the main/s tracks

Stage14-4am factors raw activation into nested gates

```text
A(B) -> Sigma(B) -> R(B) -> V_R(B)
```

for eligible bases, Selmer activation, positive Mordell--Weil rank, and first physical raw small point.

The triple track adds a genuinely new final gate

```text
V_R(B) -> V_pair(B),
```

or at object level

```text
raw physical small point (F,q)
    -> reflected quartic square at the same q
    -> compatible Humbert--Edge point.
```

This is stronger than requiring the reflected elliptic quotient merely to have positive rank or some unrelated small rational point.

Accordingly, t11 separates the remaining thinning into

\[
\frac{V_{pair}}{A}
=
\frac{\Sigma}{A}
\frac{R}{\Sigma}
\frac{V_R}{R}
\frac{V_{pair}}{V_R}.
\]

The first three factors belong primarily to main/Stage14-s. The new fourth factor is the t-side target.

## Finite diagnostic

The frozen exact Stage14 census through

```text
B = 2,000,000
```

has

```text
raw active oriented face vertices = 490
triple objects T(B)                = 0
```

so no compatible physical paired point producing a retained primitive triple object is observed at that cutoff. This is finite diagnostic evidence only and is not used as an asymptotic input.

## Next theorem interface

A useful `14-t12` theorem would control the conditional shared-q lift among raw small points. Two equivalent formulations are:

1. **point-conditioned reflected square sieve**: average, over raw physical small points `(F,q)`, the indicator that the reflected quartic is a square;
2. **fiber-product small-point count**: bound rational points of physical height `<=B` on the moving genus-5 family `C_F` after averaging over primitive Euclid parameters.

The first formulation is likely better aligned with Stage14-s5c and the explicit descent/reciprocity matrix, because it conditions on the raw point instead of restarting from all eligible bases.

## Locked boundary

```text
STAGE14_T11=COMPLETE_COMPATIBLE_PAIRED_ACTIVATION_FORMULATION
PAIR_REQUIRES_SHARED_Q=true
SIMULTANEOUS_POSITIVE_RANK_SUFFICIENT=false
SIMULTANEOUS_UNRELATED_SMALL_POINTS_SUFFICIENT=false
MU_RAW_LE_MU_PAIR=true
V_PAIR_SUBSET_V_RAW=true
PAIR_CONDITIONAL_DENSITY_DEFINED=true
OBJECT_LEVEL_PAIR_COUNT_REQUIRED=true
FINITE_B2M_RAW_ACTIVE_VERTICES=490
FINITE_B2M_TRIPLE_OBJECTS=0
FINITE_ZERO_IMPLIES_ASYMPTOTIC_ZERO=false
PAIR_THINNING_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t12 point-conditioned reflected-square average / moving fiber-product small-point bound
```
