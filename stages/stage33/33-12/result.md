# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_LERAY_SHA_2ISOGENY_GATE_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The named J2 coordinate is still one of the three nonzero functionals. The independent J2 datum `phi_*(E_J2)=(0,0) in E'[2]` remains retained.

## Elliptic-K3 kernel route retained

For the `P1_t` ruling:

```text
H=t^4-4*t^2+1
q=t^4-6*t^2+1
D=(t^2-1)^2*q
E: Y^2=X*(X^2-2*H*X+D).
```

The rational point `(0,0)` is 2-torsion. The order-two Tate-Shafarevich torsor `Y_J2` attached to the named Brauer class satisfies

```text
T(Y_J2) ~= ker(alpha_J2:T(Kc)->Q/Z).
```

Therefore the minimum norm of `T(Y_J2)` would select the marked coordinate uniquely.

## Explicit conditional 2-isogeny candidate retained

With

```text
Dplus=t^2-2*t-1
Dminus=t^2+2*t-1
q=Dplus*Dminus
H^2-D=4*t^4,
```

the rational 2-isogeny gives the conditional homogeneous-space candidate

```text
C_Dplus:
N^2 = Dplus*U^4 - 2*H*U^2*V^2
      + (t^2-1)^2*Dminus*V^4.
```

The algebraic identities and the standard homogeneous-space template are certified exactly by `j2-2isogeny-torsor-candidate.json`.

## NEW exact semantic gate

An order-two Sha class is **not automatically** a class in the kernel subgroup selected by one chosen rational 2-isogeny. Therefore the common `Dplus` support does not yet define a legitimate 2-isogeny squareclass for J2.

The correct factorization is now frozen as

```text
alpha_J2 in Br(Kc)[2]
  -> xi_J2 in H^1(Q(t),E)[2]                 (Leray/Ogg-Shafarevich)
  -> prove/reject xi_J2 lies in the relevant 2-isogeny-kernel image
  -> only then assign a descent squareclass d
  -> compare d with Dplus.
```

Exact gate certificate: `j2-2isogeny-cohomological-gate.json`; canonical SHA256 `7373416b8c0aa9ca232ba4c0a7ede76cd8400e9d0a79d84ac60d31d408f05a41`; verifier `certify_j2_2isogeny_cohomological_gate.py`.

```text
BR_2TORSION_IMPLIES_ORDER2_SHA_CLASS=true
ORDER2_SHA_AUTOMATICALLY_HAS_THIS_2ISOGENY_SQUARECLASS=false
DPLUS_SUPPORT_PROVES_ISOGENY_KERNEL_MEMBERSHIP=false
DPLUS_SUPPORT_PROVES_d=DPLUS=false
CANDIDATES_BEFORE=3
CANDIDATES_AFTER=3
```

The next exact leaf is:

`MATERIALIZE_XI_J2_AS_AN_EXPLICIT_GENUS_ONE_TORSOR_OR_CECH_COCYCLE_AND_TEST_THE_2ISOGENY_KERNEL_GATE`.

The Creutz--Viray corestricted quaternion remains the named input; its role is to certify the Brauer class, not by itself to choose the 2-isogeny coordinate.

## CI repair

The deterministic checkpoint failure at head `94a3b313...` was operational, not mathematical: the two new verifiers imported `sympy`, which is absent from the network-free Python job. Both verifiers now use exact dependency-free integer polynomial arithmetic. The new cohomological gate verifier is also wired into the checkpoint replay.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
J2 2-isogeny squareclass selected = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
