# Stage29-08 — audited fibration and marginal-family crosswalk

## 1. Stage20 Euler K3 = long-diagonal sign quotient

The full endpoint coordinates are

```text
[e:x:y:p:q:z:d]
```

with

```text
e^2+x^2=p^2
e^2+y^2=q^2
x^2+y^2=z^2
e^2+x^2+y^2=d^2.
```

Quotienting by the sign of `d` forgets only the space-root coordinate and leaves

```text
Kbar_c={e^2+x^2=p^2, e^2+y^2=q^2, x^2+y^2=z^2} subset P5.
```

This is simultaneously the Testa--Stoll normal Euler-brick K3 quotient and the Stage20 third-face completion of the Stage28 two-face host. Their minimal resolutions agree over `Q`.

On `pi_face:X_face->Y`,

```text
M_face=pi_face^*(-K_Y),
M_face^2=8,
h0(M_face)=6,
```

and the six physical sections `[e:x:y:p:q:z]` are exactly the `P5` hyperplane system.

```text
R29-K1=DISCHARGED
STAGE20_X_FACE_EQUALS_TESTA_STOLL_K_C_AT_NORMAL_AND_MINIMAL_RESOLUTION_LEVEL=true
PHYSICAL_M_FACE_EQUALS_EULER_P5_HYPERPLANE_PULLBACK=true
```

This is equation/resolution/polarization level, not an inference from the shared `h32` newform.

## 2. Stage19 complementary K_b label

Forgetting the third-face root `z` instead leaves the two automatic faces plus the space equation, exactly the Stage19 space-completion double cover of `Y`. With the physical face-label choice this is the coordinate-sign `K_b/h16` type.

```text
STAGE19_X_SP_TO_PHYSICALLY_LABELED_COORDINATE_SIGN_K_B=EXACT_MODEL_ADAPTER
ARBITRARY_K_B_ORBIT_MEMBER_EQUALITY_CLAIM=false
```

## 3. Testa--Stoll K_c elliptic fibrations

The geometric count `3+2*6=15` elliptic fibrations on `K_c` is retained. This count is geometric. Rank-4 quadrics give two rulings only over a splitting field, so Stage29 does not certify all 15 individual fibrations as `Q`-defined without a field ledger.

```text
EULER_K3_ELLIPTIC_FIBRATION_COUNT=15_GEOMETRIC
ALL_15_FIBRATIONS_Q_DEFINED_CERTIFIED=false
R29-FIB1=FifteenEulerK3FibrationPhysicalClassAndFieldOfDefinitionLedger
R29-FIB2=ArithmeticRankSpecializationAndEndpointResidualSpaceSquareLiftPerFibration
```

A marginal elliptic fibration is not by itself a perfect-cuboid family; the residual space condition remains.

## 4. Peschmann Master-Hit elliptic fibration

The May 2026 fibration

```text
H_mn -> E_mn
```

is the same Master/third-face equation at fixed `(m,n)`. By the independently audited global reduction theorem, the **total** `(m,n)` fibration is a globally covering Euler-brick marginal chart after gcd normalization.

The Weierstrass lifting criterion is only for

```text
P in E_mn(Q) \ ({O} union T_tau),
tau(P) in Q_{>0}^square,
```

followed by reduced Euclid positivity/parity/coprimality checks. A bounded Mordell-Weil enumeration remains non-exhaustive.

Whether this fibration is one of the 15 Testa--Stoll pencils, a base change, or another elliptic pencil is still open.

```text
PESCH_TOTAL_FIBRATION_GLOBAL_MARGINAL_COVERAGE=true
BOUNDED_MW_ENUMERATION_GLOBAL_COVERAGE=false
R29-PESCH2=OPEN_BOUNDED_EXACT_FIBRATION_CLASS_AND_POLARIZATION_MATCH
```

## 5. Full endpoint genus-5 fibrations

Testa--Stoll obtain six fibrations from the six rank-3 quadrics and two from each of eleven rank-4 quadrics, for a geometric total `6+2*11=28`. Rank-4 rulings require a splitting field; the first pair is explicitly defined over `Q(i)`.

```text
FULL_ENDPOINT_GENUS5_FIBRATION_COUNT=28_GEOMETRIC
ALL_28_FIBRATIONS_Q_DEFINED_CERTIFIED=false
RATIONAL_SECTION_COVERAGE_PROVED=false
RATIONAL_POINT_EXCLUSION_PROVED=false
```

The 28-fibration statement is a geometric surface atlas, not arithmetic coverage by rational sections or multisections.

## 6. Saunderson and StageA2

The Saunderson Euler-brick curve remains a one-dimensional curve on `X_face` of physical `M_face` degree 6; its endpoint lift is the audited nonsplit genus-3 curve of canonical degree 12. StageA2 remains one specific `-18` family.

```text
SAUNDERSON_GLOBAL_COVERAGE=false
STAGEA2_GLOBAL_COVERAGE=false
FAMILY_CLOSURE_IMPLIES_ENDPOINT_CLOSURE=false
```
