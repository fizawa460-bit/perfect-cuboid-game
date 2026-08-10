# Radical incidence quantifier boundary

```yaml
ID: TB-WARNING-radical-incidence-quantifier-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Keep selected kernels, full radicals, coordinate density, and packet existence distinct
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bj
SOURCE_PR: 355
SOURCE_MERGE_SHA: 7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7
SOURCE_FILES:
  - stages/stage14/14-4bi-L/result.md
  - stages/stage14/14-4bi-S/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

Any use of the kernel/radical incidence toolbox in a family count.

## OUTPUT

Preserve these distinctions:

```text
a,b,c                    = selected odd edge kernels
R_S,R_X,R_H               = full odd leg radicals
P^+(abc)                  = one largest prime diagnostic only
rectangle incidence gain = coordinate-density statement
packet count              = existential one-per-packet statement.
```

The merged results specifically imply

```text
large-but-smooth kernel is not an obstruction
small selected kernel is not an intrinsic modulus obstruction
full-radical coordinate saving is not automatically delta_post.
```

Never perform the unsupported multiplication

```text
B^(41/42) * B^(-delta_coord)
```

unless an existence/occupancy transfer theorem has been proved for the moving packet family.

## VARIABLE DICTIONARY

- `delta_coord` = saving inside a fixed witness-coordinate box.
- `delta_post` = saving in the unweighted moving packet/base count after the local theorem.
- `P^+` = largest prime factor; no longer the canonical incidence-size variable once composite/full-radical moduli are available.

## USED BY

- Main/s cross-route proof audits.
- Preventing obsolete largest-prime splits from being reintroduced.
- Checking whether a claimed exponent is coordinate-level or packet-level.

## DO NOT USE FOR

- Do not interpret this warning as saying coordinate incidence is useless; it is a proved structural input whose transfer remains separate.
- Do not treat `R_H<=B^(1/2)` as a coordinate-density statement; that sector has a genuine base/class bound.

## PROVENANCE NOTES

Merged PR #349 removes largest-prime dependence, merged PR #352 upgrades to full radicals, and merged PR #355 freezes the surviving existence-vs-coordinate-density quantifier gap.