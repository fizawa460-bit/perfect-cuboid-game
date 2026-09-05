# Stage36 36-09N source lock: 2-isogeny descent + injective specialization

Accessed: 2026-09-06

## A. Descent by 2-isogeny

Source used:
- Andrej Dujella, *Elliptic Curves*, section 15.5, “Rank of elliptic curves”, especially equations (15.29)–(15.31).
- URL: https://web.math.pmf.unizg.hr/~duje/pdf/section15-5.pdf

Exact facts used in 36-09N:

For

`E: y^2 = x^3 + a*x^2 + b*x`

with `(0,0)` rational 2-torsion, the 2-isogenous curve is

`E': y^2 = x^3 - 2*a*x^2 + (a^2-4*b)*x`.

The descent maps are

- `alpha(O)=1`, `alpha((0,0))=[b]`, `alpha((x,y))=[x]` otherwise,
- and analogously `beta` on `E'`.

Their kernels are the images of the dual 2-isogenies. If `r=rank E(Q)`, then

`2^r = |Im(alpha)|*|Im(beta)|/4`.

For a square-free divisor `b1` of `b`, writing `b=b1*b2`, the class `[b1]` lies in `Im(alpha)` exactly when the homogeneous quartic

`N^2 = b1*M^4 + a*M^2*e^2 + b2*e^4`

has a nontrivial integer solution after primitive normalization. The same statement applies to `E'`.

This is used only for the specialized rational curve at `q=6`; the relative function-field cover equations are also rederived algebraically in the Stage36 verifier.

## B. Injective specialization

Primary source:
- Ivica Gusić and Petra Tadić, “A remark on the injectivity of the specialization homomorphism”, Glasnik Matematicki 47 (2012), 265–275.
- DOI: https://doi.org/10.3336/gm.47.2.03
- journal page: https://web.math.pmf.unizg.hr/glasnik/vol_47/no2_03.html

Exact theorem used (Theorem 1.1; also restated in later literature):

Let

`E: y^2=(x-e1)(x-e2)(x-e3)`, with `e1,e2,e3 in Z[t]`,

be nonconstant. If `t0 in Q` has the property that for every nonconstant square-free divisor `h in Z[t]` of any of

- `(e1-e2)(e1-e3)`,
- `(e2-e1)(e2-e3)`,
- `(e3-e1)(e3-e2)`,

the rational number `h(t0)` is not a square in `Q`, then specialization

`E(Q(t)) -> E(t0)(Q)`

is injective.

Independent accessible restatement used to cross-check the exact criterion:
- theorem restatement in later literature: https://www.impan.pl/shop/publication/transaction/download/product/91685

## Credit boundary

These sources support only:
- the standard 2-isogeny descent/rank formula at a fixed rational specialization;
- the stated sufficient criterion for injective specialization.

All Stage36-specific polynomial identities, the complete `q0=6` divisor check, all modular/real obstructions, the explicit relative section, and the exact Kummer-image deductions are independently replayed by `verify_stage36_36_09N.py`.

No source here implies receiver emptiness, endpoint closure, a full Stage36 Selmer computation, or a perfect-cuboid theorem.
