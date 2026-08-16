# Stage26 arsenal promotion

## S26-W01 — GENERALIZED_SAUNDERSON_TWO_PARAMETER_LOWER

Accepted source: Stage26 checkpoint60 hostile audit / PR #1019.

Contract: primitive canonical Euler cuboids, no space requirement, Euclidean cutoff `R<=B`.

Reusable theorem:

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}
\qquad(\forall\varepsilon>0).
\]

Mechanism: all primitive Pythagorean triples feed the Saunderson identities; the Euclidean parameter space has quadratic size; `R<72T^6`; `w^3` is a physical face-diagonal invariant; fixed-output fibers are divisor-size.

Firewalls: no epsilon-free `B^(1/3)` lower, no asymptotic, no true exponent.

## S26-W02 — LITERAL_EULER_COMPLETION_CORRIDOR

Accepted sources: Stage26 checkpoints30, 40, 60 plus the Stage18 `M2` asymptotic.

Literal object host:

\[
H_{\ge2}=M_2+M_3,\qquad \Phi=M_3/H_{\ge2}.
\]

Raw incidence host:

\[
P=M_2+3M_3,\qquad \Theta=3M_3/P.
\]

Reusable conclusions:

\[
\Phi\to0,\qquad\Theta\to0,\qquad\Theta/\Phi\to3,
\]

and, for fixed `epsilon>0` and fixed `0<delta<1/46`,

\[
B^{-2/3-\varepsilon}(\log B)^{-5}
\ll_\varepsilon \Phi,\Theta
=o((\log B)^{-\delta}).
\]

The lower constants for `Phi` and `Theta` are not asserted equal; `Theta` carries the exact raw-incidence multiplicity-three adapter.

Firewalls: exactly-two and exactly-three are disjoint strata; this is not an objectwise survival probability between `M2` and `M3`. No independence interpretation.

## S26-W03 — K3_THIRD_FACE_UPPER_INTERFACE

Reusable upper-side interface: split `4A1` quartic-del-Pezzo/two-face host, degree-two K3 third-face cover, exact local blocker, separate growing-prime Selberg sieve, and Huang thin-cover saving.

For every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

The local-sieve and thin-cover savings are not multiplied. No K3 Manin transfer or fixed polynomial `B` saving is claimed.

## Global firewall

```text
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
UPPER_LOWER_MATCH=false
PERFECT_CUBOID_CONCLUSION=NONE
```
