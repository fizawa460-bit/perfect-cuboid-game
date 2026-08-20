# Stage27-19-r10b — Master-Hit tau-square moving section/multisection gate

```text
TASK_ID=Stage27-19-r10b
PARENT_ROUTE=Stage27-19-r10a
ROUTE_KIND=TARGETED_EXTERNAL_LOWER_ADAPTER_TEST
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
```

The Peschmann May-2026 Master-Hit construction fixes a primitive Euclid pair `(m,n)`, converts the resulting genus-one quartic to an elliptic curve `E_{m,n}`, and uses a rational function `tau` whose square values recover admissible second Euclid pairs. The published construction enumerates Mordell-Weil combinations and retains only points with

\[
\tau(P)\in \mathbb Q_{>0}^{\square}.
\]

This is a pointwise square-lift filter. It is not, as currently stated, a theorem that a nonconstant algebraic section of the elliptic fibration has `tau` identically square in the function field of the base.

For the Stage27 thick-family lower receiver, the required stronger object is one of:

1. a rational section `P(b)` of the moving elliptic surface such that `tau(P(b))=q(b)^2` in the base function field;
2. a finite-degree rational multisection on which the pullback of `tau` is a square;
3. a positive-dimensional rational subvariety of the total Master-Hit space on which the square-lift is automatic and whose height/source-count ledger satisfies `rho/h>1/4`.

The cited April genus-3 reduction instead treats the square condition as a genuine hyperelliptic covering obstruction. This is evidence against automatically-square generic sections, but it is not an impossibility theorem for all special sections or multisections.

No published statement located in the targeted Peschmann sequence supplies any of the three stronger objects above. The May paper's large computational generation count therefore cannot be promoted to a Stage19 polynomial lower bound with integral space diagonal.

Accordingly the current status is:

```text
TAU_SQUARE_IS_POINTWISE_FILTER_IN_PUBLISHED_CONSTRUCTION=true
GENERIC_MOVING_TAU_SQUARE_SECTION_PROVED=false
GENERIC_MOVING_TAU_SQUARE_MULTISECTION_PROVED=false
POSITIVE_DIMENSIONAL_PERFECT_SUBFAMILY_PROVED=false
R10_STATUS=AMBER_EXTERNAL_CONSTRUCTION_GATE
PRIMARY_GATE=MovingMasterHitSquareLiftSectionOrMultisection
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r10c
```
