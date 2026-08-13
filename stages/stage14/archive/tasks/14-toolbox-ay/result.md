# Stage14-toolbox-ay — first-consumer audit, unique top-corner intersection, and Pell-smooth fixed-U refresh

## Status

`COMPLETE_FIRST_CONSUMER_AUDIT_AND_UNIQUE_TOP_CORNER_PELL_REFRESH`

Stage14-toolbox-ax ended with the explicit instruction

```text
Stage14-toolbox-ay audit first 4cr/s7-31/t70 consumers against the five-eighths certificate.
```

This stage performs that audit on merged current main.  It does not re-prove the arithmetic in the consumer stages and it does not treat open draft work as a theorem source.  The purpose is to follow the first legal merged consumers far enough to identify the current global saturation packet and the current fixed-`U` receiver.

The audited chains are

```text
4cr   -> X9 / 4cs
s7-31 -> X9 / s7-32 / 4cs / t71
t70   -> t71

then current merged refinements

s7-32 + 4cs -> 4ct / X10
t71          -> t72.
```

The whole-family exponent stays `5/8`, but the geometry and both live receivers are substantially narrower than in toolbox-ax.

---

## 1. First consumers of 4cr

Merged `4cr` had promoted the temporary `2/3` bound and supplied the exact Cayley sign allocation

```text
C_* = C_- C_+,
gcd(C_-,C_+)=1,
```

with opposite/same Gaussian orientations on `C_-`/`C_+`.

Its first merged consumers are `X9` and `4cs`.

### X9

Merged `X9` imports the stronger `s7-31` theorem and replaces the old `2/3` saturation by a `5/8` upper/lower split.  In particular

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
```

and the old `TwoThirdsCayleyGaussianCommonGcdRootProductIncidence` is no longer minimal because merged s7-31 already makes the quotient gcd divisor-many after fixed outer data.

### 4cs

Merged `4cs` promotes the same `5/8` theorem to the mainline and identifies

```text
H = oddpart(gcd(X,Y))
  = oddpart(gcd(c_k^+,c_k^-)),

H^2 | C*u_res,
H^2 | X*Y.
```

It also sharpens the bad common-core part to

```text
C_bad | oddpart(r*s)^2 * H^2.
```

The two-boundary saturation metadata recorded in X9/4cs is valid at the point those stages are read in isolation, but it is not the current toolbox geometry after merged s7-32.

```text
FOUR_CR_FIRST_CONSUMERS_AUDITED=true
X9_FIVE_EIGHTHS_BOUNDARY_SPLIT_PROVED=true
FOUR_CS_FIVE_EIGHTHS_MAINLINE_PROMOTION_PROVED=true
FOUR_CS_TWO_BOUNDARY_SATURATION_METADATA_CURRENT=false
```

No `2/3` receiver is promoted back into the current barrier.

---

## 2. First consumers of s7-31

Merged `s7-31` proves

```text
V(B) << B^(5/8+o(1))
```

by the fixed-outer square-divisor lock

```text
oddpart(h)^2 | C*u_res.
```

Its first merged consumers are `X9`, `s7-32`, `4cs`, and `t71`.

`X9` and `4cs` are handled above.  The decisive global consumer is `s7-32`.

### s7-32 collapses the two apparent barriers to one top corner

Merged `s7-32` supplies two alternative one-host counts

```text
E_k(theta)  <= 3*theta-1/4,
E_xi(phi)   <= 3*phi-1/8,
```

and combines them with

```text
E_s(theta)=max(2*theta,1-2*theta).
```

Therefore

```text
E(theta,phi)
 <= min(max(2theta,1-2theta),3theta-1/4,3phi-1/8)
 <= 5/8,
```

with equality only at

```text
(theta,phi)=(5/16,1/4).
```

Consequently the toolbox-ax receiver

```text
FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence
```

is historical.  The lower `(3/16,3/16)` corner and the upper-edge continuum `phi<1/4` are already power-saved.

The first exact top-corner receiver is

```text
TopCornerCommonCoreXiGaussianSquareHostPrimitiveAgreementIncidence.
```

The current global exponent remains `5/8`; this is a localization of the equality set, not a new exponent saving.

---

## 3. Two independent merged refinements of the unique top corner

After s7-32, merged `4ct` and merged `X10` attack the same surviving physical top-corner packet from different exact coordinates.  Neither theorem may be used as an independent multiplicative saving.  However, every packet that can still saturate `5/8` must satisfy the necessary conditions proved by both, so their filters may be intersected at zero counting cost.

### 4ct: primitive residual Gaussian host

Merged `4ct` peels the odd coordinate gcd `g` of the xi residual host and proves that every fixed-power `g` branch is strictly saved:

```text
E_host <= 5/8-rho,
g=B^(rho+o(1)).
```

Thus a saturating packet requires

```text
g=B^o(1),
C_good=B^(3/8+o(1)).
```

The good common core lifts to a canonical Gaussian divisor

```text
W_S = g * Pi_C * T_C,
N(Pi_C)=C_good,
oddpart(N(T_C))=v_res_odd/d.
```

Its live receiver is

```text
TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence.
```

### X10: small root gcd, dominant Cayley orientation, short cofactor

Merged `X10` combines the s7-32 top corner with the 4cs root gcd and the 4cr same/opposite Cayley orientation split.

If

```text
H=oddpart(gcd(X,Y))=B^(h+o(1)),
```

then the k-one-host bound gives

```text
E_k(h)<=11/16-h.
```

Hence a potentially saturating packet must satisfy

```text
H<=B^(1/16+o(1)).
```

On this branch

```text
C_bad<=B^(1/8+o(1)),
C_*>=B^(1/4-o(1)),
C_sigma=max(C_-,C_+)>=B^(1/8-o(1)),
```

and for the corresponding Cayley sign

```text
t_sigma=|M sigma N|/C_sigma<=B^(1/8+o(1)).
```

The dominant factor is the norm of a shared same/opposite-orientation Gaussian divisor `Pi_sigma`.

Its live receiver is

```text
TopCornerSmallRootGcdDominantCayleyGaussianShortCofactorIncidence.
```

### Legal toolbox intersection

The two reductions are not declared equivalent.  They constrain different coordinates of the same surviving physical top-corner packet.  Since each theorem says that its discarded complement is already fixed-power saved, any genuine `5/8` saturation packet must lie in their intersection.

Toolbox-ay therefore records the combined survivor predicate as

```text
TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence.
```

This name is a toolbox receiver label for the intersection of already-proved necessary filters.  It is **not** a new incidence theorem and it does not multiply the 4ct and X10 gains.

The retained data include simultaneously

```text
(theta,phi)=(5/16,1/4),
C=B^(3/8+o(1)),
u_res,v_res<=B^(1/8+o(1)),
q_xi=C*v_res,
Z_S=lambda_S^2 W_S,
W_S=g*Pi_C*T_C,
g=B^o(1),
N(Pi_C)=C_good=B^(3/8+o(1)),
H<=B^(1/16+o(1)),
C_sigma>=B^(1/8-o(1)),
t_sigma<=B^(1/8+o(1)),
N(Pi_sigma)=C_sigma,
primitive xi-agreement root orientation,
full reciprocal physical masks.
```

No exact identity between `Pi_C` and `Pi_sigma` is asserted here.  That comparison remains a future arithmetic task.

---

## 4. First consumer of t70 and current fixed-U receiver

Merged `t70` leaves the fixed-`U` small-common-support receiver

```text
SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy.
```

Its first merged consumer is `t71`.

### t71 restores the Gaussian component transfer

Merged `t71` proves the exact 45-degree Gaussian linearization and transfers the whole same-squareclass kernel `kappa` into four signed numerator/denominator component cells.  It also proves

```text
gcd(J,kappa)=1,
```

so the t70 small-`J` condition does not erase the new kappa transfer.

The intermediate receiver becomes

```text
SharedUSmallCayleySupportGaussianSquareclassFourCellEnergy.
```

### t72 closes large odd kappa and isolates Pell-smooth energy

Merged `t72` proves that the signed split is already encoded by the reduced denominator:

```text
beta=gcd(kappa,v),
alpha=kappa/beta.
```

For a same-kappa pair, the whole odd part `K=oddpart(kappa)` CRT-compresses to one Cayley root line.  The fixed-anchor bound

```text
#partners <= (1+Z/K) B^o(1)
```

closes the large-`K` branch near-linearly.

The surviving small-kappa branch is reduced to the physical real-quadratic norm equations

```text
x^2-kappa*y^2 = beta*eta*Pminus,
x^2+kappa*y^2 = beta*eta*Pplus,
```

with the canonical largest-prime and smooth-companion filters retained:

```text
ell=LPF_odd(Pplus*Pminus),
v_ell(Pminus)=1,
2*oddpart(Pminus/ell)<ell,
all noncanonical odd support < ell.
```

The current fixed-`U` receiver is therefore

```text
SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy.
```

Unlike toolbox-ax, the current merged t-line now genuinely requests an independent theorem audit:

```text
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy.
```

This is a tH request, not a new toolbox-H line.  The t route is explicitly not blocked while the audit runs.

---

## 5. Cross-route promotion decision

The global top-corner receiver and the fixed-`U` Pell-smooth receiver remain different coefficient spaces.

No exact adapter has been proved from

```text
fixed-U same-kappa Pell/smooth energy
```

to

```text
moving top-corner common-core / xi residual Gaussian host incidence.
```

Merged 4ct explicitly refuses the earlier t71 cross-promotion, and t72 does not add such an adapter.  Therefore

```text
T72_CROSS_PROMOTED_TO_GLOBAL_TOP_CORNER=false
GLOBAL_AND_FIXED_U_RECEIVERS_EQUIVALENT=false.
```

The tH19 result, when available, must first be consumed by the t route.  It cannot be promoted into the global `5/8` theorem merely because both routes use Gaussian or quadratic-norm language.

---

## 6. Open-work guard

PR #531 (`Stage14-s7-33`) is currently an open draft exploratory branch.  It probes shared common-core Gaussian orientation at the unique top corner, but it is not merged and does not yet replace the merged theorem chain.

Therefore

```text
OPEN_S7_33_DRAFT_USED_AS_CANONICAL_SOURCE=false.
```

The toolbox receiver must continue to use only merged `s7-32`, `4ct`, and `X10` certificates until a later s7-33 theorem is actually merged.

---

## 7. Supervisor decision

The current ledger is

```text
WHOLE FAMILY:
V(B) << B^(5/8+o(1))
unique possible saturation: (theta,phi)=(5/16,1/4)

GLOBAL TOOLBOX SURVIVOR:
TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence

FIXED-U/T:
SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy
```

No toolbox-specific H continuation is opened.  The global route still has unused exact arithmetic (`Pi_C` versus Cayley orientation, short cofactor, primitive agreement), while the fixed-`U` route has already isolated the genuine tH19 theorem target.

The next toolbox audit should follow the first merged consumers of `4ct`, `X10`, and `t72`, and consume the tH19 result if it has become available.  It must also continue to reject open/draft stages as canonical theorem sources.

---

## Boundary

```text
STAGE14_TOOLBOX_AY=COMPLETE_FIRST_CONSUMER_AUDIT_AND_UNIQUE_TOP_CORNER_PELL_REFRESH
MERGED_TOOLBOX_AX_IMPORTED=true
FIRST_4CR_CONSUMERS_AUDITED=true
FIRST_S7_31_CONSUMERS_AUDITED=true
FIRST_T70_CONSUMER_AUDITED=true
X9_FIVE_EIGHTHS_BOUNDARY_SPLIT_PROVED=true
FOUR_CS_FIVE_EIGHTHS_MAINLINE_PROMOTION_PROVED=true
S7_32_UNIQUE_TOP_CORNER_LOCALIZATION_PROVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
CURRENT_GAP_TO_SQRT=1/8
FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=1
UNIQUE_FIVE_EIGHTHS_SATURATION_THETA=5/16
UNIQUE_FIVE_EIGHTHS_SATURATION_PHI=1/4
OLD_AX_TWO_BOUNDARY_RECEIVER_CURRENT=false
FOUR_CS_TWO_BOUNDARY_SATURATION_METADATA_CURRENT=false
S7_32_TOP_CORNER_RECEIVER_CURRENT_BASE=true
FOUR_CT_PRIMITIVE_RESIDUAL_GAUSSIAN_CORE_REDUCTION_PROVED=true
X10_SMALL_ROOT_GCD_DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION_PROVED=true
FOUR_CT_AND_X10_FILTERS_SIMULTANEOUSLY_APPLICABLE_TO_SATURATING_PHYSICAL_PACKET=true
CURRENT_GLOBAL_TOOLBOX_RECEIVER=TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence
CURRENT_GLOBAL_TOOLBOX_RECEIVER_PROVED=false
T71_GAUSSIAN_SQUARECLASS_TRANSFER_PROVED=true
T72_LARGE_ODD_KAPPA_BRANCH_NEAR_LINEAR=true
CURRENT_FIXED_U_RECEIVER=SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy
CURRENT_FIXED_U_RECEIVER_PROVED=false
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
T72_CROSS_PROMOTED_TO_GLOBAL_TOP_CORNER=false
GLOBAL_AND_FIXED_U_RECEIVERS_EQUIVALENT=false
OPEN_S7_33_DRAFT_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_H_CONTINUATION_NEEDED=false
TOOLBOX_ROUTE_BLOCKED=false
NEW_AY_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-toolbox-az audit first 4ct/X10/t72 consumers and tH19 outcome against the unique-top-corner certificate
```