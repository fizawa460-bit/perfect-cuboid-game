# Stage27-20-r303b — split same-target-class collision sources

STATUS=SUBMITTED_PENDING_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_T_PUSHFORWARD_COLLISION
PARENT_ROUTE=Stage27-20-r303a

The frozen T target class consists of at least the ordinary Gaussian modulus d, invertible residue beta mod d, strict angular sector, and endpoint/radial decorations retained by the physical packet map. Equality of target classes is therefore stronger than equality of modulus alone.

For an ordered collision pair (p,p') with pi(p)=pi(p'), expose the conditions in the order

1. d(p)=d(p');
2. beta(p)=beta(p') modulo d;
3. same sector/decorations;
4. both packets survive the same Stage14 physical masks.

This prevents the common illegal simplification in which all packets sharing one small modulus are treated as one fiber.

The collision energy may be bounded by any reconstruction theorem showing that, after fixing one packet and the exact target class, the number of partner packets is B^{rho+o(1)} with rho strictly below the exceptional-class saving exponent eta. A B^{o(1)} partner multiplicity would be ideal and would make every fixed-power exceptional-cardinality saving chargeable.

No such multiplicity bound is asserted yet. The next receiver is therefore:

TPhysicalTargetClassPartnerMultiplicity:
  sup_p #{p': pi(p')=pi(p)} <= B^{rho+o(1)},

combined with a lower bound C0 >= B^{lambda-o(1)} and M of the expected physical scale so that the resulting L2 estimate is expressed relative to M^2/C0 rather than merely M B^rho.

TARGET_CLASS_COLLISION_COMPONENTS_EXPOSED=true
POINTWISE_MODULUS_MULTIPLICITY_NOT_USED_AS_TARGET_FIBER=true
NEXT_DERIVED_ROUTE=27-20-r303c
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
