# Stage33-05 source lock — Creutz--Viray finite presentation

Primary source:

- Brendan Creutz, Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, arXiv:1306.3251v3, Math. Ann. 362 (2015), 1169--1200.
- Load-bearing locators: Theorem I; §2.3 (`x-alpha`, `gamma'`); Theorem 5.2; Corollaries 5.4--5.5; §6 dimension calculation, including Corollary 6.3 / Example 6.4 as used by the frozen Stage29 audit.

Stage33 uses the source only in the already-audited direction:

```text
reduced flat branch with simple singularities on a ruled surface
  -> finite presentation of geometric Br[2]
     by explicit unramified central-simple-algebra generators
     modulo relations coming from NS(X)
  -> presentation carries Galois action and can support arithmetic descent
```

The source itself emphasizes that group structure alone does not suffice for Brauer--Manin arithmetic; explicit representatives are needed. Accordingly Stage33-05 grants no Q-defined-class credit until the `L_{c,E}` / `x-alpha` quotient and Galois action have actually been materialized.

Internal source locks:

- `stages/stage29/29-15/k3-ruled2-audit-execution.md`
- `stages/stage29/29-02e/result.md`
- `stages/stage33/33-00/unit-closure-contract.md`

```text
SOURCE_THEOREM_APPLICABILITY=FROZEN_AUDITED
FINITE_PRESENTATION_MATERIALIZED=false
QI_OVER_Q_BRAUER_ACTION_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
```
