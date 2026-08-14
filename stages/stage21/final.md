# Stage21 — self-contained final bundle R02

STATUS=CANDIDATE_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED
SELF_CONTAINED_REVIEW_STANDARD=V1

## Population and cutoff

Stage21 studies the transition from primitive canonical exactly-one-face cuboids to the same population with integral space diagonal, under common cutoff `R<=B`; for Stage17 objects `d=R` exactly. Stage16S supplies the ambient primitive/canonical integral-space-diagonal control.

```text
SOURCE=Stage16 exactly-one face, no space requirement
TARGET=Stage17 exactly-one face + integral space diagonal
CONTROL=Stage16S ambient integral-space-diagonal population
```

## V1 upstream import contracts

### Import A — E-1e / PR #128 source asymptotic

```text
UPSTREAM_STAGE=Stage14 Euler-side E-1e / PR #128
UPSTREAM_THEOREM=M1(B)~3/(4*pi^2) B^2 log B and M1,q(B)~6 I_q/pi^4 B^2 log B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The imported population is exactly primitive/canonical, exactly one integral face, no space-diagonal requirement, under the same Euclidean radius cutoff `R<=B` used by Stage21 source objects.

### Import B — Stage17 target asymptotic

```text
UPSTREAM_STAGE=Stage17
UPSTREAM_THEOREM=N1(B)~kappa/(24*pi) B(log B)^3 and N1,q(B)~kappa I_q/(3*pi^3) B(log B)^3
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Stage17 counts primitive/canonical exactly-one-face cuboids with integral space diagonal. On those objects `d=R` exactly, so its `d<=B` cutoff is literally the Stage21 `R<=B` target cutoff.

### Import C — Stage16S ambient control

```text
UPSTREAM_STAGE=Stage16S
UPSTREAM_THEOREM=NSall(B)/U(B)~[9*zeta(3)/(8*pi*G)]/B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

`U(B)` and `NSall(B)` use the same primitive/canonical ambient population and the same compatible `R<=B` convention. No face restriction is imposed in this control ratio.

### Import D — Stage13 R07 bulk principal-sector theorem

```text
UPSTREAM_STAGE=Stage13 R07
UPSTREAM_THEOREM=the Stage17 shared-P nested-Pythagorean bulk has main term B(log B)^3 from the full principal multiplicative sector; every nonprincipal effective sector loses at least one pole and is lower order
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The Stage13 object is the distinguished-face incidence model underlying the Stage17 exactly-one count. The canonical projection and overlap subtraction are already part of the frozen Stage13/17 interface; Stage21 does not alter their multiplicity or quantifier order.

### Import E — AR-038 exact shared-P convolution

```text
UPSTREAM_STAGE=Stage11 / AR-038
UPSTREAM_THEOREM=C_raw(B)=2 sum_{P<=B} H(P)L_B(P) with primitive/canonical multiplicity identity C_prim(B)=2N1(B)+4N_exact2(B)+6N3(B)
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

For a primitive/canonical cuboid with integral space diagonal, choose an integral face and write

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

For a fixed shared `P`, `H(P)` counts positive unordered representations of `P` as a hypotenuse and `L_B(P)` counts positive representations of the same `P` as a leg with resulting `d<=B`. Each pair produces a raw distinguished-face record, and the two orders of the chosen face legs give the factor `2`, hence

\[
C_{raw}(B)=2\sum_{P\le B}H(P)L_B(P).
\]

After primitive/canonical projection, an exactly-one target object has one integral face and therefore contributes two oriented distinguished-face records; an exactly-two object contributes two faces and therefore four such records; an Euler object contributes three faces and therefore six records. Thus

\[
\boxed{C_{prim}(B)=2N_1(B)+4N_{exact2}(B)+6N_3(B)}.
\]

This is an exact multiplicity adapter, not an asymptotic approximation. Since Stage13 proves the pair and triple overlaps are `o(B(log B)^3)`, the `2N1(B)` term carries the leading primitive/canonical exactly-one target mass.

### Import F — AR-039 explicit survivor family

```text
UPSTREAM_STAGE=Stage11 / AR-039, strengthened in Stage21-50
UPSTREAM_THEOREM=N_AR039(B)=Theta(B^(1/2)) and hence N_AR039(B)=o(N1(B))
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The AR-039 construction is an injective two-parameter primitive exactly-one survivor family with exact height

\[
d=\frac{(m^2+n^2)^2+1}{2}.
\]

Its audited lower construction gives

\[
N_{AR039}(B)\ge \frac{\sqrt2}{120\pi^2}B^{1/2}-O(B^{1/4}\log B),
\]

so `N_AR039(B)\gg B^{1/2}`. For the matching upper bound, `d<=B` implies

\[
(m^2+n^2)^2<2B,
\qquad m^2+n^2<(2B)^{1/2},
\qquad m<(2B)^{1/4}.
\]

For each positive `m`, even after discarding every congruence and coprimality restriction, there are at most `m-1` positive choices `n<m`. Therefore, with `M=(2B)^{1/4}`,

\[
\#\{(m,n):d\le B\}
\le \sum_{m<M}(m-1)
=O(M^2)
=O(B^{1/2}).
\]

Injectivity of the AR-039 parametrization transfers this pair count directly to distinct physical family members. Combining upper and lower bounds gives

\[
\boxed{N_{AR039}(B)=\Theta(B^{1/2})}.
\]

Since Stage17 proves

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

we have

\[
\frac{N_{AR039}(B)}{N_1(B)}
\ll \frac{B^{1/2}}{B(\log B)^3}
=B^{-1/2}(\log B)^{-3}\to0,
\]

and therefore

\[
\boxed{N_{AR039}(B)=o(N_1(B))}.
\]

## Main transition theorem

From imports A and B,

\[
\frac{N_1(B)}{M_1(B)}
\sim
\frac{\kappa/(24\pi)}{3/(4\pi^2)}\frac{(\log B)^2}{B}
=
\boxed{\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}.
\]

Directionwise the common positive chamber factor cancels:

\[
\frac{N_{1,q}(B)}{M_{1,q}(B)}
\sim
\frac{\kappa I_q/(3\pi^3)}{6I_q/\pi^4}\frac{(\log B)^2}{B}
=
\boxed{\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}.
\]

Thus there is no new leading direction-specific thinning when the space-diagonal condition is added.

Against import C,

\[
\frac{N_1/M_1}{N_S^{all}/U}
\sim
\frac{\kappa\pi/18}{9\zeta(3)/(8\pi G)}(\log B)^2
=
\boxed{\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty}.
\]

Hence the intrinsic polynomial space cost is `B^-1`, while prior one-face conditioning produces a positive logarithmic enhancement `(log B)^2`. Direct asymptotic independence in ratio sense is false.

## Mechanism proof chain

The added target condition is the exact nested shared-`P` system

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

Import E proves that the target bulk is assembled through exact shared-`P` representation multiplicities. Import D analyzes this same bulk with the outer `h,r,s` multiplicative system and proves that the full principal sector carries the `B(log B)^3` main term while nonprincipal sectors are lower order. Therefore the logarithmic compensation is localized to the bulk shared-`P` multiplicative principal architecture.

Three competing explanations are excluded: directional chamber factors cancel in the matched source/target ratio; pair/triple overlap corrections are lower order; and import F proves the entire AR-039 explicit family is `o(N1)`, so that thin construction cannot generate the bulk enhancement.

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

The stage promotes two portable contracts in `docs/stage21-arsenal.md`: the ambient-control interaction adapter and the exact one-face-to-space transition theorem. Both inherit the explicit V1 import contracts above.

## Evidence boundary

Finite census data were used only for cross-checking enumerators and population interfaces, never as proof of the asymptotic laws.

```text
FINITE_DATA_USED_AS_PROOF=false
SELF_CONTAINED_BUNDLE_COMPLETE=true
ARSENAL_PROMOTIONS_MATERIALIZED=true
V1_UPSTREAM_IMPORT_CONTRACTS_COMPLETE=true
AR038_MULTIPLICITY_ADAPTER_EMBEDDED=true
AR039_THETA_PROOF_EMBEDDED=true
AUDIT_STATUS=PENDING_FRESH_AUDIT
```
