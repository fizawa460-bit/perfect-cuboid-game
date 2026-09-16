# Stage32 MB104 — `000707000f0f` residual sheet character

Status: **RETAINED CURRENT-FRONTIER CHARACTER REDUCTION / e=2 VS e=4 EQUIVALENT TO ZERO VS NONZERO PIC0[2] CLASS / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Scope

Work only with the remaining dangerous MB104 equality packet on

```text
Sigma = 000707000f0f,
node-type counts = (7,7,0),
d=r_odd=R8=M=112l,
l>=1.
```

The hostile-audited retained frontier leaves exactly

```text
e=2 or e=4.
```

Let the two used singular involutions be `s1,s2` and set

```text
H=<s1,s2> ~= (Z/2)^2.
```

The full modular deck group is

```text
G ~= (Z/2)^3,
```

and the Beauville free subgroup `G0` is an index-two `(Z/2)^2`.  Since `s1,s2` lie in the same outside coset of `G0`,

```text
h=s1*s2 in G0,
H cap G0=<h>.
```

Put

```text
R=C8/H.
```

The retained joint-pair leaf gives

```text
R ~= P1.
```

The quotient `G/H` has order two and acts on `R`; put

```text
S=R/(G/H)=C8/G ~= P1.
```

Write

```text
q:R -> S
```

for this residual double cover.

## 1. The two branch points of `q` are the absent stabilizer type

Let `s3` be the third singular node-stabilizer involution, absent from the support.  The node-type adapter says the three singular involutions are three distinct elements of the outside coset `G\G0`.

A point of `R=C8/H` is fixed by the nontrivial class of `G/H` exactly when a lift to `C8` is fixed by an element of the nontrivial coset `G\H`.  Among those elements, the only elements with fixed points relevant to the box-node singular locus are the absent singular type `s3`; elements in `G0` are free on `C8`, and the fourth outside involution is the retained free outside type.

The involution `s3` has eight fixed points on `C8`.  Since `s3 notin H`, its stabilizer meets `H` trivially, so these eight points form exactly two `H`-orbits.  Therefore the residual involution on `R~=P1` has exactly two fixed points

```text
a,b in R,
```

and

```text
q:R->S
```

is branched exactly at their images, which we again denote by `a,b` when no ambiguity results.

This is the factor-quotient form of the two absent-type branch values in the retained Hurwitz packet.

## 2. Both `e` cases produce a degree-`56l` map `phi:E->S`

Let `E` be the normalization of the hypothetical downstairs carrier.

### Case `e=2`

The component stabilizer is `K=H`.  The retained quotient curve is

```text
Q=Z/H=E,
```

and either descended product projection gives

```text
psi:E -> R,
deg psi=28l.
```

Define

```text
phi=q o psi:E -> S.
```

Then

```text
deg phi=56l.
```

### Case `e=4`

Now the component stabilizer is all of `G`.  Put

```text
Q=Z/H.
```

The residual quotient is the connected etale double cover

```text
pi:Q -> E=Z/G,
deg pi=2.
```

Each factor projection gives an equivariant map

```text
psi:Q -> R,
deg psi=56l,
```

for the residual involutions on `Q` and `R`.  Hence `q o psi` descends through `pi` to

```text
phi:E -> S
```

with

```text
deg phi=56l.
```

Thus both surviving cases have the same downstairs degree-`56l` factor-quotient map.

## 3. Half-fibers over the two absent-type values

For `e=2`, the retained Hurwitz calculation on `psi:E->R` exhausts its ramification at the eight `H`-branch values belonging to `s1,s2`.  Hence `psi` is unramified over the two residual branch points `a,b` of `q`.  Since `q` has ramification index two there,

```text
phi^*(q(a)) = 2 A,
phi^*(q(b)) = 2 B,
```

where `A,B` are reduced effective divisors of degree `28l`.

For `e=4`, the retained Hurwitz certificate already says that the two absent-type values are completely ramified for the downstairs degree-`56l` map.  Thus the same formulas hold:

```text
phi^*(q(a)) = 2 A,
phi^*(q(b)) = 2 B,
deg A=deg B=28l.
```

Because the two doubled divisors are fibers of one map,

```text
2(A-B) ~ 0.
```

Therefore

```text
eta := O_E(A-B) in Pic^0(E)[2].
```

This `eta` is the residual sheet character.

## 4. Fiber-product criterion

Normalize the base change of the residual modular double cover:

```text
T = Norm(E x_S R).
```

Locally one may write `q` as adjoining a square root of a rational function with odd divisor at the two branch points of `q`.  Pulling that function back by `phi` gives divisor

```text
2A-2B.
```

Hence the normalized pullback is an etale double cover of `E`, and its isomorphism class is the two-torsion line bundle

```text
eta=O_E(A-B).
```

Equivalently:

```text
eta=0      <=> T = E disjoint-union E,
eta!=0     <=> T -> E is connected etale of degree two.
```

Now identify `T` with the residual `G/H` quotient of the normalized full modular pullback.

- For `e=2`, the full pullback has two components interchanged by `G/H`; after quotienting each by `H`,

```text
T = E disjoint-union E.
```

Thus

```text
eta=0.
```

- For `e=4`, the full pullback component is `G`-stable and

```text
T=Q=Z/H -> E=Z/G
```

is the retained connected etale double cover.  Thus

```text
eta is nonzero in Pic^0(E)[2].
```

Therefore the two remaining component-degree cases are exactly classified by one concrete divisor class:

```text
e=2  <=> eta=0,
e=4  <=> eta!=0.
```

## 5. The two factor projections must give the same class

There are two product projections.  Repeat the construction for each and write

```text
phi_1,phi_2:E->S,
phi_j^*(q(a))=2A_j,
phi_j^*(q(b))=2B_j,
eta_j=O_E(A_j-B_j).
```

Both normalized fiber products

```text
Norm(E x_(S,phi_j) R)
```

are not arbitrary double covers: each is the same residual `G/H` quotient of the same normalized modular pullback.  Consequently

```text
eta_1=eta_2=:eta.
```

This is the first exact joint-character constraint beyond coarse Hurwitz capacity and joint-pair birationality.

The remaining problem is now concrete:

```text
compute eta_1 and eta_2 from the exact factor-grid / theta data,
or prove they cannot coincide with the required zero/nonzero status.
```

## What this gains

The unresolved branchwise binary sheet label is no longer an unconstrained combinatorial choice.  It is controlled globally by a single element

```text
eta in Pic^0(E)[2],
```

and the two factor maps are required to recover the same element.

This reduction also separates the two surviving cases sharply:

```text
e=2: the residual character is trivial;
e=4: the residual character is a nonzero two-torsion point.
```

No choice of local branch labels may change this global criterion.

## Firewalls

- This leaf does not compute which element of `Pic^0(E)[2]` occurs in the `e=4` case.
- It does not yet exclude `eta=0` or `eta!=0` from the exact node/grid data.
- It does not assert per-node concentration among the two `H`-orbit values.
- It does not assert an equal split of the `8l` branches at any box node.
- `e=2` remains open.
- `e=4` remains open.
- `000707000f0f` remains in the dangerous equality-packet frontier.
- The arbitrary-branch geometric core remains `864`.
- MB104, span5, receiver, theorem, endpoint, and Perfect-Cuboid credit remain zero.
- No merge authorization.
