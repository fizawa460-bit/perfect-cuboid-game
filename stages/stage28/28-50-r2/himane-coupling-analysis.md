# Stage28-50-r2 — Himane coupled-Pythagorean construction analysis

```text
ROUTE=L10_HIMANE_COUPLED_PYTHAGOREAN_COUNT
STATUS=NEGATIVE_CERTIFICATE
SOURCE=arXiv:2405.13061
TARGET=M3
```

Himane's 2024 Theorems 1-3 produce Euler bricks from two primitive Pythagorean triples plus an additional square/coupling condition.  The paper gives three symmetric templates.  Representative corollaries have edges such as

\[
a=u_1u_2,\qquad b=u_1v_2,\qquad c=v_1v_2,
\]

provided the remaining cross expression

\[
(u_1u_2)^2+(v_1v_2)^2
\]

is also a square; the other two templates permute which mixed product must be square.  Saunderson is recovered as a special structured choice in Corollary 3.

The important counting point is that the two Pythagorean triples are **not four free Euclid parameters**.  A new square equation couples them.  Himane states open Problems 1-4 precisely around solving these coupled conditions and gives examples/conjectures, not a positive-density or bounded-height count of coupled pairs.

Therefore the naive heuristic

```text
two_Pythagorean_triples => four_free_parameters => construction_exponent_gain
```

is invalid.  To improve the Stage28 target floor, one would need a theorem of the form

```text
# coupled primitive pairs of Euclid parameters of size <=T >> T^(kappa-o(1))
physical height <= T^(h+o(1))
kappa/h > 1/3
physical output fiber <= T^o(1)
```

or a concrete positive-dimensional parametrized subvariety meeting that inequality.

No such count is supplied by Himane 2024, and the checked examples do not provide an asymptotic substitute.

The paper's Conjecture 2 is additionally endpoint-sensitive: a counterexample to the simultaneous pair of square conditions described there would produce a perfect cuboid.  That branch is outside Stage28 and cannot be used as a target-family lower route.

```text
HIMANE_TWO_TRIPLES_FREE_DIMENSION_CLAIM=false
HIMANE_COUPLED_PAIR_POSITIVE_DENSITY_THEOREM=false
HIMANE_MATCHED_R_LE_B_POWER_LOWER_GT_ONE_THIRD=false
HIMANE_ENDPOINT_SENSITIVE_BRANCH_FORBIDDEN=true
RESTART_RECEIVER=CountedCoupledPythagoreanPairFamilyWithKappaOverHGreaterThanOneThird
AUDIT_REQUIRED=true
```
