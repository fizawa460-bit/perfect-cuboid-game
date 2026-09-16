# Stage32 MB104 — `000707000f0f` e=2 conductor-determinant reduction

Status: **RETAINED CANDIDATE GLOBAL CONDUCTOR CLASS / FACTOR 2-TORSION TWISTS CANCEL / H-FIXED DETERMINANT GROUP OF SIZE 64 / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Consume the retained candidate external-product consequence

```text
P=C8 x C8,
O_P(Zbar) ~= p_1^*A tensor p_2^*B,
deg A=deg B=n=28l,
```

where the normalization

```text
nu:Z -> Zbar
```

has two degree-`n` etale projections

```text
f_1,f_2:Z->C8.
```

The retained product-image defect is

```text
delta(Zbar)=784l^2+112l=n(n+4).
```

This note computes the line-bundle class of the conductor pushed to either factor. It does not identify individual Stage32 conductor pairs.

## 1. Determinant of the singular product family

Write `C=C8`, `g(C)=5`, and let

```text
pi_1:Zbar -> C
```

be the first projection. Since `Zbar` is irreducible and has positive degree over both factors, it contains no vertical fibre, so `pi_1` is finite flat of degree `n`.

The divisor exact sequence is

```text
0 -> p_1^*A^(-1) tensor p_2^*B^(-1)
  -> O_(C x C)
  -> O_Zbar
  -> 0.
```

Because `deg B=n>0`,

```text
H^0(C,B^(-1))=0,
h^1(C,B^(-1))=h^0(C,K_C tensor B)=n+4,
h^1(C,O_C)=5.
```

Pushing the sequence by `p_1` and using that `pi_1` is finite gives the determinant identity

```text
det(pi_1* O_Zbar) ~= A^(-(n+4)).              (DET-SING)
```

The same argument with the two factors exchanged gives

```text
det(pi_2* O_Zbar) ~= B^(-(n+4)).
```

## 2. Normalize and isolate the half-discriminant divisor

Let

```text
Q = nu_*O_Z / O_Zbar.
```

Push to the first factor. It is a torsion sheaf; define the effective divisor

```text
F_1 = sum_(x in C) length(Q_x) [x].
```

Then

```text
deg F_1 = length(Q)=delta(Zbar)=n(n+4).
```

From

```text
0 -> pi_1*O_Zbar -> f_1*O_Z -> (pi_1)_*Q -> 0
```

we get

```text
det(f_1*O_Z)
 ~= det(pi_1*O_Zbar) tensor O_C(F_1).
```

Hence

```text
O_C(F_1)
 ~= A^(n+4) tensor epsilon_1,                  (F1)

epsilon_1 := det(f_1*O_Z).
```

Likewise

```text
O_C(F_2)
 ~= B^(n+4) tensor epsilon_2,
epsilon_2 := det(f_2*O_Z).                     (F2)
```

The divisors `F_i` are the factorwise half-discriminant/conductor pushforwards. Their degree agrees exactly with the retained normalization defect.

## 3. The determinant correction is 2-torsion

Each `f_i` is finite etale. The trace pairing

```text
f_i*O_Z x f_i*O_Z -> O_C
```

is everywhere nondegenerate, so

```text
f_i*O_Z ~= (f_i*O_Z)^*.
```

Taking determinants gives

```text
epsilon_i^2 ~= O_C.                            (SIGN)
```

Thus `epsilon_i` is exactly the sign/determinant local system of the degree-`n` etale cover.

## 4. The 32 full-G factor twists disappear completely

The preceding fixed-Jacobian leaf writes every invariant factor class as

```text
A=A_ref(l) tensor tau,
tau in J(C)^G[2],
```

with 32 choices for `tau`. But

```text
n+4=28l+4=4(7l+1)
```

is even. Therefore

```text
tau^(n+4) ~= O_C,
```

and `(F1)` becomes

```text
O_C(F_1)
 ~= A_ref(l)^(n+4) tensor epsilon_1.            (F1-RED)
```

The half-discriminant class is independent of all 32 full-`G` factor-Picard labels. The same holds for `F_2`.

Hence the earlier 1024 ordered factor-class labels do **not** need to be enumerated for this conductor-class invariant.

## 5. Exact size of the H-fixed determinant ambiguity

In the active e=2 component the stabilizer is

```text
H=<s1,s2> ~= (Z/2)^2.
```

The cover `f_i:Z->C` is `H`-equivariant, so

```text
h^*(f_i*O_Z) ~= f_i*O_Z
```

for `h in H`. Therefore

```text
epsilon_i in J(C)[2]^H.
```

Use the same exact integral homology module as the retained full-`G` fixed-Jacobian calculation. Stack only the two matrices `(s1-I)^T,(s2-I)^T`. Deterministic integral reduction gives Smith invariants

```text
1,1,1,1,2,2,2,2,2,2.
```

Thus

```text
J(C8)^H ~= (Z/2)^6,
|J(C8)^H|=64.                                   (HFIX)
```

This sharpens the earlier generic exponent-four bound for this exact modular action.

Consequently the factorwise half-discriminant class has at most 64 determinant possibilities:

```text
O_C(F_i)
 in A_ref(l)^(n+4) tensor J(C8)^H[2].
```

## 6. Discriminant saturation check

The discriminant hypersurface for degree-`n` divisors on a genus-five curve has degree

```text
2n+2g-2 = 2n+8.
```

The family cut out by `Zbar` has parameter line bundle `A`, so its discriminant divisor has degree

```text
n(2n+8)=2n(n+4)=2 delta(Zbar).
```

This is exactly twice the conductor length because the normalization cover `f_1` is etale and contributes no ramification discriminant. Thus the numerical discriminant budget is fully saturated by conductor collision; `(F1)` is the corresponding integral line-bundle refinement.

## Route consequence

The product-correspondence continuation has now reduced the global conductor class from 32 factor-Picard possibilities per side to a 64-element determinant-sign ambiguity per projection. A useful next target is to identify `epsilon_1,epsilon_2` from the exact etale-cover monodromy or to compare `(F1-RED)/(F2-RED)` with the retained `000707` conductor support and residual `G/H` character.

This does not yet map a normalization preimage to its `R=C8/H` sheet. It is a global conductor-class constraint that may be consumed only through a separately proved adapter to the active conductor-pair variables.

## Firewalls

- `F_i` is the product-image normalization conductor pushed to a factor; it is not silently identified with the downstairs cuboid carrier conductor.
- No individual conductor pair receives a residual `G/H` sign.
- No claim that the determinant 2-torsion class is trivial.
- No claim that all 64 determinant possibilities occur.
- No weighted opposite-sheet bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
