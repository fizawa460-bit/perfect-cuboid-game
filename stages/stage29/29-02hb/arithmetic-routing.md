# Arithmetic routing for the Campedelli quotients

## 1. One-way rational-point transfer

Every coordinate sign involution is defined over `Q`, and each enumerated kernel `H` is a subgroup of that rational deck group. Hence the quotient map is defined over `Q`.

On the physical open this gives

```text
U(Q) -> C_H(Q)
```

for each of the ten admissible kernels.

Therefore a proof that **one** audited Campedelli quotient has no rational points on the corresponding image open would imply that the perfect-cuboid rational locus is empty.

This is a strict one-way implication. A rational Campedelli point need not lift to a rational point upstairs.

## 2. Lift obstruction

For an etale degree-8 quotient with

```text
H ~= (Z/2)^3,
```

the geometric fiber above a rational quotient point is an `H`-torsor. Its arithmetic lifting class lies in

```text
H^1(Q,H).
```

Without local restrictions this set is not finite. Any claim of a finite twist list therefore requires a separate ramification/Selmer argument.

Receiver:

```text
R29-CAMP2=ArithmeticHTorsorDescentForTheTwoS4QuotientTypes
```

Required payload:

1. exact Q-model for one representative in each `8+2` orbit;
2. physical-open image and deleted boundary;
3. ramification set for the H-torsor classes;
4. local solubility filters;
5. finite Selmer-style twist set if provable;
6. exact lift criterion back to the full sign cover.

## 3. Involution descent below Campedelli

A classical Campedelli surface has seven nontrivial deck involutions. The literature studies the resulting quotient surfaces and their rational/Enriques behavior.

This creates a second bounded tower:

```text
perfect-cuboid surface
  -> Campedelli quotient C_H
     -> seven order-2 quotients
        -> rational / Enriques-type models.
```

Receiver:

```text
R29-CAMP3=SevenCampedelliInvolutionQuotientsRationalVsEnriquesLedger
```

The goal is not to claim that a rational quotient automatically solves the rational-point problem. The goal is to replace a `pg=7, K^2=16` endpoint by a small set of `pg=0, K^2=2` and then lower-complexity quotient models where explicit descent may be available.

## 4. Brauer compatibility

For classical Campedelli surfaces `pg=q=0` and the Picard group has 2-primary torsion associated with the `(Z/2)^3` fundamental group. This makes their Brauer theory qualitatively different from the full endpoint's rank-14 transcendental package.

Stage29-02f already eliminated odd-primary proper transcendental Brauer on the full endpoint. The Campedelli route therefore naturally asks whether the remaining obstruction can be transported into a finite 2-primary quotient computation.

Receiver:

```text
R29-CAMP4=CampedelliBrauerAndTwoPrimaryDescentCompatibilityWith29_02f
```

No Brauer--Manin obstruction is claimed at this stage.

## 5. Why only two quotient types matter first

The ten exact kernels fall into two orbits under the audited `S4=Aut_P2(D)` arrangement symmetry, of sizes eight and two. For first-pass arithmetic it is therefore sufficient to build one Q-model per orbit, while separately checking whether the geometric symmetry connecting kernels is Q-liftable in the required quotient category.

This last Q-lift issue is part of fresh audit and `R29-CAMP2`; the orbit count alone is not used to collapse arithmetic classes without proof.
