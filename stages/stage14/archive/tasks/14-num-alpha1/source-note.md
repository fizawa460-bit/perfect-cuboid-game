# Stage14-num-α1 source note

Primary/authoritative material checked for the diagonal-first reconstruction:

- Alexander Belogourov, *Distributed search for a perfect cuboid* (2022 distributed-search report). The report states that the first full almost-perfect batch found complete Face-cuboid data, while the later accelerated version gained more than a fourfold speedup by abandoning most almost-perfect checks; its later Face-cuboid lists are explicitly incomplete.
- Public source repository `renyxadarox/pcuboid`, `pcuboid.c`, version `3.05` (copyright 2017–2018). The code fixes a body diagonal `G`, factors it, generates Girard sum-of-two-squares representations of `G^2`, and combines representation pairs.
- In `search_perfect`, for two representations `G^2=A^2+F^2=B^2+E^2`, the code tests `C^2=B^2-A^2`; when square, `(A,B,C)` has opposite face diagonals `E,F` automatically integral, and `D^2=A^2+B^2` distinguishes Perfect from Face.
- The same fast path also contains edge-divisibility cuts modulo `11` and `19`. These are treated by Stage14-num-α as perfect/Euler-brick-specific pruning and are **not** imported into the complete exactly-two-face census.

Independent Stage14 source contract checked:

- `stages/stage14/14-num3/result.md` defines the ordinary numerical population by `a^2+b^2+c^2=d^2`, `d<=B`, primitive sorted edges, and at least two integral face diagonals. Therefore the α body-diagonal range `d<=B` is exactly the ordinary physical cutoff, not a different finite region.

Stage14-num-α imports the enumeration architecture only. Historical almost-perfect counts are never used as complete Stage14 census data unless independently reproduced under the Stage14 completeness contract.
