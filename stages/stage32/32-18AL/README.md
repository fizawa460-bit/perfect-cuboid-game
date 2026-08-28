# Stage32-18AL — p436/s5 one-wall arsenal

18AK full-matrix result: 0/6 walls closed. All 18 jobs (pairwise-cached, cap-sym-active, combined-active × six walls) hit the 18M node cap. Summary: run 33129048322, artifact 9671012196, digest sha256:8db2b1bf496e9bf910bba2844a1d573b539c6c7c662a394ec19191167b07f345.

18AL concentrates compute on one wall: p436/s5. The objective is not to rank unfinished algorithms by speed; it is to break one wall with an exact COMPLETE certificate.

The new family is lower48 exact integer unimodular basis reduction. Coordinates 48..62 remain untouched, preserving both frozen x1024 shard hashes. q, cap rows and symmetry rows are transformed together, so each shear is a determinant-one Z^48 change of variables and the represented lattice problem is preserved exactly.

Seven non-identical weapon configurations hit the same wall in parallel:
- basis-forward
- basis-reverse
- basis-alternating2
- basis-forward + pairwise-cached
- basis-forward + cap-sym-active
- basis-alternating2 + pairwise-cached
- basis-alternating2 + cap-sym-active

Each gets 18M nodes and 60 minutes. max-parallel is 15. COMPLETE is the only success criterion. Existing exact failures are recorded in weapon-history.md and are not silently renamed and rerun. No finer split is authorized; all global/theorem/receiver/controller firewalls remain false.
