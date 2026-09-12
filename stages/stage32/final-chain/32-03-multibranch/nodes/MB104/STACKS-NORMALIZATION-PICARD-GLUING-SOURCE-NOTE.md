# Stage32 MB104 source note — normalization Picard kernel, glueing, and 2-torsion

Status: **SOURCE LOCK / STANDARD SINGULAR-CURVE PICARD INPUT / NO STAGE32 CREDIT BY ITSELF**

## Sources

Stacks Project, Algebraic Curves:

1. Section 53.15, `Glueing and squishing`, tag `0C1H`:
   https://stacks.math.columbia.edu/tag/0C1H
2. Lemma 53.15.5, tag `0C1M`:
   https://stacks.math.columbia.edu/tag/0C1M
3. Lemma 53.15.6, tag `0C1N`:
   https://stacks.math.columbia.edu/tag/0C1N
4. Section 53.17, `Torsion in the Picard group`, tag `0C1Y`:
   https://stacks.math.columbia.edu/tag/0C1Y

## Locked statements used by MB104

For a proper reduced curve, the normalization may be factored through elementary glueing/squishing steps as used in Stacks Section 53.17.

When two points on the same connected proper component are glued, Lemma 53.15.5 gives the multiplicative Picard-kernel contribution

```text
0 -> k^* -> Pic(X) -> Pic(X') -> 0
```

in the relevant same-component case.

When a tangent vector is squished, Lemma 53.15.6 gives the additive contribution

```text
0 -> (k,+) -> Pic(X) -> Pic(X') -> 0.
```

Over the Stage32 characteristic-zero ground field, `(k,+)` has no nonzero 2-torsion, whereas `k^*` contains the sign subgroup `mu_2`.

Therefore a 2-torsion line bundle on a singular proper curve whose pullback to the normalization is trivial can retain nontrivial multiplicative conductor/glueing data.  Triviality on the normalization alone does not imply triviality on the singular curve.

Section 53.17 uses exactly these glueing/squishing alternatives to control torsion in the Picard group.

## Scope firewall

This source note does **not** assert that an arbitrary Stage32 carrier has only nodal or multicross singularities.  A dual-graph `H^1(-,Z/2)` description is therefore used only when an additional nodal/multicross hypothesis is explicitly present.  The unconditional MB104 use is only the normalization-kernel distinction and the multiplicative-versus-additive 2-torsion separation above.
