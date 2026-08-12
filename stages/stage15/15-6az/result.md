# Stage15-6az — complete-2-descent small-height size audit

Base: merged Stage15-6ay. This is an audit stage.

## Verdict

`AUDIT_VERDICT=BLOCK` for the proposed whole-family Petit small-height implication.

Stage15-6ay gives, for one retained state,

\[
X=U^2,\qquad X-d=kV_-^2,\qquad X+d=kV_+^2,
\]

with

\[
U=\frac{kZ}{\lambda T},\qquad fg=\kappa T^2,
\qquad f^2+g^2=kZ^2,
\]

and `lambda in {1,2}` determined by the 2-primary case. Hence

\[
U^2=X=\frac{d k Z^2}{2\kappa T^2}.
\]

The physical two-state height is

\[
kZW\le 2B.
\]

It controls the product of the two Gaussian norms, not the individual ratio `Z/T` appearing in the descent coordinate. Even after retaining the old low-core branch inequality, the current exact constraints do not imply a bound of the form

\[
\hat h(P)\le (1/8+\alpha)\log d,
\qquad \alpha<1/120,
\]

for every retained Stage15 point. Therefore Petit's almost-minimal-twist theorem cannot be promoted to the whole Stage15 population.

This is a quantifier failure, not a rejection of Petit's theorem.

## Important consequence

The explicit descent equations remain valid and can be mined algebraically without canonical height. The next stage must peel the 2-primary cases in

\[
U^2\pm d=kV_\pm^2
\]

before returning to any theorem search.

## Frozen exit

```text
STAGE15_6_SUBSTAGE=6az
STAGE15_6AZ_AUDIT=true
STAGE15_6AZ_AUDIT_VERDICT=BLOCK
STAGE15_6AZ_PETIT_THEOREM_REJECTED=false
STAGE15_6AZ_PETIT_WHOLE_FAMILY_ADAPTER_PROVED=false
STAGE15_6AZ_PRODUCT_HEIGHT_CONTROLS_INDIVIDUAL_DESCENT_HEIGHT=false
STAGE15_6AZ_COMPLETE_2DESCENT_RETAINED=true
STAGE15_6AZ_EXIT=PEEL_2PRIMARY_DESCENT_FACTORIZATION
```
