# Stage14 toolbox — local 2-descent / five-column interface

This page is the reusable entrypoint for the closed Stage14 `s5` local algebra. It does **not** prove a new local theorem. It repackages merged `s5b`–`s5f` and the merged `s6-01` global-witness handoff so main/s workers can apply the local system without reopening five historical stages.

## 1. Primitive Euclid support columns and the orientation adapter

For primitive opposite-parity `m>n>0`, define the orientation-free Euclid core

```text
A=m
B=n
C=m-n
D=m+n
E=m^2+n^2

even leg = 2AB
difference leg = CD
hypotenuse = E.
```

At every odd prime the five columns `A,B,C,D,E` are pairwise coprime. Therefore every odd bad prime belongs to exactly one moving column.

The historical s5 local-row derivation uses

```text
S = CD = m^2-n^2
X = 2AB = 2mn
H = E  = m^2+n^2.
```

Hence in the **s5 local orientation**

```text
A or B  -> p|X -> label 13 if selected
C or D  -> p|S -> label 12 if selected
E       -> p|H -> label 23 if selected.
```

Some later Stage14/s6 documents use the swapped orientation

```text
S = 2AB
X = CD
H = E.
```

In that orientation the same five columns remain valid, but the `S/X` row labels swap:

```text
A or B  -> p|S -> label 12 if selected
C or D  -> p|X -> label 13 if selected
E       -> p|H -> label 23 if selected.
```

**Rule:** the local row is attached to the actual `S/X/H` role in the covering equations. Never attach `12/13` permanently to the names `m,n,m-n,m+n` without first fixing orientation.

## 2. Symmetric covering coordinates

Use

```text
z1=d1*u1^2
z2=d2*u2^2
z3=d3*u3^2
```

with

```text
z1-z2=S^2
z3-z1=X^2
z3-z2=H^2
d1*d2*d3 = square class.
```

At an odd bad prime, the nontrivial support-parity labels are

```text
12=(1,1,0)
13=(1,0,1)
23=(0,1,1).
```

For a **selected** odd bad prime, valuation parity forces

```text
p|S -> label 12
p|X -> label 13
p|H -> label 23.
```

## 3. Odd-prime row dispatcher

Write selected-prime unit parts as `di=p^ei ai`.

### Selected rows

```text
p|S / label12:
  chi(a1*a2)=+1
  chi(a3)=+1

p|X / label13:
  chi(a1*a3)=+1
  chi(-a2)=+1

p|H / label23:
  chi(a2*a3)=+1
  chi(a1)=+1
```

Using the product-square relation on the unit parts, the compressed selected form is

```text
S / 12 : chi(a3)=+1
X / 13 : chi(a2)=+1 AND chi(-1)=+1
H / 23 : chi(a1)=+1.
```

Hence a selected odd `X`-prime requires `p == 1 mod 4`.

### Unselected rows

If the bad prime is omitted from all three `d_i`, then

```text
p|S : chi(d3)=+1
p|H : chi(d1)=+1
p|X : chi(d2)=+1 OR chi(-d2)=+1.
```

Therefore

```text
p|X, p==3 mod4 : automatic
p|X, p==1 mod4 : chi(d2)=+1.
```

Do not use the selected row for an unselected bad prime or vice versa.

## 4. Reciprocity data actually needed

Because each odd bad prime has one factor column, all odd rows are functions of a finite quadratic-character matrix among squarefree pieces of the five columns. Quadratic reciprocity reduces the off-diagonal data to one triangular half plus the mod-4 residue vector.

This is the correct input for large-sieve / dispersion work. It is not an independent random-sign model once an exact physical/global witness has already forced algebraic relations.

## 5. Prime 2

The exact squareclass group is

```text
Q2*/Q2*^2 = {1,3,5,7,2,6,10,14}.
```

For

```text
A2=2^alpha*u,
B2=2^beta*v,
```

with odd `u,v`, define

```text
epsilon(u)=(u-1)/2 mod 2
omega(u)=(u^2-1)/8 mod 2.
```

Then

```text
(A2,B2)_2 = (-1)^[epsilon(u)epsilon(v)+alpha*omega(v)+beta*omega(u)].
```

The product-square condition gives 64 ordered triples before the covering equation is imposed.

For the normalized Stage14 Kummer triple

```text
[q], [q-1], [q+t^2],   v2(t)>=2,
```

exactly eight states occur:

```text
(1,1,1)
(3,7,5)
(5,1,5)
(7,7,1)
(2,1,2)
(6,7,10)
(10,1,10)
(14,7,2).
```

This eight-state membership test is the complete covering-specific `Q2` row.

## 6. Full local admissibility recipe

For one primitive Euclid base and one supported full-2-descent class:

1. Fix the oriented covering and identify the actual `S,X,H` roles.
2. Factor odd support through `m,n,m-n,m+n,m^2+n^2`.
3. Apply the orientation adapter to map each factor column to `S`, `X`, or `H`.
4. For each odd bad prime determine selected versus unselected state.
5. If selected, route by `S/X/H` to `12/13/23` and apply the selected row.
6. If unselected, apply the corresponding unselected row.
7. Check the prime-2 squareclass triple against the exact eight-state table.
8. Only after all rows pass may the class be called **locally admissible**.

The result is the complete merged local 2-descent character system.

## 7. Handoff to the global-witness side

Merged `s6-01` uses the swapped orientation

```text
S=2mn,
X=(m-n)(m+n),
H=m^2+n^2
```

and proves that an actual global small-point witness has signed squarefree kernels

```text
d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c
```

with

```text
a|rad(S)
b|rad(X)
c|rad(H)
```

and exactly 16 sign/2-adic `tau` patterns. Its odd support refines to the **same five Euclid columns**. The orientation adapter above is therefore mandatory when comparing its `S/X` edge packets to historical s5 local-row names.

The safe implication is

```text
physical hit
 -> global small-point witness
 -> globally soluble descent class
 -> locally admissible five-column character state.
```

The converse arrows are not available.

## 8. Hard boundaries

Never infer any of the following from this interface alone:

```text
local admissible => globally soluble
locally soluble cover => rational point
nonempty Selmer class => physical cuboid hit
selected-prime row => unselected-prime row
X-unselected automatic at p=3 mod4 => X-selected possible at p=3 mod4
five-column identity => same S/X labels across orientations
finite local density saving => global/height saving
```

The local system is a strong **upper-majorant / filtering interface**. Stage14's post-local wall is precisely what remains after this local algebra is closed.
