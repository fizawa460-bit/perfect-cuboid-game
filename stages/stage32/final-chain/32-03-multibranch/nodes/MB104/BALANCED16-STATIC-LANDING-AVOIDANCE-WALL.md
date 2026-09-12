# Stage32 MB104 — balanced-16 static landing-avoidance wall

Status: **RETAINED NEGATIVE ROUTE WALL / STATIC LANDING VALUES DO NOT CLOSE FOUR-ORBIT HARD CORE / MB104 INCOMPLETE / NO CREDIT**

The preceding balanced-support quotient reduces the displayed uniform genus-one P5 ray to four exact `Aut(S)` support orbits. Every surviving support has only zero, not negative, intersection with a small set of retained elliptic quartics.

For an irreducible effective carrier `C` in class

```text
D_l = 7lH - 4l sum_{i in Sigma}E_i,
```

and a retained elliptic quartic `Q` with `D_l.Q=0`, positivity of local intersection on the smooth resolution forces `C` and `Q` to be disjoint. At each shared box node, the branches of `C` must therefore avoid the exceptional landing point of `Q` on the corresponding exceptional curve.

The four balanced support orbits give only a finite static avoidance condition:

```text
orbit sizes 48,48:
  four zero-pairing quartics;
  each supported node lies on exactly two of them;
  <=2 quartic landing points are forbidden at that node.

orbit sizes 768,768:
  two zero-pairing quartics;
  each supported node lies on exactly one of them;
  <=1 quartic landing point is forbidden at that node.
```

The retained formal genus-one P5 packet has `k=4l`, supported exceptional mass `M_i=2k=8l`, and all supported branches FSM-minimal with multiplicity one and pairwise distinct nonzero exceptional landing keys.

The retained A1/local-jet interface uses an exceptional landing coordinate `lambda` on the exceptional curve and explicitly leaves the first tangential jet free. Over the geometric characteristic-zero field, the exceptional curve has infinitely many landing points. Removing the nonzero condition and at most two additional forbidden quartic landing points still leaves infinitely many admissible choices.

Therefore, for every `l>=1`, one can choose `8l` pairwise distinct nonzero local landing keys at each supported node while avoiding all zero-pairing quartic landing points. This is only a local/formal feasibility statement; it does not construct a global curve.

Consequently the implication

```text
zero-pairing elliptic quartics
+ static exceptional landing avoidance
=> contradiction
```

is invalid. Any successful continuation must couple more information than the landing value alone, for example a global tangent/first-jet condition, simultaneous algebraic compatibility across nodes, or a stronger Picard/effective-cone obstruction.

This wall is compatible with `MULTIFIBRATION-LOCAL-JET-WALL.md`: that retained wall already shows the first tangential coefficient remains free for a fixed minimal-cusp landing point. The present result says that the zero-quartic geometry also does not exhaust the landing-point freedom.

Firewalls: no global curve is constructed; no claim is made that arbitrary local choices globalize; the four balanced support orbits remain open; unequal exceptional coefficients remain open; MB104 and whole span5 remain incomplete; no theorem/receiver/endpoint/Perfect-Cuboid/merge credit.
