# Stage29-14 source refresh

Fresh source check was limited to the slice/coverage claims actually used here.

## Current Testa--Stoll low-degree source

The current publication record for Testa--Stoll, *Curves on the surface of cuboids*, DOI `10.1090/mcom/4238`, and the current arXiv/public preprint lineage continue to state the complete classification of integral curves of degree at most six on the cuboid surface. This agrees with the already-audited Stage29 source lock and does not change the 29-10/29-14 scope:

```text
ALL_INTEGRAL_CURVES_DEGREE_LE_6_CLASSIFIED=true
ALL_ENDPOINT_Q_POINTS_ON_DEGREE_LE_6_CURVES=false
```

The second line is a firewall: no source located in this refresh proves that every physical rational endpoint point lies on a low-degree rational/elliptic carrier.

### Fresh audit provenance lock

The public verification source was re-read at the immutable repository state already locked by 29-02c-LG2:

```text
repo=https://github.com/MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

It explicitly constructs the finite low-degree curve configuration on the canonical cuboid surface and performs the Picard/K3 computations used in the classification. In particular the code:

- constructs the known conic and genus-one curve orbits;
- checks the rank-64 intersection lattice used for the endpoint Picard computation;
- excludes additional conic candidates in the relevant search;
- handles the degree-four candidate classes via the Picard/K3 machinery;
- runs the K3-assisted lift search for degree six and concludes that there are no degree-six integral curves on the canonical surface.

The explicit known low-degree equations meet the physical Q-open only degenerately or not at all: representative equations force a zero side/diagonal, equality of squared sides incompatible with the face-square condition, or coefficients requiring `i` or `sqrt(2)`. Thus the imported disposition

```text
POSITIVE_NONDEGENERATE_PHYSICAL_FAMILY_AT_DEGREE_LE_6=false
```

is retained. This is a carrier statement, not an isolated-point statement.

## Other curve/family literature

Older cuboid-factor and elliptic-curve papers produce special rational/elliptic families or reducibility cases. They are not promoted in 29-14 to global coverage statements without an exact reverse map from arbitrary endpoint candidates. Those families are better handled in the scheduled 29-15 Arsenal/literature rematch.

No fresh certified source found in this bounded refresh supplies any of the following:

```text
EVERY_ENDPOINT_Q_POINT_LIES_ON_A_KNOWN_CLOSED_CURVE=false_as_a_proved_statement
FINITE_CLOSED_SLICE_UNION_COVERS_ENDPOINT_Q_POINTS=false_as_a_proved_statement
ALL_28_GENUS5_FIBRATIONS_Q_DEFINED=false_as_a_certified_statement
KNOWN_SECTIONS_GENERATE_ALL_ENDPOINT_Q_POINTS=false
K3_QUOTIENT_QPOINT_EMPTY=false_as_a_certified_statement
```

Here `false_as_a_proved_statement` means no such theorem is certified; it does not assert the logical negation if the endpoint rational set is empty.

## Audit strengthening of K3 pushforward

The canonical/resolution distinction from 29-06 was re-used explicitly. Since a physical endpoint Q-point avoids the coordinate-sign fixed locus and the F7 branch arrangement, its image under each Q-defined coordinate-sign quotient lies in the smooth locus of the normal quotient `Kbar_j`. The minimal resolution `K_j -> Kbar_j` is an isomorphism there, so the physical endpoint point gives a Q-point on `K_j` as well.

This strengthens only the forward implication:

```text
PHYSICAL_ENDPOINT_QPOINT -> Kbar_j(Q)_smooth -> K_j(Q)
```

No converse lift or quotient-point emptiness theorem is inferred.

## Source-use policy

29-14 therefore relies primarily on already-audited repository source locks plus elementary exact deductions from the F7 square coordinates. The broader missing-literature search remains assigned to `29-15_ENDPOINT_ARSENAL_REMATCH`.
