# StageA1 A1-8 — targeted global quotient/Jacobian descent

## Scope

A1-6 closed the elementary local/congruence route but left the A1-5 global receiver unresolved. This task therefore attacks the exact first-two-cover curve globally rather than increasing search bounds or repeating local sieves.

For a rational first-two-cover survivor write

```text
C: y^2 = F(x),
F(x)=x^16-16x^12+256x^10-446x^8+256x^6-16x^4+1.
```

This is the genus-7 curve already isolated in A1-6. The result below is still specific to the corrected equation-(6) Hilbert-cube family.

## 1. Exact elliptic quotient and three genus-2 receivers

Put

```text
z = x^2 + x^-2,
Y = y/x^4,
Q(z)=z^4-20z^2+256z-412.
```

Direct expansion gives the identity

```text
F(x)/x^8 = Q(x^2+x^-2).                         (A1.8.1)
```

Hence every rational point of `C` with `x!=0` maps to

```text
E: Y^2 = Q(z).                                  (A1.8.2)
```

This is exactly the A1-3/A1-4 genus-1 quotient.

Now define

```text
W0 = (x^2-x^-2)Y,
W+ = (x+x^-1)Y,
W- = (x-x^-1)Y.
```

Then every rational point of `C` also maps to the three curves

```text
G0: W0^2 = (z^2-4)Q(z),                         (A1.8.3)
G+: W+^2 = (z+2)Q(z),                           (A1.8.4)
G-: W-^2 = (z-2)Q(z).                           (A1.8.5)
```

The quartic has

```text
disc(Q) = -2^27*5^2*19,
Q(2)=36,
Q(-2)=-988.
```

Therefore `Q` is squarefree and has no root at `z=+/-2`. Consequently all three hyperelliptic curves `G0,G+,G-` are nonsingular genus-2 curves over `Q`.

This is a strict global reduction: the genus-7 receiver now has three explicit genus-2 quotient receivers in addition to its elliptic quotient.

## 2. Exact reconstruction as two simultaneous square conditions on E

For a rational nonzero `x`,

```text
z+2 = (x+x^-1)^2,
z-2 = (x-x^-1)^2.                               (A1.8.6)
```

Conversely, suppose `(z,Y) in E(Q)` and both `z+2` and `z-2` are rational squares. Choose

```text
t+^2=z+2,
t-^2=z-2.
```

Then `t+^2-t-^2=4`. Choosing compatible signs and setting

```text
x   = (t+ + t-)/2,
1/x = (t+ - t-)/2
```

gives a rational nonzero `x` with `z=x^2+x^-2`; equation (A1.8.1) then reconstructs a rational point of `C`.

Thus, away from the already-known degenerate `x=+/-1` case,

```text
C(Q) <-> {(z,Y) in E(Q): z+2 and z-2 are both squares in Q}.   (A1.8.7)
```

This formulation is more rigid than the raw genus-7 equation. It turns the remaining global problem into simultaneous square conditions on a positive-rank elliptic curve and produces the genus-2 obstruction curves (A1.8.3)-(A1.8.5).

## 3. Self-contained Jacobian isogeny decomposition

Let

```text
omega_i = x^i dx/y,   i=0,...,6,
```

which is a basis of regular differentials on the genus-7 curve `C`.

The quotient maps above pull back standard differentials as follows (irrelevant common nonzero factor `2` retained for transparency):

```text
E:
  dz/Y          -> 2(omega_5-omega_1)

G0:
  dz/W0         -> 2 omega_3
  z dz/W0       -> 2(omega_5+omega_1)

G+:
  dz/W+         -> 2(omega_4-omega_2)
  z dz/W+       -> 2(omega_6-omega_4+omega_2-omega_0)

G-:
  dz/W-         -> 2(omega_4+omega_2)
  z dz/W-       -> 2(omega_6+omega_4+omega_2+omega_0).
```

After removing the common factor `2` from each row, the `7 x 7` coefficient matrix relative to `(omega_0,...,omega_6)` has determinant

```text
8 != 0.                                                (A1.8.8)
```

Therefore these seven pullback differentials span `H^0(C,Omega^1)`. The induced homomorphism from the product of the four lower-genus Jacobians to `Jac(C)` has full-rank tangent map; dimensions are

```text
1 + 2 + 2 + 2 = 7.
```

Hence it is an isogeny over `Q`:

```text
Jac(C)  ~_Q  E x Jac(G0) x Jac(G+) x Jac(G-).           (A1.8.9)
```

No external decomposition theorem is needed for the claim: the explicit maps plus the full-rank differential calculation certify the isogeny.

This materially lowers the global arithmetic wall from a single opaque genus-7 Jacobian to one known elliptic factor and three explicit genus-2 Jacobians.

## 4. A1-5 two-branch prime-to-leg allocation, with the missing sign included

Return to the audited A1-5 primitive Pythagorean receiver. Put

```text
A=a^8-8a^4b^4+b^8,
d=a^2-b^2,
g=gcd(|d|,6) in {1,6},
epsilon=sign(A) in {+1,-1},
|A|/g=M^2-N^2,
MN=(8/g)|a^3b^3d|,
gcd(M,N)=1.
```

For every prime `q>=5` dividing `ab` or `d`, exactly one of `M,N` is divisible by `q`. Reducing `M^2-N^2=|A|/g` modulo `q` gives the exact allocation rules

```text
q|ab:
  q|M => (-epsilon*g / q)=+1,
  q|N => ( epsilon*g / q)=+1;

q|d:
  q|M => ( epsilon*(6/g) / q)=+1,
  q|N => (-epsilon*(6/g) / q)=+1,               (A1.8.10)
```

where `(./q)` is the Legendre symbol.

For `q=3 mod 4` the two candidate characters differ by `(-1/q)=-1`, so the leg is uniquely determined. This strictly strengthens the A1-5 `q=1 mod 4` squareclass filter: it now records the full `M/N` allocation after the sign of `A` is included.

At the mandatory local-sieve prime `q=7`, because `(6/7)=-1`, one obtains

```text
             A>0        A<0
  g=1        7|N        7|M
  g=6        7|M        7|N.                    (A1.8.11)
```

Equivalently, for `R=M-N`, `S=M+N`, one has

```text
7|N => S == R  (mod 7),
7|M => S == -R (mod 7).                         (A1.8.12)
```

This is an exact branch/sign signature on the coprime odd `R,S` receiver. It is not by itself a contradiction, but it is a genuine narrowing and a useful consistency check for any subsequent genus-2 or descent computation.

## 5. What is and is not closed

A1-8 produces substantive new mathematics in two independent ways:

1. it replaces the genus-7 global wall by the explicit isogeny decomposition (A1.8.9), with three genus-2 factors;
2. it strengthens the A1-5 two-branch descent to a sign-correct prime-to-leg allocation rule (A1.8.10).

Therefore StageA1 should continue to one targeted genus-2 rational-point/Jacobian computation rather than close immediately.

The next exact target is:

- determine `G0(Q), G+(Q), G-(Q)` sufficiently to test the common-`z` reconstruction condition;
- or compute ranks/Selmer information on their Jacobians and apply a rigorous genus-2 rational-point method;
- if the required arithmetic cannot be certified with the repository toolchain, freeze the precise genus-2 computation as an external computational-algebra theorem wall instead of returning to finite-height or local-prime searches.

## 6. Firewalls

This result does **not** prove:

- that `C(Q)` has no nondegenerate rational point;
- that the equation-(6) Hilbert-cube family has no anchored member;
- that equation (6) is universal;
- any new necessary condition for every perfect cuboid;
- existence or nonexistence of a perfect cuboid.

All A1-8 receivers remain family-specific. Stage27 and StructureRadar are unchanged.

```text
A1_8_STATUS=SUBMITTED_FOR_AUDIT
A1_8_GENUS7_TO_ELLIPTIC_PLUS_THREE_GENUS2=true
A1_8_JACOBIAN_ISOGENY_OVER_Q=true
A1_8_DIFFERENTIAL_MATRIX_DETERMINANT=8
A1_8_SIMULTANEOUS_SQUARE_RECONSTRUCTION=true
A1_8_SIGN_CORRECT_PRIME_TO_LEG_ALLOCATION=true
A1_8_NEW_ARBITRARY_CUBE_CONSTRAINT=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
