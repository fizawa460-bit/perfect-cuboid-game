MB104-F65 / 2026-10-29 JST

Read MB104-F65-20261029.md for the geometric proof and scope.
Python 3 standard library only:
  python3 verify_f65.py
  python3 -O verify_f65.py
  python3 verify_f65.py --replay-f64
  python3 negative_tests.py

The default verifier is read-only. It pins the frozen F64 archive, checks four formal-neighborhood unit evaluations, the null-configuration quotient intersection matrix, degree inequalities for all k>=1, thickening Euler recurrences, and exact polynomial identities for all m>=1. The optional prior replay runs F64 in normal and optimized modes. The negative runner rejects ten cases in both modes and preserves inputs.

Formal-neighborhood triviality, H1 vanishing on thickenings, KV, norm generic degree and equigeneric deformation results are geometric deductions in the note. Numeric verification is not a machine proof or independent mathematical audit.

New exact model conclusions: h1_X(mP)=4, h1_Y(mM)=6; h0_X=168m^2-56m+12, h0_Y=336m^2-112m+18; the balanced norm image has codimension336m^2-6. Conditional F37 gluing rank is504m^2+56m-12 (m1=548). For a hypothetical nodal genus-one half-curve the smoothing cokernel is224m-17 (m1=207). C isolation is reused, not new credit. These ranks live in different spaces and are not added as independent exclusions.

Actual source-fixed C/R_off and local conductor data are absent. Genus-one existence/nonexistence and coreless/no-clump remain unproved; exclusions0, no uniform degree bound, MB104 OPEN, all official credits0. The concurrent F64 audit conditional PASS and20 independent negative checks are preserved. F65 is new unaudited research. A-E/STATE/GitHub/raw manifest are unchanged. User preference: save to Google Drive, brief reports, no report links.

