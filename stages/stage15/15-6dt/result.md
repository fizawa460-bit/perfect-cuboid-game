# Stage15-6dt — same-measure Pell averaging test and Arsenal audit

Base: Stage15-6ds. The exact receiver is now a correlation of two Pell/unit orbits in the same field `K=Q(sqrt(k))`. Test whether this representation, after averaging over the reconstructed base triples and legal cores, yields a fixed-power saving on the **same physical measure**.

The target remains a genuine polynomial deficit, not a reduction of one `B^{o(1)}` multiplicity to another.

## 1. What the exact Pell decomposition actually counts

For fixed `(a,b,c,d,M,N,U,k)` the first norm has
\[
B^{o(1)}
\]
principal-ideal seeds and `O(log B)` physically bounded unit exponents per seed. Stage15-6da already charged this as one `B^{o(1)}` completion fiber.

The second norm selects those terms satisfying
\[
(b^2M L_{\nu,j})^2-kY^2=-C_2^2.
\]
Equivalently, after choosing a second Pell seed, one asks for intersections
\[
\operatorname{Re}(\zeta_{\mu,\ell})=b^2M\operatorname{Re}(\xi_{\nu,j}).
\]
For fixed two seed orbits the exponent ranges are only logarithmic. Even a theorem replacing `O(log B)` admissible intersections by `O(1)` would therefore improve only an already-charged `B^{o(1)}` fiber. By itself it would **not** produce a factor `B^{-delta}` in the outer reconstructed-base population.

A fixed-power gain must instead show that a polynomial fraction of base triples/cores admit **no** legal second-orbit intersection, uniformly in the full physical masks. No such statement follows from the pointwise Pell parametrization.

## 2. Norm-ideal averaging

The first and second seed sets are controlled by ideal divisors of `(C_1)^2` and `(C_2)^2`. Uniformly, their counts are divisor-like. Averaging divisor-like weights over the reconstructed base can at most replace worst-case `B^{o(1)}` by logarithmic/divisor moments using currently certified inputs. It cannot create a polynomial deficit.

This is precisely the safe role of **AR-016**: divisor and finite-fiber reconstruction preserves an exponent; it never supplies one. Therefore norm-ideal averaging is useful bookkeeping but is exponent-neutral for the present target.

## 3. Local valuation / recurrence-period test

For a fixed prime `p` away from the charged core and bad coefficients, a Pell/Lucas sequence modulo `p^r` is periodic. Requiring the second norm to be a square or to occupy a legal local class can remove some exponent classes `j mod ord_{p^r}(epsilon_k)`.

This is genuine local structure, but two obstacles remain:

1. the unit `epsilon_k`, the seed, and hence the local period vary with the reconstructed base/core;
2. removing exponent classes inside a logarithmic completion fiber does not by itself thin the outer base population by a fixed power.

To turn many such local restrictions into a family-level saving one would need a congruence-refined asymptotic or sieve theorem for the **same reconstructed base measure**, uniform enough in the selected primes. That theorem is not currently certified.

## 4. Required Arsenal audit

### AR-016 — direct, exponent-neutral

Applicable exactly to the seed/ideal/divisor and finite reconstruction layers. It confirms `B^{o(1)}` multiplicity only. It cannot be charged as a second saving.

### AR-023 / AR-024 — active firewalls

The triples `(M,N,U)` and legal core `k` cannot be compressed to a scalar such as `C_1`, `C_2`, `Delta`, or a recurrence discriminant merely because each scalar has divisor-many preimages. The physical masks, cells, `kg^2|Delta`, switched channel assignment and second-norm condition remain pair/triple dependent. No measure-preserving scalar adapter has been proved.

Likewise, a theorem for a superficially identical Pell or Lucas recurrence under another outer conditioning cannot be promoted to this receiver without matching the reconstructed physical measure.

### AR-028 — no recharge

The 6da completion multiplicity, the common core and the double-eliminant support have already been charged. The second Pell seed decomposition is a postfilter/re-expression of the same two survivor equations; its divisor count cannot be multiplied in as an independent source of saving.

### AR-033 — no rectangle adapter

The unit-orbit correlation is not presently a scalar coprime rectangle with a proved factorization into two marginal Dirichlet series and a summable cross correction. The required weighted coefficient norm and curved/product-height transfer are absent. The Stage12 `3/4+epsilon` tail is therefore not portable.

### AR-035 — relevant but only qualitative without a new adapter

A fixed finite set of local primes could in principle reject some reconstructed-base states. But AR-035 requires a fixed-modulus congruence-refined asymptotic for the **same ambient/reconstructed population** and, without uniformity as the prime set grows, yields only qualitative `o(1)`. Such a Stage15 Pell-base refined asymptotic has not been proved here, so AR-035 does not yield a fixed `delta>0`.

### AR-037 — wrong current analytic object

No uniform Euler factorization `F(s)=zeta(s)^z H(s)` for the varying `(k,seed,epsilon_k)` recurrence-correlation family has been established. Regulators/conductors vary with the base. Even a legal finite-order Selberg--Delange application would supply fixed logarithmic savings unless a new polynomial mechanism were separately present.

### Pell/recurrence Arsenal search

The current `STAGE14-ARSENAL-20260813-R02` index contains no dedicated Pell/Lucas recurrence theorem asset. The relevant reusable entries are therefore the generic finite-fiber, measure-firewall, no-recharge, fixed-prime and analytic-interface mechanisms audited above. No external recurrence theorem is silently promoted.

## 5. Current-input negative certificate

The Pell representation **does** sharpen the structural picture: a survivor is an intersection of two rank-one unit orbits in the same real quadratic field, with all local masks attached. But under the currently certified inputs:

- pointwise orbit length is only `B^{o(1)}` and was already known/charged;
- reducing logarithmic exponent multiplicity cannot yield a polynomial outer saving;
- ideal-divisor averaging remains divisor/logarithmic;
- local valuation restrictions lack a same-measure uniform base-triple sieve;
- the second norm algebraically returns the already-tested double eliminant after eliminating `L`.

Therefore
\[
\boxed{\text{no same-measure fixed-power saving follows from the current Pell/unit-orbit inputs}.}
\]
This is a rigorous **current-input negative certificate**, not an impossibility theorem for future recurrence/primitive-divisor or family-sieve results.

Consequently
\[
\boxed{\delta>0\text{ remains unproved},\qquad \sigma>0\text{ remains unproved}.}
\]
There is no executable polynomial overlap window from this route.

Because the receiver geometry has materially changed from centered modular occupancy to recurrence-orbit intersection, the controller protocol now requires an immediate fresh `EXHAUSTIVE_VIEW_AUDIT` and `BLIND_REDISCOVERY` before any parking or next-route selection.

```text
STAGE15_6_SUBSTAGE=6dt
STAGE15_6DT_PELL_AVERAGING_TESTED=true
STAGE15_6DT_AR016=APPLICABLE_EXPONENT_NEUTRAL
STAGE15_6DT_AR023_024=FIREWALL_PASS
STAGE15_6DT_AR028=NO_RECHARGE_PASS
STAGE15_6DT_AR033=NO_ADAPTER
STAGE15_6DT_AR035=QUALITATIVE_ONLY_NO_STAGE15_BASE_ADAPTER
STAGE15_6DT_AR037=NO_UNIFORM_EULER_ADAPTER
STAGE15_6DT_DEDICATED_PELL_ARSENAL_ASSET=NONE_FOUND
STAGE15_6DT_FIXED_POWER_FROM_CURRENT_PELL_INPUTS=false
STAGE15_6DT_DELTA_PROVED=false
STAGE15_6DT_SIGMA_PROVED=false
STAGE15_6DT_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY
STAGE15_6DT_EXIT=EXHAUSTIVE_AND_BLIND_PROTOCOL_REQUIRED
```
