# Stage14-s4b — coarse arithmetic clustering

Stage14-s4a showed that 483 of 490 active vertices have distinct exact Kummer square-class triples. Stage14-s4b therefore replaces exact-class equality by explainable coarse arithmetic signatures intended for later comparison with higher-degree Kummer/rank-jump strata.

The signature uses only discrete, reproducible invariants: unconditional PARI rank interval, full-2-torsion Selmer dimension, root number, a coarse `omega(2SXH)` bin, signs and prime-factor counts of the three Kummer square classes, a canonical-height/log(first-hit) bin, and leg orientation. Prime-support overlap between the Kummer class and the bad-prime set `p|2SXH` is audited separately.

## Finite result

```text
active vertices                  490
coarse signatures                393
largest coarse cluster             4
top 10 clusters covered           38
top 20 clusters covered           68
singleton signatures             326
Kummer support subset of 2SXH    490 / 490
mean support Jaccard              0.5226967477
```

Thus even deliberately coarse, geometry-comparable invariants do not collapse the active population to a few dominant signatures. The rank/Selmer/root layer is much simpler: the two dominant types are

```text
rank 1, Selmer dim 3, root -1    189
rank 2, Selmer dim 4, root +1    187
```

so the finite picture is two-layered: coarse rank/parity type is concentrated, while the physical small-point/descent fingerprint remains strongly dispersed.

Every Kummer square-class prime support lies inside the moving bad-prime support `p|2SXH`, as expected from the split 2-descent architecture. The mean support Jaccard is only about `0.523`, so each first-hit class typically selects a proper subset of the available bad primes rather than using a universal support pattern.

No machine-learning clustering is used, and no finite cluster is promoted to an algebraic family without a geometric parametrization.

```text
STAGE14_S4B=COMPLETE_COARSE_ARITHMETIC_CLUSTER_AUDIT
COARSE_SIGNATURES_EXPLAINABLE_AND_GEOMETRY_COMPARABLE=true
FEW_DOMINANT_COARSE_SMALL_POINT_CLASSES_OBSERVED=false
RANK_SELMER_ROOT_LAYER_CONCENTRATED=true
FINITE_CLUSTERING_PROVES_ALGEBRAIC_STRATA=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s4c reverse-count higher-degree stratum proliferation required by the finite sqrt(B) signal
```
