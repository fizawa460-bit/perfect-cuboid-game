# Quantifier ladder warning

```yaml
ID: TB-WARNING-quantifier-ladder
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not promote coordinate incidence directly to packet, base, or family counts
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
A saving proved for coordinates or witnesses inside a fixed packet, such as a CRT line-cover bound.

## OUTPUT
Keep the levels distinct:
```text
coordinate -> witness -> packet existence -> active base/direction -> sector -> whole family.
```
A transfer upward requires a proved selector/reconstruction and multiplicity bound.

## VARIABLE DICTIONARY
- coordinate = one integer/rational representative.
- packet = arithmetic class that may admit many or no representatives.
- active base/direction = a physical parameter supporting at least one hit.

## USED BY
- Deciding whether an incidence saving changes a Stage14 exponent.
- Auditing post-local arguments.

## DO NOT USE FOR
- Do not multiply `B^-eta` coordinate density into an unweighted packet count without a transfer theorem.
- Existence of one sparse representative does not imply sparse packet support.

## PROVENANCE NOTES
Merged 4bj explicitly preserves the coordinate-density versus packet-existence quantifier gap.