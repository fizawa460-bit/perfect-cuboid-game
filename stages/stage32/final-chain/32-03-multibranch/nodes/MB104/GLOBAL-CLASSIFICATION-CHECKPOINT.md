# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE AFTER INTERMEDIATE HOSTILE-AUDIT PASS / GEOMETRIC P5 CORE 864 / DANGEROUS EQUALITY-PACKET CORE 768 / `000707` ONE-FACTOR HALF-FIBER CHARACTER ACTIVE / NO CREDIT**

The most recent hostile-audited retained boundary is

```text
e269761fbe82c56cdcc8d4870584952dc2d800a3
```

with `HOSTILE AUDIT: PASS`, review `5187369070`.  This was the delta-bounded intermediate audit after the earlier boundary `39a56d2...`; long-lived-PR audit growth is measured anew from `e269761f...`.

## Scope

Displayed uniform genus-one P5 ray:

```text
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
d=112l,
l>=1.
```

Dangerous MB104 packet is stronger:

```text
r_i=M_i=8l at all 14 supported nodes,
all branches FSM-minimal (A,B)=(1,1), m=1,
R=R8=M=r_odd=d=112l.
```

Do not identify the Picard class with this branch packet.

## Current populations

The geometric uniform-ray core allowing arbitrary branch partitions remains

```text
864 = 48+48+768
```

on

```text
0000770000ff,
00007b0000ff,
000707000f0f.
```

The two size-48 dangerous equality packets are excluded for all `l>=1` by the retained `j=1728` CM / inert-7 obstruction.  Thus the dangerous equality-packet core is

```text
768
```

and consists only of

```text
000707000f0f.
```

For this mask the node-type count is `(7,7,0)` and the product-cover component degree is

```text
e=2 or e=4.
```

## Audited `000707` input

With `H=<s1,s2>`, `Q=Z/H`, `R=C8/H~=P1`, the two descended factor maps have degree

```text
e=2: 28l,
e=4: 56l.
```

Their joint map `Q->P1xP1` is birational.  The two retained zero quartics are Satake-boundary components and each forces two specific fully reduced/unramified saturated factor fibers.  These facts were included in hostile review `5187369070`.

## New post-audit reduction: one global two-torsion character

Let `G/H~=Z/2` be the residual factor-cover character.  Both surviving cases produce a degree-`56l` map

```text
phi:E->S=C8/G~=P1.
```

At the two branch values of the absent singular type,

```text
phi^*(a)=2A,
phi^*(b)=2B,
deg A=deg B=28l.
```

Define

```text
eta=O_E(A-B) in Pic^0(E)[2].
```

The normalized residual base change is classified by `eta`, hence exactly

```text
e=2  <=> eta=0,
e=4  <=> eta!=0.
```

Evidence:

- `GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md`
- matching certificate/verifier.

## Surface-Picard realization of `eta`

Stoll--Testa's two complementary product-induced isotrivial genus-five fibrations have six bad fibers each; every bad reduced component is one of the twelve known `G2` elliptic quartics and occurs with multiplicity two on the canonical model.

On the minimal resolution a bad fiber with reduced component `Q` and eight box nodes `T_Q` is

```text
F_Q=2Q+sum_(p in T_Q)E_p,
F_Q^2=0,
K.F_Q=8.
```

For the two absent-type half-fibers `Q_a,Q_b` in one factor fibration,

```text
2(Q_a-Q_b)
  ~ sum_(p in T_b)E_p - sum_(p in T_a)E_p.
```

The dangerous `000707` class has no absent-type exceptional coefficient, so an integral carrier is disjoint from those exceptional curves.  Therefore

```text
eta=O_E((Q_a-Q_b)|_E),
D_l.Q_a=D_l.Q_b=28l.
```

This is an explicit restriction of a known Picard-64 class.  Torsion-freeness of `Pic(S)` does **not** force `eta=0`, because the surface relation contains the nonzero exceptional correction.

Evidence:

- `STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md`
- `GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD.md`
- matching certificate/verifier.

## Factor-character comparison is exhausted

For the two complementary ruling coordinates

```text
t=(c+a1)/(a2+i*a3),
u=(c+a1)/(a2-i*a3),
```

the absent `b3=0` values are `+i,-i`.  Use square-class representatives

```text
f_t=(t-i)/(t+i),
f_u=(u-i)/(u+i).
```

Exact cuboid algebra gives

```text
f_t/f_u
 = (c+a3)/(c-a3)
 = ((c+a3)/b3)^2,
```

using `b3^2=c^2-a3^2`.

Thus

```text
eta_1=eta_2
```

is automatic already in the cuboid function field.  Trying to close `000707` by making the two factor characters disagree is therefore a dead route.

Evidence:

- `GENUS1-SPAN5-BALANCED16-000707-CHARACTER-PAIR-SQUARE-WALL.md`
- matching exact-polynomial certificate/verifier.

## Active next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-FIBER-CHARACTER
```

Only one binary invariant remains in the current cover reduction:

```text
is f_t|_E a square in k(E)^* ?
```

Equivalently, decide whether

```text
O_E((Q_a-Q_b)|_E)
```

is trivial or the nonzero two-torsion point.  A useful continuation must force `eta=0` (exclude `e=4`), force `eta!=0` (exclude `e=2`), or obtain an independent contradiction.  Do not reopen coarse Hurwitz capacity, zero-quartic fixedness, static landing, or the now-exhausted two-factor character comparison.

Genus-one support-span P6 and genus-zero full-span P6 remain active in parallel.

## Firewalls

- geometric arbitrary-branch core remains `864`;
- dangerous equality-packet core remains `768`;
- `000707` remains open for `e=2,e=4`;
- arbitrary unequal exceptional coefficients remain open;
- support-span five is not fully closed;
- P6 sectors remain open;
- MB104 incomplete; no finite degree window;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
