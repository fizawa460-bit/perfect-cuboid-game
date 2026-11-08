# row365 evidence: fixed signed ±18 C2 only

Read `REPORT.md` for mathematical definitions, proofs, scope, and unresolved
condition. New independent mathematical audit is PENDING. The latest accepted
parent audit is row364 PASS_SCOPED.

## Files

- `math/torsion_frame_P512.json`: frozen 512-bit maximal-order projectors,
  labeled branch factors, interpolation, all nine divisor-reduction stages,
  endpoint, and the two NEW torsion squareclasses.
- `math/compute_torsion_frame.py`: generation using cypari2/PARI and exact
  integral maximal-order multiplication. It does not prove the general theory.
- `math/verify_dyadic_frame.py`: no PARI. Integer/rational polynomial identities,
  independent coefficient error balls, inherited unit-squareclass routine,
  GF(2) frames and exact integer determinants, seven negative controls.
- `math/dyadic_transversality_certificate.json`: columns, minors, local words,
  independent precision bounds, and scoped conclusions requiring report proofs.
- `math/parents/`: exact unchanged parent mathematical inputs.
- `parent_evidence/ROW364_ORIGINAL_EVIDENCE.zip`: unchanged parent evidence.
- `record_updates/`: guarded canonical updates and readback evidence.
- `SHA256SUMS`: every regular packaged file except itself; no bytecode files.

## Replay

Dependencies: Python 3.12, python-flint 0.9.0 and numpy 2.5.4 for verification;
cypari2 2.2.4 additionally for generation. Install into a separate environment
if necessary. The existing workspace uses PYTHONPATH=work/deps.

From the extracted evidence directory:

```bash
python3 math/verify_dyadic_frame.py
python3 -O math/verify_dyadic_frame.py
python3 math/compute_torsion_frame.py --precision 512 --root-index 0 --output-dir replay
```

The verifier uses explicit exceptions, not Python `assert`. Normal and optimized
execution check the same 2848 arithmetic statements, seven negative controls,
and comparison with the frozen certificate. Parent arithmetic and parent
theorems are reused, not credited again.

The full generated JSON equals `torsion_frame_P512.json` except for elapsed
seconds. `--root-index 0` is the normative branch label. Other branch labels
require a changed unit normalization and are not part of this command.

`--build` on the verifier only recreates its deterministic certificate; do not
use it as a substitute for checking the existing frozen certificate.

The certificate does NOT claim a computed Cassels–Tate entry, a whole-MW
p163 upper space, rank7, new rational MW classes, or original-source exclusion.
