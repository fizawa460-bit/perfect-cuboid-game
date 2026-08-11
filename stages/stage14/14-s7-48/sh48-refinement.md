# Stage14-sH48 pre-dispatch refinement — primitive product / sum-of-two-squares pair

This refinement is added **before** `Stage14-sH48` dispatch and is part of the frozen s7-48 source snapshot.  It does not change the requested theorem; it gives a more theorem-ready equivalent kernel.

Define the positive rotated real coordinates

```text
m := D+A,
n := D-A.
```

On every possible square-root-saturating packet,

```text
m,n=B^(1/4+o(1)).
```

Indeed `m+n=2D=B^(1/4+o(1))`, while

```text
m*n=D^2-A^2=epsilon_- u_* R J=B^(1/2+o(1)),
```

so neither factor can have a fixed-power deficit.

Furthermore

```text
gcd(m,n) | 2*gcd(D,A)=B^o(1).
```

After the already-permitted subpolynomial gcd/2-primary peel, `(m,n)` is primitive.

The frozen H kernel is therefore equivalently

```text
boxed:
m*n = epsilon_- u_* R J,

boxed:
m^2+n^2 = 2(D^2+A^2)=2*epsilon_+ C_* S T.       (R1)
```

The same pair `(m,n)` simultaneously has:

```text
product factorization:
  m*n = epsilon_- u_* R J,

sum-of-two-squares factorization:
  m^2+n^2 = 2*epsilon_+ C_* S T.
```

The physical scales remain

```text
C_*=B^(chi+o(1)),
u_*=B^(1/4-chi+o(1)),
S,T=B^(1/4-chi/2+o(1)),
R,J=B^((chi+1/4)/2+o(1)),
1/6<=chi<=1/4.
```

The four norm blocks `C_*`, `S*T`, `u_*`, `R*J` are pairwise separated at fixed-power scale by merged s7-47.

This form makes two important boundary facts explicit.

1. The product side is not an independent random integer: its three physical factors partition the prime support of the two primitive coordinates `m,n`.
2. Every odd prime on the sum-of-two-squares side is forced into split Gaussian support after the primitive peel; however this local restriction by itself is only a sieve-density effect and is not to be promoted to a fixed `B`-power saving without a theorem.

The exact H question is unchanged:

```text
# {(m,n) physical under (R1) and all masks}
 << B^(1/2-delta+o(1))
```

for some uniform fixed `delta>0`?

The H worker should use whichever equivalent language is strongest:

```text
Gaussian norm / rotated coordinate product,
primitive balanced pair product / sum-of-two-squares,
or a legally derived centered bilinear/divisor-switch form.
```

It must not count these as independent coordinate systems.

```text
SH48_PRE_DISPATCH_REFINEMENT=true
PRIMITIVE_ROTATED_PAIR_REDUCTION_PROVED=true
ROTATED_PAIR_PRODUCT=epsilon_minus*u_star*R*J
ROTATED_PAIR_SUM_SQUARES=2*epsilon_plus*C_star*S*T
ROTATED_PAIR_BOTH_COORDINATES_QUARTER_SCALE=true
SH48_REQUESTED_OBJECT_UNCHANGED=true
```
