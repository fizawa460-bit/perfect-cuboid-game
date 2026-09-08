# Stage32EX6 scratch — V6 nef obstruction / fixed-part / canonical-restriction cohomology wall

Status: `SCRATCH_EXACT_BOUNDED_V6_NEF_OBSTRUCTION_FIXED_PART_COHOMOLOGY_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks and inherited exact input

Operational/source scope in this batch:

- PR #1715 inspected at exact head `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- preceding scratch leaf `stages/stage32-ex6/scratch-v6-c-minus-k-big-nef-vanishing-wall.md`, exact parent scratch head `a9dc14d579c88339b705b2594ea6bca03bf5926a`;
- retained V6 arithmetic source `stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md` for `C^2=758`;
- retained source `stages/stage32/residual-32-01-production/post1648at-intermediate-quotient-blowup-conductor-source-note.md` for `K_S.C=186` and `p_a(C)=473`;
- Stoll--Testa cuboid-surface geometry as source-locked in the preceding scratch leaf: on the minimal desingularization `S`, `K:=K_S` is base-point-free/nef, `K^2=16`, `chi(O_S)=8`, and the canonical morphism contracts exactly the 48 exceptional curves.

The preceding scratch leaf proved, for

`D := C-K`,

- `D^2=402`;
- `D.K=170`;
- `chi(O_S(D))=124`;
- `h^2(O_S(D))=0`;
- `h^0(O_S(D))>=124`, hence `D` is effective;
- `D` is big;
- `D` nef remains unresolved.

A bounded current-branch search did not surface a V6-specific decomposition of `D` into known nef/base-point-free classes. This is a bounded discovery statement only, not a repository-wide absence claim.

## 1. A general canonical section gives an exact 170-dimensional restriction budget

Because `|K|` is base-point-free, choose a general smooth canonical member

`H in |K|`.

Adjunction gives

`g(H) = 1 + (H^2 + K.H)/2`
`     = 1 + (16+16)/2`
`     = 17`.

The V6 class has

`deg O_H(C) = C.H = C.K = 186`.

Since

`186 > 2g(H)-2 = 32`,

Serre duality on `H` gives

`H^1(H,O_H(C))=0`.

Riemann--Roch on the genus-17 curve therefore gives

`h^0(H,O_H(C)) = 186 + 1 - 17 = 170`.

Now use

`0 -> O_S(C-K) -> O_S(C) -> O_H(C) -> 0`,

i.e.

`0 -> O_S(D) -> O_S(C) -> O_H(C) -> 0`.

The preceding scratch leaf gives `h^2(D)=0`; the same leaf also gives `h^2(C)=0`. Since `h^1(O_H(C))=0`, the relevant long exact sequence is

`0 -> H0(D) -> H0(C) -> H0(H,C) -> H1(D) -> H1(C) -> 0`.

The Euler-characteristic jump is exactly

`chi(C)-chi(D)=294-124=170`,

which equals `h^0(H,O_H(C))`.

Thus the canonical restriction step is exactly numerically balanced: there is no hidden Euler-characteristic surplus available for a vanishing contradiction.

In particular,

`H^1(C)` is a quotient of `H^1(D)`,

so

`h^1(C) <= h^1(D)`.

Therefore a direct proof `H^1(D)=0` would imply `H^1(C)=0` and recover

`h^0(C)=294`, `dim |C|=293`

without first proving `D` nef.

Conversely, `H^1(D)` need not vanish merely because the canonical restriction space has dimension 170: the connecting map

`H^0(H,O_H(C)) -> H^1(D)`

can absorb part or all of the special cohomology.

## 2. Any failure of nefness is a genuine negative fixed component

Assume `D` is not nef. Then there is an irreducible curve `R` with

`D.R < 0`.

Because `D` is effective, every effective divisor representing `D` must contain `R`: if an effective representative did not contain `R`, its intersection with `R` would be nonnegative. Hence `R` is a fixed component of `|D|`.

Write an effective representative as

`D_eff = a R + D'`, `a>=1`,

with `D'` effective and not containing `R`. Since `D'.R>=0` and `D.R<0`, necessarily

`R^2<0`.

The obstruction cannot be one of the 48 canonical exceptional curves. For such an exceptional curve `E`, `K.E=0` and the hypothetical integral carrier `C` is a distinct effective irreducible curve, so

`D.E=C.E>=0`.

Since the canonical morphism contracts exactly those 48 curves, every non-nef obstruction `R` satisfies

`K.R>0`.

Define the positive integers

`k := K.R`,
`r := -D.R`.

Because `C=D+K` and `C` and `R` are distinct effective irreducible curves,

`C.R >=0`.

Therefore

`C.R = k-r >=0`,

so

`1 <= r <= k`.

Adjunction on `R` gives

`R^2 + K.R = 2p_a(R)-2`,

hence

`R^2 = 2p_a(R)-2-k <0`.

Equivalently,

`k >= 2p_a(R)-1`.

Thus non-nefness is no longer an abstract cone statement: it requires a negative fixed curve with the exact integer profile

`(k,r,p_a(R))`,

where

- `k>0`;
- `1<=r<=k`;
- `C.R=k-r`;
- `R^2=2p_a(R)-2-k<0`.

## 3. Low-canonical-degree non-nef obstructions carry an exact H1 penalty

Because `R` is fixed in `|D|`, subtraction of one copy does not change the section space:

`h^0(D-R)=h^0(D)`.

For `k<154`, Serre duality gives

`h^2(D-R) = h^0(K-(D-R))`
`          = h^0(2K-C+R)`.

Its canonical degree is

`K.(2K-C+R)`
` = 2K^2-K.C+K.R`
` = 32-186+k`
` = k-154 <0`.

Since `K` is nef, `2K-C+R` cannot be effective. Therefore

`h^2(D-R)=0` for every such obstruction with `k<154`.

Surface Riemann--Roch gives

`chi(D)-chi(D-R)`
` = D.R - (R^2+K.R)/2`
` = -r -(p_a(R)-1)`
` = 1-p_a(R)-r`.

Thus

`chi(D-R)=chi(D)+r+p_a(R)-1`.

Using

`h^0(D-R)=h^0(D)`

and

`h^2(D-R)=h^2(D)=0`,

we obtain the exact special-cohomology identity

`h^1(D)-h^1(D-R)=r+p_a(R)-1`.

Hence every non-nef obstruction with `k<154` forces

`h^1(D) >= r+p_a(R)-1`.

This is a genuine cohomological price for low-canonical-degree fixed negativity.

In particular, if one could prove `h^1(D)=0` independently, then every `k<154` non-nef obstruction would be excluded except the unique numerical residual species

`p_a(R)=0`, `r=1`.

Indeed `r>=1`, `p_a(R)>=0`, so

`r+p_a(R)-1=0`

occurs only for that rational one-unit case. For it,

`R^2=-k-2`,
`D.R=-1`,
`C.R=k-1`.

Thus even a direct `H^1(D)=0` theorem would reduce, rather than automatically prove, nefness: the rational `r=1` fixed-curve species remains a separate geometric possibility.

## 4. Relation to the desired V6 linear-system dimension

The canonical restriction exact sequence gives a second useful ceiling on what special cohomology can do.

Let

`rho := rank(H^0(C) -> H^0(H,O_H(C)))`,

so `0<=rho<=170`. Then exactness gives

`h^0(C)=h^0(D)+rho`

and

`h^1(C)=h^1(D)-(170-rho)`.

Thus

`h^1(C) >= h^1(D)-170`.

Consequently a low-degree fixed obstruction with

`r+p_a(R)-1 >170`

would force `h^1(C)>0`.

This is not an endpoint contradiction: `h^1(C)>0` is allowed by current authority and simply raises `h^0(C)` above the RR baseline 294. It does, however, identify the exact channel by which a non-nef fixed part can survive the canonical restriction step.

## 5. Decision

Canonical scratch decisions:

- `GENERAL_CANONICAL_SECTION_GENUS = 17`;
- `V6_RESTRICTION_TO_CANONICAL_DEGREE = 186`;
- `CANONICAL_RESTRICTION_H1 = 0`;
- `CANONICAL_RESTRICTION_H0 = 170`;
- `CHI_C_MINUS_CHI_C_MINUS_K = 170`;
- `CANONICAL_RESTRICTION_EULER_BUDGET_EXACTLY_BALANCED = true`;
- `H1_C_IS_QUOTIENT_OF_H1_C_MINUS_K = true`;
- `H1_C_MINUS_K_ZERO_IMPLIES_H1_C_ZERO = true`;
- `DIRECT_H1_C_MINUS_K_ROUTE_BYPASSES_NEFNESS_FOR_VANISHING = true`;
- `NONNEF_OBSTRUCTION_IS_FIXED_COMPONENT_OF_C_MINUS_K = true`;
- `NONNEF_OBSTRUCTION_HAS_NEGATIVE_SELF_INTERSECTION = true`;
- `NONNEF_OBSTRUCTION_IS_CANONICAL_EXCEPTIONAL = false`;
- `NONNEF_OBSTRUCTION_K_DOT_R_POSITIVE = true`;
- `NONNEF_PROFILE_C_DOT_R = k-r`;
- `NONNEF_PROFILE_1_LE_R_LE_K = true`;
- `NONNEF_PROFILE_R_SQUARED = 2PA_MINUS_2_MINUS_K`;
- `LOW_K_THRESHOLD_FOR_H2_D_MINUS_R_ZERO = 154`;
- `LOW_K_FIXED_COMPONENT_H1_PENALTY = r_plus_pa_minus_1`;
- `H1_D_ZERO_LEAVES_ONLY_LOW_K_RATIONAL_R1_NUMERICAL_SPECIES = true`;
- `C_MINUS_K_NEF = UNRESOLVED`;
- `H1_O_C_MINUS_K_ZERO = UNPROVEN`;
- `H1_O_C_ZERO = UNPROVEN`;
- `H0_O_C_EQUALS_294 = UNPROVEN`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Re-entry

The V6 positivity/linear-system route is now reduced to more concrete alternatives:

1. classify or exclude negative fixed curves `R` with the profile above, especially the low-`k` rational `r=1` residual species;
2. prove `H^1(S,O_S(C-K))=0` directly, without nefness;
3. prove that the connecting map `H^0(H,O_H(C)) -> H^1(C-K)` is surjective, which is enough for `H^1(C)=0` even when `H^1(C-K)` is nonzero;
4. obtain a V6-specific nef decomposition/certificate for `C-K`;
5. or source-lock enough of the negative/Mori cone to test only the exact obstruction profile instead of all divisor classes.

No current item closes O266.

## Firewalls

- `D=C-K` effective and big does not imply nef.
- A negative fixed component in `|D|` is not automatically a fixed component of `|C|`.
- `h^1(D)>0` does not imply `h^1(C)>0`; the 170-dimensional canonical restriction connecting map can kill special cohomology.
- `h^1(D)=0` would prove the desired vanishing for `C`, but would not by itself prove `D` nef because the rational `r=1` low-`k` numerical species has zero cohomological penalty.
- No scratch result here is MAIN authority or endpoint credit.