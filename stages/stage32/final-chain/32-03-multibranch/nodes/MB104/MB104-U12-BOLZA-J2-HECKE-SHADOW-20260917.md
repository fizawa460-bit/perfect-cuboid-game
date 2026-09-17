# Stage32 MB104 — U12 Bolza `J[2]` Hecke-shadow reduction — 2026-09-17

Status: **NEW FINITE MOD-2 NECESSARY CONDITION / STANDARD-HECKE SHADOW ONLY / NOT A CLOSURE / NO CREDIT**

## Scope

Continue the conditional U12 packet-sensitive Bolza reduction:

```text
B --p1,p2--> C2,
C2: y^2=2(x^5-x),
deg p1=deg p2=n=56l,
p1,p2 etale,
(p1,p2) birational onto its image,
p2^* O(w0) ~= p1^* O(w1),
```

where `w0,w1` are specified Weierstrass points belonging to two different retained Weierstrass-type pairs.

This note asks what the last spin equality forces on the Jacobian if the correspondence is a **standard self-adjoint Hecke correspondence** commuting with the Bolza automorphism group.  It does not claim that every MB104 commensurator double coset is of that form.

## 1. Norm shadow of the spin equality

Let

```text
theta0=O_C2(w0),
theta1=O_C2(w1).
```

Both are odd theta characteristics because on a genus-two hyperelliptic curve

```text
2 wj ~ K_C2.
```

The U12 spin passport is

```text
p2^* theta0 ~= p1^* theta1.                    (SPIN)
```

Let

```text
T=(p1)_* p2^*: J(C2)->J(C2)
```

be the induced correspondence endomorphism.  Applying the norm along `p1` to `(SPIN)` gives

```text
T(theta0) ~= theta1^n.
```

Since `n=56l` is even,

```text
theta1^n ~= K_C2^(n/2).
```

Applying the same argument with the two legs exchanged gives

```text
T^dagger(theta1) ~= K_C2^(n/2).
```

For a self-adjoint Hecke correspondence `T=T^dagger`, subtraction gives the exact necessary condition

```text
T(delta)=0,
delta := theta0 tensor theta1^(-1) in J(C2)[2].   (J2-KILL)
```

Thus U12 has a finite mod-two shadow.

## 2. The six Weierstrass points as the tetrahedron-edge action

The holomorphic automorphism group of the Bolza curve is

```text
Aut(C2) ~= GL2(F3),
```

with central hyperelliptic involution.  The center fixes all six Weierstrass points, so the induced permutation action factors through

```text
PGL2(F3) ~= S4.
```

Up to equivariant relabeling this is the standard transitive action of `S4` on the six edges of a tetrahedron.

For a genus-two hyperelliptic curve,

```text
J(C2)[2]
```

is the four-dimensional `F2` space of even subsets of the six branch/Weierstrass points modulo complement.  A nonzero class represented by a pair of Weierstrass points therefore corresponds to an unordered pair of tetrahedron edges.

There are exactly two `S4` orbits:

```text
3  = pairs of opposite tetrahedron edges,
12 = pairs of adjacent tetrahedron edges.
```

The retained U12 points `w0,w1` lie in two different Weierstrass-type pairs, not in one of the three opposite pairs.  Hence

```text
delta=[w0-w1]
```

lies in the 12-element orbit.

## 3. Exact centralizer calculation

The companion verifier

```text
verify_mb104_u12_bolza_j2_centralizer.py
```

constructs the six-edge permutation module, passes to

```text
J[2] = {even vectors in F2^6}/<all-ones>,
```

and enumerates the full `S4`-equivariant endomorphism ring.

The exact result is

```text
|End_{S4}(J[2])| = 4.
```

Its four elements have ranks

```text
0, 2, 4, 4.
```

Writing the unique rank-two element as `N`, one has

```text
N^2=0,
ker(N)=the 3-element opposite-edge orbit plus 0.
```

Equivalently the centralizer is the four-element local algebra

```text
F2[epsilon]/(epsilon^2).
```

The load-bearing consequence is:

```text
if A in End_{S4}(J[2]) kills one vector in the 12-orbit,
then A=0.                                         (CENT-KILL)
```

This is finite exact group theory, not a heuristic representation argument.

## 4. Consequence for standard Bolza Hecke correspondences

A standard Hecke operator away from the level place commutes with the level automorphism action.  Therefore its reduction on `J(C2)[2]` lies in the centralizer above.

Combining `(J2-KILL)` with `(CENT-KILL)` gives the necessary condition

```text
T | J(C2)[2] = 0.                               (HECKE-MOD2-ZERO)
```

So the packet-sensitive spin condition is stronger than merely requiring an even correspondence degree: it forces the **entire** mod-two Jacobian action of a standard self-adjoint Hecke operator to vanish.

## 5. Why this still does not close U12

The Bolza group is itself a 2-adic congruence subgroup.  Katz--Katz--Schein--Vishne prove

```text
Q_B^1(2)/{+-1} < B < Q_B^1(sqrt(2))/{+-1},
B / P Q_B^1(2) ~= (Z/2)^2,
```

while the full symmetry quotient is

```text
Delta(2,3,8)/B ~= GL2(F3).
```

Thus mod-two behavior is unusually degenerate at the Bolza level.  The current note does **not** prove that `(HECKE-MOD2-ZERO)` excludes any infinite standard-Hecke family.  In particular, the Jacobian of the Bolza curve is known to split over `C` as the square of the CM elliptic curve with CM by `Z[sqrt(-2)]`, so even Hecke eigenvalues/mod-two collapse are plausible and must be checked rather than assumed contradictory.

The next exact target is therefore narrower:

```text
U12-BOLZA-SPIN-LOCAL2:
  determine the actual 2-adic/local-level action of primitive Bolza
  Hecke double cosets on the six odd theta characteristics, not merely
  the induced norm operator on J[2].
```

A successful result must decide whether infinitely many degree-`56l` primitive double cosets satisfy the **full pullback equality**

```text
p2^*theta0 ~= p1^*theta1,
```

rather than only its necessary Jacobian norm shadow.

## External source boundary

Used only for the arithmetic/symmetry background:

- Katz--Katz--Schein--Vishne, *Bolza Quaternion Order and Asymptotics of Systoles Along Congruence Subgroups*: the Bolza group is a congruence subgroup between levels `2` and `sqrt(2)`, its orientation-preserving symmetry group is `SL2(F3)`, the full `(2,3,8)` symmetry quotient is `GL2(F3)`, and `B/PQ_B^1(2) ~= (Z/2)^2`.
- Koziarz--Rito--Roulleau, *The Bolza curve and some orbifold ball quotient surfaces*: the Bolza Jacobian is the square of the CM elliptic curve with CM by `Z[sqrt(-2)]`.

The `3+12` orbit decomposition and four-element centralizer are independently replayed by the repository verifier.

## Firewalls

```text
standard_Hecke_shadow_only=true
full_spin_local2_classified=false
U12_closes_000707=false
U12_large_l_bound_proved=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
