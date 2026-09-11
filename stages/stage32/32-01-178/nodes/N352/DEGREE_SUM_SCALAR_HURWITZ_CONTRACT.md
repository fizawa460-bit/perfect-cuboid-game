# Stage32 32-01-178 N352 — degree-sum scalar Hurwitz contraction

Status: `AUDIT_CANDIDATE_NO_MAIN_CREDIT`

## Scope

N352 is a simplification of the N351 factor-Hurwitz route on the same four current
`e=48` FULL178 strata.  It does not add a stronger geometric hypothesis.  Instead it
checks, in the retained exact Picard64 marking, that the two retained factor-fibre
degrees add to the project degree:

```text
d = n1 + n2.
```

Combining this exact Picard identity with the N351 necessary cap in either factor

```text
ni <= e/2 + 2g - 2
```

gives the scalar necessary condition

```text
d <= e + 4g - 4.
```

For `e=48`, this is `d<=44` for `g=0` and `d<=48` for `g=1`, contradicting all four
current rows `d=174,176,190,192` without any SMT feasibility search.

## Exact retained Picard identity

Use the retained Stage33/Stage32 Picard64 marking and the two six-boundary packs

```text
P1 = [33,36,37,40,41,44]
P2 = [34,35,38,39,42,43].
```

For each boundary label `b` in a pack, the corresponding fibre class is reconstructed as

```text
F_b = 2*C_b + sum(E_j : C_b.E_j = 1).
```

The exact retained intersection matrix must verify:

1. every boundary label has exactly eight incident exceptional curves;
2. the six incidence sets in either pack partition labels `93..140` exactly once;
3. all six reconstructed fibre classes in a pack are equal in Picard64;
4. if `F1,F2` are the two common fibre classes, then as linear functionals on Picard64

```text
19*(D.F1 + D.F2)
  = sum_{i=1}^{92} D.C_i + 5*sum_{j=93}^{140} D.E_j
  = 19*d.
```

Therefore `D.F1 + D.F2 = d`, i.e. `n1+n2=d`, on the entire retained integral Picard64
lattice, not merely on the current terminal list.

## Dependency boundary

N352 source-locks the N351 geometric/Hurwitz derivation of
`ni <= e/2 + 2g - 2`.  It does **not** independently repair or broaden any geometric
hypothesis in that derivation.  In particular the hostile audit must still check the
N351 source argument, including the `g=0` extension, before N352 can earn pruning credit.

N352 itself is independent of:

```text
N260 [1]^48
N280 HNF
N310 fixed x4
N341 selected-x4 Picard SAT
N349 local (4,4)
N349B/N349C
self-square
SMT/QF_LIA satisfiability
```

## Current four rows

```text
g0-d174/e48: scalar cap d<=44, contradiction
ng0-d176/e48: scalar cap d<=44, contradiction
ng1-d190/e48: scalar cap d<=48, contradiction
ng1-d192/e48: scalar cap d<=48, contradiction
```

The leading `n` in the display labels above is only a Markdown list separator marker;
the authoritative verifier uses row ids `g0-d174`, `g0-d176`, `g1-d190`, `g1-d192`.

## Firewalls

```text
N352_SCALAR_CONTRACTION_CANDIDATE=true
N351_GEOMETRIC_SOURCE_AUDIT_STILL_REQUIRED=true
MAIN_PRUNING_CREDIT=false
PRODUCTION_LEAF_CREDIT=false
N350_PRODUCER_REGISTRY_CHANGED=false
FULL178_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
STAGE32_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
HOSTILE_AUDIT_REQUIRED=true
MERGE_AUTHORIZED=false
```
