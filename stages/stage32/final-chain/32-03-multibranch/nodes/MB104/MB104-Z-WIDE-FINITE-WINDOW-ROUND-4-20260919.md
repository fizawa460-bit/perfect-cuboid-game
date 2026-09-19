# Stage32 32-03 — Z-wide population finite-window scan, Round 4 (Z16-Z20) — 2026-09-19

Status: **USER-DIRECTED BREADTH SCAN / WHOLE R29-LG2-MB POPULATION / NO MATHEMATICAL CREDIT**

## Scope

Target remains the whole multibranch low-genus receiver:

```text
R29-LG2-MB
g(normalization) in {0,1}
=> population-wide finite degree/intersection window.
```

Balanced `000707` is only a hostile test case. Z2/Z12/W16-H are not deepened here.

---

## Z16 — Miyaoka / Vojta canonical-degree bound from bounded geometric genus or gonality

**Result: HARD unconditionally for the actual multibranch receiver; CONDITIONAL theorem-shape only.**

Autissier--Chambert-Loir--Gasbarri summarize two nearby statements:

1. Miyaoka proves a canonical-degree inequality for **smooth curves embedded in a minimal surface** of general type, with asymptotic coefficient `a>3/2`.
2. Vojta conjectures a stronger form for curves of bounded gonality, essentially allowing any `a>1`.

The 32-03 normalizations have gonality bounded by 1 or 2, so this is exactly the right *conjectural* global theorem shape.

But the load-bearing issue is singularity: the multibranch carrier is not a smooth embedded curve on the minimal resolution. Its normalization genus stays 0/1 while its image may carry unbounded `Delta_total`. Blowing up or normalizing changes the canonical-degree accounting by precisely the singularity/conductor data that Stage32 is trying to control.

The balanced hostile ray demonstrates the gap:

```text
g(normalization)=1,
D_l^2=336l^2,
Delta_total=168l^2+56l.
```

Thus the known smooth-curve theorem is not applicable, while the bounded-gonality statement needed to ignore this singularity growth is conjectural.

Disposition:

```text
known theorem = HARD for receiver
Vojta-shaped bounded-gonality theorem = CONDITIONAL / not admissible proof input
```

Source:
Autissier--Chambert-Loir--Gasbarri, *On the canonical degrees of curves in varieties of general type*, GAFA 22 (2012), arXiv:1003.3804.

---

## Z17 — finiteness of high-canonical-degree negative curves

**Result: HARD population-wide; possible subpopulation cleanup only.**

Ciliberto--Roulleau prove that on a surface of general type there are only finitely many irreducible curves with negative self-intersection and sufficiently large canonical degree.

This can potentially remove a negative-self-intersection tail of the 32-03 population.

It cannot be the population-wide finite-window theorem because the hostile family has

```text
D_l^2 = 336l^2 > 0
```

for every `l>=1`.

Therefore the most dangerous surviving mechanism lies entirely outside the theorem's principal negative-curve regime. No finite degree cutoff follows for nonnegative/highly positive self-intersection classes.

Source:
Ciliberto--Roulleau, *On finiteness of curves with high canonical degree on a surface*, Geom. Dedicata 183 (2016), arXiv:1406.7478.

---

## Z18 — abstract Hilbert/Chow boundedness from fixed normalization genus

**Result: HARD as a general theorem; absorbed by the earlier failed H4 architecture.**

A tempting top-level argument is:

```text
fixed surface + g(normalization)<=1
=> bounded Hilbert/Chow family
=> finitely many numerical classes/degrees.
```

There is no such general theorem for arbitrary surfaces of general type. The boundedness of canonical degree for bounded geometric genus is itself a widely believed conjectural phenomenon; the Autissier--Chambert-Loir--Gasbarri paper explicitly formulates this as a conjectural direction.

The Stage32 hostile ray also shows why finite-generation of the section ring alone is insufficient: one can have unbounded divisor classes with normalization genus kept small by a growing singularity defect.

This is the population-wide restatement of the already-parked MB104 H4 failure:

```text
unbounded l does not force one bounded Hilbert/Chow stratum or a fixed fibration.
```

So ordinary Noetherianity/properness does not create the missing degree bound.

---

## Z19 — fixed foliation / web and Poincare-type degree bounds

**Result: HARD as a universal route; absorbed by Z12 if built from symmetric differentials.**

For a **fixed** foliation of general type, Poincare-problem theorems can bound the degree of invariant algebraic curves in terms of foliation invariants and geometric genus.

That would be powerful if every 32-03 carrier were invariant under one fixed foliation or one finite fixed web.

No such population-wide invariant-foliation adapter is retained. The carrier family is defined by lying on the cuboid surface, not by being leaves of a fixed rank-one foliation.

If the foliation/web is manufactured from the cuboid symmetric differentials, then the route is not independent: it is precisely the higher-order differential direction already retained as Z12.

Thus:

```text
fixed-foliation universal adapter = missing
differential-defined web = absorbed by Z12
```

Source shape:
Pereira, *On the Poincare Problem for Foliations of General Type*, Math. Ann. 323 (2002), arXiv:math/0104185.

---

## Z20 — function-field abc / truncated counting on the normalization

**Result: HARD generic; differential refinement absorbed by Z11/Z12.**

Restrict the cuboid coordinate identities to the normalization `E) or `P^1`. Function-field abc / Nevanlinna second-main-theorem arguments can bound the degree of functions in terms of the number of distinct zeros, poles, or boundary contacts.

For the full multibranch receiver this counting support is not bounded independently of degree. Each normalization branch above a box node is a distinct source point, and the total number of such points `R` may grow linearly with `d`.

The hostile balanced ray has

```text
R=M=d=112l.
```

So a generic truncated-counting estimate still has an `O(d)` right-hand side and gives no strict cutoff.

Using the simultaneous cuboid equations more efficiently is exactly the Vojta/Garcia-Fritz symmetric-differential mechanism already isolated in Z11; increasing the jet/differential order is Z12.

Therefore generic function-field abc is not an independent finite-window engine.

---

## Round-4 portfolio update

```text
PROMISING:
  Z2   canonical-orbifold canonical-degree inequality

SOFT-PARK:
  Z3   strong effective-cone/fixed-component theorem
  Z4'  global singularity localization/collision theorem
  Z5'  packet-sensitive arithmetic product theorem
  Z12  adaptive/higher-order symmetric differentials

CONDITIONAL-ONLY:
  Z16' Vojta bounded-gonality canonical-degree theorem shape

HARD / ABSORBED AS TESTED:
  Z1 Z4 Z5 Z6 Z7 Z8 Z9 Z10
  Z11 Z13 Z14 Z15
  Z16 Z17 Z18 Z19 Z20
```

## Stronger diagnosis after Z1-Z20

Three independent broad viewpoints now point at the same wall:

```text
Z11: d <= M + 4g - 4          (exceptional contact M escapes)
Z16: smooth-curve canonical-degree bounds do not survive uncontrolled singularity defect
Z20: truncated source counting has R=O(d), and balanced hostile has R=d
```

Thus the missing population-wide input is increasingly localized to one of:

```text
(A) a strict orbifold/canonical-degree inequality that prices multibranch A1 contact
    more cheaply than coefficient 1 (Z2);

(B) a theorem forcing branch/contact complexity M or R to be sublinear/bounded
    relative to d, or forcing enough collisions to convert it into quadratic delta
    (Z4');

(C) an adaptive higher-order differential/jet mechanism whose vanishing charge
    grows with multiplicity rather than only with finite node support (Z12);

(D) a packet-sensitive arithmetic/global-cover restriction stronger than generic
    product geometry (Z5').
```

This is diagnosis only, not a finite-window theorem.

Next breadth batch:

```text
Z21-Z25
```

Do not deepen the survivors before completion of the breadth phase.

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
