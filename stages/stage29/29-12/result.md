# Stage29-12 — joint, local, parametric, and population-interaction attack portfolio

```text
STAGE=Stage29
ITEM=29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ATTACK_ROUTE_COUNT_RETAINED=11
NEW_ATTACK_ROUTE_CREATED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Scope

This stage attacks the four 29-12 owners without replaying their infrastructure:

```text
J12-JOINT-V4
J12-LOCAL-SQUARECLASS
J12-PARAMETRIC
J12-POP-INTERACTION
```

Audited 29-07 exact V4/population bridges, 29-08 global Master-Hit coverage, 29-09 odd-prime local arithmetic, Gap Scan B's Stage14 endpoint theorem, and the 29-10/11 route firewalls are inputs only. Previously proved facts receive no duplicate attack credit.

## 2. J12-POP-INTERACTION — new exact relative endpoint-density theorem

The key interaction missed before Gap Scan B is stronger when expressed in the 29-07 incidence language.

Stage29-07 defines selected two-face incidences

```text
I2   = M2 + 3*M3,
I2^S = N2 + 3*P.
```

Stage14's raw two-face graph is the same primitive/canonical, integral-space selected-pair incidence object on the endpoint-compatible cutoff. Its exact identity is

```text
E(B)=N2(B)+3P(B),
```

so under the audited Stage29 dictionary

```text
E(B)=I2^S(B).
```

The frozen Stage14 proof chain gives, for every epsilon>0,

```text
I2^S(B) <<_epsilon B^(1/2+epsilon).
```

Meanwhile Stage29-04 gives

```text
M2(B) ~ C_M2 * B*(log B)^5,  C_M2>0,
M3(B)=o(M2(B)),
```

hence

```text
I2(B)=M2(B)+3M3(B) ~ C_M2*B*(log B)^5.
```

Therefore for every epsilon>0,

\[
\boxed{
\frac{I_2^S(B)}{I_2(B)}
\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

In particular, for every fixed `0<epsilon<1/2`,

```text
I2^S(B)/I2(B) -> 0.
```

This is a literal selected-two-face incidence survival theorem: among all canonical primitive two-face incidences, the integral-space subincidences have polynomially vanishing relative density.

The same inputs give a genuine endpoint-density theorem on the legal nested host

```text
H_ge2 = M2 disjoint_union M3.
```

Since `H_ge2(B)~M2(B)` and `P subset H_ge2`,

\[
\boxed{
\frac{P(B)}{H_{\ge2}(B)}
\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

Thus

```text
P(B)/H_ge2(B) -> 0.
```

Secondary whole-host consequences are

```text
P/H_ge1 <<_epsilon B^(-3/2+epsilon)/(log B),
P/U       <<_epsilon B^(-5/2+epsilon).
```

These are relative-density theorems, not emptiness theorems.

The important firewall is unchanged:

```text
P/M3 is the literal final space-survival ratio after all three faces,
P/M3 global scale remains UNKNOWN.
```

The new theorem does not determine the conditional final step `P/M3`, does not order `P` against `N2`, and does not turn density zero into nonexistence.

Proposed receiver state:

```text
R29-POP-I2S=DISCHARGED_SELECTED_TWO_FACE_SPACE_SURVIVAL_UPPER
R29-POP-H2=DISCHARGED_ENDPOINT_DENSITY_ZERO_IN_H_GE2
J12-POP-INTERACTION=GREEN_RELATIVE_ENDPOINT_DENSITY_THEOREM_NO_EMPTINESS
```

The GREEN proposal is attack credit only for the new normalized theorem produced by combining the already-certified Stage14 endpoint/incidence bound with the exact Stage29 host/incidence dictionary. Stage14's bound itself is not re-credited.

## 3. J12-JOINT-V4 — exact joint geometry remains nondecisive

The residual V4 cells on the selected two-face floor remain exactly

```text
third NO,  space NO  : M2-N2
third NO,  space YES : N2
third YES, space NO  : 3*(M3-P)
third YES, space YES : 3*P.
```

The new `I2^S/I2` theorem controls the whole `space YES` column, but it does not identify a genuinely joint third-face/space correlation law. In particular neither

```text
P/M3
```

nor

```text
3P/(N2+3P)
```

has a nontrivial certified asymptotic scale.

The cross quotient still has a valid normal-cover/cohomological package and

```text
R29-X1=OPEN_BOUNDED_GLOBAL_ADE_ENUMERATION.
```

Completing X1 would improve the global geometric ledger but currently has no theorem that makes the physical endpoint image empty. Marginal K3 results remain owned by G10-K3-SIGN and are not re-credited here.

```text
J12-JOINT-V4=AMBER_EXACT_JOINT_MODEL_NO_JOINT_ENDPOINT_OBSTRUCTION
```

## 4. J12-LOCAL-SQUARECLASS — odd primes exact, p=2 locally positive, global transfer open

29-09 already proved the exact odd-prime law

```text
Delta_p=1/64+O(1/p)
```

with the exact correlated triple-branch term `q3`; this is consumed, not replayed.

At `p=2`, the known Euler brick `(44,117,240)` gives the base point

```text
x=44^2,
y=117^2,
z=240^2.
```

All seven values

```text
x,y,z,x+y,x+z,y+z,x+y+z
```

are nonzero Q2-squares: the first six are the three edge squares and three face-diagonal squares, while

```text
x+y+z=73225
```

is an odd 2-adic square because `73225 == 1 (mod 8)`.

Because `Q2^{*2}` is an open subgroup of `Q2^*` and all seven linear forms are nonzero at this point, there is a Q2-open projective neighbourhood on which all seven squareclasses stay trivial. Hence the full endpoint lift locus in `P2(Q2)` has nonempty interior and positive Haar measure.

This yields only the bounded qualitative child

```text
R29-KUM-LOC2-2A=DISCHARGED_POSITIVE_Q2_LIFT_CYLINDER
```

while the parent remains

```text
R29-KUM-LOC2-2=OPEN_EXACT_TWO_ADIC_STATE_DENSITY,
R29-KUM-LOC3=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER.
```

Thus `p=2` cannot currently supply a local emptiness obstruction, and the exact odd-prime densities still cannot be multiplied into a global Euler product without the height/primitivity/canonical/equidistribution adapter.

```text
J12-LOCAL-SQUARECLASS=AMBER_EXACT_LOCAL_DATA_NO_GLOBAL_TRANSFER
```

## 5. J12-PARAMETRIC — global coverage is real, decisive blocker remains conjectural

29-08 already certifies that every primitive Euler brick, hence every perfect-cuboid candidate, is represented after gcd normalization by a Master-Hit. This is true global endpoint coverage and is consumed here without duplicate credit.

The strongest endpoint-wide parametric receiver remains

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER.
```

If the exponent-one assertion were proved for every Master-Hit, it would exclude every perfect cuboid. It is not proved; finite verification cannot be promoted.

The total `(m,n)` Mordell-Weil fibration is globally covering on the Euler marginal, but bounded Mordell-Weil enumeration is not exhaustive and the remaining fibration field/arithmetic-specialization receivers stay open:

```text
R29-PESCH2=OPEN_BOUNDED,
R29-FIB1=OPEN,
R29-FIB2=OPEN.
```

No physical-height-uniform parameter theorem converts the Stage14 endpoint bound into a sharper Master-Hit parameter-count theorem without a multiplicity/height adapter.

```text
J12-PARAMETRIC=AMBER_GLOBAL_COVERAGE_WITH_CONJECTURAL_DECISIVE_BLOCKER
```

## 6. Portfolio classification

Submitted classification:

```text
J12-JOINT-V4        = AMBER
J12-LOCAL-SQUARECLASS = AMBER
J12-PARAMETRIC      = AMBER
J12-POP-INTERACTION = GREEN

GREEN_ROUTE_COUNT_29_12=1
AMBER_ROUTE_COUNT_29_12=3
ATTACK_ROUTE_COUNT_RETAINED=11
```

The GREEN route is not a solution claim. It records a new certified relative endpoint-density theorem on a legal nested host / exact selected incidence measure.

## 7. Handoff

No Stage16--28 theorem requires reopening: the Stage14 input was already repaired by Gap Scan B and is only being consumed through the exact Stage29 incidence dictionary.

```text
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=GAP_SCAN_C_ROADMAP_REVIEW_C
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
