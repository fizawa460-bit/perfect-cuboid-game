MB104 Route F61 / RESEARCH / 2026-10-28 JST

The main proof is MB104-F61-20261028.md.
This is new fixed-model research, not the F43-F56 audit.
F35 + F57-F60 conditional audit PASS is the inherited input boundary.

Full read-only replay:
  python3 verify_f61.py
Requires Python 3 standard library and g++ with C++17.
It rebuilds the matrix in a temporary directory, verifies the 4 exact Q(i)
relations, two modular determinant minors, both witness vectors, tangent
forms and all 34 excluded A1 nodes. It never edits the certificate.

F61-certificate.json: formal claim scope + frozen input/source hashes.
F61-exact-relations.json: 4 independent exact Gaussian-integer row relations.
witness97.json: unchanged MODULAR discovery record. Its
NOT_YET_ESTABLISHED characteristic-zero flag describes that record alone;
the F61 proof combines it with exact rank 892 and unit-minor lifting.
rank97.txt: selected original row and column indices for the two minors.
F61-excluded-nodes97.json: finite and infinity-node evaluation certificates.
F61-negative-tests.json: 7 rejected corrupt/missing inputs, including witness
and relation changes whose checksums were updated to reach algebra checks.

The exact characteristic-zero lifts are specified by solving the selected
unit minor after lifting free coordinates. Their enormous coefficient
expansions are not needed and were not computed. CRT is discovery only.
Optional discovery source files are included, but are not called by replay.

Source snapshots are readable native exports with BOM removed and CRLF
normalized to LF. Their hashes are normalized local-text hashes, not Git
blob IDs. Source-to-actual-carrier correspondence remains HOLD.

The all-m product construction is reducible for m>1; global reducedness,
irreducibility, genus one, norm splitting and marked conductors are unproved.
Candidate exclusions 0; MB104 OPEN; credit 0; F61 independent audit pending.
