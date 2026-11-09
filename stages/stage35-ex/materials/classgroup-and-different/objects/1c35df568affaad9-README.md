# row388 reproduction

Main proof: PROOF.md. New author's exact verification passes; independent audit pending.

Pure Python (no third-party dependencies):

```
python verify_row388.py > replay388.json
python verify_frontier388.py > frontier_replay.json
```

Compare the parsed JSON to results388.json and frontier388.json. The first checks all integer kernel witnesses, tracked pivot combinations, unit minors, the 55-dimensional local image and 44 global square relations, and the factored principalization algorithm. The second checks the complete finite factorbase projection. It does not certify class-group generation.

For full arithmetic replay, install python-flint (author: 0.9.0) and run:

```
python rebuild_profiles388.py
python minkowski_baseline388.py
```

The first recomputes every exact principal ideal valuation, both dyadic unit parts, all 4,344 support-prime decompositions and 359 additional decompositions, and asserts equality with the supplied data. Expect about two minutes. It reuses the included byte-bound audited parent381 arithmetic. Pure Python checks alone do not independently rederive number-field ideal arithmetic.

The 99 integer-kernel vectors are formal exponent relations yielding units; they are not 99 independent algebraic units. The full class-group 2-rank, qstar and signed −30 exclusion remain unknown.

parent381 contains only the parent modules/data needed by this replay. exploration contains the bounded 15 ideal reductions and is not a basis or exhaustiveness certificate.
