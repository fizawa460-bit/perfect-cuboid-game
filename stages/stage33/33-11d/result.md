# Stage33-11d carrier-prime refinement: first exact leaf

Status: **OPEN_UNRESOLVED**. This is MAIN implementation evidence, not hostile-audit closure.

The only input is the frozen PR #1449 run-92 handoff (`33213248650`, head `532d6047...`). Its 30 normalized carriers and certified `cc`, `swap12`, and `swap13` orbit partition are compactly retained in `stage33-11d-source-lock.json`. PR #1449 is not modified or replayed.

## First exact result

Five of the eight unresolved geometric representatives now have exact scheme-theoretic primary decompositions over `Q(i)`:

- `a2+a3+b1=0`: eight reduced height-one primes, multiplicity 1;
- `a2-a3-b1=0`: eight reduced height-one primes, multiplicity 1;
- `a1=0`: eight reduced height-one primes, multiplicity 1;
- `a1+b3=0`: four reduced height-one primes, each scheme multiplicity 2;
- `b3+c=0`: four reduced height-one primes, each scheme multiplicity 2.

For every case, the verifier checks the full section ideal `(Q1,Q2,Q3,Q4,l)` against the intersection of the recorded primary ideals using exact Groebner bases. Each reduced component is prime because triangular linear elimination leaves a rank-three homogeneous conic; its affine cone has dimension 2, hence its projectivization is a curve and the prime has height one in the surface. Reduced support and scheme multiplicity are separate certificate fields.

Certified orbit transport covers 13 of the 24 formerly unresolved original carriers. Together with the six direct refinements inherited from the frozen handoff, all 30 carriers are disjointly accounted for, but 11 original carriers remain unresolved.

## Explicit remaining set

The remaining primary-decomposition debt is exactly three geometric representatives:

- `08ff6ec1...`: `b1-b3+c=0` (3 original carriers);
- `3391419a...`: `b2-i*b3-c=0` (6 original carriers);
- `0b6cf3ce...`: `b1+b3-c=0` (2 original carriers).

No irreducibility or primary decomposition is inferred from a working convention for these representatives. Therefore 33-11d does not close.

## Firewalls and Actions preflight

- Stage33-11 exact connecting progress remains `0/26`; prime refinement alone promotes no connecting column.
- Stage33-11 exact closure, Stage33-12 release, Stage33-08 release, Stage33-07 closure, theorem credit, and endpoint credit all remain false.
- Verification is one lightweight exact local-algebra job; planned effective heavy concurrency is 0.
- The workflow uploads no artifact, so projected new Actions artifact storage is 0 bytes against the 500 MB operating budget.
- PR-opened events are cold. A synchronize event runs verification only when the dedicated run key advances semantically with its fixed source locks intact.
