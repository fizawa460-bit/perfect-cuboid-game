# Gap Scan B — mod 7 / mod 19 perfect-cuboid literature check

```text
ROLE=SECONDARY_EXTERNAL_NOVELTY_CHECK
MOD7_STANDARD_EDGE_DIVISIBILITY=KNOWN
MOD19_STANDARD_EDGE_DIVISIBILITY=KNOWN
NOVELTY_CLAIM_FOR_STANDARD_STATEMENTS=false
```

## Exact classical source

Tim S. Roberts, “Some constraints on the existence of a perfect cuboid,” *Australian Mathematical Society Gazette* 37(1) (2010), 29–31.

Stable publisher PDF:

`https://www.austms.org.au/wp-content/uploads/Gazette/2010/Mar10/TechPaperRoberts.pdf`

The paper was received 9 February 2009 and accepted 10 November 2009. On page 29 Roberts announces three then-previously-unpublished primitive perfect-cuboid constraints. Page 30 contains the two relevant theorems and proofs.

### Mod 7

Roberts Theorem 1 proves that at least one edge of every perfect cuboid must be divisible by `7`. The proof enumerates quadratic residues modulo 7 and observes that every admissible triple of edge-square residue classes contains `0`.

```text
CLAIM=AT_LEAST_ONE_PERFECT_CUBOID_EDGE_DIVISIBLE_BY_7
CLASSIFICATION=KNOWN
SOURCE=ROBERTS_2010_THEOREM_1_PAGE_30
```

### Mod 19

Roberts Theorem 2 proves that at least one edge of every perfect cuboid must be divisible by `19`, by the analogous quadratic-residue check modulo 19.

```text
CLAIM=AT_LEAST_ONE_PERFECT_CUBOID_EDGE_DIVISIBLE_BY_19
CLASSIFICATION=KNOWN
SOURCE=ROBERTS_2010_THEOREM_2_PAGE_30
```

A later perfect-cuboid computer-search report also lists both divisibility constraints and attributes both to Roberts; the Roberts paper is the primary source and is sufficient for provenance.

## Scope firewall

The external reviewer’s exact wording was not supplied beyond “mod 7 and mod 19 divisibility observations may be new.” Therefore this audit only rejects novelty for the standard statements above.

A stronger claim such as

- a prescribed edge rather than at least one edge,
- simultaneous divisibility of specified edges,
- a valuation lower bound,
- a finer residue-class classification,
- or a statement for Euler bricks without the space-diagonal condition

must be checked separately against its exact wording.

```text
UNSPECIFIED_STRONGER_MOD7_OR_MOD19_CLAIM=UNCERTAIN_UNTIL_EXACT_STATEMENT_SUPPLIED
```
