# Stage25-60 R503 result

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R503

The direct Yoshida generic-section route is closed by an exact identification with the plus-sign Pythagorean/Frey family and the geometric generic Mordell-Weil rank-zero theorem.

The explicit Yoshida fixed-fiber orbit at `s=5/3` is height-sparse: the cuboid parameter is Möbius in the `x`-coordinate of `[n]P`, so fixed-curve canonical height gives `h(t_n)=Theta(n^2)`, while a degree-two primitive edge ratio forces only `O(sqrt(log B))` orbit indices below physical height `B`.

The displayed Yoshida construction of infinitely many positive-rank parameters `s` is also Möbius in the same `x([n]P)` and therefore supplies only `O(sqrt(log X))` displayed parameters of rational height at most `X`.

Accordingly R503 is narrowed, not killed:

```text
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE
R503_GENERIC_GEOMETRIC_MW_RANK=0
R503_GENERIC_NONTORSION_SECTION_EXISTS=false
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED
R503_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))
R503_DISPLAYED_POSITIVE_RANK_S_SEQUENCE_COUNT_UPPER=O(sqrt(log X))
R503_BASE_CHANGE_MULTISECTION_ROUTE=OPEN_GATE
R503_QUANTITATIVE_EXCEPTIONAL_FIBER_ROUTE=OPEN_GATE
R503_UNIFORM_SMALL_POINT_ROUTE=OPEN_GATE
R503_GLOBAL_EXPONENT_UPGRADE_PROVED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```

The audited global Stage25 envelope remains unchanged:

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

If this R503 gate passes fresh audit, checkpoint60 continues under persistent route IDs with R504, R505 and R506.
