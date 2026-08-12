# Stage14-4gg — seedless reciprocal witnesses normalize to a K-free moving divisor-allocation CRT system

## Status

`COMPLETE_SEEDLESS_RECIPROCAL_WITNESS_KFREE_MOVING_DIVISOR_ALLOCATION_NORMAL_FORM`

Consumes batch-local `Stage14-4gf`, merged `Stage14-4gd/4ge`, and merged `Stage14-Work-bzX38/q17`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze all coefficient primes once

On the fixed packet retain the notation

```text
A_x=H0*x,
A_y=H0*y,
C0=4*r*s*epsilon_k,
```

and let `K_*` be the product of every nonzero frozen integer coefficient occurring in the bare reciprocal system, in particular

```text
2*A_x*A_y*C0*U*V
```

and the frozen endpoint/two-primary integer decorations. Repetition of prime powers in `K_*` is irrelevant; only its prime support is used.

For a positive integer `z`, define

```text
z_K := product over ell|K_* of ell^(v_ell(z)),
z^circ := z/z_K.
```

Thus `z^circ` is coprime to `K_*`. Put

```text
m=u*v,
m^circ=(u*v)^circ.
```

This is an exact prime-support split, not a smooth/rough density estimate.

## 2. First reciprocal divisor layer becomes two divisors of m^circ

For any `omega in Omega_rec(u,v)`, merged 4gd has

```text
p*c=A_x*m,
q*d=A_y*m.
```

Because every prime of `A_x*A_y` belongs to `K_*`, taking the `K_*`-coprime parts gives exactly

```text
p^circ*c^circ=m^circ,
q^circ*d^circ=m^circ.                              (1)
```

Hence

```text
t_p:=p^circ | m^circ,
t_q:=q^circ | m^circ,
c^circ=m^circ/t_p,
d^circ=m^circ/t_q.                                 (2)
```

All allocation of primes outside the frozen coefficient support is therefore carried by the two divisor variables `(t_p,t_q)` of the single moving integer `m^circ`.

```text
FIRST_LAYER_KFREE_MOVING_DIVISORS_EXACT=true
```

## 3. Second factor layer is a divisor allocation of t_p t_q

Write

```text
F_-=G_-*f_-,
F_+=G_+*f_+,
```

where `f_-=F_-^circ`, `f_+=F_+^circ` and `G_-,G_+` contain only primes supported on `K_*`.

Since

```text
F_-*F_+=C0*p*q
```

and `C0` is `K_*`-supported, taking coprime parts yields

```text
f_-*f_+=t_p*t_q.                                   (3)
```

Thus, after the first-layer choices, the moving part of the second factorization is just one ordered factorization of `t_p*t_q`.

The exact CRT conditions remain

```text
G_+*f_+ + G_-*f_- == 0 (mod 2U),
G_+*f_+ - G_-*f_- == 0 (mod 2V).                   (4)
```

Because every prime of `f_-f_+` is outside `K_*`, the moving factors are units modulo every odd prime of `UV`; no modulus or density factor is silently discarded. The `K_*`-supported cores `G_-,G_+` retain all valuations at coefficient primes, including those contributed by the `K_*`-part of `m`.

```text
SECOND_LAYER_KFREE_FACTOR_ALLOCATION_EXACT=true
FIXED_UV_CRT_PRESERVED_EXACTLY=true
```

## 4. Core labels cost no new fixed-power entropy

For a fixed primitive pair `(u,v)`, merged 4gd already proves

```text
#Omega_rec(u,v)=B^o(1).
```

Therefore all choices of

```text
K_*-supported parts of p,q,c,d,F_-,F_+,
finite parity/orientation labels,
endpoint-small divisibility labels
```

combined are `B^o(1)` per pair. The present normalization does not promote any one of them to a new polynomial outer variable.

Conversely, once one such core label and the moving tuple

```text
(t_p,t_q,f_-,f_+)
```

are fixed subject to (2)--(4), the full bare reciprocal witness is determined up to the already-bounded `B^o(1)` candidate multiplicity.

```text
K_SUPPORTED_CORE_RECHARGE_FORBIDDEN=true
KFREE_MOVING_ALLOCATION_CARRIES_ALL_NEW_RECIPROCAL_SUPPORT_ARITHMETIC=true
```

## 5. Relation to the homogeneous seed

The homogeneous seed of 4gf is the diagonal moving allocation in which, after the same coefficient-prime peel,

```text
t_p=t_q=m^circ,
f_-=f_+=m^circ
```

with compatible `K_*`-supported cores. Hence 4gf is not a separate arithmetic species; it is the easiest full-density diagonal inside the exact K-free allocation system.

If that diagonal seed is absent, all remaining reciprocal support must be produced by nontrivial divisor allocations satisfying (2)--(4). No sparsity is inferred merely from being off the diagonal.

```text
HOMOGENEOUS_SEED_IS_DIAGONAL_KFREE_ALLOCATION=true
SEEDLESS_REMAINDER_IS_NONTRIVIAL_KFREE_DIVISOR_ALLOCATION_CRT=true
```

## 6. Next obligation

The q17 radar proposed a first/second-moment support transfer for the witness count. The exact K-free normal form now makes it possible to decide the logical amount of moment information actually required, using the already-proved `B^o(1)` witness multiplicity rather than importing a stronger second-moment theorem by default.

No new H is opened in this stage; the moment/support reduction is still an internal counting lemma.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4gh
```

## Boundary

```text
STAGE14_4GG=COMPLETE_SEEDLESS_RECIPROCAL_WITNESS_KFREE_MOVING_DIVISOR_ALLOCATION_NORMAL_FORM
FIRST_LAYER_KFREE_MOVING_DIVISORS_EXACT=true
SECOND_LAYER_KFREE_FACTOR_ALLOCATION_EXACT=true
FIXED_UV_CRT_PRESERVED_EXACTLY=true
K_SUPPORTED_CORE_RECHARGE_FORBIDDEN=true
HOMOGENEOUS_SEED_IS_DIAGONAL_KFREE_ALLOCATION=true
SEEDLESS_REMAINDER_IS_NONTRIVIAL_KFREE_DIVISOR_ALLOCATION_CRT=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gh
```