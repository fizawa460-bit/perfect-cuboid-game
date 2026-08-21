# Stage29-08 — fibration and marginal-family crosswalk

## 1. Stage20 Euler K3 = long-diagonal sign quotient after the 29-07 bridge

The full endpoint coordinates may be written

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

Quotienting by the sign of `d` forgets only the space-root coordinate and leaves the normal Euler-brick model in `P5`:

```text
Kbar_c={e^2+x^2=p^2, e^2+y^2=q^2, x^2+y^2=z^2}.
```

By Stage29-07, the same model is obtained from the Stage28 two-face resolution `Y` by adjoining the third-face root. Its smooth minimal resolution is therefore the Stage20 third-face/Euler K3 `X_face`.

The physical line bundle also matches exactly. On the double cover `pi_face:X_face->Y`,

```text
M_face=pi_face^*(-K_Y),
M_face^2=8,
h0(M_face)=6,
```

and the six physical sections are `[e:x:y:p:q:z]`. Thus `M_face` is the pullback of the `P5` hyperplane class on the Euler K3 normal model.

Proposed strengthened adapter:

```text
R29-K1=DISCHARGED_PENDING_AUDIT
STAGE20_X_FACE_EQUALS_TESTA_STOLL_K_C_AT_NORMAL_FUNCTION_FIELD_AND_MINIMAL_RESOLUTION_LEVEL=true
PHYSICAL_M_FACE_EQUALS_EULER_P5_HYPERPLANE_PULLBACK=true
```

This is an equation-level and resolution-level adapter; it is not inferred merely from the shared modular form `h32`.

## 2. Stage19 space K3 as the complementary coordinate-sign quotient

Similarly, forgetting the third-face root `z` leaves

```text
[e:x:y:p:q:d]
```

with the two automatic faces plus the space equation. This is the Stage19 space-completion double cover of `Y`. Therefore the corresponding coordinate-sign K3 orbit is the `K_b/h16` type.

```text
STAGE19_X_SP_TO_COORDINATE_SIGN_K_B=EXACT_MODEL_ADAPTER_PENDING_AUDIT
```

No equality between arbitrary members of the three-element `K_b` orbit is claimed without the physical face-label choice.

## 3. Published K3 elliptic fibrations

Testa--Stoll's Euler K3 quotient carries 15 elliptic fibrations. With `R29-K1`, they become legitimate Stage20 marginal fibration candidates under the same physical `M_face` polarization.

Still open:

```text
R29-FIB1=FifteenEulerK3FibrationFiberClassesInPhysicalMfacePicardLedger
R29-FIB2=ArithmeticRankSpecializationAndEndpointResidualSpaceSquareLiftPerFibration
```

A fibration on `X_face` is not by itself a perfect-cuboid family: the residual space square condition must still be imposed through the joint V4 cover.

## 4. Peschmann Master-Hit elliptic fibration

The May 2026 Peschmann fibration

```text
H_mn -> E_mn
```

lives on the same Euler-brick marginal because `H_mn` is exactly the Master/third-face square equation at fixed second Euclid pair. It is therefore a concrete elliptic-fibration chart on `X_face`.

Whether it is birationally one of the 15 published Testa--Stoll fibrations, a base change of one, or a different elliptic pencil is not certified here.

```text
R29-PESCH2=OPEN_BOUNDED_EXACT_FIBRATION_CLASS_MATCH
```

## 5. Full endpoint genus-5 fibrations

The full endpoint surface has 28 published genus-5 fibrations with generic canonical degree 8. They are full-surface geometric fibrations, unlike the marginal elliptic fibrations above.

They provide a surface-covering fibration atlas geometrically, but do not give global arithmetic coverage by rational sections/multisections and do not exclude isolated rational points.

```text
FULL_ENDPOINT_28_GENUS5_FIBRATIONS=GEOMETRIC_ATLAS
RATIONAL_SECTION_COVERAGE_PROVED=false
RATIONAL_POINT_EXCLUSION_PROVED=false
```

## 6. Saunderson and StageA2

The audited Saunderson Euler-brick curve is a one-dimensional curve on `X_face` of physical `M_face` degree 6. Its lift to the endpoint is nonsplit and gives the already-audited genus-3 curve of endpoint canonical degree 12. Therefore it is a thin marginal family, not endpoint coverage.

StageA2 closes one specific `-18` family by family-specific elliptic/descent arguments. It remains a method example and a thin-family closure only; its family-specific result is not generalized into endpoint coverage.

```text
SAUNDERSON_GLOBAL_COVERAGE=false
STAGEA2_GLOBAL_COVERAGE=false
FAMILY_CLOSURE_IMPLIES_ENDPOINT_CLOSURE=false
```
