# Stage32 MB104 — `000707000f0f` e=2 ambient torsion exponent divides four

Status: **RETAINED TORSION-EXPONENT REFINEMENT / `4w~0` / EXPONENT ONE AND CONDUCTOR SIGN OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume conditionally that the retained dangerous packet is realized in the `e=2` case. The previous anti-invariant and irregularity leaves give, on the smooth residual-cover surface `Y`,

```text
w=(C_1-C_2)+sum_(j in Sigma)(d_j/2)F_j,
w == 0 numerically,
q(Y)=0,
[O_Y(w)] in Pic^tau(Y) is finite torsion.
```

The previous leaf did not compute the exponent. This refinement proves that the exponent of the relevant ambient torsion group divides `4`.

## 1. Replace `Y` birationally by the resolution of the support-specific quotient

Put

```text
P=C8 x C8,
H=<s1,s2> ~= (Z/2)^2,
X_H=P/H_diag.
```

The retained function-field bridge proves that `Y` is birational to a smooth projective resolution

```text
rho:Xtilde_H -> X_H.
```

For smooth projective surfaces, blowup factorization adds only free exceptional `Z` summands to Picard groups. Hence the torsion subgroup of the Picard group is birationally invariant. It is enough to bound torsion on `Xtilde_H`.

## 2. Every singularity of `X_H` is `A1`

The retained Hurwitz-capacity geometry gives:

```text
H={1,s1,s2,h},
h=s1*s2,
```

where each of `s1,s2` has exactly eight fixed points on `C8`, their fixed-point sets are disjoint, and `h` is fixed-point-free.

For the diagonal action on `P`, a nontrivial stabilizer can therefore only be `<s1>` or `<s2>`. At a fixed point of a nontrivial involution on a smooth complex curve, the tangent action is `-1`. Hence at a fixed point of the diagonal action the local tangent action is

```text
(u,v)->(-u,-v),
```

so the quotient singularity is an `A1` rational double point. There are no points with stabilizer all of `H` because the `s1` and `s2` fixed sets on `C8` are disjoint.

Thus every exceptional fibre of `rho` is one `(-2)` rational curve.

## 3. Torsion descends from `Xtilde_H` to `X_H`

Let

```text
L in Pic(Xtilde_H)
```

be torsion. Its restriction to each formal `A1` fibre is torsion. The reduced exceptional curve has Picard group `Z`, and the successive infinitesimal restriction kernels are additive complex vector spaces, so the formal-fibre Picard group has no nonzero finite torsion. Therefore `L` is trivial on every formal fibre.

The rational-singularity descent criterion recorded in `FINITE-QUOTIENT-TORSION-EXPONENT-FOUR-SOURCE-NOTE.md` gives a line bundle

```text
M in Pic(X_H)
```

with

```text
L ~= rho^* M.
```

## 4. Pull to `P` and kill by the order-four norm

Let

```text
pi:P -> X_H=P/H.
```

Because `M` is torsion, `A=pi^*M` is torsion on `P`. Integral `H^2(P,Z)` is torsion-free, so

```text
A in Pic^0(P).
```

The previous irregularity computation gives

```text
H^1(P,O_P)^H=0.
```

Hence the identity component of `Pic^0(P)^H` is zero-dimensional. The norm endomorphism

```text
N_H=sum_(g in H) g^*
```

has connected image contained in that fixed subgroup, so

```text
N_H=0 on Pic^0(P).
```

Since `A=pi^*M` is `H`-invariant,

```text
0=N_H(A)=4A.
```

Therefore

```text
pi^*(M^4) ~= O_P.                              (PULL4)
```

## 5. Pullback from `X_H` is injective here

Suppose `N in Pic(X_H)` and `pi^*N` is trivial. Choose a trivialization. The canonical `H`-linearization of the pullback is then a character

```text
chi:H->C^*.
```

Both generators `s1,s2` have fixed points on `P`. At a fixed point, a line bundle pulled back from the coarse quotient has trivial stabilizer action on its fibre. Hence

```text
chi(s1)=chi(s2)=1.
```

Since `s1,s2` generate `H`, `chi` is trivial. The chosen trivialization is therefore `H`-equivariant and descends to a trivialization of `N`. Thus

```text
pi^*:Pic(X_H)->Pic(P)
```

is injective.

Applying this to `(PULL4)` gives

```text
M^4 ~= O_XH,
L^4 ~= O_Xtilde_H.
```

Transporting torsion across the smooth birational equivalence yields

```text
exp Pic^tau(Y) divides 4.                      (EXP4)
```

Here `Pic^0(Y)=0` is already retained, so `Pic^tau(Y)` is exactly the finite numerically-trivial torsion group relevant to `w`.

## 6. Apply to the active anti-invariant remainder

Since `O_Y(w)` is numerically trivial, `(EXP4)` gives

```text
4w ~ 0.
```

Equivalently,

```text
4(C_1-C_2)
 ~ -2 sum_(j in Sigma) d_j F_j.                (ANTI-PIC-4)
```

This replaces the previous unspecified exponent `N_Y` by a uniform explicit divisor of `4`, independent of `l` and of the hypothetical carrier.

## What remains open

This refinement does **not** prove

```text
w~0,
2w~0,
ord(w)=4,
or ord(w)=1.
```

It also does not determine any `d_j`, conductor transition `M_(u,v)`, or residual sheet sign. The active conductor-preimage map remains the primary leaf.

The useful remaining integral-Picard question is now finite and explicit:

```text
[w] in Pic^tau(Y)[4].
```

Any later argument killing this particular 4-torsion class upgrades the retained numerical anti-invariant decomposition to exponent-one linear equivalence.

## Firewalls

- The support-specific `H=<s1,s2>` is used; it is not replaced by the Beauville free subgroup.
- No claim that `P->X_H` is etale.
- No exponent-two or exponent-one claim.
- No conductor sign or weighted-cut upper bound.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
