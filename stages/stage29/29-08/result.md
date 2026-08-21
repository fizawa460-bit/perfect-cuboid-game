# Stage29-08 — parametrization, fibration and coverage atlas

```text
STAGE=Stage29
ITEM=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Main result

29-08 now separates three questions that had been conflated in earlier screens:

```text
A. exact coordinate crosswalk to the audited endpoint hub
B. geometric/fibration location of a family
C. global arithmetic coverage of all endpoint candidates
```

A route may pass A and B while failing or leaving C open.

## 2. Peschmann exact crosswalk closes the independence question

For the Euclid triples

```text
(U1,V1,W1)=(a^2-b^2,2ab,a^2+b^2)
(U2,V2,W2)=(m^2-n^2,2mn,m^2+n^2)
```

Peschmann uses

```text
e=U1U2, x=V1U2, y=U1V2.
```

The two automatic faces are exactly the Stage29-07 two-face model. With

```text
t1=x/e=V1/U1,
t2=y/e=V2/U2,
```

one has identically

```text
Master/e^2  = t1^2+t2^2       = f_face
H-total/e^2 = 1+t1^2+t2^2     = f_sp.
```

Therefore Peschmann's two residual square conditions are literally the same two roots of the audited joint V4 cover.

Proposed disposition:

```text
R29-PESCH1=DISCHARGED
PESCHMANN_PROVEN_F2_ADAPTER=true
PESCHMANN_INDEPENDENCE_RESOLVED=true
PESCHMANN_INDEPENDENT_FOUNDATION=false
PESCHMANN_ROUTE=J12-PARAMETRIC
H_NAMESPACE_REOPEN_REQUIRED_BY_PESCHMANN=false
```

This does not make Peschmann redundant: the genus-3 and elliptic quotient/fibration machinery supplies a strong chart and attack language on the existing joint-V4 architecture.

## 3. Coverage is still not certified

The current 2026 Peschmann source sequence is not internally safe to compress into a global coverage theorem without reconciliation.

- `arXiv:2604.28072` states in its abstract that every primitive Euler brick arises from the standard `(a,b,m,n)` parametrization up to scaling.
- the later `arXiv:2605.00573` explicitly says it does not claim the converse that every primitive body cuboid arises from a Master-Hit.

Stage29 therefore does not choose the stronger statement by convenience.

```text
PESCHMANN_GLOBAL_EULER_BRICK_COVERAGE_CERTIFIED=false
R29-PESCH-COV=OPEN_SOURCE_SCOPE_RECONCILIATION_AND_GLOBAL_COVERAGE_ADAPTER
```

The finite 1,072-fiber theorem and million-brick computations remain finite-family results only.

## 4. New May-2026 Peschmann fibration imported without creating a new foundation

`arXiv:2605.00573` gives an elliptic fibration of the Master-Hit equation over `(m,n)`:

```text
H_mn: s^2=V2^2*t^4+(4U2^2-2V2^2)*t^2+V2^2,
```

plus a Weierstrass curve `E_mn` and a rational square-value test `tau(P)=t^2`.

Since `H_mn` is exactly the Master/third-face equation under the crosswalk above, this fibration lies on the Stage20 Euler K3 marginal. It is routed under the existing `J12-PARAMETRIC` attack route.

```text
R29-PESCH2=OPEN_BOUNDED_FIBRATION_CLASS_AND_POLARIZATION_MATCH
```

The same paper's exponent-one blocker remains conjectural despite large finite verification:

```text
R29-PESCH-E1=AMBER_CONJECTURAL
FINITE_VERIFICATION_IS_NOT_THEOREM=true
```

## 5. Stage20 / Testa--Stoll Euler K3 bridge sharpens

After the exact 29-07 sign tower, quotienting the full endpoint by the space-diagonal sign leaves

```text
[e:x:y:p:q:z] in P5
```

with exactly the three face equations. This is both:

- the Testa--Stoll Euler K3 normal quotient `Kbar_c`, and
- the Stage20 third-face completion of the two-face host.

The minimal resolutions therefore agree as the same Euler K3 model, and

```text
M_face=pi_face^*(-K_Y)
```

is the pullback of the `P5` hyperplane class under the six physical sections.

Proposed disposition:

```text
R29-K1=DISCHARGED_PENDING_AUDIT
```

This is an equation-level bridge, not an inference from matching `h32`.

The 15 published elliptic fibrations on the Euler K3 are therefore legitimate Stage20 marginal fibration candidates, but their fiber classes and residual space-square arithmetic remain open:

```text
R29-FIB1=OPEN
R29-FIB2=OPEN
```

## 6. Atlas classification

The machine-readable atlas `coverage-atlas.json` records at least:

```text
Peschmann Euclid-pair chart        -> exact two-face/joint-V4 chart; coverage open
Peschmann genus-3 family           -> necessary curve-level slices; converse specialization guarded
Peschmann MW elliptic fibration    -> Stage20 Euler marginal
Peschmann 1072-fiber theorem       -> finite fibers only
Peschmann exponent-one blocker     -> conjectural, finite verified
Saunderson                         -> thin Stage20 curve; endpoint lift genus 3 / degree 12
StageA2 -18                        -> one family only
Testa-Stoll degree<=6 curves       -> complete low-degree curve classification, not point coverage
28 endpoint genus-5 fibrations     -> geometric full-surface fibration atlas
15 Euler-K3 elliptic fibrations    -> marginal K3 atlas, endpoint residual square still required
```

## 7. Coverage hierarchy frozen for downstream work

29-12 must distinguish:

```text
GLOBAL_ENDPOINT_COVERAGE
GLOBAL_MARGINAL_COVERAGE
GEOMETRIC_FIBRATION_COVERAGE
PARAMETRIC_CHART_COVERAGE
THIN_FAMILY_ONLY
FINITE_FIBER_ONLY
EMPIRICAL_DATABASE_ONLY
```

Only the first category can support a direct endpoint-wide conclusion without a separate coverage theorem.

## 8. Route ownership / roadmap

No twelfth attack route is created. New Peschmann receivers are owned by `J12-PARAMETRIC`.

Proposed receiver updates:

```text
R29-PESCH1=DISCHARGED
R29-PESCH-COV=OPEN -> J12-PARAMETRIC
R29-PESCH2=OPEN_BOUNDED -> J12-PARAMETRIC
R29-PESCH-E1=AMBER_CONJECTURAL -> J12-PARAMETRIC
R29-K1=DISCHARGED_PENDING_AUDIT
R29-FIB1=OPEN -> J12-PARAMETRIC
R29-FIB2=OPEN -> J12-PARAMETRIC
```

No Stage16--28 backflow is required.

```text
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
