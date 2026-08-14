# Stage24-30 — theorem-level survivor law

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Literal transition

Stage24 compares

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\},
\]

under one primitive canonical physical measure and the exact common cutoff `R<=B`. Thus

\[
M_2(B)=\#\mathcal B_2(B),\qquad N_2(B)=\#\mathcal A_2(B)
\]

form a literal source/subset pair with no population, cutoff, multiplicity, measure or quantifier adapter.

## 2. Strongest certified quantitative survivor law

Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

while Stage19 imports the certified whole-family numerator bound

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore

\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
\to0.
}
\]

Equivalently, for every fixed `delta<1/2`,

\[
N_2(B)/M_2(B)\ll_\delta B^{-\delta}.
\]

This is the strongest certified quantitative Stage24 ratio law at checkpoint30. The exponent `1/2` is inherited from the Stage14/19 numerator theorem and is not asserted to be the true target exponent.

## 3. Leading-constant search

Stage15-2b proves

\[
C_{M_2}=C_a+C_b+C_c,\qquad C_a,C_b,C_c>0,
\]

and identifies these as toric/Tamagawa chamber constants. But it explicitly records that neither `C_M2` nor the directional constants were evaluated in closed numerical form. The numerator theorem is also a big-O theorem with an implicit `epsilon`-dependent constant. Hence no rigorous numerical leading constant exists for the quantitative survivor upper bound at the frozen interface level.

```text
LEADING_CONSTANT_SEARCH=COMPLETE
SOURCE_CONSTANT_EXISTS=true
SOURCE_CONSTANT_EXPLICIT=false
NUMERATOR_UPPER_CONSTANT_EXPLICIT=false
SURVIVOR_RATIO_LEADING_CONSTANT_AVAILABLE=false
FINITE_ESTIMATE_PROMOTED_TO_CONSTANT=false
```

## 4. Directional theorem refinement

For each unique shared-edge direction `j=a,b,c`, Stage15 proves

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0.
\]

Since `N_{2,j}(B)<=N_2(B)`, the whole-family upper theorem immediately gives

\[
\boxed{
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\varepsilon,j}
B^{-1/2+\varepsilon}(\log B)^{-5}
\to0
}
\]

for all three directions. This proves direction-by-direction zero relative density but no directional survivor constants or limiting order.

## 5. Three independent zero-density routes

### Route A — quantitative quotient

The Stage19 whole-family upper theorem divided by the Stage18 source asymptotic gives the boxed quantitative ratio bound above.

### Route B — squareclass local sieve

The exact Stage19 condition is

\[
R\in\mathbf Z\iff \operatorname{sf}(A)=\operatorname{sf}(B).
\]

At good split primes `p=1 mod 4`, the same-measure local acceptance satisfies

\[
\rho_p=1-4/p+O(p^{-2}).
\]

For each fixed finite prime set, take `B->infinity` first; only afterward enlarge the set. The product of local acceptances tends to zero, proving independently

\[
N_2(B)/M_2(B)\to0.
\]

This route does not prove the half-power rate.

### Route C — new space-square thin cover

On the Stage18 shared-edge toric surface

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2,
\]

adjoin

\[
w^2=e^2+x^2+y^2.
\]

To verify that this quadratic cover does not split geometrically, work on `e=1` and use the standard Pythagorean rational parameters

\[
x=2t/(1-t^2),\quad u=(1+t^2)/(1-t^2),
\qquad
y=2s/(1-s^2).
\]

Then the radicand is

\[
\frac{u^2s^4+(4-2u^2)s^2+u^2}{(1-s^2)^2}.
\]

As a quadratic in `z=s^2`, its numerator has discriminant

\[
16(1-u^2)=-16x^2,
\]

which is nonzero generically. Its two `z`-roots are distinct and nonzero, so the numerator has four simple roots in `s` and is not a square. Therefore the radicand is not a square in the geometric function field. The cover is geometrically integral and generically degree two, hence its rational image is type-II thin.

Stage15-2b already verifies on the same toric resolution and exact height `R` the hypotheses used for Browning-Loughran thin-set zero density. Consequently

\[
\boxed{N_2(B)=o(B(\log B)^5)},\qquad
\boxed{N_2(B)/M_2(B)\to0}.
\]

This proof is independent of both the Stage14 half-power upper theorem and the Stage15/19 split-prime squareclass sieve. It yields qualitative zero density, not an effective fixed power. Full proof ledger: `space-thin-cover.md`.

## 6. Directional zero density from the thin cover

The global thin-image count is `o(B(log B)^5)`. Since each directional denominator satisfies `M2,j(B)~C_j B(log B)^5` with `C_j>0`, it follows independently that

\[
N_{2,j}(B)/M_{2,j}(B)\to0
\]

for every direction.

## 7. Million-scale finite evidence

Checkpoint20/r202 supplies exact same-population data through one million. At the endpoint,

\[
M_2(10^6)=13{,}817{,}725,\qquad N_2(10^6)=255,
\]

so

\[
N_2/M_2=1.8454557461521345\times10^{-5}.
\]

The directional finite ratios are approximately

```text
a: 98 / 4592536 = 2.1338972629e-5
b: 101 / 5816786 = 1.7363540622e-5
c: 56 / 3408403 = 1.6429982018e-5
```

They are consistent with the directional zero-density theorem but do not identify directional limits. The finite effective slope of the global ratio changes from about `-0.494` on 1k->100k to about `-0.782` on 100k->1m, so checkpoint30 refuses to infer a single empirical power law.

## 8. What checkpoint30 proves and does not prove

Proved:

- literal matched survivor ratio;
- quantitative upper ratio `B^(-1/2+epsilon)(log B)^-5`;
- global zero relative density;
- directional zero relative density in all three shared-edge chambers;
- a third independent qualitative zero-density proof via a geometrically integral degree-two space-square cover.

Not proved:

- `N2(B)->infinity`;
- a positive-power lower bound for `N2`;
- a matching half-power lower bound;
- `N2(B)~C B^(1/2)` or any other asymptotic;
- a strict sub-square-root numerator theorem;
- that exponent `1/2` is intrinsic;
- an explicit survivor leading constant;
- directional survivor limits or preferential removal;
- any perfect-cuboid existence/nonexistence statement.

## 9. Exit

Checkpoint30 settles the first theorem-level Stage24 survivor law but does not complete Stage24. Checkpoint40 must reopen the upper side and attack strict sub-square-root improvement rather than treating the inherited half-power ceiling as final.

```text
DISCOVERY_CHECKPOINT=30
DISCOVERY_LEDGER_STATUS=COMPLETE
QUANTITATIVE_RATIO_PROVED=true
GLOBAL_ZERO_DENSITY_PROVED=true
DIRECTIONAL_ZERO_DENSITY_PROVED=true
INDEPENDENT_PROOF_ROUTE_SEARCH=COMPLETE
INDEPENDENT_ZERO_DENSITY_ROUTES=3
NEW_ROUTE=SPACE_SQUARE_THIN_COVER
LEADING_CONSTANT_SEARCH=COMPLETE_NOT_EXPLICIT
TRUE_RATIO_EXPONENT_IDENTIFIED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
