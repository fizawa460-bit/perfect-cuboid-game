# Stage35-EX Goal4BC source lock — post-Goal4AS ledger exhaustion fresh-view audit

Scope: execute a new breadth cycle after Goal4AT–Goal4BB have exact-tested every candidate lens recorded by Goal4AS. Audited authority remains V74 / Goal4AK. This leaf is a route audit and receiver-selection preflight only; it grants no E1, Stage35, endpoint, or Perfect Cuboid credit.

## 1. Trigger

Goal4AS generated seven blind lenses. They have now all received an exact test or blocker:

```text
MARKED_ELLIPTIC_2DESCENT_KUMMER              -> AT/AU/AV,
CANONICAL_HEIGHT_LOWER_VS_ENDPOINT_UPPER     -> AW,
GENUINE_NONLINEAR_FULL_ENDPOINT_DESCENT      -> AY,
FINITE_EXPLICIT_BRAUER_SHORTCUT              -> BA/BB,
LINKED_SELMER_CASSELS_COMMON_COVER           -> AU/AV boundary,
AMPLIFICATION_OR_STRONGER_COUNTING           -> AZ,
CROSS_FACE_NORM_LATTICE_SPINOR_TORSOR        -> AX.
```

Goal4BB materially strengthens the Brauer boundary:

```text
for every finite F subset Br(U), (A_src^loc)^F != empty,
```

while Goal4AR retains the full infinite-Brauer endpoint equivalence. The previous finite-Brauer lens is therefore exhausted and cannot simply be rerun with more explicit classes.

This is a cycle-safety trigger for a new blind pass.

## 2. Blind pass before Arsenal

No Arsenal route recommendations were consulted while generating the following new lenses.

### BC-B1 — simultaneous three-marked rank-jump fiber-product receiver

A physical endpoint has three cyclic edge orientations. Goal4L sends one orientation to a non-torsion marked point on

```text
E_q : Y^2=X(X-1)(X+q^2),
```

and Goal4AT/AU apply the same marked construction cyclically. AU only couples the **three Kummer squareclasses** and AV only tests the induced split common coefficient torsor. Neither leaf materializes the joint algebraic image of all three marked elliptic points as one receiver over the common physical endpoint variables.

Fresh missing object:

```text
R_3MW = source-locked image/fiber product of the three cyclic Goal4L marked-point maps,
```

including the exact compatibility equations inherited from one `(A,B,C,D_AB,D_AC,D_BC,W)` endpoint.

The test is not “do the three Selmer classes multiply to one?”; that is already AU. The test is whether the **joint marked-point receiver plus physical compatibility** has lower-dimensional, locally impossible, or receiver-degenerate rational locus.

### BC-B2 — gcd-reservoir quadratic-reciprocity cycle

AU gives exact odd reservoirs

```text
h_a=gcd(a,r_BC), h_b=gcd(b,r_AC), h_c=gcd(c,r_AB),
```

with `r_AB,r_AC,r_BC` primitive Pythagorean hypotenuses. Every odd prime dividing any `r_ij` is `1 mod 4`; hence every odd prime in `h_a h_b h_c` is `1 mod 4`.

This is stronger arithmetic information than support allocation alone. A fresh route may record Legendre/Jacobi symbols of residual primes around the three primitive Pythagorean faces and test a cyclic quadratic-reciprocity parity identity. No contradiction is presently claimed.

### BC-B3 — finite-conductor boundary-escape versus height

BB proves every finite Brauer subsystem is satisfiable on `A_src^loc`, while AQ/AR require an infinite character intersection to reconstruct a rational endpoint. The known finite-subsystem constructions approach the boundary anchor `y=0` with local depth depending on the chosen finite classes.

Fresh quantitative question:

```text
can conductor/character complexity force a universal lower bound on boundary depth,
and can source height/primitivity provide an incompatible upper bound?
```

A valid result would need a universal statement about **all** finite-subsystem adelic solutions of bounded complexity, not merely the particular BB construction. No such bound is currently available.

### BC-B4 — derived fourth-square defect two-cycle

AY proves the primitive derived-cuboid operator is the exact involution

```text
(x,y,z ; a,b,c) <-> (a,b,c ; x,y,z)
```

on the three-face population and cannot be a universal strict descent. A distinct route could study the fourth-square defect under this involution rather than require the derived operator itself to preserve perfect endpoints. No invariant or obstruction is currently materialized.

### BC-B5 — toric visible-unit coordinate surface with source-integrality

AQ reconstructs the endpoint from

```text
u1=p+x, u2=q+y, u3=w+z.
```

These give a torus-coordinate presentation via

```text
x=(u1-u1^-1)/2,
y=(u2-u2^-1)/2,
z=(u3-u3^-1)/2,
```

with one Laurent relation `z^2=x^2+y^2`. Without an additional source-integrality/primitivity invariant this is only endpoint reparameterization, overlapping AQ/AX, so it is parked as equivalent until a genuinely new integral condition is supplied.

## 3. Arsenal deduplication after blind generation

The active missing object is now an exact **joint receiver plus receiver-condition intersection test** for BC-B1.

Repository asset discovery was performed according to `docs/research-os/policies/repository-asset-discovery.md`, then `docs/arsenal/index.json`, then the single matching formal card `S34-W03`.

`S34-W03` (`RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION`) is applicable only as a procedure **after** a common branch/receiver `B` and an additional exact physical condition `K` are materialized. It allows closure of `B(Q) intersect K(Q)` without classifying all of `B(Q)`. It does not construct `R_3MW`, does not supply the physical compatibility equations, and gives no current closure credit.

Other already-consumed structures do not solve the new missing object:

- `S31-W01` is the quartic-to-elliptic adapter already used in Goal4L;
- AU/AV provide Kummer/common-cover relations, not the full three-marked-point receiver;
- AW supplies height boundaries, not a joint receiver;
- AX is a split norm-torus chart and endpoint reparameterization;
- AY is a three-face involution, not a three-elliptic-point compatibility variety;
- BA/BB settle finite Brauer shortcuts and do not constrain `R_3MW`.

Therefore BC-B1 survives deduplication as materially new.

## 4. Priority decision

Priority order after the audit:

```text
1. SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER
2. GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE
3. FINITE_CONDUCTOR_BOUNDARY_ESCAPE_VS_HEIGHT
4. DERIVED_FOURTH_SQUARE_DEFECT_TWO_CYCLE
5. TORIC_VISIBLE_UNIT_COORDINATES_WITHOUT_NEW_INTEGRAL_INVARIANT = PARK_EQUIVALENT
```

BC-B1 is selected because all ingredients for three cyclic Goal4L maps already exist source-locked, while the missing common receiver has never been materialized. It also admits a precise fail-closed test: compute the common image/compatibility equations, dimension and degeneracy loci; if an exact extra receiver condition yields a local or global empty intersection, apply `S34-W03` only at that point.

## 5. Next exact leaf

```text
35EX-35_GOAL4BD_SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_PREFLIGHT
```

Required outputs:

1. write all three cyclic Goal4L marked-point maps from one physical endpoint in a common coordinate convention;
2. materialize the joint image/fiber-product equations and exact exceptional loci;
3. compute the generic dimension of the joint receiver relative to the physical endpoint surface;
4. determine whether the common physical compatibility gives a genuinely smaller/intersection condition rather than a birational reparameterization;
5. if a smaller receiver exists, test exact local exclusion using `S34-W03`; otherwise fail-close this view without calling it a Selmer/Cassels obstruction.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
