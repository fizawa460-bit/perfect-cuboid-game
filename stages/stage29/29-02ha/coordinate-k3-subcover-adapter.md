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

is generically a

\[
(\mathbf Z/2)^5
\]

Kummer cover branched along the **other six** lines.

The finite-cover Riemann--Hurwitz formula gives

\[
K_{K_T}=\pi_T^*\left(-3H+\frac12(6H)\right)=0
\]

as a `Q`-Cartier class on the normal quotient. Testa--Stoll independently certify that the minimal resolutions of the seven coordinate-sign quotients are K3 surfaces, so the rational-double-point corrections are crepant. Thus deleting exactly one of the seven branch characters lands at the K3 boundary.

## Exact Q versus Q(i) symmetry audit

The seven-line arrangement itself has a projective automorphism group

```text
Aut_P2(D) ~= S4,
|Aut_P2(D)|=24,
```

and all 24 transformations are represented by matrices over `Q`. That statement is only about the **base plane**. A base projectivity lifts to the full sign cover over a field `F` iff the seven line multipliers have one common class in `F*/F*^2`.

The exact audit in `arrangement_check.py` evaluates this cocycle for all 24 projectivities:

```text
Q-liftable base transformations:      6  ~= S3
Q(i)-liftable base transformations:  24  ~= S4.
```

Therefore the line orbits on coordinate-sign quotients are exactly

```text
Q:
{A1,A2,A3}       size 3
{B1,B2,B3}       size 3
{C}               size 1

Q(i):
{A1,A2,A3,C}     size 4
{B1,B2,B3}       size 3.
```

This closes the field-of-definition scope that was left open at submission. In particular, it gives a direct sign-cover explanation of the previously audited arithmetic pattern

```text
3*K_a + 3*K_b + 1*K_c
<-> 3*h8 + 3*h16 + 1*h32,
```

while the enlargement `K_a ~= K_c` occurs only after adjoining `i`.

## Full geometric automorphism group recovered

The sign deck group has order `64`. The audited base arrangement group has order `24`, and all 24 lift geometrically. Hence the sign-cover construction produces a geometric automorphism subgroup of order

```text
64 * 24 = 1536.
```

Testa--Stoll Theorem 1 independently proves that the **full** geometric automorphism group has order `1536` and fits the exact sequence

```text
1 -> mu_2^7/mu_2 -> Aut(Sbar) -> S4 -> 1.
```

Consequently the sign/Kummer tower recovers the full automorphism group, not merely a proper subgroup. Over `Q`, the liftable base subgroup is the six-element `S3`, so the corresponding Q-defined sign semidirect subgroup has order `64*6=384`.

## Canonical eigenspaces

The seven canonical coordinates are seven distinct one-dimensional character eigenspaces for the sign deck group in `H^0(K_S)`. Hence the coordinate-K3 decomposition used in Stage29-02e is naturally the character decomposition of this full sign-cover tower rather than an accidental collection of seven quotients.

```text
R29-KUM2=CoordinateK3AsSixLineKummerSubcovers
STATUS=PASS_AUDITED
R29-KUM2A=ArithmeticThreeOneThreeFromBranchLineQOrbits
STATUS=DISCHARGED_BY_EXACT_Q_QI_LIFT_COCYCLE
BASE_ARRANGEMENT_AUT_GROUP=S4
Q_LIFTABLE_BASE_SUBGROUP=S3
QI_LIFTABLE_BASE_GROUP=S4
FULL_GEOMETRIC_AUT_ORDER_RECOVERED=1536
```
