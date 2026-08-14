# Stage24-50 literature recheck — rational face / nearly-perfect cuboids

ROLE=NOVELTY_AND_INDEPENDENT_STRUCTURE_AUDIT
STATUS=COMPLETE

Checkpoint50's unboundedness conclusion must not be presented as a novelty claim.

## Primary-source matches

### Meskhishvili 2015

Mamuka Meskhishvili, *Parametric Solutions for a Nearly-Perfect Cuboid*, arXiv:1502.02375.

The abstract defines the nearly-perfect cuboid class as cuboids where the only irrational among the relevant lengths is one face diagonal, and states that three rational one-parameter parametrizations are obtained.

This is directly adjacent to the Stage19 object type at the rational/similarity level: two face diagonals and the space diagonal are rational while the remaining face diagonal is irrational.

Stage24 does not import its parametrizations as the proof of the new lower bound. It records the paper as independent evidence that infinite rational NPC structure is known and that no novelty claim should be made merely from proving Stage19 unboundedness.

### Yoshida 2024/2026 revision

Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825, current revision dated March 22, 2026.

The paper defines rational face cuboids by rational edges, two face diagonals, and space diagonal, constructs a finite-to-one map from non-torsion elliptic-curve data to similarity classes, and proves in Corollary 4.6 that there are infinitely many rational face-cuboid classes up to similarity. It also proves infinitely many parameters with positive Mordell-Weil rank.

This is a strong independent elliptic-curve corroboration of the general Stage19-type arithmetic geometry. Because the paper's face-cuboid class is not used here to enforce the Stage24 exact primitive/canonical measure or the third-face nonsquare mask, it is not substituted for the repo-native proof.

## What Stage24 checkpoint50 actually adds to this repository

The checkpoint50 theorem candidate is intentionally narrower than a novelty claim. It provides a self-contained adapter into the exact Stage19 population:

1. explicit integer formulas inherited from Stage15-2;
2. a specific mixed-parity genus-one space-lift curve `p^4+q^4=17Z^2`;
3. exact primitive proof;
4. a fixed canonical physical cone under the actual `R=D` height;
5. a genus-five proof that the third-face-square exceptions inside this special family are finite;
6. a repo-native asymptotic lower statement `N2(B)>>sqrt(log B)` from elliptic height and real equidistribution.

No claim is made that the quartic family, the infinitude statement, or the general elliptic mechanism is new to mathematics.

```text
DIRECT_RELEVANT_LITERATURE_FOUND=true
RATIONAL_NPC_PARAMETRIZATIONS_KNOWN=true
RATIONAL_FACE_CUBOID_INFINITE_CLASSES_KNOWN=true
STAGE24_NOVELTY_CLAIM=false
LITERATURE_USED_AS_PRIMARY_PROOF=false
REPO_NATIVE_POPULATION_ADAPTER_PROVED_SEPARATELY=true
```
