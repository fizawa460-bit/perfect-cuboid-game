# Stage25-60 R504 exceptional Prym external-gate discovery ledger

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

## Repository reuse preflight

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=PR992_COMPLETE_Q_DEGREE2_DESCENT;PR993_NONSPLIT_RANK_JUMP;PR994_SECOND_SECTION;PR995_MOD2_PHYSICAL_COSET;PR996_GROWING_RANK_TWO_HEIGHT;PR997_GENERIC_PRYM_E0_OBSTRUCTION;R504_FULL_SPLIT_NORMAL_FORM
STRONGER_PRIOR_RESULT_FOUND=false
```

The closest current result is PR #997: it removes the generic K-defined `E0` factor but explicitly leaves the exceptional rational specialization/Hom-isogeny jump locus open.  The full-split normal-form artifact already closes the reciprocal/commuting-involution mechanism and warns that non-bielliptic isogeny factors need not arise from an involution.

## Current-round search

```text
SEARCH_TERMS=PRYM;E0;ISOGENY;HECKE;HUMBERT;EXCEPTIONAL;SPECIALIZATION;CM;UNLIKELY_INTERSECTION
STRUCTURAL_SIGNATURES=GENUS3_DOUBLE_COVER;DIMENSION2_PRYM;FIXED_CM_ELLIPTIC_FACTOR;UNBOUNDED_ISOGENY_DEGREE
TARGETED_COMPUTATION=PGL2_F7_F11_EXACT_FROBENIUS_SIEVE
FINITE_DATA_USED_AS_PROOF=false
```

No repository artifact supplies an a priori bound on the isogeny degree of a possible exceptional `E0` factor, nor a theorem controlling rational points on the union over all such degrees.

## New reduction

The projective matrix parameter has dimension three.  Source scaling `u -> lambda*u` multiplies the first matrix column by `lambda^2` and gives an isomorphic cover.  Thus the effective Prym-moduli image is generically two-dimensional; two dense-chart invariants are `AB/(CD)` and `AD/(BC)`.

For each fixed isogeny/homomorphism complexity `N`, the `E0`-factor condition is a proper algebraic Hecke/Humbert-type locus because PR #997 proves the generic Hom group to `E0` is zero.  The unresolved set is the union over unbounded `N`.

A finite symbolic search in `N` therefore cannot close the route without an independent global degree bound.

## Finite-field hostile search

The exact verifier enumerates all projective invertible matrices over two inert primes for `Q(i)`:

```text
p=7:  |PGL2(F_p)|=336;  E0 Frobenius-factor hits=36
p=11: |PGL2(F_p)|=1320; E0 Frobenius-factor hits=80
```

Every hit belongs to the already classified reciprocal divisor `(AB-CD)(AB+CD)(AD+BC)=0` modulo the tested prime.  This is recorded only as evidence that no obvious low-complexity non-bielliptic branch was missed.  It is not used to infer a characteristic-zero containment theorem.

## External theorem-class check

Primary-literature theorem classes matching the remaining shape include:

- Martin Orr, *Unlikely intersections with Hecke translates of a special subvariety* (2017): Hecke-translate unlikely intersections in Shimura varieties, with unconditional results for certain curves/Hecke correspondences and conditional general statements.
- Christopher Daw and Martin Orr, *Unlikely intersections with E x CM curves in A_2* (2019): finiteness statements for intersections with special curves parametrizing abelian surfaces isogenous to products with a CM elliptic factor, under stated hypotheses.

These papers identify the correct external mathematical technology, but this submission does not claim their published hypotheses directly settle the present two-dimensional Prym image.  The point is the opposite: the remaining uniform all-degree closure is theorem-class external rather than another finite repository mutation.

```text
EXTERNAL_CLASS=HECKE_ORBIT_UNLIKELY_INTERSECTION_IN_A2
EXTERNAL_RESULT_DIRECTLY_APPLIED=false
NEW_EXTERNAL_THEOREM_OR_APPLICABILITY_PROOF_REQUIRED=true
```

## Handoff

```text
R504_FULL_SPLIT_GENERIC_PRYM_E0_HOM_OVER_K=0
R504_FULL_SPLIT_FIXED_DEGREE_E0_FACTOR_LOCI=PROPER_ALGEBRAIC
R504_FULL_SPLIT_EXCEPTIONAL_UNBOUNDED_ISOGENY_LOCUS=OPEN_EXTERNAL
R504_FULL_SPLIT_PRYM_ROUTE=EXTERNAL_THEOREM_GATE_CANDIDATE
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
DISCOVERY_LEDGER_STATUS=COMPLETE_FOR_THIS_GATE_CLASSIFICATION
