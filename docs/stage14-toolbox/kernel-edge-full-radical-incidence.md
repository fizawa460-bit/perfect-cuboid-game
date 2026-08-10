# Stage14 toolbox — odd kernel edge packet and full-radical incidence

This page is the reusable arithmetic/incidence interface between the integral witness layer and the later two-quadrics/genus-one geometry. It repackages merged Stage14-s6-01, Stage14-4bi-L, Stage14-4bi-S, and Stage14-4bj. It does not prove a new Stage14 theorem.

## 1. Signed squarefree kernel edge packet

From an integral witness write

```text
Gi = di*ui^2
```

with `di` signed squarefree. Since `G0 G1 G2` is a square and the pairwise odd gcd supports lie only on the three Pythagorean edges, the odd support has the exact edge form

```text
d0 = tau0*a*b
d1 = tau1*a*c
d2 = tau2*b*c
```

where

```text
a | rad_odd(S)
b | rad_odd(X)
c | rad_odd(H)
gcd(a,b)=gcd(a,c)=gcd(b,c)=1.
```

Each `tau_i` lies in `{+1,-1,+2,-2}`. The condition that `d0*d1*d2` is a positive square leaves exactly 16 admissible ordered `tau` packets:

```text
product of the three signs = +1
number of even tau_i is even.
```

Thus the moving odd kernel state is carried by the three edge variables `a,b,c`; sign and the 2-primary part are finite.

## 2. Five-column refinement

For the s6 orientation

```text
S=2mn
X=(m-n)(m+n)
H=m^2+n^2,
```

the odd supports split uniquely as

```text
a = a_m * a_n
  a_m | rad(m)
  a_n | rad(n)

b = b_- * b_+
  b_- | rad(m-n)
  b_+ | rad(m+n)

c | rad(m^2+n^2).
```

This is the same five-column support system used by the closed local descent algebra. Use the orientation adapter from toolbox-ae if the historical s5 `S/X` convention is being used.

## 3. Edge-normalized equations

The fixed witness equations imply

```text
tau0*b*u0^2 - tau1*c*u1^2 = a*(S/a)^2*D^2
tau2*c*u2^2 - tau0*a*u0^2 = b*(X/b)^2*D^2
tau2*b*u2^2 - tau1*a*u1^2 = c*(H/c)^2*D^2.
```

Reducing modulo the selected composite edge kernels gives

```text
mod a: tau0*b*u0^2 == tau1*c*u1^2
mod b: tau2*c*u2^2 == tau0*a*u0^2
mod c: tau2*b*u2^2 == tau1*a*u1^2.
```

These congruences use the whole squarefree edge kernel. A largest prime divisor is not required.

## 4. Composite squarefree line cover

Let `q` be odd squarefree and let `A,B` be units modulo `q`. The solutions of

```text
A*x^2 == B*y^2 (mod q)
```

are covered by at most

```text
2^omega(q)
```

CRT projective lines modulo `q`. Each line is a rank-two lattice of index `q`. Hence in a dyadic rectangle of side lengths `U,V`,

```text
N_q(U,V)
  << 2^omega(q) * (U*V/q + min(U,V) + 1)
  <<_eps B^eps * (U*V/q + min(U,V) + 1)
```

for Stage14 witness variables in a polynomial `B`-box.

Therefore a large but very smooth squarefree kernel is still a useful modulus.

## 5. Full odd leg radicals

Define

```text
R_S = rad_odd(S)
R_X = rad_odd(X)
R_H = rad_odd(H).
```

Because `a|R_S` and every prime of `R_S/a` divides `S/a`,

```text
R_S | a*(S/a)^2.
```

Similarly,

```text
R_X | b*(X/b)^2
R_H | c*(H/c)^2.
```

Thus the edge-normalized equations strengthen to

```text
tau0*b*u0^2 == tau1*c*u1^2 (mod R_S)
tau2*c*u2^2 == tau0*a*u0^2 (mod R_X)
tau2*b*u2^2 == tau1*a*u1^2 (mod R_H).
```

This remains useful even if

```text
a=b=c=1.
```

So a small selected kernel is not an intrinsic modulus obstruction.

## 6. Full-radical rectangle bound

For example on the H-edge,

```text
N_H(U1,U2)
  <<_eps B^eps * (U1*U2/R_H + min(U1,U2) + 1).
```

The same bound holds with `(R_S,U0,U1)` and `(R_X,U0,U2)`.

If

```text
R_H >= B^rho
U_* = max(U1,U2) >= B^nu,
```

then the fixed witness-coordinate layer gains

```text
B^(-min(rho,nu)+eps)
```

relative to the unconstrained incident rectangle.

This is a coordinate-density theorem. It is not automatically an unweighted packet-existence saving.

## 7. Radical-poor bases

Merged 4bi-S proves

```text
#{n<=B : rad(n)<=B^rho} << B^(rho+eps).
```

After primitive Pythagorean representation multiplicity and the closed packet multiplicity are included,

```text
#{supported base/classes : H<=B, R_H<=B^rho}
  << B^(rho+eps).
```

Taking `rho=1/2` therefore places the radical-poor hypotenuse family already at square-root scale.

## 8. Radical-rich long/short split

For a radical-rich H-edge let

```text
U_* = max(|u1|,|u2|).
```

The normalized packet equation gives the deterministic size forcing

```text
D <= 2*U_*.
```

Hence for thresholds `rho,nu>0`:

```text
R_H >= B^rho and U_* >= B^nu
  -> full-radical coordinate gain B^(-min(rho,nu)+eps)

R_H >= B^rho and U_* < B^nu
  -> D < 2*B^nu.
```

At the main-track critical choice

```text
rho = 1/2
nu  = 10/21,
```

the long coordinate layer supplies the whole missing `10/21` coordinate exponent, while the short layer transfers to small denominator.

## 9. Hard quantifier boundary

Never use

```text
B^(41/42) packet count * B^(-delta) coordinate density
```

without an existence/occupancy transfer theorem. A packet counts once if it has one witness; a coordinate-density estimate counts possible witness coordinates inside a fixed packet box.

Accordingly:

```text
coordinate incidence saving != packet-existence saving
small selected kernel != small full radical
largest prime factor not required
full-radical long-coordinate saving != full-family delta_post
```

The merged main track eventually isolates the remaining packet-level issue as radical-rich least-denominator/canonical-witness occupancy. This atlas does not claim that issue is solved.

## 10. Handoff

Use this interface as follows:

```text
integral witness
 -> signed kernel edge packet
 -> five-column odd support
 -> selected composite edge modulus
 -> full leg radical modulus
 -> CRT line/lattice incidence
 -> radical-rich long coordinate OR small-D transfer.
```

The next toolbox theme treats the fixed packet as an intersection of two quadrics and records its genus-one geometry. Do not mix that geometric layer into the arithmetic support rules above.
