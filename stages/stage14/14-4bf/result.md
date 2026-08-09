# Stage14-4bf — import s5t, upgrade the local retainer, and refocus the main track

## Result

Stage14-4be instantiated the first explicit unweighted local retainer on the physical cutoff scale:

```text
rho_loc(B) << B^(-1/400+epsilon),
E_loc(B)=0.
```

That exponent inherited the deliberately conservative `M^(-1/200)` local-system saving used before Stage14-s5t.

Merged Stage14-s5t has now optimized the same closed three-case local architecture. It proves on regular Euclid boxes

```text
N_local(M) <<_epsilon M^(2-1/41+epsilon),
```

with optimized thresholds

```text
sigma=2/41,
lambda=5/41,
delta_M=1/41.
```

The old `1/200` was therefore not structural. Converting `M<=B^(1/2)` gives

```text
N_local(B) <<_epsilon B^(81/82+epsilon).
```

Since Stage14-4al gives `A(B)=B/pi+O(sqrt(B)log B)` and Stage14-4au gives `S(B)<=N_local(B)`, the Stage14-4as unweighted cumulative retainer can be upgraded to

```text
rho_loc(B) <<_epsilon B^(-1/82+epsilon),
E_loc(B)=0.
```

Hence the physical-scale local exponent is now

```text
delta_loc=1/82.
```

The direct one-sided physical bound improves simultaneously to

```text
V(B) <<_epsilon B^(81/82+epsilon).
```

This stage also makes the roadmap decision requested by 4be. The main `14-4` line will **not wait for further local optimization**. Stage14-s5u remains worthwhile as one bounded parallel attempt to compress the all-short sector, because s5t identifies an explicit bookkeeping loss and s5p/s5q already provide the relevant Hilbert/Fourier `ell^2` energy. But the main track now refocuses on post-local global/small-point thinning.

---

## 1. Imported s5t optimization

Stage14-s5t writes

```text
S=M^sigma,
L=M^lambda
```

for the long-neighbor and very-long thresholds. Its three-case savings are

```text
Case A, long-long QLS:
  delta_A=sigma/2;

Case B, very-long vertex with only short neighbors:
  delta_B=lambda/2-3sigma/4;

Case C, all-short periodic tuple summation:
  delta_C1=1-8lambda,
  delta_C2=2-12lambda.
```

Thus

```text
delta(sigma,lambda)
=min(sigma/2,
     lambda/2-3sigma/4,
     1-8lambda,
     2-12lambda).
```

The exact optimum in the current three-case proof is

```text
sigma=2/41,
lambda=5/41,
delta=1/41.
```

At this point

```text
delta_A=1/41,
delta_B=1/41,
delta_C1=1/41,
delta_C2=22/41.
```

All earlier single-edge and E-transition savings are strictly larger than `1/41`, so they do not become new bottlenecks.

Therefore

```text
S5T_LOCAL_M_EXPONENT_1_OVER_41_IMPORTED=true.
```

---

## 2. Updated unweighted local retainer

The cumulative physical family satisfies

```text
M<=B^(1/2).
```

Hence

```text
N_local(B)
 << B^((2-1/41)/2+epsilon)
 = B^(81/82+epsilon).
```

The ambient primitive oriented Pythagorean base count is

```text
A(B)=B/pi+O(sqrt(B)log B),
```

so `A(B)>>B` for large `B`.

Since

```text
S(B)<=N_local(B),
```

we get

```text
S(B)/A(B)
 << B^(-1/82+epsilon).
```

Thus a valid Stage14-4as specialization is

```text
rho_loc(B)=C_epsilon B^(-1/82+epsilon),
E_loc(B)=0.
```

This supersedes the `1/400` exponent from 4be.

As in 4be, `E_loc=0` is an **outer-interface choice** after the full local system has already been bounded. It does not assert that internal Fourier errors, the reciprocal error, or the separate constant mode are literally zero.

---

## 3. Updated direct physical upper bound

Merged s5s supplied the one-sided inclusion

```text
physical hit
=> globally soluble small-point descent class
=> locally soluble descent class.
```

Therefore the improved local-system theorem immediately gives

```text
V(B)
 <= #L_B
 <<_epsilon B^(81/82+epsilon).
```

No local-to-global converse and no Sha hypothesis is needed for this upper bound.

This is stronger than the prior

```text
B^(399/400+epsilon)
```

bound, but it is still far above the observed square-root scale.

---

## 4. The old local exponent was bookkeeping, not arithmetic resonance

Stage14-s5t explicitly proves

```text
OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL=false,
NEW_ARITHMETIC_RESONANCE_FOUND=false.
```

The current `1/41` optimum is only the optimum of the present three-case architecture with the all-short sector summed tuplewise in absolute value.

The current explicit weak step is

```text
#tuples <= M^(4lambda)
```

followed by absolute summation of the centered periodic bound for every tuple.

Later s5p/s5q already provide bounded Fourier `ell^2` energy and Hilbert-space contraction machinery. Consequently a targeted all-short energy compression is mathematically motivated; this is exactly the task assigned to s5u.

So 4bf does **not** declare the local exponent structurally final.

---

## 5. Why the main track should nevertheless refocus now

The current physical local saving is

```text
delta_loc=1/82.
```

In the 14-4as three-retainer ledger, the square-root main-term condition becomes

```text
delta_glob+delta_ht
 >= 1/2-1/82
 =20/41.
```

Thus almost the entire square-root gap remains after the current local theorem.

There is also a useful architecture ceiling. Suppose s5u miraculously removed the all-short Case C loss completely while leaving the present Case A/B estimates unchanged. Then any common saving `delta_M` must still satisfy

```text
delta_M <= sigma/2,
delta_M <= lambda/2-3sigma/4,
0<=lambda<=1.
```

For the first two bounds to both be at least `delta_M`, one needs

```text
lambda >= 5sigma/2.
```

Since `lambda<=1`,

```text
sigma<=2/5,
delta_M<=1/5.
```

After `B~M^2`, even this idealized Case-C-free ceiling would give only

```text
delta_loc<=1/10.
```

and would still leave at least

```text
1/2-1/10=2/5
```

of post-local thinning to reach a square-root main-term exponent.

This ceiling is conditional on leaving the current Case A/B estimates unchanged; it is **not** claimed as an absolute barrier to all future local methods. It is enough, however, to settle the roadmap decision: further local optimization cannot be the only main-track strategy.

---

## 6. Roadmap decision

The Stage14-4 main line now adopts the following policy.

```text
MAIN_TRACK_WAITS_FOR_S5U=false.
```

The already-proved local input is frozen for main-track propagation at

```text
delta_loc=1/82,
E_loc=0,
```

until a stronger merged theorem becomes available.

In parallel:

```text
s5u
```

gets one targeted attempt at replacing the all-short tuplewise absolute sum by the existing `ell^2`/Hilbert energy machinery. If it improves the exponent, a later 14-4 stage may import the improvement. Main-track progress does not depend on it.

The primary 14-4 problem now becomes the **post-local physical thinning**:

```text
locally soluble supported descent classes
-> classes carrying a global rational point
-> classes carrying a point in the physical logarithmic height window.
```

For an upper bound it is not necessary to prove a local-to-global converse or a standalone Sha density theorem. A direct joint estimate for global small-point classes inside the locally soluble majorant is equally valid and may be preferable to separately proving `rho_glob` and `rho_ht`.

Thus the next main-track stage should compare the two interfaces:

```text
separated: rho_glob * rho_ht,

direct:    one post-local global-small-point retainer,
```

and select the first quantitatively attackable theorem.

---

## 7. Relation to bridge1 chamber diagnostics

Merged Stage14-bridge1 routes the observed directional second-face survival asymmetry to a chamber-resolved diagnostic of

```text
D_loc/A_W.
```

That diagnostic concerns the **directional constant-mode mechanism** and whether it can explain the finite `ab/ac/bc` survival ordering.

It does not alter the unweighted cumulative upper-bound retainer proved here, because that retainer uses the complete local-system theorem before a lossy modewise absolute-value split.

Accordingly:

```text
CHAMBER_D_LOC_DIAGNOSTIC_RELEVANT_TO_DIRECTION_LAW=true,
CHAMBER_D_LOC_DIAGNOSTIC_REQUIRED_FOR_CURRENT_UPPER_BOUND=false.
```

No directional asymptotic is claimed in 4bf.

---

## 8. Updated 14-4as ledger

For the unweighted cumulative family, use

```text
rho_loc(B) << B^(-1/82+epsilon),
E_loc(B)=0.
```

If separated future retainers are used,

```text
rho_glob << B^(-delta_glob+o(1)),
rho_ht   << B^(-delta_ht+o(1)),
```

then the 14-4as main term is

```text
B^(1-1/82-delta_glob-delta_ht+o(1)).
```

The square-root main-term condition is

```text
delta_glob+delta_ht>=20/41.
```

The local propagated error remains zero in this specialization.

Alternatively a future direct post-local retainer

```text
H_phys(B) <= rho_post(B) S(B) + E_post(B)
```

may bypass the artificial separation between Sha/global solubility and first-small-point height. 4bf does not assert such a theorem; it identifies it as a valid next target.

---

## Boundary

```text
STAGE14_4BF=S5T_IMPORTED_LOCAL_EXPONENT_UPGRADED_AND_MAIN_TRACK_REFOCUSED
S5T_SAVING_OPTIMIZATION_IMPORTED=true
OLD_LOCAL_B_EXPONENT_1_OVER_400_SUPERSEDED=true
LOCAL_M_SCALE_SAVING_EXPONENT=1/41
UNWEIGHTED_LOCAL_B_SCALE_SAVING_EXPONENT=1/82
UNWEIGHTED_RHO_LOC=O_epsilon(B^(-1/82+epsilon))
UNWEIGHTED_E_LOC=0
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=true
EXPLICIT_COMPLETE_E_LOC_PROVED=true
ACTIVE_PHYSICAL_BASE_UPPER_BOUND=B^(81/82+epsilon)
ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED=true
OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL=false
ALL_SHORT_ABSOLUTE_TUPLE_SUM_IS_CURRENT_BOTTLENECK=true
NEW_ARITHMETIC_RESONANCE_FOUND=false
ONE_TARGETED_S5U_OPTIMIZATION_JUSTIFIED=true
MAIN_TRACK_WAITS_FOR_S5U=false
MAIN_TRACK_PRIMARY_FOCUS=POST_LOCAL_GLOBAL_SMALL_POINT_THINNING
CURRENT_SQRT_REMAINING_DELTA=20/41
CASE_C_REMOVED_CURRENT_AB_ARCHITECTURE_LOCAL_B_CEILING=1/10
CASE_C_REMOVED_CURRENT_AB_ARCHITECTURE_STILL_REQUIRES_POST_LOCAL_DELTA_GE_2/5=true
CHAMBER_D_LOC_DIAGNOSTIC_RELEVANT_TO_DIRECTION_LAW=true
CHAMBER_D_LOC_DIAGNOSTIC_REQUIRED_FOR_CURRENT_UPPER_BOUND=false
ARBITRARY_WEIGHT_LOCAL_RETAINER_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
DIRECT_POST_LOCAL_SMALL_POINT_RETAINER_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bg formulate and compare the separated global/Sha-plus-height retainer versus a direct post-local global-small-point retainer on the now-proved B^(81/82+epsilon) local majorant; select the first quantitatively attackable post-local theorem, importing s5u only if it has already produced a stronger merged local exponent
```
