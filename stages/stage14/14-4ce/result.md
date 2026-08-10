# Stage14-4ce — dual allocation injectivity and double-disagreement switch packet

## Status

`COMPLETE_DUAL_ALLOCATION_INJECTIVITY_AND_DOUBLE_DISAGREEMENT_REDUCTION`

Merged 4cd localizes any block that can still saturate `7/8` to

```text
P,Q,Q-P,Q+P=B^(1/2+o(1)),
xi=ker(PQ)=B^(3/4+o(1)),
k=ker(Q^2-P^2)=B^(1+o(1)).
```

Merged s7-18 proves the difference-kernel allocation theorem: same `k_- / k_+` split is injective in the critical region, and every remaining 4cd-endpoint collision has

```text
K_switch >= B^(3/8-o(1)).
```

4ce proves the exact dual theorem for the product-kernel allocation `xi=a*b`, then combines both sides. No 14-4 H line is created and no unproved t/tH selector theorem is imported.

## 1. Xi-side quartic

For a reduced coordinate `0<P<Q<=X`, write

```text
P=a*x^2,
Q=b*y^2,
xi=a*b=ker(PQ),
Q^2-P^2=k*h^2,
```

with `a,b,k` squarefree. Reducedness gives

```text
gcd(a,b)=gcd(x,y)=1,
gcd(xi,k*h)=1.
```

The exact quartic is

```text
b^2*y^4-a^2*x^4=k*h^2.                             (1.1)
```

and

```text
x^2<=X/a,
y^2<=X/b,
h^2<=X^2/k.                                         (1.2)
```

## 2. Fixed xi split is injective

For two states with the same `xi,k,a,b`, cross multiplication gives

```text
b^2(y1^4*h2^2-y2^4*h1^2)
 =a^2(x1^4*h2^2-x2^4*h1^2).
```

Hence `a^2` divides the first bracket and `b^2` the second. Their absolute values are at most

```text
2X^4/(b^2*k),
2X^4/(a^2*k).
```

Therefore

```text
boxed: xi^2*k>2X^4                                  (2.1)
```

forces both brackets to vanish. Positivity gives `x1/y1=x2/y2`; primitivity gives equality of the roots and hence of `(P,Q)`.

Thus

```text
XiFixedSplitInjectivity:
xi^2*k>2X^4 => at most one state for a fixed xi=a*b split and fixed k.
```

On the old critical shell `xi~B^(3/4)`, `k>=B^(3/4-o(1))`, `X<=B^(1/2+o(1))`, the exponent margin is `1/4`.

## 3. Cross-split xi collision

For two different allocations of the same squarefree `xi`, write uniquely

```text
a1=A*B, b1=C*D,
a2=A*C, b2=B*D,
A*B*C*D=xi,
```

with pairwise-coprime squarefree cells. Put

```text
Xi_agree=A*D,
Xi_switch=B*C=xi/Xi_agree.
```

Cross multiplication gives

```text
D^2(C^2*y1^4*h2^2-B^2*y2^4*h1^2)
 =A^2(B^2*x1^4*h2^2-C^2*x2^4*h1^2).
```

Thus `A^2` divides the first bracket and `D^2` the second, with sizes at most

```text
2X^4/(D^2*k),
2X^4/(A^2*k).
```

If `(A*D)^2*k>2X^4`, both brackets vanish. A prime divisor of `B` or `C` then contradicts `gcd(xi,k*h)=1`; hence `B=C=1`, the splits coincide, and Section 2 forces equality.

Therefore every off-diagonal same-`(xi,k)` collision satisfies

```text
boxed: (Xi_agree)^2*k <= 2X^4.                     (3.1)
```

Equivalently

```text
boxed: Xi_switch >= xi*sqrt(k)/(sqrt(2)*X^2).       (3.2)
```

At exponent scale `xi~B^gamma`, `k~B^kappa`, `X<=B^(1/2+o(1))`,

```text
log_B Xi_switch >= gamma+kappa/2-1-o(1).           (3.3)
```

Hence

```text
old 7/8 residual: gamma=3/4, kappa>=3/4
=> Xi_switch>=B^(1/8-o(1));

4cd endpoint: gamma=3/4, kappa=1
=> Xi_switch>=B^(1/4-o(1)).                         (3.4)
```

## 4. Double disagreement after merged s7-18

Merged s7-18 gives

```text
K_switch >= k*sqrt(xi)/(sqrt(32)*X^2).
```

Thus every 4cd-endpoint off-diagonal collision satisfies simultaneously

```text
boxed:
Xi_switch>=B^(1/4-o(1)),
K_switch >=B^(3/8-o(1)),
Xi_switch*K_switch>=B^(5/8-o(1)).                  (4.1)
```

This is the canonical `DoubleDisagreementSwitchPacket`.

## 5. Switching primes are Gaussian-split

Merged 4cd gives for every odd prime `ell`

```text
ell|a   => ( k/ell)=+1,
ell|b   => (-k/ell)=+1,
ell|k_- => ( xi/ell)=+1,
ell|k_+ => (-xi/ell)=+1.                            (5.1)
```

If an odd `ell` lies in an xi-switch cell, it is in `a` for one state and `b` for the other. Hence both `(k/ell)=1` and `(-k/ell)=1`, so

```text
boxed: ell == 1 (mod 4).                            (5.2)
```

Likewise an odd prime switching between `k_-` and `k_+` satisfies both `(xi/ell)=1` and `(-xi/ell)=1`, hence

```text
boxed: ell == 1 (mod 4).                            (5.3)
```

Thus every odd `3 mod 4` prime is allocation-frozen throughout a same-`(xi,k)` collision fiber. The statewise coupled residue graph is

```text
ell|Xi_switch => (k/ell)=+1,
p|K_switch    => (xi/p)=+1.                         (5.4)
```

This is exact and is not treated as independent local half-density.

## 6. Boundary

Large switching divisors and `1 mod 4` support do not alone give a fixed power because divisor allocation counts are `2^omega(.)=B^o(1)` and the split-prime support restriction is only logarithmic at this level.

Therefore

```text
boxed: V(B)<<B^(7/8+o(1)).
```

remains current.

The next receiver is

```text
CoupledDoubleSwitchQuadraticResidueIncidence
```

retaining `Xi_agree, Xi_switch, K_agree, K_switch, xi, k` and the physical masks. Forbidden shortcuts are multiplying local residue densities, claiming fixed-power sparsity from `1 mod 4`, or collapsing to raw `(xi,k)` before both switch products are used.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

The t-route tH15/t55 results are independent references and are not prerequisites for 14-4ce/4cf.

## 7. Stage boundary

```text
STAGE14_4CE=COMPLETE_DUAL_ALLOCATION_INJECTIVITY_AND_DOUBLE_DISAGREEMENT_REDUCTION
MERGED_4CD_IMPORTED=true
MERGED_S7_18_IMPORTED=true
XI_FIXED_SPLIT_INJECTIVE_IF_xi2_k_GT_2_X4=true
XI_CROSS_SPLIT_AGREEMENT_NECESSARY_BOUND=(Xi_agree)^2*k<=2*X^4
XI_SWITCH_LOWER_BOUND=xi*sqrt(k)/(sqrt(2)*X^2)
OLD_CRITICAL_XI_SWITCH_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4
FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8
FOUR_CD_ENDPOINT_DOUBLE_SWITCH_PRODUCT_LOWER_EXPONENT=5/8
ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true
ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true
INERT_3_MOD_4_ALLOCATION_FROZEN=true
COUPLED_SWITCH_PRIME_RESIDUE_GRAPH_EXACT=true
COUPLED_DOUBLE_SWITCH_QUADRATIC_RESIDUE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cf
```
