# Stage30-06 — source lock for V4 sign-deck lift and Q(i)/Q cocycle

```text
ROLE=V4_SIGN_DECK_AND_GALOIS_COCYCLE_SOURCE_LOCK
STATUS=SUBMITTED_PENDING_STAGE30_AUDIT
FIELD=Q(i)
GALOIS_GENERATOR=sigma
```

## 1. Primary common-model source

Damiano Testa and Michael Stoll, *The surface parametrizing cuboids*, current arXiv v2 / published-version manuscript, Section 4, “The cuboid surface as a modular surface”.

Load-bearing statements used here:

```text
X: u^2=2xy, v^2=x^2-y^2, w^2=x^2+y^2 is X(8),
Aut_geom(X)=PSL2(Z/8),
G0=ker(PSL2(Z/8)->PSL2(Z/4)) ~= (Z/2)^3,
G0 acts on X by sign changes of u,v,w,
Sbar_Q(i) ~= (X x X)/Delta G0.
```

For the diagonal quotient the exact invariant coordinates are

```text
U=u1*u2, V=v1*v2, W=w1*w2,
X=x1*x2, Y=y1*y2, T=x1*y2, Z=x2*y1,
XY=TZ,
U=2*b1, V=2*b2, W=2*b3,
X=a1+c, Y=-a1+c,
T=a2+i*a3, Z=a2-i*a3.
```

The same section states that factor exchange on `X x X` descends to the sign change

```text
a3 -> -a3
```

on the cuboid surface and uses this to describe the Q-form via Weil restriction.

Stable source locator: arXiv:1009.0388v2, Section 4; current HTML lines corresponding to the modular-surface discussion, especially the quotient coordinates and Q-form paragraph.

## 2. Audited repository inputs

### Seven-line/sign cover

`stages/stage29/29-02ha/exact-sign-cover-model.md`

```text
G_sign ~= (Z/2)^7/<common sign> ~= (Z/2)^6
```

acts by independent signs on

```text
a1,a2,a3,b1,b2,b3,c
```

modulo simultaneous projective sign.

### Exact level-4 modular Q-datum

`stages/stage29/29-02g/exact-q-moduli-adapter.md`

For a rational endpoint point on the physical noncuspidal locus:

```text
E/Q(i),
(P1,P2) basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

The retained level-4 semilinear sign matrix is

```text
D4=diag(1,-1) mod 4.
```

### Bounded sigma action on K8

`stages/stage29/29-15/bounded-execution.md`

```text
K8=ker(SL2(Z/8)->SL2(Z/4)) ~= (Z/2)^3,
SIGMA_ACTION_ON_K8=TRIVIAL,
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8.
```

This is retained as a downstream arithmetic-defect input. It is not the same object as the Stage30 common-model descent cocycle.

### Stage30 common action projection

`stages/stage30/30-05/*` audited in PR #1331:

```text
H=PSL2(Z/4) ~= S4,
rho:H -> S3_branch,
ker(rho)=V_mod={g04,g06,g12,g14} ~= V4,
|im(rho)|=6.
```

The exact displayed `S,T` gauge is noncanonical up to conjugacy, but `ker(rho)=V_mod` and image order 6 are audited gauge-invariant statements.

## 3. Scope firewalls

The following objects must not be conflated:

```text
c_sigma in G_sign
  = cocycle of the Q(i) common-model coordinate isomorphism;

V_mod in PSL2(Z/4)
  = kernel of the residual modular action on seven branch squareclasses;

K8 in SL2(Z/8)
  = eight possible marked arithmetic defects kappa=psi^sigma psi.
```

Stage30-06 may determine `c_sigma`, the exact lift `V_mod -> G_sign`, and the semilinear action on residual `S4`. It may not eliminate any `K8` state.

```text
DEFECT_ELIMINATION_COUNT=0
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
