# Stage14-bridge2 — translate the p=7 shared-edge signature into the Stage14 local-state system

## Purpose

Stage14-num-alpha11-diag4 found a reproducible finite direction association with

```text
7 | shared edge
```

inside the exact B=500m exactly-two population. Stage14-num-alpha11-diag5 then showed that this association survives equal-space-diagonal and equal-face-component reweighting.

Bridge2 does not promote that finite association to an asymptotic law. Its task is to identify the exact proof-side object represented by `7|shared edge`, and to hand the smallest falsifiable local/chamber test to the proof routes.

Authoritative numerical sources:

```text
SOURCE_NUM_STAGE=Stage14-num-alpha11-diag4 + Stage14-num-alpha11-diag5
SOURCE_NUM_PR=310,312
SOURCE_NUM_MERGE_SHA=b41f428dc4ffc522088fdf6f4b7d7cecb6fa4ef8,cc78cb01496d9fe247f1511f32d54ecb70f6f813
FINITE_SCOPE=B<=500000000 exact exactly-two population, 3495 objects
```

The frozen diag4 contingency is

```text
7 ∤ shared : (a,b,c)=(616,492,274)
7 | shared : (a,b,c)=(758,879,476)
Holm-adjusted p = 3.194718059358186e-05
Cramer's V      = 0.0872267549763834
```

and diag5 preserves the ordering after the two tested dependence reweightings. These statistics are calibration/finite evidence only.

---

## 1. Exact physical pair coordinates

For a canonical exactly-two cuboid, let

```text
e = shared edge,
(e,x) = first integral face,
(e,y) = second integral face,
x<y.
```

The direction labels are exactly the three archimedean chambers

```text
a : 1 < x/e < y/e,
b : x/e < 1 < y/e,
c : x/e < y/e < 1.
```

For each physical face reduce independently by

```text
g_i = gcd(e,other_i),
shared_i = e/g_i,
other_i  = other_i/g_i.
```

The primitive face has one odd leg `S_i` and one even leg `X_i`. Therefore the physical shared edge may become either

```text
shared_i=S_i
```

or

```text
shared_i=X_i
```

after primitive reduction. Bridge2 deliberately does not assume one parity chart.

The deterministic audit verifies the chamber dictionary on every frozen B500m object.

---

## 2. Algebraization of `7 | shared edge`

Global primitivity gives the exact implication

```text
7|e
=>
7 remains in at least one primitive shared_i.
```

Indeed, if the factor 7 disappeared into both face gcds then `7|e,x,y`, contradicting `gcd(e,x,y)=1`.

The converse is immediate. Hence

```text
7|e
iff
7 divides the primitive shared leg in at least one of the two face orientations.
```

Now recover primitive Euclid parameters

```text
S_i=m_i^2-n_i^2=(m_i-n_i)(m_i+n_i),
X_i=2m_i n_i.
```

Thus each occurrence of the p=7 shared-edge state lands in one of the existing s5 moving-factor columns:

```text
shared role S:
  7|S_i
  iff 7|(m_i-n_i) or 7|(m_i+n_i);

shared role X:
  7|X_i
  iff 7|m_i or 7|n_i.
```

There is therefore no new mysterious `p=7` variable. The num observable is an incidence condition on the already-owned four linear Euclid columns

```text
m, n, m-n, m+n.
```

This is the bridge2 L3/L4 translation.

---

## 3. Exact receiving local rows at p=7

Merged s5c/s5d already classify the odd local rows.

For `p|S`:

```text
selected S/12:   chi_p(a3)=+1     (after product-square compression),
unselected S:    chi_p(d3)=+1.
```

For `p|X`:

```text
selected X/13 requires chi_p(-1)=+1,
unselected X requires chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

At `p=7`,

```text
(-1/7)=-1.
```

Therefore

```text
selected X/13 at p=7: impossible,
unselected X at p=7: automatic for every unit d2.
```

while an S-row still carries a one-character condition.

So the p=7 shared-edge observable has a genuine proof-side **row-type asymmetry** after primitive face reduction:

```text
S-role incidence != X-role incidence
```

inside the full local 2-descent state system.

This does not yet prove that this asymmetry explains the finite direction vector; it identifies exactly what must be tested.

---

## 4. The missing-third-face QR_0 fact is not the mechanism

Diag4 exhaustively checked the finite-field universe

```text
x^2+y^2 is QR_0,
x^2+z^2 is QR_0,
x^2+y^2+z^2 is a nonzero QR.
```

At p=7 it found

```text
54/54
```

states also satisfy

```text
y^2+z^2 is QR_0.
```

Bridge2 reproduces this exact finite-field fact.

Hence after conditioning on the two integral-face residue conditions plus unit space diagonal, the missing-third-face Legendre test contributes **no independent p=7 filter**.

In particular, Stage13's `lambda_7=3/4` belongs to the different one-face -> additional-face conditioning problem and is not a null model for this Stage14 two-face state.

The live p=7 mechanism is instead the shared-leg valuation / s5-row packet described above.

---

## 5. Frozen B500m row-packet decomposition

The bridge audit applies only deterministic transformations to the already-frozen 3495-row B500m source. It introduces no new census.

First, both primitive shared-leg roles actually occur in every direction. The ordered role pairs `(face1|face2)` are

```text
          S|S   S|X   X|S   X|X
a          340   256   292   486
b          300   257   286   528
c          160   138   130   322
```

Thus an S-only translation would have been wrong; the X-row must be retained.

Among objects with `7|e`, let `kappa_7` be the number of primitive face orientations in which 7 survives in the shared primitive leg. Then

```text
          kappa_7=1   kappa_7=2
a              437           321
b              540           339
c              251           225
```

so the double-bad fractions within the `7|e` class are approximately

```text
a  0.42348
b  0.38567
c  0.47269.
```

Counting local-row incidences, rather than objects, gives

```text
          S-row incidences   X-row incidences   X fraction
a                   530                549        0.50880
b                   544                674        0.55337
c                   286                415        0.59201
```

The X-row incidence fraction therefore moves substantially across the three chambers in this finite source. This makes the receiving row-packet test non-vacuous.

The exact ordered `good/S/X` packet counts and the finer `{good,m,n,m-n,m+n}^2` packet counts are generated by the audit; a compact frozen summary is stored at

```text
stages/stage14/data/14-bridge2/p7_row_packet_summary.json.
```

Important boundary: these packet decompositions use the same B500m objects as diag4. They are **not independent confirmation**, do not establish causality, and do not prove a limiting packet mixture.

---

## 6. Receiver dictionary

```text
NUM: direction a/b/c
<->
14-4: chamber of (x/e,y/e)

NUM: 7|shared edge e
<->
primitive face orientations: p=7 survives in at least one shared leg
<->
s5 moving columns: m,n,m-n,m+n
<->
s5c/s5d local row type: good / S-row / X-row
```

The receiving object should therefore be an ordered two-face `p=7` row packet, not a standalone third-face QR factor.

For each exactly-two matching pair define

```text
R_7(F1,F2)=(row_7(F1),row_7(F2)),
row_7 in {good,S,X}.
```

The audit additionally refines this to the exact moving-factor packet

```text
{good,m,n,m-n,m+n}^2.
```

---

## 7. Smallest falsifiable receiving test

The next proof-side test is:

```text
P7-ROW-PACKET-CHAMBER-TEST

1. In the exact 14-4 two-face matching parameterization, split each a/b/c chamber by ordered R_7(F1,F2).
2. Insert the already-proved s5c/s5d p=7 local weights for good/S/X rows.
3. Compute the chamber-resolved leading local/archimedean density of the packet mixture.
4. Compare only the predicted ordering/sign pattern with the frozen finite p=7 direction association; do not fit constants to B500m.
5. If the row-packet mixture is chamber-neutral, reject p=7 local-row composition as the explanation and leave the residual to global/height/archimedean correlation.
6. If it is chamber-dependent, freeze the exact local-density vector and pass it to the direction-density side of 14-4.
```

This is an L5 handoff. It does not require reopening the already-closed reciprocal-character estimate and it is not a blocker for the unweighted upper-bound retainer proved by 14-4be.

Primary receiver:

```text
RECEIVER_ROUTE=Stage14-4
RECEIVER_OBJECT=chamber-resolved p7 row-packet local/archimedean density
SUPPORTING_LOCAL_SOURCE=Stage14-s5c/s5d/s5f
```

---

## 8. Evidence ladder and claim boundary

```text
L1  diag4 exact finite p7 direction association
L2  diag5 survival under equal-d / equal-component controls
L3  exact primitive-face valuation and Euclid-column reformulation
L4  exact dictionary to s5 good/S/X rows and 14-4 chambers
L5  P7-ROW-PACKET-CHAMBER-TEST
```

Bridge2 does not claim L6.

```text
STAGE14_BRIDGE2=COMPLETE_P7_SHARED_EDGE_TO_LOCAL_ROW_PACKET_TRANSLATION
P7_SHARED_EVENT_HAS_EXACT_PROOF_SIDE_DICTIONARY=true
P7_SHARED_EVENT_MAPS_TO_EXISTING_S5_LINEAR_COLUMNS=true
P7_S_AND_X_ROW_TYPES_DIFFER_AT_7=true
P7_ROW_PACKET_FINITE_DECOMPOSITION_FROZEN=true
P7_X_ROW_INCIDENCE_FRACTION_A_B_C=0.5088044485634847,0.5533661740558292,0.5920114122681883
P7_MISSING_THIRD_FACE_QR0_FORCED=true
P7_MISSING_THIRD_FACE_QR0_INDEPENDENT_FILTER=false
STAGE13_LAMBDA7_REUSED_AS_NULL=false
REOPEN_RECIPROCAL_ANALYSIS=false
ASYMPTOTIC_DIRECTION_CLAIM=false
FINITE_ZERO_NONEXISTENCE_CLAIM=false
NEXT=Stage14-bridge3 residual direction-drift mechanism after bridge2 merge
```
