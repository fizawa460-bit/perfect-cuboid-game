# Stage34-01 — exact EXT-C / Paper C source reconstruction

Status: `PREAUDIT_PASS_EXACT_OBJECT_WINDOW_ADAPTER_AND_GLOBAL_POPULATION_EVIDENCE_COMPLETE`.

## Exact object

Stage29 `R29-EXT-CHANG-C` / `K16-C3-EXT-C-PRIMITIVE-DIVISOR` is pinned to Paper C at external commit `bd3018b896c8ac15b56cadc382af1477dca9e97a`.

The load-bearing object is not one ordinary EDS. It is the reduced Face-3 numerator along elliptic Mordell--Weil orbits:

```text
E_q: y^2=x(x+1)(x+q^2)
c(Q)=2*y(Q)*q/(q^2-x(Q)^2)
F3(Q)=c(Q)^2+1+q^2
N(Q)=Num(F3(Q)) in lowest terms
```

Six rank-one fibers use `Q=nP_q+T`; the rank-two `q=60/11` fiber uses `Q=aG1+bG2+T`; all use the full order-8 torsion subgroup.

Source locks:

- `exact-sequence-lock.json`
- `finite-window-lock.json`
- `cuboid-obstruction-adapter-lock.json`
- `global-population-contract.json`

## Finite source window

Paper C certifies exactly:

```text
rank one:
  six fibers
  1 <= n <= 200
  all 8 torsion translates
  9,600 cosets
  Face-3 squares = 0

rank two q=60/11:
  |a|,|b| <= 12, (a,b)!=(0,0)
  all 8 torsion translates
  4,992 cosets
  Face-3 squares = 0
```

This remains finite-window credit only.

## Same-point cuboid obstruction

If the reduced numerator `N(Q)` has a prime of odd valuation, then `F3(Q)` is not a rational square, so the same source point is excluded from the Paper-C cuboid condition. Primitive/fresh divisors are only a proposed mechanism for forcing odd valuation.

The distinction is load-bearing: Paper C's `q=20/21,n=5` example has primitive prime `29` with even valuation `v_29(N_5)=2`.

## Global population contract repaired

The original source reconstruction exposed three gaps. Their preaudit evidence status is now:

### A. Full Mordell--Weil source lattice — evidence complete 7/7

Formal Arsenal workflow `S31-WF01 CAS_MW_FULL_GROUP_CERTIFICATION` was used rather than treating PARI `ellrank` points as automatically saturated.

Official Magma V2.29-9 `Saturation(points)` gave source free index `1` for:

```text
q=20/21
q=24/7
q=60/11 (rank two)
```

The rank-two source-coordinate matrix is

```text
[0 -1]
[1  0]
```

with determinant absolute value `1`.

The public Magma calculator hit its explicit 60-second resource limit on the other four fibers. That was retained as a resource wall, not a mathematical failure, in `mw-magma-partial-certificate.json`.

Those four rank-one fibers were independently replayed with Ubuntu `eclib-tools` / `mwrank`:

```text
q=80/39
q=84/13
q=48/55
q=20/99
```

`mwrank -o` returned the Paper-C source point itself as the saturated free generator on every one of these four curves. `run_eclib_mw_certificate.py` also exact-replayed the group law and verified `4(P-G)=O` in every case. Since `E_q(Q)_tors = Z/4 x Z/2`, the source point and mwrank basis have the same free class.

Evidence:

- `mw-magma-partial-certificate.json`
- `mw-eclib-certificate.json`
- `mw-eclib-execution.json`

Therefore all seven Paper-C source free lattices have complete preaudit index-one evidence.

### B. Torsion translates — quantifiers fixed

The rank-one theorem target is now per fixed torsion translate:

```text
N_{q,T}(n)=Num(F3(nP_q+T)).
```

A theorem for `T=O` does not silently cover the other seven translates.

### C. Rank two — no fake primitive ordering

No artificial one-dimensional primitive-divisor ordering is imposed on `Z^2`. The accepted rank-two target is instead an effective direct theorem proving odd valuation / nonsquareness outside an explicit finite box, with the remaining finite annulus discharged exactly.

The complete definitions are in `global-population-contract.json`.

## Arsenal use

- `S31-WF01` supplied the MW full-group/saturation proof workflow.
- `S30-WF02` supplies immutable execution/certificate binding discipline.
- `S30-WF03` keeps population repair separate from theorem, receiver and endpoint credit.

There is still no Arsenal mathematical weapon that directly proves the required global odd-valuation theorem for the Face-3 orbit-value numerators.

## Current boundary

34-01 evidence is complete, but repository-wide credit policy requires hostile audit before authoritative closure and downstream release.

```text
STAGE34_01_EVIDENCE_COMPLETE=true
STAGE34_01_HOSTILE_AUDIT_PASSED=false
STAGE34_02_RELEASED=false
```

Next command-level action is `stage34audit`. A hostile PASS may promote the global population contract and release `34-02_SEQUENCE_CLASSIFICATION_AND_THEOREM_FUNNEL`.

## Firewalls

```text
preaudit evidence complete != audited closure
ellrank tight rank != saturated basis without certification
untranslated nP theorem != all nP+T
one-variable primitive divisor != rank-two lattice theorem
EDS denominator B_n != Face-3 numerator N(Q)
primitive divisor != odd valuation
finite window != all multiples
MW population repair != primitive-divisor theorem
receiver closure != parent route closure
seven-fiber closure != perfect-cuboid nonexistence
```
