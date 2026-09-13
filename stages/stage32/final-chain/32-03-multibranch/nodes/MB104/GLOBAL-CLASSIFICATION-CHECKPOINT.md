# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE AFTER INTERMEDIATE HOSTILE-AUDIT PASS / GEOMETRIC P5 CORE 864 / DANGEROUS EQUALITY-PACKET CORE 768 / `000707` e2 CONDUCTOR DESCENT-GLUING MAP ACTIVE / NO CREDIT**

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

## e=2 ambient Kummer monodromy constraint

Put

```text
U=S\\B_abs.
```

The relation `2L_abs~B_abs` defines one fixed degree-two etale Kummer torsor over `U`, hence one character

```text
alpha_abs: pi_1(U) -> Z/2.
```

The restricted cover on the singular carrier is obtained by base change. In the `e=2` case its pullback to the normalization `E` is split, so `alpha_abs` vanishes on normalization loops, but conductor branch identifications may still evaluate nontrivially. For two normalization branches `beta_i,beta_j` above a singular point, let `lambda_(p;i,j)` be the corresponding ambient fibre-transport loop. Then the retained sheet labels satisfy

```text
epsilon_i+epsilon_j=alpha_abs(lambda_(p;i,j)).
```

Consequently the exact cross-sheet formula is

```text
y/2
 = sum_p sum_(i<j) I_p(beta_i,beta_j)
                    * alpha_abs(lambda_(p;i,j)).
```

Thus the conductor/gluing character `kappa` is not an arbitrary element of the normalization kernel and local sheet labels cannot be chosen independently. The missing computation is now the image of conductor identification cycles in `pi_1(U)` (or a valid mod-two homology realization) followed by this fixed character.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-KUMMER-MONODROMY.md` and `STACKS-KUMMER-AMBIENT-ETALE-MONODROMY-SOURCE-NOTE.md`.

## Explicit Kummer representative

For the same factor coordinate

```text
f_t=(t-i)/(t+i),
```

the complete resolved bad fibers satisfy

```text
div(f_t)=F_a-F_b
        =2(Q_a-Q_b)+E_a-E_b
        =2L_abs-B_abs.
```

Therefore the ambient etale double cover on `U=S\\B_abs` is represented by the explicit square-class `[f_t]`. On `U`, the only remaining zero/pole divisors are `2Q_a` and `2Q_b`, so all codimension-one valuations are even. Nontrivial conductor signs, if present, are global square-root monodromy rather than local odd branching.

In the `e=2` case, choose `g in k(E)^*` with

```text
g^2=f_t|_E.
```

For two normalization preimages identified in the singular carrier, `alpha_abs(lambda_(p;i,j))` is exactly the same-sign/opposite-sign comparison of the limiting values of `g`. Thus the next computation can bypass a full presentation of `pi_1(U)` and work directly with the modular/product-cover lift of `sqrt((t-i)/(t+i))`.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md`.

## Residual base-cover semantic correction

The square-root transport is now fixed at the residual quotient level

```text
q:R=C8/H -> S=C8/G,
phi:E->S.
```

Choose `h in k(S)^*` representing `q`, so `k(R)=k(S)(sqrt(h))`. The normalized base change `Norm(E x_S R)` is represented by

```text
[h o phi] in k(E)^*/k(E)^{*2}.
```

The explicit surface representative satisfies the verified square-class match

```text
[f_t|_E]=[h o phi],
f_t=(t-i)/(t+i),
```

but literal equality of rational functions is not asserted. Thus in the `e=2` case the correct sign-transport object is the square root of the pulled-back residual-cover class. The missing datum is an explicit map from each conductor normalization preimage to its lift in `R` above `phi(x)`; only this determines same-sheet versus opposite-sheet gluing.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-SQRT-FACTOR-BASECHANGE-SEMANTICS.md`.

## O210 precedent transfer boundary

A bounded cross-lane lookup found the closest retained precedent in the post-1490 O210 chain. There, relative-H actions are source-locked on the 48 marked X node lifts and may transport already-attached marked-point data such as multiplicities. The same chain explicitly records that no local equation, tangent cone, branch jet, strict-transform point on the exceptional line, or infinitely-near cluster is retained.

Therefore these O210 assets do not determine the MB104 branch-to-residual-sheet map. In particular:

```text
marked-node permutation != normalization-branch permutation,
multiplicity transport != residual-sheet transport.
```

The active missing input is now narrowed to local modular geometry: a completed-local or theta-coordinate map near a supported box node that sends a local carrier branch parameter to its point in `X(8)xX(8)`, then to `C8/H` coordinates and the residual `G/H` sheet.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-O210-LOCAL-LIFT-PRECEDENT-BOUNDARY.md`.

## Invariant A1 branch normalization boundary

With `B=C[[p^2,pq,q^2]]=C[[x,y,z]]/(xz-y^2)`, an exact downstairs carrier branch plus its normalization determines only the unordered pair of product lifts related by `(p,q)->(-p,-q)`. Thus the branch germ cannot canonically select a residual sheet. For conductor-identified normalization points, the missing datum is the descent/gluing isomorphism between their residual-cover fibres; identity and deck-twisted gluing have the same downstairs invariant branches but opposite conductor character.

Evidence: `GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION.md`.

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
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP
```

Assume `e=2` and choose `g` on the normalization with `g^2=f_t|_E`, where `f_t=(t-i)/(t+i)`. Compute at each conductor identification whether the two normalization preimages have the same or opposite limiting square-root sign using the explicit modular/product-cover lift. The opposite-sign weighted intersection sum is exactly `y/2`. Any strict upper bound below `84l^2` contradicts `(E2-HODGE)` and excludes `e=2`. Even valuations of `f_t` on `U` prove etaleness, not global triviality.

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
