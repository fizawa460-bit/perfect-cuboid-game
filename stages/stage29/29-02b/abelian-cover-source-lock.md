# Stage29-02b — abelian-cover source lock

The canonical-class calculation uses the standard ramification/Hurwitz formula for normal abelian covers.

Primary reference:

- Rita Pardini, `Abelian covers of algebraic varieties`, Journal für die reine und angewandte Mathematik 417 (1991), 191--214, DOI `10.1515/crll.1991.417.191`.

For a finite abelian cover with ramification index two along the reduced branch components, the canonical divisor is obtained from

```text
K_X = pi^*(K_Y + 1/2 D_total)
```

in the present `V4` situation, equivalently by applying Hurwitz to the two independent quadratic ramification divisors.

Stage29-02b uses this only for divisor-class/intersection preflight.  The exact singularities of the concrete toric model are audited separately before promoting minimal-resolution invariants.

```text
CANONICAL_FORMULA_SOURCE_LOCKED=true
SINGULARITY_AUDIT_REPLACED_BY_FORMULA=false
```
