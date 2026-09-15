# Stage32 MB104 source note — quotient resolution torsion exponent

Status: **EXTERNAL/STANDARD SOURCE ADAPTER / EXPONENT-FOUR BOUND ONLY / NO CONDUCTOR SIGN / NO CREDIT**

## Scope

This note records the standard descent and Picard facts used to refine the active `000707`, `e=2` torsion ambiguity. It does not assert that the relevant torsion class is trivial and does not evaluate a conductor transition.

## 1. Descent from a rational-singularity resolution

Let

```text
rho : Xtilde -> X
```

be a resolution of a complex variety with rational singularities. Bridgeland--King--Reid, Lemma 3.2, states that a line bundle `L` on `Xtilde` is pulled back from a line bundle on `X` if and only if its restriction to every formal fibre of `rho` is trivial; in that case the descended bundle is `rho_*L`.

Reference:

- T. Bridgeland, A. King, M. Reid, *The McKay correspondence as an equivalence of derived categories*, J. Amer. Math. Soc. 14 (2001), Lemma 3.2, DOI `10.1090/S0894-0347-01-00368-X`.
- Stacks Project, Resolution of Surfaces, Section 54.9 (`0B4V`) for rational surface singularities.

For an `A1` surface singularity the reduced exceptional fibre of the minimal resolution is one `P1`. Its Picard group is `Z`, hence has no finite torsion. For the successive infinitesimal thickenings, the kernels of restriction on Picard groups are controlled by the multiplicative filtration `1+I^n/I^(n+1)`; in characteristic zero these successive kernels are additive complex vector spaces and have no finite torsion. Therefore the Picard group of the formal `A1` fibre has no nonzero finite torsion.

Consequently a torsion line bundle on the resolution restricts trivially to every formal `A1` fibre and descends to the singular surface.

## 2. Torsion on a product of curves lies in `Pic^0`

For

```text
P=C8 x C8
```

the integral cohomology group `H^2(P,Z)` is torsion-free by the Kunneth theorem because the integral cohomology of a compact Riemann surface is torsion-free. The exponential sequence therefore shows that every torsion line bundle on `P` lies in

```text
Pic^0(P)=J(C8) x J(C8).
```

## 3. Norm-zero on the `H`-fixed Picard variety

Let

```text
H ~= (Z/2)^2
```

act diagonally on `P`, and assume

```text
H^1(P,O_P)^H=0.
```

The identity component of the fixed subgroup `Pic^0(P)^H` has tangent space `H^1(P,O_P)^H`, hence is zero-dimensional. The group endomorphism

```text
N_H = sum_(h in H) h^* : Pic^0(P) -> Pic^0(P)
```

has connected image and its image is contained in `Pic^0(P)^H`. Therefore `N_H=0`.

If `A in Pic^0(P)` is `H`-invariant, then

```text
0=N_H(A)=4A.
```

Thus every `H`-invariant torsion class in `Pic^0(P)` has order dividing `4`.

## 4. Pullback from the coarse quotient is injective in the present fixed-point-generated case

Let

```text
pi:P -> X=P/H
```

be the coarse quotient, with `P` connected and projective. Suppose `M in Pic(X)` has trivial ordinary pullback `pi^*M`.

The pullback carries its canonical `H`-linearization. After choosing a trivialization `pi^*M ~= O_P`, that linearization is given by a character

```text
chi:H->C^*
```

because all global units on connected projective `P` are constant. If `h in H` fixes a point of `P`, the canonical action of `h` on the fibre of a bundle pulled back from the coarse quotient is the identity; hence `chi(h)=1`.

Therefore, if elements having fixed points generate `H`, then `chi` is trivial. The trivialization is `H`-equivariant and taking invariants gives `M ~= O_X`. Hence in this case

```text
pi^*:Pic(X)->Pic(P)
```

is injective.

## 5. Consequence for the present `H=(Z/2)^2` quotient

If a torsion line bundle descends to `X=P/H`, its pullback is an `H`-invariant torsion element of `Pic^0(P)`, so its fourth power pulls back trivially. If the two generators of `H` each have fixed points on `P`, the injectivity above then gives

```text
M^4 ~= O_X.
```

Thus the torsion exponent on the smooth resolution divides `4`, provided the retained geometry verifies:

- all singularities of `X=P/H` are `A1` rational double points;
- the two fixed-point-bearing involutions generate `H`;
- `H^1(P,O_P)^H=0`.

Those are repository-side facts and must be source-locked by the downstream certificate.

## Firewalls

- No claim that every quotient by `(Z/2)^2` has torsion exponent `4`.
- No use of the Beauville free subgroup in place of the support-specific `H`.
- No claim that the order is exactly `4`, `2`, or `1`.
- No conductor sign, weighted-cut bound, `e=2` closure, MB104 credit, heavy-compute authorization, or merge authorization.
