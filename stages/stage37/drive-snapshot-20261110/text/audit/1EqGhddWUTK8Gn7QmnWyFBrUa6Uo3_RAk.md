# TI-004 scoped adversarial audit — PASS

2026-09-30. Within-session audit, not external peer review.

PASS: L1 excludes only nonresidue d at odd VW primes. PASS: L2 uses anisotropy at U primes3mod4 and distinct odd valuations, not reduction modq alone. PASS: L3 applies only U primes1mod4; extending it to3mod4 would be wrong. PASS: dual free sign counted separately; denominator4 in rank formula retained. Nonzero sf(VW) kernel vector makes delta_dual nonnegative. delta>0 is an upper-bound defect, never positive rank certification.
PASS: K_char closure requires G_tor; X_tor not discarded. No infinitude/density claimed. PASS: unique Master inverse uses coprime face gcds; primitive reconstruction and K divisibility checked. Same physical R symbol retained explicitly; no numerical weight was evaluated. Diagonal impossible for nondegenerate Euler bricks; symmetrized pair weight is1/2, total per brick1. No multiplicity or independent-source credit.

Independent replay: ti004_audit.py PASS,28 full primitive-pair cover checks, exhaustive binary kernels for both fixtures, independent edge enumeration maxedge<=300 returning two primitive bricks and distinct inverse pairs. This finite verification supplements, not proves, the universal lemmas. Files: card; ti004_legendre.py; ti004_examples.json; ti004_audit.py; ti004_audit.json.

OPEN: prove K_char infinite / density if needed; evaluate exact physical defect and exceptional marginal weights; show either o(M3). Existing1072-worker inconsistency unexamined and HOLD. Main gate and all asymptotic/nonexistence flags stay false.
