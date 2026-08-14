# Stage23 post-Stage24 R01 — specific overlap-channel lower bound

## Claim

Let `A_ac,bc(B)` denote the Stage17 raw pair-overlap channel in which both face diagonals `ac` and `bc` are integral under the common primitive/canonical/integral-space cutoff `R=d<=B`. Then the audited Stage24 mixed-parity `C17` family implies

\[
\boxed{A_{ac,bc}(B)\gg\sqrt{\log B}}.
\]

The same construction gives a target-direction lower bound

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}},
\]

where `N_{2,c}` counts Stage19 exactly-two boxes whose two integral faces are `ac` and `bc`, equivalently whose common edge is the canonical largest edge `c`.

## Proof adapter

Stage24 checkpoint50 uses coprime positive solutions of

\[
p^4+q^4=17Z^2
\]

and defines

\[
e=4pq,
\qquad x=4p^2-q^2,
\qquad y=4q^2-p^2.
\]

On the audited physical cone

\[
1<q/p<\frac{1+\sqrt2}{2},
\]

we have

\[
0<x<y<e.
\]

Hence the canonical edge assignment is exactly

\[
(a,b,c)=(x,y,e).
\]

The two Pythagorean identities are

\[
x^2+e^2=(4p^2+q^2)^2,
\]

and

\[
y^2+e^2=(4q^2+p^2)^2.
\]

Therefore every physical member lies in the `ac,bc` pair-overlap channel.

The remaining face `ab` is square only on the audited genus-five fiber product. Faltings leaves only finitely many such rational exceptions in this family. Removing finitely many points preserves the Stage24 quantitative count

\[
\gg\sqrt{\log B}
\]

below space height `R=d<=B`.

Thus all but finitely many counted family members are exactly-two Stage19 objects in the `c`-shared direction, proving both displayed lower bounds.

## Compatibility with the historical Stage17 overlap theorem

Stage17 proves

\[
A_{ac,bc}(B)=o(B(\log B)^3).
\]

There is no conflict. Together the two results give

\[
\boxed{
\sqrt{\log B}\ll A_{ac,bc}(B)=o(B(\log B)^3).
}
\]

Thus this channel is quantitatively unbounded but still negligible relative to the dominant Stage17 exactly-one population.

## Nonclaims

- no asymptotic for `A_ac,bc(B)`;
- no claim that `A_ac,bc` is the dominant pair-overlap channel;
- no claim that `N_{2,c}` is a positive proportion of `N2`;
- no positive-power lower bound;
- no inference about perfect cuboids.

```text
SOURCE_THEOREM=Stage24-50 audited C17 lower family
CANONICAL_EDGE_MAP=(a,b,c)=(x,y,e)
GUARANTEED_FACES=ac,bc
THIRD_FACE_EXCEPTIONS=FINITE_GENUS5
N2_C_LOWER_BOUND=sqrt(log B)
A_AC_BC_LOWER_BOUND=sqrt(log B)
FINITE_DATA_USED_AS_PROOF=false
```
