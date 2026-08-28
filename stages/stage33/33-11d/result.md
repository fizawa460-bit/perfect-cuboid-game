# Stage33-11d carrier-prime refinement: MAIN-complete handoff

Status: **MAIN_COMPLETE_PENDING_AUDIT**. The 33-11d MAIN exit condition is satisfied, but this is not a fresh audit and does not close Stage33-11 or promote connecting columns.

The only mathematical input is the frozen PR #1449 run-92 handoff (`33213248650`, head `532d6047...`). Its 30 normalized carriers and certified `cc`, `swap12`, and `swap13` orbit partition are compactly retained in `stage33-11d-source-lock.json`. PR #1449 is not modified or replayed.

## Exact result

All eight formerly unresolved geometric representatives now have actual height-one-prime refinements over `Q(i)`.

Five split or nonreduced sections are certified by exact primary-ideal intersection:

- `a2+a3+b1=0`: eight reduced height-one primes, multiplicity 1;
- `a2-a3-b1=0`: eight reduced height-one primes, multiplicity 1;
- `a1=0`: eight reduced height-one primes, multiplicity 1;
- `a1+b3=0`: four reduced height-one primes, each scheme multiplicity 2;
- `b3+c=0`: four reduced height-one primes, each scheme multiplicity 2.

For these five cases, the verifier checks the full section ideal `(Q1,Q2,Q3,Q4,l)` against the intersection of the recorded primary ideals using exact Groebner bases. Each reduced component is prime because triangular linear elimination leaves a rank-three homogeneous conic. Reduced support and scheme multiplicity are separate certificate fields.

The remaining three sections are each a single reduced height-one prime:

- `b1-b3+c=0`;
- `b2-i*b3-c=0`;
- `b1+b3-c=0`.

For each of these three cases, the verifier proves `(I:b3^infinity)=I`, computes the exact `b3=1` chart as a four-step multiquadratic presentation over `Q(i)(t)`, factors every radicand over `Q(i)`, and obtains finite-prime valuation-matrix rank 4 over `F2`. Thus the four squareclasses are independent, the multiquadratic fraction-field degree is 16, the chart is a domain, and saturation lifts primeness to the whole homogeneous section.

Certified orbit transport now covers all 24 carriers that were unresolved in #1449. Together with the six direct refinements inherited from the frozen handoff, actual height-one-prime refinement coverage is `30/30`, with unresolved representatives and original carriers both zero.

## Audit and promotion boundary

- 33-11d MAIN exit condition: satisfied.
- 33-11d fresh audit: not yet performed.
- Stage33-11 exact connecting progress: still `0/26`.
- Exact connecting columns promoted here: 0.
- Next logical continuation remains 33-11e prime-level Galois transport, after a stable 33-11d handoff/audit decision.
- Stage33-11 exact closure, Stage33-12 release, Stage33-08 release, Stage33-07 closure, theorem credit, and endpoint credit all remain false.

## Actions preflight

- Verification is one lightweight exact local-algebra job; planned effective heavy concurrency is 0.
- The workflow uploads no artifact, so projected new Actions artifact storage is 0 bytes against the 500 MB operating budget.
- PR-opened events are cold. A synchronize event runs verification only when the dedicated run key advances semantically with its fixed source locks intact.
