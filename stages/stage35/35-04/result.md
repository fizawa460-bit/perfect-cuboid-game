# Stage35 35-04 — minimal uniform theorem statement

```text
UNIT=35-04_MINIMAL_UNIFORM_THEOREM_STATEMENT
VERDICT=PASS_TARGET_LOCKED_NOT_PROVED
TARGET=T35-R3-PHYS-EMPTY
ARSENAL_ROUTE=S34-WF01
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-05_BAD_FIBER_AND_EXCEPTIONAL_LOCUS
```

The historical Class-3 wording is broader than Stage35 now needs. Because `TS-S-R3-Q1` is a single `Q`-defined direct fibration covering every physical endpoint and 35-03 gives an exact inverse reconstruction, the receiver-matched replacement obligation is

```text
for every t in Q with t>1:
    U_t(Q) = empty,
```

where `U_t` is the nondegenerate physical open of the exact genus-5 curve `C_t` from 35-03.

Equivalently, every rational point on `C_t` for every rational `t>1` must be receiver-degenerate. Proving this does not prove the originally named general specialization theorem for all genus-3/genus-5 fibrations, and Stage35 does not require such a broader theorem.

`S34-WF01 CLASS3_RECEIVER_REPLACEMENT_THEOREM_PIPELINE` is applicable as the workflow firewall: exact population, field, parameter quantifier, and endpoint adapter are frozen; finite-cover reducibility is not assumed. Any generic arithmetic theorem may exclude a bad parameter locus only if 35-05 exhaustively discharges its rational physical part.

No uniform arithmetic theorem has been proved at this leaf. 35-06 owns external theorem/method comparison after the bad/exceptional locus is exact.
