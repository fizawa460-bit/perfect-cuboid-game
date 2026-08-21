# Stage29-08 — audited source refresh and coverage resolution

## Peschmann source sequence

The Stage29-02hd screen used `arXiv:2604.09328` and `arXiv:2604.28072`. Stage29-08 also checks the later `arXiv:2605.00573`.

### arXiv:2604.09328

Audited-use facts:

- two Euclid pairs give two automatic face diagonals;
- Master and H-total are the third-face and space square conditions;
- perfect cuboid implies a nondegenerate rational point on the genus-3 curve;
- the specialized converse is not used without its square-factor/coprimality verification.

### arXiv:2604.28072 — Theorem 2.4 independently audited

This source does not merely make an abstract coverage claim. Theorem 2.4 gives a reduction theorem with proof: every primitive Euler brick, after choosing its unique odd edge `X`, has

```text
(X,Y,Z)=(U1U2/g, V1U2/g, U1V2/g),
g=gcd(U1,U2),
```

for unique primitive Euclid pairs, and the third-face condition makes the resulting tuple a Master-Hit.

Fresh Stage29 audit independently re-derived every load-bearing step (`gcd(d,e)=1`, Euclid uniqueness, the scaling identity, and the Master square) and accepts the theorem.

```text
PESCHMANN_GLOBAL_EULER_BRICK_COVERAGE_CERTIFIED=true
PESCHMANN_GLOBAL_ENDPOINT_COVERAGE_VIA_MASTER_HITS=true
R29-PESCH-COV=DISCHARGED_BY_INDEPENDENT_PROOF_AUDIT
```

The 1,072-fiber nonexistence theorem remains finite-fiber only.

### arXiv:2605.00573 — genuine source contradiction, not a theorem veto

The later source explicitly says in Remark 2.3 that it does not claim every primitive body cuboid arises from a Master-Hit. This conflicts with the previous day's Theorem 2.4.

The audit records the contradiction rather than silently harmonizing the prose:

```text
PESCHMANN_SOURCE_CONTRADICTION_PRESENT=true
EARLIER_THEOREM_HAS_EXPLICIT_PROOF=true
EARLIER_THEOREM_INDEPENDENTLY_RECHECKED=true
SOURCE_CONTRADICTION_INVALIDATES_CHECKED_THEOREM=false
```

Stage29 coverage is certified from the independently checked proof, not from authorial consistency.

## May-2026 Mordell-Weil fibration scope

The May source gives the genus-one quartic `H_mn`, Weierstrass model `E_mn`, and rational function `tau` returning `t^2`. The exact lift criterion has a domain restriction:

```text
P in E_mn(Q) \ ({O} union T_tau),
tau(P) in Q_{>0}^square,
```

followed by positivity, parity and coprimality checks on the reduced Euclid pair. `T_tau` is the two-torsion pole set of `tau`.

The total `(m,n)` fibration is globally covering on the Euler-brick marginal because of the audited reduction theorem. A bounded Mordell-Weil enumeration is not exhaustive.

```text
PESCH_TOTAL_FIBRATION_GLOBAL_MARGINAL_COVERAGE=true
BOUNDED_MW_ENUMERATION_GLOBAL_COVERAGE=false
R29-PESCH2=OPEN_BOUNDED_FIBRATION_CLASS_AND_POLARIZATION_MATCH
```

## Exponent-one blocker

Conjecture 4.1 remains explicitly conjectural. Finite verification does not prove it. But the coverage dependency is now gone: if the universal exponent-one blocker is proved for all Master-Hits, the global reduction theorem immediately rules out every perfect cuboid.

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER
PESCH_E1_IF_PROVED_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=true
PESCH_E1_CURRENTLY_PROVED=false
FINITE_DATABASE_IS_GLOBAL_THEOREM=false
```
