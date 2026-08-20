# Stage27-19-r8c — thick moving-family exponent ledger

```text
TASK_ID=Stage27-19-r8c
PARENT_ROUTE=Stage27-19-r8b
ROUTE_KIND=LOWER_THICK_FAMILY_RECEIVER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The alternative to lowering one-parameter physical height is to keep degree eight but increase the effective number of independent source parameters.

Let a physical family have source-count exponent `rho`, meaning that after primitive/canonical restrictions and bounded-to-subpower multiplicity it supplies

\[
T^{\rho+o(1)}
\]

distinct physical objects for source height `T`, while physical size satisfies

\[
B\asymp T^h.
\]

Then the lower exponent supplied by the family is

\[
\boxed{\lambda=\rho/h}.
\]

The audited R501/R502 families have `(rho,h)=(2,8)` and hence `lambda=1/4`.

Therefore a degree-eight family beats one quarter exactly when

\[
\boxed{\rho>2}.
\]

For a genuine two-rational-parameter construction with four primitive homogeneous source coordinates, the ambient source count can be `T^{4+o(1)}` before equations and identifications. Even one independent algebraic relation can leave a source exponent near three in favorable circumstances, which would give the aspirational scale `3/8`. This is only a dimension/counting receiver: the Stage19 physical equation, exactly-two filter, primitive normalization, and finite-to-subpower multiplicity must all be proved on the same family.

The practical lower search therefore has two nonduplicate targets:

- **L1:** one-parameter curve with `h_alg<=7` via low degree or polynomial cross-cancellation;
- **L2:** moving family with `rho>2` and controlled physical height, ideally `h<=8`.

This clarifies that blindly searching higher-degree one-parameter curves is not the only lower route. A surface/rational multisection family with sufficiently many physical rational points can beat the known quarter family even without lowering degree eight.

```text
GENERAL_LOWER_EXPONENT_LEDGER=lambda=rho/h
KNOWN_QUARTER_CALIBRATION=rho2_h8
DEGREE8_PROGRESS_GATE=rho>2
THICK_FAMILY_RECEIVER_MATERIALIZED=true
ASPIRATIONAL_RHO3_H8_EXPONENT=3/8
THICK_PHYSICAL_FAMILY_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r8d
```
