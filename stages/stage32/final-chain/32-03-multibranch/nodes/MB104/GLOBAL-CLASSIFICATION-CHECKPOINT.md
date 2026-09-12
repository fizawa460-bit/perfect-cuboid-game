# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / UNIFORM P5 GEOMETRIC CORE 864 / MB104 EQUALITY-PACKET CORE 768 / 000707 JOINT PAIR BIRATIONAL + SATURATED BOUNDARY FIBERS / INTERMEDIATE AUDIT APPROACHING / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of a standalone `R8<d/4+O(1)` inequality remains frozen unless a genuinely new lever appears.

The most recent hostile-audited retained boundary is

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`. The retained continuation below is newer and unaudited. The shared PR is now in the high-80s of retained commits beyond that boundary; the next substantial retained wave should be preceded by an intermediate hostile audit checkpoint under the repository-wide long-lived-PR policy.

## 1. Scope

Potentially infinite sectors remain

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
N>=14.
```

`span` means the box-node support span, not carrier containment.

For the displayed uniform genus-one P5 ray,

```text
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
d=112l,
l>=1.
```

The dangerous MB104 packet is stronger:

```text
r_i=M_i=8l on all 14 supported nodes,
all branches FSM-minimal (A,B)=(1,1), m=1,
R=R8=M=r_odd=d=112l.
```

The Picard class and this branch packet must not be conflated.

## 2. Geometric uniform-ray core

Incidence `24`, `20`, `19`, `15`, and all incidence-`14` ambient support orbits are closed for the displayed ray. Incidence16 originally left

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

`00070b000f0f` is closed for every `l>=1` by exact two-zero-quartic gluing monodromy

```text
17+12*sqrt(2).
```

Thus the geometric uniform-ray support population allowing arbitrary branch partitions is still

```text
864 = 48+48+768
```

on the first three masks.

All retained zero-pairing quartics on those 864 supports are nonfixed for all `l>=1`; the conic/quartic fixed-component route, hidden Pic0, static landing, and null-union gluing are exhausted there.

## 3. Global singularity walls

For a hypothetical integral genus-one member,

```text
p_a(D_l)=1+168l^2+56l,
Delta_total=168l^2+56l.
```

Lu--Miyaoka gives

```text
n_ordinary_node_or_triple >= max(0,112l-224).
```

Miyaoka 2008 single-curve orbibundle BMY gives no `l`-bound, and the sharp A1 conductor coefficient `delta>=r-1` is insufficient by itself.

## 4. Beauville equality rigidity

On the dangerous packet, `g=1` and `r_odd=d`. Pulling to

```text
P=C8 x C8,
g(C8)=5,
P->X=P/G0,
G0~=(Z/2)^2
```

forces both projections of every connected product-cover component `Z` to be finite etale of equal degree

```text
14 e l,
e in {1,2,4}.
```

Node-type replay gives

```text
0000770000ff : (14,0,0)
00007b0000ff : (14,0,0)
000707000f0f : (7,7,0).
```

For `000707`, the two used outside involutions exclude `e=1`; only `e=2,4` remain.

## 5. Size48 equality packets are closed by CM inert-7

For either one-type size48 support, quotienting `Z` by the unique singular involution gives an elliptic curve `B1`. Freitag--Salvati Manni's modular/Kummer model gives the corresponding factor quotient

```text
E0:y^2=x^3-x,
j(E0)=1728,
End^0(E0)=Q(i).
```

The two product projections descend to equal-degree isogenies

```text
B1 -> E0,
degree 14 e l.
```

Since `7` is inert in `Q(i)`, equal degree forces a common nontrivial 7-primary kernel, so the pair map has generic degree divisible by `7`. But the same modular map factors geometrically through the box/Kummer quotient with generic degree `e` or `2e`, one of `{1,2,4,8}`. Contradiction.

Therefore the dangerous equality packet is impossible on both size48 orbits for all `l>=1`.

Population split:

```text
geometric arbitrary-branch core: 864;
MB104 dangerous equality-packet core: 768,
```

with the latter consisting only of `000707000f0f`.

## 6. `000707` Hurwitz capacity

Let the two used singular involutions be `s1,s2` and

```text
H=<s1,s2> ~= (Z/2)^2.
```

For `e=2`, component stabilizer `K=H`; for `e=4`, `K=G~=(Z/2)^3`.

The quotient-Hurwitz regimes are

```text
e=2: degree 28l genus1 -> P1 with 8 involutory marked values;
e=4: degree 56l genus1 -> P1 with 6 involutory marked values.
```

In both cases the `112l` supported minimal branches exhaust the total unramified capacity. Coarse one-factor RH does not close either case.

## 7. Joint factor-pair map is birational

Put

```text
Q=Z/H,
R=C8/H ~= P1.
```

Then `g(Q)=1`, and the two descended factor maps

```text
psi1,psi2:Q->R
```

have common degree

```text
e=2: 28l;
e=4: 56l.
```

For

```text
Psi=(psi1,psi2):Q->R x R,
```

the only possible generic common quotient would come from a relative deck symmetry `(1,r)`, `r in H`. Any such nontrivial symmetry descends to a type-preserving automorphism of the 14-node support.

Exact `Aut(S)` replay gives support stabilizer order exactly `2`; its unique nonidentity element swaps

```text
b1=0 <-> b2=0,
```

so the type-preserving support stabilizer is trivial. Hence the relative symmetry group is trivial and

```text
Psi is birational onto its image.
```

The image has exact bidegree

```text
e=2: (28l,28l);
e=4: (56l,56l),
```

with normalization genus one.

Evidence:
- `GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md`
- matching certificate/verifier.

## 8. Satake-boundary fiber saturation

The two zero quartics are

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0.
```

Each is a smooth elliptic quartic with eight box nodes and seven supported nodes. Freitag--Salvati Manni identify the Satake boundary with

```text
Z1 Z2 Z3=b1 b2 b3=0,
```

whose irreducible components are the twelve smooth elliptic boundary curves. Hence `Q0,Q1` are Satake-boundary components.

For both remaining cases set

```text
B=Z/H.
```

Then

```text
e=2: B=E, g(B)=1, deg(psi_j)=28l;
e=4: B->E is etale degree2, g(B)=1, deg(psi_j)=56l.
```

A boundary component fixes one factor at a four-cusp `G`-orbit. Modulo `H`, that orbit splits into exactly two values. Therefore the seven supported nodes on one zero quartic place all their dangerous-packet branches over two specific factor-quotient values.

For `e=2`,

```text
7*(8l)=56l=2*(28l),
```

so those two specific degree-`28l` fibers are completely reduced, unramified, and saturated: exactly `28l` supported points in each.

For `e=4`, the residual etale double cover doubles the supported points on `B`:

```text
2*7*(8l)=112l=2*(56l),
```

so the two corresponding degree-`56l` fibers are likewise completely reduced, unramified, and saturated: `56l` points in each.

No per-node concentration, even split of the `8l` branches at a node, or orientation relation between `Q0,Q1` is assumed.

Evidence:
- `BEAUVILLE-SATAKE-BOUNDARY-SOURCE-NOTE.md`
- `GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md`
- matching certificate/verifier.

## 9. Current exact missing invariant

The `000707` equality packet is now constrained by all of:

```text
e in {2,4};
Psi birational of bidegree (28l,28l) or (56l,56l);
for each zero quartic, two specific factor fibers are completely saturated and unramified.
```

This still does not decide branch-by-branch which of the two `H`-orbit values is selected. Distinct exceptional landing keys do not currently identify that residual product-cover sheet.

The next leaf is therefore

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.
```

Required input: compute the restriction to the carrier pullback of the remaining nontrivial character(s) of the free `G0` cover, or derive an algebraic incompatibility between the two birational factor maps and the two saturated fiber pairs. Do not assume per-node concentration or equal splitting.

## 10. Audit checkpoint

The retained shared PR is now at roughly the repository warning boundary measured from the last hostile-audited exact head. Before another large substantive retained wave, freeze an exact head and run an intermediate delta-bounded `stage32mb` hostile audit. Scratch exploration may continue off the shared retained surface if permitted by the active contract.

## Firewalls

- geometric arbitrary-branch uniform-ray support core remains `864`;
- only the dangerous equality-packet core is `768`;
- `000707` remains open for both `e=2` and `e=4`;
- support-span five is not fully closed;
- arbitrary unequal exceptional coefficients remain open;
- P6 sectors remain open;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and finite Picard enumeration is unreleased;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
