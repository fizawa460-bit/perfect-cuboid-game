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

or an absolute bound. This ledger records which routes do and do not currently provide that input.

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

For the multibranch receiver the exceptional term is `M=E.D`, so the degree computation controls `d` only through `M`; it does not bound `M` or `R8` from above. Their refinements also give lower exceptional-incidence bounds, not the required upper multiplicity bound.

Thus this route does not supply `alpha<1/4` for `R8`.

External source: arXiv:1804.07671, Theorem 3.1 and Corollaries 3.3/3.6.

## 3. Stoll--Testa rank-3 genus-5 fibrations — exact simple-intersection wall

For each of the six rank-3 quadrics, the corresponding genus-5 fibration has

```text
2 F_Q = H - sum_{i in B_Q} E_i,
```

and the six 8-node base sets partition the 48 nodes. Nefness gives

```text
sum_{i in B_Q} M_i <= d,
```

hence after summing

```text
M <= 6d,
R8 <= R <= M <= 6d.
```

The slope is `6`, so base-locus intersection nonnegativity alone cannot close MB104. The full 28-fibration system remains useful only with an additional branchwise ramification/tangent charging mechanism; simple unit charging has already been shown insufficient.

External source: Stoll--Testa, DOI `10.1090/mcom/4238`; upstream verification `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`.

## 4. Other retained global/local walls

Current exact walls include:

- Hodge projection: `R8<=sqrt(6d^2+96d-192g+192)`;
- one-fibration local jet: minimal cusp type alone does not force ramification;
- all 28 genus-5 fibrations with unit charging: at best `R8<=d+2g-2`; slope `<1/4` would need aggregate branch charge `q>112`;
- powers of BTVA `omega_7`: hyperplane vanishing / A1 regularization ratio `1/2`, no extra slack;
- BTVA 13-form order-two principal parts: rank 3 at every node and saturation after three landing directions;
- downstairs conductor: `R8<=p_a(C)-g+48`, locally sharp, while standard Castelnuovo in `P^6` is quadratic;
- Beauville odd-contact cover: `r_odd` even and `r_odd>=d-4g+4`, a lower bound in the wrong direction;
- Weierstrass/transvection layer: parity-only and blind to adding branch pairs.

No item supplies `R8<=alpha*d+beta` with `alpha<1/4`.

## 5. Fixed finite local jets — general saturation wall

The order-two wall is not exceptional. In the A1 resolution chart

```text
x=s, y=s*t, z=s*t^2, E={s=0},
```

fix nonzero `lambda`. For every fixed `J>=0` and arbitrary distinct constants `c`, the branches

```text
s=tau,
t=lambda+c*tau^(J+1)
```

are distinct, meet `E` transversely with multiplicity one, preserve the FSM-minimal leading type `(A,B)=(1,1)`, and have the same branch `J`-jet.

Hence any fixed finite local condition portfolio that factors through a bounded jet depth gives identical evaluation vectors on arbitrarily many repeated minimal branches. Increasing branch multiplicity need not increase local rank.

At fixed symmetric order `m`, the most singular `ds^m` coefficient is a degree-`m` landing polynomial `P_m(t)/(2^m s^(m/2))`, so repeated branches with the same `lambda` also repeat the leading principal-part row. Higher subleading coefficients can probe higher jets, but any fixed finite collection still has some maximum jet depth and is subject to the same construction.

Verdict: **fixed finite local jet depth alone is dominated as an `R8` multiplicity counter**. This does not exclude a global jet-collision bound, high-contact conductor/intersection charge, or adaptive jet depth growing with multiplicity/degree.

Artifacts:
`FINITE-JET-MULTIPLICITY-SATURATION-WALL.md`,
`FINITE-JET-MULTIPLICITY-SATURATION-CERTIFICATE.json`,
`verify_mb104_finite_jet_multiplicity_saturation.py`.

## 6. Current literature ceiling

The 2026 Stoll--Testa paper still leaves the classification of all geometric-genus `<=1` curves open. Its low-genus and low-span results constrain distinct support / low degree but do not source-lock an upper bound on normalization multiplicity `R8`. BTVA likewise gives powerful low-support finiteness while leaving the `N>=14` high-support sector.

So no presently retained literature result in this chain supplies the needed `R8` upper bound.

## 7. Live route

After the finite-jet saturation wall, the next useful statement must be branch-sensitive **and global**. Viable forms are now:

1. a cuboid-specific linear conductor/arithmetic-genus/intersection inequality with slope strong enough for `R8<d/4+O(1)`;
2. a global collision lemma bounding how many minimal branches can share a fixed jet, or charging their forced high contact to a degree-linear divisor;
3. an adaptive/unbounded jet or symmetric-differential construction whose depth grows with multiplicity/degree and has controlled global dimension/vanishing;
4. high-span geometry directly restricting genus-zero full-span or genus-one span-5/6 carriers.

The pure local A1 route, simple fibration intersection, order-two portfolio, and fixed finite local-jet generalization should not be rerun as if still open.

## Firewalls

- MB104 remains incomplete.
- No finite degree window is released.
- No finite Picard enumeration is released.
- No receiver/effectivity/final-milestone/theorem/endpoint or Perfect Cuboid credit.
- No merge authorization.
