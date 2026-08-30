# Stage33-12 MAIN exact assembly checkpoint

Status: `R3_R4_BRAUER_SHA_BRIDGE_REPAIRED_PENDING_FRESH_SUPER_HOSTILE_R4_4_8_12_OPEN_R5_BLOCKED_4_OF_5`

Stage33-12 remains open. Stage33-13 is not released. PR #1464 is not merge-authorized. No theorem, receiver, endpoint, or Perfect Cuboid existence/nonexistence credit is released.

## Current mathematical audit state

The fresh mathematical super-hostile audit separates the Stage33-05 J2 repair into the following credit layers:

```text
R0 PASS
R1 PASS
R2 PASS
R3 mathematical content PASS
R3 -> R4 Brauer-to-Sha bridge was missing at audit time
R4 attempt4 orientation / phi-cover construction PASS
R4 named-J2-torsor credit was premature before that bridge
R4 exit {4,8,12} OPEN
R5 NOT RUN / BLOCKED BY R4
```

The historical Q-defined `ell_J2` remains revoked: it is zero in the geometric Creutz--Viray quotient. It MUST NOT be regenerated or reused as the corrected nonzero J2 witness.

## Retained R0-R3 chain

R1 confirms the abstract quotient-basis class J2 is nonzero independently of the revoked historical `ell_J2`.

R2 source-locks the corrected geometric full-L pair

```text
J2 = (f2,1),
f2=(t+1+sqrt(2))/(t-1+sqrt(2)),
```

and proves it is nonzero in `Lbar^*/(Kbar^* Lbar^{*2})` using the exact quadratic-extension square test and odd valuations.

R3 applies Creutz--Viray Lemma 4.6 to this corrected pair and obtains the explicit cocycle

```text
xi(rho)=Tr,
Tr=((t^2-1)^2,0),
```

where `rho` flips `sqrt(f2)`. The B+ partition is identified with Tr by an exact function-field square identity, not by branch-orbit labeling.

Certificates:

- `stages/stage33/33-05/j2-corrected-full-l-representative.json`
- `stages/stage33/33-05/j2-corrected-cv-e2-cocycle.json`

## Repaired R3 -> R4 Brauer-to-Sha bridge

The audit correctly identified a missing semantic adapter. A correctly oriented 2-isogeny cover with matching cocycle data is not, by itself, enough to identify the surface Brauer class J2 with that genus-one torsor.

The repair is now materialized in

```text
stages/stage33/33-05/j2-r3-r4-brauer-sha-bridge.json
canonical_sha256 = 4703d20bc8421eb1f46a0e9d5b2c97b76aa228c1dabecd90244a7820f18aceec
```

with deterministic verifier

```text
stages/stage33/33-05/certify_j2_r3_r4_brauer_sha_bridge.py
```

The adapter records the exact chain

```text
corrected (f2,1) represents abstract J2
  -> gamma(f2,1), the Creutz--Viray Brauer/corestriction class
  -> h0(gamma(f2,1)) = d(f2,1)          [Creutz--Viray Proposition 5.1]
  -> d(f2,1) is represented by xi       [Creutz--Viray Lemma 4.6]
  -> xi(rho)=Tr                         [R3 exact computation]
  -> standard Tr-kernel phi-descent for d=f2
  -> corrected attempt4 quartic.
```

Thus the new bridge supplies the missing named-class identity route. However, this promotion is deliberately marked

```text
PROVISIONAL_PENDING_FRESH_SUPER_HOSTILE_AUDIT
```

until the bridge itself is independently re-audited. No primitive NS/T computation is to be charged before that audit gate passes.

The old interfaces are explicitly superseded/resolved by this bridge:

- `stages/stage33/33-12/j2-brauer-to-sha-leray-edge-interface.json`
- `stages/stage33/33-12/j2-twisted-poincare-torsor-target.json`

The old warning remains load-bearing: one rational 2-isogeny squareclass alone is not sufficient. The new identity uses the Creutz--Viray `h0 o gamma = d` compatibility, not the squareclass alone or matching support.

## R4 attempt4 scope

Attempt4 itself is now intentionally scoped only as the correctly oriented phi-cover candidate:

```text
N^2 = f2*U^4
      - 2*(t^2+1)^2*U^2*V^2
      + ((t^4-6*t^2+1)^2/f2)*V^4.
```

Exact binary-quartic invariants prove

```text
Jac(attempt4) = E_Kc.
```

The historical `+a,b/f2` attempt has Jacobian `Eprime_Tr` and remains superseded as named Kc-torsor evidence.

Attempt4 certificate:

`stages/stage33/33-05/j2-r4-2isogeny-orientation-correction.json`

Its standalone firewall is now explicit:

```text
named_J2_torsor_credit_without_brauer_sha_bridge = false.
```

## R4 exit remains open

The fixed marked receiver is still

```text
T(Kc) = diag(4,8).
```

The three index-2 kernels remain exactly distinguishable by minimum norm:

```text
functional [0,1] -> minimum norm 4
functional [1,0] -> minimum norm 8
functional [1,1] -> minimum norm 12
```

But the primitive NS/T discriminant form of the corrected J2 torsor has not yet been computed. Therefore

```text
candidate minimum norms = {4,8,12}
minimum norm selected = false
marked Brauer coordinate selected = false
```

No value among 4, 8, or 12 is currently authoritative.

## Evidence hygiene and firewalls

The stale historical positive J2-descent Actions path is revoked and blocked. Historical attempt1/2 producers are not current semantic evidence. Current controller, repair-state, audit-state, and replay workflow distinguish phi-cover construction from named-J2 promotion.

Current firewalls:

```text
Q_defined_descent_credit_restored = false
named_J2_torsor_authoritative_credit = false
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

## Next exact gate

```text
FRESH_SUPER_HOSTILE_AUDIT_R3_R4_BRAUER_SHA_BRIDGE
```

Only if that audit passes may MAIN proceed to

```text
R4_COMPUTE_PRIMITIVE_NS_DISCRIMINANT_GROUP_AND_QUADRATIC_FORM_OF_X_J2
AND_SELECT_MINIMUM_NORM_4_8_12.
```

R5 remains blocked until the R4 exit is actually established.
