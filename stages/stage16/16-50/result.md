# Stage16-50 — lower-bound / construction ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Question

Checkpoint 50 freezes the strongest certified lower bound and the construction mechanisms for
\[
M_1(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ \text{exactly one integral face diagonal}\}.
\]

It does not search for a stronger theorem. Stage16-30 has already passed fresh audit and proves the matching lower bound
\[
\boxed{M_1(B)\gg B^2\log B.}
\]
Together with checkpoint 40,
\[
M_1(B)\asymp B^2\log B.
\]
No leading asymptotic constant is claimed.

## Sharp Stage16 construction

The sharp lower bound is the explicit family already certified inside Stage16-30.

Choose a primitive Pythagorean face
\[
(x_0,y_0,h),
\]
a scale `k` with
\[
kh\le B/4,
\]
and a third edge
\[
B/3<z\le B/2,
\qquad (z,k)=1.
\]
Then
\[
R^2=(kh)^2+z^2< B^2,
\]
and because `(x_0,y_0)=1`, global primitivity is exactly ensured by `(z,k)=1`.

The two possible accidental second-face squares are removed using
\[
X^2+z^2=w^2
\quad\Longrightarrow\quad
(w-z)(w+z)=X^2,
\]
so for fixed `X` there are at most `\tau(X^2)` bad third edges. This deletion is lower order uniformly in the construction range.

For fixed `k`, the available coprime third edges contribute
\[
\frac{B}{6}\frac{\varphi(k)}{k}+O(\tau(k)),
\]
while primitive face shapes with `h\le B/(4k)` contribute `\gg B/k`. Summing gives
\[
B^2\sum_{k\le cB}\frac{\varphi(k)}{k^2}
\asymp B^2\log B,
\]
and the coprimality and accidental-square errors are lower order. The unique integral face makes the construction injective.

Thus the strongest certified construction lower bound is
\[
\boxed{M_1(B)\gg B^2\log B.}
\]
This is order-sharp against checkpoint 40.

## AR-039 adapter and its proper role

AR-039 gives a different, much thinner two-parameter family. For coprime
\[
m>n\ge1,\qquad m\equiv2\pmod{14},\quad n\equiv1\pmod{14},
\]
set
\[
x=m^2-n^2,\quad y=2mn,\quad p=m^2+n^2,
\]
\[
c=\frac{p^2-1}{2},\qquad d=\frac{p^2+1}{2}.
\]
The canonical triple `(min(x,y),max(x,y),c)` is primitive, has exactly the `xy` face integral, and has integral space diagonal `d`. Modulo 7 forces both remaining face sums to be nonsquares.

Because Stage16 does **not** require the space diagonal to be nonintegral, this AR-039 family is a valid subset of the Stage16 population. On this subset
\[
R=d
\]
exactly, so its historical cutoff `d\le B` is the same Stage16 cutoff `R\le B`. Therefore AR-039 legally implies the weaker regression lower bound
\[
M_1(B)\gg B^{1/2}.
\]

This is not charged as the sharp Stage16 lower bound. It is retained because it supplies:

1. an explicit symbolic exactly-one family;
2. an integral-space-diagonal regression subset useful for Stage17/21 compatibility checks;
3. a local mod-7 certificate preventing accidental second/third face squares.

It must not replace the ambient Stage16 construction or be used to infer the Stage16 growth exponent.

## Lower-bound capability ledger

```text
LOWER_BOUND=M_1(B) >> B^2 log B
EVIDENCE_LEVEL=PROVED_AND_FRESH_AUDITED_VIA_STAGE16_30
ORDER_SHARP=true
MAIN_CONSTRUCTION=Stage16-30_PYTHAGOREAN_FACE_SCALE_FREE_THIRD_EDGE_WITH_ACCIDENTAL_SQUARE_DELETION
INJECTIVE=true
GLOBAL_PRIMITIVITY_PROVED=true
EXACT_ONE_PROVED=true
R_CUTOFF_EXACT=true
LEADING_CONSTANT_PROVED=false
AR039_ADAPTED=true
AR039_ROLE=WEAKER_INTEGRAL_SPACE_DIAGONAL_REGRESSION_SUBFAMILY
AR039_CUTOFF_ADAPTER=R_EQUALS_d_EXACTLY
AR039_NOT_USED_FOR_STAGE16_EXPONENT=true
POPULATION_CONTRACT_CHANGED=NO
FINITE_DATA_USED_AS_PROOF=false
```

## What is and is not charged

- **AR-001:** direct reuse for primitive/canonical and exact-one conventions.
- **AR-002:** direct reuse for the unique primitive Euclid face decomposition.
- **AR-039:** exact subset adapter only; its `B^{1/2}` lower bound is recorded but is strictly weaker than the audited ambient lower bound.
- Stage14/15 exactly-two or survivor upper bounds are not imported.
- Stage16-20 finite counts remain diagnostic only.
- No asymptotic constant, directional law, Stage16-to-Stage17 survival ratio, or perfect-cuboid conclusion is added.

Checkpoint 50 adds no theorem stronger than Stage16-30. It freezes the sharp lower-bound mechanism and separates it from the narrower AR-039 regression family. Checkpoint 60 will be the first place to synthesize the causal decomposition, so the main lane stops here for fresh audit.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=50
CHECKPOINTS_ATTEMPTED=50
CHECKPOINTS_SUBMITTED=50
NEW_CLAIMS=NONE; lower-bound/construction ledger extracted from audited Stage16-30, with an exact subset/cutoff adapter for AR-039
REUSED_WEAPONS=AR-001,AR-002,AR-039
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 50 is a compact proof-ledger and exact population/cutoff adapter; no repository-heavy implementation or unavailable execution is required.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
```
