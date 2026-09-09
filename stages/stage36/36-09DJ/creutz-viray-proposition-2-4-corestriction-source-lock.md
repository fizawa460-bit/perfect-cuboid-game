# Stage36 36-09DJ Creutz--Viray Proposition 2.4 corestriction source lock

## Source

Brendan Creutz and Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, Manuscripta Mathematica 147 (2015), 139--167, DOI 10.1007/s00229-014-0721-7, arXiv:1403.2924.

Exact interface used: Proposition 2.4 and Corollary 2.5.

Let `f=r0` be monic and let `g=r1` represent `ell in L^*`, with `deg(g)<deg(f)`. Define the Euclidean remainder chain by choosing `r_{i+2}` of degree less than `deg(r_{i+1})` such that

`r_{i+2} == r_i mod r_{i+1}`.

Let `a_i` be the leading coefficient of `r_i`, and let `n` be the first integer with `r_{n+2}=0`. Proposition 2.4 gives

`Cor((ell,x-alpha)_2) = sum_{i=0}^n (r_{i+1},r_i)_2 + sum_{i=0}^n (a_{i+1},a_i)_2`.

The second sum is constant over the base field. Therefore, at two local points where all displayed rational functions can be evaluated, the difference of local invariants of the corestriction is exactly the difference obtained from the variable sum

`sum_{i=0}^n (r_{i+1}(t),r_i(t))_2`.

On the hyperelliptic curve `z^2=f(t)`, the `i=0` term `(r1,f(t))_2` is also pointwise trivial whenever `f(t)` is represented by the local square `z^2`.

## Stage36 use

36-09DJ applies this formula to the `L_1` input representing the Brauer difference `F5+R5`. A nonzero difference of local invariants between two `Q_5` receiver points proves that `F5+R5` is nonconstant modulo `Br(Q)`, hence proves `F5 != R5 mod Br(Q)`.

## Firewalls

This source lock does not compute `Pic^0(C3_2)/2`, does not compute the full `L_1/(x-alpha)Pic^0` quotient, does not prove that `F5` lies outside the entire rational-component image, and does not grant full Brauer-group, Brauer--Manin, fixed-parameter, receiver, or endpoint credit.
