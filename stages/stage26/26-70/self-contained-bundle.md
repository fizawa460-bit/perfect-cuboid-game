# Stage26 self-contained theorem bundle

## Contract

All counts use primitive canonical cuboids, no integral-space requirement, and Euclidean cutoff `R<=B`.

`M2(B)` counts exactly-two-face objects and `M3(B)` counts exactly-three-face Euler objects. They are disjoint strata, not a literal source/target subset relation.

The literal at-least-two physical host and completion fraction are

\[
H_{\ge2}=M_2+M_3,\qquad \Phi=\frac{M_3}{M_2+M_3}.
\]

The raw shared-edge incidence host and completion fraction are

\[
P=M_2+3M_3,\qquad \Theta=\frac{3M_3}{M_2+3M_3}.
\]

## Frozen results

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

For every fixed `epsilon>0`,

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}.
\]

For every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Therefore

\[
M_3/M_2\to0,
\qquad \Phi\to0,
\qquad \Theta\to0,
\qquad \Theta/\Phi\to3,
\]

and

\[
H_{\ge2}\sim P\sim M_2\sim C_{M_2}B(\log B)^5.
\]

For every fixed `0<delta<1/46`,

\[
M_3/M_2,\Phi,\Theta=o((\log B)^{-\delta}).
\]

For every fixed `epsilon>0`, the generalized Saunderson lower gives

\[
M_3/M_2,\Phi\gg_\varepsilon B^{-2/3-\varepsilon}(\log B)^{-5},
\]

with the corresponding raw-incidence lower for `Theta` after its exact multiplicity-three adapter.

## Lower construction

For every primitive Pythagorean triple `u^2+v^2=w^2`, define

\[
A=u|4v^2-w^2|,\quad B_1=v|4u^2-w^2|,\quad C=4uvw.
\]

Then

\[
A^2+B_1^2=w^6,
\]

\[
A^2+C^2=u^2(4v^2+w^2)^2,
\]

\[
B_1^2+C^2=v^2(4u^2+w^2)^2.
\]

Primitive Euclidean parameters `(r,s)` give quadratically many inputs under `r,s<=T`, while `R<72T^6`. A fixed output has at most three candidate `w` values because `w^3` is one physical face diagonal; fixed-`w` fibers are bounded by `r_2(w^2)<=4 tau(w^2)=B^o(1)`. Hence `M3(B)>=B^(1/3-o(1))`, equivalently the endpoint-free `B^(1/3-epsilon)` lower above.

## Upper mechanism

The third-face-square condition is a degree-two K3 cover of the split `4A1` quartic-del-Pezzo two-face host. The current upper interface uses an exact local blocker, a separate growing-prime Selberg sieve, and a Huang thin-cover saving. Their savings are not multiplied.

## Non-claims

```text
M3_LOWER_B_ONE_THIRD_WITHOUT_EPSILON_PROVED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
UPPER_LOWER_MATCH=false
ENDPOINT_DELTA_1_OVER_46_PROVED=false
FIXED_POWER_SAVING_UPPER_PROVED=false
K3_MANIN_TRANSFER=false
INDEPENDENCE_CLAIM=false
PERFECT_CUBOID_CONCLUSION=NONE
```
