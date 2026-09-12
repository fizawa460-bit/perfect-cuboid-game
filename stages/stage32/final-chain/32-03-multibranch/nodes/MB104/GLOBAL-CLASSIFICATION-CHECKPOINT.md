# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE AFTER INTERMEDIATE HOSTILE-AUDIT PASS / GEOMETRIC P5 CORE 864 / DANGEROUS EQUALITY-PACKET CORE 768 / `000707` e2 CROSS-SHEET CONDUCTOR UPPER BOUND ACTIVE / NO CREDIT**

The most recent hostile-audited retained boundary is

```text
e269761fbe82c56cdcc8d4870584952dc2d800a3
```

with `HOSTILE AUDIT: PASS`, review `5187369070`. Long-lived-PR audit growth is measured anew from this exact head.

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

on `0000770000ff`, `00007b0000ff`, `000707000f0f`.

The two size-48 dangerous equality packets are excluded for all `l>=1` by the retained `j=1728` CM / inert-7 obstruction. Thus the dangerous equality-packet core is `768`, consisting only of `000707000f0f`.

For this mask the node-type count is `(7,7,0)` and the product-cover component degree is

```text
e=2 or e=4.
```

## Audited `000707` input

With `H=<s1,s2>`, `Q=Z/H`, `R=C8/H~=P1`, the two descended factor maps have degree `28l` for `e=2` and `56l` for `e=4`. Their joint map `Q->P1xP1` is birational. The two retained zero quartics are Satake-boundary components and each forces two specific fully reduced/unramified saturated factor fibers. These facts were included in hostile review `5187369070`.

## Residual two-torsion character

Both surviving cases produce a degree-`56l` map

```text
phi:E->C8/G~=P1.
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

The normalized residual base change is classified by `eta`, hence

```text
e=2 <=> eta=0,
e=4 <=> eta!=0.
```

Evidence: `GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md` and matching certificate/verifier.

## Surface half-fiber and canonical half-branch class

For a product-induced genus-five fibration, let `Q_a,Q_b` be the two absent-type reduced `G2` bad fibers, with disjoint eight-node sets `T_a,T_b`. Their resolution fibers give

```text
2(Q_a-Q_b)
  ~ sum_(p in T_b)E_p - sum_(p in T_a)E_p.
```

Set

```text
Delta=Q_a-Q_b,
L_abs=Delta+sum_(p in T_a)E_p.
```

Then

```text
2L_abs ~ B_abs,
B_abs=sum_(all 16 absent-type nodes p) E_p.
```

The `000707` carrier class has coefficient zero at all sixteen absent exceptionals and an integral carrier therefore avoids them. Hence on the normalization

```text
eta=O_E(L_abs|_E)=O_E(Delta|_E).
```

Exact numerical data are

```text
B_abs^2=-32,
L_abs^2=-8,
H.L_abs=K.L_abs=D_l.L_abs=0,
L_abs.E_p=-1 for every absent exceptional E_p.
```

Evidence: `GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md` and matching certificate/verifier.

## Numerical Picard wall

The rank-64 Picard lattice identifies `L_abs` and all displayed intersections exactly. It does **not**, by numerical pairings alone, distinguish

```text
L_abs|_E = 0
```

from a nonzero element of `Pic^0(E)[2]`: both have degree zero and numerically trivial first Chern class after restriction to the genus-one normalization.

Similarly, a surface-cohomology calculation on the singular carrier cannot be promoted directly to a statement on the normalization without controlling conductor/gluing data. Therefore the purely numerical Picard-pairing route is exhausted; the actual restriction/monodromy is required.

## e=2 split-normalization Hodge constraint

Let `pi:Y->S` be the double cover defined by `L_abs`, branched along `B_abs`. The carrier is disjoint from the branch divisor, so the induced cover over the singular carrier is etale.

If `e=2`, then `eta=0` and the normalization of `pi^{-1}(C)` is two copies of `E`. The singular preimage can nevertheless remain connected by cross-sheet conductor gluing. It has two irreducible components `C_1,C_2`, exchanged by the deck involution. Put

```text
y=C_1.C_2.
```

Projection formula gives

```text
C_1^2=C_2^2=D_l^2-y=336l^2-y.
```

For any ample divisor `A` on `S`,

```text
(C_1-C_2).pi^*A=0.
```

Hodge index on `Y` yields

```text
(C_1-C_2)^2=672l^2-4y <=0,
```

hence the new quadratic requirement

```text
y >= 168l^2.                                  (E2-HODGE)
```

Adjunction on `S` gives

```text
Delta(C)=168l^2+56l.
```

If `delta_same` denotes the normalization defect internal to either lifted component, etaleness and the union formula give

```text
2Delta(C)=2delta_same+y.
```

Thus `e=2` requires

```text
y/2 >=84l^2,
delta_same <=84l^2+56l.
```

This is compatible with the current quadratic delta budget and therefore is not yet a contradiction. It is a new target for conductor geometry.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR.md` and matching certificate/verifier.

## Two-factor comparison

For complementary factor coordinates

```text
t=(c+a1)/(a2+i*a3),
u=(c+a1)/(a2-i*a3),
```

and absent type `b3=0`, exact cuboid algebra gives

```text
[(t-i)/(t+i)] / [(u-i)/(u+i)]
  = (c+a3)/(c-a3)
  = ((c+a3)/b3)^2.
```

Thus the two factor square classes agree; comparing them cannot distinguish `e=2` from `e=4`. Only the common one-factor class remains.

## Active next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-CROSS-SHEET-CONDUCTOR-UPPER-BOUND
```

For `e=2`, derive an independent upper bound for

```text
y=C_1.C_2.
```

Any strict inequality

```text
y<168l^2
```

contradicts `(E2-HODGE)` and excludes `e=2`, forcing the nonzero residual character `e=4`.

Candidate inputs are explicit local conductor/singularity types, a global conductor divisor bound, or exact modular/commensurator monodromy. The retained Lu--Miyaoka ordinary-node/triple bound is only linear and does not by itself contradict the quadratic requirement.

In parallel, `e=4` remains the one-factor Abel--Jacobi/monodromy problem `eta!=0`.

The 2026 Stoll--Testa classification of integral curves of degree at most `6` does not directly settle this leaf because the current carrier has degree `112l`.

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
