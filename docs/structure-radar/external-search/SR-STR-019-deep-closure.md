# SR-STR-019 deep closure attempt

Date: 2026-08-19
Status: `FIRST_MISSING_LEMMA_IDENTIFIED`
Arsenal decision: unchanged (`EXTERNAL_GATE`).

## Closed reduction

The two frozen quadratic congruences can be combined exactly by generalized CRT. With

```text
N=t_p t_q,
h=gcd(U,V),
q=lcm(2U,2V)=2UV/h,
```

local compatibility reduces on the inherited coprime moving stratum to the frozen condition `h|G_+`; otherwise the cell contributes zero. On surviving cells the pair is equivalent to one exact congruence

```text
f^2 = G_- + lambda_h N (mod q).
```

This is an exact encoding of both original root conditions, not a one-root simplification.

The nested divisor structure can also be separated exactly using `gcd(u,v)=1`:

```text
t_p=a_p b_p,
t_q=a_q b_q,
a_p,a_q|u^circ,
b_p,b_q|v^circ,
A=a_p a_q,
B=b_p b_q,
f=r s,
r|A,
s|B.
```

A nonzero additive Fourier mode therefore becomes

```text
E_a =
sum_{u,v}
sum_{a_p,a_q|u^circ}
sum_{b_p,b_q|v^circ}
sum_{r|A}
sum_{s|B}
W_C(...) e_q(a[r^2 s^2-lambda_h A B]).
```

After exact packet compression the core is an individual-modulus bilinear incidence

```text
sum_X alpha_X sum_Y beta_Y 1_{X dot Y = G_- (mod q)},
```

where `alpha_X,beta_Y` retain common-parent divisor multiplicities.

Standard complete-sum/Weil/spectral machinery gives an error of schematic size

```text
q^(1/2+o(1)) ||alpha||_2 ||beta||_2,
```

so the problem is no longer the CRT/root geometry but the pointwise energy of the common-parent packet coefficients.

## First missing lemma

```text
FIRST_MISSING_LEMMA=IndividualCellCommonParentNestedDivisorBilinearIncidenceEstimate
```

For one hard exponent-full packet, a sufficient fixed-power deficit condition is a pointwise energy bound equivalent to

```text
e_L+e_R <= 2(lambda_L+lambda_R)-gamma-2eta,
```

where `q=B^(gamma+o(1))`, `||alpha||_1=B^(lambda_L+o(1))`, `||beta||_1=B^(lambda_R+o(1))`, and `||alpha||_2^2=B^(e_L+o(1))`, `||beta||_2^2=B^(e_R+o(1))`.

No frozen input supplies this every-cell energy saving. Averaged modulus/cell estimates are unusable because the receiver quantifier freezes exactly the potentially exceptional high-energy cell.

```text
CRT_NORMALIZATION=PROVED
NESTED_DIVISOR_MULTILINEARIZATION=PROVED
COMMON_PARENT_POINTWISE_ENERGY_BOUND=OPEN
AVERAGE_MODULUS_SUBSTITUTION_FORBIDDEN=true
SR_STR_019_STATUS=EXTERNAL_GATE
ADAPTER_CLOSURE_VERDICT=FIRST_MISSING_LEMMA_IDENTIFIED
```
