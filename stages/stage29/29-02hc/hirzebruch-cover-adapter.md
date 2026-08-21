# Hirzebruch-cover adapter — audited field scope

## 1. What is literally the same

Stage29-02ha gives the normal endpoint map

```text
pi:Sbar_cub -> P2
G=(Z/2)^6
D=x y z (x+y)(x+z)(y+z)(x+y+z)=0.
```

The rational projective change

```text
x=X, y=-Y, z=Z-X
```

identifies the **branch arrangement** with Suciu's standard non-Fano arrangement

```text
XYZ(X-Y)(X-Z)(Y-Z)(X+Y-Z)=0.
```

Thus the cuboid map and the non-Fano construction have the same seven-line branch incidence and the same abstract mod-2 deck group.

## 2. Projective congruence cover convention

For seven projective lines,

```text
H1(P2\D,Z)=Z^6,
H1/2H1=(Z/2)^6.
```

The corresponding unbranched projective congruence cover has degree 64.  Normalizing `P2` in its function field gives the branched Kummer cover; its minimal desingularization is the `N=2` Hirzebruch surface construction.

No rank-seven central-arrangement convention is used for this degree-64 compact cover.

## 3. Adversarial Q-form check

Branch equivalence does not determine the arithmetic Kummer cover.  If a projectivity sends line forms by

```text
phi^* L_i = lambda_i L_sigma(i),
```

then it lifts between the two sign/Kummer Q-forms iff all `lambda_i` have one common class in `Q*/Q*^2`.

For the displayed transformation the seven multiplier classes are

```text
+,-,-,+,+,-,-,
```

and, relative to the seventh branch form, the six Kummer generators acquire the constant twist

```text
-,+,+,-,-,+.
```

The exact checker exhausts all 24 `PGL3(Q)` equivalences between the two arrangements and finds

```text
PGL3_Q_EQUIVALENCES_TOTAL=24
STANDARD_NF_Q_COVER_LIFTABLE_EQUIVALENCES=0
QI_COVER_LIFTABLE_EQUIVALENCES=24.
```

Therefore the submitted statements

```text
Sbar_cub ~=_Q Xbar_2(NF_standard)
S_cub    ~=_Q M_2(NF_standard)
```

are **not certified and are false as cover-over-P2 identifications**.

The correct audited statement is

```text
Sbar_cub x_Q Q(i) ~= Xbar_2(NF_standard) x_Q Q(i),
S_cub    x_Q Q(i) ~= M_2(NF_standard)    x_Q Q(i),
```

while over `Q`, `Sbar_cub` is the explicit constant-sign twist of the standard non-Fano mod-2 Kummer cover determined above.

```text
STANDARD_NF_Q_COVER_IDENTIFICATION=false
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=true
CUBOID_Q_FORM_IS_EXPLICIT_CONSTANT_SIGN_TWIST=true
ABSTRACT_Q_SURFACE_ISOMORPHISM_TO_STANDARD_M2_PROVED=false
```

The last firewall is deliberate: the audit rules out the submitted arrangement-cover Q-identification; it does not prove that no unrelated abstract Q-isomorphism of the resolved surfaces can exist.

## 4. Globality and resolution

Over `Q(i)` (and geometrically) the two normal covers are the normalization of `P2` in the same Kummer function field, so the identification is global rather than merely generic.

For `N=2`, a triple branch point has eight points above it and local `A1` type.  The six triple points give all 48 A1 nodes.  Ordinary double intersections are smooth on the normal cover.  Hence minimal resolutions agree after the field extension.

The standard Hirzebruch formulas therefore recover the geometric/compact invariants of the cuboid surface:

```text
K^2=16, c2=80, q=0, pg=7.
```

These invariant equalities do not repair the Q-form distinction by themselves.

## 5. Audited receiver

```text
R29-NF0 = CuboidBranchArrangementToNonFanoPGL3QAdapter          DISCHARGED
R29-NF1G = CuboidCoverToNonFanoHirzebruchM2OverQi             DISCHARGED
R29-NF1Q = ExplicitConstantSignQTwistOfStandardNonFanoM2       DISCHARGED_AS_TWIST_DESCRIPTION
R29-NF1QISO = AbstractQSurfaceIsomorphismToStandardM2          OPEN_NOT_NEEDED
```
