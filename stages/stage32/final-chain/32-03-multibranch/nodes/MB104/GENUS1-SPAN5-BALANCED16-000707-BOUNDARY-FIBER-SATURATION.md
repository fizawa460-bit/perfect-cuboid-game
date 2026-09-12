# Stage32 MB104 — `000707000f0f` boundary-fiber saturation

Status: **RETAINED CURRENT-FRONTIER EQUIVARIANT-LIFT REDUCTION / TWO FACTOR FIBERS SATURATED PER ZERO QUARTIC / e=2,4 BOTH OPEN / NO CREDIT**

## Scope

Work only with the remaining MB104 equality-packet support orbit

```text
Sigma = 000707000f0f,
node-type counts = (7,7,0),
D_l = 7lH - 4l sum_(p in Sigma) E_p,
d = r_odd = R8 = M = 112l,
l>=1.
```

At each of the fourteen supported nodes the dangerous packet has exactly

```text
8l
```

distinct normalization branches, all FSM-minimal and odd.

The retained Beauville reduction leaves only

```text
e=2 or e=4.
```

This leaf strengthens those two cases using the fact that the two zero-pairing quartics are actual Satake-boundary components.

## 1. The rank-two subgroup common to both cases

Let `s1,s2` be the two singular stabilizer involutions occurring in the support and put

```text
H=<s1,s2> ~= (Z/2)^2.
```

Let `Z` be the connected product-cover component from equality rigidity.

- If `e=2`, the component stabilizer is exactly `K=H`, hence

```text
B:=Z/H = E,
g(B)=1.
```

- If `e=4`, the component stabilizer is the full group `G`.  The retained Hurwitz certificate says every nontrivial element other than `s1,s2` acts freely on `Z`.  Therefore

```text
B:=Z/H -> E:=Z/G
```

is an etale double cover, so again

```text
g(B)=1.
```

The two product projections descend to

```text
psi_1, psi_2 : B -> C8/H.
```

The factor quotient has genus zero, and quotienting source and target by the same `H` does not change projection degree. Thus

```text
e=2: deg(psi_j)=28l,
e=4: deg(psi_j)=56l.
```

Write this common degree as `n`.

## 2. The two zero quartics are Satake-boundary components

The retained exact zero-quartic equations are

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0.
```

Each is a smooth elliptic quartic containing exactly eight box nodes.  The published modular source identifies

```text
b1 b2 b3 = Z1 Z2 Z3 = 0
```

with the Satake boundary, whose irreducible components are the twelve smooth elliptic boundary curves.  Hence `Q0` and `Q1` are boundary components.

For `000707000f0f`, each zero quartic contains exactly seven supported nodes and omits one box node:

```text
|Sigma cap Q0|=|Sigma cap Q1|=7.
```

A boundary component is the image of a `G`-orbit of vertical or horizontal lines with one factor fixed at a cusp.  For a component of singular type `s_j`, its four-cusp `G`-orbit splits into exactly two `H`-orbits.  Therefore, on the factor which is fixed along that boundary component, every product-cover point above a node of `Qj` maps under the relevant `psi_k` to one of exactly two marked values

```text
q_j^+, q_j^- in C8/H ~= P1.
```

No claim is made that all branches at one box node choose the same one of these two values.

## 3. Equality-packet branches fill both fibers completely

Fix one of `Q0,Q1`, and let `psi` denote the projection whose factor coordinate is fixed along that boundary component.

There are seven supported nodes on `Q`.  Downstairs on `E` they contribute

```text
7*(8l)=56l
```

distinct normalization points.

### Case `e=2`

Here `B=E` and `deg(psi)=28l`.  Thus the `56l` supported branch points lie in

```text
psi^{-1}(q^+) union psi^{-1}(q^-),
```

whose total scheme length is

```text
2*(28l)=56l.
```

At every supported odd branch the same order-two stabilizer occurs in source and target before taking the `H` quotient, so the quotient projection is unramified at the corresponding point.  Therefore the `56l` distinct supported points already account for the entire scheme length of the two fibers.

Hence both fibers are completely reduced and completely occupied by supported branches:

```text
#psi^{-1}(q^+) = #psi^{-1}(q^-) = 28l,
```

and every point in those two fibers is unramified.

Equivalently, the unresolved two-value sheet assignment of the seven-node packet must split the `56l` branches exactly `28l/28l`.

### Case `e=4`

Now `B->E` is etale of degree two and `deg(psi)=56l`.  Each of the `56l` downstairs supported branch points has two lifts to `B`, giving

```text
112l
```

distinct points over the same two marked factor values.  Their union of fibers has total scheme length

```text
2*(56l)=112l.
```

The same local inertia cancellation makes all of these points unramified for `psi`.  Hence again both fibers are completely reduced and completely occupied:

```text
#psi^{-1}(q^+) = #psi^{-1}(q^-) = 56l.
```

Thus every zero quartic forces a two-fiber saturation equality in both remaining component-degree cases.

## 4. What this gains, and why it still does not close `000707`

The earlier Hurwitz-capacity leaf only controlled totals over all marked values of a stabilizer type.  The boundary geometry now localizes half of that information to the **specific pair of factor-quotient values attached to each zero quartic**.

For each of `Q0,Q1`:

```text
e=2: two specific fibers of degree 28l are both fully unramified and full;
e=4: two specific fibers of degree 56l are both fully unramified and full.
```

This is a genuine joint-lift constraint, but by itself it is not contradictory.

In the `e=2` case the current retained local data do not determine, branch by branch, which of the two `H`-orbit values is chosen.  The exact saturation condition only forces the global `28l/28l` split.  Distinct exceptional landing keys do not currently identify this binary product-cover sheet.

In the `e=4` case the residual etale double cover `B->E` supplies the additional sheet, and the same two-fiber saturation is numerically compatible with the full-degree lift.

Therefore the next missing invariant is no longer coarse Riemann--Hurwitz capacity.  It is the **residual product-cover sheet/character assignment** on the branches, or an equivalent algebraic relation between the two factor maps `psi_1,psi_2` that forbids the required saturated fibers.

## Firewalls

- No per-node concentration at `q^+` or `q^-` is asserted.
- No claim that the `8l` branches at one node split evenly is asserted.
- No divisibility of a local branch count beyond the retained `8l` packet is used.
- No orientation claim (`Q0` vertical/horizontal versus `Q1`) is required for the saturation result.
- `e=2` remains open.
- `e=4` remains open.
- `000707000f0f` remains in the MB104 equality-packet frontier.
- The arbitrary-branch geometric uniform-ray frontier remains `864`.
- MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain zero.
- No merge authorization.
