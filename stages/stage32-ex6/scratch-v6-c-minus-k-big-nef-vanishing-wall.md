# Stage32EX6 scratch — V6 `C-K` big / nef / vanishing wall

Status: `SCRATCH_EXACT_BOUNDED_V6_C_MINUS_K_BIG_NEF_UNRESOLVED_VANISHING_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

Repo / EX6:

- PR #1715 operational head inspected in this batch: `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- `stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md` retains the exact V6 resolved self-intersection `C^2=758`.
- `stages/stage32/residual-32-01-production/post1648at-intermediate-quotient-blowup-conductor-source-note.md` retains `K_S.C=186`, and equivalently the V6 strict-transform arithmetic genus `p_a(C)=473`.

External source lock:

- M. Stoll, D. Testa, *The surface parametrizing cuboids*, updated manuscript / 2026 accepted version. On the minimal desingularization `S`, `K_S` is the pullback of the hyperplane section, `K_S^2=16`, `chi(O_S)=8`, `p_g=7`, `q=0`, and the canonical map is a morphism contracting exactly the 48 exceptional curves before the box embedding. In particular `K_S` is base-point-free and hence nef.

A bounded repository/Arsenal search in this batch found no retained effective-cone/Mori-cone generator theorem or V6-specific nef certificate. This is a bounded discovery statement, not a repository-wide absence claim.

The updated Stoll--Testa manuscript also exhibits negative-self-intersection genus-3 curves outside the cone spanned by the classical 140 curves `G`. Therefore the fact that `G` generates `Pic(S)` does not authorize using nonnegative intersection with only those 140 curves as a nefness certificate.

## 1. Exact Riemann--Roch relation for the V6 carrier class

Write `K=K_S`.

For the hypothetical integral V6 carrier class `C`, retained arithmetic gives

`C^2=758`, `K.C=186`.

Surface Riemann--Roch gives

`chi(O_S(C)) = chi(O_S) + (C.(C-K))/2`
`              = 8 + (758-186)/2`
`              = 294`.

By Serre duality,

`h2(O_S(C)) = h0(O_S(K-C))`.

But

`K.(K-C)=16-186=-170`.

Because `K` is nef, every effective divisor has nonnegative intersection with `K`; hence `K-C` cannot be effective. Therefore

`h2(O_S(C))=0`.

Consequently the exact relation is

`h0(O_S(C)) - h1(O_S(C)) = 294`,

and in particular

`h0(O_S(C)) >= 294`.

The previous lower bound is thus source-locked directly by RR plus canonical nefness, but equality still requires `h1=0`.

## 2. The adjoint difference `D=C-K` is effective

Define

`D := C-K`.

Then

`D^2 = C^2 - 2K.C + K^2`
`    = 758 - 372 + 16`
`    = 402`,

and

`D.K = C.K-K^2 = 186-16 = 170`.

Riemann--Roch gives

`chi(O_S(D)) = 8 + (D.(D-K))/2`
`             = 8 + (402-170)/2`
`             = 124`.

Again by Serre duality,

`h2(O_S(D)) = h0(O_S(K-D)) = h0(O_S(2K-C))`.

But

`K.(2K-C)=32-186=-154`,

so nefness of `K` excludes effectivity of `2K-C`. Thus

`h2(O_S(D))=0`.

Hence

`h0(O_S(D)) = 124 + h1(O_S(D)) >=124`.

Therefore `D=C-K` is not merely a positive numerical class: it is an effective divisor class, with at least 124 global sections.

## 3. `D=C-K` is big

For every integer `n>=1`,

`K.(K-nD)=16-170n<0`.

Nefness of `K` therefore gives

`h2(O_S(nD))=h0(O_S(K-nD))=0`.

Riemann--Roch yields

`chi(O_S(nD))`
` = 8 + (n^2 D^2 - n D.K)/2`
` = 8 + 201 n^2 - 85 n`.

Since `h1>=0` and `h2=0`,

`h0(O_S(nD)) >= 8 + 201 n^2 - 85 n`.

Thus `h0(nD)` has quadratic growth and

`kappa(D)=2`.

So

`C-K` is **big**.

## 4. The exact remaining vanishing blocker is nefness

Kawamata--Viehweg would give

`H^i(S,O_S(K+D))=0` for `i>0`

if `D=C-K` were nef and big. Because `K+D=C`, this would imply

`h1(O_S(C))=0`

and hence the exact linear-system dimension

`h0(O_S(C))=294`, `dim |C|=293`.

Bigness is now proved, but nefness is not.

Some obvious tests are nonnegative under the hypothetical carrier semantics: for each exceptional curve `E_i`, `K.E_i=0` and `D.E_i=C.E_i>=0`. These tests do not determine the full nef cone.

The classical 140 Stoll--Testa curves cannot be treated as a Mori-cone generating set merely because they generate `Pic(S)`: the updated manuscript contains additional negative-self-intersection genus-3 curves outside their cone. Therefore a finite 140-curve intersection replay would not certify nefness.

No retained theorem inspected in this bounded batch proves that all negative curves, all Mori extremal rays, or the relevant Zariski negative part are exhausted by a finite tested set. Accordingly

`D=C-K NEF`

remains unresolved.

## 5. Decision

Canonical scratch decisions:

- `SURFACE_K_SQUARED = 16`;
- `SURFACE_CHI_O = 8`;
- `SURFACE_CANONICAL_NEF = true`;
- `V6_C_SQUARED = 758`;
- `V6_K_DOT_C = 186`;
- `CHI_O_C = 294`;
- `H2_O_C = 0`;
- `H0_O_C_MINUS_H1_O_C = 294`;
- `H0_O_C_LOWER_BOUND = 294`;
- `D_EQUALS_C_MINUS_K_SQUARED = 402`;
- `D_DOT_K = 170`;
- `CHI_O_D = 124`;
- `H2_O_D = 0`;
- `H0_O_D_LOWER_BOUND = 124`;
- `C_MINUS_K_EFFECTIVE = true`;
- `C_MINUS_K_BIG = true`;
- `C_MINUS_K_NEF = UNRESOLVED`;
- `CLASSICAL_140_CURVES_GENERATE_PICARD_NOT_CERTIFIED_MORI_CONE = true`;
- `KAWAMATA_VIEHWEG_FOR_O_C = NOT_AUTHORIZED`;
- `H1_O_C_ZERO = UNPROVEN`;
- `H0_O_C_EQUALS_294 = UNPROVEN`;
- `EXACT_V6_LINEAR_SYSTEM_DIMENSION_293 = UNPROVEN`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Re-entry

The adjoint/linear-system route has been reduced to one genuinely geometric missing input. Useful re-entry would be one of:

1. a complete nef/Mori-cone certificate sufficient for the specific class `C-K`;
2. a V6-specific decomposition of `C-K` as a nonnegative sum of known nef/base-point-free classes;
3. a Zariski-decomposition theorem showing the negative part is zero;
4. or a direct cohomological argument proving `H1(S,O_S(C))=0` without nefness of `C-K`.

Absent such an input, `effective + big` cannot be promoted to Kawamata--Viehweg vanishing.

## Firewalls

- Positive square and positive canonical degree do not imply nefness.
- Picard generation by 140 curves does not imply effective-cone or Mori-cone generation by those curves.
- `h0(C)>=294` is not `h0(C)=294`.
- No scratch result here is MAIN authority or endpoint credit.
