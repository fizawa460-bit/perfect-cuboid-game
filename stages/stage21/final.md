# Stage21 — self-contained final bundle R01

STATUS=CANDIDATE_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED
SELF_CONTAINED_REVIEW_STANDARD=V1

## Population and cutoff

Stage21 studies the transition from primitive canonical exactly-one-face cuboids to the same population with integral space diagonal, under common cutoff `R<=B`; for Stage17 objects `d=R` exactly. Stage16S supplies the ambient primitive/canonical integral-space-diagonal control.

```text
SOURCE=Stage16 exactly-one face, no space requirement
TARGET=Stage17 exactly-one face + integral space diagonal
CONTROL=Stage16S ambient integral-space-diagonal population
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

## Frozen source interfaces

The strongest matched Stage16 interface recovered from E-1e / PR #128 is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Directionwise,

\[
M_{1,q}(B)\sim \frac{6I_q}{\pi^4}B^2\log B.
\]

Stage17 proves

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad
N_{1,q}(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Stage16S proves

\[
\frac{N_S^{all}(B)}{U(B)}\sim \frac{9\zeta(3)}{8\pi G}\frac1B.
\]

## Main transition theorem

Dividing matched source and target laws gives

\[
\boxed{\frac{N_1(B)}{M_1(B)}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}.
\]

For each `q=ab,ac,bc`, the common chamber factor `I_q` cancels, so

\[
\boxed{\frac{N_{1,q}(B)}{M_{1,q}(B)}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}.
\]

Thus there is no new leading direction-specific thinning when the space-diagonal condition is added.

Against the Stage16S ambient control,

\[
\boxed{\frac{N_1/M_1}{N_S^{all}/U}\sim \frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty}.
\]

Hence the intrinsic polynomial space cost is `B^-1`, while prior one-face conditioning produces positive logarithmic enhancement `(log B)^2`. Direct asymptotic independence in ratio sense is false.

## Mechanism proof chain

For the unique integral face,

\[
x^2+y^2=P^2,
\]

and the added space-diagonal condition is

\[
P^2+z^2=d^2.
\]

This is an exact nested shared-`P` Pythagorean system. AR-038 freezes the raw convolution

\[
C_{raw}(B)=2\sum_{P\le B}H(P)L_B(P),
\]

with primitive/canonical multiplicity identity

\[
C_{prim}(B)=2N_1(B)+4N_{exact2}(B)+6N_3(B).
\]

Stage13 R07 analyzes the same bulk through outer parameters `h,r,s`. Its principal multiplicative sector carries the full `B(log B)^3` numerator main term; every nonprincipal effective sector loses at least one pole and is lower order. Therefore the logarithmic compensation is localized to the bulk shared-`P` multiplicative principal architecture.

Three competing explanations are rigorously excluded. First, directional chamber factors cancel in the source/target ratio. Second, pair/triple overlap corrections are `o(B(log B)^3)`. Third, Stage21-50 proves the entire AR-039 explicit family satisfies

\[
N_{AR039}(B)=\Theta(B^{1/2})=o(N_1(B)),
\]

so that thin explicit family cannot generate the bulk enhancement.

## Intrinsic status

```text
TRUE_POLYNOMIAL_EXPONENT_IDENTIFIED=true
INTRINSIC_SPACE_DIAGONAL_COST=B^-1
INTERACTION_SIGN=POSITIVE
INTERACTION_SCALE=(log B)^2
INDEPENDENT_OF_PRIOR_ONE_FACE_CONDITION=false
LEADING_DIRECTION_SPECIFIC_INTERACTION=false
DOUBLE_CHARGE_CHECK=PASS
```

## Open gate

The proof does not canonically assign the two net logarithms to two individually named pole slots or local factors. No independent-factor product or stochastic independence statement is asserted.

```text
OPEN_GATE=LOG_SQUARED_FINE_POLE_OR_LOCAL_FACTOR_DECOMPOSITION_UNRESOLVED
OPEN_GATE_BLOCKS_STAGE21_CLOSEOUT=false
```

## Reusable outputs

The stage promotes two portable contracts in `docs/stage21-arsenal.md`: the ambient-control interaction adapter and the exact one-face-to-space transition theorem. Both inherit the population/cutoff/multiplicity restrictions above.

## Evidence boundary

Finite census data were used only for cross-checking enumerators and population interfaces, never as proof of the asymptotic laws. The load-bearing asymptotic inputs are the audited Stage16/E-1e, Stage17, Stage16S, Stage13 R07, and AR-038/039 interfaces.

```text
FINITE_DATA_USED_AS_PROOF=false
SELF_CONTAINED_BUNDLE_COMPLETE=true
ARSENAL_PROMOTIONS_MATERIALIZED=true
AUDIT_STATUS=PENDING_FRESH_AUDIT
```
