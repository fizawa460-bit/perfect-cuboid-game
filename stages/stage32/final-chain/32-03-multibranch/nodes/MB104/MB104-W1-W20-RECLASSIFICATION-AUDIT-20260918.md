# Stage32 MB104 — W1--W20 shallow-scan reclassification audit — 2026-09-18

Status: **RECLASSIFIED / 5 HARD-DROP / 15 SOFT-PARK / 0 PROMOTE / NO CREDIT**

## Why this audit exists

The first wide-scan rounds used `DROP` too broadly.  A failed cheap test can mean either

1. the route architecture itself is impossible; or
2. only the first implementation failed.

This audit does **not** recompute W1--W20.  It reads the retained Round A--D checkpoints and reclassifies the meaning of their conclusions.

Definitions:

- **HARD-DROP** — the exact architecture is incompatible with retained facts.  Do not rerun it unless the architecture changes.
- **SOFT-PARK** — the tested implementation failed, but the broader direction remains mathematically open.
- **PROMOTE** — shallow evidence already gives positive closing pressure.
- **UNCLEAR** — retained evidence is insufficient even for that distinction.

## Classification

| Route | New status | What is actually dead | What is still alive | Revisit |
|---|---|---|---|---|
| W1 Bogomolov--Reider superabundance | **SOFT-PARK** | Full genus-defect cluster has negative Bogomolov discriminant; that exact Serre package cannot destabilize. | A smaller canonical/source-complete Cayley--Bacharach cluster could change c2 and restore instability. | MEDIUM |
| W2 symbolic/Waldschmidt non-effectivity | **HARD-DROP** | h0(O(D_l))>0 for every l>=1, so the exact ray is effective. | Irreducibility or singular-member questions are different routes, not W2 non-effectivity. | NONE |
| W3 Aut(S)-norm invariant section | **SOFT-PARK** | The norm class is big/positive and known low-degree tests give no overload. | A full invariant-ring or representation-theoretic vanishing theorem could still obstruct the required invariant section. | MEDIUM |
| W4 K3 quotient pushdown | **SOFT-PARK** | Parity, Hodge and sampled fibration tests are compatible. | The full rank-20 K3 lattice / nef-effective cone for the seven explicit pushdown rays was not computed. | HIGH |
| W5 higher symmetric differentials | **SOFT-PARK** | Order-2 and every fixed finite jet-depth architecture saturate and cannot count 8l branches. | An adaptive/unbounded-order global differential construction growing with l is not ruled out. | HIGH |
| W6 modular-form valence on X(8)xX(8) | **SOFT-PARK** | Pure factorwise valence is exactly saturated on the zero-quartic fibers. | A genuinely coupled two-factor modular relation or bivariate divisor-slope theorem is not ruled out. | MEDIUM-HIGH |
| W7 cyclic/abelian-cover BMY | **SOFT-PARK** | The smooth-branch cyclic-cover BMY slack stays positive for all n,l. | Singular branch-cover corrections or a different abelian-cover arrangement could alter the quadratic coefficient; not analyzed. | LOW-MEDIUM |
| W8 simultaneous coordinate-sign quotient RH | **HARD-DROP** | None of the seven coordinate-sign involutions preserves the active support, so none acts on the carrier normalization as required. | Other quotient maps are W4/different routes; the W8 simultaneous-involution architecture has no source object. | NONE |
| W9 finite-characteristic specialization | **SOFT-PARK** | Bare specialization does not preserve integral normalization-genus-one packet strongly enough for reverse exclusion. | A proper stable-map/packet compactification or specialization theorem could make the idea valid. | LOW |
| W10 ambient fat-point zero-Hilbert obstruction | **HARD-DROP** | The exact degree/multiplicity graded pieces are nonzero for all l; h0(D_l)>=168l^2-56l+8. | Hilbert methods for irreducibility/singularity are different routes, not W10 vanishing. | NONE |
| W11 elliptic normalization linear-series collapse | **SOFT-PARK** | Degree and h0 counts comfortably accommodate the saturated 112l-point divisor. | Special relations among the seven ambient sections, beyond bare elliptic RR/Abel dimension, remain possible. | MEDIUM |
| W12 receiver-preserving degeneration | **SOFT-PARK** | Ordinary flat degeneration does not preserve integrality, normalization genus or exact branch packet. | A degeneration with a proved compactified receiver/specialization theorem could still work. | LOW-MEDIUM |
| W13 stable factorization / fixed component | **SOFT-PARK** | Known low-degree curves reduce the only null candidates to zero quartics, which are nonfixed. | A source-complete effective/nef-cone theorem could reveal other forced components. | MEDIUM-HIGH |
| W14 individual zero-quartic fixedness | **HARD-DROP** | Retained primitive-rank leaf proves explicit nonzero restriction and both active zero quartics nonfixed for every l>=1. | The exact W14 claim is settled negatively; broader fixed-component ideas belong to W13. | NONE |
| W15 joint zero-quartic restriction-rank fixedness | **HARD-DROP** | For active 000707, Q0 union Q1 is connected with H0(O_Z)=k, and retained primitive section restricts nonzero; the joint restriction image is nonzero rank 1, so it cannot force one quartic fixed. | Other global relations on the two quartics are different routes. | NONE |
| W16 minimal Cayley--Bacharach conductor subcluster | **SOFT-PARK** | The obvious source-complete length-112l cluster C intersect B_E yields a tautological split Serre bundle. | A nontrivial canonical proper CB subcluster with small c2 is not ruled out and would be numerically strong. | HIGH |
| W17 support-stabilizer carrier dichotomy | **SOFT-PARK** | The first invariant/non-invariant numerical checks are both packet-compatible. | A stronger quotient theorem in the invariant case or forced intersection theorem in the non-invariant case could still close. | MEDIUM |
| W18 elliptic projection / secant-center capacity | **SOFT-PARK** | Generic linear secant/collision count leaves 112l-49 positive slack. | Cuboid-specific special-position/secant-defect geometry could impose extra nonlinear conditions. | MEDIUM-HIGH |
| W19 adaptive Wronskian / unbounded jets | **SOFT-PARK** | Equal images of distinct branches force no ramification; naive unit charging is far below Wronskian capacity. | A global theorem forcing high-order ramification/contact from the cuboid packet is not ruled out; fixed-jet methods alone are hard-dead. | MEDIUM |
| W20 support-hyperplane residue / Abel | **SOFT-PARK** | The basic Abel relation is tautological and ordinary principal-part dimensions have ample room. | A cuboid-specific global residue/moment identity fixing principal parts across nodes is not ruled out. | MEDIUM |

## HARD-DROP set

Exactly five routes are hard-dead **in their stated architecture**:

```
W2  non-effectivity / Waldschmidt vanishing
W8  simultaneous coordinate-sign involution RH
W10 exact fat-point graded-piece vanishing
W14 individual zero-quartic fixedness
W15 joint zero-quartic fixedness
```

### W2 / W10

These are genuinely closed because

```
h0(O_S(D_l)) >= 168l^2-56l+8 >0
```

for every `l>=1`.  The exact ray is effective and its exact graded piece does not vanish.

This does **not** ban Hilbert/effective-cone methods aimed at irreducibility or singular-member structure; those would be different architectures.

### W8

No coordinate-sign involution preserves the active support.  Therefore the proposed simultaneous involution action on the genus-one normalization does not exist.  Other quotient-map methods remain separate.

### W14

The retained primitive-rank leaf proves explicit characteristic-zero sections nonzero on the two active zero quartics.  Both are nonfixed for every `l>=1`.

### W15

For `000707`, the two zero quartics form a connected union `Z=Q0 union Q1` with

```
H0(O_Z)=k.
```

The retained primitive section `F` restricts nontrivially to `Q0`.  A global section on the connected union cannot be nonzero constant on `Q0` and zero on `Q1` across their intersection points, so its restriction to `Z` is nonzero.  Hence

```
rank(H0(A) -> H0(O_Z))=1.
```

The joint-rank fixed-component architecture is therefore closed negatively.

## SOFT-PARK set

The other fifteen routes were previously over-labelled as DROP:

```
W1 W3 W4 W5 W6 W7 W9 W11 W12 W13 W16 W17 W18 W19 W20
```

They must remain in the research portfolio.

The most useful distinction is the **hard subclaim** already killed versus the **broader direction** still alive.

Examples:

- W1: full-defect Reider is dead; smaller canonical CB subcluster remains open.
- W4: easy K3 parity/Hodge/fibration tests are dead; full rank-20 lattice/nef-cone test remains open.
- W5: fixed-order/fixed-finite-jet symmetric differentials are dead; adaptive order growing with `l` remains open.
- W6: factorwise valence is dead; coupled two-factor modular identities remain open.
- W13: known zero quartics are not fixed; a complete effective-cone theorem could still force another component.
- W16: the obvious CB cluster is tautologically split; a nontrivial canonical proper subcluster remains open.
- W18: generic secant dimension has slack; cuboid-specific secant defect/special-position geometry remains open.
- W19: naive ramification charging is dead; a theorem forcing high contact from global packet geometry remains open.

## Current priority among SOFT-PARK routes

This is **not** a proof ranking; it is a research-efficiency ranking for future revisit.

Higher-value soft parks:

```
W4   full K3 lattice / nef-effective cone
W5   adaptive higher symmetric differentials
W6   coupled two-factor modular relation
W13  complete effective-cone / stable-base theorem
W16  nontrivial canonical CB subcluster
W18  cuboid-specific secant defect
```

The remaining soft parks stay retained but have weaker current pressure.

## PROMOTE / UNCLEAR

After this audit:

```
PROMOTE = none
UNCLEAR = none
```

This does **not** mean no route can work.  It means none of W1--W20 currently has enough positive shallow evidence to justify abandoning the broad scan and going deep.

## Operating correction

Future wide scans must record two fields separately:

```
tested_architecture_status
broader_direction_status
```

A cheap-test failure may set the first to HARD-DROP while leaving the second SOFT-PARK.

Only a source-complete contradiction against the broader direction may remove it from the portfolio.

No mathematical credit changes.
