# Stage14-t103 — common elementary boundary skeleton across generic mover primes

## Status

`COMPLETE_COMMON_ELEMENTARY_BOUNDARY_SKELETON_PRIME_INCIDENCE_REDUCTION`

Consumes merged Stage14-t102, merged Stage14-Work-biX21, merged Stage14-t101/t100/t98, and completed frozen Stage14-tH27. No H snapshot is reopened or refined. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Packet-wide elementary boundary dictionary

Fix one live square-root-saturating fixed-U packet. Let

```text
P_G = {generic split-prime orientation bits},
r = |P_G| = omega(delta_G)=B^o(1).
```

Merged t98 decomposes every generic-prime physical symmetric difference into elementary tests of three types. Once the packet is fixed, their **selector labels** lie in one packet-wide dictionary

```text
E_U = E_SIGN union E_DIV union E_PROJ
```

independent of the selected prime `p`.

- SIGN: one of `O(1)` fixed sign/order reconstruction functionals. For a fixed label `e`, t100 gives fixed integral linear forms `S_e,D_e`; only the Gaussian coefficients `(A_p,B_p)` vary with `p`.
- DIV: one fixed reconstruction functional and one packet divisor `q|A0*B0`. The divisor set is divisor-many, hence `B^o(1)` labels. The modulus itself is **not** asserted small.
- PROJ: one packet-fixed endpoint projective acceptance test modulo the fixed conductor `d=B^o(1)`.

Therefore

```text
|E_U|=B^o(1).
```

```text
PACKET_WIDE_ELEMENTARY_BOUNDARY_DICTIONARY_PROVED=true
PACKET_WIDE_ELEMENTARY_BOUNDARY_DICTIONARY_SIZE=Bo1
DIV_MODULUS_FORCED_SMALL=false
```

## 2. Double pigeonhole to one common selector skeleton

For `p in P_G`, let

```text
I_p = Inf_p(f)
```

be the exact prime influence. For `e in E_U`, let `b_{p,e}(x)` be the corresponding `0/1` elementary boundary event and

```text
J_{p,e}=E_x b_{p,e}(x).
```

The t98 union decomposition gives

```text
I_p <= sum_{e in E_U} J_{p,e}.
```

Merged t102 proves, on every live square-root-saturating packet,

```text
I_bar := (1/r) sum_p I_p = B^(-o(1))
```

in the lower-bound/exponent-zero sense. Hence

```text
I_bar
 <= sum_{e in E_U} (1/r) sum_p J_{p,e}.
```

Because `|E_U|=B^o(1)`, there is one packet-wide label `e_*` with

```text
J_bar(e_*) := (1/r) sum_p J_{p,e_*}
            >= I_bar/|E_U|
            = B^(-o(1)).
```

Thus the square-root survivor cannot hide the entire mover mass in unrelated elementary selectors prime by prime: one **common elementary boundary skeleton** carries exponent-zero prime-average incidence.

This improves the t102 lock only in the selector-skeleton sense. The prime action coefficients may still vary.

```text
COMMON_ELEMENTARY_BOUNDARY_SKELETON_ACROSS_PRIMES_PROVED=true
COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ACROSS_PRIMES_PROVED=false
COMMON_ELEMENTARY_BOUNDARY_PRIME_AVERAGE_EXPONENT_ZERO=true
```

## 3. The three common-skeleton realizations

### SIGN

For one fixed SIGN label, t100 gives fixed forms `S,D`. Writing the p-primary Gaussian factor as

```text
varpi_p^e=A_p+iB_p,
```

the boundary is

```text
A_p^2 S(x)^2-B_p^2 D(x)^2 < 0.
```

Away from ties this is

```text
|S(x)/D(x)| < |B_p/A_p|.
```

So the state statistic `|S/D|` is fixed and all prime dependence is the single Gaussian slope parameter

```text
t_p=|B_p/A_p|.
```

```text
COMMON_SIGN_FORMS_FIXED_ACROSS_PRIMES=true
SIGN_PRIME_DEPENDENCE_REDUCED_TO_GAUSSIAN_SLOPE_PARAMETER=true
```

### DIV

For one fixed DIV label, `q,S,D` are fixed and

```text
L_{p,+}=A_p S+B_p D,
L_{p,-}=A_p S-B_p D.
```

The event is

```text
1_{q|L_{p,+}} xor 1_{q|L_{p,-}}.
```

Genericity excludes the packet exceptional support, so `(A_p,B_p)` is primitive modulo every prime factor of the fixed packet divisor `q`. Thus the varying prime acts only through its primitive residue/projective class modulo this one common `q`.

```text
COMMON_DIV_MODULUS_AND_FORMS_FIXED_ACROSS_PRIMES=true
DIV_PRIME_DEPENDENCE_REDUCED_TO_PRIMITIVE_RESIDUE_ACTION_MOD_Q=true
```

No `1/q` saving is claimed.

### PROJ

For one fixed endpoint label, the modulus `d` and acceptance set `C_d` are fixed. Prime `p` contributes only its orientation-switch action `tau_p`, and the event is

```text
1_{z in C_d} xor 1_{tau_p z in C_d}.
```

```text
COMMON_PROJ_MODULUS_AND_ACCEPTANCE_SET_FIXED_ACROSS_PRIMES=true
PROJ_PRIME_DEPENDENCE_REDUCED_TO_FINITE_PROJECTIVE_ACTION=true
```

## 4. Common-skeleton mover support and energy

For the selected skeleton define

```text
rho_p := J_{p,e_*},
rho_bar := (1/r) sum_p rho_p.
```

Then `rho_bar=B^(-o(1))` in the lower-bound sense. Since `0<=rho_p<=1`,

```text
P_*={p:rho_p>0}
```

satisfies

```text
|P_*|/r >= rho_bar = B^(-o(1)).
```

Jensen gives

```text
E_* := (1/r) sum_p rho_p^2
     >= rho_bar^2
     = B^(-o(1))
```

in the lower-bound/exponent-zero sense.

Also, for

```text
H_*={p:rho_p>=rho_bar/2},
```

one has

```text
|H_*|/r >= rho_bar/(2-rho_bar).
```

Hence the same elementary skeleton is active with density at least `B^(-o(1))` on an exponent-zero fraction of generic prime bits, and every prime in that heavy set has boundary density at least `B^(-o(1))`.

```text
COMMON_SKELETON_MOVER_PRIME_SUPPORT_DENSITY_EXPONENT_ZERO=true
COMMON_SKELETON_PRIME_ENERGY_EXPONENT_ZERO=true
COMMON_SKELETON_HEAVY_PRIME_FRACTION_EXPONENT_ZERO=true
```

These are three consequences of the same already-charged incidence mass and cannot be multiplied as independent savings.

## 5. Two-level principal/centered decomposition

Merged t101 centers every elementary boundary within each prime fiber. Set

```text
b_p(x)=b_{p,e_*}(x),
rho_p=E_x b_p(x),
rho_bar=E_p rho_p.
```

Then exactly

```text
b_p(x)
 = rho_bar
 + (rho_p-rho_bar)
 + (b_p(x)-rho_p).
```

with

```text
E_p(rho_p-rho_bar)=0,
E_x(b_p-rho_p)=0  for every p.
```

The Bernoulli incidence matrix obeys the exact total-variance identity

```text
E_{p,x}(b_p-rho_bar)^2
 = Var_p(rho_p)
 + E_p[rho_p(1-rho_p)].
```

Thus the common-skeleton obstruction splits into

```text
common principal prime-average density
+
centered between-prime density fluctuation
+
centered within-prime boundary discrepancy.
```

```text
TWO_LEVEL_PRIME_STATE_CENTERING_EXACT=true
TOTAL_VARIANCE_DECOMPOSITION_EXACT=true
```

## 6. Relation to Work-biX21

Merged Work-biX21 proves a common prime-support/energy skeleton between global and fixed-U routes, but not a common arithmetic adapter. Stage14-t103 advances only the fixed-U side by compressing the varying SIGN/DIV/PROJ incidences to one common selector skeleton.

It does not identify that skeleton with the global fixed-heavy-prime norm-ratio collision packet.

```text
WORK_BIX21_FIXED_U_COMMON_BOUNDARY_REQUIREMENT_ADVANCED=true
GLOBAL_FIXED_U_ARITHMETIC_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## 7. H decision

The receiver is materially cleaner but still not a new theorem-ready external average. Inside one fixed-U packet there are only

```text
r=B^o(1)
```

generic prime factors, and the action parameter still varies:

```text
SIGN: |B_p/A_p|,
DIV : (A_p,B_p) mod q,
PROJ: tau_p mod d.
```

No polynomial-length Gaussian-prime family, fixed common action parameter, or independent modulus average is proved. Therefore tH27 is not reopened and tH28 is not yet warranted.

```text
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
```

## 8. Frozen boundary

```text
STAGE14_T103=COMPLETE_COMMON_ELEMENTARY_BOUNDARY_SKELETON_PRIME_INCIDENCE_REDUCTION
MERGED_T102_CONSUMED=true
MERGED_WORK_BIX21_CONSUMED=true
PACKET_WIDE_ELEMENTARY_BOUNDARY_DICTIONARY_PROVED=true
PACKET_WIDE_ELEMENTARY_BOUNDARY_DICTIONARY_SIZE=Bo1
COMMON_ELEMENTARY_BOUNDARY_SKELETON_ACROSS_PRIMES_PROVED=true
COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ACROSS_PRIMES_PROVED=false
COMMON_ELEMENTARY_BOUNDARY_PRIME_AVERAGE_EXPONENT_ZERO=true
COMMON_SIGN_FORMS_FIXED_ACROSS_PRIMES=true
SIGN_PRIME_DEPENDENCE_REDUCED_TO_GAUSSIAN_SLOPE_PARAMETER=true
COMMON_DIV_MODULUS_AND_FORMS_FIXED_ACROSS_PRIMES=true
DIV_PRIME_DEPENDENCE_REDUCED_TO_PRIMITIVE_RESIDUE_ACTION_MOD_Q=true
COMMON_PROJ_MODULUS_AND_ACCEPTANCE_SET_FIXED_ACROSS_PRIMES=true
PROJ_PRIME_DEPENDENCE_REDUCED_TO_FINITE_PROJECTIVE_ACTION=true
COMMON_SKELETON_MOVER_PRIME_SUPPORT_DENSITY_EXPONENT_ZERO=true
COMMON_SKELETON_PRIME_ENERGY_EXPONENT_ZERO=true
COMMON_SKELETON_HEAVY_PRIME_FRACTION_EXPONENT_ZERO=true
TWO_LEVEL_PRIME_STATE_CENTERING_EXACT=true
TOTAL_VARIANCE_DECOMPOSITION_EXACT=true
GLOBAL_FIXED_U_ARITHMETIC_ADAPTER_PROVED=false
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFCommonElementaryBoundarySkeletonPrimeActionIncidenceWithTwoLevelCentering
NEXT=Stage14-t104
```
