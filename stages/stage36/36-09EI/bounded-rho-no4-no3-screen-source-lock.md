# Stage36 36-09EI — bounded rho no4/no3 screen source lock

## Purpose

36-09EH gives an exact sufficient criterion for excluding a fixed physical parameter `p` through the single rho elliptic quotient:

```text
Sel2_dim(E_rho,p/Q)=2,
+/-8h are both nonsquares,
E_rho,p(Q)[3]=0,
```

where `h=p-1/p`.

This leaf performs a deterministic exact **screen only** on the same bounded primitive positive parameter domain used by 36-09AX:

```text
p=a/b,
1 <= a,b <= 10,
gcd(a,b)=1,
a!=b.
```

It resolves the cheap no4/no3 parts of the EH criterion and identifies the remaining Sel2 obligation. It does not infer rank or fixed-p exclusion from the screen alone.

## Integral rho model for primitive a/b

Put

```text
N=a^2-b^2,
M=a^2+b^2,
d=ab.
```

Starting from the exact EH model

```text
Y^2=(X-4h)(X+4h)(X+r^2),
h=N/d,
r=M/d,
```

scale

```text
x=d^2 X,
y=d^3 Y.
```

Then the rho curve is Q-isomorphic to the integral full-2-torsion model

```text
y^2=(x-4Nd)(x+4Nd)(x+M^2).
```

The squareclasses controlling rational order-4 torsion are therefore exactly

```text
+8Nd,
-8Nd,
```

since multiplication by the square `d^2` does not change squareclass.

## Integral 3-division polynomial

The scaled Weierstrass equation is

```text
y^2=x^3+M^2*x^2-16*N^2*d^2*x-16*N^2*d^2*M^2.
```

Substituting into the standard `a1=a3=0` 3-division formula gives

```text
psi3(x)=
  3*x^4
  +4*M^2*x^3
  -96*N^2*d^2*x^2
  -192*N^2*d^2*M^2*x
  -64*N^2*d^2*(M^4+4*N^2*d^2).
```

Its leading coefficient is `3`. Hence any rational root has denominator dividing `3`. For any prime `q != 3`, a rational root would reduce to a root modulo `q` after clearing its possible denominator. Therefore a prime `q != 3` for which `psi3` has no root in `F_q` is an exact certificate that `psi3` has no rational root, hence that `E_rho,p(Q)[3]=0`.

## Deterministic witness-prime screen

The verifier enumerates all 62 ordered primitive pairs in the AX box and, for each row, performs:

1. exact integer square tests on `+8Nd` and `-8Nd`;
2. exact exhaustive root tests of `psi3 mod q` in the ordered witness-prime list
   `[5,7,11,13,17,19,23,29,31,37,41,43,47]`;
3. records the first prime with no root.

Exact outcome:

```text
ordered_parameter_count = 62
no4_pass_count = 62
no3_pass_count = 62
witness_prime_counts = {5:20, 11:36, 29:6}
```

The canonical row encoding is

```text
a,b,plus8Nd_is_square,minus8Nd_is_square,first_no_root_prime
```

in lexicographic `(a,b)` order, with booleans encoded as `0/1` and a trailing newline. Its SHA-256 digest is

```text
76ccf3835d0834c9f994822530719fc53e8915c1b06376c26f3f345ea7ac7973
```

## Exact interpretation

Every parameter in this bounded AX domain satisfies the EH no4 and no3 conditions. Thus, **within this bounded sample**, the only unresolved EH criterion is

```text
Sel2_dim(E_rho,p/Q)=2.
```

This is a reduction of the candidate computation, not a parameter exclusion. In particular:

```text
new_parameter_outside_EG_orbit_excluded = false
candidate_parameter_set_shrunk = false
receiver_emptiness_proved = false
```

A later leaf must source-lock an exact Sel2 computation (or another exact rank-zero/torsion certification) before any new fixed-p exclusion credit can be granted.
