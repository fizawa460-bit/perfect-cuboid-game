# Stage35 35-06 — uniform arithmetic attack branches

```text
UNIT=35-06_UNIFORM_ARITHMETIC_ATTACK_BRANCHES
VERDICT=CLASS3_WALL_RETAINED_SHARPER
TARGET=T35-R3-PHYS-EMPTY
APPLICABLE_UNIFORM_CLOSURE_THEOREM_FOUND=false
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-07_FINITE_EXHAUSTIVE_REDUCTION_FALLBACK
```

The exact nearest arithmetic framework is Stoll's 2019 treatment of diagonal genus-5 curves. The structural match is strong: the selected Stage35 fiber is an intersection of three diagonal quadrics in `P4`, has five elliptic quotients with full rational 2-torsion over the ground field, and admits the same covering-collection / elliptic-Chabauty and function-field Mordell--Weil toolkit.

The quantifier mismatch is decisive. Fixed-fiber covering/Chabauty can close an individual `C_t(Q)` when its rank/Selmer hypotheses are certified, but not all rational `t>1`. Function-field classification controls `C(Q(t))`, i.e. rational sections; it does not exclude rational points that appear only after specialization. Likewise injectivity of `E(Q(t)) -> E_t(Q)` is the wrong direction for excluding new specialized points.

The Class-3 wall is therefore sharper than Stage29's original formulation:

```text
On the single exact Q-defined smooth diagonal genus-5 family TS-S-R3-Q1,
uniformly exclude specialization-new rational points in the physical open for
every t in Q, t>1; alternatively prove a receiver-restricted obstruction with
the same quantifier.
```

No all-28 field ledger, bad-fiber subproblem, K3 residual-square lift, or complete fixed-fiber point-set classification is now part of the minimum wall.
