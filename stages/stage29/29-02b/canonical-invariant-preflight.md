# Stage29-02b — canonical-invariant preflight

```text
ROLE=BIDOUBLE_COVER_CANONICAL_CLASS_PREFLIGHT
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

## Certified base/branch classes

Stage28 gives

```text
Y=Bl_4(P1xP1),
L=-K_Y,
L^2=(-K_Y)^2=4,
D_face ~ -2K_Y,
D_sp   ~ -2K_Y.
```

The two reduced branch divisors have no common irreducible component.

## Joint degree-four cover

On the normal bidouble-cover model with independent square roots of the two branch functions, ramification gives

\[
K_{X_{joint}}
=\pi^*K_Y+R_{face}+R_{sp}
=\pi^*\left(K_Y+\tfrac12D_{face}+\tfrac12D_{sp}\right).
\]

Substituting the Stage28 branch classes,

\[
\boxed{K_{X_{joint}}\sim\pi^*(-K_Y).}
\]

At the intersection-theory level before any non-crepant resolution correction,

\[
\boxed{K_{X_{joint}}^2=4(-K_Y)^2=16.}
\]

This is a strong internal cross-check: the independently known full cuboid surface has canonical minimal-model invariant `K^2=16`.  Since `function-field-adapter.md` identifies the endpoint and joint cover birationally on dense opens, the agreement is expected rather than a new numerical coincidence.

```text
JOINT_CANONICAL_CLASS_SIGNAL=pi^*(-K_Y)
JOINT_FORMAL_K2=16
FULL_ENDPOINT_K2_FROM_EXISTING_GEOMETRY=16
K2_CROSSCHECK=PASS_CANDIDATE
```

Firewall: the formula is first written on the normal finite-cover model.  The exact boundary/singularity analysis still has to verify that only canonical/crepant corrections occur before this is promoted as a standalone derivation of the minimal-model invariant.  The external full-surface theorem is an independent confirmation, not permission to skip this local audit.

## Cross quadratic quotient

The cross branch divisor is the mod-2 union

```text
D_cross=D_face+D_sp ~ -4K_Y.
```

For the corresponding normal double cover, `2L_cross~D_cross`, so `L_cross~-2K_Y` and

\[
K_{X_{cross}}
\sim\pi_{cross}^*(K_Y+L_{cross})
=\pi_{cross}^*(-K_Y).
\]

Thus the pre-resolution square is

\[
\boxed{K_{X_{cross}}^2=2(-K_Y)^2=8.}
\]

```text
CROSS_CANONICAL_CLASS_SIGNAL=pi_cross^*(-K_Y)
CROSS_FORMAL_K2=8
CROSS_GENERAL_TYPE_MINIMAL_MODEL_PROVED=false
```

The cross quotient is therefore canonically much closer to the full general-type endpoint than either marginal K3 quotient, whose canonical class is trivial.  This gives a precise geometric reason why the cross character can contain joint information invisible in the two marginal K3s.

## Marginal comparison

```text
X_face  : K3, K~0
X_sp    : K3, K~0
X_cross : canonical signal pullback(-K_Y), formal K2=8
X_joint : canonical signal pullback(-K_Y), formal K2=16
```

This quotient-type asymmetry is structural only.  It is not a counting theorem and does not imply a rational-point ordering.
