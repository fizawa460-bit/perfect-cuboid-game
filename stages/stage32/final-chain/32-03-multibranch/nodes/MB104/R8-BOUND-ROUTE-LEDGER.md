# MB104 — minimal-cusp branch count `R8` route ledger

Status: **ACTIVE RESEARCH ROUTING / NO FINITE WINDOW / NO CREDIT**

The branchwise Freitag--Salvati Manni lemma reduced MB104 to

```text
d <= 16g - 16 + 4 R8,
```

where `R8` is the number of normalization branches over the 48 box nodes of minimal cusp type `(A,B)=(1,1)`. To obtain a finite degree window it is enough to prove

```text
R8 <= alpha*d + beta,  alpha < 1/4,
```

or an absolute bound. This ledger records which obvious routes do and do not currently provide that input.

## 1. Purely local A1 landing data — dominated

The retained A1 adapter gives minimal branches

```text
gamma_lambda(t)=(t,lambda*t,lambda^2*t)
```

with arbitrary nonzero exceptional landing parameter `lambda`. Distinct `lambda` values give pairwise distinct resolved landing points, so arbitrarily many minimal branches at one node are compatible with the local A1/FSM model without forcing strict-transform delta there.

Therefore no bound `R8<=48`, no bounded multiplicity per node, and no `R8` bound from MB101/MB102 local data is available.

Source lock:
`stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150`.

## 2. Garcia-Fritz--Urzua symmetric differential degree — wrong-side multiplicity

Garcia-Fritz--Urzua, *Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Math. Z. 2020, Theorem 3.1, gives for the perfect-cuboid surface a pulled-back symmetric-differential degree

```text
-deg(C) + (E.C') + 4g(C) - 4.
```

If this is negative, the image is omega-integral. In the smooth-at-nodes case this yields their Corollary 3.3

```text
d <= 4g + 44.
```

For the multibranch receiver the exceptional term is `M=E.D`, so outside the explicitly omega-integral locus the same degree computation controls `d` only through `M`; it does not bound `M` or `R8` from above. Their multi-differential refinement (Theorem 3.5 / Corollary 3.6) instead gives lower exceptional-incidence bounds, e.g. `C.E>=8` for the relevant rational curves.

Thus this route does not supply `alpha<1/4` for `R8`.

External source: arXiv:1804.07671, Theorem 3.1, Corollaries 3.3 and 3.6.

## 3. Stoll--Testa rank-3 genus-5 fibrations — exact simple-intersection wall

Stoll--Testa, *Curves on the surface of cuboids* (Math. Comp. 2026), Section 5, constructs six genus-5 fibrations from the six rank-3 quadrics. For each rank-3 quadric `Q`, its base locus on the cuboid surface consists of eight singular points `B_Q`, and on the minimal resolution its fiber class satisfies

```text
2 F_Q = H - sum_{i in B_Q} E_i.
```

The six base sets partition the 48 nodes exactly:

- Lemma 3 characterizes every singular point by vanishing of the three coordinates occurring in one of the six rank-3 quadrics;
- there are exactly 48 singular points;
- each of the six rank-3 singular loci meets the surface in exactly eight points;
- hence the six 8-point sets, whose union is the singular locus, are disjoint.

For an effective integral strict transform `D`, the fiber class is nef, so

```text
0 <= 2 D.F_Q = d - sum_{i in B_Q} M_i.
```

Thus for each rank-3 block

```text
sum_{i in B_Q} M_i <= d.
```

Summing the six partition blocks gives only

```text
M <= 6d,
R8 <= R <= M <= 6d.
```

This has slope `6`, far above the required `<1/4`. Therefore **base-locus intersection nonnegativity from the six rank-3 fibrations cannot close MB104**.

The full Section 5 has 28 genus-5 fibrations (`6 + 2*11`). The remaining rank-4 fibrations may still be useful only if one proves an additional branchwise ramification/tangent/landing charging lemma. Merely knowing that complementary fiber classes sum to a hyperplane class, or that some rank-4 maps have eight-node base loci, does not by itself multiply-charge `R8` strongly enough.

External source: Stoll--Testa, DOI `10.1090/mcom/4238`; accepted/public manuscript Section 2 and Section 5. Upstream verification source: `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/Section5_fibrations.log` blob `9cfef75aa58335655d6ae3e78597f5924b6c2433`.

## 4. Current literature ceiling

The 2026 Stoll--Testa paper still asks whether all geometric-genus `<=1` curves are the known set. Its Lemma 21 proves only lower exceptional-incidence bounds:

```text
rational non-conic: C.E >= 8,
genus one:          C.E >= 4.
```

Bruin--Thomas--Varilly-Alvarado show that rational curves outside known exceptions must meet at least seven nodes spanning the ambient `P^6`, genus-one curves at least two nodes, and asymptotically that only finitely many genus `0/1` curves pass through at most 13 nodes. These constrain **distinct node support**, not the number `R8` of normalization branches of one minimal cusp type over those nodes.

So no presently source-locked literature result in this chain supplies the needed `R8` upper bound.

## 5. Live route

The next useful statement must be genuinely branch-sensitive. The currently viable forms are:

1. a global branchwise ramification/conductor inequality in which every `(A,B)=(1,1)` branch contributes to a bounded divisor with coefficient large enough to force `R8 < d/4 + O(1)`;
2. a multi-fibration lemma proving that every minimal cusp branch is forced to be ramified/critical for sufficiently many of the 28 genus-5 maps, followed by summed Riemann--Hurwitz;
3. a modular/symmetric-differential construction with extra node/tangent vanishing that decreases the `8k` pole charge of minimal cusp branches.

None of these statements is proved here. The rank-3 simple-intersection route and local A1 route should not be rerun as if they were still open.

## Firewalls

- MB104 remains incomplete.
- No finite degree window is released.
- No finite Picard enumeration is released.
- No receiver/effectivity/final-milestone/theorem/endpoint or Perfect Cuboid credit.
- No merge authorization.
