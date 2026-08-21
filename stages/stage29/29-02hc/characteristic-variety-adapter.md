# Non-Fano characteristic-variety adapter

The identification with the non-Fano arrangement opens a topological finite-cover package that was not available in the cuboid coordinates alone.

## Published non-Fano data

Suciu Example 10.5 records

```text
V1 = C125 ∪ C136 ∪ C246 ∪ C345 ∪ C237 ∪ C567 ∪ Pi1 ∪ Pi2 ∪ Pi3,
Pi1=C(25|36|47),
Pi2=C(17|26|35),
Pi3=C(14|23|56),
V2={1,rho},
rho=(1,-1,-1,1,-1,-1,1)
```

over characteristic zero, with special mod-2 resonance behavior.

The same source records

```text
b1(X_N)=9N^2-3  if N even,
        =9N^2-2  if N odd,

b1(M_N)=9(N-1)(N-2).
```

Here `X_N` is the unbranched congruence cover of the arrangement complement and `M_N` the compact Hirzebruch covering surface.

## Endpoint at N=2

The endpoint deck group is the full elementary 2-abelian congruence group. Therefore its character group is exactly the set of order-dividing-two characters of the projective arrangement complement.

The isolated character `rho` and the nine components of `V1` give an exact finite character-support ledger for the open 64-sheet cover. This is qualitatively different from the K3/newform decomposition of 29-02e: it concerns the topology of the **arrangement complement cover** and the behavior of deck characters before compactification.

At `N=2`, compactification/resolution kills irregularity completely:

```text
b1(M_2)=0,
```

while the unbranched congruence cover has nontrivial first homology. This makes the branch/boundary attachment itself load-bearing.

## New receivers

```text
R29-NF3A = ExactOrder2CharacterSupportLedgerForEndpointArrangementOpen
R29-NF3B = IdentifyRhoAsExplicitCuboidSignCharacter
R29-NF3C = BoundaryAttachmentMapKillingOpenH1AtN2
R29-NF3D = CompareCharacterSubspacesWithSevenK3AndTenCampedelliQuotients
```

Potential relevance:

- `R29-NF3C` may organize the Stage29-02f boundary complex from the opposite, topological side.
- `R29-NF3D` may select which intermediate quotients carry exceptional local-system cohomology, reducing blind quotient searches.

## Firewall

Characteristic varieties and Betti numbers are complex-topological invariants. They do **not** by themselves imply absence of `Q`-points, Brauer-Manin obstruction, height saving, or population decay.

```text
RATIONAL_POINT_OBSTRUCTION_PROVED=false
BRAUER_OBSTRUCTION_PROVED=false
POPULATION_SAVING_PROVED=false
```
