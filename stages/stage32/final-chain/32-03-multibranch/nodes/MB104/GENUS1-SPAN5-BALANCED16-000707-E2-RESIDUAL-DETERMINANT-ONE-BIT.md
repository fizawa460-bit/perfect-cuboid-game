# Stage32 MB104 — `000707000f0f` e=2 residual determinant one-bit reduction

Status: **RETAINED CANDIDATE RESIDUAL-`G/H` DETERMINANT REDUCTION / ONE DISTINGUISHED `G`-FIXED 2-TORSION CLASS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding conductor-determinant leaf reduced each factorwise product-image half-discriminant to

```text
O(F_i)=A_ref(l)^(n+4) tensor epsilon_i,
epsilon_i in J(C8)^H[2],
J(C8)^H ~= (Z/2)^6.
```

The active residual quotient is

```text
G/H ~= Z/2,
```

represented, in the retained standard singular basis, by the third generator `s3`. This note computes its exact action on the 64 determinant possibilities.

## 1. H-fixed and G-fixed 2-torsion dimensions

The retained exact integral-homology replay gives

```text
J(C8)^H[2] ~= F_2^6,
J(C8)^G[2] ~= F_2^5.
```

Let `T` denote the nontrivial residual class `s3H`. Since `G` is elementary abelian, `T` preserves the H-fixed subgroup. Over `F_2`,

```text
N_res := T-1 = T+1
```

satisfies `N_res^2=0`.

Its kernel on `J(C8)^H[2]` is exactly the full-`G` fixed subgroup, so

```text
dim ker(N_res)=5,
dim im(N_res)=1.                                (RANK1)
```

Thus all failure of an H-fixed determinant line to be T-invariant is measured by one distinguished nonzero full-`G` fixed 2-torsion class.

## 2. Exact distinguished class in the retained homology basis

Use the deterministic homology basis `h1,...,h10` and full-`G` fixed basis `tau1,...,tau5` from the retained explicit-basis leaf.

The exact mod-two matrix replay gives the unique nonzero image vector

```text
kappa_num=(1,1,0,1,1,1,0,1,1,0).
```

In the retained `tau` basis this is

```text
kappa = tau1 + tau5.                            (KAPPA)
```

Hence

```text
im(T-1) = {0,kappa}.
```

Equivalently, for every H-fixed determinant class `epsilon`,

```text
epsilon tensor T^*epsilon in {O_C, kappa}.      (ONEBIT)
```

There are 32 T-fixed determinant classes and 32 nonfixed classes, the latter forming 16 two-element residual orbits.

## 3. Consequence for the two residual product components

In the e=2 geometry the nontrivial residual element sends the product component `Z` to the distinct component `TZ`. If

```text
epsilon_i(Z)=det(f_i*O_Z),
```

then equivariance gives

```text
epsilon_i(TZ)=T^*epsilon_i(Z).
```

The factor reference class `A_ref(l)^(n+4)` is full-`G` invariant, so the corresponding half-discriminant classes satisfy

```text
O(F_i(TZ)-F_i(Z))
 in {O_C,kappa}.                                (DISC-DIFF)
```

Therefore the residual comparison of product-component conductor determinant classes is not a 64-way ambiguity. It is a single global binary invariant.

## 4. Relation to the active conductor-sheet bit

The active conductor problem also has a binary residual character, namely the `G/H` sheet of

```text
q:R=C8/H -> S=C8/G.
```

Both bits are controlled by the same residual group element `T`, but they live in different constructions:

- the active sheet bit is pointwise transport of `r0` / `(r_z,r_w)` at conductor normalization preimages;
- `(ONEBIT)` is the residual action on the determinant line of the full etale product cover.

No equality between these two bits is asserted here. A valid continuation needs an adapter showing how the determinant norm class `kappa` is computed from, or constrains, the weighted pointwise conductor transitions.

## Route consequence

The new global target is now extremely small:

```text
residual determinant discrepancy = 0 or kappa=tau1+tau5.
```

A successful adapter from conductor-pair transitions to the determinant/sign local system would convert the unresolved branchwise sheet data into one global parity equation. Such an adapter may then be combined with the retained node-orbit and A1 energy formulas.

## Firewalls

- `kappa` is not identified with the residual Kummer cover class itself.
- No individual conductor pair is assigned same/opposite sheet.
- No parity formula for the weighted conductor cut is claimed yet.
- No claim that `epsilon_i` must be non-T-invariant because `Z` and `TZ` are distinct.
- No weighted-cut upper bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
