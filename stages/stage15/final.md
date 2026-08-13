# Stage15 final self-contained causal comparison verdict

**Bundle ID:** `STAGE15-FINAL-SELF-CONTAINED-20260813-R01`

**Status:** fresh-audit candidate. This document is the Stage15 roadmap-item-8 synthesis target. It does not reopen the closed Stage15-6 internal search.

## Executive verdict

Stage15 compares primitive canonical cuboids with exactly two integral face diagonals under one common geometric cutoff, before and after imposing an integral space diagonal.

Let
\[
M_2(B)=\#\mathcal B_2(B)
\]
count the ambient exactly-two population with `R<=B`, and let
\[
N_2(B)=\#\mathcal A_2(B)
\]
count the subpopulation for which the space diagonal `R` is an integer.

The final Stage15 picture has two complementary theorem species.

First, the **strongest quantitative comparison** is
\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]
This follows by combining the Stage14 whole-family numerator bound
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]
with the Stage15 ambient asymptotic
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]
The fixed-power numerator loss is therefore inherited from Stage14. Stage15 does not claim that the exponent `1/2` was rederived from its local squareclass mechanism.

Second, Stage15 supplies an **independent causal zero-density theorem**. In exact toric coordinates, imposing an integral space diagonal is precisely equality of two Gaussian-norm squareclasses. A fixed-prime local squareclass sieve on the same physical measure proves independently that
\[
\boxed{
\frac{N_2(B)}{M_2(B)}\longrightarrow0.
}
\]
The exact local rejection is of order `4/p` at good split primes, so this internal primewise mechanism naturally accumulates only logarithmically. Stage15-6 proves no internal fixed `delta>0` and no `sigma>0`.

Thus Stage15 answers both comparison questions:

1. **How sparse are the integral-space-diagonal survivors?** At least polynomially sparse by the certified Stage14 numerator plus Stage15 denominator comparison.
2. **What arithmetic mechanism inside the Stage15 ambient model explains that survivors have density zero?** Equality of coupled Gaussian norm squareclasses, detected by infinitely many split-prime valuation-parity filters on the same toric physical measure.

Neither conclusion proves existence or nonexistence of a perfect cuboid.

---

## 1. Scope, physical objects, and common cutoff

A physical object is a primitive canonical cuboid
\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]
Its geometric space-diagonal length is
\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}.
\]

Let `I_ab,I_ac,I_bc` denote the three face-square predicates. Define
\[
\mathcal B_2(B)
=
\{(a,b,c):R\le B,\ I_{ab}+I_{ac}+I_{bc}=2\},
\]
and
\[
\mathcal A_2(B)
=
\{C\in\mathcal B_2(B):R\in\mathbf Z\}.
\]
Then
\[
M_2(B)=\#\mathcal B_2(B),\qquad N_2(B)=\#\mathcal A_2(B).
\]

On `A_2`, write `d=R`. Then exactly
\[
R\le B\iff d\le B.
\]
This identifies the Stage15 numerator with the Stage14 physical exactly-two population under the same cutoff. No constant-factor height substitution is used in the final ratio theorem.

Every exactly-two object has one unique shared edge between its two integral faces. Choosing that shared edge as `e` and ordering the other two legs by `x<y` gives the Stage15 shared-edge counting model without extra object multiplicity.

---

## 2. Ambient exactly-two theorem

The shared-edge surface is
\[
X:\quad u^2=e^2+x^2,\qquad v^2=e^2+y^2.
\]
Its smooth split toric resolution is
\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad \rho(Y)=6.
\]
The Stage15 height `R` is itself an anticanonical adelic height on `Y`.

Stage15-2b proves that the third-face-square locus is a geometrically integral degree-two thin image and is lower order. Consequently
\[
\boxed{
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0.
}
\]

For the three canonical shared-edge directions `j=a,b,c`, it also proves
\[
M_{2,j}(B)\sim C_jB(\log B)^5,
\qquad C_j>0.
\]

The external theorem interfaces used here are limited to:

- Batyrev--Tschinkel for anticanonical counting on smooth projective toric varieties;
- Huang for Manin--Peyre equidistribution and adelic-neighbourhood counting on smooth proper split toric varieties;
- Browning--Loughran for zero density of thin subsets under the stated almost-Fano/equidistribution hypotheses.

The K3 geometry of the three-face cover is identified internally; no conjectural K3 rational-point asymptotic is used.

---

## 3. Exact survivor normal form

Use positive coprime toric pairs
\[
m>n>0,\qquad r>s>0.
\]
Define
\[
A=m^2r^2+n^2s^2=N(mr+i\,ns),
\]
\[
B=m^2s^2+n^2r^2=N(ms+i\,nr).
\]
Stage15-4 proves the exact identity
\[
G^2R^2=4AB
\]
for the primitive reconstruction gcd `G`, and hence
\[
\boxed{
R\in\mathbf Z
\iff AB\in\mathbf Z^2
\iff \operatorname{sf}(A)=\operatorname{sf}(B).
}
\]

Equivalently, there is a unique squarefree integer `k>0` and positive integers `P,Q` with
\[
A=kP^2,\qquad B=kQ^2.
\]
The common core is supported only on `2` and primes `1 mod 4`.

The positive toric parameter pair is uniquely reconstructible from the physical shared-edge incidence, so this normal form does not hide an uncontrolled parametrization multiplicity. Positivity, canonical ordering, primitiveness, the exactly-two postfilter, direction, and the exact physical height remain explicit filters.

This squareclass equality is the arithmetic event whose thinning Stage15 studies.

---

## 4. Strongest quantitative survival theorem

Stage14 final Theorem 2.1 proves, on the primitive canonical exactly-two family with integral space diagonal `d<=B`,
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]
The exact cutoff identification in Section 1 makes this the Stage15 numerator.

Combining it with the positive Stage15 ambient denominator gives
\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]
Therefore, for every fixed `delta<1/2`,
\[
\frac{N_2(B)}{M_2(B)}\ll_\delta B^{-\delta}.
\]

Directionally, because `N_{2,j}(B)<=N_2(B)` and `M_{2,j}(B)~C_jB(log B)^5`,
\[
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\varepsilon,j}
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]
This proves zero relative density in each direction, but it does not compare directional survivor constants or prove that one direction is preferentially removed.

### Quantitative non-claims

The theorem does not prove

- `N_2(B)~C B^{1/2}`;
- a matching lower bound;
- that `1/2` is the true survivor exponent;
- a strict numerator improvement `N_2(B)<<B^{1/2-delta}`;
- a perfect-cuboid statement.

Most importantly for causal accounting, the half-power input is Stage14's theorem. It is not a consequence attributed to the Stage15-6 local parity tensor.

---

## 5. Independent causal zero-density theorem

Every survivor satisfies, for every prime `p`,
\[
v_p(A)\equiv v_p(B)\pmod2.
\]

For odd inert primes `p=3 mod 4`, Gaussian norm valuations are automatically even, so the local acceptance density is
\[
\rho_p=1.
\]
They cause no thinning.

For every good split prime `p=1 mod 4`, Stage15-6 computes on the same charged physical toric measure
\[
\boxed{
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
}
\]
and
\[
\boxed{
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
}
\]

For each fixed finite set `S` of good split primes, adelic equidistribution on the same Stage15 physical measure gives
\[
M_{2,S}(B)
=
C_{M_2}
\left(\prod_{p\in S}\rho_p\right)
B(\log B)^5
+o_S(B(\log B)^5).
\]
Every survivor belongs to every local acceptance set, so
\[
\limsup_{B\to\infty}
\frac{N_2(B)}{M_2(B)}
\le
\prod_{p\in S}\rho_p.
\]

The quantifier order is essential: `S` is fixed first, then `B->infinity`. Only afterward is `S` enlarged. Since the reciprocal-prime sum over split primes diverges and `1-rho_p=4/p+O(p^-2)`,
\[
\prod_{p\in S}\rho_p\longrightarrow0.
\]
Therefore
\[
\boxed{
\frac{N_2(B)}{M_2(B)}\longrightarrow0.
}
\]

This proof is independent of the Stage15-5 ratio bound. It gives an internal explanation for zero density directly from the exact squareclass condition.

### Internal quantitative boundary

The local product over split primes through `z` has natural scale
\[
(\log z)^{-2+o(1)}.
\]
Thus this exact primewise parity mechanism is logarithmic in nature. Stage15-6 proves

```text
INTERNAL_FIXED_DELTA_PROVED=false
INTERNAL_SIGMA_PROVED=false
```

and does not claim that no future global mechanism could do better.

---

## 6. Quantitative versus causal comparison

The final Stage15 interpretation is deliberately two-column rather than a merged pseudo-proof.

| Question | Answer | Proof source |
|---|---|---|
| Is the survivor density zero? | yes | independently by Stage15-5 and Stage15-6 |
| What is the strongest certified rate? | `B^{-1/2+eps}(log B)^-5` in the survival ratio | Stage14 numerator + Stage15-2b denominator, assembled in Stage15-5 |
| What exact arithmetic condition does `R in Z` impose? | equality of two coupled Gaussian norm squareclasses | Stage15-4 |
| What internal mechanism explains zero density? | infinitely many split-prime valuation-parity filters on the same toric measure | Stage15-6 |
| Did that internal mechanism recover a fixed power? | no | Stage15-6 negative boundary |

The stronger theorem and the causal theorem are compatible because they answer different questions. Their savings are not multiplied, and one is not presented as the proof of the other.

---

## 7. Matched finite evidence

Stage15-3 exactly enumerates the common denominator through `B=100000` and finds
\[
M_2(100000)=796698,
\qquad
N_2(100000)=89,
\]
so the observed ratio is approximately
\[
1.11711\times10^{-4}.
\]
The directional survivor counts are `(33,33,23)`.

These data motivated the mechanism search and are consistent with strong thinning, but Stage15-3 explicitly refuses to infer an asymptotic survivor exponent or a directional rate from them. The final theorems above do not use an empirical slope.

The normalized real-place defect is close to flat at coarse scale in the finite census, while the arithmetic squareclass structure is highly restrictive. This observation is diagnostic only; the rigorous causal statement is the p-adic squareclass sieve.

---

## 8. Provenance and theorem firewalls

The load-bearing sources are:

1. `stages/stage15/15-2b/result.md` for the ambient toric asymptotic and exact `R` height;
2. `stages/stage15/15-3/result.md` for finite matched evidence only;
3. `stages/stage15/15-4/result.md` for the exact squareclass survivor condition and reconstruction multiplicity;
4. `stages/stage14/final.md` for the whole-family square-root numerator upper bound;
5. `stages/stage15/15-5/result.md` for the matched quantitative ratio theorem;
6. `stages/stage15/15-6-final.md` for the independent causal zero-density theorem and internal quantitative boundary;
7. `stages/stage15/15-7-controller.json` for the final synthesis contract.

The following firewalls are part of the final claim:

- the Stage14 numerator theorem is used only on `A_2`, never promoted to the ambient family;
- the Stage15-6 local sieve is on the same physical toric object measure, not on an existentially projected scalar host;
- fixed-prime asymptotics are used with the ordered limit `B->infinity` before the prime set grows;
- multiplicity-one reconstruction is accounting, not a saving;
- no squarefree core, root orientation, Pell completion, divisor fiber, or residual switch is charged again in Stage15-7;
- finite census evidence is never promoted to an asymptotic theorem.

---

## 9. Negative knowledge and future gates

The completed Stage15 program does **not** establish:

- a matching lower bound for `N_2(B)`;
- the true order of growth of `N_2(B)`;
- an asymptotic constant for `N_2(B)`;
- a Stage15-internal derivation of a fixed survival power;
- a strict sub-square-root numerator theorem beyond Stage14's `B^{1/2+o(1)}` ceiling;
- a directional survivor asymptotic;
- perfect-cuboid existence or nonexistence.

Effective growing-modulus adelic/local sieving and stronger global squareclass-correlation mechanisms are retained only as possible future external quantitative programs. They are not unfinished Stage15-6 routes and are not required for the present Stage15 causal verdict.

---

## 10. Relation to the perfect cuboid problem

A perfect cuboid has all three face diagonals integral. Stage15's main populations are exactly-two-face objects, with and without an integral space diagonal. The ambient comparison therefore studies a neighboring arithmetic population, not the perfect-cuboid set itself.

Showing that integral-space-diagonal exactly-two boxes have zero relative density does not imply that perfect cuboids do not exist. A zero-density subset may still be infinite, finite nonempty, or empty, and the exactly-three population is a different arithmetic stratum.

No statement in Stage15 changes the open existence status of perfect cuboids.

---

## 11. Final causal comparison verdict

Under the exact common physical cutoff `R<=B`:

\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5}
\]
with `C_M2>0`, while the integral-space-diagonal survivors satisfy the certified upper comparison
\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]

Independently, the extra condition `R in Z` is exactly a paired Gaussian-norm squareclass coincidence, and its split-prime valuation-parity constraints have a product density tending to zero on the same physical toric measure. Hence
\[
\boxed{
\frac{N_2(B)}{M_2(B)}\to0
}
\]
for a direct arithmetic reason internal to the Stage15 normal form.

The final interpretation is therefore:

> Imposing an integral space diagonal on primitive canonical exactly-two-face cuboids selects a zero-density arithmetic subpopulation. The strongest certified polynomial upper thinning comes from the Stage14 numerator theorem, while Stage15 independently identifies and proves a local squareclass mechanism that explains zero density but does not internally recover that fixed power.

This is the Stage15 causal comparison verdict. It is not a perfect-cuboid existence theorem.

---

## 12. R01 audit boundary

R01 is intended to be self-contained at the declared provenance level: all load-bearing populations, cutoffs, main theorem statements, the exact normal form, the local density formula, the ordered-limit mechanism, and the theorem-species separation are stated here. External literature is invoked only through the explicit Stage15-2b theorem interfaces above.

A fresh `Stage15-7-audit` must still check:

- theorem-species separation;
- physical population and `R<=B` cutoff;
- reconstruction multiplicity;
- external theorem contracts;
- local-density and quantifier order;
- no double charge/cross-promotion;
- finite evidence separation;
- completeness of the provenance manifest;
- whether any known note is load-bearing.

Until that audit passes, this is a final-bundle **candidate**, not a closed Stage15 final.
