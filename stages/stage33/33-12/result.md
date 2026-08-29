# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_BATCH4_HOSTILE_AUDIT_REVOKED_CLASS2_NO_GO_UPSTREAM_J2_REPRESENTATIVE_REPAIR_REQUIRED_4_OF_5`

Stage33-12 remains open. Stage33-13 is not released. Class-3 promotion is **not** authorized.

## Batch 4 / 4 hostile-audit verdict

The committed four-batch class-2 audit budget is exhausted, but the Batch3 `NO_GO_AFTER_BATCH3` verdict does **not** survive hostile audit. The reason is upstream: the Stage33-05 Q-defined function currently called the named geometric `J2` representative is geometrically trivial in the exact Creutz--Viray function quotient.

The Stage33-05 source is

```text
stages/stage33/33-05/j2_arithmetic_descent.py
blob a63be5592c793c3812da99275478f14dd0d2687b
```

with

```text
F=t^2(1-a^2)^2+a^2(1-t^2)^2,
q=t^4-6t^2+1,
z=(2t^2(1-a^2)-(1-t^2)^2)/(1-t^2),
ell_Q=4(a^2t^2+t^4-4t^2+2)/((t^2-1)(t^2-2t-1)).
```

The new dependency-free exact verifier proves, after clearing denominators,

```text
znum^2-q*zden^2 = 4*t^2*F.
```

Hence the normalization coordinate `z` really is an element of the full branch algebra `Lbar=Qbar(t)[a]/(F)`.

The same verifier then substitutes the retained Hilbert-90 identity

```text
ell_z = f2*g90^2,
f2=(t+1+sqrt(2))/(t-1+sqrt(2)) in Qbar(t)^*,
```

and proves the corresponding cleared identity in `Q(sqrt(2))[t,a]` is a multiple of `F`. Therefore

```text
ell_Q = f2*g^2 in Lbar^*.
```

Creutz--Viray define the relevant geometric function quotient by scalars and squares,

```text
Lbar^*/(Kbar^* Lbar^{*2}),  Kbar=Qbar(t),
```

so the currently promoted representative satisfies

```text
[ell_Q]=0.
```

The surfaces paper explicitly places the finite presentation in the quotient by `K^*L^{*2}` and Corollary 5.4 maps the resulting `L_{c,E}` to `Br X[2]`. The curves paper Lemma 4.6 gives an explicit `E[2]` cocycle `d(ell)`, and Proposition 5.1 identifies this explicit descent map with the Brauer image modulo constants. Thus the generic-fiber explicit-cocycle route is not a missing new theorem.

Certificate: `j2-cv-lclass-zero-regression.json`.
Verifier: `certify_j2_cv_lclass_zero_regression.py`.

## Consequences

The following Batch3 statements are revoked:

```text
CLASS2_GO_NO_GO = NO_GO_AFTER_BATCH3
live_class2_routes_after_audit = 0
class3 escalation from the named-J2 marking gap
```

This does **not** prove that the abstract geometric basis element called `J2` in the Stage33-05 finite F2 presentation is zero. It proves that the specific promoted Q-defined branch-algebra function `ell_Q` cannot represent a nonzero geometric class under the stated CV quotient. The inconsistency must be resolved upstream before any marked coordinate can receive credit.

Possible repair outcomes are deliberately left open:

1. the Hilbert-90 identity was applied to only a normalization component and the branch-algebra dictionary was overstated;
2. `ell_Q` was incorrectly identified with the abstract quotient-basis element `J2`;
3. the Stage33-05 named representative itself must be replaced;
4. another ruling/branch-algebra dictionary was silently substituted.

## Restored executable class-2 route

After a corrected nonzero `ell` is fixed, Creutz--Viray Lemma 4.6 gives an explicit finite route

```text
corrected named ell
  -> d(ell) in H^1(Qbar(t),E[2])
  -> explicit 2-cover / genus-one torsor
  -> compactify and resolve
  -> T(X_J2)
  -> minimum norm 4 / 8 / 12
  -> marked [0,1] / [1,0] / [1,1].
```

No identification of branch orbit `(1,0)` with the marked Brauer coordinate is made.

## Batch-budget interpretation

The four MAIN batches have been used. Batch4 did what it was supposed to do: hostile-audit the class-2 NO-GO. Since that audit found a concrete contradiction and an explicit literature-backed class-2 map, the contractual class-3 escalation condition is **not satisfied**. The correct state is upstream repair, not class-3 promotion.

## Firewalls

```text
class-2 budget used = 4/4
Batch3 class-2 NO-GO = REVOKED_BY_HOSTILE_AUDIT
Stage33-05 named ell geometric nontriviality = REVOKED_PENDING_REPAIR
explicit CV E[2] cocycle route = LIVE_AFTER_REPRESENTATIVE_REPAIR
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
class3 promoted = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```

Next exact leaf:

```text
REPAIR_OR_REPLACE_THE_STAGE33_05_NAMED_J2_CV_REPRESENTATIVE,
THEN COMPUTE_THE_CREUTZ_VIRAY_LEMMA_4_6_E2_COCYCLE.
```
