# Stage35-EX 35EX-13 — alternate-norm symmetry and Gaussian coupling

## Scope

Assume the conditional exact reductions through 35EX-12 and a hypothetical E1 counterexample. This leaf tests only

```text
35EX-13_ALTERNATE_NORM_SYMMETRY_COMPATIBILITY
```

The purpose is to decide whether the unused `W2/V1` cross channel creates a genuinely new primitive condition, or merely reproduces the already-audited three-reservoir receiver after exchanging the two primitive Euclid triples.

No E1, receiver, Stage35, Stage29-parent, or endpoint credit is claimed.

## 1. Exact alternate norm and canonical gcd

Keep

```text
U1=a^2-b^2, V1=2ab, W1=a^2+b^2,
U2=m^2-n^2, V2=2mn, W2=m^2+n^2,
c=gcd(U1,U2),
p=gcd(W1,V2),
q=gcd(V1,V2).
```

Introduce the unused cross gcd

```text
d = gcd(V1,W2).
```

Primitivity gives

```text
gcd(c,d)=gcd(p,d)=gcd(q,d)=1,
d odd.
```

The alternate raw legs satisfy the identity

```text
(W1*U2)^2 + (U1*V2)^2
  = (U1*W2)^2 + (V1*U2)^2.              (AN)
```

Indeed both sides differ by

```text
U2^2*(W1^2-V1^2)-U1^2*(W2^2-V2^2)=0.
```

Exactly as in 35EX-02, the only cross-prime contributions to

```text
g1 = gcd(U1*W2, V1*U2)
```

come from `(U1,U2)` and `(W2,V1)`. Hence

```text
g1 = c*d.                               (AGCD)
```

## 2. Second primitive E1 triple

If E1 fails, the left side of `(AN)` is a square. Therefore the alternate raw pair is square as well. Dividing by its exact gcd `c*d` gives the primitive odd/even pair

```text
xi_alt  = (U1/c)*(W2/d),
eta_alt = (V1/d)*(U2/c).
```

Thus there are coprime opposite-parity integers

```text
x > y > 0
```

with

```text
(U1/c)*(W2/d) = x^2-y^2,
(V1/d)*(U2/c) = 2*x*y,
z = x^2+y^2.                              (ALT-PYTH)
```

If `w=r^2+s^2` is the original reduced E1 hypotenuse from 35EX-03, equality of the positive raw hypotenuses gives

```text
c*p*w = c*d*z,
p*w = d*z.                                (ALT-HYP)
```

Since `gcd(p,d)=1`,

```text
d | w,
p | z,
```

so there is a positive odd integer `k` with

```text
w=d*k,
z=p*k.
```

This common-hypotenuse coupling is not part of the original one-orientation three-reservoir graph.

## 3. Index-swap involution: what is not new

Exchange the two primitive Euclid triples:

```text
(U1,V1,W1) <-> (U2,V2,W2).
```

The Master square is invariant, the E1 norm is carried to the right side of `(AN)`, and

```text
c -> c,
q -> q,
p -> d,
d -> p,
k1<k2 <-> k1>k2.
```

Therefore the alternate primitive triple `(x,y)` is exactly the original 35EX-03 E1 construction applied to the swapped Master-Hit. Consequently a second four-factor receiver obtained only by replaying 35EX-05 with `(x,y)` is not an independent theorem species: it is the index-swapped copy of the already-audited reduction.

For completeness, the swapped additive receiver is explicit. In original Branch L (`k1<k2`) one has

```text
2*d*x*y = q*(u^2-v^2),
d*(x^2-y^2) +/- 2*q*u*v = (U1/c)*(m +/- n)^2,
```

which yields the Branch-R-shaped four-factor square

```text
[x(u-v)-y(u+v)]
[x(u+v)+y(u-v)]
[x(u-v)+y(u+v)]
[x(u+v)-y(u-v)] = square.
```

In original Branch R (`k1>k2`) one has

```text
d*x*y = q*u*v,
d*(x^2-y^2) +/- q*(u^2-v^2) = (U1/c)*(m +/- n)^2,
```

which yields the Branch-L-shaped four-factor square

```text
(xu+yv)(xv-yu)(xu-yv)(xv+yu) = square.
```

These are useful mirrored coordinates, but by themselves they are dominated by the exact index-swap involution and do not count as a new independent receiver.

## 4. New joint Gaussian compatibility

Define the two source Gaussian integers

```text
Z1 = W1*U2 + i*U1*V2,
Z2 = U1*W2 + i*V1*U2.
```

Under an E1 counterexample the fixed odd/even orientation gives, with no unit ambiguity,

```text
Z1/(c*p) = (r+i*s)^2,
Z2/(c*d) = (x+i*y)^2.
```

Hence every E1 counterexample must satisfy the source-only condition

```text
Q = (d/p)*(Z1/Z2) in Q(i)^{x2}.          (GQ)
```

More explicitly,

```text
Q = ((r+i*s)/(x+i*y))^2.
```

This is the genuinely new information in the alternate-norm view: not the mirrored receiver separately, but the squareclass coupling between the two orientations.

The norm of `Q` is identically the rational square

```text
N_Q = (d/p)^2.
```

Writing

```text
N = (W1*U2)^2 + (U1*V2)^2,
```

and using

```text
Z1+Z2 = 2*(a*m-b*n)*[(a*m+b*n)+i*(a*n+b*m)],
```

one obtains an equivalent one-coordinate rational-square test

```text
S_plus = d*(W1*W2+V1*V2)/(p*N) in Q^{x2}.   (GS)
```

Indeed for a square root `Q=(X+iY)^2`,

```text
X^2 = (d/p + Re(Q))/2
    = (a*m-b*n)^2 * S_plus.
```

The factor `a*m-b*n` is nonzero for positive primitive Euclid parameters here, so `(GQ)` and `(GS)` are equivalent. The imaginary coordinate is then rational automatically from `2XY=Im(Q)`.

Thus `(GS)` is a cheap exact source-only necessary condition for an E1 counterexample. It is weaker than E1 itself and must not be promoted to an E1 theorem.

## 5. Bounded regression evidence only

For the deterministic primitive panel

```text
2 <= a <= 50,
1 <= b < a,
2 <= m <= 100,
1 <= n < m,
gcd(a,b)=gcd(m,n)=1,
a-b and m-n odd,
Master square = square,
```

there are 131 Master-Hits. The source-only Gaussian condition `(GS)` survives on exactly three:

```text
(8,5,11,2),
(11,2,8,5),
(17,16,52,47).
```

All three still fail E1 directly. Therefore this bounded panel records only

```text
GAUSSIAN_SOURCE_SIEVE_KILLS_128_OF_131=true
GAUSSIAN_SOURCE_SIEVE_PROVES_E1=false.
```

The count is regression/evidence only and carries no global theorem credit.

## 6. Exact route decision

35EX-13 therefore separates two conclusions:

```text
MIRRORED_FOUR_FACTOR_RECEIVER_NEW_INDEPENDENT_THEOREM=false
INDEX_SWAP_DOMINATES_MIRRORED_RECEIVER=true
GAUSSIAN_ORIENTATION_COUPLING_PROVED_CONDITIONALLY=true
SOURCE_ONLY_GAUSSIAN_SQUARE_SIEVE_PROVED_CONDITIONALLY=true
E1_PROVED=false
```

The alternate-norm route is not frozen: the new coupling is materially stronger than merely replaying the swapped three-reservoir graph. The next exact leaf should analyze the arithmetic structure of the `Q`-square survivors and test whether the joint orientation condition supplies an exact receiver-restricted local obstruction. If it does not, freeze the alternate-norm route before changing theorem species.

## Next exact leaf

```text
35EX-14_GAUSSIAN_RATIO_SURVIVOR_STRUCTURE
```

Required tasks:

1. derive prime/gcd support of the rational square condition `(GS)` without using bounded counts as proof;
2. compare it with the original and swapped three-reservoir routing simultaneously;
3. consult the already-matched `S34-W03` receiver-restricted intersection pattern before inventing a new local theorem;
4. either obtain an exact joint-local obstruction or record the surviving free support and freeze this route.

## Credit boundary

```text
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
