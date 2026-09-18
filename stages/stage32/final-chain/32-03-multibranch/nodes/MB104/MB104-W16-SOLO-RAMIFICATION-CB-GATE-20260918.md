# Stage32 MB104 — W16 solo: canonical CB cluster via normalization ramification — 2026-09-18

Status: **W16 NARROWED / EXACT O(l) NORMALIZATION CANDIDATE FOUND / SURFACE DESCENT OPEN / NO MATHEMATICAL CREDIT**

## Scope

This checkpoint advances W16 only.

The Hartshorne–Serre package under consideration is

`0 -> O_S(K) -> E -> I_Z(D_l) -> 0`.

For local freeness, `Z` must be a zero-dimensional lci Cayley–Bacharach scheme for `|D_l|`. Its Chern data are

`c1(E)=D_l+K`,
`c2(E)=K.D_l+length(Z)=112l+length(Z)`.

Hence

`c1(E)^2-4c2(E)=(D_l-K)^2-4 length(Z)`

with

`(D_l-K)^2=336l^2-224l+16`.

A source-complete cluster with `length(Z)<=112l` would therefore give

`>=336l^2-672l+16`,

which is positive for every `l>=2`.

Source for the Serre/CB criterion: Huybrechts–Lehn, The Geometry of Moduli Spaces of Sheaves, Theorem 5.1.1 / standard Hartshorne–Serre correspondence.

## 1. Existing canonical conductor schemes are too large

The full normalization defect is

`Delta=168l^2+56l`.

Using the whole conductor/genus-defect package as `Z` gives

`(D_l-K)^2-4Delta = -336l^2-448l+16 <0`.

So the source-complete full conductor package remains on the wrong side of Bogomolov instability.

The retained even-`l` norm-form conductor scheme is smaller but still quadratic. In the `e=2` candidate eigensection framework,

`length Z_res = y/2 >=84l^2`

by the retained split-Hodge lower bound. Therefore even its best possible discriminant satisfies

`(D_l-K)^2-4 length Z_res <=16-224l<0`.

Thus the currently materialized intrinsic conductor/base-locus schemes cannot realize W16.

## 2. A universal linear-size object does exist on the normalization

The retained residual-sheet construction gives, in both surviving `e` cases, a degree-`56l` residual base map

`phi:E -> P1`

from the elliptic normalization.

Riemann–Hurwitz on `g(E)=1` gives the ramification divisor

`R_phi`

with

`deg R_phi = 2 deg(phi) =112l`.

This is exactly the W16 target length.

So the numerical part of W16 is not speculative: every hypothetical carrier carries a canonical normalization-side divisor of precisely the right linear size.

## 3. Why the ramification divisor does not yet give a Serre scheme on S

The carrier `C` is a Cartier divisor on the smooth surface `S`, hence Gorenstein, with

`omega_C ~= (K_S+C)|_C`.

Let `nu:E->C` be its normalization. The conductor divisor `A_cond` on `E` satisfies the standard normalization duality formula

`omega_E ~= nu^*omega_C tensor O_E(-A_cond)`.

Since `g(E)=1`,

`deg A_cond = deg omega_C = D_l^2+K.D_l =336l^2+112l =2Delta`.

For the finite residual-base map on the singular carrier, the canonical different/ramification line is

`omega_C tensor f^*omega_P1^(-1)`.

After pullback to the normalization this becomes

`O_E(A_cond+R_phi)`.

Hence its degree is

`(336l^2+112l)+112l =336l^2+224l`.

This matches the standard different formula for a finite generically étale Gorenstein map. See Stacks Project, Section 49.16, especially Remark 49.16.3.

Therefore the canonical descended ramification object on the singular carrier is quadratic. The desired small divisor `R_phi` appears only **after subtracting the conductor divisor on the normalization**.

No retained source-complete construction performs that subtraction and produces a zero-dimensional lci subscheme

`Z_l subset S`

of length `112l`.

Pushforward of the divisor on `E` as a zero-cycle is not enough: several normalization points may map to one singular point, and the Serre construction needs an actual lci scheme on the smooth surface with a verified CB property.

## 4. Complete-intersection CB constructions are tautological

There is also a general split wall. Suppose a CB scheme is obtained as a complete intersection

`Z=A cap B`

with

`A+B=D_l-K`.

The Koszul resolution, twisted by `D_l`, gives the Hartshorne–Serre bundle explicitly as

`O_S(K+A) direct_sum O_S(K+B)`.

So complete-intersection constructions that obtain CB automatically are decomposable and do not provide the non-tautological instability package W16 needs.

This subsumes the earlier split/ambient-cut failure: simply cutting the carrier packet with an ambient divisor is not enough.

## 5. W16 solo conclusion

W16 is **not** closed negatively.

It has been narrowed to one exact missing bridge:

`normalization ramification R_phi (length 112l)`
` -> conductor-subtracted descent to a surface lci scheme Z_l`
` -> CB(|D_l|)`
` -> Hartshorne–Serre/Bogomolov instability`.

The first object is now exact and universal. The second arrow is absent.

Thus

`W16 = SURVIVES_ONLY_AS_RAMIFICATION_TO_CB_DESCENT`.

## Post-solo comparison

- `W4`: closed negatively.
- `W5`: explicit order two exhausted; genuinely primitive/twisted higher order remains open.
- `W20`: finite-E[2] bridge closed negatively; branch-specific conductor descent remains a different route.
- `W16`: exact linear-size candidate exists and the remaining obstruction is a specific descent/CB theorem.

On current evidence W16 is the most concrete next route to continue. This is research routing, not mathematical credit.

## Firewalls

- No ramification divisor on the normalization is silently treated as a subscheme of `S`.
- No CB property is asserted for `R_phi`.
- No `l>=2` exclusion is proved.
- No MB104 completion, finite window, receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
