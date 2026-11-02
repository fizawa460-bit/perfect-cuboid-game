MB104-F64 / 2026-10-29 JST

Read MB104-F64-20261029.md for the geometric proof and limitations.
Python 3 standard library only:
  python3 verify_f64.py
  python3 -O verify_f64.py
  python3 verify_f64.py --replay-f63
  python3 negative_tests.py

Default verification is read-only. It pins the nested original F63 package, checks the four omitted-node values, the 108-dimensional canonical subsystem (24192 jet identities), four canonical charts, divisor intersections, the two-point cubic 22-by-22 jet matrix, and genus/node formulas. The optional prior replay checks the complete F63 verifier in normal and optimized modes. The negative runner rejects 10 cases in both modes using temporary copies and preserves inputs.

Basepoint freedom, the canonical embedding, Bertini, the incidence dimension argument and all-m generic nodality/genus are geometric deductions in the note. The numerical checks do not constitute a formal machine proof or an independent audit.

Generic normalization genus is 336*m^2+112*m+1 and generic strict off-support nodes are 336*m^2. Genus one requires special singular half-curves with delta 336*m^2+112*m; their existence or nonexistence is not proved. Actual marked conductor, coreless/no-clump and the original source adapter remain unproved. Candidate exclusions 0, MB104 OPEN, all official credits 0.

The concurrent F63 audit is preserved: model math conditional PASS, only 4 audit-side negative checks independently sampled. F64 is new unaudited research. A-E, STATE, GitHub, credits and raw DRIVE-WORK-HANDOFF.json were not modified.

