# Stage29-02ha — coordinate K3 quotients as six-line subcovers

Let `g_T` be the deck involution changing the sign of one canonical coordinate

```text
T in {a1,a2,a3,b1,b2,b3,c}.
```

The quotient

\[
K_T:=\bar S/\langle g_T\rangle
\]

still maps to `P^2`. The inertia of the branch line `L_T=0` becomes trivial after quotienting by `g_T`, while the other six branch involutions remain. Therefore

\[
K_T\to\mathbf P^2
\]

is generically the uniform

\[
(\mathbf Z/2)^5
\]

Kummer cover branched along the **other six** lines.

The abelian-cover canonical formula now gives

\[
K_{K_T}=\pi_T^*\left(-3H+\frac12(6H)\right)=0
\]

away from the rational-double-point corrections. Testa–Stoll independently certify that the minimal resolutions of these seven coordinate-sign quotients are K3 surfaces. Thus the line-cover model explains structurally why deleting exactly one of seven square-root conditions lands at the K3 boundary between general type and Calabi–Yau type.

## The audited `3+1+3` arithmetic pattern becomes visible on the branch arrangement

Under the rational index-permutation symmetry `S3`, the seven branch lines split as

```text
{A1,A2,A3}     size 3
{B1,B2,B3}     size 3
{C}             size 1.
```

The Stage29-02e audited K3/newform assignment is exactly

```text
omit B_i -> K_b -> h16   (3 copies)
omit C   -> K_c -> h32   (1 copy)
omit A_i -> K_a -> h8    (3 copies).
```

The full geometric line-arrangement automorphism group has order 24 and acts with line orbits

```text
{A1,A2,A3,C}   size 4
{B1,B2,B3}     size 3.
```

The first orbit enlargement requires the non-rational lift visible in the Testa–Stoll automorphism involving `i`; this is consistent with the audited fact that `K_a` and `K_c` become isomorphic over `Q(i)` while their Q-forms carry different modular signals.

This provides a single geometric explanation for the previously separate facts

```text
7 coordinate K3 quotients
= 3 K_b + 1 K_c + 3 K_a
<-> 3 h16 + 1 h32 + 3 h8.
```

## Canonical eigenspaces

The seven canonical coordinates are also seven distinct one-dimensional character eigenspaces for the sign deck group in `H^0(K_S)`. Hence the coordinate-K3 decomposition used in Stage29-02e is naturally the character decomposition of this full sign-cover tower rather than an accidental collection of seven quotients.

```text
R29-KUM2=CoordinateK3AsSixLineKummerSubcovers
STATUS=PASS_CANDIDATE
R29-KUM2A=ArithmeticThreeOneThreeFromBranchLineQOrbits
STATUS=PASS_CANDIDATE_NEEDS_FRESH_AUTOMORPHISM_SCOPE_AUDIT
```
