# Stage32 MB104 — `000707000f0f` e=2 ambient H1 / Picard-torsion kill

Status: **RETAINED CANDIDATE TOPOLOGICAL REFINEMENT / `H1(Y,Z)=0` / `Pic^tau(Y)=0` / `w~0` / CONDUCTOR SIGN OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The previous retained chain gives

```text
w=(C_1-C_2)+sum_j(d_j/2)F_j,
w == 0 numerically,
q(Y)=0,
[w] in Pic^tau(Y),
4w ~ 0
```

at candidate level. This note computes the ambient first integral homology directly and removes the remaining finite Picard-torsion ambiguity. It does not evaluate an individual conductor pair.

## 1. Exact one-factor orbifold passport

For the support-specific group

```text
H=<s1,s2>~=(Z/2)^2
```

repository evidence gives

```text
C8/H ~= P1,
```

with eight order-two branch values: four of inertia `s1`, four of inertia `s2`, and `s1*s2` fixed-point-free.

Thus use

```text
Delta=<x1,...,x8 | x_i^2=1, x1*...*x8=1>
```

and

```text
phi(x1)=...=phi(x4)=s1,
phi(x5)=...=phi(x8)=s2.
```

For two factors the group acting on the simply connected product universal cover with coarse quotient

```text
X_H=(C8 x C8)/H_diag
```

is

```text
F=Delta x_H Delta.
```

Equivalently `F` is the index-four kernel in `Delta x Delta` of the difference of the two `H` labels.

## 2. Reidemeister-Schreier abelianization

Present `Delta x Delta` with generators

```text
x1,...,x8,y1,...,y8
```

using the two orbifold presentations and the 64 cross-commutators `[x_i,y_j]`.

Use the `H` transversal

```text
1, x1, x5, x1*x5.
```

Reidemeister-Schreier rewriting gives 64 provisional Schreier generators. Including trivial-Schreier relations and the four transversal rewrites of every ambient relator gives

```text
331 integer abelianized relations.
```

Before imposing coarse fixed-point relations the exact Smith computation is

```text
F_ab ~= (Z/2)^13.
```

This intermediate value is diagnostic only; the coarse orbit space requires Armstrong's fixed-point normal closure.

## 3. Exact fixed-point relation table

A nontrivial elliptic element of `Delta` is conjugate to one of the eight cone generators. A pair in `F` fixes a point of the product universal cover iff both components are elliptic with the same `H` label.

Modulo conjugation by `F`, a fixed pair is represented by:

- one of four first-factor cone generators of a chosen inertia type;
- one of four second-factor cone generators of the same inertia type;
- one of four relative `H` cosets of their conjugators.

Hence the complete finite table has

```text
2*4*4*4 = 128
```

relations.

Appending these relations gives an integer relation matrix

```text
459 x 64.
```

In canonical row order its SHA-256 is

```text
d15f8d93410f8d448cb92de3be81e3a8a01dcc34ec39ddb0c37a78126b0ab3d4.
```

A 64-row submatrix at zero-based row indices

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
 25,26,27,28,33,41,49,53,54,55,56,61,69,77,89,90,91,92,97,
 98,99,100,107,115,123,131,135,136,137,138,331,332,333,334,
 335,339,343,363,395,396,397,399,403]
```

has exact determinant

```text
+1.
```

Therefore the relation lattice is all of `Z^64`, so

```text
(F/N_fixed)_ab = 0.
```

By Armstrong,

```text
H_1(X_H,Z)=0.
```

No numerical approximation or probabilistic rank test is used in this conclusion.

## 4. Resolution and the active torsion class

The retained quotient geometry has only isolated `A1` rational double points. Replacing each singular cone neighborhood by its minimal-resolution neighborhood preserves `H_1`, and smooth blowups preserve `H_1`. Since the retained `Y` is a smooth projective model birational to this quotient resolution,

```text
H_1(Y,Z)=0.
```

The retained irregularity computation already gives

```text
q(Y)=0,
Pic^0(Y)=0.
```

Universal coefficients plus the exponential sequence then give

```text
Pic^tau(Y)=0.
```

Hence the active numerical remainder is actually linearly trivial:

```text
w ~ 0,
(C_1-C_2) ~ -sum_j(d_j/2)F_j.               (LIN)
```

This strengthens the earlier candidate `4w~0` to exponent one.

## 5. What this does not solve

`(LIN)` is a global integral Picard relation. It does **not** choose the simultaneous residual sign `(r_z,r_w)` at an individual normalization preimage. Therefore it does not by itself materialize

```text
M_(u,v),
chi_res(M_(u,v)),
weighted opposite-sheet cut.
```

The conductor-pair leaf remains open. A later continuation may use `(LIN)` as a new global constraint on the centered branch variables `d_j`, but such a deduction must be proved separately.

## Firewalls

- No claim that `pi_1(X_H)` itself is trivial; only its abelianization is killed by the displayed relation lattice.
- No conductor sign is assigned.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.