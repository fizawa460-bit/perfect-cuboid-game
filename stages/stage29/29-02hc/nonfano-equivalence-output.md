# Stage29-02hc adversarial checker output

```text
SCRIPT=stages/stage29/29-02hc/nonfano_equivalence_check.py
ARITHMETIC=EXACT_RATIONAL_AND_F2_SQUARECLASS
STATUS=PASS_ALL_ASSERTIONS
```

Exact output:

```text
PGL3_Q_BRANCH_EQUIVALENCE=PASS
PGL3_Q_EQUIVALENCES_TOTAL=24
STANDARD_NF_Q_COVER_LIFTABLE_EQUIVALENCES=0
QI_COVER_LIFTABLE_EQUIVALENCES=24
DISPLAYED_LINE_MULTIPLIER_CLASSES=+,-,-,+,+,-,-
DISPLAYED_RELATIVE_TWIST=-,+,+,-,-,+
Q_FORM_STANDARD_NF_COVER_IDENTIFICATION=FAIL_AS_STATED
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=PASS
INCIDENCE=t3:6,t2:3,total:9
HIRZEBRUCH_N2_DEGREE=64
TRIPLE_FIBER=8
NODES=48
C1SQ=16
C2=80
COMPACT_B1=0
Q=0
CHI_O=8
PG=7
CENTRAL_OPEN_B1_N2=33
PROJECTIVE_OPEN_B1_N2=32
```

Interpretation:

- the seven branch lines are exactly `PGL3(Q)`-equivalent to Suciu's standard non-Fano arrangement;
- this does **not** identify the two standard Kummer covers over `Q`: none of the 24 rational projective equivalences has one common multiplier squareclass on all seven lines;
- every equivalence lifts after adjoining `i`, so the cuboid cover is the standard non-Fano `N=2` Hirzebruch cover over `Q(i)`;
- over `Q`, the cuboid cover carries the explicit constant-sign twist represented for the displayed equivalence by `(-,+,+,-,-,+)` relative to the seventh line;
- the compact invariant/node package remains unchanged;
- Suciu's displayed `b1(X_N)` is central-arrangement data.  At `N=2`, its value is 33; the projective 64-sheet arrangement-open cover relevant to the endpoint has the extra `C*` factor removed and has `b1=32`.

This checker does not prove that no abstract `Q`-surface isomorphism to another standard presentation exists.  It disproves the submitted **cover-over-`P2` Q-identification** and records the exact repair.