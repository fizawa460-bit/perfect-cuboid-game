# Stage27-20-r306b — low-core branch becomes a support-count receiver

STATUS=SUBMITTED_PENDING_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_LOW_CORE_SUPPORT
PARENT_ROUTE=Stage27-20-r306a

Inside P_lo(kappa), all already-charged common/root-line moduli are <B^kappa. Reusing their congruence spacing cannot create a fixed B-power once kappa is chosen arbitrarily small. The only legal next step is therefore to count the low-core wall support itself.

Let S_lo(kappa;B) be the set of occupied reduced wall labels after fixing the canonical packet decorations and quotienting the known B^o(1) reconstruction fibers. Since reconstruction multiplicity is exponent-neutral, it suffices to prove

  |S_lo(kappa;B)| <= B^(1/2-delta+o(1))

for some fixed kappa,delta>0.

Equivalently, one may prove a low-core exceptional-set statement showing that the set of physical wall packets whose every available core modulus is <B^kappa has fixed-power density deficit on the exact Stage27 packet measure.

This receiver is distinct from r302: no Fourier operator norm, arbitrary coefficient vector, or same-H_phys quadratic-form theorem is requested. The target is direct support sparsity after a core cutoff.

The next task is to search the existing Stage14/15/StructureRadar arsenal for a theorem that becomes legal precisely because the low-core cutoff restricts the remaining variables: divisor-in-short-interval geometry, determinant/lattice bounds after eliminating the small core, or a separated character sum if coefficient separation appears only on this low-core slice.

LOW_CORE_SUPPORT_RECEIVER_MATERIALIZED=true
RECONSTRUCTION_FIBERS_CHARGED_ONCE=true
FOURIER_OPERATOR_GATE_REQUIRED=false
NEXT_DERIVED_ROUTE=27-20-r306c
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
