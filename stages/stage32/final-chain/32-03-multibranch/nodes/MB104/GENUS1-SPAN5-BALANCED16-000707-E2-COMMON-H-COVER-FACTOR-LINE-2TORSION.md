# Stage32 MB104 — `000707000f0f` e=2 common-`H`-cover factor-line 2-torsion

Status: **RETAINED CANDIDATE COMMON-ABELIAN-COVER REFINEMENT / FACTOR FIBER LINES DIFFER BY AT MOST E[2] / TYPEWISE RAMIFICATION DIVISORS LINEARLY MATCH / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the preceding etale-basechange passport.  For the two quotient factor maps write

```text
psi_i:E->R=C8/H ~= P1,
M_i:=psi_i^*O_R(1),
deg M_i=n=28l,
i=1,2.
```

The same connected curve `Z` carries the diagonal action of

```text
H=<T',TT'R> ~= (Z/2)^2
```

and in the `e=2` case

```text
E=Z/H.
```

Hence both factor constructions recover the **same character-labelled `H`-cover**

```text
Z->E.
```

This note compares the two constructions at the level of the two quadratic eigensheaves.

## 1. The two branch characters of `C8->R`

In the retained coordinate model

```text
u^2=(r^4+4)/4,
v^2=(r^4-4)/4.
```

Thus the two independent quadratic subcover characters have branch divisors

```text
B_u={r^4=-4},
B_v={r^4=+4},
```

each of degree four on `R=P1`.

Their defining square-root line on `R` is therefore

```text
O_R(2),
```

since

```text
O_R(B_u) ~= O_R(B_v) ~= O_R(4) ~= O_R(2)^2.
```

## 2. Normalize one pulled-back quadratic character

Fix `chi in {u,v}` and factor `i`.  The etale-basechange passport gives only local ramification indices `1` or `2` for `psi_i` above `B_chi`.

Write the pullback divisor as

```text
psi_i^* B_chi = U_chi + 2 R_(i,chi).             (PB)
```

Here:

- `U_chi` is the reduced divisor of points where `psi_i` is unramified over `B_chi`;
- `R_(i,chi)` is the reduced divisor of simple ramification points over `B_chi`.

After normalizing the pulled-back double cover, the doubled zeros in `2R_(i,chi)` are removed from the branch divisor.  Therefore its character building line is

```text
N_(i,chi)
 = M_i^2 tensor O_E(-R_(i,chi)),                (BUILD)
```

and

```text
N_(i,chi)^2 ~= O_E(U_chi).                      (SQ)
```

The divisor `U_chi` is exactly the branch divisor on `E` of the corresponding character subcover of `Z->E`.

## 3. The character building lines are intrinsic to `Z->E`

The two factor projections are `H`-equivariant for the **same diagonal `H` action on `Z`**.  Therefore the `chi`-eigensheaf in the finite algebra

```text
p_*O_Z,
p:Z->E,
```

is intrinsic and does not depend on whether it is reconstructed from factor 1 or factor 2.

Consequently

```text
N_(1,u) ~= N_(2,u),
N_(1,v) ~= N_(2,v).                             (EIG)
```

Using `(BUILD)`, for each `chi` this gives

```text
M_1^2 tensor O(-R_(1,chi))
 ~=
M_2^2 tensor O(-R_(2,chi)).                     (TYPE)
```

## 4. Riemann--Hurwitz collapses the factor-line difference to 2-torsion

All ramification of `psi_i` lies above `B_u union B_v`, so

```text
Ram(psi_i)=R_(i,u)+R_(i,v).
```

Since `E` has genus one and `R=P1`, Riemann--Hurwitz gives the line-bundle identity

```text
O_E(Ram(psi_i))
 ~= K_E tensor psi_i^*K_R^(-1)
 ~= M_i^2.                                      (RH-LINE)
```

Multiply the two character identities `(TYPE)` for `u` and `v`.  Their left side is

```text
M_1^4 tensor O(-Ram(psi_1)),
```

and their right side is the analogous factor-2 expression.  Substituting `(RH-LINE)` gives

```text
M_1^2 ~= M_2^2.                                 (SQUARE-LINE)
```

Therefore

```text
delta_fac := M_1 tensor M_2^(-1)
 in Pic^0(E)[2].                                (FAC2)
```

Because `E` is elliptic,

```text
|Pic^0(E)[2]|=4.
```

Thus the relative factor fiber-line ambiguity is at most four classes, uniformly in `l`.

## 5. Typewise ramification divisors also match linearly

Substitute `(SQUARE-LINE)` back into `(TYPE)`.  For each inertia type,

```text
O_E(R_(1,u)) ~= O_E(R_(2,u)),
O_E(R_(1,v)) ~= O_E(R_(2,v)).                  (RAM-MATCH)
```

So the two degree-`28l` maps do not merely have the same total ramification degree.  Their ramification divisors belonging to the two `H` characters are pairwise linearly equivalent on the common elliptic normalization.

This is a genuinely global Abel--Jacobi constraint.  The retained node-count/saturation equations record only the cardinalities of the unramified pieces and do not imply `(RAM-MATCH)` by themselves.

## 6. Relation to the previously retained residual class

The previously retained class

```text
eta in Pic^0(E)[2]
```

classifies the **residual `G/H` cover** and satisfies

```text
e=2 <=> eta=0.
```

The new class

```text
delta_fac=M_1 tensor M_2^(-1)
```

compares the two degree-`28l` `H`-quotient factor pencils.  They arise from different constructions.

No equality

```text
delta_fac=eta
```

is asserted.  In particular `e=2` does not by itself force `M_1~=M_2`; it only leaves the four possibilities in `(FAC2)`.

## Route consequence

Any future explicit realization of the two factor maps may be tested against the finite condition

```text
M_1 tensor M_2^(-1) in E[2]
```

and the two typewise divisor equalities `(RAM-MATCH)`.

A useful next target is to identify `delta_fac` from the explicit box/factor rational functions or to show that one of the three nontrivial elliptic 2-torsion possibilities is incompatible with the `000707` conductor/gluing data.

## Firewalls

- No claim that `delta_fac` is trivial.
- No identification of `delta_fac` with the residual half-branch class `eta`.
- Linear equivalence of typewise ramification divisors is not equality of their point sets.
- No conductor pair is assigned same/opposite residual sheet.
- No weighted-cut upper bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
