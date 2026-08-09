# Rational witness -> kernel packet -> two quadrics

```yaml
ID: TB-DICTIONARY-witness-kernel-two-quadrics
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Rational witness to signed kernel packet and shared two-quadrics
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-4bg/result.md
```

## INPUT

- Primitive oriented Pythagorean first-face base `F=(S,X,H)` with `S^2+X^2=H^2`.
- A bounded-height non-torsion rational witness on

```text
E_F: W^2=Z(Z-S^2)(Z+X^2)
```

written in primitive monic-Weierstrass denominator form.

## OUTPUT

The rational coordinates normalize as

```text
Z=A/D^2
W=Y/D^3
D>0
gcd(A,D)=1.
```

Define

```text
G0=A
G1=A-S^2D^2
G2=A+X^2D^2.
```

Then

```text
Y^2=G0*G1*G2
G0-G1=S^2D^2
G2-G0=X^2D^2
G2-G1=H^2D^2.
```

Write uniquely

```text
Gi=di*ui^2
```

with signed squarefree `di`. Their odd support factors as

```text
d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c

a|rad_odd(S)
b|rad_odd(X)
c|rad_odd(H)
```

where `tau_i in {+1,-1,+2,-2}` and the product condition leaves sixteen abstract sign/2-adic packets.

For a fixed packet `sigma=(tau0,tau1,tau2,a,b,c)`, the same object used by the merged main and s routes is

```text
d0*u0^2-d1*u1^2=S^2D^2
d2*u2^2-d0*u0^2=X^2D^2
```

or equivalently

```text
tau0*a*b*u0^2-tau1*a*c*u1^2=S^2D^2
tau2*b*c*u2^2-tau0*a*b*u0^2=X^2D^2.
```

## VARIABLE DICTIONARY

- `A` = numerator of the rational `Z` coordinate; not the s5 A-column.
- `D` = square-root of the reduced rational `Z` denominator for the chosen witness.
- `Y` = integral numerator of `W=Y/D^3`.
- `G0,G1,G2` = three denominator-cleared cubic factors.
- `d0,d1,d2` = signed squarefree kernels of `G0,G1,G2`.
- `u0,u1,u2` = positive square variables with `Gi=di ui^2`.
- `a,b,c` = positive odd squarefree pair-support divisors on the `S`, `X`, `H` edges respectively.
- `tau0,tau1,tau2` = finite sign/2-adic factors.
- `sigma` = fixed signed kernel packet.

## USED BY

- Stage14-4bg and later main-track post-local witness incidence.
- Stage14-s6-01 and later s-route global-small-point incidence.
- Any toolbox recipe that needs to pass from local support to actual global square variables.

## DO NOT USE FOR

- `D` is the denominator of a selected rational representative. It is not automatically `D_min` and is not automatically the torsion-normalized physical denominator `D_T`.
- `G0,G1,G2` are not the physical gluing scale `G=gcd(S,S2)*d` introduced later in s6-06.
- The fixed-packet two-quadrics equations do not by themselves imply that every algebraic solution reconstructs a physical cuboid candidate.
- A coordinate-density saving on `(u_i,D)` cannot be multiplied into the unweighted packet count without a proved moving-packet/existence transfer.

## PROVENANCE NOTES

- Stage14-s6-01 gives the complete signed edge-packet and five-column refinement.
- Stage14-4bg, PR #344, merge `80e59daf772f39ec6d48435717440e1c120c4e47`, independently freezes the same rational witness equation and two-quadrics on the main route. This is the primary cross-route identification.
