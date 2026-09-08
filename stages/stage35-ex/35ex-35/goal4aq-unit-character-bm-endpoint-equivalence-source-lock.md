# Stage35-EX Goal4AQ source lock — full unit-character Brauer orthogonality is endpoint-equivalent

Scope: continue provisionally after exact-head-green Goal4AP while audited authority remains V74 / Goal4AK. Goal4AQ evaluates the infinite Q-defined unit-character filtration piece of `Br_a(U)` on the source-marked adelic relaxation from Goal4AO. The result is an exact equivalence, not a nonexistence theorem: orthogonality to the full unit-character layer is equivalent to existence of an actual source-marked rational endpoint, hence to existence of a Stage35 E1 counterexample under the already hostile-audited 35EX-31 population adapter.

No E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence credit is granted.

## 1. Exact retained inputs

Goal4AP source-locks the extended-Picard filtration for the open receiver `U={h!=0}` and proves

```text
K := H^0(UPic(Ubar)) = O(Ubar)^*/kbar^* ~= Z^3,
Br_a(U) ~= H^2(Q,UPic(Ubar)),
```

with `K` a trivial Galois lattice. The unit-cohomology filtration subgroup is

```text
B_unit := image(H^2(Q,K) -> H^2(Q,UPic(Ubar)))
        ~= H^2(Q,K) / image(d2^(0,1)).
```

Goal4AP also proves `B_unit` is infinite and that the two Goal4Y classes A,B do not exhaust `Br_a(U)`.

Goal4Y and 35EX-22 identify three explicit Q-defined units on the affine open:

```text
u1 = p+x,   (p+x)(p-x)=1,
u2 = q+y,   (q+y)(q-y)=1,
u3 = w+z,   (w+z)(w-z)=1.
```

They need not be identified term-by-term with an arbitrary SNF basis of `K`. For every individual Q-defined unit `u in K^G`, the homomorphism of trivial lattices

```text
Z -> K, 1 |-> u
```

induces `H^2(Q,Z) -> H^2(Q,K)`, so the full subgroup `B_unit` contains the image of every character-unit class needed below.

Goal4AO fixes the source-marked adelic relaxation

```text
A_src^loc = U_PC(R)^+ x U_PC(Q_2)^src x product'_{l odd} U_PC(Q_l),

U_PC(Q_2)^src = {P : v2(x)>0, v2(y)>0, v2(x)!=v2(y)}.
```

The hostile-audited 35EX-31 reverse adapter proves that a positive rational endpoint satisfying this source marking reconstructs a genuine Stage35 Master-Hit/E1-counterexample source tuple; modulo source-pair swap and positive scaling/edge permutation, the hypothetical populations are equivalent.

## 2. Character-unit class and local evaluation

For a place `v`, let

```text
Xi_v = Hom_cts(G_{Q_v}, Q/Z).
```

J. S. Milne, *Arithmetic Duality Theorems*, second edition, Appendix A, Theorem A.3, identifies the cup product

```text
H^0(G_{Q_v}, Qbar_v^*) x H^2(G_{Q_v}, Z)
   -> H^2(G_{Q_v}, Qbar_v^*) = Br(Q_v)
```

with a pairing `<a,chi>` satisfying the local reciprocity formula

```text
inv_v <a,chi> = chi(Art_v(a)).                       (LR)
```

For a global finite-order character

```text
chi in Hom_cts(G_Q,Q/Z) ~= H^2(Q,Z)
```

and a Q-defined unit `u`, functoriality of the map `K[0] -> UPic(Ubar)` gives a class

```text
beta(chi,u) in B_unit subset Br_a(U).
```

At a local point `P_v`, its evaluation modulo constants is represented by the cup product

```text
< u(P_v), chi_v > in Br(Q_v).                       (EVAL)
```

Changing the Q-defined representative of the geometric unit by a constant `c in Q^*` changes `(EVAL)` by the constant class `<c,chi>`. Its sum of local invariants is zero by global reciprocity, so the adelic functional is well-defined on `Br_a(U)`.

The possible `d2^(0,1)` ambiguity causes no loss. The Brauer--Manin evaluation functional on `H^2(Q,K)` is the pullback of the functional on its image `B_unit`, hence it automatically annihilates `image(d2^(0,1))`. Therefore

```text
P orthogonal to B_unit
=> sum_v inv_v <u(P_v),chi_v> = 0                  (BM-u)
```

for every global finite-order `chi` and every Q-defined unit `u`, whether or not a particular `H^2(Q,K)` representative survives injectively in the quotient.

## 3. Global class field theory converts (BM-u) to an idele statement

J. S. Milne, *Class Field Theory*, v4.03, Chapter V:

- Theorem 5.3 constructs the global Artin map as the product of the local Artin maps and gives reciprocity;
- Remark 5.7(a) states that for a number field the global Artin map on the idele class group is surjective and its kernel is exactly the identity connected component;
- Lemma 5.9 gives, for Q, the explicit topological factorization

```text
I_Q ~= Q^* x R_{>0} x product_p Z_p^*,
C_Q ~= R_{>0} x product_p Z_p^*.
```

For an adelic point `P=(P_v)` and a Q-defined unit `u`, form the idele

```text
a(u,P) = (u(P_v))_v in I_Q.
```

This is an idele because an adelic point is integral at almost all finite places and a regular invertible function on the chosen integral model is a local unit outside finitely many places.

By `(LR)` and Theorem 5.3, equation `(BM-u)` is exactly

```text
chi(Art_Q([a(u,P)])) = 0
```

for every finite-order global character `chi`. Such characters separate the profinite group `Gal(Q^ab/Q)`, hence

```text
Art_Q([a(u,P)]) = 1.
```

Remark 5.7(a) gives

```text
[a(u,P)] in C_Q^0.
```

By Lemma 5.9, `C_Q^0=R_{>0} x {1}`. Equivalently there are unique data

```text
r_u in Q^*,   t_u in R_{>0}
```

such that

```text
u(P_p)=r_u               for every finite prime p,
u(P_infinity)=r_u*t_u.                                  (CONST-u)
```

Thus full unit-character orthogonality forces each Q-defined unit value to be one single rational number simultaneously at every finite place.

## 4. The three visible units reconstruct all endpoint coordinates over Q

Apply `(CONST-u)` to

```text
u1=p+x, u2=q+y, u3=w+z,
```

and write the resulting rationals as `r1,r2,r3 in Q^*`.

Because the conjugate products are exactly one, at every finite place

```text
p+x=r1, p-x=r1^(-1),
q+y=r2, q-y=r2^(-1),
w+z=r3, w-z=r3^(-1).
```

Therefore every finite local component has the same rational coordinates

```text
x0=(r1-r1^(-1))/2,   p0=(r1+r1^(-1))/2,
y0=(r2-r2^(-1))/2,   q0=(r2+r2^(-1))/2,
z0=(r3-r3^(-1))/2,   w0=(r3+r3^(-1))/2.          (REC)
```

In particular, the Q_2 component `P_2` equals this rational tuple inside `Q_2^6`. Since `P_2` lies on `U_PC(Q_2)`, the rational quantities in `(REC)` satisfy

```text
p0^2=1+x0^2,
q0^2=1+y0^2,
z0^2=x0^2+y0^2,
w0^2=1+x0^2+y0^2
```

as equalities in Q: a rational number that is zero in Q_2 is zero in Q.

The source-marked Q_2 condition also gives

```text
x0 != 0, y0 != 0,
v2(x0)>0, v2(y0)>0, v2(x0)!=v2(y0).
```

The open condition supplies the remaining nonzero coordinates. Replacing the six rational coordinates by their absolute values preserves all square equations and all 2-adic valuations, producing a positive rational source-marked endpoint. By hostile-audited 35EX-31, this reconstructs a genuine Stage35 E1 counterexample.

Hence

```text
(A_src^loc)^(B_unit) nonempty
=> positive source-marked U_PC(Q) nonempty.          (FORWARD)
```

## 5. Converse and exact equivalence

Conversely, a positive source-marked rational point `P in U_PC(Q)` defines its diagonal adele. Every Brauer class, in particular every class in `B_unit`, has zero sum of local invariants on a diagonal rational point by global Brauer reciprocity. Thus

```text
positive source-marked U_PC(Q) nonempty
=> (A_src^loc)^(B_unit) nonempty.                    (REVERSE)
```

Combining `(FORWARD)` and `(REVERSE)` gives the exact equivalence

```text
(A_src^loc)^(B_unit) != empty
iff U_PC(Q)^src,+ != empty
iff Stage35 E1-counterexample population != empty.   (AQ-EQUIV)
```

The last equivalence is exactly the hostile-audited 35EX-31 population adapter, not a new endpoint assertion.

## 6. Route consequence

The infinite algebraic unit-character layer is therefore a *complete but endpoint-equivalent* obstruction on the source-marked local relaxation. It does not simplify the remaining arithmetic problem:

- proving its Brauer--Manin set empty is equivalent to proving that no Stage35 E1 counterexample exists;
- constructing a point in its Brauer--Manin set is equivalent to constructing an actual source-marked rational endpoint;
- finite truncations of the character family cannot inherit this equivalence without a separate finite-generation/conductor theorem.

Thus the Brauer route has reached an exact endpoint-equivalence blocker at the full unit-character level. This does not rule out genuinely different information from the Picard-lift A/B quotient, transcendental Brauer classes, or a distinct non-Brauer route, but it forbids treating the infinite unit-character family as an easier finite Brauer completion problem.

## 7. Credit firewall

Certified provisionally only:

- exact character/unit local-evaluation adapter for the Q-defined units;
- global class-field conversion of full character orthogonality into constant rational finite-place unit values;
- exact reconstruction of a source-marked rational endpoint from the three visible unit values;
- equivalence `(AQ-EQUIV)` and the resulting endpoint-equivalence blocker.

Not certified:

- emptiness or nonemptiness of either side of `(AQ-EQUIV)`;
- a finite character subset sufficient for the full equivalence;
- the full transcendental Brauer group;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
