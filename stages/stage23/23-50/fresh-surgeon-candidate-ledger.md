# Stage23-50 fresh Stage19 surgeon candidate-generation ledger

Scope: repair only. Q04/Q11 are not reopened. These candidates are generated from the Stage17 Pythagorean-chain interface rather than copied from the Stage14/15 attack ledger.

Stage19 test contract used for every candidate: two integral face diagonals, integral space diagonal, positive/canonical edges after reordering, primitive representative, unbounded parameter potential, and controlled physical height `d`.

## F50-S1 — synchronized two-level Pythagorean parameters

Start from two Pythagorean extensions and deliberately synchronize their primitive parameters. For coprime positive `u>v`, set

\[
x=(u^2-v^2)^2,\quad y=2uv(u^2-v^2),\quad p=u^4-v^4,
\]
\[
z=2uv(u^2+v^2),\quad d=(u^2+v^2)^2.
\]

Then identically

\[
x^2+y^2=p^2,\qquad p^2+z^2=d^2.
\]

Thus this is an explicit infinite Stage17-chain ansatz with physical height `d=(u^2+v^2)^2`. The two possible added faces reduce to

\[
x^2+z^2=u^8+14u^4v^4+v^8,
\]

and

\[
y^2+z^2=8u^2v^2(u^4+v^4).
\]

For the `yz` branch, squarehood is equivalent (up to the visible square `(2uv)^2`) to

\[
W^2=2(u^4+v^4).
\]

If `u,v` have opposite parity, the right side is `2 mod 16`, impossible for a square. Hence any primitive-parameter survivor must have `u,v` both odd. In that parity class the raw edges have a common factor, so primitive reduction is required before interpreting multiplicity; division by the common scale preserves all Pythagorean equalities, but the residual quartic square equation remains. No infinite nontrivial solution family is produced here.

For the `xz` branch the fresh receiver is the binary octic square equation

\[
Q^2=u^8+14u^4v^4+v^8.
\]

No identity makes it square. This candidate therefore reaches a concrete quartic/octic arithmetic gate rather than failing at the Stage17 contract.

Status: `LIVE_BUT_NO_LOWER_BOUND`; useful new candidate geometry, no certified Stage19 infinite family.

## F50-S2 — second-face factor-gap ansatz

Do not parametrize the second face by another independent Pythagorean pair. Instead factor it directly. For a desired second face `x^2+z^2=q^2`, write

\[
(q-z)(q+z)=x^2.
\]

Choose a positive divisor parameter `r=q-z` of `x^2`. Then

\[
q=\frac{x^2/r+r}{2},\qquad z=\frac{x^2/r-r}{2}.
\]

Combining this with the Stage17 chain `x^2+y^2=p^2`, `p^2+z^2=d^2` converts Stage19 construction into a divisor-controlled compatibility equation rather than the Stage14/15 squareclass receiver.

The most aggressive fixed-gap specialization `r=1` gives `z=(x^2-1)/2`. If it is combined with the standard unit-gap space extension `z=(p^2-1)/2`, then `x^2=p^2`, hence `x=p`, forcing `y=0`. Positivity fails identically. Thus the tempting double-unit-gap family is globally dead, not merely absent in a finite scan.

For fixed `r>1`, compatibility with the unit-gap space extension gives

\[
x^2=r p^2+r(r-1),
\]

with `p^2=x^2+y^2`. Eliminating `p` yields

\[
(1-r)x^2=r y^2+r(r-1).
\]

For `r>1`, the left side is nonpositive while the right side is positive, so no positive solution exists. Therefore the entire fixed factor-gap + unit-gap-space subfamily is excluded.

Status: `GLOBAL_POSITIVITY_OBSTRUCTION`; fresh construction route killed exactly.

## F50-S3 — proportional synchronization ansatz

Try to force an infinite one-parameter family by taking proportional Pythagorean parameters at the two levels: `(U,V)=(ku,kv)` before primitive normalization. The space triple then scales by `k^2`, while its leg ratio `p/z` is unchanged. Matching its leg `p` to the first-face hypotenuse only changes an overall scale. After dividing the global gcd to return to the primitive Stage19 population, `k` disappears.

Thus the apparent new parameter creates only homothetic copies of the same primitive object. It cannot prove target unboundedness or any positive-power lower bound because Stage19 counts primitive canonical representatives once.

Status: `PRIMITIVE_COLLAPSE`; no lower-bound contribution.

## F50-S4 — near-diagonal synchronized slice

Apply F50-S1 on a genuinely one-dimensional near-diagonal slice `u=v+h` with fixed nonzero integer `h`. This differs from checkpoint30's AR-039 consecutive-parameter slice: the ambient family and resulting receivers are different. The physical height is

\[
d=((v+h)^2+v^2)^2\asymp v^4,
\]

so any infinite survivor sequence would yield an explicit constructive lower bound of order at least `B^(1/4)` up to multiplicity/congruence losses.

The added `yz` face becomes

\[
W^2=2((v+h)^4+v^4).
\]

For `h` odd, `u,v` have opposite parity, so the RHS is `2 mod 16` and the entire slice is excluded. Therefore only even `h` can survive this local gate; but then `u,v` have the same parity, incompatible with coprime primitive Pythagorean parameters unless both are odd, which forces `v` odd and `h` even. That residual class is not automatically excluded, but still must solve the quartic square equation. No identity or parametrization was found that makes it square identically.

The `xz` branch becomes the explicit degree-eight square-value problem

\[
Q^2=(v+h)^8+14(v+h)^4v^4+v^8.
\]

Again there is no automatic square identity. The candidate survives positivity and height growth but stalls at a concrete high-degree arithmetic condition.

Status: `LOCAL_PARITY_SPLIT_THEN_HIGH_DEGREE_GATE`; no certified infinite Stage19 family.

## Surgeon conclusion

Four fresh candidate mechanisms were generated and pushed through the literal Stage19 contract. They fail at distinct points:

- F50-S1: explicit Stage17 infinite chain reaches new quartic/octic square receivers; no infinite Stage19 solution family certified.
- F50-S2: direct factor-gap construction is globally killed by positivity when paired with the unit-gap space extension.
- F50-S3: proportional parameter freedom collapses under primitive normalization.
- F50-S4: near-diagonal synchronized slices split by a mod-16 obstruction and otherwise reach explicit high-degree square-value gates.

No candidate proves a stronger upper bound, target unboundedness, or a positive-power Stage19 lower bound. The negative result is therefore a generated-candidate ledger, not a claim of exhaustive nonexistence.

```text
FRESH_CANDIDATES_GENERATED=4
COPIED_FROM_STAGE14_15_LEDGER=false
STAGE19_CONTRACT_TESTED=true
NEW_PROMOTABLE_BREAKTHROUGH=false
FRESH_NEGATIVE_RESULT=SUPPORTED_BY_CANDIDATE_LEDGER
SURGEON_SEARCH_PROVES_EXHAUSTIVENESS=false
Q04_Q11_REOPENED=false
```
