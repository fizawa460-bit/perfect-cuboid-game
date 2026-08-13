# Stage14-s6-00 — post-local global-small-point architecture

## Purpose

Stage14-s5u closes the s5 local-2-descent / reciprocity-sieve method with the unconditional physical-base upper bound

```text
V(B) <<_epsilon B^(41/42+epsilon).
```

The remaining gap to the finite square-root signal is not an unresolved internal local-sieve defect.  It is a strength gap.  Stage14-s6 therefore starts from a fresh question:

> after the complete local 2-descent system has accepted a base/class, how often does that class actually contain a **global rational point in the physical logarithmic small-point window**?

This stage compares the plausible next mechanisms, locks the exact exponent budget, and selects one primary route.  It proves no new square-root asymptotic and no new global-solubility theorem.

The selected route is a **direct post-local global-small-point incidence count**.  We do not first try to estimate Sha and then separately estimate least-point heights.  Instead we count the explicit supported 2-cover incidences which possess a bounded-height rational point mapping back to the physical Stage14 chart.

---

## 1. Frozen input from s5

Stage14-s5u proves, on the physical cutoff scale,

```text
N_local(B) <<_epsilon B^(41/42+epsilon),
```

where `N_local(B)` is an admissible supported locally-soluble descent-class majorant for physical active bases.  In particular

```text
V(B) <= N_local(B)
```

up to the already-controlled subpolynomial class multiplicity.

The s5 method is deliberately closed because its next already-proved internal ceiling is the single-edge exponent `1/20` on Euclid scale.  Even perfect micro-optimization of the current modules would only move the physical exponent from `41/42` toward `39/40`, still far from `1/2`.

Thus Stage14-s6 does **not** reopen the local character polynomial unless a later global argument creates a specific new weighted local theorem that is genuinely necessary.

---

## 2. Frozen geometric input: the fixed-curve square-root mechanism is dead

Stage14-4ah showed that a fixed physical rational curve can contribute at the square-root scale only in the extremal pattern

```text
M.C = 4,
deg(C -> P1_r) = 2,
```

i.e. a rational `M`-degree-four bisection.

Stage14-4ai reduced that to one final split singular-anticanonical mechanism, and Stage14-4ak eliminated that last case by the exact deck anti-invariant lattice parity-coset computation.

Therefore

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true.
```

Stage14-s6 must be a **collective moving-arithmetic** mechanism.  Broad K3 fixed-curve searching is not reopened.

---

## 3. Frozen first-hit interpretation

Stage14-4al defines the first physical height `mu(F)` for a primitive oriented Pythagorean first-face base `F` and locks

```text
V(B) = #{F : mu(F) <= B}.
```

The ambient oriented primitive Pythagorean-base count is

```text
A(B) = B/pi + O(sqrt(B) log B).
```

Consequently a genuine square-root law would be equivalent to inverse-square-root activation density.

Stage14-s3 gives the necessary elliptic height gate:

```text
physical hit below B
  => a non-torsion rational point
     with canonical height O(log B).
```

Positive rank alone is not enough: the finite s1/s3 audits contain many positive-rank inactive controls, and 4al records a wide first-hit-height distribution.  Therefore Stage14-s6 must retain the physical small-point condition rather than replacing it by a rank-density problem.

---

## 4. Exact post-local exponent budget

Let

```text
N_gs(B)
```

denote the number of supported locally-soluble base/class pairs which in addition possess a **global rational point** satisfying all of the following:

1. it lies on the actual Stage14 supported 2-cover class;
2. it maps through the frozen s3 birational chart to the physical positive Stage14 open set;
3. it is non-torsion;
4. its physical height satisfies `d<=B` (equivalently it lies in the s3 logarithmic canonical-height window).

Then

```text
V(B) <= N_gs(B) <= N_local(B)
```

up to `B^epsilon` supported-class multiplicity.

The first Stage14-s6 quantitative target is therefore

```text
N_gs(B)
 <<_epsilon
 B^(41/42-delta_gs+epsilon)
```

for some fixed

```text
delta_gs > 0.
```

Any positive `delta_gs` is a genuine new theorem beyond s5.

To reach the square-root **upper bound** from the current s5u exponent one needs

```text
41/42 - delta_gs <= 1/2,
```

hence exactly

```text
boxed: delta_gs >= 10/21.
```

This is the central s6 exponent budget.

It is intentionally separated from the harder tasks of proving a lower bound, a constant, or an asymptotic.

---

## 5. Route comparison

### Route A — keep optimizing the s5 local sieve

Status: **rejected as the Stage14-s6 primary route**.

Reason: s5u already isolates the current module ceiling.  The available gain before a new local theorem is tiny compared with the required `10/21` post-local saving.

```text
S6_LOCAL_ONLY_PRIMARY=false.
```

### Route B — fixed low-degree accumulating rational curves

Status: **closed upstream**.

The unique fixed `M`-degree-four square-root mechanism is eliminated by 4ak.

```text
S6_FIXED_M4_BISECTION_PRIMARY=false.
```

Higher fixed degrees would need polynomially proliferating moving strata, exactly as s4c records, so this is no longer a finite fixed-curve classification problem.

### Route C — positive-rank density first

Status: **not selected**.

Positive rank does not imply a physical hit below `B`; s3 proves the least-physical-small-point gate is genuine.  A rank theorem without point-height control cannot provide the required direct retainer.

```text
S6_RANK_DENSITY_PRIMARY=false.
```

### Route D — separately estimate Sha/global solubility and then least-point height

Status: **valid decomposition, but not selected as first theorem target**.

This factorization would require two moving-family inputs:

```text
local soluble -> globally soluble,

globally soluble -> physical point with hhat=O(log B).
```

No merged Stage14 theorem currently supplies a positive power in either factor uniformly for this non-twist Pythagorean family.  Splitting the problem would therefore create two hard moving targets before obtaining any quantitative gain.

```text
S6_SEPARATED_SHA_THEN_HEIGHT_PRIMARY=false.
```

### Route E — direct post-local global-small-point incidence

Status: **selected**.

A supported local class already comes with explicit finite 2-descent / Kummer data.  Requiring global solubility plus the physical small-point window means requiring an actual bounded-height rational point on an explicit low-degree cover, together with the physical reconstruction constraints.

That event can be attacked directly by arithmetic incidence methods without proving an average Sha theorem first.

```text
S6_PRIMARY_ROUTE=DIRECT_POST_LOCAL_GLOBAL_SMALL_POINT_INCIDENCE.
```

---

## 6. What the selected object should look like

The next stage must produce a denominator-cleared, primitive integral incidence model of the schematic form

```text
C_{m,n,sigma}(z,w)=0,
```

where

- `(m,n)` are primitive opposite-parity Euclid coordinates;
- `sigma` is one of the `B^epsilon` supported descent states already generated by s5;
- `(z,w)` are rational-point / cover coordinates after a fixed chart and denominator clearing;
- the physical reconstruction inequalities/sign/order conditions are explicit;
- `d<=B` gives a polynomial box in the integral variables;
- torsion and boundary components are removed exactly before any counting theorem is invoked.

The crucial design constraint is that **the global point variables remain present**.  Summing them out and returning to a local indicator would merely recreate s5.

The intended count is therefore a family incidence count, not another local character average.

---

## 7. First arithmetic weapon: canonical large-prime incidence

The merged t-track has already established a useful structural lesson on related Stage14 2-cover packets.

For a canonical large bad/support prime, the visible branch frequently becomes an explicit primitive congruence line rather than a new independent character gate.  In the t29 four-linear packet this gives projective incidence moduli, while the kernel-invisible branch requires Gaussian/dual routing.

Stage14-s6 will reuse that **architecture**, not the t-track theorem target:

```text
supported global-small-point cover
  -> choose canonical largest relevant odd support prime ell
  -> visible projective-incidence branch
     OR Gaussian/dual-invisible branch
  -> keep a smooth-support exceptional branch explicit.
```

The first quantitative test is whether the physical bounded-height incidence supplies enough independent geometry after conditioning on the local state to turn the large prime into a genuine dimension-reducing congruence.

No power saving is asserted in s6-00.

---

## 8. Determinant/square-sieve backup, not a black box

If the large-prime visible branch produces a fixed low-degree hypersurface or surface after the local state and prime residue are frozen, determinant-method / square-sieve bounds become plausible tools.

But Stage14-s6 will not cite a generic rational-point theorem before checking:

1. the exact dimension and degree of the incidence variety;
2. irreducibility of the relevant component;
3. accumulating linear/rational subvarieties;
4. uniform dependence on moving coefficients/state moduli;
5. whether the physical height box matches the theorem's height.

This avoids repeating the earlier error pattern of applying a correct general theorem to the wrong moving family.

---

## 9. Literature boundary

Three nearby bodies of work are retained as **models**, not imported theorems.

1. Pierre Le Boudec, *Height of rational points on congruent number elliptic curves* (arXiv:1802.07136): proves strong lower bounds for the least non-torsion point for a positive proportion in the congruent-number twist family.  This shows that least-point height can be a powerful thinning mechanism, but Stage14 is not that twist family.
2. Joachim Petit, *On the number of quadratic twists with a rational point of almost minimal height* (arXiv:2004.02500): obtains an asymptotic in a fixed-curve quadratic-twist setting with an almost-minimal point.  Again, the family geometry is different, so only the counting philosophy transfers.
3. Browning--Heath-Brown determinant-method work on bounded-height rational points on hypersurfaces supplies a general backup once the exact Stage14 incidence variety has been reduced to a theorem-compatible fixed-degree family.

No literature result is declared directly applicable at s6-00.

---

## 10. Stage14-s6 provisional roadmap

The roadmap is intentionally numbered from `00` and is trigger-driven rather than padded to a predetermined length.

```text
s6-00  architecture / exponent budget / route selection                 [this stage]
s6-01  exact denominator-cleared global-small-point 2-cover incidence
s6-02  primitive box, torsion/boundary removal, support-prime split
s6-03  visible large-prime projective-incidence counting theorem or obstruction
s6-04  Gaussian/dual kernel-invisible branch counting theorem or obstruction
s6-05  cover-conditioned smooth-support exceptional branch
s6-06  assemble first direct post-local retainer delta_gs>0
s6-07  optimize/amplify and compare with required delta_gs=10/21
s6-08  square-root upper-bound gate or isolate the new structural barrier
s6-09  close s6 theorem package / decide asymptotic or next-method handoff
```

Stages `s6-03..s6-05` may split only if they expose genuinely independent theorem-sized branches.  We do **not** pre-create `s6-03a`, `s6-03b`, etc.

The expected core length is therefore roughly ten stages, with `s6-00..s6-09` as the default envelope rather than a promise that every number will be needed.

---

## 11. Stop/reopen rules

### Do not reopen s5 merely because an s6 count has local congruences

The s5 local theorem is already a valid majorant.  Reopen it only if s6 creates a specific external weight for which an arbitrary-weight local retainer is quantitatively necessary.

### Do not reopen the fixed K3 bisection search

The fixed `M=4` mechanism is theorem-level closed by 4ak.  Reopen K3 lattice geometry only on a new explicit divisor/fibration trigger.

### Do not promote a positive post-local exponent to sqrt(B)

A theorem

```text
delta_gs>0
```

is valuable but does not imply the target scale.  The current exact requirement is

```text
delta_gs >= 10/21
```

for a square-root upper bound.

### Upper bound is not asymptotic

Even if s6 reaches

```text
V(B) << B^(1/2+epsilon),
```

that does not prove

```text
V(B) ~ c sqrt(B).
```

A matching lower mechanism / density constant is a separate gate.

---

## Decision

```text
STAGE14_S6_00=COMPLETE_POST_LOCAL_GLOBAL_SMALL_POINT_ARCHITECTURE
S5_METHOD_ACCEPTED_AS_CLOSED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
ANY_POSITIVE_POST_LOCAL_SAVING_IS_NEW_PROGRESS=true
FIXED_M4_BISECTION_ROUTE_REOPEN=false
LOCAL_SIEVE_CONTINUATION_PRIMARY=false
RANK_DENSITY_PRIMARY=false
SEPARATED_SHA_THEN_HEIGHT_PRIMARY=false
DIRECT_POST_LOCAL_GLOBAL_SMALL_POINT_INCIDENCE_PRIMARY=true
CANONICAL_LARGE_PRIME_INCIDENCE_FIRST_WEAPON=true
GAUSSIAN_DUAL_INVISIBLE_BRANCH_RESERVED=true
SMOOTH_SUPPORT_BRANCH_MUST_BE_COUNTED=true
DETERMINANT_METHOD_IMPORT_UNCONDITIONAL=false
S6_EXPECTED_DEFAULT_RANGE=00..09
S6_PREEMPTIVE_SUBSTAGE_SPLIT_REQUIRED=false
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s6-01 exact denominator-cleared supported 2-cover global-small-point incidence model and physical height box
```
