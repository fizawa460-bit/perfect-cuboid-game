# Stage35-EX Goal4AO source lock — canonical 2-adic source marking does not rescue the known two-class Brauer route

Scope: continue provisionally from Goal4AN while audited authority remains V74 / Goal4AK. Goal4AO consumes the hostile-audited 35EX-31 primitive-source endpoint equivalence and tightens the exact surface-open adelic population at the unique load-bearing source place `2`. It tests only the fixed independent algebraic classes A and B. It does not compute the full algebraic/transcendental Brauer group, prove Brauer--Manin nonemptiness for the discrete global E1 source population, prove E1, or close Stage35.

## Audited source-population input

35EX-31 PR #1583 hostile re-audit PASS review `5120329847` at exact head `5598342cf54f2827a5d8e1cae025c4c19e142d29`; exact-head aggregate `33952582056 / 101270003525` SUCCESS; merged as `8211bb0ef80de61ecf39c3b97743c58f1193187a` after the accepted population-equivalence line was retained.

The audited 35EX-31 result is:

- on the source-labelled normalized endpoint `(1,x,y)`, source primitivity gives `v2(x)>0` and `v2(y)>0`;
- `d3^2=x^2+y^2` forces `v2(x)!=v2(y)`;
- reduced `x=V1/U1`, `y=V2/U2` then reconstruct the two primitive odd/even Pythagorean source triples, Master-Hit data, E1 counterexample data, and canonical `h,g0` normalization channels;
- for every positive rational perfect cuboid the three edge `v2` valuations are pairwise distinct, so the unique minimum-v2 edge gives a canonical scaling/permutation gauge;
- modulo source-pair swap on the Stage35 side and positive scaling/edge permutation on the endpoint side, the hypothetical populations are equivalent.

This is population equivalence only. It is not an existence/nonexistence theorem.

## Present exact surface coordinates

Use

```text
U_PC:
p^2=1+x^2,
q^2=1+y^2,
z^2=x^2+y^2,
w^2=1+x^2+y^2,
x*y*p*q*z*w != 0.
```

In this chart the canonical source-local 2-adic marked subset is

```text
U_PC(Q_2)^src = {P in U_PC(Q_2): v2(x)>0, v2(y)>0, v2(x)!=v2(y)}.
```

This is a necessary local relaxation of the audited global source-marked population. No claim is made that an arbitrary adelic point satisfying these placewise conditions globalizes to a primitive Stage35 source tuple.

Define the source-marked adelic relaxation

```text
A_src^loc = U_PC(R)^+ x U_PC(Q_2)^src x product'_{l odd} U_PC(Q_l),
```

where the restricted product uses integral `U_PC(Z_l)` components for almost all odd primes.

## Goal4AN/35EX-22 anchor

Goal4AN source-locks the 35EX-22 smooth affine specialization

```text
P*=(x,y,p,q,z,w)=(272/225,0,353/225,1,272/225,353/225).
```

It lies outside `U_PC` only because `y=0`. Its first ratio satisfies

```text
v2(272/225)=4>0.
```

35EX-22 proves that at every fixed local place one may keep `x=272/225`, `p=353/225` and choose a nonzero `y` sufficiently close to zero so that `q,z,w` have local square roots near `1,272/225,353/225`, the resulting point lies in `U_PC`, and the deformation can be taken in an arbitrarily small prescribed neighborhood of `P*`.

At `Q_2`, every sufficiently small nonzero `y` has arbitrarily large positive `v2(y)`. Therefore choose the 2-adic deformation so small that

```text
v2(y)>4.
```

Then

```text
v2(x)=4>0,
v2(y)>0,
v2(x)!=v2(y),
```

so the deformed point lies in `U_PC(Q_2)^src` and the normalized edge `1` is the unique minimum-v2 edge.

## Known Brauer classes and local constancy

Retain exactly the two independent classes from Goal4Y with the fixed explicit representatives used in Goal4AN:

```text
A = (-1,(p+x)(q+y)(w+z)) + (2,(q+y)(w+z)(z+q))  mod Br_0(U),
B = (-1,F_B),  F_B=A31/B31                      mod Br_0(U).
```

Goal4AN already proves a genuine restricted-product adelic point on `U_PC` with positive real component orthogonal to `<A,B>` by:

1. using local constancy of A and B in finite bad-place deformations near `P*`;
2. using the positive real deformation near `P*`;
3. using integral `U_PC(Z_l)` points and spread-out vanishing outside a finite set;
4. comparing all local invariants to the diagonal rational evaluation at `P*` and applying global Brauer reciprocity.

The Goal4AO modification changes only the 2-adic bad-place choice: choose it inside the same common local-constancy neighborhood but with `v2(y)>4`. Such a choice exists because every 2-adic neighborhood of `y=0` contains nonzero elements of arbitrarily large valuation. Hence A and B retain exactly their `P*` invariants at `2` while the point simultaneously satisfies the audited source marking.

All other local components are chosen exactly as in Goal4AN. Therefore for `alpha=A` and `alpha=B`, every invariant still agrees with the corresponding diagonal `P*` invariant, and

```text
sum_v inv_v alpha(Q_v)=0.
```

Thus

```text
(A_src^loc)^{<A,B>} != empty.
```

## Route consequence

The canonical minimum-v2/source-marking condition from the hostile-audited primitive reverse adapter does not rescue a Brauer--Manin obstruction from the two currently explicit independent classes A and B. In particular, the exact real invariant `inv_infinity(B)=1/2` remains compensable at finite places even after the required 2-adic source marking is imposed.

This is stronger than Goal4AN only in local-population semantics. It does **not** prove that the actual discrete global primitive Stage35 source population has a Brauer--Manin point, and it does not show that the full `Br_a(U)` or transcendental Brauer group is exhausted by A and B.

The next legal Brauer-side question is therefore completeness: compute enough of `H^2(Q,UPic(Ubar))` / the algebraic unit-symbol layer to determine whether A and B exhaust the relevant algebraic quotient, or isolate additional classes. A separate preserved non-Brauer route remains legal if completeness is blocked.

## Credit firewall

Certified provisionally only:
- the audited 35EX-31 canonical source marking is correctly transported to the present `U_PC` chart;
- one restricted-product adelic point exists in the source-marked local relaxation `A_src^loc` orthogonal to the known span `<A,B>`;
- the known two-class span cannot close E1 merely by adding the canonical 2-adic source marking.

Not certified:
- exact adelization/globalization of the discrete primitive source population;
- `Br_a(U)/Br_0(U)=<A,B>`;
- transcendental Brauer computation;
- complete finite local images;
- Brauer--Manin obstruction or nonobstruction for the full actual E1 source population;
- E1, R29, Stage35, endpoint, or Perfect Cuboid closure.
