# Stage29-15 audit — fresh claimed-solution vetting

A fresh search located the 2026 self-published repository `AEjonanonymous/Non-existence-of-Perfect-Cuboids`, which claims a formal Lean proof of perfect-cuboid nonexistence. This source was not in the submitted literature refresh, so it was checked adversarially rather than accepted by title or `No Goals` status.

## Lean scope check

The file `No Perfect Cuboids.lean` proves only conditional statements. In particular:

- `parity_wall_consistency` assumes the extra congruences `x^2=4`, `y^2=0`, `z^2=1 (mod 8)`; it does not derive them from an arbitrary perfect cuboid.
- `is_torsion_point(u)` is defined to mean `u in {0,1,-1}`.
- `perfection_locus_empty` assumes `is_torsion_point(u)`.
- the final theorem `no_perfect_cuboid_final` assumes both `h_rational_limit : is_torsion_point u` and the asserted perfection equation. There is no formal theorem deriving `h_rational_limit` from an arbitrary rational/integer perfect cuboid.

Thus the Lean kernel verifies the displayed conditional implications, not the missing global reduction from arbitrary perfect cuboids to those hypotheses.

The README's numerical/parametric discussion also does not supply that universal coverage theorem. In particular a parametric sweep or a rank claim on one selected family cannot replace the Stage29 global endpoint/Master-Hit coverage requirement.

```text
R29-EXT-REED-2026=REJECTED_AS_GLOBAL_PROOF_MISSING_UNIVERSAL_ENDPOINT_REDUCTION
LEAN_FILE_KERNEL_CHECKED_CONDITIONAL_STATEMENTS=true
LEAN_FORMALIZES_ARBITRARY_PERFECT_CUBOID_NONEXISTENCE=false
NEW_ENDPOINT_RECEIVER_CREATED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This is a negative source-vetting certificate only; it is not a criticism of using Lean for a correctly specified endpoint theorem.