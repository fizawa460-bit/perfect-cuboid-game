# Stage14-tH7 — roadworks stress test, cycle-1 park, and next-cycle gate

## Purpose

Stage14-tH0 created a deliberately non-blocking support track around the live `t` route.  Stages tH1--tH6 then built, in order,

1. Gaussian primary/ray-class/conductor normalization;
2. the divisor-coupled Gaussian norm hyperbola engine;
3. the all-order character/conductor/shared-modulus adapter;
4. the weighted Mellin/Hecke large-sieve transfer layer;
5. exact Gaussian-pair coefficient collision energy;
6. an abstract power-saving exponent receiver.

Stage14-tH7 is the gate promised in tH0.  It does **not** invent another theorem merely to keep the sequence alive.  It adversarially tests the completed roadworks against structural failure modes and against every currently merged live-`t` interface that materially changes the analytic shape.

The resulting decision is two-part:

```text
old tH1--tH6 infrastructure cycle: COMPLETE and PARKED for reuse
support route as a whole: CONTINUES, because merged t38 creates a genuinely new independent roadwork lane
```

The new lane is Gaussian spin / Dirichlet-symbol Type-I/II infrastructure.  It is not a repair of tH1--tH6 and does not require Stage14-t39 to exist before it can be developed.

No Stage14 global power saving, `T=o(sqrt(B))`, or perfect-cuboid nonexistence statement is claimed here.

---

## 1. Frozen infrastructure stack

The cycle-1 stack is frozen as

```text
tH0  non-blocking support architecture
  |
tH1  Gaussian primary / units / ray class / conductor
  |
tH2  k|epsilon*m hyperbola -> g,h,r,delta
  |
tH3  all-order spectral packet + shared modulus envelope
  |
tH4  L2-safe masks/weights/Mellin/divisor transfer
  |
tH5  exact (U,V) coefficient collision energy
  |
tH6  exponent-transfer receiver
```

The important interface identities are

\[
N(U)=hr,\qquad N(V)=gh\delta,
\]

with

\[
g\mid\varepsilon,\qquad (h,\varepsilon/g)=1,
\qquad hr\delta\le Y,
\]

and the tH3 shared-modulus rule

\[
\mathfrak q_{UV}=\operatorname{lcm}(\mathfrak f_U,\mathfrak f_V),
\]

so a common oriented Gaussian prime ideal appears once, not once per coordinate.

For the live Stage14 `mu_4`-trivial Mellin family, the tH1/tH3 two-adic conductor correction vanishes.

The standard roadwork overhead through tH1--tH5 is only `B^o(1)`, so tH6 records zero fixed-power roadwork overhead.

---

## 2. Adversarial stress matrix

The road is accepted only if every stress case is either

- `SAFE`: already represented by the frozen interface with no fixed-power loss;
- `EXTERNAL_ANALYTIC`: the road can carry the input, but a genuine analytic theorem is still missing;
- `REOPEN_OLD_CYCLE`: the frozen adapter would actually have to be modified;
- `NEW_CYCLE`: useful independent infrastructure exists, but it is a different road rather than a defect in the old one.

### S1. Higher-order local Mellin characters

A local character is not assumed quadratic.

**Classification: SAFE.**

tH1 stores arbitrary exponent `j mod p-1`; tH3 retains arbitrary order.  The `mu_4` specialization is an optional fast path, not the only supported character model.

### S2. Non-`mu_4`-trivial unit signatures

A later application may have local unit signature `J != 0 mod 4`.

**Classification: SAFE.**

tH1 already records

```text
J=0 -> e2=0
J=2 -> e2=2
J=1,3 -> e2=3
```

so the ramified `(1+i)` factor changes conductor norm only by an absolute bounded factor.

### S3. Same oriented auxiliary prime used on U and V

Both coordinate characters are nontrivial at one oriented prime ideal `l`.

**Classification: SAFE and REQUIRED.**

The joint evaluation modulus contains `l` once.  Replacing it by independent `l_U,l_V` is explicitly forbidden.

### S4. Both conjugate Gaussian primes genuinely active

Both `l_{p,+}` and `l_{p,-}` occur.

**Classification: SAFE.**

They are distinct ideals and are retained separately.  Their combined norm may legitimately contribute `p^2`; this is not the forbidden same-oriented-prime squaring.

### S5. Bad auxiliary prime divides a physical norm factor

A rational auxiliary prime divides `g*h*r*delta`.

**Classification: SAFE.**

tH3 exposes the exact mask

\[
\gcd(Q_{\rm rat},ghr\delta)=1.
\]

The mask is zero-one and is therefore L2-safe by tH4.

### S6. Many divisor decompositions collapse to one exact norm pair

Many `(h,r,delta)` may yield the same `(m,n)`.

**Classification: SAFE.**

tH5 proves that after fixed `(epsilon,g,m,n)` the only remaining freedom is `h`, with

\[
h\mid\gcd(m,n/g).
\]

Hence the multiplicity is divisor-bounded, `Y^{o(1)}`.

### S7. Gaussian representation multiplicity

A fixed norm admits several integral Gaussian representatives.

**Classification: SAFE.**

`r_2(n)<=4 tau(n)` and the exact-pair tH5 energy remains near-linear up to `B^o(1)`.

### S8. Unit-orbit quotienting

Downstream code wishes to identify associates.

**Classification: SAFE WITH POLICY.**

The four unit choices on each coordinate cost an absolute factor at most 16 for a pair.  Gaussian conjugation/orientation is **not** included in that quotient and must remain explicit.

### S9. Projecting away V and retaining only U

A later proof tries to simplify coefficients to one coordinate before controlling the physical fiber.

**Classification: REOPEN_OLD_CYCLE / INVALID SHORTCUT.**

tH5 explicitly shows pair retention is essential.  The discarded coordinate can contain a polynomial-size `delta` fiber.  A theorem that genuinely requires U-only coefficients needs a new projection-energy argument; the current road must not pretend that projection is free.

### S10. Prime-power odd conductors

A later spectral theorem requires characters primitive modulo `l^a`, `a>=2`, rather than the squarefree oriented-prime support used by the current adapter.

**Classification: REOPEN_OLD_CYCLE.**

The current active-support/lcm adapter is built for the residue/ray-class family actually needed in the tH1--tH6 cycle.  Prime-power local conductor growth would require an explicit local extension before reuse.

### S11. Polynomial spectral packet energy

Suppose

\[
E_{\rm spec}=B^\sigma
\]

with fixed `sigma>0`.

**Classification: SAFE TO ACCOUNT, NOT FREE.**

tH4/tH6 do not hide the loss.  The squared-moment overhead ledger receives `Omega += sigma`.

### S12. Polynomial Mellin-kernel budget

Suppose

\[
K_W=B^\kappa.
\]

Because tH4 pays `K_W^2` in squared norm,

**Classification: SAFE TO ACCOUNT, NOT FREE**, with

\[
\Omega\mathrel{+}=2\kappa.
\]

### S13. Polynomial number of assembled blocks

If a decomposition has `J=B^beta` pieces and only generic Cauchy assembly is available,

**Classification: SAFE TO ACCOUNT, NOT FREE**, with squared-level overhead `Omega += beta`.

The standard tH decomposition has only polylogarithmically many pieces, hence beta=0.

### S14. Independent U/V modulus tensorisation

A proof replaces one shared modulus by independently chosen `q_U,q_V`.

**Classification: INVALID SHORTCUT.**

This destroys the collision geometry.  It is forbidden by both tH3 and tH4.

### S15. Same-modulus residue collision theorem is absent

No theorem yet supplies a fixed-power joint same-modulus second moment or direct-count saving.

**Classification: EXTERNAL_ANALYTIC.**

This is not a roadworks defect.  tH6 is precisely the receiver for such a theorem when one becomes available.

### S16. Direct count versus squared second moment

A later theorem outputs count-level saving rather than L2 saving.

**Classification: SAFE.**

tH6 has separate ledgers; it does not incorrectly take or omit a square root.

### S17. New number field or non-Gaussian norm algebra

A future route leaves `Q(i)`.

**Classification: REOPEN_OLD_CYCLE OR NEW TRACK.**

The Gaussian primary/unit/conductor rules are field-specific and must not be silently reused.

### S18. Higher-rank packet with more than two physical coordinates

A later theorem requires a genuine three-or-more-coordinate shared-modulus packet.

**Classification: REOPEN_OLD_CYCLE.**

The present exact collision-energy theorem is a paired `(U,V)` theorem.  A higher-rank version would need its own coefficient-energy audit.

---

## 3. Exponent-ledger stress test

Let an analytic input give a squared-second-moment saving `Gamma`, and let all nonstandard fixed-power costs total `Omega`.

The tH6 receiver gives

\[
\Gamma_{\rm eff}=\Gamma-\Omega.
\]

If exactly one final Cauchy/square-root conversion is used,

\[
\boxed{\delta_{\rm delivered}=\frac{\Gamma-\Omega}{2}.}
\]

The stress cases above imply the additive fixed-power ledger

\[
\boxed{
\Omega
=\sigma+2\kappa+\beta+\Omega_{\rm new},
}
\]

where

- `sigma` is any polynomial spectral-energy exponent;
- `kappa` is the Mellin-kernel exponent;
- `beta` is any polynomial block-assembly exponent;
- `Omega_new` denotes any explicitly proved additional nonstandard loss.

For the **standard frozen tH1--tH5 road**, all four are zero at the fixed-power level:

\[
\boxed{\Omega_{\rm standard}=0.}
\]

Thus the cycle passes the central anti-hidden-loss test.

The existing Stage14 post-local target remains

\[
\frac{41}{42}-\frac12=\frac{10}{21}.
\]

Under a one-root squared-moment path, the conditional requirement is therefore

\[
\Gamma-\Omega\ge\frac{20}{21}.
\]

This is a receiver threshold only, not a theorem that such a `Gamma` exists.

---

## 4. Current merged live-t compatibility through Stage14-t38

At the tH7 gate, the merged live t route has reached Stage14-t38.

T38 proves, among other things,

- a moving-canonical-prime genus-one packet description;
- `B^o(1)` moving-prime multiplicity per fixed descended packet;
- a global `B^(1/2+o(1))` super-square-root packet bound;
- fixed power saving away from the critical `ell=B^(1/2+o(1))` strip;
- reduction of the remaining critical strip to a bilinear average across Gaussian primes and descended packets.

None of these findings invalidates tH1--tH6.

However t38 also identifies a genuinely new analytic technology:

```text
Friedlander--Iwaniec Gaussian spin / Jacobi--Kubota multiplier
      -> Gaussian Dirichlet-symbol kernel (z/w)
      -> Type-I / Type-II bilinear sums
```

The Stage14 critical-strip packet is **not yet** proved to equal the classical Jacobi--Kubota spin.  The missing live-t transfer is to convert the quartic square-sieve correlation into a Gaussian Dirichlet-symbol Type-I/II kernel, or prove the obstruction.

This new kernel is not naturally represented as the old tH3 object

```text
fixed auxiliary residue/ray-class modulus
+ character pair on exact Gaussian hyperbola coefficients.
```

In the spin architecture the modulus/kernel is tied to the moving Gaussian variables themselves.  Therefore pretending that tH1--tH6 already cover it would be a category error.

---

## 5. Park/continue decision

### 5.1 Cycle-1 roadworks are complete

No stress case revealed a hidden fixed-power loss inside the advertised tH1--tH6 interface.

Accordingly,

```text
TH_CYCLE1_T_H1_TH6_COMPLETE=true
TH_CYCLE1_REUSABLE=true
TH_CYCLE1_PARKED=true
```

The old cycle should be reopened only when one of its explicit structural assumptions changes, for example

1. prime-power odd conductors are required;
2. a one-coordinate projection becomes unavoidable;
3. polynomial spectral/Mellin/block budgets appear and cannot simply be charged in the tH6 ledger;
4. a higher-rank packet replaces the exact `(U,V)` pair;
5. the arithmetic leaves `Q(i)`.

The absence of a same-modulus power-saving theorem by itself is **not** a reason to reopen the old cycle.

### 5.2 The support route itself should not park

Merged t38 has created useful work that is independent of future t39 details.

The next support cycle can build a reusable Gaussian-spin bilinear interface around

\[
[wz]=\epsilon[w][z]\left(\frac zw\right)
\]

and Type-I/Type-II forms

\[
\sum_w^*\sum_z \alpha_w\beta_z\left(\frac zw\right),
\]

including

- primary/associate normalization for the spin kernel;
- exact coprimality and reciprocity conventions;
- dyadic norm boxes;
- sector and progression masks;
- coefficient L2 budgets;
- diagonal/common-factor exclusions;
- an abstract exponent receiver compatible with the existing tH6 ledger.

All of that can be done without knowing whether t39 ultimately succeeds in expressing the Stage14 quartic trace in the spin kernel.

Therefore

```text
TH_SUPPORT_ROUTE_PARKED=false
TH_NEW_INDEPENDENT_ROADWORK_AVAILABLE=true
```

---

## 6. Stage14-tH8 handoff

The recommended next support stage is

**Stage14-tH8 — Gaussian spin / Dirichlet-symbol Type-I/II infrastructure.**

Its minimum input is the merged classical Gaussian-spin boundary recorded by t38, not a future t39 result.

The tH8 contract should be:

```text
input:
  primary Gaussian variables w,z
  dyadic norm ranges W,Z
  bounded coefficient arrays alpha_w,beta_z
  sector/AP/coprimality masks
  Gaussian Dirichlet-symbol kernel (z/w)

output:
  exact normalization and admissibility interface
  reusable Type-I/II coefficient-energy ledger
  precise literature theorem hypotheses / missing hypotheses
  NO claim that the Stage14 quartic trace has already been converted to this kernel
```

Thus tH can continue surrounding the live route without waiting for t39 and without reopening already-completed tH1--tH6 work.

---

## 7. Deterministic audit contract

The tH7 audit is intentionally architectural rather than numerical-search heavy.  It checks:

1. every frozen tH0--tH6 boundary marker needed by this gate;
2. all stress cases have exactly one declared classification;
3. every `REOPEN_OLD_CYCLE` case has an explicit reason;
4. every polynomial budget is charged with the correct exponent;
5. the standard-road exponent overhead is exactly zero;
6. direct-count and squared-moment ledgers remain distinct;
7. the Stage14 `10/21` and one-root `20/21` thresholds are exact;
8. the currently merged t38 boundary is present;
9. the t38 Gaussian-spin need is classified as `NEW_CYCLE`, not falsely marked as already solved;
10. no global theorem flag is promoted.

---

## Boundary

```text
STAGE14_TH7=COMPLETE_ROADWORKS_STRESS_GATE_AND_NEW_CYCLE_DECISION
TH_REQUIRES_FUTURE_T_RESULT=false
TH0_TH6_INTERFACE_STRESS_TESTED=true
STANDARD_TH1_TH5_FIXED_POWER_OVERHEAD=0
STANDARD_ROAD_HIDDEN_FIXED_POWER_LOSS=false
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
SAME_MODULUS_MISSING_THEOREM_IS_ROADWORKS_DEFECT=false
PAIR_RETENTION_ESSENTIAL=true
INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false
PRIME_POWER_ODD_CONDUCTOR_EXTENSION_PROVED=false
ONE_COORDINATE_PROJECTION_ENERGY_PROVED=false
TH_CYCLE1_T_H1_TH6_COMPLETE=true
TH_CYCLE1_REUSABLE=true
TH_CYCLE1_PARKED=true
T38_CURRENT_LIVE_INTERFACE_AUDITED=true
T38_GAUSSIAN_SPIN_TYPE_I_II_NEW_ROADWORK_IDENTIFIED=true
T38_PACKET_EQUALS_FI_JACOBI_KUBOTA_SPIN=false
TH_SUPPORT_ROUTE_PARKED=false
TH_NEW_INDEPENDENT_ROADWORK_AVAILABLE=true
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH8 Gaussian spin / Dirichlet-symbol Type-I/II infrastructure; do not wait for t39
```
