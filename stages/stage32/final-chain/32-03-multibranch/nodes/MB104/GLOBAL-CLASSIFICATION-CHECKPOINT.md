# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / UNIFORM P5 GEOMETRIC CORE 864 / MB104 MINIMAL-BRANCH EQUALITY-PACKET CORE 768 / SIZE48 CLOSED FOR THE EQUALITY PACKET BY CM INERT-7 / 000707 ACTIVE / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of a standalone `R8<d/4+O(1)` inequality remains frozen unless a genuinely new lever appears.

The most recent hostile-audited retained boundary is

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`. Everything below that depends on later retained continuation is unaudited until the next hostile checkpoint.

## 1. Hard-sector semantics

The active potentially infinite sectors remain

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
N>=14.
```

`span` is the projective span of the box-node support. It is not a containment statement for the carrier curve.

For the displayed uniform genus-one P5 Picard ray,

```text
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
d=112l,
l>=1.
```

The MB104 dangerous formal packet is stronger than the divisor class alone:

```text
r_i=M_i=8l at all 14 supported nodes,
all branches FSM-minimal (A,B)=(1,1), m=1,
R=R8=M=r_odd=d=112l.
```

The distinction between the Picard class and this branch packet is load-bearing in the current checkpoint.

## 2. Support classification and the geometric uniform-ray core

Exact node-spanned P5 hyperplane incidence distribution:

```text
14:1248, 15:256, 16:27, 19:48, 20:48, 24:28.
```

For the displayed uniform ray, incidence `24`, `20`, `19`, `15`, and all five incidence-14 ambient orbits are closed by retained fixed-component arguments.

Incidence16 originally left four balanced support orbits

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

The orbit `00070b000f0f` is closed for every `l>=1` by the exact two-zero-quartic gluing monodromy

```text
17+12*sqrt(2).
```

Therefore the current **geometric uniform-ray support population**, allowing an arbitrary exceptional branch partition compatible with the class, is

```text
864 = 48+48+768
```

on

```text
0000770000ff,
00007b0000ff,
000707000f0f.
```

This geometric number remains `864` after the new CM leaf.

## 3. Zero-quartic route is exhausted on all 864 geometric survivors

For every retained zero-pairing elliptic quartic `Q`, the exact hyperflex calculation gives

```text
O_Q(D_l) ~= O_Q.
```

The two size48 orbits have four pairwise-disjoint zero quartics. Exact primitive degree-seven jet calculation gives

```text
h0(A)=124,
h1(A)=4,
rank(jet_4)=220,
rank(H0(A)->H0(Z4,O_Z4(A)))>=2.
```

Hence all four are nonfixed, and powers give nonfixedness for all `l>=1`.

For `000707000f0f`, exact primitive calculation gives

```text
h0(A)=124,
h1(A)=4,
rank(jet_4)=220,
```

plus an explicit primitive section nonzero on one zero quartic. Support-stabilizer transport gives nonfixedness of both zero quartics; powers again give all `l>=1`.

Thus negative low-degree pairing, static landing avoidance, hidden Pic0, null-union gluing, and zero-quartic fixedness are all exhausted on the geometric 864 core.

## 4. Global singularity walls retained before the new cover route

For a hypothetical integral genus-one member in the class,

```text
p_a(D_l)=1+168l^2+56l,
Delta_total=168l^2+56l.
```

Lu--Miyaoka gives the necessary condition

```text
n_ordinary_node_or_triple >= max(0,112l-224).
```

Miyaoka's 2008 single-curve orbibundle inequality gives no bound on `l` on this ray. The sharp A1 conductor inequality `delta>=r-1` is also insufficient by itself.

These remain structural constraints, not closure.

## 5. Beauville equality rigidity for the MB104 minimal-branch packet

The equality packet lies exactly on

```text
g=1,
r_odd=d.
```

Let `Y` be the connected Beauville pullback and let `Z` be one connected component after pulling to

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

then equality in the product-cover canonical/Riemann--Hurwitz estimate forces **both** projections

```text
Z -> C8
```

to be finite etale of equal degree

```text
14el.
```

This upgrades the old wrong-direction inequality `d<=r_odd` into rigid product-cover geometry on the equality face.

## 6. Current node-type quotient

The three singular stabilizer types are the unique zero among `b1,b2,b3`. Exact current-mask replay gives

```text
mask             b1=0  b2=0  b3=0
0000770000ff       14     0     0
00007b0000ff       14     0     0
000707000f0f        7     7     0.
```

Thus the two size48 supports are one-type, while `000707` is two-type.

For `000707`, the two outside involutions force the component stabilizer to meet `G0` nontrivially, so

```text
e in {2,4};
```

`e=1` is excluded.

The two surviving quotient-Hurwitz regimes are

```text
e=2: degree 28l genus1 -> P1 with 8 involutory branch values;
e=4: degree 56l genus1 -> P1 with 6 involutory branch values.
```

In both cases the `112l` supported minimal branches exhaust the full unramified capacity over the quotient branch values. Coarse Riemann--Hurwitz alone does not contradict either case.

## 7. New closure for both size48 MB104 equality packets: CM inert-7

For either size48 support all `112l` branches have one singular type `s`.

Let `K` be the product-component stabilizer, `|K|=2e`, and put

```text
B1=Z/<s>.
```

Each supported normalization branch lifts to `e` points of `Z` fixed by `s`, so

```text
#Fix_Z(s)=112el.
```

Equality rigidity also gives

```text
2g(Z)-2=112el.
```

Riemann--Hurwitz therefore forces

```text
g(B1)=1.
```

Freitag--Salvati Manni's modular/Kummer model identifies the corresponding factor quotient with

```text
E0: y^2=x^3-x,
j(E0)=1728,
End^0(E0)=Q(i),
```

and gives

```text
(E0 x E0)/H ~= B/sigma,
H~=(Z/2)^2.
```

The two etale product projections descend to equal-degree isogenies

```text
alpha1,alpha2:B1 -> E0,
deg(alpha1)=deg(alpha2)=14el.
```

Put `nu=alpha2 alpha1^{-1}` in `Q(i)^*`. Equal degree gives `Norm(nu)=1`.

The prime `7` is inert in `Q(i)`. Hence `nu` is a 7-adic unit, so `alpha1` and `alpha2` have the same nontrivial 7-primary kernel. Therefore the pair map

```text
(alpha1,alpha2):B1 -> E0 x E0
```

has generic degree divisible by `7`, and this divisibility remains after the finite `H` quotient.

But the same modular map factors geometrically as

```text
B1 -> E=Z/K -> C subset B -> B/sigma.
```

Its generic degree is `e` or `2e`, hence one of

```text
1,2,4,8.
```

This is a power of two and cannot be divisible by seven. Contradiction.

Therefore the retained MB104 uniform minimal-branch equality packet is impossible on both size48 support orbits for every `l>=1`.

Evidence:

- `BEAUVILLE-KUMMER-CM-SOURCE-NOTE.md`
- `GENUS1-SPAN5-BALANCED16-SIZE48-CM-INERT7-OBSTRUCTION.md`
- matching certificate/verifier.

### Frontier split after the CM leaf

Geometric uniform-ray supports with arbitrary branch partition:

```text
864 = 48+48+768.
```

MB104 dangerous equality-packet supports:

```text
864 -> 768,
```

with only

```text
000707000f0f   size 768
```

remaining.

Do not conflate these two populations.

## 8. Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-000707-EQUIVARIANT-LIFT`:

1. treat the `e=2` and `e=4` equality cases separately;
2. use the **joint** two-factor lift, not only one-factor Riemann--Hurwitz;
3. encode the actual seven supported nodes of each of the two stabilizer types as pairs of fixed-point orbits in the two factors;
4. test whether the capacity-saturating branch fibers can lift to one connected etale correspondence `Z subset C8 x C8`;
5. if no contradiction is obtained, isolate the exact missing equivariant/Nielsen-class datum rather than reopening exhausted local routes.

Genus-one support-span P6 and genus-zero full-span P6 remain active in parallel.

## Firewalls

- the Picard-class geometric support core is still 864 when arbitrary branch partitions are allowed;
- only the MB104 minimal-branch equality-packet core has dropped to 768;
- support-span five is not fully closed;
- arbitrary unequal exceptional coefficients remain open;
- P6 sectors remain open;
- no population-wide finite degree window is proved;
- MB104 is incomplete and finite Picard enumeration is unreleased;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
