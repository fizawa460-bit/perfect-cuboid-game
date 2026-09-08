# Stage35-EX Goal4AP source lock — the open receiver has an infinite algebraic Brauer unit-character layer

Scope: continue provisionally after Goal4AO while audited authority remains V74 / Goal4AK. This leaf computes a structural consequence of the already exact Goal4Y extended Picard complex. It determines that the two explicit Picard-lift classes A and B do not exhaust `Br_a(U)`: the Q-defined rank-3 unit lattice contributes an infinite algebraic Brauer filtration piece. This is not a Brauer--Manin obstruction, does not compute the transcendental Brauer group, and grants no E1 or Stage35 closure.

## Exact repo input

Goal4Y fixes the open receiver `U={h!=0}` and its extended Picard complex. Exact retained data:

- source lock: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift-source-lock.md`, blob `2c5cc829b508a917f071a624f6a3bb9419864a77`;
- artifact: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json`, blob `9351c92747365838cda92d98854ad136df1847d5`.

Goal4Y proves

```text
H^0(UPic(Ubar)) = K = kbar[U]^*/kbar^* ~= Z^3,
H^1(UPic(Ubar)) = Pic(Ubar) ~= Z^35,
```

and the Galois action on `K` is trivial. Three visible Q-defined units are

```text
p+x,
q+y,
w+z,
```

with conjugate products equal to `1`. Goal4Y also proves

```text
H^1(Q,Pic(Ubar)) ~= Z/2 x Z/2
```

for the relevant exact Galois action, and both generators survive the unit transgression and lift to two independent algebraic Brauer classes A and B.

The rational smooth point `(x,y,p,q,z,w)=(3/4,0,5/4,1,3/4,5/4)` is exact. Therefore the `Br_a(U)` identification below applies.

## Literature locks

### Extended Picard / algebraic Brauer identification

Mikhail Borovoi and Joost van Hamel, *Extended Picard complexes and linear algebraic groups*, J. reine angew. Math. 627 (2009), 53--82, Corollary 2.20(ii).
Canonical preprint: `https://arxiv.org/abs/math/0612156`.

For smooth geometrically integral `X`, there is a canonical injection

```text
Br_a(X) -> H^2(k,UPic(Xbar)),
```

which is an isomorphism when `X(k)` is nonempty. Hence here

```text
Br_a(U) ~= H^2(Q,UPic(Ubar)).
```

### Hypercohomology spectral sequence

Use the standard hypercohomology spectral sequence for a bounded-below two-term Galois complex (for example Weibel, *An Introduction to Homological Algebra*, §5.7.10 and the group-hypercohomology specialization §6.1.15):

```text
E2^(p,q)=H^p(Q,H^q(UPic))  =>  H^(p+q)(Q,UPic).
```

Since `UPic` has cohomology only in rows `q=0,1`, total degree two has the exact two-step filtration

```text
0 -> coker(d2^(0,1): Pic(Ubar)^G -> H^2(Q,K))
  -> H^2(Q,UPic(Ubar))
  -> ker(d2^(1,1): H^1(Q,Pic(Ubar)) -> H^3(Q,K))
  -> 0.                                                     (FILT)
```

There are no higher differentials touching these total-degree-two pieces because only rows `q=0,1` exist.

Goal4Y's exact two-step lift computation says both generators of `H^1(Q,Pic(Ubar)) ~= (Z/2)^2` have zero unit transgression. Thus the right term in `(FILT)` is exactly

```text
Z/2 x Z/2,
```

and A,B realize this Picard-lift quotient piece.

### Cohomology of the trivial integer lattice

J. S. Milne, *Class Field Theory*, v4.03, Chapter II, Lemma 3.3 and the continuous/profinite discussion in §4.
Canonical source: `https://www.jmilne.org/math/CourseNotes/CFT.pdf`.

For a finite group `G`, Lemma 3.3 obtains from

```text
0 -> Z -> Q -> Q/Z -> 0
```

and the vanishing of positive cohomology of the uniquely divisible module `Q` the canonical isomorphism

```text
H^2(G,Z) ~= Hom(G,Q/Z).
```

For profinite `G` with discrete coefficients, continuous cohomology is the direct limit over finite quotients. Therefore for the absolute Galois group

```text
H^2(Q,Z) ~= Hom_cts(G_Q,Q/Z).
```

Since `K ~= Z^3` with trivial action,

```text
H^2(Q,K) ~= Hom_cts(G_Q,Q/Z)^3.                  (UNIT-H2)
```

This group is infinite; already the infinitely many quadratic characters of `G_Q` provide infinitely many order-2 elements.

## The left filtration piece is infinite

`Pic(Ubar) ~= Z^35`, so its invariant subgroup `Pic(Ubar)^G` is a finitely generated free abelian group of rank at most 35.

Continuous `H^2(Q,K)` is torsion (Milne, Chapter II, Corollary 4.3). Therefore the image of

```text
d2^(0,1): Pic(Ubar)^G -> H^2(Q,K)
```

is a finitely generated torsion abelian group, hence finite.

But `(UNIT-H2)` contains infinitely many independent/distinct quadratic-character elements. Quotienting by the finite `d2^(0,1)` image leaves an infinite group, with an infinite 2-primary part:

```text
coker(d2^(0,1)) is infinite.                      (UNIT-INF)
```

Combining `(FILT)`, Goal4Y's surviving right-hand `(Z/2)^2`, and Borovoi--van Hamel gives

```text
Br_a(U) is infinite.
```

More precisely, `Br_a(U)` has an infinite unit-cohomology filtration subgroup whose quotient by that subgroup contains the two-dimensional Picard-lift piece represented by A and B.

## Consequence for the current route

The previous working question "do A and B exhaust the algebraic Brauer quotient?" is answered negatively before any further finite search:

```text
<A,B> != Br_a(U).
```

There is no finite algebraic-Brauer-basis completion obtained merely by adding finitely many further Goal4Y-like Picard lifts. The live Brauer-side problem is instead the evaluation of the infinite Q-defined unit-character layer on the source-marked adelic population.

This leaf does **not** identify a canonical explicit cyclic/quaternion representative for every unit-character class. The abstract hypercohomology injection is enough for the infinitude statement, but local evaluation requires a separate exact character/unit-symbol adapter and class-field-theoretic pairing computation.

Arsenal comparison after exact object identification:

- provisional `S33-PW07` is routing-only here: it requires an exact common cocycle/torsor semantics and does not itself compute this unit-character layer;
- provisional `LIT-PW15` is also routing-only: its open descent/etale-Brauer terminal requires an exact torsor/twist family and complete adelic computation, which are not supplied by Goal4AP.

## Credit firewall

Certified provisionally only:
- exact total-degree-two UPic filtration specialized to the retained Goal4Y data;
- the unit-cohomology left piece is infinite, including infinitely many 2-primary classes;
- `Br_a(U)` is infinite;
- A/B are not a complete algebraic Brauer basis.

Not certified:
- explicit representatives for the full unit-character layer;
- its finite-place or real local evaluation images;
- its Brauer--Manin pairing on the actual source population;
- the transcendental Brauer group;
- a Brauer--Manin obstruction or nonobstruction for E1;
- E1, R29, Stage35, endpoint, or Perfect Cuboid closure.
