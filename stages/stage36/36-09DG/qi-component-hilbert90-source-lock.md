# Stage36 36-09DG Q(i)-component / Hilbert-90 source lock

## Sources

1. Hilbert Theorem 90 for a cyclic extension `E/K`: an element `u in E^*` with norm one is `u=beta/sigma(beta)`. Convenient reference: MIT 18.785 Number Theory I, Lecture 24, Corollary 24.2.
2. Creutz--Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, Theorems 1.1, 1.2, 1.4 and Proposition 5.1, as already frozen by 36-09CW/DD.

No new-theorem credit is granted.

## Quadratic squareclass consequence

Let `E=Q(i)` and `V=E^*/E^{*2}`. If `alpha in E^*` has square norm, write `N(alpha)=s^2` with `s in Q^*`. Then `u=alpha/s` has norm one. Hilbert 90 gives

`u=beta/conj(beta)=beta^2/N(beta)`.

Hence

`alpha=(s/N(beta))*beta^2`,

so the squareclass of `alpha` is represented by a rational number. Conversely every rational element has square norm from `E/Q`. Therefore the kernel of the norm map on `E`-squareclasses is exactly the rational-squareclass image (with the harmless fact that `-1=i^2` already dies in `V`).

For the Stage36 branch algebra `L=E^4`, the rational-component subgroup consists of tuples whose four coordinate norm squareclasses are individually trivial. A genuinely non-rational input in `L_1` must therefore have at least two coordinates with the same/nontrivially balancing norm squareclass.

## First paired input

Take `pi=2+i`, with `N(pi)=5`. Then

`ell_5=(pi,pi,1,1) in L^*`

has total norm `5^2`, hence defines an element of `L_1`. By Creutz--Viray Theorem 1.1 its image

`F_5=gamma(ell_5)`

is an unramified 2-torsion Brauer class on `C3_2`.

This input has norm-vector squareclasses `(5,5,1,1)`, so it is not in the rational-component input subgroup. This input-level observation alone does not prove independence after quotienting by the `x-alpha` Picard image; that must come from an actual evaluation test.

## Split Q_5 evaluation interface

At 5, `Q(i) tensor Q_5` splits because `-1` is a square modulo 5. Use the two embeddings reducing `i` to `+2` and `-2` modulo 5. The element `pi=2+i` is a unit in the first embedding and has valuation one in the second (their product is 5).

For factor `t^2+4`, the chosen root is `2i`; in the valuation-one embedding it reduces to `1 mod 5`. For factor `t^2+1/4`, the chosen root is `i/2`; there it reduces to `4 mod 5`.

Thus, at a Q_5 receiver point with `t` integral and avoiding residues 1 and 4, the local evaluation of `F_5` is the 5-adic Hilbert/Legendre character of

`(t-1)(t-4)`.

The unit embedding contributes zero, and at the valuation-one embedding the odd-prime Hilbert rule `(5*u,v)_5=(v/5)` for unit `v` applies. Since the two branch components add in the corestriction, their characters multiply.

## Firewalls

This lock does not compute the full `L_1` quotient, does not compute `Pic^0(C3_2)/2`, does not identify `F_5` with a full-Brauer complement generator, and does not grant a Brauer--Manin obstruction or fixed-p exclusion.
