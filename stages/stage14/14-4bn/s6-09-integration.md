# Stage14-4bn — merged s6-09 provenance note

The 4bn branch base is main commit `54aa839606d2ebeee8747837acec940da26a1534`, which is the merge commit of Stage14-s6-09 / PR #373.

Therefore s6-09 is part of the formal merged base of 4bn.

The main `result.md` was drafted while the same fixed-fiber statement was being independently rederived from merged s6-08 + merged t36.  Its phrase that the then-open s6-09 result was not used as a theorem input should be read only as a derivation-provenance statement, not as a claim that the final branch base excludes s6-09.

Canonical final provenance is:

```text
MERGED_S6_09_BASE_PRESENT=true
S6_09_FIXED_FIBER_RESULT_REDERIVED_INDEPENDENTLY=true
```

4bn's genuinely new result beyond merged s6-09 is the converse direction:

```text
B-admissible positive cross-square primitive-face pair
  -> primitive raw cuboid with two integer face diagonals + integer space diagonal
```

with the exact reconstructed cutoff

```text
d_rec = gcd(H,X2)*H3 <= B.
```

This upgrades the s6-07 one-way physical transfer to an exact bijection and makes the active-direction object an exact count rather than an upper-majorant relaxation.
