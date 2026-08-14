# Stage23-50 fresh Stage19 surgeon candidate-generation ledger

Scope: checkpoint50 fresh-surgeon repair only. Q04/Q11 are not reopened. Four candidates were generated from the Stage17 Pythagorean-chain interface and tested against the literal Stage19 contract.

## Certified Stage19 lower-bound status

The current proved lower bound is

\[
\boxed{N_2(B)\ge3495\qquad(B\ge500{,}000{,}000)}.
\]

It follows from the exact census `N2(500000000)=3495` and monotonicity of the nested cutoff. This is a certified constant floor only.

```text
STAGE19_CERTIFIED_CONSTANT_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
STAGE19_UNBOUNDEDNESS_PROVED=false
STAGE19_POSITIVE_POWER_LOWER_BOUND_PROVED=false
STAGE19_MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
```

## F50-S1 — synchronized two-level Pythagorean parameters

For coprime `u>v`, set

\[
x=(u^2-v^2)^2,
\quad y=2uv(u^2-v^2),
\quad p=u^4-v^4,
\]
\[
z=2uv(u^2+v^2),
\quad d=(u^2+v^2)^2.
\]

Then `x^2+y^2=p^2` and `p^2+z^2=d^2` identically. The two added-face conditions reduce to

\[
Q^2=u^8+14u^4v^4+v^8,
\qquad
W^2=2(u^4+v^4).
\]

Opposite parity is excluded on the `W` branch modulo 16. Residual classes reach genuine quartic/octic square-value gates. No infinite primitive Stage19 family is proved.

Status: `LIVE_BUT_NO_LOWER_BOUND`.

## F50-S2 — second-face factor-gap ansatz

Factor `x^2+z^2=q^2` by `r=q-z`. Coupling the resulting formula to the unit-gap Stage17 space extension gives `r=1 => x=p => y=0`, and for every fixed `r>1` elimination yields

\[
(1-r)x^2=r y^2+r(r-1),
\]

whose left side is nonpositive and right side positive. The entire fixed factor-gap + unit-gap-space subfamily is excluded.

Status: `GLOBAL_POSITIVITY_OBSTRUCTION`.

## F50-S3 — proportional synchronization

Taking proportional parameter pairs `(U,V)=(ku,kv)` only changes global scale. Primitive normalization removes `k`, so this produces homothetic copies rather than new primitive objects.

Status: `PRIMITIVE_COLLAPSE`.

## F50-S4 — near-diagonal synchronized slice

Set `u=v+h` with fixed nonzero `h`. Then

\[
d=((v+h)^2+v^2)^2\asymp v^4.
\]

The earlier statement that **mere infinitude** of survivors would imply a `B^(1/4)` lower bound is withdrawn. An infinite survivor sequence may be arbitrarily sparse. The correct statement is conditional: because `d\asymp v^4`, a quantitatively dense survivor set with count of order `V` for `v<=V` would live on a natural `B^(1/4)` counting scale.

For the `yz` branch,

\[
W^2=2((v+h)^4+v^4).
\]

Odd `h` is excluded modulo 16. Residual even-gap classes and the `xz` branch

\[
Q^2=(v+h)^8+14(v+h)^4v^4+v^8
\]

reach high-degree square-value gates, with no infinite family or quantitative survivor density proved.

```text
F50_S4_INFINITE_SEQUENCE_IMPLIES_B_QUARTER=false
F50_S4_DENSE_SURVIVOR_COUNT_COULD_YIELD_B_QUARTER_SCALE=true
```

Status: `LOCAL_PARITY_SPLIT_THEN_HIGH_DEGREE_GATE`.

## Surgeon conclusion

The four fresh candidates fail at distinct points: new quartic/octic gates, positivity, primitive collapse, and parity/high-degree gates. They do not improve the inherited upper bound and do not improve the certified Stage19 lower bound beyond the constant floor 3495.

```text
FRESH_CANDIDATES_GENERATED=4
COPIED_FROM_STAGE14_15_LEDGER=false
STAGE19_CONTRACT_TESTED=true
NEW_PROMOTABLE_BREAKTHROUGH=false
FRESH_NEGATIVE_RESULT=SUPPORTED_BY_CANDIDATE_LEDGER
SURGEON_SEARCH_PROVES_EXHAUSTIVENESS=false
Q04_Q11_REOPENED=false
```
