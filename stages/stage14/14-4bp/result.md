# Stage14-4bp — largest incidence prime-power packets and moving-z elliptic receiver

## Purpose

Merged Stage14-4bo compresses the unresolved main-track residual to a normalized core

```text
C=(a0,b0,c0,d0)
Q=q11*q12*q21*q22=X2_good>B^(16/21)
```

with

```text
kappa2*a0*b0=X2_cross<B^(4/21)
kappa3*c0*d0=X3/Q<B^(5/21)
#C << B^(3/7+o(1)).
```

For fixed `Q`, allocation of its prime powers among the four pairwise-coprime good gcd cells costs only `4^omega(Q)=B^o(1)`.

This stage decomposes the one-dimensional moving-`Q` receiver at its largest prime. The outcome is:

1. the largest prime of `Q` is an **incidence prime**, not the t37/t38 Gaussian-norm canonical prime;
2. after extracting its full prime power `z=ell^v_ell(Q)` from its unique cell, fixing the normalized core and the remaining cofactor turns the normalized square condition into `Y^2=K*(A^2-B^2*z^4)` up to sign;
3. this is a smooth genus-one quartic with rational 2-torsion on the Jacobian, so the merged t22 bounded-height mechanism gives only `B^o(1)` admissible moving `z` values per fixed descended packet;
4. consequently

```text
E_res(z>=B^lambda) << B^(10/7-lambda+o(1)).
```

At `lambda=29/63` this reaches the already-proved cross ceiling `B^(61/63+o(1))`.

The complementary composite incidence sector remains open, so the whole-family exponent stays `41/42`.

---

## 1. Merged inputs

For the transferred primitive half-angle pairs write

```text
F2: (a,b)
F3: (c,d)
```

with odd-prime coprimality `gcd(a,b)=gcd(c,d)=1`.

The good gcd cells satisfy

```text
q11=q--, q12=q-+, q21=q+-, q22=q++

a=q11*q12*a0
b=q21*q22*b0
c=q11*q21*c0
d=q12*q22*d0

Q=q11*q12*q21*q22=X2_good.
```

Merged s6-08 gives

```text
F=(q12^2*a0*d0)^2-(q21^2*b0*c0)^2
G=(q22^2*b0*d0)^2-(q11^2*a0*c0)^2
Delta_norm=F*G=square>0.
```

The raw `Q^2` factor has already been extracted as an automatic square; no `1/Q` density gain may be recharged.

Merged t37/t38 instead uses a Gaussian direction

```text
A_c=a+i*b=pi*U
N(pi)=ell_can
```

so its canonical prime divides `a^2+b^2`.

---

## 2. The largest prime of Q is not the t37/t38 canonical prime

Let `ell=P+(Q)`. Since `Q|X2_good|X2` and `X2=kappa2*a*b`, an odd `ell|Q` divides exactly one of `a,b`. Therefore

```text
ell|a => a^2+b^2 == b^2 != 0 mod ell
ell|b => a^2+b^2 == a^2 != 0 mod ell.
```

Hence

```text
boxed: gcd(Q,a^2+b^2)=1
boxed: gcd(Q,H2)=1
```

at odd primes. Thus

```text
4bo incidence prime: ell | X2
t37/t38 norm prime:  ell_can | H2
```

and they are arithmetically disjoint on the same primitive direction.

```text
T37_T38_CANONICAL_PRIME_IDENTIFIED_WITH_Q_LARGEST_PRIME=false.
```

The t38 theorem cannot be imported by renaming `ell`.

---

## 3. Extract the full largest-prime power

Put

```text
e=v_ell(Q)
z=ell^e
R=Q/z.
```

Because the four cells are pairwise coprime and each good prime power occurs with its full exponent, `z` lies in exactly one cell. Write that cell as `qij=z*rij`.

Fixing the core, the cell index, the residual `rij`, and the other cells defines a descended incidence packet. For fixed `R`, the cell allocation multiplicity is at most

```text
4^(omega(R)+1)=B^o(1).
```

The largest-prime constraints may be discarded in upper bounds.

---

## 4. Exact moving-z quartic

Fix a descended packet and move only `z`.

If `z|q11`, write `q11=z*r11`. Then

```text
F = fixed
G(z)=(q22^2*b0*d0)^2-(r11^2*a0*c0)^2*z^4.
```

If `z|q22`,

```text
F = fixed
G(z)=(r22^2*b0*d0)^2*z^4-(q11^2*a0*c0)^2.
```

If `z|q12`,

```text
G = fixed
F(z)=(r12^2*a0*d0)^2*z^4-(q21^2*b0*c0)^2.
```

If `z|q21`,

```text
G = fixed
F(z)=(q12^2*a0*d0)^2-(r21^2*b0*c0)^2*z^4.
```

Therefore in all four cells

```text
boxed: Delta_norm(z)=K*(A^2-B^2*z^4)
```

up to replacing `K` by `-K`, with fixed nonzero integers `A,B,K`. Physical nondegeneracy gives `A^2-B^2*z^4 != 0` at every counted point.

---

## 5. Genus-one multiplicity

For fixed nonzero `A,B,K`, consider

```text
C: Y^2=K*(A^2-B^2*Z^4).
```

The quartic factors as

```text
K*(A-B*Z^2)*(A+B*Z^2).
```

Since `ABK!=0`, it has four distinct geometric branch points and is a smooth genus-one curve. The rational factorization into two quadratics gives rational 2-torsion on the Jacobian.

If the descended packet is active, one actual physical `z0` supplies a rational point, so the twist is an elliptic curve over `Q`. Its coefficients and physical `z` height are polynomially bounded in `B`.

The merged t22 bounded-height theorem, used already in t37/t38 for the same rational-2-torsion genus-one setup, therefore yields

```text
boxed:
# {admissible z for one fixed descended packet} <= B^o(1).
```

This counts all bounded-height rational/integer `Z`, so it is stronger than restricting to largest prime powers.

```text
T38_CANONICAL_PRIME_THEOREM_DIRECTLY_APPLIED=false
T22_BOUNDED_HEIGHT_GENUS_ONE_MECHANISM_REUSED=true.
```

---

## 6. Large-z sector

Let `L=B^lambda`. If `z>=L`, then `Q=zR<=X2<=B`, hence `R<=B/L`.

There are `B^(3/7+o(1))` normalized cores. For each core there are `O(B/L)` possible `R`, only `B^o(1)` cell allocations, and only `B^o(1)` admissible moving `z` values per descended packet. Hence

```text
boxed:
E_res(z>=L)
 << B^(3/7)*(B/L)*B^o(1)
 = B^(10/7)/L * B^o(1).
```

Equivalently,

```text
boxed:
E_res(z>=B^lambda)
 << B^(10/7-lambda+o(1)).
```

---

## 7. Exact exponent thresholds

To beat the current `41/42`, one needs

```text
lambda > 10/7-41/42 = 19/42.
```

To reach the merged cross ceiling `61/63`, one needs

```text
lambda >= 10/7-61/63 = 29/63.
```

Thus

```text
boxed:
z>=B^(29/63)
=> E_res << B^(61/63+o(1)).
```

For `z>=B^(1/2)`,

```text
E_res << B^(13/14+o(1))
```

and

```text
41/42-13/14 = 1/21.
```

To force this residual alone to square-root scale would require `lambda>=13/14`.

---

## 8. Hard complement

Use `lambda0=29/63`. The unresolved complement has

```text
Q>B^(16/21)=B^(48/63)
z<B^(29/63).
```

Since `Q=zR`,

```text
boxed: R>B^(19/63).
```

Thus the remaining moving-`Q` problem has the two-scale form

```text
z < B^(29/63)
R > B^(19/63)
Q=zR > B^(48/63)
P+(R)<P+(z)
```

up to endpoint constants. This is now a genuine composite Type-I/Type-II incidence receiver rather than an arbitrary moving integer.

---

## 9. Relation to merged t38 and s7

Merged t38's prime is a Gaussian norm prime; the present `ell` is an incidence prime. The theorem itself does not transfer.

The architecture does transfer:

```text
fix descended packet
-> move one distinguished arithmetic factor
-> obtain a genus-one quartic
-> apply uniform bounded-height multiplicity.
```

4bp executes this independently for the rational incidence prime power `z`.

Merged s7 remains the family-level first-nonboundary-point route. 4bp is complementary and supplies a concrete two-scale arithmetic receiver.

---

## Boundary

```text
STAGE14_4BP=LARGEST_INCIDENCE_PRIME_POWER_ELLIPTIC_PACKET_AND_LARGE_Z_BOUND
MERGED_4BO_IMPORTED=true
MERGED_S6_08_IMPORTED=true
MERGED_T37_T38_BOUNDARY_AUDITED=true
Q_LARGEST_PRIME_IS_INCIDENCE_PRIME=true
Q_ODD_PRIMES_COPRIME_TO_DIRECTION_NORM=true
T37_T38_CANONICAL_PRIME_IDENTIFIED_WITH_Q_LARGEST_PRIME=false
FULL_LARGEST_PRIME_POWER_Z=ell^v_ell(Q)
LARGEST_PRIME_POWER_OCCURS_IN_UNIQUE_GCD_CELL=true
MOVING_Z_QUARTIC_EXACT=true
MOVING_Z_CURVE_GENUS_ONE=true
MOVING_Z_JACOBIAN_HAS_RATIONAL_2_TORSION=true
FIXED_DESCENDED_PACKET_MOVING_Z_MULTIPLICITY=B^o(1)
LARGE_Z_SECTOR_BOUND=B^(10/7-lambda+o(1))
LARGE_Z_ANY_IMPROVEMENT_THRESHOLD=19/42
LARGE_Z_CROSS_CEILING_THRESHOLD=29/63
SUPER_SQRT_Z_SECTOR_BOUND=B^(13/14+o(1))
SUPER_SQRT_Z_SECTOR_GAIN_VS_41_42=1/21
HARD_COMPLEMENT_Z_EXPONENT_LT=29/63
HARD_COMPLEMENT_R_EXPONENT_GT=19/63
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bq
```
