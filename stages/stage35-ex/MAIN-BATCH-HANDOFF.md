# Stage35-EX MAIN batch handoff — Goal4BK fixed-i quartic dual and two-adic ray-class boundary

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BK are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BJ is exact-green:

- exact head: `ffbb6ee4864490113bfa551fb1e14614c30f5051`
- aggregate: `34312988913`
- `verify-stage35-ex-current`: `102344458981`
- result: `SUCCESS`

Goal4BJ constructed the source-canonical support-cleaned Gaussian carrier

```text
Xi=Xi_a*Xi_b*Xi_c
```

with selected-reservoir valuations `+1,-1,0` encoding `sigma=-1,+1,nonsecondary`, and proved that `[Xi]_4` retains the information while `[Xi]_2` does not.

## Goal4BK provisional exact result

The ambient Gaussian field already supplies a canonical order-four dual character. For odd primary Gaussian `alpha`, set

```text
chi_i(alpha)=(i/alpha)_4.
```

For `Xi=N/D`, extend multiplicatively by

```text
chi_i(Xi)=chi_i(N)*chi_i(D)^(-1).
```

At a selected prime `pi`, the local contribution is

```text
chi_i(pi)^(v_pi(Xi)).
```

When `chi_i(pi)` has order four this distinguishes the orientation exponent `+1` from `-1`.

The standard supplementary law for primary `alpha=A+B*i` is

```text
(i/alpha)_4=i^((1-A)/2).
```

Primary normalization fixes

```text
A odd, B even, A+B=1 mod 4,
```

but not `A mod 8`. Thus the fixed-unit character is not constant on the primary class. Ambient primary-prime diagnostics already give

```text
-1+2i  (N=5)  -> chi_i=i,
 3+2i  (N=13) -> chi_i=-i,
 1+4i  (N=17) -> chi_i=1.
```

These examples are not endpoint claims; they certify that primary normalization plus `ell=1 mod4` alone cannot fix the quartic value.

Hence the global odd-prime orientation product

```text
product chi_i(pi)^(v_pi(Xi))=chi_i(Xi)
```

is balanced by a deeper ramified `2`-adic/ray-class factor. Goal4BJ gives only

```text
Xi == 1 mod (1+i)^3,
```

which is insufficient to make that factor constant.

Natural complementary source cofactors do not yet repair this. In direction `a`, the exact secondary residue ratio is

```text
C_a^S/C_a^F == sigma_a*x*(a/ell^m)/c mod p_a,
```

with cyclic analogues. The normalization `a/ell^m` is prime-dependent, and the nonvanishing space cofactor itself depends on `sigma_a`, so no fixed global source second slot is obtained. BH Hensel leading units are likewise prime-local.

Exact route status:

```text
canonical fixed-i quartic dual = obtained;
local orientation sensitivity = yes;
chi_i(Xi) source-fixed constant = no;
primary congruence sufficient = no;
two-adic/ray-class compensator = remains;
natural cofactor fixed dual = not obtained;
global quartic contradiction = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bk-fixed-i-quartic-dual-two-adic-ray-class-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bk-fixed-i-quartic-dual-two-adic-ray-class.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bk_fixed_i_quartic_dual.py`

## Next exact leaf

```text
35EX-35_GOAL4BL_XI_TWO_ADIC_RAY_CLASS_PARITY_PREFLIGHT
```

Compute the source-canonical deeper `2`-adic/ray-class residue of `M_i^-/M_i^+` and `Xi` beyond primary normalization, using the three primitive parity branches and the face/space primary square-root units. Test whether `chi_i(Xi)` is forced. Only then can the fixed-unit quartic reciprocity identity become a nontrivial sigma relation.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
