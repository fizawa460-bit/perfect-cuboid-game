# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_EXPLICIT_J2_TORSOR_K3_NEXT_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
beta1=t1/8 -> [1,0]
beta2=t2/16 -> [0,1]
```

The named nonzero J2 class is still one of `[1,0]`, `[0,1]`, `[1,1]`. The certified kernel fingerprints remain

```text
[1,0] -> minimum norm 8
[0,1] -> minimum norm 4
[1,1] -> minimum norm 12
```

The independent J2-side datum is retained:

```text
phi_*(E_J2)=(0,0) in E'[2]
```

## Breadth audit result retained

`EXHAUSTIVE_VIEW_AUDIT + BLIND_REDISCOVERY` selected the kernel-first route: construct the J2-twisted transcendental kernel intrinsically rather than evaluate the named class on unmaterialized abstract `t1,t2` cycles.

Certificate: `j2-marked-brauer-exhaustive-view-audit.json`.

## NEW: explicit elliptic-K3 / torsor-kernel reduction

The Stage33-05 `P1_t` ruling has generic fiber

```text
w^2=t^2*(1-s^2)^2+s^2*(1-t^2)^2.
```

After `y=w/t`, this is

```text
y^2=s^4+A*s^2+1,
A=(t^4-4*t^2+1)/t^2.
```

The square leading coefficient gives the two rational infinity points, hence a section. The standard Jacobian quartic transformation gives, after clearing denominators,

```text
H=t^4-4*t^2+1
q=t^4-6*t^2+1
Y^2 = X*(X^2 - 2*H*X + (t^2-1)^2*q).
```

The identity

```text
A^2-4=((t^2-1)^2*q)/t^4
```

is verified exactly. The Jacobian model has rational 2-torsion `(0,0)`.

For an elliptic K3 with section, the Brauer group is identified with the Tate-Shafarevich torsor group. For the named order-two class `alpha_J2`, let `Y_J2` be its genus-one K3 torsor. The twisted-transcendental formalism gives the target reduction

```text
T(Y_J2) ~= T(Kc,alpha_J2) ~= ker(alpha_J2:T(Kc)->Q/Z).
```

Therefore an explicit construction of `Y_J2` followed by an exact `NS(Y_J2)` / transcendental-lattice computation determines the J2 marked coordinate without first choosing topological representatives of `t1,t2`.

Certificate: `j2-elliptic-torsor-kernel-reduction.json`.
Canonical SHA256: `9e3520da8c6945a4e90f3e6e87711100df666c58a50caf2787a268e0ca9d0bde`.
Verifier: `certify_j2_elliptic_torsor_kernel_reduction.py`.

Current exact boundary:

```text
J2_TORSOR_K3_SEMANTIC_REDUCTION=PASS_NEW_GATE_FROM_STRONGER_VIEW
EXPLICIT_Y_J2_EQUATION_MATERIALIZED=false
Y_J2_PICARD_OR_T_LATTICE_MATERIALIZED=false
CANDIDATES_BEFORE=3
CANDIDATES_AFTER=3
```

This is genuine progress in the missing interface: the problem is no longer an unspecified abstract-cycle marking. It is now the concrete algebraic task of constructing the order-two genus-one torsor `Y_J2` from the already Q-defined Creutz--Viray J2 class and computing its rank-two transcendental lattice (or just its minimum norm).

## Route ledger

```text
TWISTED_TRANSCENDENTAL_KERNEL_RECONSTRUCTION  LIVE / ACTIVE
EXPLICIT_J2_GENUS_ONE_TORSOR_K3               LIVE / NEXT EXACT LEAF
TWISTED_MUKAI_OR_DERIVED_HODGE                UNTESTED FALLBACK
K3_LEVEL_SHIODA_INOSE_CORRESPONDENCE           UNTESTED HIGH-COST FALLBACK
ALGEBRAIC_AZUMAYA_C1_MOD2                      UNTESTED FALLBACK
BRANCH_COHOMOLOGICAL_MAP                       EQUIVALENT / ARCHIVED
GOOD_REDUCTION_ETALE_SPECIALIZATION            EQUIVALENT-BLOCKED
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR            REJECTED_EXACTLY
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION        BLOCKED
```

Next exact leaf:

`CONSTRUCT_THE_EXPLICIT_ORDER_2_GENUS_ONE_TORSOR_Y_J2_FROM_THE_NAMED_CV_J2_CLASS_AND_COMPUTE_ITS_NS_OR_T_MINIMUM_NORM`.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
