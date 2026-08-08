# E-1e — pair-overlap lower order and exactly-one synthesis

> **STATUS:** `E_1E_COMPLETE_EXACT_ONE_ASYMPTOTIC`
>
> **COUNTING:** primitive canonical `0<a<b<c`, with `a^2+b^2+c^2<=B^2`
>
> **SPACE DIAGONAL:** integrality not required

E-1e closes the first Euler-side population layer.  E-1d already proved the raw one-face asymptotic

```text
A_q(B) ~ [6 I_q/pi^4] B^2 log B,
q in {ab,ac,bc},
```

with the Stage13 chamber integrals `I_q`.  The only remaining question was whether removing cuboids with a second or third integral face could change that leading term.

It cannot.  On the Euler side the overlap bound is substantially simpler than the Stage13 space-diagonal-side sieve because two integral faces necessarily share one ordinary edge, and the number of Pythagorean partners of a fixed edge is divisor-bounded.

## 1. Fixed-edge Pythagorean partner lemma

For a positive integer `n`, define

```text
P(n) = {x>0 : n^2+x^2 is a square}.
```

If `x in P(n)`, write

```text
n^2+x^2=y^2,
y>x>0.
```

Then

```text
(y-x)(y+x)=n^2.
```

Thus every Pythagorean partner `x` determines a positive factor pair

```text
u=y-x,
v=y+x,
uv=n^2,
u<v.
```

Conversely, a factor pair with the required parity gives

```text
x=(v-u)/2,
y=(v+u)/2.
```

For an upper bound parity need not be analyzed.  The map from solutions to factor pairs is injective, hence

```text
|P(n)| <= tau(n^2),
```

where `tau` is the divisor-counting function.

This is the key simplification.

## 2. Pair-overlap bounds

Let

```text
O_ab_ac(B)
O_ab_bc(B)
O_ac_bc(B)
```

be the primitive canonical populations in which the indicated two face diagonals are both integral.  The geometric cutoff and primitivity restriction can only reduce the following upper bounds.

### `ab & ac`

The two integral faces share edge `a`:

```text
a^2+b^2 = square,
a^2+c^2 = square.
```

For fixed `a`, both `b` and `c` lie in `P(a)`.  Therefore the number of possible ordered/canonical pairs is at most

```text
|P(a)|^2 <= tau(a^2)^2.
```

Since every edge is `<B`,

```text
O_ab_ac(B) <= sum_{a<B} tau(a^2)^2.
```

### `ab & bc`

The shared edge is `b`:

```text
a^2+b^2 = square,
b^2+c^2 = square.
```

For fixed `b`, both `a` and `c` are Pythagorean partners of `b`, so

```text
O_ab_bc(B) <= sum_{b<B} tau(b^2)^2.
```

### `ac & bc`

The shared edge is `c`:

```text
a^2+c^2 = square,
b^2+c^2 = square.
```

For fixed `c`, both `a` and `b` are partners of `c`, hence

```text
O_ac_bc(B) <= sum_{c<B} tau(c^2)^2.
```

Consequently every pair overlap satisfies the uniform bound

```text
O_qr(B) <= sum_{n<B} tau(n^2)^2.
```

## 3. Divisor bound gives lower order

The standard divisor bound says that for every `epsilon>0`,

```text
tau(m) <<_epsilon m^epsilon.
```

Equivalently, after renaming the exponent,

```text
tau(n^2)^2 <<_epsilon n^epsilon
```

for every fixed `epsilon>0`.  Therefore

```text
sum_{n<B} tau(n^2)^2 <<_epsilon B^(1+epsilon).
```

Hence for each pair of directions,

```text
O_qr(B) = B^(1+o(1)).
```

In particular, choosing any fixed `epsilon<1`, for example `epsilon=1/2`, gives

```text
O_qr(B) = O(B^(3/2))
        = o(B^2 log B).
```

The precise exponent `3/2` is not intrinsic; it is only a convenient consequence of the general divisor bound.  The useful statement is

```text
O_qr(B)=B^(1+o(1))=o(B^2 log B).
```

No quadratic-residue sieve is needed on this side.

## 4. Triple overlap is automatically lower order

Let `T(B)` be the population with all three face diagonals integral, i.e. the primitive Euler-brick population under the same canonical cutoff.  Every triple-overlap point belongs to every pair overlap, so

```text
0 <= T(B) <= O_qr(B)
```

for each pair `qr`.  Therefore

```text
T(B)=B^(1+o(1))=o(B^2 log B).
```

This is a population upper bound only.  It does **not** say that Euler bricks are absent; they are known to exist, and E-1e makes no emptiness claim.

## 5. Transfer from raw to exactly-one

The exact inclusion-exclusion identities are

```text
N_ab = A_ab - O_ab_ac - O_ab_bc + T,
N_ac = A_ac - O_ab_ac - O_ac_bc + T,
N_bc = A_bc - O_ab_bc - O_ac_bc + T.
```

All correction terms are `o(B^2 log B)`.  Combining this with E-1d gives, categorywise,

```text
N_q(B)
 = A_q(B) + o(B^2 log B)
 ~ [6 I_q/pi^4] B^2 log B.
```

Thus the raw theorem transfers unchanged to the **exactly-one** population.

## 6. Main E-1 theorem

For primitive canonical integer triples

```text
0<a<b<c,
gcd(a,b,c)=1,
a^2+b^2+c^2<=B^2,
```

with exactly one integral face diagonal and with no condition on integrality of the space diagonal,

```text
N_ab(B) ~ [6 I_ab/pi^4] B^2 log B,
N_ac(B) ~ [6 I_ac/pi^4] B^2 log B,
N_bc(B) ~ [6 I_bc/pi^4] B^2 log B.
```

The chamber constants are

```text
I_ab = 0.659705248705705...
I_ac = 0.3026997526726076...
I_bc = 0.2712955487578571...
I_ab+I_ac+I_bc = pi^2/8.
```

Summing the three categories,

```text
N_1(B)
 ~ [6/pi^4]*(pi^2/8) B^2 log B
 = [3/(4 pi^2)] B^2 log B.
```

Numerically,

```text
3/(4 pi^2) = 0.07599088773175333...
```

## 7. Normalized exactly-one limit

After dividing by `N_1(B)`,

```text
(N_ab,N_ac,N_bc)/N_1
->
(8 I_ab/pi^2,
 8 I_ac/pi^2,
 8 I_bc/pi^2)
```

which is

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
```

Equivalently, normalized by `bc`,

```text
ab:ac:bc
-> 2.431684750178191 : 1.115756428951881 : 1.
```

This is exactly the normalized Stage13 space-diagonal-side theorem.

So the earlier numerical surprise is now structural rather than merely empirical:

```text
space diagonal integral      -> same leading directional vector
space diagonal unrestricted  -> same leading directional vector
```

while the absolute growth laws differ strongly.

## 8. Comparison with the space-diagonal-first track

The two exactly-one asymptotics now have the parallel form

```text
Euler / unrestricted-D side:
N_q^E(B) ~ [6 I_q/pi^4] B^2 log B

space-diagonal-integral side:
N_q^S(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3.
```

The common factor `I_q` is the canonical real-place chamber weight.  The space-diagonal condition changes the radial/arithmetic density and therefore the absolute scale, but it does not change the leading normalized direction.

This explains why the two experiments can look so similar in `ab/ac/bc` proportions even though they select very different sets of integer cuboids.

## 9. Finite overlap audit

The E-1b exact enumeration already shows the expected separation of scales.  Define the summed pair-overlap ledger

```text
O_sum=O_ab_ac+O_ab_bc+O_ac_bc.
```

For the audited E-1b cutoffs,

| B | O_sum / raw-incidence-total | O_sum / (B^2 log B) |
|---:|---:|---:|
| 100 | 2.0498e-2 | 1.2160e-3 |
| 200 | 1.3223e-2 | 8.1158e-4 |
| 500 | 7.0139e-3 | 4.4733e-4 |
| 1,000 | 4.1300e-3 | 2.6825e-4 |
| 2,000 | 2.4075e-3 | 1.5896e-4 |
| 5,000 | 1.1718e-3 | 7.8632e-5 |
| 10,000 | 6.6817e-4 | 4.5297e-5 |

These finite values are not needed for the proof, but they are consistent with the divisor-bound lower-order theorem.

## 10. Consequence for the next Euler layer

The proof also gives an immediate coarse upper bound for populations with at least two integral face diagonals:

```text
N_{>=2}(B) = B^(1+o(1)).
```

Thus the exactly-two / Euler-brick layer is much sparser than the exactly-one `B^2 log B` layer.  E-2 should study its internal directional structure rather than expect another population on the same scale.

## 11. Decision

```text
E_1E=COMPLETE_EXACT_ONE_ASYMPTOTIC
E_1=COMPLETE
CANONICAL_ORDER=0<a<b<c
SPACE_DIAGONAL_INTEGRALITY_REQUIRED=false
FIXED_EDGE_PARTNER_BOUND=|P(n)|<=tau(n^2)
PAIR_OVERLAP_BOUND=B^(1+o(1))
PAIR_OVERLAP_LOWER_ORDER=true
TRIPLE_OVERLAP_LOWER_ORDER=true
RAW_TO_EXACT_ONE_TRANSFER=true
EXACT_ONE_SCALE=B^2_LOG_B
EXACT_ONE_TOTAL_CONSTANT=3/(4*pi^2)
EXACT_ONE_DIRECTIONAL_CONSTANT_q=6*I_q/pi^4
NORMALIZED_LIMIT_PROVED=true
NORMALIZED_LIMIT_EQUALS_STAGE13=true
LIMIT_EQUALS_2_1_1=false
NEXT=E-2a exactly-two population definition and finite census
```
