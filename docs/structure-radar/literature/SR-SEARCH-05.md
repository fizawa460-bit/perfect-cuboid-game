# StructureRadar literature ledger — search batch 05

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-05-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-031,SR-STR-032,SR-STR-033,SR-STR-036,SR-STR-037,SR-STR-038,SR-STR-039,SR-STR-040
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=primary sources for external theorem claims; audited repo arsenal checked first
NOVELTY_BY_SEARCH_ABSENCE=false

## Primary sources checked

- de la Bretèche--Tenenbaum, *Remarks on the Selberg--Delange method*, Acta Arith. 200 (2021), arXiv:2010.12929: theorem-species support only; receiver-specific factorization, regularity, vertical growth, coefficient majorant and uniformity remain mandatory.
- Yekutieli, *Pythagorean Triples, Complex Numbers, Abelian Groups and Prime Numbers*, arXiv:2101.12166: normalized triples/fixed-hypotenuse enumeration; background only.
- Sharipov, *A note on a perfect Euler cuboid*, arXiv:1104.1716: adjacent cuboid reduction only.
- Ramsden--Sharipov, *On two algebraic parametrizations for rational solutions of the cuboid equations*, arXiv:1208.2587: adjacent rational cuboid parametrization only.

## Decisions

- `SR-STR-031` / `AR-037`: `ACTIVE`; finite-order Selberg--Delange contract, with no uncontrolled conductor or varying expansion-depth promotion.
- `SR-STR-032` / `AR-038`: `PARKED`; raw shared-hypotenuse convolution is not primitive-object multiplicity and moving-base triple correction remains.
- `SR-STR-033` / `AR-039`: `PARKED`; proved mod-7 exactly-one lower subfamily only, not a full `N1` asymptotic or `N2` comparison.
- `SR-STR-036` / `AR-002`: `PARKED`; exact Euclid background, with orientation/parity/scale explicit and face primitivity distinct from cuboid primitivity.
- `SR-STR-037` / `AR-003`: `ACTIVE`; exact two-face gluing/multiplicity-one reconstruction under original primitive/canonical hypotheses.
- `SR-STR-038` / `AR-004`: `ACTIVE`; `E(B)=N2(B)+3T(B)=1/2 sum_F deg_B(F)`, preserving raw-pair measure/triple multiplicity/original cutoff; `9T(B)^2 <= Q_edge(B)` is collision measure, not saving.
- `SR-STR-039` / `AR-006`: `ACTIVE`; `N2(B) << B^(1/2+o(1))` only for the Stage14 primitive canonical integral-space exactly-two population; no ambient `M2`, lower, strict sub-half-power, or perfect-cuboid conclusion.
- `SR-STR-040` / `AR-028`: `ACTIVE`; no-double-charge/recharge proof-accounting firewall preserving original measure and quantifier order.

ACTIVE=SR-STR-031,SR-STR-037,SR-STR-038,SR-STR-039,SR-STR-040
PARKED=SR-STR-032,SR-STR-033,SR-STR-036
EXTERNAL_GATE=none
NEW_EXTERNAL_ACTIVE_WEAPONS=0
SEARCHES_COMPLETED=8
ARSENAL_DECISIONS_RESOLVED=8

## State transition

UNRESOLVED_SEARCHES=177->169
PENDING_ARSENAL_DECISIONS=196->188
SEARCH_QUEUE_TASKS=23->22
NEXT_READY=SR-STR-041,SR-STR-042,SR-STR-043,SR-STR-044,SR-STR-045,SR-STR-046,SR-STR-047,SR-STR-048

## Firewalls

Search absence is not novelty. Selberg--Delange uniformity is receiver-specific. Raw representation weight is not primitive-object multiplicity. A lower subfamily is not a full asymptotic. Face primitivity is not cuboid primitivity. Stage14 population and cutoff remain fixed. No perfect-cuboid existence/nonexistence claim is introduced.
