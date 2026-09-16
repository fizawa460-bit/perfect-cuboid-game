# Stage32 MB104 — `000707000f0f` e=2 determinant `G`-linearization bridge

Status: **RETAINED CANDIDATE EQUIVARIANT-PICARD BRIDGE / ETALE DETERMINANT LINES LIE IN THE FOUR-CLASS LINEARIZABLE FIXED-JACOBIAN KERNEL / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the retained e=2 etale base-change passport for

```text
f_i:Z -> C8,
epsilon_i := det((f_i)_* O_Z) in J(C8)[2],
i=1,2,
```

and the retained equivariant-Picard refinement

```text
Ker(obs_G | J(C8)^G) ~= (Z/2)^2,
|Ker(obs_G | J(C8)^G)|=4,
G ~= (Z/2)^3.
```

The passport already proves

```text
T^* epsilon_i ~= epsilon_i
```

for the residual involution `T`, but invariance of a line-bundle class does not by itself imply a `G`-linearization. This note checks the missing compatibility with the canonical `H`-linearization and proves that the determinant lines actually lie in the four-class linearizable kernel.

## 1. Canonical `H`-linearization of the determinant line

The component stabilizer in the e=2 case is

```text
H=<T',TT'R> ~= (Z/2)^2.
```

Each projection `f_i` is `H`-equivariant. Therefore `(f_i)_*O_Z` carries its canonical `H`-equivariant vector-bundle structure, and taking determinant gives a canonical `H`-linearization on

```text
epsilon_i=det((f_i)_*O_Z).
```

The only possible obstruction to extending this to full `G=<H,T>` is the commutator between a chosen `T`-isomorphism and the two `H` generators.

## 2. Normalize a `T`-isomorphism

The retained passport proves

```text
T^*epsilon_i ~= epsilon_i.                       (TINV)
```

Choose an isomorphism

```text
phi:T^*epsilon_i -> epsilon_i.
```

Because `T^2=1`, the composite

```text
phi o T^*phi
```

is a nonzero scalar automorphism of `epsilon_i`. Over `C`, rescale `phi` by a square root of that scalar so that

```text
phi o T^*phi = id.                               (T2)
```

Thus only commutation with `H` remains.

## 3. Determinant fibre character at an `H`-fixed point

Fix one generator

```text
h in {T',TT'R}.
```

Let `q` be one of the four branch values of the quotient

```text
C8 -> R=C8/H
```

whose inertia is `<h>`. Choose an `h`-fixed point `x in C8` above `q`.

For the corresponding degree-`n` map

```text
psi_i:E->R,
n=28l,
```

write

```text
nu_q + 2 r_q = n,
```

where `nu_q` is the number of unramified points and `r_q` the number of simple ramification points over `q`.

The base-change local models are exact:

- an unramified point gives `u^2=v`, hence one `h`-fixed sheet over `x`;
- a simple ramification point gives `u^2=v^2`, whose two normalized branches are exchanged by `h`.

Therefore the permutation of the fibre `f_i^{-1}(x)` induced by `h` has exactly `r_q` transpositions. The canonical determinant linearization acts on the one-dimensional fibre `(epsilon_i)_x` by

```text
chi_x(h)=(-1)^(r_q).                             (FIBRE-SIGN)
```

This is the same sign bit denoted `b_q` in the retained etale-basechange passport.

## 4. Residual pairing kills the commutator

The residual element `T` commutes with `h` and sends the branch value `q` to `-q`. Hence `Tx` is an `h`-fixed point above `-q`.

The retained passport proves for every residual pair

```text
b_q=b_-q,
```

i.e.

```text
r_q == r_-q mod 2.                              (PAIR-SIGN)
```

By `(FIBRE-SIGN)`, the canonical `H`-characters on the two determinant fibres agree:

```text
chi_x(h)=chi_(Tx)(h).                            (FIBRE-EQ)
```

Now compare the two maps from `(T^*epsilon_i)_x=(epsilon_i)_(Tx)` to `(epsilon_i)_x` obtained by applying `h` before or after `phi`. Since both source and target are one-dimensional, their ratio is the scalar commutator `c_h`. Evaluating at `x` and using `(FIBRE-EQ)` gives

```text
c_h=1.
```

This holds for both generators of `H`. Thus the normalized `T`-isomorphism commutes with the canonical `H`-linearization.

Consequently

```text
epsilon_i is G-linearizable.                    (G-LIN)
```

## 5. Exact finite consequence

The retained diagonal-`G` linearization obstruction leaf computed

```text
Ker(obs_G | J(C8)^G)
 = <lambda_1,lambda_2>
 ~= (Z/2)^2,
```

where one may take

```text
lambda_1=O(R1-R3),
lambda_2=O(R1-R5)
```

for suitably ordered reduced full-`G` ramification-orbit divisors.

By `(G-LIN)`, each determinant line satisfies

```text
epsilon_i in Ker(obs_G | J(C8)^G)
```

and therefore

```text
epsilon_i in {O,lambda_1,lambda_2,lambda_1 tensor lambda_2}.   (DET-KER4)
```

This identifies the earlier `at most four` determinant ambiguity with the **same algebraic four-class linearizable fixed-Jacobian kernel** that controls the relative external-product factor class.

The e=2 determinant passport sharpens this further factorwise:

```text
d_-(f1)=0,
d_+(f1)=((x0+x1+x2+x3+x24+x25+x26)/2) mod 2,

d_+(f2)=0,
d_-(f2)=((x8-x9+x10-x11-x32+x33-x34)/2) mod 2.
```

Thus each factor determinant moves on at most one binary line inside `(DET-KER4)`. This note does not choose an unproved identification of those two passport bit axes with the retained `lambda_1,lambda_2` basis.

## 6. What this does and does not solve

This bridge removes one semantic ambiguity:

```text
T-invariant determinant class
```

is strengthened to

```text
full-G-linearizable determinant class.
```

Hence future determinant/conductor calculations may work inside the exact invariant-divisor subgroup `<lambda_1,lambda_2>` rather than the full five-bit fixed Jacobian.

It does **not** identify the determinant line with the pointwise residual `G/H` conductor character. The retained passport already shows that determinant sign monodromy loses information: its residual discrepancy is zero while the singular-curve conductor gluing character may remain nontrivial.

## Source locks / inherited boundaries

- `GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT.md` — local base-change passport, determinant sign, and `b_q=b_-q`.
- `GENUS1-SPAN5-BALANCED16-000707-E2-DIAGONAL-G-LINEARIZATION-OBSTRUCTION.md` — exact four-class linearizable kernel.
- `EQUIVARIANT-PICARD-LINEARIZATION-SOURCE-NOTE.md` — invariant versus linearized Picard obstruction.

## Firewalls

- No individual conductor pair is assigned the class `0` or `gamma_Q`.
- No equality between `epsilon_i` and the singular-carrier gluing class `kappa` is asserted.
- No equality between the factor-1 and factor-2 determinant bits is asserted.
- No weighted-cut upper bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
