# Stage14-toolbox-ap — theorem-compatibility matrix and import-rejection audit

Stage14-toolbox-ap audits the live main/s/t/tH results against the typed collision/dispersion interface frozen in toolbox-ao. It separates exact reusable reductions from adapters, conditional estimates and prohibited promotions.

## Result

- 4cd four-root endpoint localization is directly importable as support geometry, but supplies no centered cancellation;
- s7-17 projective slope reduction is an admissible adapter, but `PrimePairProjectiveSlopeDispersion` remains unproved;
- t51/tH14 residue cleanup is directly importable only for the residue diagonal;
- t53's `6+1+5` partition and t54's fixed-U divisor fan are exact imports;
- t54 does not reduce the shared-U family to one dimension: `SharedUBipartiteSquareclassEnergy` remains a genuine two-coordinate receiver;
- fixed-row t36 and fixed-column t38 estimates cannot be globalized by formal Cauchy;
- complete-family traces cannot replace sparse physical selectors;
- absolute completion, U/V tensorization, blockwise absolute recombination, and precompletion cross-kernel collapse are rejected;
- no equivalence between the s projective receiver and the t principal receiver is currently proved.

## Toolbox-H decision

toolbox-H0 remains optional and parallel-safe. ap has now encoded the import rejection rules mechanically, so H0 is useful only as an independent adversarial check of connection hypotheses and counterexamples. It is not required for `ap -> aq`, does not replace tH15, and toolbox main must not wait for it.

~~~text
STAGE14_TOOLBOX_AP=COMPLETE_THEOREM_COMPATIBILITY_MATRIX_AND_IMPORT_REJECTION_AUDIT
MERGED_TOOLBOX_AO_IMPORTED=true
MERGED_4CD_IMPORTED_AS_SUPPORT_GEOMETRY=true
MERGED_S7_17_IMPORTED_AS_ADAPTER_ONLY=true
MERGED_T53_IMPORTED_AS_EXACT_STRATIFICATION=true
MERGED_T54_IMPORTED_AS_DIVISOR_FAN_ONLY=true
FOUR_ROOT_LATTICE_IMPLIES_CENTERED_DISPERSION=false
PROJECTIVE_REDUCTION_IMPLIES_PRIME_PAIR_DISPERSION=false
FIXED_U_DIVISOR_FAN_IMPLIES_BIPARTITE_ENERGY=false
ROW_COLUMN_ENERGY_GLOBALIZATION_ALLOWED=false
RESIDUE_DIAGONAL_DISTINCT_FROM_PRINCIPAL_COHERENCE=true
SPARSE_SELECTOR_REPLACEABLE_BY_COMPLETE_FAMILY=false
PER_MODULUS_ABSOLUTE_COMPLETION_IMPORT_ALLOWED=false
UV_TENSORIZATION_IMPORT_ALLOWED=false
PRECOMPLETION_CROSS_KERNEL_COLLAPSE_ALLOWED=false
PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_PROVED=false
DUAL_SPLIT_K_CENTERED_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_KUMMER_INCIDENCE_PROVED=false
NONPRINCIPAL_SELECTOR_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AP=false
TOOLBOX_H_REQUIRED_FOR_TOOLBOX_MAIN=false
TOOLBOX_H0_STATUS=OPTIONAL_PARALLEL_SAFE_ADVERSARIAL_AUDIT
TOOLBOX_MAIN_BLOCKED_BY_H=false
TH15_REPLACED_BY_TOOLBOX_H=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-aq minimal common theorem envelope and receiver separation
~~~
