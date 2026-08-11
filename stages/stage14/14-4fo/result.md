# Stage14-4fo — polynomial complementary dilation: inner physical weight to outer-pair support

## Status

`COMPLETE_POLYNOMIAL_E_WEIGHTED_UNITARY_CORRELATION_TO_OUTER_PAIR_PHYSICAL_SUPPORT`

Consumes batch-local `Stage14-4fn`, merged `Stage14-4fm`, merged `Stage14-s7-95`, and merged `Stage14-Work-btX32`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Polynomial-E branch

On the branch

```text
E=B^(epsilon+o(1)), epsilon>0,
```

write

```text
n=E*m,
u || m,
v=m/u.
```

Let

```text
U_phys(E,m)
```

be the transported short unitary-divisor interval and let

```text
k(E,m,u)
 := m_E(E) m_cpl(E*m,u,m/u,E)
```

be the exact retained physical Boolean. No factorization between `E`, `m`, and `u` is assumed.

The polynomial-E heavy incidence is

```text
I_poly
 = sum_E sum_m
   sum_{u || m, u in U_phys(E,m)} k(E,m,u).         (1)
```

## 2. The inner unitary fiber remains subpolynomial for every outer pair

For each fixed `(E,m)`,

```text
#{u || m : u in U_phys(E,m)}
 <= 2^omega(m)
 <= tau(m)
 = B^o(1).                                         (2)
```

Therefore define

```text
A_poly(E,m)
 := 1{there exists u || m,
       u in U_phys(E,m),
       k(E,m,u)=1}.
```

Exactly as in Stage14-4fn,

```text
A_poly(E,m)
 <= sum_u k(E,m,u)
 <= B^o(1) A_poly(E,m).                            (3)
```

Summing over the polynomial outer pair gives

```text
sum_{E,m} A_poly(E,m)
 <= I_poly
 <= B^o(1) sum_{E,m} A_poly(E,m).                  (4)
```

Hence the inner-dependent canonical/reverse weight cannot create polynomial multiplicity at a fixed outer pair. At exponent level it projects to the support of the exact outer-pair acceptance Boolean `A_poly(E,m)`.

```text
POLYNOMIAL_E_FIXED_OUTER_PAIR_INNER_FIBER=Bo1
POLYNOMIAL_E_OUTER_PAIR_ACCEPTANCE_BOOLEAN_DEFINED=true
POLYNOMIAL_E_WEIGHTED_INCIDENCE_OUTER_PAIR_SUPPORT_EXPONENT_EQUIVALENT=true
POINTWISE_OUTER_INNER_FACTORING_ASSUMED=false
```

## 3. What does and does not disappear

The projection (4) removes only inner **multiplicity** as a possible square-root obstruction. It does not remove the arithmetic correlation itself:

```text
A_poly(E,m)=1
```

still means that at least one unitary divisor of `m` in the moving short interval simultaneously satisfies every complementary-E, canonical, reverse, root-origin, parity and charged physical condition.

Polynomial motion in `E` therefore remains genuine. The outer support now lives on a two-variable hyperbolic family `(E,m)` with `n=E*m`, rather than on a scalar `m` alone.

```text
POLYNOMIAL_E_ARITHMETIC_CORRELATION_REMOVED=false
INNER_MULTIPLICITY_AS_POLYNOMIAL_SOURCE_REMOVED=true
OUTER_PAIR_E_M_REMAINS_GENUINE=true
```

## 4. Heavy-mass implication

If this branch carries exponent `mu`,

```text
I_poly >= B^(mu-o(1)),
```

then

```text
#{(E,m): A_poly(E,m)=1}
 >= B^(mu-o(1)).                                   (5)
```

Thus any future saving must prove a fixed-power deficit for the outer-pair support itself, not a pointwise bound on the number of unitary divisors.

## H decision

No new H is opened at this step. A theorem target must distinguish the scalar fixed-E support problem from the polynomial two-outer-variable correlation. Ford-type unrestricted one-variable divisor results do not directly control (5).

```text
Q14_FORD_DIRECT_ON_POLYNOMIAL_E_BRANCH=false
NEW_HEAVY_MAIN_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-4fp
```
