# Stage32-18AL — lower48 unimodular basis matrix

18AK full-matrix result: 0/6 walls closed. All 18 jobs (pairwise-cached, cap-sym-active, combined-active × six walls) hit the 18M node cap. Summary: run 33129048322, artifact 9671012196, digest sha256:8db2b1bf496e9bf910bba2844a1d573b539c6c7c662a394ec19191167b07f345.

18AL changes algorithm family. It does not add another local 2x2 pruning rule. Instead it applies exact integer unimodular basis shears only inside coordinates 0..47 before constructing the enumerator. Coordinates 48..62 are untouched, so the frozen x1024 primary/secondary shard identity remains unchanged.

Three basis weapons are run on every remaining wall:
- forward-greedy: one lower-triangular greedy size-reduction sweep;
- reverse-greedy: one upper-triangular greedy size-reduction sweep;
- alternating2: two forward+reverse sweeps.

Each elementary shear is an integer determinant-one coordinate change, and q / cap rows / symmetry rows are transformed together. Therefore Z^48 is preserved bijectively. The search tree and LDL geometry change, but the exact represented lattice problem does not.

All six walls receive all three weapons: 18 jobs, max-parallel 15, 18M node cap, 60-minute certifier wallclock. A wall counts closed only on exact COMPLETE. No unfinished runtime winner is selected. No finer split is authorized. All global/theorem/receiver/controller firewalls remain false.
