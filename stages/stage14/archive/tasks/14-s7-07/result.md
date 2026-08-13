# Stage14-s7-07 — balanced denominator strip and inert-prime trace receiver

## Purpose

Merged Stage14-s7-06 reduces every physical first-hit pair to one squarefree `j=1728` twist

```text
E_n: Y^2 = X^3 + 4 n^2 X,
```

with `n>1`, positive rank, and a two-point multiplicative-height condition.  This stage puts that one-dimensional twist receiver back into exact reduced-coordinate variables and asks where a new saving below the current whole-family exponent `20/21` could come from.

The result is a precise receiver plus a precise barrier:

1. the twist parameter is the squarefree kernel of one fixed binary quartic
   `F(P,Q)=P Q (Q-P)(Q+P)`;
2. every sector with one small denominator is already bounded by the merged fixed-coordinate genus-one mechanism, so any improvement below `20/21` must occur in the balanced strip
   `Q,S = B^(1/2+O(1/42))`;
3. for every odd inert prime `p=3 mod 4`, the complete quadratic-character trace of `F` is exactly zero, and the same is true for squarefree products of inert primes;
4. however, one polynomial-size CRT modulus carries only `B^o(1)` independent sign bits, so a single-modulus equidistribution argument cannot by itself provide the fixed `B^(-1/21)` saving needed to beat `20/21`.

Thus the next analytic object is a **multi-modulus inert-prime second moment / large-sieve problem on the balanced denominator strip**, not another fixed-modulus congruence count.

No result from open Stage14-4bu is used as a theorem input.  The fixed quartic and inert-prime trace are derived independently here from merged s7-06.

---

## 1. Merged inputs

### 1.1 s7-06 squarefree twist receiver

For a reduced rational coordinate

```text
u=P/Q,
0<P<Q,
gcd(P,Q)=1,
```

merged s7-05/s7-06 define

```text
xi = ker(PQ),
k  = ker(Q^2-P^2),
n  = k*xi.
```

Because

```text
gcd(PQ,Q^2-P^2)=1,
```

we have `gcd(k,xi)=1`, hence `n` is squarefree.  Physical pairs satisfy `n>1`, and the two corresponding points differ by an infinite-order point on `E_n`.

The first two-point receiver is

```text
V(B) <= B^o(1) * #{squarefree n << B^2 : H_2(n) << B}.
```

The current proved whole-family exponent remains

```text
V(B) << B^(20/21+o(1)).
```

### 1.2 s7-03/s7-04 multiplicative height

For the two reduced physical coordinates

```text
u=P/Q,
w=R/S,
0<w<u<1,
```

we have

```text
H_mult = Q*S,
H_mult <= 2B.
```

For each fixed reduced coordinate, the merged bounded-height genus-one mechanism gives only `B^o(1)` compatible opposite coordinates in the physical polynomial-height range.

---

## 2. One fixed binary quartic

Define

```text
F(P,Q) = P*Q*(Q-P)*(Q+P)
       = P*Q*(Q^2-P^2).
```

Because the two factors `PQ` and `Q^2-P^2` are coprime,

```text
ker(F(P,Q))
 = ker(PQ) * ker(Q^2-P^2)
 = xi*k
 = n.
```

Hence every reduced physical coordinate represents the same squarefree twist parameter by the exact formula

```text
boxed:
n = ker(F(P,Q)).
```

For `0<P<Q`,

```text
0 < F(P,Q) < Q^4,
```

so

```text
n < Q^4.
```

The second coordinate gives the same identities with `(R,S)`.

Therefore a physical pair gives

```text
ker(F(P,Q)) = ker(F(R,S)) = n,
Q*S <= 2B.
```

The whole s7 first-point problem is now a same-squareclass collision problem for one fixed binary quartic on a denominator hyperbola.

---

## 3. Small-denominator sector

Let `L>=1`.  If

```text
min(Q,S) <= L,
```

then choose the smaller denominator coordinate first.  The number of reduced rationals with denominator at most `L` is

```text
O(L^2).
```

For each such fixed coordinate, merged s7-04 gives only `B^o(1)` compatible physical opposite coordinates.  Hence

```text
N_small(L) << L^2 * B^o(1).
```

To match the current `20/21` ceiling, take

```text
L = B^(10/21).
```

Then

```text
N_small(L) << B^(20/21+o(1)).
```

More generally, for any fixed `eta>0`,

```text
min(Q,S) <= B^(10/21-eta)
```

contributes

```text
O(B^(20/21-2eta+o(1))).
```

Therefore any new proof that beats `20/21` may restrict its genuinely difficult part to

```text
Q,S >= B^(10/21-o(1)).
```

Since `QS<=2B`, this simultaneously gives

```text
Q,S <= B^(11/21+o(1)).
```

Thus the critical receiver is the balanced strip

```text
boxed:
B^(10/21-o(1)) <= Q,S <= B^(11/21+o(1)),
Q*S <= 2B.
```

This is a much narrower family than the original unrestricted denominator hyperbola.

---

## 4. Exact inert-prime zero trace

Let `p` be an odd prime with

```text
p == 3 (mod 4).
```

Let `chi_p` be the quadratic character modulo `p`, extended by `chi_p(0)=0`.

For `Q!=0 mod p`, put `t=P/Q`.  Since `Q^4` is a square,

```text
chi_p(F(P,Q)) = chi_p(t*(1-t^2)).
```

Define

```text
T_p = sum_{t mod p} chi_p(t*(1-t^2)).
```

For `t notin {0,+1,-1}`, inversion gives

```text
f(1/t)/f(t) = -1/t^4,
f(t)=t*(1-t^2).
```

Because `p=3 mod 4`,

```text
chi_p(-1)=-1,
```

and therefore

```text
chi_p(f(1/t)) = -chi_p(f(t)).
```

The exceptional points `0,+1,-1` contribute zero.  Hence inversion pairs all remaining terms with opposite sign and

```text
boxed:
T_p=0.
```

Consequently the complete two-dimensional trace is exactly

```text
boxed:
sum_{P,Q mod p} chi_p(F(P,Q)) = 0.
```

No Weil error term is needed: this is exact cancellation.

---

## 5. Squarefree inert moduli

Let

```text
m = product p_i
```

be odd squarefree with every `p_i=3 mod 4`.  Let `chi_m` be the Jacobi symbol.

By CRT the complete two-dimensional sum factors into the product of the prime-modulus sums.  Since every prime factor contributes zero,

```text
boxed:
sum_{P,Q mod m} chi_m(F(P,Q)) = 0.
```

Thus every all-inert squarefree modulus is an exact zero-trace modulus for the fixed quartic.

---

## 6. Primitive incomplete-box bound

For `m<=U`, define

```text
S_m(U)
 = sum_{1<=P,Q<=U, gcd(P,Q)=1} chi_m(F(P,Q)).
```

Use Möbius inversion in `gcd(P,Q)`.  Since `F` is homogeneous of degree four, scaling by a `d` coprime to `m` multiplies `F` by the square `d^4`, so the character is unchanged; if `d` is not coprime to `m`, the corresponding terms vanish at a prime divisor of `m`.

For `X>=m`, tile the `X x X` box into complete `m x m` blocks plus boundary strips.  Complete blocks cancel exactly and the boundary has `O(Xm)` points.

For `X<m`, use the trivial `O(X^2)` bound.

Splitting the Möbius sum at `d=U/m` gives

```text
boxed:
S_m(U) << U*m*log(2U)
```

uniformly for all-inert squarefree `m<=U`.

This is a genuine signed cancellation estimate available on the balanced strip.

---

## 7. Why one CRT modulus is not enough

The same-squareclass condition implies that, away from primes dividing the values,

```text
chi_p(F(P,Q)) = chi_p(F(R,S))
```

for every inert test prime `p`.

It is tempting to choose one large squarefree inert modulus `m` and classify coordinates by the vector of signs

```text
(chi_p(F(P,Q)))_{p|m}.
```

However a polynomial-size modulus has only subpolynomially many prime factors:

```text
omega(m) = O(log B / log log B)
```

for `m<=B^C`.  Hence the total number of sign/zero patterns is at most

```text
3^omega(m) = B^o(1).
```

Even perfect equidistribution among all such patterns can therefore supply only a `B^o(1)` partition gain.  It cannot by itself force the fixed power

```text
B^(-1/21)
```

needed to improve the current `20/21` exponent.

This is an information-capacity obstruction for a **single polynomial-size CRT modulus**.  It does not rule out averaging over many independently varying moduli or primes.

So the exact zero trace is useful, but the next proof must exploit it through a true second moment / large sieve / dispersion family rather than a one-modulus residue-class split.

---

## 8. Correct next analytic receiver

On a dyadic balanced block

```text
Q ~ U,
S ~ V,
U*V <= B,
B^(10/21-o(1)) <= U,V <= B^(11/21+o(1)),
```

define the squareclass multiplicities

```text
r_U(n)
 = #{primitive 0<P<Q~U : ker(F(P,Q))=n},
```

with the physical-open / bounded-height restrictions retained when needed.

The principal collision energy is

```text
C(U,V) = sum_n r_U(n) r_V(n).
```

Merged fixed-curve geometry controls each fixed `n` fiber, but summing all twists still reaches the exponent-one barrier.  The inert-prime trace supplies exact nonprincipal character cancellation for the fixed quartic.

The next theorem must convert that cancellation into a bound of the schematic form

```text
C(U,V) << (UV)^(1-delta) * B^o(1)
```

or an equivalent active-twist estimate, with enough strength that the global exponent is strictly below `20/21`.

At the current threshold the required direct saving remains

```text
delta > 1/21
```

when measured against an exponent-one joint receiver; after one Cauchy, the corresponding squared-energy budget is `>2/21`.

The precise next target is therefore a **multi-modulus inert-prime squareclass large sieve for the fixed quartic `F(P,Q)` in the balanced denominator strip**.

---

## 9. What is proved and what remains

Proved here:

- exact fixed quartic twist formula `n=ker(PQ(Q-P)(Q+P))`;
- `n<Q^4` and the symmetric `n<S^4`;
- small-denominator sector `O(L^2 B^o(1))`;
- critical balanced strip `10/21` to `11/21`;
- exact zero complete trace for every inert prime `p=3 mod 4`;
- exact zero complete trace for all-inert odd squarefree moduli;
- primitive incomplete-box bound `S_m(U)<<U*m*log(2U)` for `m<=U`;
- one polynomial-size CRT modulus has only `B^o(1)` sign-pattern capacity and therefore cannot alone yield the needed fixed `1/21` power saving.

Not proved here:

- a multi-modulus squareclass large sieve with the required strength;
- a bound below `B^(20/21+o(1))`;
- the square-root upper bound.

```text
STAGE14_S7_07=COMPLETE_FIXED_QUARTIC_BALANCED_STRIP_AND_INERT_TRACE_RECEIVER
MERGED_S7_06_IMPORTED=true
OPEN_4BU_USED_AS_THEOREM_INPUT=false
TWIST_PARAMETER_FIXED_QUARTIC=PQ(Q-P)(Q+P)
TWIST_PARAMETER_IS_FIXED_QUARTIC_SQUAREFREE_KERNEL=true
SMALL_DENOMINATOR_SECTOR_BOUND=L^2*B^o(1)
CRITICAL_DENOMINATOR_EXPONENT=10/21
BALANCED_DENOMINATOR_STRIP_LOWER=10/21
BALANCED_DENOMINATOR_STRIP_UPPER=11/21
INERT_PRIME_COMPLETE_CHARACTER_SUM_ZERO=true
INERT_SQUAREFREE_MODULUS_COMPLETE_CHARACTER_SUM_ZERO=true
INERT_MODULUS_PRIMITIVE_BOX_BOUND=U*m*log(2U)
SINGLE_POLYNOMIAL_CRT_MODULUS_FIXED_POWER_SAVING=false
MULTI_MODULUS_INERT_LARGE_SIEVE_REQUIRED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-08
```
