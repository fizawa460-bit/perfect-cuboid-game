# Stage32 O210 rational character algebra / integral-index boundary source note

Scope: source-lock only the rational Neron-Severi character structure needed after the exact V220 lock `delta_D=2018`, `r_u+r_v+r_uv=377`. This note does **not** claim an integral NS(X) lattice, primitive embedding, Gaussian-integer order, or intersection-form scale.

## Beauville

Arnaud Beauville, *Some surfaces with maximal Picard number*, J. Ecole polytechnique — Math. 1 (2014), 101-116, DOI 10.5802/jep.5, arXiv:1310.3402v2, Section 5 Proposition 8 and proof.

Exact facts used:
- the curve `C` is the modular curve `X(8)`;
- `Gamma` is isomorphic to `(Z/2Z)^2` and acts freely on `C`;
- `H^0(C,K_C)=L+V`, with trivial `Gamma` action on `L` and `V` the sum of the three nontrivial one-dimensional characters;
- `NS((C x C)/Gamma) tensor Q = Q^2 + (End_Gamma(JC) tensor Q)`;
- `End_Gamma(JC) tensor Q = M2(Q(sqrt(-2))) x Q(i)^3`.

The last two statements are explicitly rational (`tensor Q`). They do not source-lock the integral index/order/primitive embedding of any nontrivial character lattice.

## Freitag–Salvati Manni

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495, Section 4.

Exact facts used:
- `Gamma'[4]/Gamma[8]` is isomorphic to `(Z/2Z)^2` and acts freely on the level-8 modular curve;
- the Beauville manifold is the diagonal quotient of the product of two level-8 modular curves by `Gamma'[4]`;
- the resolved two-fold map to the resolved box surface is ramified along the 48 exceptional divisors.

## Character bookkeeping

For `X=(C x C)/Gamma_diag`, the residual deck group `(Gamma x Gamma)/Gamma_diag` is naturally isomorphic to `Gamma`. In the cross-term of cohomology, diagonal invariants pair equal `Gamma` characters. Therefore each of the three nontrivial residual deck characters corresponds rationally to one of the three `Q(i)` factors in Beauville's `End_Gamma(JC) tensor Q`, giving a 2-dimensional rational NS contribution for each nontrivial character.

This is a rational representation-theoretic adapter only. No integral congruence stronger than the already locked `E_t^2=-8-16r_t` is promoted.
