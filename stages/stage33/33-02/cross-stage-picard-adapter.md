# Stage33-02 — exact adapter from audited Stage32 Picard core

Stage33-02 may reuse the audited Stage32 Picard core because the mathematical object and source lock are identical, and the boundary selection is exact.

## Source identity

The Stage32 core was produced from:

```text
repo   = MichaelStollBayreuth/Verification
commit = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file   = Cuboids/cuboids.magma
blob   = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

Stage33-02 is locked to the same source. The audited Stage32 artifact is:

```text
workflow_run = 32614857845
artifact_id  = 9486641560
artifact_sha256 = cae5c9b5aa00d9a730510c9f0e01ab609acef9d759fcc93f64708da123d6813d
picard_core canonical sha256 = de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870
```

## Ordering identity

`run_sparse_picard_export.py` explicitly asserts

```text
#Cs = 92
#pts = 48
bdim = 140
```

and exports upstream classes `j=1..140` without reordering. It then converts those 140 classes to a primitive integral rank-64 Picard basis and stores them in `known_classes` in that same order.

The frozen Stage29 BR0A probe defines the 72 physical boundary generators by

```text
side_inds = [1..24]
exc_inds  = [#Cs+j : j=1..48]
```

Hence the exact Stage32-core rows are

```text
1..24, 93..140.
```

No matching, heuristic identification, or geometric relabeling is involved.

## Exact maps reconstructed

Let `G` be the audited primitive-basis Gram matrix and let `M` be the 72x64 matrix consisting of the rows above. Then:

```text
Div_D -> Pic(Sbar)     is represented by M;
restriction/pairing of boundary generators against the Picard basis is M*G;
boundary intersection matrix is M*G*M^T.
```

The artifact additionally contains the original direct Magma pairings of all 140 classes against the chosen 64 basis classes. Stage33 independently requires `M*G` to reproduce those raw exported pairings for all 72 selected boundary rows.

## Integral certification

Stage33 computes an exact Smith decomposition over `Z` rather than a rational-rank substitute. This yields:

- the exact integral kernel of `Div_D -> Pic`;
- the exact rank and torsion of `Pic / im(Div_D)`;
- the exact saturation index of the boundary image;
- an explicit basis of the saturated boundary-image lattice.

Thus the reuse is an explicit audited mathematical adapter, not generic infrastructure reuse and not automatic Stage32 theorem credit.
