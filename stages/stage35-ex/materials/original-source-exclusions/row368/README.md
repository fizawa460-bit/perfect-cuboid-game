# Stage35EX R3-07 row368 evidence

The proof and finite-arithmetic replay concern the original indexed LOW source.
The Ward and C118 inputs are identified in the proof. The Ward congruences,
support tables, and rank-3 auxiliary curve counts are exact. Independent audit
of row368 is pending.

Run with Python 3.10+ and SymPy. The author run used SymPy 1.14.0.

    python3 verify_row368.py

This regenerates row368_exact.json. The 288 entries include both signed
indices and both labels for the 72 nominal absolute indices. The old
A-even-only masks are credited before row368. The point counts and field
congruences are complete finite checks. The proof gives the global deductions.
P112_SOURCE_EVIDENCE.json is the original P112 data reproduced for the named
baseline comparison.
