# Stage35EX R3-07 row364

The new result is an exact all-place fake Jacobian Selmer intersection of
dimension 8 and, by the report's explicit genuine-lifting argument using the
rational infinity difference, genuine 2-Selmer dimension exactly 9.
The quotient by the seven known rational Kummer classes has dimension 2.

MW rank remains 7..9. The CT entry is NOT computed. The whole-MW 163-adic
upper space U, whole-MW a0 unit, and original-source exclusion are NOT proved.
New row364 independent mathematical audit is PENDING. A separately received
scoped PASS for parent row363 is retained under record_updates.

## Reproduce the new exact arithmetic

```bash
python -m pip install -r requirements.txt
python math/verify_exact_selmer9.py
python -O math/verify_exact_selmer9.py
python record_updates/verify_writeback.py
python verify_manifest.py
```

New local arithmetic has 541 successful checks and 7 negative controls in
both normal and optimized modes. Writeback readback has 64 checks.
The mathematical report supplies the cohomology, good-reduction and
Cassels-Tate arguments; these general theorems are not machine proved by
the finite arithmetic checks.

The parent_evidence ZIPs are unchanged received files. Follow their own
requirements for full parent replay. Their audit fields are historical
snapshots; use the separately retained current audit receipt for row363.

exploratory contains only bounded searches, not global completeness
certificates. No extra independent rational MW direction was found.
