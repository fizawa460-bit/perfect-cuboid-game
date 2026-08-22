# Stage29-16 — decision frontier after receiver compression

The purpose of this note is to separate three very different meanings of "remaining work" after the audited 29-15 four-class pass.

A receiver can be unfinished yet still be nondecisive. Conversely, a theorem can be very narrow but decisive because the repository already proved global coverage of the family to which it applies.

## 1. One currently named theorem with a proved direct nonexistence implication

The sharpest theorem-shaped target is

```text
K16-C3-PESCH-EXPONENT-ONE
  <- R29-PESCH-E1.
```

The repository has already audited the Master-Hit coverage of every primitive Euler brick. The remaining exponent-one statement is still conjectural, but its logical consequence is exact:

```text
PESCH_E1_IF_PROVED_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=true.
```

This makes it unusually attractive as a new-theorem target: it is narrower than a general rational-point theorem on the full endpoint surface and already comes with the required coverage adapter.

No theorem credit is granted here; the statement remains unproved.

## 2. Decision-capable kernels whose completion may or may not return an obstruction

The following kernels can, in principle, decide endpoint emptiness if the completed arithmetic returns an empty rational/adelic/lift set, but merely completing the computation or theorem adapter does not guarantee that outcome:

```text
K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
K16-C3-CAMPEDELLI-UNIFORM-TORSOR
K16-C3-BEAUVILLE-ONE-STEP-DESCENT
K16-C2-BRAUER-EXPLICIT-CHAIN
K16-C3-QWEB-CLIFFORD-OBSTRUCTION
K16-C3-MOVING-FIBER-ARITHMETIC
```

The exact one-way maps are different:

- full endpoint: a theorem directly classifying/emptying `U(Q)` is decisive;
- Campedelli: every endpoint Q-point pushes to every audited Q-defined quotient, so one quotient with empty `Q`-points is decisive;
- Beauville: the union over physical quadratic twists is exact; an empty one-step descent/etale-Brauer set is decisive;
- Brauer: an empty physical-open Brauer--Manin set is decisive;
- QWEB/Clifford: the receiver is explicitly defined to require an isotropy theorem strong enough to obstruct the endpoint;
- moving fibers: a genuinely exhaustive all-fiber theorem with exact reconstruction can be decisive.

These are not equivalent obstruction species and are not merged with one another.

## 3. Global-scale kernels that remain important but do not prove nonexistence by themselves

```text
K16-C3-M3-LOCAL-TO-GLOBAL
K16-C3-TERMINAL-P-OVER-M3
```

The first would legally transfer the exact local squareclass information to the primitive canonical Euler population. The second is the literal final survival ratio.

Even a theorem

```text
P(B)/M3(B) -> 0
```

would not imply `P(B)=0`. It would establish asymptotic rarity inside Euler cuboids, not nonexistence.

The population firewall therefore remains absolute:

```text
P/(M2+M3)->0 does not imply P/M3->0,
and P/M3->0 would not imply P=0.
```

## 4. Supporting kernels

The following active kernels are valuable but cannot decide the endpoint alone:

```text
K16-C2-LOWGENUS-PICARD-PRODUCTION
K16-C2-MODULAR-S4-ACTION
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
K16-C3-EXT-C-PRIMITIVE-DIVISOR
```

Reasons:

- low-genus classification lacks a theorem covering every rational point of the surface;
- the modular S4 adapter identifies arithmetic defect data but does not eliminate a defect class;
- EXT-E and EXT-C concern thin/special parametric loci rather than all endpoint candidates.

The K3-specific two-primary computation is not listed separately here because its active work has been execution-merged into `K16-C2-BRAUER-EXPLICIT-CHAIN`.

## 5. New-theorem target size

For later research planning, the nine Class-3 kernels split naturally by scope:

```text
narrow-specific:
  K16-C3-PESCH-EXPONENT-ONE
  K16-C3-EXT-C-PRIMITIVE-DIVISOR

medium / family-uniform:
  K16-C3-CAMPEDELLI-UNIFORM-TORSOR
  K16-C3-BEAUVILLE-ONE-STEP-DESCENT
  K16-C3-MOVING-FIBER-ARITHMETIC

broad / structural:
  K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
  K16-C3-QWEB-CLIFFORD-OBSTRUCTION
  K16-C3-M3-LOCAL-TO-GLOBAL
  K16-C3-TERMINAL-P-OVER-M3
```

This is a research-scope classification, not a probability estimate and not a claim about publishability or novelty. Any future theorem claim must still be literature-checked and independently audited.

## 6. Current endpoint consequence

```text
PERFECT_CUBOID_EXISTENCE_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
PERFECT_CUBOID_FINITENESS_PROVED=false
P_OVER_M3_SCALE_KNOWN=false
```

29-16 only compresses the exact residual frontier. It does not infer a solution from the number of remaining kernels.
