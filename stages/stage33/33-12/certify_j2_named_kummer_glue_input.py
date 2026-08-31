#!/usr/bin/env python3
"""TOMBSTONE: revoked historical J2 Kummer-glue producer.

The historical implementation consumed j2_arithmetic_descent.py and promoted
its old Q-defined ell_J2 as a nonzero named J2 witness.  Hostile replay proved
that geometric CV class is zero, so this producer must never create current
Kummer/HS credit again.

Current corrected input:
  stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json

That corrected certificate materializes only normalization/full-L
representative-level descent data.  The surface H^2(mu_2) lift, Pic/2 defect,
integral Pic lift, and Hochschild--Serre d2 remain OPEN.
"""
raise SystemExit(
    "SUPERSEDED_REVOKED_OLD_ELL_J2: use corrected pre-Kummer descent cochain; "
    "surface mu2/Pic/HS-d2 adapter remains open"
)
