# Stage32 MB104 — H6 finite monodromy / Nielsen-passport shallow gate — 2026-09-18

Status: **H6 SHALLOW GATE FAIL / PARKED / CYCLE 2 COMPLETE / H9 NEXT / NO MATHEMATICAL CREDIT**

## Gate tested

H6 asks whether the active `000707` balanced packet can be compressed into a finite monodromy/Nielsen object, independent of `l`, without reintroducing the retracted branch-concentration assumption and with a reverse adapter back to the original carrier.

No Nielsen enumeration is run before this adapter gate passes.

## Retained e=2 branch-cycle interface

For one factor in the active e=2 geometry,

```
psi:E->P1
```

has degree

```
n=28l
```

and is ramified only over eight fixed branch values.

At a branch value `q`, etaleness of the product-cover base change gives only simple ramification, hence the branch-cycle type is

```
2^(r_q) 1^(u_q),
u_q+2r_q=28l.
```

The retained passport also gives

```
sum_q u_q=112l,
sum_q r_q=56l,
u_q even.
```

For the first factor, the exact node table groups the eight values into four residual pairs with total unramified populations

```
32l, 24l, 56l, 0.
```

The `56l` pair is forced to split `28l+28l`, and the zero pair is fixed.

## A growing family already exists before choosing permutations

For the first residual pair, every value

```
u_(+a)=4l+2i,
u_(-a)=28l-2i,
0<=i<=12l
```

satisfies the retained degree bounds, evenness, and pair total `32l`.

For the second pair, every

```
u_(+b)=2j,
u_(-b)=24l-2j,
0<=j<=12l
```

satisfies the corresponding constraints.

Keep

```
u_(+u0)=u_(-u0)=28l,
u_(+v0)=u_(-v0)=0.
```

Then automatically

```
sum u_q=112l
```

and, with `r_q=(28l-u_q)/2`,

```
sum r_q=56l.
```

The retained residual-pair sign condition is also automatic: in the first pair

```
(u_(+a)+u_(-a))/2=16l
```

is even, and in the second pair it is `12l`, also even, so the two local sign bits in each pair agree.

Thus the **retained aggregate interface alone** permits at least

```
(12l+1)^2
```

distinct aggregate branch-cycle-type vectors.

This is not a claim that every such vector is realized by an actual connected cover. It is enough for the shallow gate: current source-locked data do not eliminate them, so an exact reduction is not allowed to discard them without a new theorem.

## Why a full Nielsen tuple does not repair finiteness

A genuine degree-`28l` Nielsen tuple consists of eight permutations in `S_(28l)`, with the displayed cycle types, product one and transitive generated subgroup.

Passing from aggregate cycle types to actual permutations adds data; it does not turn the growing family into an `l`-independent finite object.

The roadmap stop condition therefore triggers before enumeration:

```
cycle data grow freely with l.
```

## Reverse-adapter failure

The carrier packet contains normalization branches at specific box nodes. The finite product-cover quotient additionally needs to know which fixed lift each branch reaches.

That pointwise branch-to-fixed-lift information is not encoded by the aggregate `u_q,r_q` vector. Different unresolved branch allocations can therefore have the same reduced passport.

If H6 compresses those configurations together, a conclusion at the compressed Nielsen level cannot be reversed source-completely to the original carrier. If H6 keeps all allocations, its state space grows with `l` and no uniform finite reduction has been achieved.

## Decision

```
degree-l Nielsen description: available in principle
l-independent finite passport: FAIL
reverse adapter: FAIL
H6 shallow gate: FAIL
H6: PARKED
Cycle 2: COMPLETE, no DEEP candidate
finite degree window: NOT PROVED
next shallow gate: H9 uniform stable-base / Zariski-ray obstruction
```

The Class-3 roadmap records the Cycle-2 rescore and the next candidate order `H9, H10, H11`.

No heavy computation, conductor-sign guess, MB104 closure, receiver, theorem, endpoint, Perfect-Cuboid, or merge credit is claimed.
