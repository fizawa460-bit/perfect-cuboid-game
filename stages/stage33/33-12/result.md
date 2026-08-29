# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_d2_TORSOR_DISCRIMINANT_GROUP_4_OF_5`

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

## Named J2 torsor already fixed

The exact CV/Leray adapter gives squareclass `d=2`, hence

```text
Y_J2/K:
N^2 = 2*U^4 - 2*H*U^2*V^2 + (D/2)*V^4,
H=t^4-4*t^2+1,
D=(t^2-1)^2*(t^4-6*t^2+1).
```

The earlier `d=Dplus` candidate is rejected as the named J2 coordinate.

## NEW exact fiber/lattice gate

The Jacobian factors as

```text
E: Y^2=X*(X-r1)*(X-r2),
r1=(t^2-1)^2,
r2=q=t^4-6*t^2+1,
r1-r2=4*t^2.
```

Therefore, up to a nonzero constant,

```text
Delta = t^4*(t^2-1)^4*q^2.
```

The elliptic K3 fiber configuration is

```text
I4 at t=0,+1,-1,infinity,
I2 at the four simple roots of q,
Euler sum = 4*4 + 4*2 = 24,
root lattice = A3^4 + A1^4,
root rank = 16,
root discriminant = 4^4*2^4 = 4096.
```

The order-2 J2 torsor has the same Jacobian fiber types and a degree-2 multisection. This turns the remaining problem into an explicit component/bisection glue computation in `NS(Y_J2)`.

There is also a useful shortcut. The three possible transcendental kernels have Smith groups

```text
[0,1]: Gram diag(4,32)      -> Z/4 + Z/32, min 4
[1,0]: Gram diag(8,16)      -> Z/8 + Z/16, min 8
[1,1]: Gram [[12,-4],[-4,12]] -> Z/4 + Z/32, min 12.
```

Hence a full minimum-norm computation is not always necessary: if the discriminant group of `NS(Y_J2)` is `Z/8 + Z/16`, J2 is immediately `[1,0]`. If it is `Z/4 + Z/32`, only the residual quadratic form is needed to distinguish `[0,1]` from `[1,1]`.

Exact certificate: `j2-d2-torsor-fiber-lattice-gate.json`; verifier: `certify_j2_d2_torsor_fiber_lattice_gate.py`.

Next exact leaf:

`COMPUTE_NS_DISCRIMINANT_GROUP_FROM_I4^4_I2^4_FIBER_COMPONENTS_AND_DEGREE2_MULTISECTION_GLUE`.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
