# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_BRAUER_TO_SHA_LERAY_EDGE_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked Brauer functional is still one of the three nonzero functionals.

## Retained exact rejections

The scalar projections are not the named geometric J2 torsor:

```text
constant d=2 -> geometrically trivial after Qbar base change
q=t^4-6*t^2+1 -> single-isogeny homogeneous space has an explicit Q(t)-point
Dplus=t^2-2*t-1 -> half-divisor pushforward/support datum only
```

The Stage33-05 Hilbert-90 identity

```text
ell_z=f2*g90^2,
f2=(t+1+sqrt(2))/(t-1+sqrt(2))
```

is retained as geometric branch data, not as a generic-fiber Sha coordinate.

## NEW exact rejection: naive CV branch algebra -> split E[2] Kummer

For the even quartic branch algebra

```text
s^4+A*s^2+1,
A=(t^4-4*t^2+1)/t^2,
ell=4*(t^2*s^2+t^4-4*t^2+2)/((t^2-1)*(t^2-2*t-1)),
```

the root pattern is `{r,-r,1/r,-1/r}` and `ell` is even in `s`.

If one naively converts the CV representative to the three split-2-torsion partition characters by pair products, then:

```text
{r,-r}|{1/r,-1/r}: square -> class 1
{r,1/r}|{-r,-1/r}: 32/(t^2-2*t-1)^2 -> class 2
third partition: class 2
```

The key exact identity is

```text
(t^2*beta+c)*(t^2/beta+c)=2*(t^2-1)^2,
c=t^4-4*t^2+2,
beta+beta^-1=-(t^4-4*t^2+1)/t^2.
```

So the naive split-E[2] character triple is

```text
(1,2,2).
```

After base change to `Qbar(t)`, constant `2` is a square, hence this naive class becomes `(1,1,1)` and is geometrically trivial. That cannot equal the named J2 class, which is already certified geometrically nontrivial.

Therefore the CV branch-algebra class must **not** be identified directly with generic-fiber `H^1(Q(t),E[2])` Kummer coordinates. The missing semantic map is the actual Brauer-to-Sha Leray/Ogg-Shafarevich edge for the elliptic K3 fibration.

Certificate: `j2-naive-cv-branch-to-e2-kummer-rejection.json`; verifier: `certify_j2_naive_cv_branch_to_e2_kummer_rejection.py`.

## Next exact leaf

```text
MATERIALIZE_THE_BRAUER_TO_SHA_LERAY_EDGE_FOR_THE_NAMED_CV_AZUMAYA_CLASS
AS_A_CECH_OR_DIVISOR_COCYCLE_ON_THE_ELLIPTIC_K3_FIBRATION
```

Only after that edge is explicit should any `H^1(Q(t),E[2])` or Weil-Chatelet coordinate be assigned.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
J2 full E[2] Kummer coordinates materialized = false
J2 torsor equation materialized = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
