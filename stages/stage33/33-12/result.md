# Stage33-12 MAIN exact assembly checkpoint

Status: `R3_R4_BRAUER_SHA_BRIDGE_FRESH_SUPER_HOSTILE_PASS_NAMED_X_J2_AUTHORITATIVE_R4_4_8_12_OPEN_R5_BLOCKED_4_OF_5`

Stage33-12 remains open. Stage33-13 is not released. PR #1464 is not merge-authorized. No theorem, receiver, endpoint, or Perfect Cuboid existence/nonexistence credit is released.

## Current mathematical state

```text
R0 PASS
R1 PASS
R2 PASS
R3 PASS
R3 -> R4 Brauer-to-Sha bridge PASS_FRESH_SUPER_HOSTILE_MATHEMATICALLY
R4 attempt4 phi-cover orientation PASS
R4 named J2 torsor identity AUTHORITATIVE over Kgeom=Qbar(t)
R4 exit {4,8,12} OPEN
R5 NOT RUN / BLOCKED BY R4
```

The historical Q-defined `ell_J2` remains revoked: it is geometrically zero in the Creutz--Viray quotient and MUST NOT be reused as the corrected J2 witness. `Q_defined_descent_credit_restored=false` remains load-bearing.

## R0--R3 retained chain

R1 proves the abstract quotient-basis element `J2` is outside `im(x-alpha)` for all four unresolved `(b,d)` presentation normal forms, without using the revoked historical `ell_J2`.

R2 source-locks the corrected geometric full-L pair

```text
J2=(f2,1),
f2=(t+1+sqrt(2))/(t-1+sqrt(2)),
```

and proves it is nonzero in `Lbar^*/(Kbar^* Lbar^{*2})` by the exact quadratic-extension square test and odd valuations.

R3 applies Creutz--Viray Lemma 4.6 and obtains

```text
xi(rho)=Tr,
Tr=((t^2-1)^2,0),
```

with the B+ partition identified with `Tr` by an exact function-field square identity.

## Fresh-super-hostile-passed R3 -> R4 bridge

The earlier semantic gap was that a correctly oriented 2-isogeny cover with matching support/squareclass is not by itself enough to identify the surface Brauer class `J2` with that torsor. The repaired bridge is:

```text
stages/stage33/33-05/j2-r3-r4-brauer-sha-bridge.json
canonical_sha256 = 4289ef568ce4c793c1ecc91fd55dac9e74f5ecd01e5aad99c5b98917e1df2a66
```

with verifier:

```text
stages/stage33/33-05/certify_j2_r3_r4_brauer_sha_bridge.py
```

The exact named-class chain is now source-locked as

```text
abstract J2 = corrected (f2,1)
  -> gamma(f2,1), the CV Brauer/corestriction class
  -> h0(gamma(f2,1)) = d(f2,1)          [CV Proposition 5.1]
  -> d(f2,1) is represented by xi       [CV Lemma 4.6]
  -> xi(rho)=Tr                         [R3 exact computation]
  -> standard <Tr> phi-descent with d=f2
  -> attempt4 quartic.
```

The fresh super-hostile audit additionally checked the possible Kummer-kernel failure. It is excluded because R1+R2 make `gamma(f2,1)` nonzero modulo constants and the Hochschild--Serre edge `h0` used in CV Proposition 5.1 is injective. Therefore

```text
[xi] != 0 in H^1(Kgeom,E_Kc).
```

The bridge certificate now explicitly records `generic_weil_chatelet_class_nonzero=true`.

The two load-bearing source locks requested by the audit are also materialized:

1. Creutz--Viray, *On Brauer groups of double covers of ruled surfaces*, DOI `10.1007/s00208-014-1153-0`: §1.2 gives the purity filtration `Br X subset Br C`; §2.3 Theorem 2.5 gives the generic-fiber `gamma`; Corollary 5.4 gives the surface presentation `Pic C/2 -> Lc,E -> Br X[2] -> 0`.
2. *Derived Equivalence for Elliptic K3 Surfaces and Jacobians*, DOI `10.1093/imrn/rnae061`, §4.1 equation (4.1): for an elliptic K3 surface with section, `Br(S) ~= Sha(S)` and the corresponding elements parametrize `S`-torsors.

The standard 2-isogeny homogeneous-space formula is also source-locked in the bridge certificate.

Fresh audit verdict:

```text
PASS_FRESH_SUPER_HOSTILE_MATHEMATICALLY
```

Hence `named_J2_torsor_authoritative_credit=true` is now allowed at the geometric `Kgeom=Qbar(t)` layer.

## Authoritative named J2 torsor

Attempt4 by itself remains only an orientation/phi-cover certificate. Together with the audited bridge, its quartic is now authoritatively identified as the named geometric torsor `X_J2`:

```text
X_J2:
N^2 = f2*U^4
      - 2*(t^2+1)^2*U^2*V^2
      + ((t^4-6*t^2+1)^2/f2)*V^4,
Jac(X_J2)=E_Kc.
```

The historical `+a,b/f2` quartic has Jacobian `Eprime_Tr` and remains superseded as named-Kc-torsor evidence.

## R4 exit remains open

The fixed marked receiver is

```text
T(Kc)=diag(4,8).
```

The three possible nonzero order-2 functionals have distinct index-2 kernel minima:

```text
[0,1] -> minimum norm 4
[1,0] -> minimum norm 8
[1,1] -> minimum norm 12
```

But the primitive `NS/T` discriminant form of `X_J2` has not yet been computed. Therefore:

```text
candidate minimum norms = {4,8,12}
minimum norm selected = false
marked Brauer coordinate selected = false
R4 exit = OPEN
R5 = NOT RUN / BLOCKED BY R4
```

## Firewalls

```text
Q_defined_descent_credit_restored = false
named_J2_torsor_authoritative_credit = true   # geometric Kgeom layer only
minimum norm selected = false
marked Brauer coordinate selected = false
Stage33-05 reclosed = false
Stage33-12 exact closure = false
Stage33-13 released = false
R5 run = false
class3 promoted = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence claim = false
perfect cuboid nonexistence claim = false
merge allowed = false
Stage33 progress = 5/11
```

## Next exact leaf

```text
R4_COMPUTE_PRIMITIVE_NS_DISCRIMINANT_GROUP_AND_QUADRATIC_FORM_OF_X_J2
AND_SELECT_MINIMUM_NORM_4_8_12.
```

Only after that exact R4 exit may R5 run.
