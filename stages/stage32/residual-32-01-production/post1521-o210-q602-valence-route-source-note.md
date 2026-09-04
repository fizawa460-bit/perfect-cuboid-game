# Stage32 post-1521 O210/Q602 valence route

Scope: fixed Stage32 target `g1-d186`, `O=210`, correspondence `Gamma` on `C0 x C0`, with `g(C0)=2`, bidegree `(105,81)`, and hostile-audited necessary `Q(T)=602` / 18-value diagonal spectrum. This note selects a genuinely new scalar-coupling route after the audited post1520 retained-geometry test ended `18 -> 18`.

## Research OS / Arsenal precheck

Current Arsenal was checked by exact applicability before external literature work.

- `S34-W03` (`RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION`) requires an already source-locked branch `B`, extra receiver condition `K`, and an exact joint `B+K` test. It can consume a scalar condition but does not manufacture the missing predicate on `(Gamma,Delta)`.
- `S32-PW03` (`LATTICE_IMAGE_HNF_GATE`) requires an already source-locked exact observable map. It can gate a known scalar/observable image but does not create the missing geometry-to-scalar adapter.
- `S28-W04` (`COMMON_POLARIZATION_FIXED_CURVE_DIFFERENTIAL`) concerns the Stage19/20 K3 physical low-degree curve spectra and does not match the present genus-2 correspondence object.

Therefore there is no direct applicable Arsenal card for the missing weapon type `CORRESPONDENCE_GEOMETRY_TO_DIAGONAL_SCALAR`. This is a bounded routing conclusion, not an Arsenal-absence theorem.

## External source lock: valence

Source: Igor Dolgachev, *Topics in Classical Algebraic Geometry*, Section 5.5.1, Proposition 5.5.1 and Corollary 5.5.2 (Cayley-Brill formula). Public course copy/search surface: `https://mathweb.ucsd.edu/~eizadi/207A-14/CAG.pdf` (Section 5.5.1).

The source states that for a correspondence `R` of valence `nu` on a nonsingular curve `C`:

1. valence `nu` is equivalent to the induced Jacobian homomorphism `phi_R` being multiplication by `-nu`;
2. if `R` has type `(a,b)` on a genus-`g` curve, the number of united points, i.e. `R.Delta` counted with multiplicity, is

   `a + b + 2*nu*g`.

For the present Stage32 object, if `Gamma` has valence `nu in Z`, then

`T = -nu * id_J(C0)`

and, because `g(C0)=2` and `(a,b)=(105,81)`,

`(Gamma,Delta) = 105 + 81 + 4*nu = 186 + 4*nu`.

This is consistent with the already source-locked Stage32 trace identity

`Tr_Q(T) = 186 - (Gamma,Delta)`

because scalar multiplication by `-nu` on a genus-2 Jacobian has rational trace `-4*nu`.

## Conditional Q602 exclusion

The retained principal Rosati normalization is

`Tr_Q(T^dagger*T) = 2*Q(T)`.

Under the valence hypothesis, `T=-nu id`, hence `T^dagger*T=nu^2 id`. On the 4-dimensional rational first homology of a genus-2 Jacobian,

`Tr_Q(nu^2 id)=4*nu^2`.

Therefore

`Q(T)=2*nu^2`.

The required value `Q(T)=602` would force

`nu^2 = 301 = 7*43`,

which has no integral solution. Equivalently, applying the audited 18 diagonal values to `nu=((Gamma,Delta)-186)/4` gives

`nu in {-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17}`,

and none satisfies `2*nu^2=602`.

Thus:

**Conditional theorem:** if the actual Stage32 correspondence `Gamma` has integral valence, then `Q(T)=602` and therefore the fixed `O=210` carrier are excluded.

## What is NOT proved

This leaf does **not** prove that `Gamma` has valence. The Bolza/genus-2 Jacobian has extra endomorphisms, so valence cannot be inferred from genus alone or from bidegree alone. The next mathematical leaf is precisely to prove (or refute) valence for this specific `Gamma`, preferably from an exact symmetry/centralizer statement or from a direct source-locked divisor-class identity `Gamma + nu*Delta ~ vertical + horizontal`.

No geometric realization, no Q602/O210 exclusion, no O212+ authorization, and no receiver/route/theorem/endpoint/perfect-cuboid credit is promoted by this conditional route alone.
