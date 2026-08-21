# Stage29-07 — audited exact physical population / subcover counting adapter

```text
ROLE=R29-KUM4B
STATUS=AUDITED_PASS
KUM4A_INPUT=DISCHARGED_BY_29_04
```

## 1. Physical host and exact predicates

Keep the audited common host

```text
U(B)={0<a<b<c, gcd(a,b,c)=1, R=sqrt(a^2+b^2+c^2)<=B}.
```

Let the three face predicates be `F1,F2,F3` and the space predicate be `S`. Stage29-04 already proved pointwise, on the same F7 map, that these are exactly the triviality tests of the four remaining Kummer squareclasses after the two edge-ratio squareclasses are automatically trivial for physical integer edges.

Thus for any chosen subset `J` of the four predicates:

```text
physical object satisfies every predicate in J
iff
its positive edge-root point lifts rationally to the partial sign subcover for J.
```

A failed predicate means failure to lift over `Q` to that higher partial cover. It does not mean the object occupies a different rational sign sheet.

## 2. Positive-sheet / primitive normalization bijection

A positive rational point on a labeled partial cuboid cover has rational edge coordinates and the required rational diagonal coordinates. Clear denominators simultaneously so all represented coordinates are integral. If `g=gcd(a,b,c)`, every already-required integral face/space diagonal `r` is divisible by `g`: its defining equation gives `g^2|r^2`, and prime-by-prime valuations imply `g|r`. Dividing all represented coordinates by `g` therefore preserves integrality of every already-required diagonal and produces a primitive edge triple.

Imposing

```text
0<a<b<c
```

chooses the canonical ordering, and positivity chooses one sign representative. Conversely every primitive canonical physical object with the selected predicates supplies exactly one such positive labeled incidence point.

Therefore the population adapter is exact after

```text
PROJECTIVE_SCALE -> UNIQUE_PRIMITIVE_INTEGER_EDGE_REPRESENTATIVE
SIGN_ORBIT       -> POSITIVE_DIAGONAL_REPRESENTATIVE
PERMUTATION      -> CANONICAL_EDGE_ORDER.
```

No algebraic cover degree is interpreted as a physical multiplicity.

## 3. Exact physical height

For the primitive representative define

```text
H_R=sqrt(a^2+b^2+c^2).
```

This is exactly the frozen physical cutoff `R`. If `S` holds, the rational square-root coordinate `d` equals `R`; if `S` fails, `R` is still the same positive real norm even though `d` is not rational.

Hence

```text
HEIGHT_POWER_LOSS=0
COUNTING_CUTOFF=H_R<=B
STANDARD_WEIL_HEIGHT_IDENTIFICATION_CLAIM=false.
```

This is an exact arithmetic height dictionary, not a transfer theorem for Manin-type asymptotics.

## 4. Incidence hosts are the correct literal subcover counts

Let `M_k(B)` denote primitive canonical cuboids with exactly `k` integral face diagonals, `k=1,2,3`, and let

```text
N1=exactly one face + space
N2=exactly two faces + space
N3:=P=exactly three faces + space.
```

For `j=1,2,3`, attach to an object a choice of `j` among its satisfied face predicates. The exact count is

\[
I_j(B)=\sum_{k=j}^3 {k\choose j}M_k(B),
\]

and the space-positive part is

\[
I_j^S(B)=\sum_{k=j}^3 {k\choose j}N_k(B).
\]

Explicitly,

```text
I1=M1+2*M2+3*M3
I2=M2+3*M3
I3=M3

I1^S=N1+2*N2+3*P
I2^S=N2+3*P
I3^S=P.
```

These binomial multiplicities are exactly the number of selected-face incidence lifts and are not algebraic sign-sheet multiplicities.

## 5. Two-face floor and residual V4 ledger

For `j=2`, each incidence chooses two satisfied faces and lands on one Stage28 two-face floor. The two residual predicates are

```text
C=remaining third-face condition
S=space condition.
```

The exact four incidence counts are

```text
C=0,S=0 : M2-N2
C=0,S=1 : N2
C=1,S=0 : 3*(M3-P)
C=1,S=1 : 3*P,
```

whose sum is

```text
M2+3*M3=I2.
```

The factor `3` on the three-face strata is forced by the three choices of two-face subset. The residual V4 cover may have four algebraic sign lifts when both square roots exist, but the positive physical representative contributes one physical object per chosen incidence, not four.

## 6. Exact strata as lift-locus differences

The exact populations are recovered from rational lift loci and their complements:

```text
M1 = exactly one of F1,F2,F3 true, S arbitrary
N1 = exactly one face true and S true
M2 = exactly two faces true, S arbitrary
N2 = exactly two faces true and S true
M3 = all three faces true, S arbitrary
P  = all three faces true and S true.
```

Thus Stage16--20 populations are exactly encoded by the selected-subcover lift Boolean lattice, but not as six successive finite-cover floors.

```text
STAGE16_20_POPULATION_MASKS_HAVE_EXACT_SUBCOVER_LIFT_INTERPRETATION=true
EXACT_STRATA_ARE_SUCCESSIVE_SIGN_TOWER_FLOORS=false
BOOLEAN_16_EQUALS_SIGN_64=false.
```

## 7. KUM4B verdict

All items left open by Stage29-04 now have an exact dictionary:

```text
common host                              = physical edge-root / selected-predicate incidence host
YES-subcover vs NO-complement semantics = rational lift vs nonlift over Q
map direction                            = partial higher cover -> lower selected-predicate cover
rational sign multiplicity               = positive representative; not physical multiplicity
physical R-height                        = primitive Euclidean norm H_R
primitivity                              = exact gcd normalization
canonical ordering                       = 0<a<b<c
population multiplicity                  = binomial incidence coefficients C(k,j).
```

Therefore

```text
R29-KUM4B=DISCHARGED_EXACT_PHYSICAL_POPULATION_TO_SELECTED_SUBCOVER_INCIDENCE_ADAPTER
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true
TARGETED_BACKFLOW_REQUIRED=false
OLD_STAGE_CONTRACT_REPAIR_REQUIRED=false.
```

No Stage16--28 theorem changes. This is a Stage29 representation theorem for the already-frozen physical populations.

## 8. What is not transferred

```text
COVER_DEGREE_AS_POPULATION_SAVING=false
SIGN_SHEET_COUNT_AS_POPULATION_FACTOR=false
ASYMPTOTIC_TRANSFER_AUTOMATIC=false
LOCAL_SAVING_MULTIPLICATION=false
NEW_POPULATION_ASYMPTOTIC=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false.
```
