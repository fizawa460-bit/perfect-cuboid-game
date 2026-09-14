# Stage32 MB104 — `000707000f0f` e=2 relative-`G` Fourier character refinement

Status: **RETAINED EXACT RELATIVE-G CHARACTER DECOMPOSITION / RESIDUAL CHARACTER PICARD DIRECTION MATERIALIZED / CONDUCTOR TRANSITION STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Keep the retained support

```text
Sigma={P0,P1,P2,P3,P8,P9,P10,P11,P24,P25,P26,P32,P33,P34},
D=7l H-4l sum_(p in Sigma) E_p.
```

For one factor the three singular generators act on the box coordinates as the three independent sign flips

```text
beta1 : b1 -> -b1,
beta2 : b2 -> -b2,
beta3 : b3 -> -b3.
```

Here

```text
beta1 <-> s1=T',
beta2 <-> s2=TT'R,
beta3 <-> s3=T,
```

so the support subgroup is

```text
Hrel=<beta1,beta2>,
```

and the residual character is the quotient character

```text
chi_res(beta1^a beta2^b beta3^c)=c in F2.
```

This note computes the exact orbit of the Picard ray under all eight relative-factor translations and takes the finite Fourier component for `chi_res`.

## 1. Exact eight-support orbit

Write a group element as `(a,b,c)` with `a,b,c in F2`. Exact replay on the retained 48-node model gives

```text
000 : 0,1,2,3,8,9,10,11,24,25,26,32,33,34
001 : 0,1,2,3,8,9,10,11,24,25,27,32,33,35
010 : 0,1,2,3,8,9,10,11,24,26,27,32,33,34
011 : 0,1,2,3,8,9,10,11,25,26,27,32,33,35
100 : 0,1,2,3,8,9,10,11,24,25,26,32,34,35
101 : 0,1,2,3,8,9,10,11,24,25,27,33,34,35
110 : 0,1,2,3,8,9,10,11,24,26,27,32,34,35
111 : 0,1,2,3,8,9,10,11,25,26,27,33,34,35.
```

Relative to `Sigma`, the three nonzero elements of `Hrel` have overlap sizes

```text
|Sigma cap beta1 Sigma|       =13,
|Sigma cap beta2 Sigma|       =13,
|Sigma cap beta1 beta2 Sigma| =12,
```

while every element of the nontrivial residual coset `beta3 Hrel` has overlap exactly

```text
12.
```

Using

```text
D_Sigma.D_Sigma'=(784-32|Sigma cap Sigma'|)l^2,
```

this gives the complete first row of the relative-`G` Gram matrix:

```text
000 : 336 l^2,
100 : 368 l^2,
010 : 368 l^2,
110 : 400 l^2,
001,101,011,111 : 400 l^2.
```

In particular all four residual-coset relative translates have the same exact Picard intersection budget `400l^2`.

## 2. Two exact linear relations

The eight orbit classes span rank exactly `6` in the free lattice generated here by `H,E_0,...,E_47`. The only two independent orbit relations are

```text
D_000-D_010-D_100+D_110=0,                    (R0)
D_001-D_011-D_101+D_111=0.                    (R1)
```

Equivalently each residual-coset layer is an affine parallelogram in the two used-type sign directions.

The two vanishing Fourier modes are the characters

```text
(a,b,c) -> (-1)^(a+b),
(a,b,c) -> (-1)^(a+b+c).
```

No geometric branch allocation is inferred from these class relations.

## 3. Residual-character Fourier component

Use the multiplicative sign representative

```text
varepsilon_res(a,b,c)=(-1)^c.
```

Define the orbit Fourier sum

```text
F_res := sum_(g in Grel) varepsilon_res(g) beta_g(D).
```

The hyperplane terms cancel. Exact exceptional-coordinate collection gives

```text
F_res=8l K_res,                                 (F)
```

where the primitive integral class is

```text
K_res = -E24+E25-E26+E27-E32+E33-E34+E35.      (K)
```

Thus the same finite quotient character that defines the residual `G/H` sheet has a completely explicit one-dimensional Fourier component on the relative-`G` orbit of the active Picard ray.

The exact intersections are

```text
K_res^2=-16,
D.K_res=-16l,
F_res^2=-1024l^2,
D.F_res=-128l^2.                                (NORM)
```

The last equality is also the character-weighted Gram identity

```text
336+368+368+400 -4*400 = -128.
```

## 4. Full Fourier spectrum

For completeness, the eight character eigenvalues of the orbit Gram kernel, ordered by characters `(u,v,w) in F2^3`, are

```text
000 : 3072 l^2,
001 : -128 l^2,   <- residual character
010 :  -64 l^2,
011 :  -64 l^2,
100 :  -64 l^2,
101 :  -64 l^2,
110 :    0,
111 :    0.
```

The two zero eigenvalues are exactly the two class relations `(R0),(R1)` above.

## 5. Consequence for the active conductor leaf

This refinement does **not** identify a conductor pair with an intersection against a relative translate. It therefore does not convert `(F)` into a conductor-sign formula and does not upper-bound the Hodge cut.

What has changed is the finite-group side of the missing adapter. Previously the residual sheet character was explicit only as

```text
G/H -> {+1,-1}.
```

For the exact active Picard orbit it now has a unique explicit Fourier output

```text
chi_res -> K_res
```

with fixed norm and fixed pairing against `D`. Any future branch/conductor-to-relative-translate adapter must therefore land in this already-fixed character channel; it cannot choose an independent Picard anti-character direction.

The remaining load-bearing step is still to prove a semantic map

```text
conductor normalization pair
 -> relative/full modular transition
 -> chi_res,
```

or an equivalent residual square-root comparison. Only after that adapter is source-locked may `(F)` or the `400l^2` residual-coset budgets be used quantitatively on the weighted conductor cut.

## Firewalls

- `K_res` is a Picard-orbit Fourier class, not the ambient half-branch class `L_abs`.
- No equality between `K_res` and the residual Kummer divisor is asserted.
- No conductor pair is assigned a relative translate.
- No conductor sign is assigned.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
