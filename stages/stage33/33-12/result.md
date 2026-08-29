# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_2ISOGENY_ADAPTER_NEXT_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The named J2 coordinate is still one of the three nonzero functionals. The independent J2 datum `phi_*(E_J2)=(0,0) in E'[2]` remains retained.

## Elliptic-K3 kernel route retained

For the `P1_t` ruling the certified Jacobian is

```text
H=t^4-4*t^2+1
q=t^4-6*t^2+1
D=(t^2-1)^2*q
E: Y^2=X*(X^2-2*H*X+D).
```

The rational point `(0,0)` is 2-torsion. An order-two Tate-Shafarevich torsor `Y_J2` attached to the named Brauer class satisfies the kernel target

```text
T(Y_J2) ~= ker(alpha_J2:T(Kc)->Q/Z).
```

Thus the minimum norm of `T(Y_J2)` would select the marked coordinate uniquely.

## NEW: explicit 2-isogeny homogeneous-space candidate

Factor

```text
Dplus=t^2-2*t-1
Dminus=t^2+2*t-1
q=Dplus*Dminus.
```

The exact identity

```text
H^2-D=4*t^4
```

gives the dual 2-isogenous curve

```text
Ehat: Y^2=X*(X^2+4*H*X+16*t^4).
```

For `E:y^2=x(x^2-2H*x+D)`, the standard 2-isogeny homogeneous-space template is

```text
C_d: N^2=d*U^4-2*H*U^2*V^2+(D/d)*V^4.
```

The two named support points `P_plus,P_minus` of `E_J2` are exactly the ramification points cut out by `Dplus(t)=0`. Therefore the natural J2 candidate squareclass is `d=Dplus`, giving the completely explicit quartic

```text
C_Dplus:
N^2 = Dplus*U^4 - 2*H*U^2*V^2
      + (t^2-1)^2*Dminus*V^4.
```

Its algebraic compatibility with the certified Jacobian/2-isogeny template is checked exactly. Certificate: `j2-2isogeny-torsor-candidate.json`; canonical SHA256 `4a4cf285c3f68f8f3be69a2e24af32f008525d600b88bdf66d7526f90c4f98ea`; verifier `certify_j2_2isogeny_torsor_candidate.py`.

## Exact semantic boundary

This candidate is **not yet promoted to `Y_J2`**. The common support polynomial alone does not prove that the Creutz--Viray Brauer class maps to the 2-isogeny Tate-Shafarevich squareclass `Dplus`.

```text
CANDIDATE_TORSOR_EQUATION_MATERIALIZED=true
NAMED_J2_TORSOR_IDENTIFICATION_CERTIFIED=false
CANDIDATES_BEFORE=3
CANDIDATES_AFTER=3
ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
```

The missing interface is now a single explicit adapter:

`PROVE_CV_J2_CLASS_MAPS_TO_2ISOGENY_DESCENT_SQUARECLASS_DPLUS_UNDER_BR_KC_TO_SHA_OF_THE_P1_T_JACOBIAN_FIBRATION`.

Once that adapter is exact, compute `NS(C_Dplus)` or `T(C_Dplus)` and compare its minimum norm with `4,8,12`.

## Route ledger

```text
CV_J2_TO_2ISOGENY_DPLUS_ADAPTER              LIVE / ACTIVE
EXPLICIT_DPLUS_GENUS_ONE_TORSOR               LIVE / CONDITIONAL ON ADAPTER
KERNEL_LATTICE_FINGERPRINT                    LIVE / COMPARISON
TWISTED_MUKAI_OR_DERIVED_HODGE                UNTESTED FALLBACK
K3_LEVEL_SHIODA_INOSE_CORRESPONDENCE           UNTESTED HIGH-COST FALLBACK
ALGEBRAIC_AZUMAYA_C1_MOD2                      UNTESTED FALLBACK
BRANCH_COHOMOLOGICAL_MAP                       EQUIVALENT / ARCHIVED
GOOD_REDUCTION_ETALE_SPECIALIZATION            EQUIVALENT-BLOCKED
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR            REJECTED_EXACTLY
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION        BLOCKED
```

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
