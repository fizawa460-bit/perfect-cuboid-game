# Stage34-01 — exact EXT-C / Paper C source reconstruction

Status: `AUDITED_PASS_P1_EXACT_OBJECT_AND_GLOBAL_POPULATION_CLOSED`.

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
- `audit-closure.json`

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

## Global population contract — audited 7/7

Formal Arsenal workflow `S31-WF01 CAS_MW_FULL_GROUP_CERTIFICATION` was used rather than treating PARI `ellrank` points as automatically saturated.

Official Magma V2.29-9 `Saturation(points)` gave source free index `1` for `q=20/21`, `q=24/7`, and rank-two `q=60/11`; the rank-two source-coordinate matrix is `[[0,-1],[1,0]]` with determinant absolute value `1`.

The public Magma calculator hit its explicit 60-second resource limit on the other four fibers. That is preserved as a resource wall, not a mathematical failure, in `mw-magma-partial-certificate.json`.

The residual rank-one fibers `80/39`, `84/13`, `48/55`, `20/99` were independently replayed with Ubuntu `eclib-tools` / `mwrank -q -v 1 -o`. The pinned artifact explicitly reports that the rank and full Mordell--Weil basis were determined unconditionally, returns the Paper-C source point itself as the saturated free generator, and the Stage34 exact group-law replay verifies `4(P-G)=O` in each case.

Therefore all seven Paper-C source free lattices equal the full free Mordell--Weil lattice modulo torsion.

## Quantifier repair

Rank one is authoritative per fixed torsion translate:

```text
N_{q,T}(n)=Num(F3(nP_q+T)).
```

A theorem for `T=O` does not silently cover the other seven translates.

Rank two uses the full nonzero lattice `(a,b) in Z^2`. No artificial one-dimensional primitive-divisor order is imposed; the accepted target is instead a direct effective odd-valuation / nonsquare theorem outside an explicit finite box.

## Hostile audit

PR #1479 hostile audit PASS was submitted against head `e320e5af68cb780654987ef9c4f7e90f4b7ba1f5` and independently checked source locks, raw Magma/eclib evidence, rank-two coordinates, torsion-translate semantics, and promotion firewalls.

The audit promotes only:

```text
P1 exact object + global population = CLOSED
GLOBAL_RECEIVER_POPULATION_SOURCE_LOCKED_AUTHORITATIVE=true
STAGE34_02_RELEASED=true
```

It does **not** promote P2/P3/P4/P6, receiver closure, parent-route closure, endpoint closure, or any perfect-cuboid claim.

The audit's nonblocking eclib hardening note is implemented on the continuation branch: future reruns positively require mwrank's explicit unconditional full-MW-basis success sentence.

## Next unit

`34-02_SEQUENCE_CLASSIFICATION_AND_THEOREM_FUNNEL`

The task is now genuinely theorem-facing: classify which theorem species can apply to the exact fixed-torsion rank-one orbit-value numerators and which replacement theorem species can handle the rank-two lattice, without importing standard EDS denominator results by analogy.

## Firewalls

```text
P1 population closure != primitive/fresh-factor theorem
untranslated nP theorem != all nP+T
one-variable primitive divisor != rank-two lattice theorem
EDS denominator B_n != Face-3 numerator N(Q)
primitive divisor != odd valuation
finite window != all multiples
receiver closure != parent route closure
seven-fiber closure != perfect-cuboid nonexistence
```
