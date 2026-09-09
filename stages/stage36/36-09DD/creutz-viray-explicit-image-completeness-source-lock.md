# Creutz--Viray explicit-image completeness source lock

## Source

Brendan Creutz and Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, Manuscripta Mathematica 147 (2015), 139--167, DOI 10.1007/s00229-014-0721-7, arXiv:1403.2924.

Exact source used here: Theorems 1.1, 1.2, 1.4 and Proposition 5.1.

## Frozen interface

For an even hyperelliptic curve `C: z^2=c f(t)` with branch algebra `L`, set

`Lbar = L^*/(K^* L^{*2})`

and

`L_c = {ell in Lbar : Norm(ell) lies in <c> in K^*/K^{*2}}`.

Theorem 1.1 gives the unramifiedness criterion for `gamma'(ell)`. Theorem 1.2 gives only a complex

`Pic(C)/2 Pic(C) --(t-alpha)--> L_c --gamma--> (Br(C)/Br_0(C))[2]`.

Theorem 1.4 identifies the homology at `L_c`: `ker(gamma)/im(t-alpha)` is zero except for the stated Picard-degree-one exceptional case, where it has order at most two. In the present Stage36 specialization the leading scalar is `c=1`, hence `c` is a square and `L_c=L_1`; the exceptional `L_c/L_1` term is therefore trivial. Thus the complex is exact at `L_1` for this specialization.

Proposition 5.1 gives the exact sequence

`Pic^0(C)/2 Pic^0(C) --(t-alpha)--> L_1 --gamma--> Br_2^Upsilon(C)/Br_0(C) -> 0`.

This identifies the Creutz--Viray explicit image as a quotient of `L_1`, but does **not** identify that image with all of `(Br(C)/Br_0(C))[2]` over a number field without an additional surjectivity/exactness hypothesis. The paper explicitly warns that its image can be proper in general.

## Stage36 consequence

For `p=2`, the physical curve is

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`

with branch algebra `L ~= Q(i)^4` and leading scalar `1`.

Therefore:

1. every CW class `A_{d,j}=(d,t^2+a_j^2)_2` comes from `L_1` and lies in the Creutz--Viray explicit image;
2. proving that finitely many already-constructed classes span the explicit image requires control of the `t-alpha` image of `Pic^0(C3_2)/2`, not merely the four factor labels;
3. even exhaustion of the explicit image would not by itself prove exhaustion of the full 2-torsion Brauer group without the separate surjectivity hypothesis.

## Firewalls

This lock does not compute `Pic^0(C3_2)(Q)/2`, does not compute the full Creutz--Viray image, does not compute the full Brauer group, and does not grant any Brauer--Manin obstruction or fixed-parameter exclusion credit.
