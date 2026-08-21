# Stage29-02ha — subcover tower bridges

The sign-cover model is useful because every partial cuboid condition is represented by forgetting some square roots.

## Two-face host and the Stage28 joint V4

Fix, for example, the two face roots `b2,b3`. Over the base plane function field

\[
F=\mathbf Q(x/z,y/z)
\]

consider the partial sign field obtained by adjoining the edge roots and these two face roots:

\[
F_{2f}=F(\sqrt{x},\sqrt{y},\sqrt{z},\sqrt{x+z},\sqrt{x+y})
\]

with the usual projective common-sign quotient understood.

The full endpoint then adds exactly the two remaining completion roots

\[
\sqrt{y+z}=b_1,
\qquad
\sqrt{x+y+z}=c.
\]

Generically these two square classes are independent over `F_2f`, hence

\[
F_{\rm endpoint}/F_{2f}
\]

is a `V4` extension.

This is the same abstract shape as the audited Stage29-02b / Stage28 joint completion field

```text
K(Y)(sqrt(f_face), sqrt(f_sp)).
```

The remaining adapter is to identify the chosen two-face sign subcover birationally, with exact boundary/multiplicity conventions, with the Stage28 toric base `Y=Bl_4(P1xP1)`.

```text
R29-KUM3A=TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
STATUS=OPEN_HIGH_VALUE
R29-KUM3B=JointV4AsResidualTwoSquareRootsOfFullSignTower
STATUS=PASS_FORMAL_CONDITIONAL_ON_KUM3A
```

## Population stages as partial lifts

The old population program can now be reinterpreted without making it the final proof method:

- edge-square data chooses the base-plane square-root chamber;
- each integral face diagonal means one more branch form has a rational square root;
- the integral space diagonal means the final `C` branch form has a rational square root;
- moving from one population to another is passage to a deeper subcover of the same finite `(Z/2)^6` tower.

This does **not** by itself transfer any Stage16–20 asymptotic, because physical height, primitivity, canonical ordering and exact-vs-at-least face multiplicity still need adapters. It does provide a single structural object on which those adapters can be formulated.

```text
R29-KUM4=Stage16To20PopulationMaskAsSignSubcoverLattice
STATUS=NEW_TARGETED_BACKFLOW_RECEIVER
HEIGHT_AND_PRIMITIVITY_TRANSFER=OPEN
```

## A new S4 bridge candidate

Stage29-02g independently found the generic residual modular group

\[
PSL_2(\mathbf Z/4)\cong S_4
\]

of order 24 after forgetting level-4 structure. The seven-line arrangement has an exact incidence automorphism group `S4` of order 24, acting faithfully on the four lines `{A1,A2,A3,C}`.

The equality of abstract groups is not enough to identify the actions. However, the coincidence is now precise enough to create a bounded receiver:

```text
R29-KUM5=IdentifyArrangementS4WithModularLevel4ResidualS4AndItsQLiftCocycle
STATUS=OPEN_PROMISING
```

If discharged, this would connect the elementary seven-square-root model directly to the Stage29-02g modular descent rather than treating the two foundations as unrelated.
