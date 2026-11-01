MB104-F63 / 2026-10-29 JST

Read MB104-F63-20261029.md for the geometric proof and scope.
Replay with Python 3 standard library only:
  python3 verify_f63.py
  python3 -O verify_f63.py
  python3 negative_tests.py

The default replay is read-only with temporary matrix rebuilds. It checks complete dependency coverage, exact relations, nonzero minors, both local witnesses, excluded nodes including infinity, norm slices and Bezout identities, and half-section identities. All executable checks remain enabled under -O. The negative runner uses temporary copies, rejects 10 cases in both modes, and preserves inputs.

The original finite witnesses came from fixed 32-trial samples using mt19937 seed 610028 in the even and odd kernels, with trial indices 4 and 6 selected. Discovery is not trusted evidence; the delivered verifier checks the selected vectors directly.

All-m integral split-norm existence is a conditional geometric deduction using Bertini and the unit-minor lift; the numerical replay is not a machine proof or independent mathematical audit. Normalization genus one, actual marked conductor, coreless/no-clump and the original source adapter remain unproved. Candidate exclusions 0, MB104 OPEN, all official credits 0.

The concurrent 2026-10-29 F61/F62 audit delta is preserved. A-E, STATE, GitHub, official credits and raw DRIVE-WORK-HANDOFF.json were not modified.

