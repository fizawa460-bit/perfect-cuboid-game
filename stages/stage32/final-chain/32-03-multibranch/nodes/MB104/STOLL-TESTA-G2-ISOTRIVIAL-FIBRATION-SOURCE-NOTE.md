# Stage32 MB104 source note — Stoll--Testa `G2` isotrivial fibrations

Status: **PUBLISHED SOURCE ADAPTER / G2 HALF-FIBER INPUT / NO CLOSURE / NO CREDIT**

## Source

Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, especially Definition 6, Proposition 7, Theorem 8, and Section 5 (fibrations in curves of genus five).  The version consulted is the authors' PDF `Cuboidi.pdf`; the Picard/fibration statements used below also appear in the published/article record.

Only the following facts are imported.

## 1. Picard group and the `G2` curves

For the minimal desingularization `S` of the cuboid surface, Stoll--Testa prove

```text
Pic(S) is a free abelian group of rank 64.
```

Their set `G2` consists of the twelve strict transforms of genus-one curves contained in

```text
b1=0, b2=0, b3=0.
```

Each such genus-one curve has self-intersection `-4` on `S`.

This source fact is used only as identity/background here; the downstream residual-character leaf does **not** infer that a restriction of a non-torsion surface class to a carrier is trivial merely because `Pic(S)` is torsion-free.

## 2. The two product-induced isotrivial genus-five fibrations

The first rank-four quadric in the Stoll--Testa fibration construction is the canonical quadric

```text
a1^2+a2^2+a3^2=c^2.
```

Over the splitting field it gives two complementary fibrations of the cuboid surface in genus-five curves.  These are the two isotrivial fibrations induced by the two projections of the product modular model.

For either one, Stoll--Testa state that there are exactly six bad fibers.  Each bad fiber consists, on the singular canonical model, of one `G2` genus-one curve taken with multiplicity two.  Across the two complementary fibrations, each of the twelve `G2` curves occurs exactly once in this way.

One displayed factor parameter is

```text
t=(c+a1)/(a2+i*a3)=(a2-i*a3)/(c-a1),
```

with bad values

```text
0, infinity, +1, -1, +i, -i.
```

## 3. Resolution correction at an A1 node

The paper's `G2` bad-fiber sentence is stated on the singular canonical model.  For Stage32 we use its pullback to the minimal resolution.

At a box node lying on a `G2` component `Q`, the singularity is A1 and the doubled Weil branch `2*Qbar` is Cartier.  If `E_p` is the exceptional `(-2)`-curve and `Q` is the strict transform, the Cartier pullback is locally

```text
2*Q + E_p.
```

Indeed `Q.E_p=1`, so `(2Q+E_p).E_p=2-2=0`, as required for the pullback of a Cartier divisor; this is the standard A1 local resolution calculation.

Every `G2` curve contains eight box nodes.  Therefore a bad fiber with reduced `G2` component `Q` has divisor on `S`

```text
F_Q = 2*Q + sum_(p in T_Q) E_p,
|T_Q|=8.
```

The numerical checks are

```text
F_Q^2 = 4*(-4) + 4*8 - 2*8 = 0,
K_S.F_Q = 2*(K_S.Q)=8,
```

consistent with a genus-five fiber.

## 4. Difference of two half-fibers in one fibration

If `Q_a,Q_b` are two bad reduced `G2` components in the same isotrivial fibration, their full fibers are linearly equivalent. Hence

```text
2*(Q_a-Q_b)
  ~ sum_(p in T_b) E_p - sum_(p in T_a) E_p.
```

This is the exact surface-Picard form of the residual half-fiber relation used downstream.

It does **not** say `Q_a-Q_b` is torsion in `Pic(S)`: the exceptional correction is load-bearing.  Thus torsion-freeness of `Pic(S)` alone does not close the `e=4` case.

## Firewalls

- No carrier existence or nonexistence is asserted.
- No claim that the half-fiber difference is zero in `Pic(S)`.
- No claim that its restriction to every curve is trivial.
- No receiver/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
