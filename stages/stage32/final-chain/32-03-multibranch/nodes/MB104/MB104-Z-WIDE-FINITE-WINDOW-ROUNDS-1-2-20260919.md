# Stage32 32-03 — Z-wide population finite-window scan, Rounds 1-2 — 2026-09-19

Status: **USER-DIRECTED BREADTH SCAN / POPULATION-WIDE / NO MATHEMATICAL CREDIT**

## Scope

This scan deliberately sits above the balanced `000707` / W16 subtree.

Target population:

```text
R29-LG2-MB = all nonexceptional integral multibranch low-genus carriers
g(normalization) in {0,1}
```

Target theorem shape:

```text
population-wide d <= D
or an equivalent finite Picard/intersection window
```

One shallow kill-test is allowed per Z-route. No Z-route is deepened until the six planned breadth rounds are complete.

Retained prerequisites:
- MB101 exact normalization/node profile;
- MB102 exact delta/genus ledger, including unconstrained `Delta_off`;
- MB103 exact Aut(S)-profile quotient semantics;
- MB104 finite-window theorem remains unproved.

The balanced `000707` ray is used only as a hostile test case; it is not identified with the full receiver.

---

## Round 1 — Z1 to Z5

### Z1 — smooth-resolution Bogomolov / big cotangent

**Result: HARD for known criteria.**

On the smooth resolution,

```text
K_S^2 = 16
c2(S) = 80
s2(S) = -64.
```

The already-retained canonical-model-singularity calculation with 48 A1 points gives the Asega--De Oliveira--Weiss CMS expression `-32/9`, so the known smooth-model big-cotangent criterion does not fire.

This does not kill all future differential methods; it kills the currently known population-wide big-cotangent criterion as a direct finite-window theorem.

### Z2 — canonical-orbifold canonical-degree inequality

**Result: PROMISING / DO NOT DEEPEN YET.**

The singular canonical cuboid surface has

```text
c2_orb = 8
K^2 = 16
s2_orb = 8 > 0.
```

For the balanced hostile ray, retained U8 gives the exact critical identity

```text
K_X.C = 2 * deg K_orb(source).
```

Therefore a source-valid quotient/orbifold canonical-degree theorem with effective coefficient strictly below `2` would immediately have the correct asymptotic shape for a finite window.

Nearby literature exists (Miyaoka canonical-degree/orbibundle bounds; Sabatino log-canonical degree bounds), but no theorem is presently source-valid for the full 32-03 quotient-singular / multibranch receiver. Keep this route as the current strongest breadth survivor.

### Z3 — effective cone / Mori / stable base

**Result: SOFT-PARK.**

The balanced ray is already known effective for every `l>=1`, so polyhedrality/finitely generated effectivity alone cannot bound degree.

A stronger theorem could still work if it forces every sufficiently large low-genus multibranch class to acquire a fixed component or become reducible. No population-wide source-complete effective-cone theorem of that strength is retained.

### Z4 — aggregate delta / singularity inequalities

**Result: HARD for aggregate-only architecture.**

MB102 leaves `Delta_off` unconstrained. Existing H8/U6 formal ordinary-node witnesses keep the standard BMY/log inequalities on the allowed side.

A revival requires a new global localization/collision theorem forcing the quadratic genus defect into analytically controlled singularities. The aggregate-only route is closed.

### Z5 — generic product-cover / Castelnuovo--Severi / de Franchis / Hurwitz

**Result: HARD for generic architecture.**

For the balanced hostile product-correspondence test,

```text
n = 28l
g(Z) = 4n+1,
```

while Castelnuovo--Severi has quadratic slack. De Franchis fixes the source; fixed-degree Hurwitz finiteness fixes the degree. Neither bounds `n` while the source and degree grow.

Packet-sensitive arithmetic refinements remain a different possible theorem species, but generic product-correspondence boundedness does not give the 32-03 window.

---

## Round 2 — Z6 to Z10

### Z6 — fixed modular product cover / bi-disk inequality

**Result: HARD for generic product-hyperbolicity.**

Stoll--Testa/Beauville give the fixed quotient

```text
bar S ~= (X(8) x X(8)) / G0,
G0 ~= (Z/2)^3,
g(X(8)) = 5.
```

For a lifted irreducible component `Z` with projection degrees `m,n`, Riemann--Hurwitz gives

```text
g(Z)-1 >= 4m,
g(Z)-1 >= 4n,
K_(XxX).Z = 8(m+n) <= 4(g(Z)-1).
```

The balanced hostile family exactly saturates this shape: both projection degrees are `n=28l`, `g(Z)=4n+1`, hence

```text
K_(XxX).Z = 16n = 4(g(Z)-1).
```

So a generic product/bi-disk hyperbolicity inequality cannot produce a degree cutoff. Any useful product-cover theorem must use extra cuboid packet data, not the product geometry alone.

### Z7 — multipoint Seshadri / exceptional-contact ratio

**Result: HARD standalone.**

Seshadri-type inequalities give lower bounds on degree in terms of imposed local multiplicities. The full multibranch receiver requires only that at least one box node have at least two normalization branches.

There is no retained population-wide lower bound of the form

```text
total node multiplicity/contact >= c * d, c>0.
```

The balanced ray has strong proportional contact, but that is special-sector data. Therefore multipoint Seshadri bounds have the wrong direction for the full receiver unless a new theorem first forces contact mass to scale with degree.

### Z8 — canonical complete-intersection quadrics / syzygy rank

**Result: HARD for generic quadratic-syzygy architecture.**

The cuboid surface is cut out by four quadrics in `P^6`. On the normalization of a genus-0/1 carrier, the seven ambient coordinates give a 7-dimensional subsystem

```text
V subset H0(L),  deg L=d.
```

The four surface quadrics only imply

```text
dim image(Sym^2 V -> H0(L^2)) <= 24.
```

But

```text
h0(L^2)=2d+1  (g=0),
h0(L^2)=2d    (g=1),
```

and for large `d`, `V` is a highly incomplete linear series. There is no reason for `Sym^2 V -> H0(L^2)` to be surjective. Thus the four quadratic relations alone do not bound `d`.

A cuboid-specific theorem forcing normal generation/extra syzygy growth would be new input; the generic projective route is closed.

### Z9 — Miyaoka total elliptic-degree bound on the canonical surface

**Result: ABSORBED BY Z2 / not a new route.**

For a smooth canonical surface Miyaoka's 2009 Proposition B bounds the total canonical degree of elliptic curves when

```text
sigma = c2/K^2 < 1.
```

The smooth cuboid resolution has `sigma=80/16=5`, so the theorem does not apply there.

Replacing `c2` formally by `c2_orb=8` would give `sigma_orb=1/2`, but this is not a legal substitution: a multibranch curve passing through A1 points acquires stacky source complexity. The retained U8 identity on the balanced hostile ray is exactly

```text
K_X.C = 2 * deg K_orb(source).
```

Therefore the tempting singular-model transplantation is precisely the missing orbifold canonical-degree theorem already isolated as Z2. Z9 adds no independent route.

### Z10 — stable-map / normal-bundle negative expected dimension

**Result: HARD standalone.**

For a genus-`g` stable map of class `beta` to a surface,

```text
vdim = g - 1 - K.beta.
```

Thus the expected dimension becomes strongly negative as canonical degree grows. But negative virtual dimension is an obstruction/rigidity statement, not an emptiness theorem: isolated obstructed maps can exist.

This is the population-wide version of the already-observed W22 wall. Without a cosection/semiregularity theorem that kills the actual moduli support, it cannot yield a finite degree window.

---

## Portfolio after two rounds

```text
PROMISING:
  Z2  canonical-orbifold canonical-degree inequality

SOFT-PARK:
  Z3  strong effective-cone/fixed-component theorem
  Z4' global singularity localization/collision refinement
  Z5' packet-sensitive arithmetic product refinement

HARD / ABSORBED AS TESTED:
  Z1 Z4 Z5 Z6 Z7 Z8 Z9 Z10
```

The scan has **not** proved that Z2 works. It has only survived the first two breadth rounds.

Next breadth batch:

```text
Z11-Z15
```

No W16-H deepening before the planned Z1-Z30 breadth scan is completed or explicitly stopped by the user.

## Firewalls

```text
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
finite_picard_enumeration_released=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
