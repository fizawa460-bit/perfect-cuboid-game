# Stage32 MB104 — U12 prime-to-dyadic standard-Hecke exclusion — 2026-09-17

Status: **STANDARD CONNECTED AWAY-DYADIC HECKE SUBCLASS EXCLUDED / DYADIC COMMENSURATOR OPEN / NO MAIN CREDIT**

## Scope

Continue the conditional U12 Bolza reduction for the dangerous `000707000f0f` equality packet:

```text
B --p1,p2--> C2,
C2: y^2=2(x^5-x),
deg p1=deg p2=56l,
p1,p2 etale,
(p1,p2) birational,
p2^*theta0 ~= p1^*theta1,
```

where `theta0=O(w0)` and `theta1=O(w1)` are two specified odd theta characteristics attached to different retained Weierstrass-type pairs.

This note excludes only the standard connected Hecke correspondences whose adelic double-coset representative is trivial at the dyadic place `(sqrt(2))`, and for which the full Bolza level-automorphism action transports the correspondence.  Arbitrary commensurator correspondences and correspondences with nontrivial dyadic local component remain open.

## 1. Transporting one spin equality by the Bolza level symmetry

The six Weierstrass points carry the standard `S4=PGL2(F3)` action on the six edges of a tetrahedron.  The retained pair `(w0,w1)` lies in the adjacent-edge orbit.

The companion exact verifier

```text
verify_mb104_u12_bolza_j2_centralizer.py
```

checks that ordered adjacent edge pairs form one `S4` orbit of size `24`.

For an `S4`-equivariant correspondence, applying the level symmetry to

```text
p2^*theta0 ~= p1^*theta1
```

therefore gives the analogous equality for every ordered adjacent pair `(a,b)`:

```text
p2^*theta_a ~= p1^*theta_b.                    (ORB-SPIN)
```

Fix an edge `a`.  It has four adjacent edges `b`.  Comparing `(ORB-SPIN)` for two such neighbors `b,c` gives

```text
p1^*(theta_b theta_c^(-1)) = 0 in J(B)[2].      (KILL-a)
```

The exact verifier checks:

```text
for one fixed anchor a:
  these neighbor-differences span rank 3 in J(C2)[2];

over all six anchors:
  the generated differences have rank 4;
  in fact all 15 nonzero classes of J(C2)[2] occur.
```

Hence the full transported spin passport forces

```text
p1^* : J(C2)[2] -> J(B)[2]
```

to be the zero map.  By symmetry the same holds for `p2^*`.

This is stronger than the earlier norm/Hecke-operator shadow `T|J[2]=0`: it kills the pullback itself.

## 2. Topological subgroup consequence

Let

```text
Gamma = pi_1(C2),
Lambda <= Gamma
```

be the index-`56l` subgroup corresponding to `p1:B->C2`.

The pullback on mod-two cohomology is restriction:

```text
H^1(Gamma,F2) -> H^1(Lambda,F2).
```

If this map is zero, every homomorphism `Gamma->F2` vanishes on `Lambda`.  Therefore

```text
Lambda <= Gamma^(2) := [Gamma,Gamma] Gamma^2.    (HOM2)
```

For a genus-two surface group,

```text
Gamma/Gamma^(2) ~= H_1(C2,F2) ~= (F2)^4,
[Gamma:Gamma^(2)] = 16.
```

Thus every equivariant realization satisfying the full transported spin passport obeys the necessary divisibility

```text
16 | [Gamma:Lambda] = 56l,
```

hence

```text
l is even.                                      (L-EVEN)
```

This congruence is unconditional once the `S4`-equivariant transport hypothesis is imposed.

## 3. Relation with the Bolza congruence level

Katz--Katz--Schein--Vishne identify the Bolza group `Gamma=B_Bolza` as a congruence subgroup of the Bolza quaternion order and prove

```text
P Q_B^1(2) < Gamma < P Q_B^1(sqrt(2)),
Gamma / P Q_B^1(2) ~= (Z/2)^2.
```

The quotient on the right is elementary abelian.  Hence the mod-two homology kernel satisfies

```text
Gamma^(2) <= P Q_B^1(2).
```

Combining with `(HOM2)` gives

```text
Lambda <= P Q_B^1(2).                           (LEVEL2-DROP)
```

So the U12 packet does not merely require even degree: in this equivariant subclass the source subgroup must drop through the proper level-`2` congruence cover.

## 4. Standard away-dyadic Hecke correspondences are incompatible

The same arithmetic source proves that the Bolza quaternion algebra is ramified at the unique dyadic prime `(sqrt(2))` and split at every other finite place.

Consider now a **standard connected Hecke correspondence supported away from `(sqrt(2))`**.  In the usual adelic Hecke construction its local double-coset component at the dyadic place is the identity, so the Bolza compact-open/level structure at `(sqrt(2))` is unchanged.  Equivalently, under the standard strong-approximation/CRT level semantics, the source arithmetic subgroup retains the Bolza image in the quotient

```text
Gamma / P Q_B^1(2) ~= (Z/2)^2
```

rather than being contained in the proper kernel `P Q_B^1(2)`.

That contradicts `(LEVEL2-DROP)`.

Therefore, within this explicitly scoped standard-Hecke subclass,

```text
prime-to-dyadic Hecke support
+ Bolza level-symmetry equivariance
+ U12 spin passport
=> impossible.                                  (AWAY2-EXCLUDE)
```

In particular the infinite odd-prime Hecke families that survive the degree-only U10/U12 test cannot realize the full MB104 spin passport in this subclass.

## 5. What remains

`(AWAY2-EXCLUDE)` is not a closure of U12 or MB104.  The arithmetic `(2,3,8)` commensurator can contain correspondences with nontrivial dyadic local component, and the quaternion algebra is division at that very place.  Those are not covered by the unchanged-level argument.

The live arithmetic target becomes

```text
U12-DYADIC-LOCAL:
  classify the possible local double cosets at the ramified prime (sqrt(2))
  that can satisfy the exact odd-theta pullback passport,
  and determine their allowed global degrees 56l.
```

This is substantially narrower than generic commensurator classification: every remaining arithmetic realization must carry a nontrivial dyadic level change.

## Exact finite verifier

```text
verify_mb104_u12_bolza_j2_centralizer.py
```

replays, over `F2`, all finite claims used above:

- the `3+12` orbit decomposition of nonzero `J[2]`;
- the four-element `S4` centralizer;
- the 24-element ordered-adjacent-pair orbit;
- rank `3` of neighbor differences at each fixed anchor;
- rank `4` globally;
- occurrence of all `15` nonzero `J[2]` classes among the transported differences.

It deliberately does not encode the adelic unchanged-level statement; that part is the scoped arithmetic input of this note.

## Source boundary

Arithmetic source:

K. Katz, M. Katz, M. Schein, U. Vishne,
*Bolza Quaternion Order and Asymptotics of Systoles Along Congruence Subgroups*, Experimental Mathematics 25 (2016), 399--415.

Used facts:

- Theorem 1.5 / Section 13: the Bolza group lies strictly between the principal congruence groups of levels `2` and `sqrt(2)`;
- Corollary 13.4 and Remark 13.5: the Bolza symmetry quotient and `Gamma/PQ_B^1(2) ~= (Z/2)^2`;
- Proposition 5.5: the quaternion algebra is ramified at `(sqrt(2))` and split at all other nonarchimedean places.

The statement about a standard Hecke correspondence supported away from the dyadic place retaining the dyadic compact-open is the usual adelic definition of an away-from-level Hecke correspondence; it is part of the scope assumption here, not a classification of arbitrary commensurator elements.

## Firewalls

```text
standard_connected_away_dyadic_Hecke_excluded=true
arbitrary_commensurator_excluded=false
dyadic_local_component_classified=false
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
