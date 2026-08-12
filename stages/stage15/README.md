# Stage15-0/1 — comparison interface and paired enumerator

Base snapshot: `b4b5b901d8707d7a9d9d9258b6772d524a9df882` (merged Stage15 roadmap, PR #823).

This directory implements the first two gates of the merged Stage15 roadmap. Stage15 compares the exactly-two-face family without space-diagonal integrality, `B_2(B)`, against its integral-space-diagonal subfamily, `A_2(B)`, under one common geometric cutoff.

## Stage15-0 — exact comparison contract

For positive integer edges define

\[
R^2=a^2+b^2+c^2,
\qquad 0<a<b<c,
\qquad \gcd(a,b,c)=1.
\]

Let `I_ab`, `I_ac`, `I_bc` be the exact integer-square predicates for the three face sums. The ambient exactly-two family is

\[
\mathcal B_2(B)=\{(a,b,c):R^2\le B^2,\ I_{ab}+I_{ac}+I_{bc}=2\},
\]

with the primitive/canonical conditions above understood. Its integral-space-diagonal subfamily is

\[
\mathcal A_2(B)=\{(a,b,c)\in\mathcal B_2(B):R^2\text{ is a square}\}.
\]

### Cutoff equivalence

If `(a,b,c)` lies in `A_2`, write `d=sqrt(R^2)` with `d>0`. Then `R=d` as positive real numbers, hence

\[
R\le B\iff d\le B.
\]

Therefore the Stage15 primary cutoff is exactly the Stage14 cutoff after restriction to `A_2`; no denominator, height, or quantifier adapter is hidden here.

### Inclusion and multiplicity

`A_2(B) subset B_2(B)` is literal set inclusion: `A_2` adds only the exact predicate that `R^2` is a square.

An exactly-two object has a unique edge shared by its two integral faces. Each integral face has a unique scale-times-primitive Euclid decomposition. Gluing those two face certificates along their common edge reconstructs the unordered edge triple; sorting gives the unique canonical representative `a<b<c`. Consequently the paired generator has glue multiplicity one on exactly-two objects.

A triple-face object has three possible shared edges and therefore exactly three glue witnesses. Triple-face objects are retained separately as `B_3`/`A_3`; they are never silently folded into `M_2`/`N_2`.

### Reuse matrix

| Stage12–14 component | Stage15 status | Reason |
|---|---|---|
| `0<a<b<c`, `gcd(a,b,c)=1` | exact reusable | same physical convention |
| exact integer-square face predicates | exact reusable | same arithmetic predicate |
| primitive Euclid decomposition of one square face | exact reusable | independent of space-diagonal integrality |
| shared-edge gluing multiplicity | exact reusable after the explicit `R^2<=B^2` adapter | exactly-two has one shared edge; triples have three |
| Stage14 numerical finite counts | validation only | usable only after restricting Stage15 output to `R^2` square |
| Stage14 nested space-diagonal generator | `A_2` cross-check only | its nesting already encodes integral space diagonal, so it cannot generate ambient `B_2` |
| Stage14 raw-pair graph identity | `A_2` reusable; `B_2` needs its own graph statement if later needed | Stage14 graph was defined on the integral-space-diagonal physical family |
| Stage14 elliptic-fiber degree bound | forbidden cross-promotion to `B_2` | the fiber and height comparison use the integral-space-diagonal structure |
| Stage14 whole-family `N_2(B) << B^(1/2+o(1))` | `A_2` theorem only | says nothing directly about `M_2(B)` |
| Stage14 MAIN/T/S strict-saving receivers | forbidden cross-promotion | their hypotheses retain the Stage14 integral-space-diagonal measure and parameter system |
| Stage12/13 one-face asymptotics | diagnostic/context only for `B_2` | proved under the inherited integral-space-diagonal population |

The authoritative Stage14 lock used by Stage15-1 validation is `stages/stage14/data/14-num-alpha11-diag8/extended_denominator_summary.json`. At `B=100000` it records exactly-two directional counts `[33,33,23]`, total `89`, and zero triples through the tested range. The final theorem source remains `docs/stage14-final-self-contained.md`; review bundles are not imported as independent proof inputs.

```text
STAGE15_COMPARISON_CONTRACT_PROVED=true
STAGE15_0_FORBIDDEN_CROSS_PROMOTION_RECORDED=true
STAGE15_0_EXACT_TWO_TRIPLE_SEPARATION=true
```

## Stage15-1 — exact paired enumerator

Implementation: `stages/stage15/scripts/paired_enumerator.py`.

The enumerator generates every integer Pythagorean triangle with face hypotenuse at most `B`, indexes each triangle by either leg, and glues pairs sharing one leg. This is exhaustive because every member of `B_2(B)` has two integral faces and therefore supplies exactly such a pair; each face hypotenuse is `< R <= B`. Every candidate is then checked with integer arithmetic only:

- `R^2<=B^2` (no floating point cutoff);
- strict canonical ordering;
- global primitiveness;
- exact three-face square mask;
- exact-two versus triple separation;
- exact space-square predicate;
- deterministic Pythagorean certificates for the two integral faces;
- exact lower/upper square defects of the third face;
- glue-source multiplicity.

The output can retain `(a,b,c)`, `R^2`, integral-space status and `d`, face mask, direction/shared edge, third-face defect, primitive/canonical flags, the two Euclid certificates `(m,n,scale,hypotenuse)`, and deduplication provenance.

Validation: `stages/stage15/replay/validate_paired_enumerator.py`.

1. Independent brute force at `B=300` agrees object-for-object, including face mask and space-square status.
2. At `B=100000`, restricting to `R^2` square reproduces the frozen Stage14 exactly-two direction vector `[33,33,23]` and total `89`, with `N_3=0`.
3. Every exactly-two object has one glue source; every triple has three.

`stages/stage15/evidence/stage15_0_1_validation.json` freezes these validation facts only. The ambient counts in that file are not promoted to an asymptotic or Stage15-3 inference.

```text
BRUTE_FORCE_B300_MATCH=true
STAGE14_B100K_N2_LOCK_MATCH=true
EXACT_TWO_GLUE_MULTIPLICITY_ONE=true
TRIPLE_GLUE_MULTIPLICITY_THREE=true
PAIRED_ENUMERATOR_VALIDATED=true
STAGE15_1_NUMERICAL_ASYMPTOTIC_CLAIM=false
```
