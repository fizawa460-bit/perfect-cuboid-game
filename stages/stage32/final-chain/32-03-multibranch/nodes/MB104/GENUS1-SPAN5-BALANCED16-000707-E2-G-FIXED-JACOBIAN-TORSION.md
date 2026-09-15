# Stage32 MB104 — `000707000f0f` e=2 exact full-`G` fixed Jacobian torsion

Status: **RETAINED CANDIDATE INTEGRAL-HOMOLOGY REPLAY / `J(C8)^G ~= (Z/2)^5` / 32 FACTOR CLASSES / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding external-product Picard reduction showed conditionally that

```text
O_(C8 x C8)(Zbar) ~= p_1^*A tensor p_2^*B,
A,B in Pic^(28l)(C8)^G,
```

and bounded the difference of two invariant factor classes by 4-torsion.  This note computes the fixed subgroup `J(C8)^G` exactly from the retained six-branch topological passport.  No complex period approximation is used.

## 1. Retained topological passport

The retained `G` action has

```text
G ~= (Z/2)^3,
C8/G ~= P1,
```

with six branch values of order two, two for each of the three singular involutions.  The three singular involutions are independent and generate `G`; after a harmless change of `F_2` basis call them

```text
e1,e2,e3.
```

The orbifold fundamental group of the base therefore has presentation

```text
Gamma = <x1,...,x6 |
         x1^2=...=x6^2=1,
         x1*x2*x3*x4*x5*x6=1>,
```

with monodromy

```text
x1,x2 -> e1,
x3,x4 -> e2,
x5,x6 -> e3.
```

Its kernel `K` is the ordinary surface group `pi_1(C8)`.

## 2. Exact Reidemeister--Schreier abelianization

Use the prefix-closed transversal

```text
t_(a,b,c) = x1^a x3^b x5^c,
(a,b,c) in (Z/2)^3.
```

For every coset `g` and orbifold generator `xi`, form the Schreier generator

```text
S(g,i)=t_g xi t_(g+mon(xi))^(-1).
```

Exactly seven of the 48 formal Schreier generators freely cancel, leaving 41 nontrivial generators.  Rewriting the six involution relators and the product relator in every one of the eight cosets gives 56 integral abelian relations.

A deterministic unit-pivot integer elimination uses only unimodular row/column operations and reduces the `56 x 41` relation matrix to

```text
diag(I_31,0_10).
```

Thus

```text
H_1(C8,Z) ~= Z^10
```

with no torsion, as required for a genus-five curve.  This also supplies an integral basis in which the deck action is replayed exactly.

## 3. Integral deck action sanity check

Conjugating the Schreier generators by lifts of `e1,e2,e3`, then passing through the same unimodular quotient basis, gives three commuting integral involutions on `Z^10`.

Their traces, and the traces of their products, are

```text
trace(1)=10,
trace(e1)=trace(e2)=trace(e3)=-6,
trace(e1e2)=trace(e1e3)=trace(e2e3)=trace(e1e2e3)=2.
```

Dividing by two gives the holomorphic traces

```text
5, -3, -3, -3, +1, +1, +1, +1,
```

which exactly matches the retained fixed-point/Riemann--Hurwitz character data after the above change of `G` basis.  This is an independent consistency check that the integral deck module is the intended one.

## 4. Fixed points of the Jacobian

Topologically

```text
J(C8) = H_1(C8,R) / H_1(C8,Z)
```

with the same deck action.  Let `Q_i` be the three `10 x 10` integral matrices for `e_i`.  A class represented by a column vector `v in R^10` is fixed by all of `G` exactly when

```text
(Q_i-I)^T v in Z^10,   i=1,2,3.
```

Stack these three blocks to form the `30 x 10` integer matrix

```text
B = stack_i (Q_i-I)^T.
```

The verifier performs another deterministic unimodular reduction.  It finds five unit invariant factors.  After removing those rows/columns, every entry of the remaining `25 x 5` block is divisible by two; dividing by two leaves a matrix that unit-reduces to `I_5`.  Therefore the Smith invariants of `B` are exactly

```text
1,1,1,1,1,2,2,2,2,2.
```

Hence

```text
J(C8)^G ~= (Z/2)^5,
|J(C8)^G| = 32.                                  (JFIX)
```

In particular the previous generic exponent-four bound sharpens, for the full-`G` factor classes, to exponent two.

## 5. Consequence for the e=2 external-product factor classes

The preceding leaf constructed an explicit `G`-invariant degree-`28l` reference class for each parity of `l`.  Since the difference of two `G`-fixed degree-`28l` classes lies in `J(C8)^G`, `(JFIX)` gives

```text
|Pic^(28l)(C8)^G| = 32.
```

Therefore the candidate external-product line bundle has only

```text
32 * 32 = 1024
```

ordered invariant factor-class pairs

```text
(A,B).
```

This is independent of `l`.  It replaces the preceding crude `4^20` ambient pair bound by an exact 1024-class finite target.

## Route consequence

A finite exact continuation is now available:

1. enumerate the 32 invariant factor classes as the parity reference class translated by the five binary fixed-Jacobian generators;
2. test the 1024 ordered pairs for compatibility with the retained `000707` support passport, irreducibility, and the degree-`28l` common-etale normalization;
3. if all pairs fail, close this e=2 external-product route; otherwise feed surviving pairs back into the conductor/residual-sheet leaf.

The present note does not yet construct explicit divisor representatives for the five fixed-Jacobian generators, so step 1 is a newly finite target rather than completed enumeration.

## Firewalls

- The calculation uses only the retained six-order-two-branch `G` passport; it does not transfer the historical `(5,5,4)` support counts to `000707`.
- Reordering the six branch values or changing the `F_2` basis of `G` changes the Schreier matrices by integral conjugacy and does not change `(JFIX)`.
- `J(C8)^G ~= (Z/2)^5` is a statement about fixed Jacobian points, not a claim that every one produces an effective factor divisor compatible with the carrier.
- No conductor sign or weighted opposite-sheet bound is computed.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
