# Stage32-07 — degree-8 bounded-multiplicity signature-cell pilot

This is the first Stage32-main-batch step after the degree-4 row closure.  It does **not** reuse the binary-exceptional Stage32-05/32-06 assumption at degree 8.

At `d=8`, the exact dual caps are

```text
known nonexceptional intersection <= 4
exceptional intersection <= 2
```

so the 48 selected exceptional coordinates live in `0..2` and the 16 selected normal coordinates live in `0..4`.

The pilot builds an exact bounded-multiplicity replacement for the binary MITM layer:

1. source-lock the rank-64 Picard core and reverify all 140 dual-cap certificates;
2. reconstruct the selected 64-coordinate transform (`det=2^38`, inverse denominator 8) and the canonical q-tail HNF quotient;
3. verify that the degree-8 q-tail domain `0..4` reaches exactly the same mod-8 subgroup as `0..3`: every q-tail generator has order dividing 4, so the extra value 4 contributes residue zero;
4. split the 48 exceptional coordinates into the same `16+4+4` A/B/C halves, but use exact dynamic programming over values `0,1,2` rather than combinations of binary masks;
5. preserve the total A/B/C multiplicities and quotient signature together, including the exact number of exceptional assignments represented by every compressed state;
6. join left/right states only when their quotient signatures can be completed by a legal q-head total and the q-tail residue subgroup;
7. treat every matched `(aggregate, split, left signature, right signature)` as an immutable **signature cell**.  This partitions the bounded exceptional assignments without materializing them one by one;
8. for solve-mode parents, run one exact QF_NIA problem per signature cell with all 64 lattice-image congruences, all 140 cap inequalities, degree/mass identities, q-head sum, exact side multiplicities and the adjunction quadratic inequality.  SAT is retained; UNKNOWN receives no closure credit; only UNSAT for every cell closes a parent.

The discovery workflow deliberately uses three solve parents of increasing size plus one count-only stress parent.  The stress parent measures compression of the bounded exceptional space but receives no mathematical closure credit.

Mandatory firewalls:

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
RECEIVER_CREDIT=false
LOW_DEGREE_PREFIX_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

## Scope stop

This PR is a bounded algorithm/closure pilot, not the degree-8 row sweep.  Do not launch all degree-8 parents or any degree above 8 until the pilot demonstrates that the signature-cell partition is both complete and computationally useful.  If any solve parent reaches `UNKNOWN(timeout)`, preserve the exact cell inventory and expose that signature cell as the next Class-2 wall rather than extending timeouts blindly.
