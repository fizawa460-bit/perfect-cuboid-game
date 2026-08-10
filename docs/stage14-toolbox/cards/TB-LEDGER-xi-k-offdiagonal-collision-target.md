# Off-diagonal (xi,k) collision-energy target

```yaml
ID: TB-LEDGER-xi-k-offdiagonal-collision-target
TYPE: LEDGER
STATUS: CURRENT
TITLE: Direct current obstruction is average off-diagonal recurrence in the joint labels (xi,k)
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-14
SOURCE_PR: 437
SOURCE_MERGE_SHA: 31c3636016f5f0ff80133f0c1b6a9cbbd91a3697
SOURCE_FILES:
  - stages/stage14/14-s7-14/result.md
```

## INPUT

For a canonical reduced coordinate `P/Q`, define

```text
xi=ker(PQ)
k =ker(Q^2-P^2)
gcd(xi,k)=1
```

and

```text
r_B(xi,k)=#{P/Q in the Stage14 canonical window with these labels}.
```

## OUTPUT

A physical pair must collide in both labels. The direct receiver is

```text
E_off(B)=sum_xi sum_k r_B(xi,k)*(r_B(xi,k)-1).
```

On the critical shell `xi~B^(3/4+o(1))`, any theorem

```text
E_off,critical(B) << B^(7/8-delta+o(1))
```

with fixed `delta>0` is sufficient for a strict whole-family improvement after the standard off-critical slack split.

## VARIABLE DICTIONARY

- `xi`: shared squarefree label `ker(PQ)`.
- `k`: transverse squarefree difference label `ker(Q^2-P^2)`.
- critical range: `k<=B^(1+o(1))`, `xi*k<=B^(7/4+o(1))`.

## USED BY

- Stage14-s7-15 style collision-energy attacks.
- Deciding whether a candidate squareclass/mean-square theorem attacks the direct current obstruction.

## DO NOT USE FOR

- Pointwise fixed-`(xi,k)` multiplicity is not this average theorem.
- A t/tH second-moment estimate is not automatically this receiver without an exact operator bridge.

## PROVENANCE NOTES

Merged s7-14 defines this receiver and explicitly leaves its power saving unproved.