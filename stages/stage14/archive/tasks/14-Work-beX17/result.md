# Stage14-Work-beX17 — integrated toolbox-be and X17 centered-degree interface audit

## Status

`COMPLETE_POST_BDX16_CUMULANT_WALSH_PARITY_INTERFACE_AND_NO_CROSS_PROMOTION`

This integrated Work stage consumes only merged sources on latest main through

```text
Stage14-Work-bdX16,
Stage14-4dj -> Stage14-4dk,
Stage14-s7-52 -> Stage14-s7-53,
Stage14-t92 -> Stage14-t93,
Stage14-tH26,
Stage14-X15.
```

The source main SHA is

```text
88cd710b54e99d66b35cad764ac8483f2303677c.
```

No draft/open/unmerged descendant is imported as a theorem source.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here.

---

## 1. Why the Work gate is RUN rather than WAIT

The previous integrated boundary `Stage14-Work-bdX16` audited through

```text
mainline: Stage14-4di / 4diH,
s route : Stage14-s7-51 / sH50,
fixed U : Stage14-t91 / tH26.
```

Current merged main has advanced materially to

```text
mainline: Stage14-4dk,
s route : Stage14-s7-53,
fixed U : Stage14-t93.
```

Thus mainline, s and fixed-U have each gained two substantive deterministic consumers, and both live receivers have changed form.  The canonical Work start gate is therefore satisfied.

```text
STAGE14_WORK_TOOLBOX_X_GATE=RUN
PREVIOUS_INTEGRATED_STAGE=Stage14-Work-bdX16
CURRENT_INTEGRATED_STAGE=Stage14-Work-beX17
```

The numbering is derived from merged history:

```text
toolbox-bd -> toolbox-be,
X16 -> X17.
```

---

## 2. Toolbox-be component — current global receiver

Merged 4dj proves that every fixed-power deficit in exact principal cell occupancy already gives the same fixed-power saving.  Hence any square-root-saturating principal sequence must satisfy

```text
omega(c)=B^(-o(1)).
```

Merged s7-52 then removes boundary-variance three-way cells.  On a genuinely three-projection saturating cell,

```text
mu_j=B^(-o(1)),
1-mu_j=B^(-o(1)),
Var(W_j)=B^(-o(1))
```

for `j in {+,-,k}`.

Merged 4dk intersects these two reductions.  The surviving cells are simultaneously

```text
full conductor,
near-maximal principal occupancy,
interior in all three selector marginals.
```

Merged s7-53 then splits the signed obstruction exactly into

```text
A. positive near-maximal principal occupancy,
B. at least one pairwise covariance Gamma_ij=B^(-o(1)),
C. all pairwise covariances power-small but connected kappa_3=B^(-o(1)).
```

Therefore the current global receiver is not one undifferentiated covariance object.  Its canonical toolbox-be form is

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagorean
PrincipalOrPairwiseCovarianceOrConnectedThirdCumulant.
```

This is a strict receiver contraction relative to bdX16, not an exponent improvement.

```text
GLOBAL_PRINCIPAL_BRANCH_RETAINED=true
GLOBAL_PAIRWISE_BRANCH_SEPARATED=true
GLOBAL_CONNECTED_THIRD_CUMULANT_BRANCH_SEPARATED=true
GLOBAL_BOUNDARY_OCCUPANCY_REMOVED=true
GLOBAL_BOUNDARY_VARIANCE_THREE_WAY_OBSTRUCTION_REMOVED=true
```

---

## 3. Toolbox-be component — current fixed-U receiver

Merged t92 gives the exact Walsh decomposition of the generic split-prime orientation cube

```text
epsilon in {+1,-1}^r,
C_U(epsilon)=sum_S hat C_U(S) chi_S(epsilon).
```

The empty-set coefficient

```text
mu_U=hat C_U(emptyset)
```

is the principal cube mean.  Centering removes only this constant mode from the oscillatory remainder; no bounded Walsh degree follows from the inherited physical masks.

Merged t93 adds the exact conjugation antipode

```text
epsilon -> -epsilon.
```

Because

```text
chi_S(-epsilon)=(-1)^|S| chi_S(epsilon),
```

the physical coefficient splits into exact even and odd Walsh sectors.  The odd sector is antipodally centered and sums to zero.  The principal mean lies in the even sector and is not killed by conjugation.  The centered even nonconstant spectrum also remains.

Hence the current fixed-U receiver is

```text
SharedUCanonicalLPFPrincipalEvenOccupancyPlusCenteredEvenOrientationCorrelation.
```

The live fixed-U obstruction has therefore contracted from arbitrary centered Walsh spectrum to the even sector only.

```text
FIXED_U_ODD_WALSH_SECTOR_ELIMINATED=true
FIXED_U_PRINCIPAL_MEAN_SURVIVES=true
FIXED_U_CENTERED_EVEN_SPECTRUM_SURVIVES=true
BOUNDED_WALSH_DEGREE_PROVED=false
```

No tH27 is justified by this contraction alone.

---

## 4. X17 test — compare correlation degree, not coordinate vocabulary

The natural cross-route temptation is to identify

```text
global pairwise covariance <-> Walsh degree 2,
global connected kappa_3    <-> Walsh degree 3,
```

because both sides use centered Boolean functions.

There is a valid algebraic analogy:

- a centered two-selector product is a degree-two multilinear monomial;
- a centered three-selector product is a degree-three multilinear monomial;
- on the fixed-U cube, Walsh characters are multilinear monomials indexed by subsets;
- conjugation annihilates the odd parity sector of the fixed-U coefficient.

This gives a common **degree/parity language**.

```text
COMMON_CENTERED_MULTILINEAR_DEGREE_LANGUAGE_PROVED=true
```

But it does not give a common charged-once arithmetic adapter.

The global variables are the three physical selector values

```text
(W_+,W_-,W_k)
```

on conditioning cells indexed by quarter-pair / conductor / Pythagorean data.  The fixed-U variables are the `r=omega(delta_G)` independent Gaussian split-prime orientation bits after fixing

```text
(U,epsilon,k,h,kappa,beta,Q,...).
```

No merged theorem constructs a measure-preserving map, finite-fiber map, character pullback, or common modulus carrying

```text
Gamma_ij or kappa_3
```

to

```text
hat C_U(S).
```

The dimensions also differ: global has exactly three selector coordinates, while fixed-U has a moving `r`-dimensional orientation cube.  Formal polynomial degree therefore cannot be charged as a common saving mechanism.

```text
GLOBAL_SELECTOR_SPACE_DIMENSION=3
FIXED_U_ORIENTATION_CUBE_DIMENSION=r_moving
GLOBAL_FIXED_U_BOOLEAN_SPACES_IDENTIFIED=false
GLOBAL_FIXED_U_MEASURES_IDENTIFIED=false
GLOBAL_CUMULANT_TO_WALSH_COEFFICIENT_MAP_PROVED=false
COMMON_ADAPTER_PROVED=false
```

---

## 5. Antipodal cancellation does not transfer to the global connected branch

A second tempting transfer is to use the t93 antipode to eliminate the global odd-degree connected term `kappa_3`.

That transfer is invalid on current merged data.  The fixed-U antipode is simultaneous Gaussian conjugation of every generic split-prime orientation bit.  No merged global theorem supplies an involution of the physical quarter-pair conditioning cell which simultaneously sends

```text
X_+ -> -X_+,
X_- -> -X_-,
X_k -> -X_k
```

while preserving the physical measure and all reciprocal/orientation masks.

In fact the global centered variables are deviations of nonnegative selector indicators from their conditional means, not independent orientation signs.  Thus odd multilinear degree does not imply antipodal cancellation.

```text
GLOBAL_THREE_SELECTOR_ANTIPODE_PROVED=false
GLOBAL_CONNECTED_KAPPA3_KILLED_BY_PARITY=false
T93_ANTIPODAL_CANCELLATION_CROSS_PROMOTABLE=false
```

This no-go is the principal X17 result.

---

## 6. What is genuinely shared

After beX17, the common interface can be stated more sharply than in bdX16:

```text
positive principal component
+
centered multilinear correlation decomposed by degree/parity.
```

On the global side the live signed degrees are explicitly separated into degree two and connected degree three.  On the fixed-U side conjugation removes odd Walsh parity, leaving principal degree zero and centered even degrees `2,4,6,...` (with no bounded-degree theorem).

Therefore the intersection of the two formal analytic languages is the **principal plus centered even-order correlation template**.  This is useful for theorem bookkeeping and for deciding which future estimates are even structurally eligible.

It is not an arithmetic bridge and cannot promote a fixed-U saving to the whole family.

```text
COMMON_PRINCIPAL_PLUS_CENTERED_EVEN_ORDER_TEMPLATE=true
COMMON_TEMPLATE_IS_ARITHMETIC_BRIDGE=false
SAVING_CROSS_PROMOTABLE=false
```

Notably, even if a future t-stage kills every centered even Walsh coefficient, its fixed-packet quantifier order would still have to be legally summed over `U` and the other fixed packet variables before affecting the global exponent.

---

## 7. Supersession and charged-once audit

The following prior structures remain charged exactly once:

```text
X15 primitive Pythagorean cone,
X15 three complete exponent-1/2 coordinate systems,
4dj principal occupancy deficit,
s7-52 boundary variance peel,
s7-53 pairwise/connected cumulant decomposition,
t92 Walsh decomposition,
t93 conjugation parity split.
```

beX17 does not multiply the 4dj and s7-52 savings; it intersects their survivor conditions.  It does not recharge the X15 cone.  It does not treat the three X15 coordinate systems as independent counts.  It does not identify formal cumulant degree with fixed-U Walsh degree as a counting equivalence.

```text
X15_COMPLETE_COORDINATE_COUNTS_MULTIPLICABLE=false
PYTHAGOREAN_CONE_FRESH_SAVING_ALLOWED=false
OCCUPANCY_AND_VARIANCE_SAVINGS_MULTIPLIED=false
CUMULANT_AND_WALSH_DEGREE_COUNTS_MULTIPLIED=false
```

---

## 8. H decisions

### Mainline

No new mainline H is requested.  The current global split is still undergoing deterministic reduction: s7-53 explicitly directs the pairwise branch back into the existing two-projection coordinates before any new theorem audit.  A theorem target frozen before this pairwise audit would be premature.

```text
MAINLINE_H_NEEDED=false
MAINLINE_H_TARGET=NONE_DETERMINISTIC_PAIRWISE_REDUCTION_NOT_EXHAUSTED
```

### s route

No new s H is requested.  The merged next step is deterministic `Stage14-s7-54`, which must test the three pairwise branches against already-proved mixed-root/full-conductor finite-fiber structure.

```text
S_ROUTE_H_NEEDED=false
S_ROUTE_H_TARGET=NONE_PAIRWISE_COORDINATE_AUDIT_PENDING
```

### fixed U

No new fixed-U H is requested.  t93 has removed odd Walsh parity but has not proved bounded degree, a decaying even-degree tail, or multiplicativity of the surviving even spectrum.  Until t94 or a descendant creates a theorem-ready even-spectrum object, tH27 would be underspecified.

```text
FIXED_U_H_NEEDED=false
FIXED_U_H_TARGET=NONE_EVEN_WALSH_COMPLEXITY_NOT_YET_REDUCED
TH27_NEEDED=false
```

---

## 9. Current receivers

Global:

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagoreanPrincipalOrPairwiseCovarianceOrConnectedThirdCumulant
```

Fixed U:

```text
SharedUCanonicalLPFPrincipalEvenOccupancyPlusCenteredEvenOrientationCorrelation
```

Common formal interface:

```text
PrincipalPlusCenteredMultilinearDegreeParityCorrelationTemplate
```

The first two are not equivalent.

---

## 10. Whole-family ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

The progress is receiver contraction and a cross-route no-go/eligibility theorem, not a new exponent.

---

## 11. Next revisit condition

Do not rerun the permanent Work task after only one immediate successor.

The normal revisit condition is:

```text
mainline merged through at least Stage14-4dm,
s route merged through at least Stage14-s7-55,
fixed-U merged through at least Stage14-t95,
```

or earlier if one of the following occurs:

```text
1. a strict whole-family exponent improvement;
2. a new H/tH audit with nonzero certified delta;
3. a proof that one global pairwise covariance branch collapses to finite fibers;
4. a proof of bounded/effectively truncated even Walsh degree on fixed U;
5. an explicit arithmetic map between global selector correlations and fixed-U orientation characters.
```

---

## Locked boundary

```text
STAGE14_WORK_BEX17=COMPLETE_POST_BDX16_CUMULANT_WALSH_PARITY_INTERFACE_AND_NO_CROSS_PROMOTION
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
TOOLBOX_BE_COMPONENT_COMPLETE=true
X17_COMPONENT_COMPLETE=true
AUDITED_THROUGH_MAINLINE=Stage14-4dk
AUDITED_THROUGH_S_ROUTE=Stage14-s7-53
AUDITED_THROUGH_FIXED_U=Stage14-t93_and_tH26
PREVIOUS_INTEGRATED_STAGE=Stage14-Work-bdX16
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_GLOBAL_RECEIVER=FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagoreanPrincipalOrPairwiseCovarianceOrConnectedThirdCumulant
CURRENT_FIXED_U_RECEIVER=SharedUCanonicalLPFPrincipalEvenOccupancyPlusCenteredEvenOrientationCorrelation
COMMON_CENTERED_MULTILINEAR_DEGREE_LANGUAGE_PROVED=true
COMMON_PRINCIPAL_PLUS_CENTERED_EVEN_ORDER_TEMPLATE=true
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
GLOBAL_THREE_SELECTOR_ANTIPODE_PROVED=false
T93_ANTIPODAL_CANCELLATION_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH27_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=4dm_and_s7-55_and_t95_or_material_early_trigger
```
