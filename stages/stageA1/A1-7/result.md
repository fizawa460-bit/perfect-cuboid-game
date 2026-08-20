# StageA1 A1-7 — integration verdict audit

## Submitted category

```text
PROPOSED_STAGE_A1_VERDICT=NEW_FAMILY_EXCLUSION
```

That category remains a reasonable **eventual integration label** because A1-2 rigorously excludes anchored nondegenerate members of the displayed Theorem 1.5 and Theorem 1.6 Hilbert-cube families. It is not, however, sufficient by itself to justify closing the entire StageA1 line at this checkpoint.

## Independent audit split

A1-6 passes. It proves that the elementary local/congruence route on the first-two-cover curve is saturated in the precise scope stated there:

- genus 7 and the discriminant factorization are correct;
- Hasse-Weil reduces the specific trivial-reduction-prime mechanism to primes below 211;
- the complete list for that mechanism is `{3,5,7,23}`;
- the `p=3` condition is automatic for coprime `(a,b)`;
- the nonvacuous primes `5,7,23` give no further obstruction merely by lifting the same divisibility condition to higher powers;
- the nondegenerate first-two-cover curve has points over every completion of `Q`.

Thus repeating the same prime scan, the same `p^k` lift, or a larger finite height search does not count as substantive progress.

## Closure audit

The submitted transition

```text
STAGE_A1_STATUS=CLOSED_NEW_FAMILY_EXCLUSION
STOP_AFTER_AUDIT=true
```

is **premature** under the operator's progress-based continuation rule.

The reason is not a failure of A1-6. The reason is that A1-5 already produced a strictly narrower two-branch arithmetic receiver that has not yet received the targeted global attack it explicitly proposed. Every hypothetical survivor lies in `g=1` or `g=6`, and with

```text
R=M-N,
S=M+N,
```

one has positive odd coprime integers satisfying

```text
RS = |A|/g,
S^2-R^2 = (32/g)|a^3 b^3(a^2-b^2)|,
```

with the branch-specific divisibility and cube-exponent allocation recorded in A1-5.

A1-6 exhausts the elementary **local** route, but it does not test whether this `R,S` receiver yields a further global descent, finite cover decomposition, Jacobian/cover reduction, or exact rational-point statement. Therefore the condition "no concrete new reduction remains" has not yet been established.

## Audited routing

```text
A1_6_AUDIT=PASS
A1_7_INTEGRATION_CATEGORY_CANDIDATE=NEW_FAMILY_EXCLUSION
A1_7_CLOSURE_AUDIT=FAIL_THEN_REPAIRED_TO_DEFERRED
STAGE_A1_STATUS=RECONNAISSANCE_ACTIVE_OPERATOR_OVERRIDE
STOP_AFTER_AUDIT=false
NEXT_TARGET=A1-8_TARGETED_GLOBAL_TWO_BRANCH_DESCENT
NEXT_EXPECTED_COMMAND=StageA1-main-batch
```

The next batch must **not** return to larger finite searches or another scan of the same local mechanism. It should attack the audited `g=1/6`, coprime-`R,S` receiver globally. Suitable substantive outcomes include:

- a genuine descent or strict factorization obstruction;
- a finite family of lower-genus covers;
- a Jacobian/quotient decomposition that materially lowers the rational-point problem;
- a rigorous rational-point restriction;
- an exact theorem/computational-algebra adapter.

If that targeted global attempt produces no new mathematics and only repackages the same genus-7/reconstruction-cover wall, then freezing the exact wall and integrating StageA1 as `NEW_FAMILY_EXCLUSION` is appropriate.

## Firewalls

```text
NEW_GENERAL_CONSTRAINT=false
NEW_STAGE27_WEAPON=false
EQUATION6_GLOBAL_EXCLUSION=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
STAGE27_STRUCTURE_RADAR_CHANGED=false
```

Equation (6) is still not proved universal. All A1-5/A1-6 arithmetic remains family-specific. Everywhere local solubility does not imply a rational point.
