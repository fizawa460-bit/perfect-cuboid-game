# Stage29-14 source refresh

Fresh source check was limited to the slice/coverage claims actually used here.

## Current Testa--Stoll low-degree source

The current publication record for Testa--Stoll, *Curves on the surface of cuboids*, DOI `10.1090/mcom/4238`, and the current arXiv/public preprint lineage continue to state the complete classification of integral curves of degree at most six on the cuboid surface. This agrees with the already-audited Stage29 source lock and does not change the 29-10/29-14 scope:

```text
ALL_INTEGRAL_CURVES_DEGREE_LE_6_CLASSIFIED=true
ALL_ENDPOINT_Q_POINTS_ON_DEGREE_LE_6_CURVES=false
```

The second line is a firewall: no source located in this refresh proves that every physical rational endpoint point lies on a low-degree rational/elliptic carrier.

## Other curve/family literature

Older cuboid-factor and elliptic-curve papers produce special rational/elliptic families or reducibility cases. They are not promoted in 29-14 to global coverage statements without an exact reverse map from arbitrary endpoint candidates. Those families are better handled in the scheduled 29-15 Arsenal/literature rematch.

No fresh source found in this bounded refresh certifies any of the following:

```text
EVERY_ENDPOINT_Q_POINT_LIES_ON_A_KNOWN_CLOSED_CURVE=false
FINITE_CLOSED_SLICE_UNION_COVERS_ENDPOINT_Q_POINTS=false_as_a_proved_statement
ALL_28_GENUS5_FIBRATIONS_Q_DEFINED=false_as_a_certified_statement
KNOWN_SECTIONS_GENERATE_ALL_ENDPOINT_Q_POINTS=false
K3_QUOTIENT_QPOINT_EMPTY=false_as_a_certified_statement
```

Here `false_as_a_proved_statement` means no such theorem is certified; it does not assert the logical negation if the endpoint rational set is empty.

## Source-use policy

29-14 therefore relies primarily on already-audited repository source locks plus elementary exact deductions from the F7 square coordinates. The broader missing-literature search remains assigned to `29-15_ENDPOINT_ARSENAL_REMATCH`.
