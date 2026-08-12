# Stage15-6-cycle — 6an through 6aq

Base: merged previous cycle through Stage15-6am (`PR #843`, merge commit `e67258aa`).

This cycle starts at the small-`kappa` quartic theorem audit, closes the coordinate-core branch quantitatively at fixed norm core, and stops at the first remaining common norm-core aggregation theorem gate.

## Cycle path

```text
6an
  small-kappa quartic is not geometrically moving
  -> exact universal Qbar model Y^2=P^4-Q^4
  -> binary quartic I=12k^2, J=0, geometric j=1728
  -> identify uniform degree-4 projective-curve theorem species

6ao
  exact coordinate squareclass split
  -> two quadrics in ordinary P3
  -> projective height H << k^(1/4) Z^(1/2)
  -> apply Heath-Brown uniform degree-4 curve bound
  -> one-state fixed-kappa count << B^epsilon k^(1/8) Z^(1/4)

6ap
  couple z,w over the same kappa without multiplying #kappa
  -> Cauchy from L-infinity fiber bound + L1 host mass
  -> fixed-k dyadic count << B^epsilon k^(1/8)(ZW)^(5/8)
  -> using kZW<=2B: << B^(5/8+epsilon) k^(-1/2)
  -> coordinate-core dichotomy quantitatively closed at fixed k

6aq
  audit remaining norm-core k aggregation
  -> allowed k values are not B^o(1)
  -> naive sum k^(-1/2) has polynomial cost
  -> old AR-009 norm-core modulus cannot be recharged
  -> Stage14-sH48 is structural guidance, not direct saving
  -> targeted future routes: same-point norm/product correlation or explicit j=1728 twist-height adapter
  -> stop
```

## Main advance

The formerly unresolved small-coordinate-core branch has a pointwise arithmetic count. The key fixed-`k` estimate is

\[
\boxed{
N_k(Z,W)
\ll_\varepsilon
B^\varepsilon k^{1/8}(ZW)^{5/8}
\le
B^{5/8+\varepsilon}k^{-1/2}.
}
\]

This is a causal-mechanism estimate derived from the exact Stage15 Gaussian receiver. It does not reproduce the whole-family Stage15-5 half-power theorem.

## Cycle stop

The remaining obstruction is no longer:

- an unknown quartic geometry;
- a singular/conic branch;
- an uncounted `kappa=1` branch;
- an average-to-pointwise theorem mismatch.

It is the single arithmetic gate

```text
common Gaussian norm-core k
-> aggregate every k under the product height
-> without recharging its old root-line information
-> without paying polynomial #k cost.
```

## Frozen cycle exit

```text
STAGE15_6_CYCLE_START=6an
STAGE15_6_CYCLE_END=6aq
STAGE15_6_CYCLE_SMALL_KAPPA_ISOTRIVIAL_J1728=true
STAGE15_6_CYCLE_UNIFORM_DEGREE4_THEOREM_APPLIED=true
STAGE15_6_CYCLE_SMALL_KAPPA_FIXED_K_COUNT_PROVED=true
STAGE15_6_CYCLE_FIXED_K_SMALL_KAPPA_EXPONENT=5/8
STAGE15_6_CYCLE_COORDINATE_CORE_OBSTRUCTION_CLOSED_AT_FIXED_k=true
STAGE15_6_CYCLE_NORM_CORE_GLOBAL_AGGREGATION_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=J1728_TWIST_HEIGHT_OR_NORM_CORE_CORRELATION_THEOREM_GATE
```

A future continuation should begin only by proving one of the two exact adapters named at the exit. It should not restart generic genus-one theorem search or recharge `k` as a fresh AR-009 modulus.
