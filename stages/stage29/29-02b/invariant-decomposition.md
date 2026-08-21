# Stage29-02b — eigensheaf/invariant decomposition

```text
ROLE=V4_EIGENSHEAF_INVARIANT_PREFLIGHT
STATUS=AUDIT_REPAIRED
```

The common base `Y=Bl_4(P1xP1)` is the rational degree-4 **weak del Pezzo** surface used by Stage28, with

```text
(-K_Y)^2=4,
q(Y)=p_g(Y)=0,
h^0(-K_Y)=5.
```

Here `-K_Y` is nef and big; the anticanonical model may contract boundary curves of anticanonical degree zero. No ampleness claim is needed below.

Because `Pic(Y)` has no torsion and each marginal branch divisor is linearly equivalent to `-2K_Y`, both quadratic building line bundles are

```text
L_face = L_sp = -K_Y.
```

## 1. Joint V4 cover eigensheaves

For the fiber product of the two independent double covers,

\[
\pi_*\mathcal O_{X_{joint}}
\cong
\mathcal O_Y
\oplus\mathcal O_Y(K_Y)
\oplus\mathcal O_Y(K_Y)
\oplus\mathcal O_Y(2K_Y),
\]

corresponding to the four characters of `V4`.

The canonical preflight gives

\[
K_{X_{joint}}\sim\pi^*(-K_Y).
\]

Projection formula therefore gives

\[
\pi_*K_{X_{joint}}
\cong
\mathcal O_Y(-K_Y)
\oplus\mathcal O_Y
\oplus\mathcal O_Y
\oplus\mathcal O_Y(K_Y).
\]

Since `h^0(-K_Y)=5`, `h^0(O_Y)=1`, and `h^0(K_Y)=0`,

\[
\boxed{p_g(X_{joint})=5+1+1=7}
\]

at the normal-cover level.

For irregularity,

```text
H^1(O_Y)=0,
H^1(K_Y)=0,
H^1(2K_Y)=0.
```

The first two vanish by rationality/Serre duality. By Serre duality, `H^1(2K_Y)` is dual to `H^1(-K_Y)`. The latter vanishes by Kawamata--Viehweg in characteristic zero, because

```text
-K_Y = K_Y + (-2K_Y)
```

and `-2K_Y` is nef and big on this weak del Pezzo surface. Hence

\[
\boxed{q(X_{joint})=0.}
\]

Together with the canonical square preflight,

```text
JOINT_K2=16
JOINT_pg=7
JOINT_q=0
JOINT_chi_O=8
```

and, if the global singularities are rational double points so the resolution is crepant/rational, Noether gives

```text
JOINT_c2=12*8-16=80.
```

The independently known full cuboid surface has exactly `K^2=16`, `p_g=7`, `q=0`. This is a strong consistency check and, together with the dense-open endpoint identification, fixes the birational minimal-model invariant package even though the concrete toric boundary ledger is still pending.

## 2. Cross quotient eigensheaves

The cross double cover has branch class `-4K_Y`, so its building line bundle is

```text
L_cross=-2K_Y.
```

Thus

\[
\pi_{cross*}\mathcal O_{X_{cross}}
\cong
\mathcal O_Y\oplus\mathcal O_Y(2K_Y).
\]

With

\[
K_{X_{cross}}\sim\pi_{cross}^*(-K_Y),
\]

projection formula yields

\[
\pi_{cross*}K_{X_{cross}}
\cong
\mathcal O_Y(-K_Y)\oplus\mathcal O_Y(K_Y).
\]

Therefore on the normal cover

\[
\boxed{p_g(X_{cross})=5},
\qquad
\boxed{q(X_{cross})=0}.
\]

For the **minimal resolution**, retaining the same `p_g,q,K^2` package requires the remaining global singularities to be rational/canonical and the resolution to be crepant. Under that proviso the predicted package is

```text
CROSS_K2=8
CROSS_pg=5
CROSS_q=0
CROSS_chi_O=6
CROSS_c2=64
```

and `X_cross` is a concrete candidate surface of general type rather than merely a character-sum bookkeeping device.

## 3. Interpretation

The quotient diamond has the structural contrast

```text
X_face  : K3, pg=1, q=0, K~0
X_sp    : K3, pg=1, q=0, K~0
X_cross : predicted minimal general-type package, pg=5, q=0, K2=8
X_joint : full-endpoint birational type, pg=7, q=0, K2=16
```

The two extra holomorphic 2-forms beyond the cross quotient are exactly the two marginal nontrivial characters in the `V4` eigenspace decomposition. This creates a natural cohomological bridge to the endpoint L-function lens.

## Firewalls

```text
GLOBAL_SINGULARITY_ENUMERATION_COMPLETE=false
CROSS_MINIMAL_GENERAL_TYPE_AUDITED=false
NOETHER_C2_PROMOTED_WITHOUT_ADE_AUDIT=false
RATIONAL_POINT_COUNT_FROM_INVARIANTS=false
```

The invariant package is a structural receiver and cross-check, not a perfect-cuboid existence/nonexistence theorem.
