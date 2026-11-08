# Stage35EX-C R3 independent Hcs rank-one arithmetic audit — R0 handoff


Integrated baseline verified at start: C35-117, R0 receipt COMPLETE.
Mathematical status: NEW INDEPENDENT AUDIT CERTIFICATE and NEW combined fixed-X four-point classification **candidate for R0 review**. Prior C35-104 arithmetic rank-one claim and prior C35-117 p3 logarithm are old and receive no theorem/novelty recredit. No formal authority mutation.


## Reproduce


Requires Python 3 with `sympy`; no Magma, Sage, PARI or network needed.


1. From this folder: `python r3_c118_independent_sel2_audit.py > fresh_selmer_stdout.txt`
2. Compare produced `r3_c118_independent_sel2_evidence.json` byte-for-byte against the bundled version (copy the bundled original elsewhere first), or inspect full JSON equality.
3. From this folder: `python r3_c117_p3_logdifference_verify.py > fresh_p3_log_replay.json`. The prior fixed 44D source is bundled at `p3prev/r3_c116_hcs_p3_zero_disk_evidence.json`.
4. Compare `fresh_p3_log_replay.json` to `r3_c118_imported_p3_log_replay.json` by semantic JSON equality. Read SHA256 manifest for original source identity.
5. Review the full proof and its dependency firewalls before interpreting the fixed-X theorem.


## Exact expected results


- p11 genuine local Kummer image 8 elements; p37 genuine image 8 elements; every component valuation even.
- S-unit supported dimension 10; p5 128 candidates, real 256, intersection 32, with p2 only 8.
- Eight masks 0,81,150,199,269,348,411,458; rational witnesses T0,TA,D' masks 81,150,269; no nonzero kernel over simultaneous real/p5/p2 localization.
- 2-adic mod16 alternative unit-square check passes 66/45 pair tests.
- Original p3 accepted scalar `log(44D)(omega2-omega1)/3 = 1 mod3` reproduced with `s = 65 mod81`.
- Section334 remains R0-owned; Branch A paused, Branch B open, Stage35 open, E1 unproven.


## Distinguish proof and certification


This package independently recomputes finite arithmetic, provides a conventional written proof invoking standard classical theorems, and proposes unconditional rank-one and fixed-X statements **for formal R0 audit**. It does not claim proof-assistant verification, worldwide novelty, external hostile certification, full original physical source, infinite-index coverage, four TRUE GOOD/H pool upper, or owner-state promotion.