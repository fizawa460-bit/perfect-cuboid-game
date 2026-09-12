# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / UNIFORM P5 GEOMETRIC CORE 864 / MB104 MINIMAL-BRANCH EQUALITY-PACKET CORE 768 / SIZE48 EQUALITY PACKETS CLOSED / 000707 e=2,4 BOUNDARY-FIBER SATURATION / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of a standalone `R8<d/4+O(1)` inequality remains frozen unless a genuinely new lever appears.

The most recent hostile-audited retained boundary is

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`. Everything below that depends on later retained continuation is unaudited until the next hostile checkpoint.

## 1. Hard-sector and semantic scope

Potentially infinite sectors remain

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
N>=14.
```

`span` means the projective span of the box-node support, not containment of the carrier curve.

For the displayed uniform genus-one P5 Picard ray,

```text
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
d=112l,
l>=1.
```

The MB104 dangerous packet is stronger than the Picard class:

```text
r_i=M_i=8l on all 14 supported nodes,
all branches FSM-minimal (A,B)=(1,1), m=1,
R=R8=M=r_odd=d=112l.
```

The distinction between the class and this branch packet remains load-bearing.

## 2. Geometric uniform-ray support core

Exact P5 support reduction closes incidence `24`, `20`, `19`, `15`, and all five incidence-`14` ambient orbits. Incidence16 originally left four balanced support orbits

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

The last orbit is closed for every `l>=1` by two-zero-quartic gluing monodromy

```text
17+12*sqrt(2).
```

Hence the current **geometric** uniform-ray support population, allowing arbitrary exceptional branch partitions compatible with the class, is

```text
864 = 48+48+768
```

on

```text
0000770000ff,
00007b0000ff,
000707000f0f.
```

This geometric population is still `864`.

## 3. Exhausted zero-quartic route

For every retained zero-pairing elliptic quartic `Q`,

```text
O_Q(D_l) ~= O_Q.
```

Primitive degree-seven calculations on the two size48 orbits and on `000707000f0f` give

```text
h0(A)=124,
h1(A)=4,
rank(jet_4)=220,
```

with explicit nonzero restrictions and stabilizer transport proving all retained zero quartics nonfixed for every `l>=1`.

Thus negative low-degree pairing, static landing avoidance, hidden Pic0, null-union gluing, and zero-quartic fixedness are exhausted on the geometric 864 core.

## 4. Global singularity walls

For a hypothetical integral genus-one member,

```text
p_a(D_l)=1+168l^2+56l,
Delta_total=168l^2+56l.
```

Lu--Miyaoka gives

```text
n_ordinary_node_or_triple >= max(0,112l-224).
```

Miyaoka 2008 single-curve orbibundle BMY gives no bound on `l`, and the sharp A1 conductor coefficient `delta>=r-1` is insufficient by itself.

## 5. Beauville equality rigidity

On the dangerous packet,

```text
g=1,
r_odd=d.
```

Let `Y` be the connected Beauville pullback and `Z` a connected component after pulling to

```text
P=C8 x C8,
g(C8)=5,
P->X=P/G0,
G0~=(Z/2)^2.
```

If

```text
e=deg(Z->Y) in {1,2,4},
```

then equality in the product-cover canonical/Riemann--Hurwitz estimate forces both product projections

```text
Z -> C8
```

to be finite etale of equal degree

```text
14el.
```

## 6. Current node-type quotient and size48 closure

The three singular stabilizer types are the unique zero among `b1,b2,b3`. Exact current-mask replay gives

```text
mask             b1=0  b2=0  b3=0
0000770000ff       14     0     0
00007b0000ff       14     0     0
000707000f0f        7     7     0.
```

For `000707`, two used outside involutions exclude `e=1`, leaving only

```text
e=2 or e=4.
```

For the two one-type size48 masks, the quotient by the singular involution is elliptic. Freitag--Salvati Manni identify the factor quotient with

```text
E0: y^2=x^3-x,
j(E0)=1728,
End^0(E0)=Q(i).
```

The two product projections descend to equal-degree isogenies of degree `14el`. Since `7` is inert in `Q(i)`, equal degree forces a common nontrivial 7-primary kernel, so the pair map has generic degree divisible by `7`. The same modular map factors through the box/Kummer quotient with generic degree `e` or `2e`, one of

```text
1,2,4,8.
```

Contradiction. Therefore the dangerous equality packet is impossible on both size48 support orbits for every `l>=1`.

The two populations must remain distinct:

```text
geometric arbitrary-branch uniform-ray core: 864;
MB104 dangerous equality-packet core:       768.
```

The latter now consists only of

```text
000707000f0f   size 768.
```

## 7. `000707` coarse Hurwitz regimes

For `000707`, the retained quotient-Hurwitz regimes are

```text
e=2: degree 28l genus1 -> P1 with 8 involutory marked values;
e=4: degree 56l genus1 -> P1 with 6 involutory marked values.
```

In both cases the supported minimal branches exhaust the total unramified capacity. Coarse one-factor Riemann--Hurwitz does not contradict either case.

## 8. New exact refinement: Satake-boundary two-fiber saturation

The two zero quartics are

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0.
```

Each is a smooth elliptic quartic with eight box nodes, seven of which are supported by `000707`.

Freitag--Salvati Manni identify the Satake boundary as the divisor

```text
Z1 Z2 Z3 = b1 b2 b3 = 0
```

with twelve smooth elliptic components. Hence `Q0,Q1` are Satake-boundary components.

Let the two used singular involutions be `s1,s2` and put

```text
H=<s1,s2> ~= (Z/2)^2.
```

For both remaining cases define

```text
B=Z/H.
```

Then

```text
e=2: B=E, g(B)=1, deg(psi_j)=28l;
e=4: B->E is etale degree 2, g(B)=1, deg(psi_j)=56l,
```

where

```text
psi_1,psi_2:B->C8/H ~= P1
```

are the descended factor maps.

A Satake-boundary component fixes one factor at a four-cusp `G`-orbit. Because `H` contains its singular stabilizer, that four-cusp orbit splits into exactly two `H`-orbits. Therefore every product-cover point above a node of a fixed zero quartic lands over one of two specific factor-quotient values.

For one zero quartic the seven supported nodes contribute `56l` normalization points downstairs.

### `e=2`

```text
7*(8l)=56l = 2*(28l).
```

All those points are unramified for the fixed-factor quotient map, so they exhaust the two fibers. Each of the two specific fibers is reduced and contains exactly

```text
28l
```

supported points.

### `e=4`

The residual etale double cover `B->E` doubles the `56l` downstairs points:

```text
2*7*(8l)=112l = 2*(56l).
```

Again the two specific fibers are completely reduced and saturated, each with

```text
56l
```

supported points.

This is stronger than the earlier total-capacity statement: each zero quartic now localizes its entire seven-node branch population to a **specific pair of completely saturated factor fibers**.

Evidence:

- `BEAUVILLE-SATAKE-BOUNDARY-SOURCE-NOTE.md`
- `GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md`
- matching certificate and fail-closed verifier.

### Why this is not yet closure

The retained local data do not determine, in the `e=2` case, which one of the two `H`-orbit values is chosen by each individual branch. The exact result forces only the global

```text
28l / 28l
```

split. No per-node concentration or even split is assumed.

For `e=4`, the residual etale double cover is numerically compatible with the same two-fiber saturation.

Thus both `e=2` and `e=4` remain open.

## 9. Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER`:

1. identify the residual product-cover sheet/character carried by each supported branch after quotienting by `H=<s1,s2>`;
2. equivalently, compute the restriction to the carrier pullback of the remaining nontrivial character(s) of the free `G0` cover;
3. test whether that character can realize the two saturated fiber pairs simultaneously for `psi_1,psi_2`;
4. do not assume per-node branch-value concentration or equal splitting;
5. if the character cannot yet be computed, isolate the exact missing modular divisor/2-torsion datum rather than reopening exhausted finite-landing, zero-quartic, fixed-jet, or coarse Hurwitz routes.

Genus-one support-span P6 and genus-zero full-span P6 remain active in parallel.

## Firewalls

- the Picard-class geometric support core is still 864 when arbitrary branch partitions are allowed;
- only the MB104 minimal-branch equality-packet core is 768;
- `000707000f0f` remains open for `e=2` and `e=4`;
- support-span five is not fully closed;
- arbitrary unequal exceptional coefficients remain open;
- P6 sectors remain open;
- no population-wide finite degree window is proved;
- MB104 is incomplete and finite Picard enumeration is unreleased;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
