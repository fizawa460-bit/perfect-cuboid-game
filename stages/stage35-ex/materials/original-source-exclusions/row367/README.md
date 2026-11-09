# row367: fixed signed ±18 original-source obstruction

Read REPORT.md for the mathematical proof. New result: INTERNAL EXACT PROOF,
independent mathematical audit PENDING. Parents row365/366 retain their PASS.
LOW and Branch B remain OPEN. The new exclusion treats absolute index18 and
both signed indices only, with the inherited original source adapter.

## Normative evidence

- math/q8_P256.json: actual positive-chart 8-division, 256-bit Hensel root.
- math/q4_P32.json: explicit formal4-division; true beta4=0 follows from8-division.
- math/sixteenth_P256.json: maximal-order square root, complete RR linear system,
  exact solution, dyadic inverse witness, 147-bit coefficient ball, coprimality,
  actual16-half polynomial, unit2F(theta)/u^60 and its squareclass.
- math/source_obstruction_certificate.json: rank12 minor(det3), scalar-safe
  separating functional0x1405c23, precise scope and unproved claims.
- math/verify_source_obstruction.py: no PARI; independent full formal-log check,
  integer RR equations, inverse and coefficient balls, norm constraints,
  inherited local unit-character map and all-torsion separation.
- parent_evidence/: unchanged parent evidence and proof/audit snapshots.
- record_updates/: canonical guarded changes and readback evidence.
- SHA256SUMS: all packaged regular files except itself; bytecode excluded.

## Verify

Requires Python3.12, python-flint0.9.0, numpy2.5.4. From extracted evidence:

```bash
python3 math/verify_source_obstruction.py
python3 -O math/verify_source_obstruction.py
```

The proof of full Kummer zero explicitly keeps the norm sign. A fake zero alone
would not discard Dinf. General descent/RR/Neron/log arguments are mathematical
proofs in REPORT.md, not claims that finite tests mechanically prove them.

## Recompute

```bash
python3 math/formal_jacobi.py --precision 256 --output-dir replay
python3 math/compute_sixteenth.py --q8 replay/q8_P256.json --output-dir replay
```

Formal generation uses integral AS coefficient recurrence and scalar Newton
sums. Verification uses polynomial inverse-square-root Newton and traces of
companion-matrix powers, so it does not repeat that implementation.
Generation may take a few minutes. Compare arithmetic fields; elapsed seconds
in the RR file are not mathematical input. Keep replay separate from frozen data.

The original row366 script snapshot has its historical /mnt/data dependency
and is retained as source evidence; it is not claimed to be the new verifier.

This report does NOT claim rank7, CT computation, construction of whole-MW U,
the full q-inclusion for every X in16Z2, n4<=5, allLOW completion, or BranchB closure.
