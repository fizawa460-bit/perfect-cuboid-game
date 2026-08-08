# Stage14-s4b — coarse arithmetic clustering

Stage14-s4a showed that 483 of 490 active vertices have distinct exact Kummer square-class triples. Stage14-s4b therefore replaces exact-class equality by explainable coarse arithmetic signatures intended for later comparison with higher-degree Kummer/rank-jump strata.

The signature uses only discrete, reproducible invariants: unconditional PARI rank interval, full-2-torsion Selmer dimension, root number, a coarse `omega(2SXH)` bin, signs and prime-factor counts of the three Kummer square classes, a canonical-height/log(first-hit) bin, and leg orientation. Prime-support overlap between the Kummer class and the bad-prime set `p|2SXH` is audited separately.

No machine-learning clustering is used, and no finite cluster is promoted to an algebraic family without a geometric parametrization.

```text
STAGE14_S4B=COMPLETE_COARSE_ARITHMETIC_CLUSTER_AUDIT
COARSE_SIGNATURES_EXPLAINABLE_AND_GEOMETRY_COMPARABLE=true
FINITE_CLUSTERING_PROVES_ALGEBRAIC_STRATA=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s4c reverse-count higher-degree stratum proliferation required by the finite sqrt(B) signal
```
