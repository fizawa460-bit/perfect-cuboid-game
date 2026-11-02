MB104 Route F62 / RESEARCH / 2026-10-28 JST

Main proof: MB104-F62-20261028.md.
Read-only finite verification (Python standard library):
  python3 verify_f62.py
Also replay the complete frozen F61 input (needs g++ / C++17):
  python3 verify_f62.py --replay-f61

F62-norm-slices97.json stores four degree-112 norm polynomials, their
leading coefficients, and two full Bezout identities. The verifier rebuilds
them from the pinned F61 modular vectors and separately multiplies the four
biquadratic conjugates. Both directions and full-degree preservation matter.

F62 does not infer characteristic-zero existence from finite-field gcds
alone: the proof uses the F61 unit-minor lifts, two specialized resultants,
and the degree bounds. Absence of fixed curves plus 572>17 gives a
2-dimensional image for the FULL linear system. Jouanolou irreducibility
and characteristic-zero Bertini are applied to that full system and its
product-generated series W_m, not merely to the F,G pencil. Reducible products
only certify nonemptiness of the desired local open conditions.

This proves conditional existence of integral fixed-model curves for every
m with 14 ordinary 16m-branch supports and avoidance of the other 34 A1 nodes.
It does not prove genus one, residual quadratic norm splitting, marked
conductors, or the original source-to-actual-carrier adapter. The quartic
elimination norm here is distinct from the residual quadratic norm gate.
Strict arithmetic genus is 672m^2+112m+1; genus one requires delta 672m^2+112m.

The seven negative tests include changed norm and Bezout coefficients with
updated checksums, missing slices, false claims, altered prior bytes and a
missing certificate. Inputs were preserved.

F62-REFERENCES.json contains primary theorem locations.
Source exports are normalized readable text, not historical Git blobs.
discovery/ contains an unused bounded finite-field point scan; the F62 proof
does not depend on that scan. F61 is a conditional, independently unaudited
input. F62 is independently unaudited research. Candidate exclusion 0;
MB104 OPEN; all official credit 0; GitHub/STATE/A-E unchanged.
