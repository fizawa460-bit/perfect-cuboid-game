# Goal4AG bounded principalization degree exclusion — source lock

This leaf is a **bounded principalization exclusion only** for the second open-receiver class-B `Q(i)/Q` cyclic target. It does not materialize `F_B`, prove the target globally non-principal, compute the full algebraic Brauer group, or prove E1.

## Exact parent and target

Parent authority schema:
`STAGE35_EX_PESCH_E1_STATE_V69_GOAL4AF_C5_MARKED_PICARD_ADAPTER_COMPUTED_TARGET_SPAN_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT`.

The retained Goal4AA/4Z target has 69 nonzero formal support coefficients. The positive and negative effective parts both have hyperplane degree `396`, while the surface hyperplane class satisfies `H^2=16`. Therefore a homogeneous numerator/denominator realization has degree at least `ceil(396/16)=25`.

## Exact diagnostics

Source head: `8bed9082aeeb893b3c34c5fc0da4103415d215f1`.

Degree-25 residual diagnostic:
- workflow run `34076057541`
- job `101602278476`
- conclusion `SUCCESS`
- degree-25 residual: `H.R=4`, `R^2=-6780`
- retained C2/C3 or two-C1 plus nonnegative exceptional completion matches: `0`
- this subtest is not global degree-25 exhaustion.

Fixed-component stripping generation 2:
- workflow run `34076057633`
- job `101602278686`
- conclusion `SUCCESS`
- diagnostic blob `8a3dbd418d650f6d5454482678aa91e6d6e62fe1`
- exact tested range `25..128`.

The stripping rule is fail-closed: if an effective divisor has negative intersection with a retained irreducible curve, that curve is a forced fixed component. Forced components are removed deterministically. `H` is nef; once the residual has negative `H`-degree it is noneffective. The computation proves noneffectivity for degrees `25,26,27,28,29,30`.

Degree `31` is the first residual on which the retained-curve negative-intersection test stops: its stripped residual has `H`-degree `96` and square `212`, and is nef only against the retained 140-curve packet. This means **the test survives**, not that the residual is effective and not that a principal function exists.

## Exact conclusion

The homogeneous principalization route is excluded through degree `30`. General principalization remains open from degree `31` onward. The generation-2 sweep through degree `128` does not alter that boundary because every tested degree `31..128` survives the retained-curve test rather than being proved effective or principal.

## Credit firewall

The following remain false: hostile-audit pass; explicit `F_B`; global non-principality; all-degree exhaustion; degree-31 effectivity; general principal-function closure; full `Br_a(U)`; local evaluation; verticality; Brauer-Manin obstruction; E1; R29-PESCH-E1; R29-FIB2; Stage35 closure; perfect-cuboid existence/nonexistence.
