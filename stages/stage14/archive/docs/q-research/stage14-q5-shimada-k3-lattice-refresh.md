# Stage14-q5 — Shimada K3 / lattice computational refresh

## Status

```text
STAGE14_Q5=COMPLETE_SHIMADA_K3_LATTICE_REFRESH
CHECKED_AT=2026-08-09
TRIGGER_STAGE=Stage14-4 current analytic frontier after 4ak geometric closure
EXACT_OBSTRUCTION=determine whether any unused level-4 K3/lattice literature or machine data still closes a live Stage14 gap
SHIMADA_FIXED_CURVE_PACKAGE_CONSUMED=true
PHYSICAL_M_IN_S0_BASIS_KNOWN=true
PHYSICAL_DECK_MATRIX_IDENTIFIED=true
ANTI_INVARIANT_LATTICE_ENUMERATED=true
REQUIRED_PARITY_COSET_EMPTY=true
UNUSED_SHIMADA_DATA_IS_LIVE_BLOCKER=false
DIRECT_NEW_GEOMETRIC_WEAPON_COUNT=0
RESERVE_METHOD_COUNT=1
NEXT=Stage14-q6 cross-track weapon test
```

## Purpose

Stage14-q5 refreshes the geometric/lattice literature radar after the Stage14-4 main line moved far beyond the original PR #185 Shimada handoff. The question is narrow:

> Is there still a live Stage14 geometric/lattice obstruction that can be closed by a piece of Shimada's level-4 modular K3 computation package, or by a newer exact K3 automorphism/Mordell--Weil computation that has not yet been consumed?

The answer is **no for the current frontier**. The exact Shimada package was not merely cited: it was already converted into a fixed-basis Stage14 computation in 14-4aj/4ak, and the fixed `M`-degree-4 curve mechanism was killed before the later Galois/effectivity filters were needed.

This q-stage therefore closes a literature-surveillance loop rather than reopening the K3 route.

## 1. Primary-source assets rechecked

### 1.1 Ichiro Shimada, level-4 modular K3 — DIRECT / CONSUMED

Primary paper:

- Ichiro Shimada, *The elliptic modular surface of level 4 and its reduction modulo 3*, Ann. Mat. Pura Appl. 199 (2020), 1457--1489; arXiv:1806.05787.

Author-hosted computation page still exposes the paper, explanation, and the exact computational files

```text
S0S3.txt
PGU.txt
Borcherds.txt
Enriques.txt
```

as well as a zipped archive.

The paper identifies the level-4 modular surface as a Picard-rank-20 K3 and computes its automorphism group via the Neron--Severi lattice and reduction modulo 3. This is the correct classical K3 underlying the Stage14 Pythagorean elliptic family after the already-locked base change.

Classification: `DIRECT / CONSUMED`.

### 1.2 Shimada 2024 Mordell--Weil/automorphism method — RESERVE

Primary paper:

- Ichiro Shimada, *Mordell--Weil groups and automorphism groups of elliptic K3 surfaces*, Rev. Mat. Iberoam. 40 (2024), 1469--1503; arXiv:2210.01328.

The author's computation page supplies `CompDataXfg.txt` and an explanation. The paper gives a method for calculating the action of an elliptic K3 Mordell--Weil group on the numerical Neron--Severi lattice.

For Stage14 this is a **reserve method**, not a current direct weapon. The live 14-4 obstruction is no longer an unidentified elliptic fibration or an uncomputed Mordell--Weil action; it is an analytic family-average problem. Reopening a full automorphism/MW computation would therefore be unjustified unless a future stage produces a new explicit low-degree geometric class or alternative fibration whose orbit structure must be computed.

Classification: `RESERVE / NEAR only if a new geometric trigger appears`.

## 2. What Stage14 already consumed from Shimada

The q1 ledger was conservative because it only knew that the Shimada package was computationally actionable. The merged 14-4 chain has since consumed the package in detail.

### 2.1 Level-4/Kummer identification — consumed in 14-4ag

The Stage14 elliptic surface

```text
Y^2 = X(X-1)(X+t^2)
```

was explicitly identified with Shimada's level-4 modular K3 after a base change over `Q(i)`, and over `C` with the relevant Kummer surface. The K3 reference is therefore not merely analogous geometry; it is the actual geometric model used by Stage14.

### 2.2 Physical height/polarization — consumed in 14-4ah

The physical cuboid height was matched to the Kummer divisor

```text
M = pi^*(-K_Y),
M^2 = 8,
H_M(P)=d.
```

This reduced a potential fixed-curve `sqrt(B)` source to rational curves with the extremal pattern

```text
M.C = 4,
deg(C -> P1_r)=2.
```

### 2.3 Intrinsic bisection reduction — consumed in 14-4ai

All degree-four fixed rational-curve mechanisms except a split singular anticanonical case were eliminated intrinsically. The sole remaining target was converted into an exact NS-lattice problem.

### 2.4 Fixed-basis Shimada interface — consumed in 14-4aj

Stage14 locked the exact deck involution on the elliptic fiber as

```text
delta(P) = (0,0)-P
         = tau_(0,0) o [-1],
```

then mapped it to Shimada's torsion-translation and inversion matrices.

The physical class was reduced to a finite label search using published objects including

```text
GramS0
L40vs
SixFs
fsigma
AutX0h0
AutX0f
MWtorsigmaz
Tsigma
iotasigmaz
```

with the published row-vector/right-action convention.

### 2.5 Physical `M` and deck labels — fully known in 14-4ak

A representative complete labeling is frozen as

```text
f_s = [0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
M   = [1,-1,1,-1,0,0,0,2,0,2,2,2,0,2,2,0,0,0,0,0]
deck 2-torsion label = [0,2]
```

The alternative surviving labeling is `AutX0f`-equivalent. Thus the q1 uncertainty

```text
physical class M in Shimada S0 basis = unknown
```

is obsolete. It is now known exactly.

## 3. The decisive lattice computation is already complete

For a hypothetical split component `C`, Stage14 introduced

```text
x = 2C-M.
```

The exact conditions become

```text
delta(x) = -x
x^2 = -16
x = M mod 2.
```

The saturated anti-invariant lattice has

```text
rank = 6
positive-form determinant = 256
```

and exact vector census

```text
norm 0  : 1
norm 4  : 60
norm 8  : 252
norm 12 : 544
norm 16 : 1020
```

but

```text
parity-compatible norm-16 vectors = 0.
```

The conclusion is stronger than a failed rational-descent filter: the necessary **integral Neron--Severi class does not exist**.

Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

is already a completed geometric result.

## 4. Apparent unused data are not unresolved obligations

PR #185 / 14-4aj mentioned additional objects such as

```text
Wout0
Galmu
zsigma
PGU.txt
Enriques.txt
```

and later effectivity, chamber, Galois-descent, irreducibility, and physical-open filters.

q5 classifies these carefully.

### 4.1 `Wout0` / chamber-effectivity machinery — NOT NEEDED FOR CLOSED TARGET

These data would matter if an integral root candidate survived and Stage14 needed to decide effectivity/chamber membership. The parity-compatible root set is empty, so there is no candidate to filter.

This is not an unproved hypothesis.

### 4.2 `Galmu` / rational-descent machinery — NOT NEEDED FOR CLOSED TARGET

Likewise, Galois descent would be needed only after a geometric NS class survived. The integral parity-coset void occurs earlier, so failure to run `Galmu` on nonexistent candidates cannot reopen the result.

### 4.3 `PGU.txt` / reduction-mod-3 machinery — BACKGROUND / ALREADY ENCODED UPSTREAM

Shimada's reduction-mod-3 and Borcherds setup is the engine behind the published automorphism/lattice data. Stage14 does not currently need a second independent reconstruction of the entire automorphism group from `PGU.txt`; it consumed the exact published NS/action outputs needed for the finite label/orbit problem.

### 4.4 `Enriques.txt` — BACKGROUND

The Enriques involution data are valuable for the paper's own Enriques-surface results but do not currently target the Stage14 physical deck involution or analytic family-average obstruction. No Stage14 theorem gate should be invented merely to consume this file.

## 5. Current 14-4 frontier is no longer a K3 classification problem

After the fixed-curve mechanism was rejected, the main line returned to the moving specialization problem. By the current `14-4ax` frontier the live obstacles are analytic:

```text
MEDIUM_DETERMINANT_DISPERSION
MICROSCOPIC_SMALL_SIDE_INDUCTION
NORM_MIXED_SIGN_D_TIMES_S_DISPERSION
```

followed by the already-separated global/Sha and first-small-point height retainers.

None of these is naturally an NS-lattice enumeration, automorphism-orbit, or Galois-descent problem on the fixed level-4 K3.

Therefore the correct q5 decision is:

```text
DO_NOT_REOPEN_GENERIC_K3_SEARCH=true
DO_NOT_REENUMERATE_M_DEGREE4_CURVES=true
DO_NOT_TREAT_UNUSED_SHIMADA_FILES_AS_PROOF_GAPS=true
```

## 6. When to reactivate the K3 weapon shelf

The Shimada/K3 route should be reopened only on a named geometric trigger. Valid triggers include:

1. a new fixed rational/multisection mechanism of a different `M`-degree;
2. an explicit alternative elliptic fibration whose MW action could reduce a new orbit problem;
3. a surviving algebraic curve class requiring `Wout0` effectivity or `Galmu` rational descent;
4. a proof that the analytic exceptional set is supported on finitely many algebraic curves, requiring classification of those curves;
5. a triple/square-value stage that produces a concrete fixed K3 correspondence whose automorphism orbit can reduce the parameter space.

Without one of these triggers, further broad K3 literature search is low-value relative to the active analytic tasks.

## 7. Direct handoff to q6

q6 should treat the geometric shelf as a **completed negative weapon**:

```text
SHIMADA_K3_FIXED_CURVE_WEAPON
  input: potential fixed M-degree-4 sqrt(B) mechanism
  output: impossible; required NS parity coset empty
  status: CONSUMED / CLOSED
```

It should not send another 14-4 worker back into Shimada's package unless a new geometric trigger appears.

The positive cross-track weapons carried forward to q6 are instead:

- q2: separated Jacobi large sieve / Wilson hyperbolic bilinear tools plus dispersion escalation;
- q3: Le Boudec-style large-prime + complete-2-descent small-point architecture;
- q4: square/polynomial sieve for the t-track collision cover;
- q5: Shimada fixed-curve K3 mechanism is closed and should be used as a **negative routing result**, preventing wasted geometric work.

## Decision

The original PR #185 Shimada lead was highly valuable and was successfully consumed. There is no forgotten direct K3/lattice theorem currently blocking Stage14.

```text
STAGE14_Q5=COMPLETE_SHIMADA_K3_LATTICE_REFRESH
SHIMADA_LEVEL4_PRIMARY_DATA_RECHECKED=true
PHYSICAL_M_IN_S0_BASIS_KNOWN=true
SHIMADA_FIXED_CURVE_PACKAGE_CONSUMED=true
REQUIRED_NS_PARITY_COSET_EMPTY=true
POST_ROOT_EFFECTIVITY_FILTER_REQUIRED=false
POST_ROOT_GALOIS_FILTER_REQUIRED=false
NEW_DIRECT_K3_LATTICE_WEAPON_FOR_CURRENT_FRONTIER=false
SHIMADA_2024_MW_AUTOMORPHISM_METHOD=RESERVE_ONLY
NEXT=Stage14-q6 cross-track weapon test
```
