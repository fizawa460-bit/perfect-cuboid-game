# Stage14-2c — finite census closure

## Purpose

Close Stage14-2 only after the finite census has been checked through a second generation route that does not reuse the production gluing order.

Stage14-2a built the standalone Stage14 production census. Stage14-2b extended it through `B=2,000,000`. Stage14-2c performs the missing independent cross-check, consolidates the 11 audited rows, and freezes the finite table before Stage14-3.

## Two generation routes

Production route (`two_face_census.py`):

```text
choose an integral face x^2+y^2=p^2
join p^2+z^2=d^2
canonicalize/deduplicate
recompute all face-square flags
```

Independent audit route (`shared_leg_crosscheck.py`):

```text
generate Pythagorean faces
join two faces that share a leg
only then test a^2+b^2+c^2=d^2
canonicalize/deduplicate
recompute all face-square flags
```

The second route starts from the two-face condition itself rather than from a distinguished face followed by a space-diagonal extension. Agreement therefore checks the main finite population by a materially different construction path.

## Frozen 11-row population

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 0 | 0 | 2 | 0 |
| 2,000 | 2 | 2 | 1 | 5 | 0 |
| 5,000 | 6 | 6 | 3 | 15 | 0 |
| 10,000 | 9 | 11 | 5 | 25 | 0 |
| 20,000 | 16 | 16 | 10 | 42 | 0 |
| 50,000 | 24 | 24 | 14 | 62 | 0 |
| 100,000 | 33 | 33 | 23 | 89 | 0 |
| 200,000 | 42 | 50 | 24 | 116 | 0 |
| 500,000 | 70 | 78 | 40 | 188 | 0 |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 |

Every row agrees exactly between the two generation routes. Every row also satisfies the exact pair-minus-triple identities. No triple object occurs in this finite range; this is not a nonexistence theorem.

## Finite directional warning

The finite leader is not stable. The `b` direction leads at `B=200k,500k,1m`, while `a` leads at `B=2m`. Therefore Stage14-3 must treat monotone directional convergence as an empirical question rather than an assumption.

At the largest audited cutoff,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\]

and the c-normalized ratio is

\[
1.775:1.675:1.
\]

## Stage13 isolation

No Stage13 analytic theorem is needed for this closure:

```text
STAGE13_CODE_IMPORTED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
```

The historical first seven rows remain useful as checksums, but the Stage14 production and independent audit routes now reproduce them directly. The four extension rows are Stage14-owned finite results.

Any Stage13 asymptotic statement currently under external review is quarantined from Stage14 finite conclusions.

## Stop line after Stage14-3

The current research policy is:

```text
Stage14-2  finite population census                     COMPLETE
Stage14-3  finite directional diagnostics               ALLOWED / NEXT
Stage14-4  true asymptotic growth order                 PAUSED
Stage14-5  directionwise asymptotic structure           PAUSED
```

Stage14-4 and Stage14-5 are not entered until the one-face / Stage13 proof review has clarified which structural results are reliable enough to serve as a map. Stage14-3 may describe finite data, compare candidate diagnostics, and record what a later proof must explain, but it must not promote an empirical fit to a theorem.

## Decision

```text
STAGE14_2A=COMPLETE
STAGE14_2B=COMPLETE
STAGE14_2C=COMPLETE
STAGE14_2=COMPLETE
FINITE_CENSUS_FROZEN=true
INDEPENDENT_GENERATION_ROUTES=2
ALL_11_ROWS_MATCH=true
MAX_VERIFIED_B=2000000
PERFECT_CUBOID_WITNESS_FOUND=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
NEXT=Stage14-3 finite directional-ratio analysis
```
