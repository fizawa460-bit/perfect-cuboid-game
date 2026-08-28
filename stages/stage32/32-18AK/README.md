# Stage32-18AK — b16 active-set / cached-pairwise scout

18AJ reran the clean 18AF baseline at 18M nodes on all six remaining x1024 walls and closed 0/6. Its summary is run 33126100211, artifact 9669160823, digest sha256:0a3220d47503dfc12be9f18a31095120f62489b4dd957d94dc529c0e8e47084d.

18AK does not repeat full production. It races three exact-search viewpoints on representatives (436,5) and (922,13):

- baseline: 18AF scheduler 1.0 control;
- pairwise-cached: deep-only exact symmetry/symmetry 2x2 Gram/KKT with lazy exact cross-Gram cache;
- cap-sym-active: deep-only exact 2x2 active-set propagation coupling a violated cap face with a violated symmetry breaker.

All actual rejection tests are exact rational inequalities. Floating arithmetic only schedules exact tests. x1024 shard identity is unchanged; coordinates 48–62 and both split hashes are untouched. Each scout gets 6M nodes / 15 minutes. Matrix max-parallel is 6. No finer split is authorized. All completion/theorem/controller firewalls remain false.
