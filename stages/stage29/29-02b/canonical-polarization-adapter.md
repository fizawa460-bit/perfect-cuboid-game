# Stage29-02b — endpoint canonical / marginal physical polarization adapter

```text
ROLE=CANONICAL_TO_PHYSICAL_POLARIZATION_ADAPTER
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

This is the main geometric adapter produced by 29-02b.

## 1. Common base line bundle

Stage28 certifies

```text
L=-K_Y,
M_face=pi_face^*L,
M_sp=pi_sp^*L,
```

where `M_face` and `M_sp` are the audited physical quasi-polarizations on the two marginal K3 covers.

For the joint cover

```text
pi_joint:X_joint -> Y,
```

29-02b gives

\[
K_{X_{joint}}\sim\pi_{joint}^*L.
\]

Let

```text
q_sp   : X_joint -> X_face
q_face : X_joint -> X_sp
```

be the two quotient maps.  Since

```text
pi_joint = pi_face o q_sp = pi_sp o q_face,
```

one obtains the exact line-bundle identities

\[
\boxed{K_{X_{joint}}=q_{sp}^*M_{face}}
\]

and

\[
\boxed{K_{X_{joint}}=q_{face}^*M_{sp}}
\]

on the normal/canonical cover model (and on a crepant resolution after the ADE audit).

Thus the Stage28 physical polarization is not merely analogous to the full-endpoint canonical polarization: it is its quotient pullback.

## 2. Exact curve-degree adapter

Let `C` be an integral curve on the joint/full endpoint model not contracted by `q_sp`, and let `C_face=q_sp(C)`.  If the generic degree of `C->C_face` is `delta`, projection formula gives

\[
\boxed{K_{X_{joint}}\cdot C
=\delta\, M_{face}\cdot C_{face}.}
\]

Similarly, for `C_sp=q_face(C)`,

\[
\boxed{K_{X_{joint}}\cdot C
=\delta'\, M_{sp}\cdot C_{sp}.}
\]

This is the exact missing degree adapter between Stage28 fixed-curve spectra and the full endpoint canonical degree.

```text
ENDPOINT_CANONICAL_DEGREE_ADAPTER=ZERO_LOSS
STAGE28_M_DEGREE_TO_ENDPOINT_DEGREE=GENERIC_LIFT_DEGREE_MULTIPLIER
CROSS_SURFACE_DEGREE_IDENTIFICATION_FIREWALL_REPAIRED=true
```

## 3. Saunderson consequence and prior-work rematch

Stage28 certifies an integral rational Saunderson curve `C_S` on `X_face` with

```text
M_face.C_S=6.
```

The endpoint preimage under `q_sp` is the space-diagonal square lift of this Euler-brick family.

If that quadratic lift split generically into degree-one components, each component `C` would satisfy

```text
K_endpoint.C = 1*6 = 6.
```

But Testa--Stoll Theorem 17 proves that the full cuboid endpoint surface has no integral projective/canonical degree-six curve.  Therefore the space-completion cover cannot split generically over the Saunderson curve.  Since `C_S` is not contained in the space branch divisor, its endpoint pullback is a genuine connected degree-two curve cover and has canonical degree

\[
\boxed{12}.
\]

Equivalently the restricted space radicand is not a square in the Saunderson function field.

This **nonsquare / non-split conclusion is not new to the repo**.  Audited Stage27-19-r9a/r9c already computes the exact restricted equation

\[
y^2=t^8+68t^6-122t^4+68t^2+1,
\]

proves the degree-eight polynomial squarefree, and identifies the endpoint lift as a smooth genus-3 hyperelliptic curve.  Faltings then proves only finitely many rational points on that fixed curve.  Stage29-02b supplies a new global-geometric explanation and degree adapter for the already-audited nonsplitting.

```text
SAUNDERSON_SPACE_LIFT_GENERIC_SPLIT=false
SAUNDERSON_SPACE_RADICAND_SQUARE_IN_Q(C_S)=false
SAUNDERSON_ENDPOINT_LIFT_DEGREE=2
SAUNDERSON_ENDPOINT_CANONICAL_DEGREE=12
SAUNDERSON_ENDPOINT_GENUS=3_AUDITED_STAGE27_R9
SAUNDERSON_NONSPLIT_NEW_TO_REPO=false
NEW_CONTENT=GLOBAL_CANONICAL_DEGREE_EXPLANATION_AND_GENERAL_ADAPTER
```

Thus Stage29 does not reopen or duplicate the frozen Stage27 Saunderson route.

## 4. Stage19-side consequence

The same degree argument applies to a fixed integral curve on the Stage19 space K3.  If a source curve has physical `M_sp` degree at most `6`, a degree-one third-face lift would create a full-endpoint curve of the same canonical degree.

The full endpoint low-degree classification therefore forbids any nondegenerate split lift through degree six.  In particular, even if the still-open Stage19 physical `M=6` spectrum contains a curve, that curve cannot by itself produce a trivial degree-one perfect-cuboid family after imposing the third face.

```text
STAGE19_M6_PRESENCE_WOULD_NOT_IMPLY_SPLIT_ENDPOINT_FAMILY=true
ENDPOINT_SPLIT_LIFT_THROUGH_M6=FORBIDDEN_BY_FULL_SURFACE_GEOMETRY
```

This changes the interpretation of the old Stage28 optional `PhysicalLowDegreeRootSpectrumM6` receiver for endpoint work: it can still matter for marginal geometry, but it is no longer a direct low-degree route to a perfect-cuboid family.

## 5. Remaining firewalls

- Degree multiplication does not count rational points.
- A connected quadratic lift may have genus 0, 1, or higher depending on branch data; genus must be computed separately unless already audited.
- The Saunderson restricted cover can still have isolated rational points; Stage27-r9 explicitly preserves this possibility.
- The Testa--Stoll low-degree theorem is external input pending fresh Stage29 audit.
- Boundary curves contracted by the quotient/polarization require separate treatment.

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
COUNTING_EXPONENT_FROM_DEGREE=false
OLD_SAUNDERSON_GATE_REPLAY=false
```
