# Stage34-01 — exact EXT-C / Paper C source reconstruction

Status: `PARTIAL_PASS_EXACT_OBJECT_WINDOW_ADAPTER_LOCKED_GLOBAL_POPULATION_CONTRACT_OPEN`.

## What is now exact

Stage29 `R29-EXT-CHANG-C` / `K16-C3-EXT-C-PRIMITIVE-DIVISOR` refers to Lightman Chang's Paper C source set, pinned here to external repository `weiqi-kids/perfect-cuboid-problem` commit `bd3018b896c8ac15b56cadc382af1477dca9e97a`.

The load-bearing object is **not one ordinary EDS sequence**. It is the numerator of the Face-3 rational function along Mordell--Weil orbits:

```text
E_q: y^2=x(x+1)(x+q^2)
c(Q)=2*y(Q)*q/(q^2-x(Q)^2)
F3(Q)=c(Q)^2+1+q^2
N(Q)=Num(F3(Q)) in lowest terms
```

For six rank-one source fibers the checked orbit is `Q=nP+T`; for the rank-two source fiber `q=60/11` it is `Q=aG1+bG2+T`, always over the full order-8 torsion subgroup.

Exact details and source blobs are in:

- `exact-sequence-lock.json`
- `finite-window-lock.json`
- `cuboid-obstruction-adapter-lock.json`

## Finite window fixed exactly

Paper C's extended check certifies only:

```text
rank one:
  q = 20/21, 80/39, 24/7, 84/13, 48/55, 20/99
  1 <= n <= 200
  all 8 torsion translates
  9,600 cosets total
  Face-3 squares = 0

rank two:
  q = 60/11
  |a|,|b| <= 12, (a,b)!=(0,0)
  all 8 torsion translates
  4,992 cosets total
  Face-3 squares = 0
```

No all-multiples credit is imported.

## Exact cuboid obstruction

For any source point in the exact population, if a prime has odd valuation in the reduced numerator `N(Q)=Num(F3(Q))`, then `F3(Q)` is not a rational square. Paper C's cuboid reduction requires a candidate on that fiber to have `F3(Q)` a nonzero rational square. Thus odd numerator valuation is a valid same-point exclusion adapter.

Primitivity is only a proposed mechanism for forcing such an odd valuation uniformly. It is not itself the cuboid obstruction. In particular, Paper C records the exact counterexample `q=20/21`, `n=5`, primitive prime `29`, `v_29(N_5)=2`.

## New source-contract gaps found by 34-01

### 1. Full Mordell--Weil population is not yet certified

Paper C's conjecture is stated for every non-torsion rational point expressed in a free Mordell--Weil basis. Its `verify_ranks.gp` script calls PARI/GP `ellrank` and treats the returned independent points as generators, but does not call `ellsaturation` or otherwise certify that they generate the full free part.

PARI/GP 2.15.4 documentation distinguishes these facts: a tight rank interval plus the returned independent points proves a finite-index subgroup; saturation/full-basis credit is a separate obligation.

Therefore:

```text
TIGHT_RANK=true
SOURCE_POINTS_INDEPENDENT=true
FULL_MW_Z_BASIS_SOURCE_LOCKED=false
SOURCE_LATTICE_EQUALS_ALL_EqQ_MOD_TORSION=false
```

Stage34 must either certify the full basis/saturation for all seven fibers or source-lock that the Stage29 receiver intentionally targets only the finite-index source lattice.

### 2. Torsion-translated primitive-divisor theorem is not formulated

Paper C's displayed missing theorem is written for `N_n=Num(F3(nP))`, but its finite theorem and all-fiber conjecture quantify over every `nP+T`. A theorem for the untranslated sequence does not automatically cover every torsion translate.

### 3. Rank-two primitive-divisor semantics are not defined

Paper C says an analogous two-variable input would close `q=60/11`, but does not define a two-variable primitive ordering/divisibility sequence on `(a,b) in Z^2`.

Thus the Stage29 phrase `EFFECTIVE_ODD_MULTIPLICITY_PRIMITIVE_DIVISOR_THEOREM` is still too compressed to be a theorem target for the whole receiver.

## Arsenal check

After the exact object and missing weapon type were identified, the current Arsenal router was checked. No formal mathematical weapon directly supplies an odd-multiplicity primitive-divisor theorem for these elliptic orbit-value numerators, torsion translates, or the rank-two lattice.

Relevant reusable workflow only:

- `S30-WF02 IMMUTABLE_LAYERED_CERTIFICATE_REPLAY` for immutable source/certificate binding;
- `S30-WF03 ADAPTER_CREDIT_LAYER_FIREWALL` for keeping finite-window, adapter, receiver and endpoint credit separate.

No theorem is imported from Arsenal by topic similarity.

## Current exact next leaf

```text
RESOLVE_EXT_C_GLOBAL_POPULATION_CONTRACT:
  A. certify full Mordell--Weil basis/saturation for the seven source fibers,
     or narrow/source-lock the receiver population;
  B. define the translated rank-one orbit families needed for all torsion cosets;
  C. define a valid rank-two global indexing/primitive notion, or replace the
     primitive-divisor route there by another deterministic nonsquare theorem.
```

Only after this is exact should 34-02 classify theorem species.

## Firewalls

```text
ellrank tight rank != full saturated Mordell--Weil basis
untranslated nP theorem != all nP+T
one-variable primitive divisor != rank-two lattice theorem
EDS denominator B_n != Face-3 numerator N(Q)
primitive divisor != odd valuation
finite window != all multiples
seven-fiber closure != perfect-cuboid nonexistence
```
