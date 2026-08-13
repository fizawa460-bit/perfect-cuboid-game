# Stage15-6ea — AR-035 ordered-limit verdict, causal zero density, and fixed-power negative certificate

Base: Stage15-6dz. The same-measure fixed-finite-prime refined asymptotic is now proved, so the ordered-limit mechanism can finally be tested without a measure or quantifier gap.

For every good split prime,
\[
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
\]
and
\[
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
\]
For inert `p=3 mod 4`, `rho_p=1`.

## 1. Literal AR-035 hypothesis versus the Stage15 adapter

AR-035's original Stage13 contract assumed that sufficiently large selected primes have acceptance bounded by one fixed `rho<1`. That literal hypothesis **fails** here because
\[
\rho_p\to1.
\]
Thus no constant rejection factor may be assigned to every new split prime.

However the ordered-limit idea has a legal Stage15 variant. Since
\[
\sum_{p\equiv1\,({\rm mod}\,4)}\frac1p=\infty
\]
and `1-rho_p=4/p+O(1/p^2)`, one has
\[
\boxed{
\prod_{\substack{p\le z\\p\equiv1\,(4)}}\rho_p\longrightarrow0
\qquad(z\to\infty).
}
\]
No prime set grows with `B` in this statement.

## 2. Ordered limits give an independent qualitative zero-density theorem

Let `S_z` be any increasing finite set of good split primes tending through all such primes. For each **fixed** `z`, Stage15-6dz gives
\[
\limsup_{B\to\infty}\frac{N_2(B)}{M_2(B)}
\le\prod_{p\in S_z}\rho_p.
\]
Now, and only now, send `z->infinity`. The right side tends to zero. Therefore
\[
\boxed{
\frac{N_2(B)}{M_2(B)}\longrightarrow0.
}
\]
Using Stage15-2b,
\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]
so this route independently proves
\[
\boxed{
N_2(B)=o(B(\log B)^5).
}
\]
This is a **causal Stage15 local-squareclass proof** of zero density. It does not use the stronger Stage15-5 thinning theorem and does not import the Stage14 final exponent.

## 3. Why this mechanism cannot supply a fixed power

The local rejection itself is too sparse. Classical Mertens asymptotics in the progression `1 mod 4` give
\[
\sum_{\substack{p\le z\\p\equiv1\,(4)}}\frac1p
=\frac12\log\log z+O(1),
\]
so the local product has the natural scale
\[
\prod_{\substack{p\le z\\p\equiv1\,(4)}}\rho_p
=(\log z)^{-2+o(1)}.
\]
Therefore even a hypothetical effective refinement uniform for every prime `p<=B^theta` would yield only
\[
(\log B)^{-2+o(1)},
\]
not `B^{-delta}`.

This is stronger than the present lack of uniformity: **the exact local densities themselves rule out a fixed-power gain from tensoring one exact squareclass-parity filter per distinct prime in a polynomial-sized prime block.**

Using higher powers `p^r` does not create a new independent rejection factor, because `rho_p` in 6dy already integrates the complete p-adic valuation-parity condition over all `r>=1`.

Hence
\[
\boxed{\delta>0\text{ is not obtainable from this fixed-prime parity tensor alone}.}
\]
This is a mechanism-specific negative certificate, not an impossibility theorem for all future global arguments.

## 4. Effective-uniformity audit

The currently certified fixed-set asymptotic has error
\[
o_S(B(\log B)^5)
\]
with no rate uniform in `S`. Consequently the repository does **not** even promote the displayed `log^{-2}` heuristic scale to a quantitative Stage15 bound.

What is proved is exactly:

- each fixed finite prime set has the correct product density;
- the ordered `B->infinity` then `S->all split primes` limit proves qualitative `o(1)`;
- no growing-modulus step is used;
- no fixed `delta>0` follows.

## 5. Arsenal, reconstruction, measure, and quantifier audit

### AR-035

`EXACT_ADAPTER_PROVED_WITH_MODIFIED_LOCAL_PROFILE`: the fixed-modulus same-measure hypothesis is now proved, but the uniform fixed-`rho<1` local acceptance hypothesis is false. The ordered-limit mechanism survives because the rejection sum diverges; its output is qualitative zero density only.

### AR-016 / AR-023 / AR-024 / AR-028

All remain active firewalls. No divisor/finite completion is charged as a density factor; the toric/reconstructed labels are multiplicity one; no scalar host replaces the physical incidence measure; no core/root/completion information is charged twice.

### AR-026 / AR-027

No soft moment or average-to-pointwise promotion is used. The local condition is pointwise necessary for every survivor, and the only average is the exact fixed-adelic asymptotic on the same ambient physical population.

### AR-033 / AR-037

No coefficient rectangle or Euler-product asymptotic is imported to manufacture a rate. The finite local product is used only after its exact p-adic density is proved.

## 6. EXHAUSTIVE_VIEW_AUDIT after the local-density receiver change

The fixed-prime route changes the receiver from complementary divisor size to an adelic parity sieve, so re-audit all distinct internal mechanisms before any parking decision.

| Route | Current status |
|---|---|
| deterministic reconstruction / 6da completion | consumed, exponent-neutral |
| double eliminant / factor incidence | consumed / equivalent |
| `k=1` factor-gap | consumed as branch postfilter |
| `k>1` Pell/unit orbit | current-input negative certified |
| orientation-blind pair resultant | current-input negative certified |
| centered character/Ramanujan dispersion | current-input negative certified |
| ambient and cell complementary switch | equivalent; no `delta` or `sigma` |
| fixed-prime local overlap sieve | **qualitative zero density proved here; fixed-power negative certified** |
| growing-modulus/effective adelic sieve | external quantitative gate; exact local product predicts log-scale, not a fixed power |
| genus-one/height or Stage14 exponent transfer | no same-measure adapter; parked external/different-measure species |

No untested internal receiver in the current ledger supplies a distinct fixed-power mechanism.

## 7. BLIND_REDISCOVERY from the exact local condition

Restart only from
\[
AB\in\mathbf Q^{\times2}
\]
on the physical toric surface. Prime by prime, inert primes are automatically harmless and every split prime rejects only the codimension-one tubes where one of the four Gaussian linear factors acquires odd valuation. The measure of such tubes is `~1/p`, so any independent primewise tensor necessarily accumulates logarithmically.

Thus blind rediscovery returns the same conclusion:

1. local parity gives a clean causal explanation for zero density;
2. primewise independence alone cannot explain a polynomial survival exponent;
3. a fixed-power theorem requires a genuinely global correlation/reconstruction mechanism beyond this local tensor, and every such internal candidate presently in the ledger has already been consumed or negative-certified.

## 8. Stage15-6 closure candidate

Stage15-6 was opened to seek an internal/causal explanation of the thinning and, if possible, a power saving without circular Stage14 exponent transfer. The first objective is now achieved:
\[
\boxed{N_2/M_2\to0}
\]
by an exact local squareclass sieve on the same physical measure. The stronger fixed-power objective remains unavailable from the internal receiver ledger.

Accordingly this batch does **not** invent another route. It emits a closure/parking candidate for fresh audit.

```text
STAGE15_6_SUBSTAGE=6ea
STAGE15_6EA_AR035_LITERAL_FIXED_RHO_HYPOTHESIS=false
STAGE15_6EA_AR035_STAGE15_ORDERED_PRODUCT_ADAPTER=true
STAGE15_6EA_QUALITATIVE_ZERO_DENSITY_PROVED=true
STAGE15_6EA_ZERO_DENSITY_INDEPENDENT_OF_STAGE15_5=true
STAGE15_6EA_LOCAL_PRODUCT_SCALE=LOGARITHMIC_NOT_POLYNOMIAL
STAGE15_6EA_FIXED_POWER_FROM_LOCAL_PARITY_TENSOR=false
STAGE15_6EA_DELTA_PROVED=false
STAGE15_6EA_SIGMA_PROVED=false
STAGE15_6EA_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6EA_BLIND_REDISCOVERY=true
STAGE15_6EA_INTERNAL_FIXED_POWER_ROUTE_REMAINS=false
STAGE15_6EA_CLOSURE_CANDIDATE=true
STAGE15_6EA_SPLIT_TRIGGER=false
STAGE15_6EA_AUDIT_REQUIRED=true
STAGE15_6EA_CODEX_REQUIRED=false
STAGE15_6EA_MERGE_ALLOWED=false
STAGE15_6EA_EXIT=FRESH_AUDIT_OF_LOCAL_ZERO_DENSITY_AND_STAGE15_6_CLOSURE_CANDIDATE
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6ea
NEXT_GATE=FRESH_AUDIT_OF_LOCAL_ZERO_DENSITY_AND_STAGE15_6_CLOSURE_CANDIDATE
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```
