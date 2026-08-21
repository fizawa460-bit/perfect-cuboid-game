# Stage29-02hc source lock — audited scope

## S1 — Suciu, non-Fano characteristic and covering package

Alexander I. Suciu, **Fundamental groups of line arrangements: Enumerative aspects**, Contemporary Mathematics 276 (2001), 43–79, arXiv `math/0010105`, DOI `10.1090/conm/276/04510`.

Load-bearing locators:

- §6.1: projective arrangement complement has `H1=Z^(n-1)`; the compact branched cover has deck `(Z/N)^(n-1)` and minimal desingularization `M_N(A)`;
- Theorem 6.3: Chern-number formulas;
- Theorem 6.5: compact-cover `b1` via torsion-character depths;
- Example 10.5 / Figure 6: non-Fano polynomial `xyz(x-y)(x-z)(y-z)(x+y-z)`, `n=7,s=9,m2=3,m3=6`, characteristic varieties, `rho`, compact formula `b1(M_N)=9(N-1)(N-2)`, and specialized Chern formulas.

Audit repair: Example 10.5's displayed

```text
b1(X_N)=9N^2-3 (N even), 9N^2-2 (N odd)
```

is central-arrangement unbranched-cover data.  Suciu also records the central/projective product splitting.  It must not be copied verbatim to the endpoint's projective degree-64 open cover.  At `N=2` the audited values are central `33`, projective `32`.

## S2 — Hirzebruch original construction

Friedrich Hirzebruch, **Arrangements of Lines and Algebraic Surfaces**, *Arithmetic and Geometry II*, Progress in Mathematics 36 (1983), 113–140, DOI `10.1007/978-1-4757-9286-7_7`.

Use: original branched abelian/Kummer covering-surface construction and Chern-number method.

## S3 — non-Fano naming/incidence cross-check

Hal Schenck and Ştefan O. Tohăneanu, **The Orlik-Terao algebra and 2-formality**, Mathematical Research Letters 16 (2009), 171–182, arXiv `0901.0253`, DOI `10.4310/MRL.2009.v16.n1.a17`.

Example 1.7 identifies the non-Fano arrangement as the unique seven-line projective configuration with six triple points.  This is only a naming/incidence cross-check; the PR's exact `PGL3(Q)` branch transformation is stronger.

## S4 — cuboid endpoint baseline

Damiano Testa and Michael Stoll, **Curves on the surface of cuboids**, Mathematics of Computation, DOI `10.1090/mcom/4238`, arXiv `1009.0388`.

Use: audited cuboid equations, 48 A1 singularities, minimal-resolution invariants, Picard data and automorphisms.

## Q-form source firewall

None of S1–S3 identifies the **cuboid Q-form** with the standard non-Fano Kummer Q-form.  Fresh exact audit finds that the branch arrangements are `PGL3(Q)`-equivalent but none of the 24 rational arrangement equivalences lifts between the two standard Kummer Q-forms; all lift over `Q(i)`.

Therefore literature geometry may be imported over `Qbar/Q(i)`, while arithmetic claims about a displayed standard non-Fano Q-model require the explicit constant-sign twist adapter.

## Novelty firewall

Broad searches did not surface a source stating the cuboid recognition in this exact form, but search absence is not a novelty theorem.

```text
LITERATURE_NOVELTY_CLAIM=false
NOVELTY_IN_REPO=HIGH_VALUE_NAMED_RECOGNITION_ADAPTER_ON_F7
INDEPENDENT_FOUNDATION=false
SOURCE_LOCK_AUDIT=PASS_AFTER_CENTRAL_PROJECTIVE_AND_QFORM_SCOPE_REPAIR
```
