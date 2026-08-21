# Stage29-02hc — non-Fano / Hirzebruch-cover foundation

## Verdict

`HIGH_VALUE_NEW_NAMED_GLOBAL_FOUNDATION` — audit required.

The audited Stage29-02ha seven-line sign cover is not merely analogous to a standard arrangement construction. After an explicit `PGL_3(Q)` coordinate change, its branch divisor is the classical **non-Fano arrangement**. The full endpoint canonical cover is therefore the `N=2` branched congruence/Kummer cover of that arrangement, and its minimal resolution is the classical **Hirzebruch covering surface `M_2(NF)`**.

No literature-novelty claim is made. The new repo content is the exact cuboid-to-non-Fano adapter and the identification of the endpoint with the named Hirzebruch surface package.

## 1. Exact Q-projective identification of the seven lines

Write the Stage29-02ha base coordinates as `[x:y:z]=[a1^2:a2^2:a3^2]`. The branch divisor is

```text
D_cub : x y z (x+y)(x+z)(y+z)(x+y+z)=0.
```

The rational projective change

```text
x = X,
y = -Y,
z = Z-X
```

sends these seven factors, up to nonzero scalar multiples and permutation, to

```text
X,
Y,
Z,
X-Y,
X-Z,
Y-Z,
X+Y-Z.
```

Hence

```text
D_cub  ~=_Q  D_NF,
Q_NF = XYZ(X-Y)(X-Z)(Y-Z)(X+Y-Z).
```

Suciu Example 10.5 uses exactly this defining polynomial for the non-Fano arrangement. Schenck–Tohaneanu Example 1.7 identifies the non-Fano arrangement as the unique configuration of seven projective lines with six triple points; this independently matches the audited `t3=6,t2=3` incidence ledger.

```text
R29-NF0 = CuboidSevenLineArrangementToNonFanoPGL3QAdapter
STATUS = PASS_CANDIDATE
```

## 2. The 64-sheet endpoint is the N=2 congruence/Kummer cover

For a projective arrangement of `n=7` lines, the complement has

```text
H1(P2\D,Z) ~= Z^(n-1) = Z^6.
```

Hirzebruch's/Suciu's level-`N` branched congruence cover has deck group

```text
(Z/N)^(n-1).
```

At `N=2` this is

```text
(Z/2)^6,
degree = 2^6 = 64,
```

exactly the audited Stage29-02ha sign deck group and degree. On the arrangement complement, the cuboid cover adjoins square roots of the seven branch forms modulo the single global projective sign relation, so it is the canonical mod-2 congruence cover itself, not a selected subcover.

Let `Xbar_2(NF)` denote the normal branched congruence cover and `M_2(NF)` its minimal desingularization. Then the proposed exact identification is

```text
Sbar_cub ~=_Q Xbar_2(NF),
S_cub    ~=_Q M_2(NF).
```

The first line is an equality of the normal sign/Kummer constructions after the displayed `PGL3(Q)` base change; the second is the uniqueness of minimal resolution of the resulting A1 surface singularities.

```text
R29-NF1 = EndpointEqualsNonFanoHirzebruchM2
STATUS = PASS_CANDIDATE
```

## 3. Independent recovery of the cuboid invariants from arrangement theory

For non-Fano:

```text
n=7,
s=9,
m2=3,
m3=6,
b2=15.
```

Hirzebruch's Chern-number formula, quoted as Suciu Theorem 6.3, gives for this arrangement

```text
c1^2(M_N) = N^4(10N^2 - 32N + 25),
c2(M_N)   = N^4( 4N^2 - 16N + 21).
```

At `N=2`:

```text
c1^2 = 16,
c2    = 80.
```

Suciu Example 10.5 gives

```text
b1(M_N)=9(N-1)(N-2),
```

hence

```text
b1(M_2)=0,
q=0.
```

Noether then gives

```text
chi(O)=(16+80)/12=8,
pg=chi-1+q=7.
```

These independently recover the audited cuboid values

```text
K^2=16,
pg=7,
q=0,
c2=80.
```

At each non-Fano triple point (`r=3`) the `N=2` branched congruence cover has

```text
2^(6-3)=8
```

points above it. With six triple points this gives `6*8=48`, recovering the full node count again from the general Hirzebruch-cover construction.

```text
R29-NF2 = HirzebruchInvariantAndNodeRecovery
STATUS = PASS_CANDIDATE
```

## 4. Characteristic-variety package now becomes available

Suciu computes the characteristic varieties of the non-Fano arrangement explicitly:

```text
V1 = six local components + three non-local braid components,
V2 = {1,rho},
rho=(1,-1,-1,1,-1,-1,1),
```

with a special order-2 character `rho`. The congruence-cover Betti numbers exhibit parity:

```text
b1(X_N)=9N^2-3  (N even),
        =9N^2-2  (N odd).
```

The compact Hirzebruch surfaces satisfy

```text
b1(M_N)=9(N-1)(N-2).
```

Thus the cuboid endpoint sits at the most 2-primary member `N=2` of a named arrangement-cover tower whose topology is controlled by torsion characters and characteristic varieties.

This opens a genuinely different toolbox:

- arrangement-complement fundamental groups;
- Alexander matrices;
- characteristic/resonance varieties;
- Sakuma/Hironaka formulas for finite abelian covers;
- explicit mod-2 resonance and the distinguished character `rho`.

No arithmetic obstruction is imported merely from these complex-topological facts.

```text
R29-NF3 = NonFanoCharacteristicVarietyToEndpointDeckCharacterLedger
R29-NF4 = DistinguishedOrder2CharacterToCuboidIntermediateDoubleCover
R29-NF5 = ArrangementFiniteAbelianCoverTopologyToCampedelliAndK3Quotients
```

## 5. Physical/rational-point firewall

The full arrangement complement removes all seven branch lines. The physical algebraic open from Stage29-02f deletes only the side-zero divisors (plus exceptional boundary on the resolution). Over `Q`, however, a nondegenerate rational cuboid cannot have a face diagonal or space diagonal equal to zero, so every physical rational endpoint point lies over the full seven-line complement.

Therefore the arrangement-complement cover may be used as a **necessary-locus** for rational endpoint points, but its complex boundary and Brauer theory are not automatically equal to those of the Stage29-02f physical open.

```text
PHYSICAL_OPEN_EQUALS_ARRANGEMENT_OPEN=false
PHYSICAL_Q_POINTS_LIE_IN_ARRANGEMENT_OPEN=true
BRAUER_TRANSFER_AUTOMATIC=false
```

## 6. Relation to earlier Stage29 foundations

This is not a renamed `ha` claim. `ha` supplied the raw seven-line sign cover. `hc` identifies that object with a named classical global construction carrying a pre-existing theorem package.

It also reframes `hb`: the ten Campedelli quotients are rank-3 quotients of the `N=2` Hirzebruch deck group. The seven K3 quotients and the joint-V4 layers likewise become finite abelian quotients/subcovers of one standard congruence cover.

Promising new bridges:

```text
R29-NF6 = CampedelliKernelsInsideNonFanoCongruenceCharacterLattice
R29-NF7 = Stage29_02fTwoPrimaryBoundaryVsNonFanoMod2Resonance
R29-NF8 = Stage16To20PopulationMasksVsArrangementSubcoverCharacterSupport
```

`R29-NF7` and `R29-NF8` are receivers only; no Brauer or population theorem is claimed.

## Routing

```text
NOVELTY_IN_REPO=HIGH_VALUE_NEW_NAMED_GLOBAL_FOUNDATION
LITERATURE_NOVELTY_CLAIM=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM_AFTER_PASS=29-02hd
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
