# 32R-38 Base-locus tool: automatic reproduction of d=8 / d=10 (2026-10-22)

## What was built (folder `stoll/`)
- `make_curves.py`, `match.py`: Stoll's 92 explicit curves + 48 nodes ↔ repo labels 1..140 (48 nodes unique, 4186 pairings agree).
- `geo_perms.py`: Stoll's 9 coordinate substitutions → permutations of the 140 curves (curves by linear span, nodes by incidence);
  each preserves the 140×140 intersection matrix; generated group order **1536** (geometric Aut). Output `geo_perms.json`.
  Orbits: d=8 1830 classes → **10 orbits** (384,384,192,96,32,384,192,96,64,6); d=10 256 → **1 orbit**. `reps_d8_d10.json`.
- `baselocus.py`: for class x, MILP decomposition mK − x = D over 140 known curves; Singular script for
  h0(|mK − D|), base locus outside D, Hilbert polynomial (degree, p_a); in char p = 10009 a generic linear projection
  to P^2 (birational iff image degree = space degree) and `normal.lib genus` of the plane curve + F_p factorisation.
  Genus via projection: ~1 min (direct space-curve genus: 50 min for d=8, timeout for d=10).
- `sweep.py` + `run_sweep.sh`: all orbit reps, char 0 and char p; whole sweep 1m04s on 12 cores.

## Sweep result (char 0 and char p agree everywhere)
| orbit rep | size | C² | m | h0 | residual |
|---|---|---|---|---|---|
| d8 #0,#1,#12 | 384 each | −8 | 1 | 0 | – (no curve) |
| d8 #14 | 192 | −8 | 1 | 0 | – |
| d8 #6,#29 | 96 each | −8 | 1 | 0 | – |
| d8 #74 | 64 | −8 | 2 | 0 | – |
| d8 #2 | 192 | −4 | 2 | 1 | deg 8, p_a 3, irreducible mod p, genus 3 |
| d8 #9 | 32 | −4 | 2 | 1 | deg 8, p_a 3, genus 3 |
| d8 #312 | 6 | 0 | 1 | 2 | moving pencil — outside the tool |
| d10 #0 | 256 | −2 | 1 | 1 | deg 10, p_a 5, irreducible mod p, genus 5 |

h0=0: 1600 = 1536+64; h0=1: 224 = 192+32; matches the merged d=8 leaf (#1844) and d=10 leaf (#1845).

## Logic
C² < 0 and C + D ∈ |mK| ⇒ C ⊂ Bs|mK − D|. h0 = 0 ⇒ no such C. h0 = 1 ⇒ C = residual; genus_p = p_a and
F_p-irreducible ⇒ the char-0 residual is integral with geometric genus p_a ≥ 2. (Semicontinuity; char-p h0 ≥ char-0 h0.)
Not covered: C² ≥ 0 (h0 ≥ 2, pencils) — the 6 classes of type (8,0) need the fibration argument as in #1844.

## Next
d=12: bottleneck is the class enumeration (~4e12 nodes, 32R-33), not the decision. Idea to test: use the
base-locus/decomposition structure to prune enumeration (classes must sit in Bs of a known-curve system).
