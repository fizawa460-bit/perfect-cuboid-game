# Stage32 MB104 — wide shallow closure scan Round E — 2026-09-18

Status: **ROUND E COMPLETE / NO PROMOTE / TESTED ARCHITECTURES HARD-DROP / BROADER DIRECTIONS SOFT-PARK / NO CREDIT**

This round uses the corrected two-level policy:

```
tested_architecture_status
broader_direction_status
```

A failed scalar test does not remove the surrounding mathematics from the portfolio.

## W21 — first-jet / polar singularity capacity

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

For `L=O_S(D_l)`,

```
0 -> Omega_S^1 tensor L -> J^1(L) -> L -> 0.
```

Hence `J^1(L)` has rank three on a surface and

```
c2(J^1(L))
 = c2(S)+2K.L+3L^2
 = 80+224l+1008l^2.
```

Two failures occur immediately.

First, singular points of a divisor section are zeros of `j^1(s)`, a section of a **rank-three** bundle on a **surface**.  Thus `c2(J^1(L))` is not a top-Chern count of those zeros.

Second, even as a crude numerical capacity,

```
1008l^2+224l+80
```

is much larger than

```
Delta=168l^2+56l.
```

So the proposed c2-capacity obstruction does not work.

A lower-rank polar/degeneracy construction adapted to the cuboid equations remains open.

## W22 — stable-map virtual dimension / normal sheaf

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

For a genus-one stable map in class `D_l` to a surface, the unmarked expected dimension is

```
-K.D_l=-112l.
```

For an immersed elliptic normalization, the normal line bundle likewise has negative degree

```
deg N_f=-112l.
```

This proves strong obstruction/rigidity pressure, but not emptiness.  Negative expected dimension does not prohibit isolated obstructed maps.

The route becomes useful only with an additional theorem forcing unobstructedness, semiregularity, a cosection, or another vanishing mechanism.

## W23 — Castelnuovo--Severi on the joint factor pair

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

The retained pair

```
E -> P1 x P1
```

is birational onto its image, with factor degrees

```
e=2: 28l,28l
e=4: 56l,56l.
```

Castelnuovo--Severi gives, because the maps have no common proper factor,

```
g(E) <= (d1-1)(d2-1).
```

Thus it says only

```
1 <= (28l-1)^2
```

or

```
1 <= (56l-1)^2.
```

This is completely compatible.  The inequality is in the wrong direction for exclusion.

Special singularity/grid geometry of the bidegree image remains open.

## W24 — dualizing conductor / different

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

Adjunction gives

```
deg nu^*omega_C
 =(K+D_l).D_l
 =336l^2+112l.
```

The elliptic normalization has canonical degree zero, while

```
2Delta
 =2(168l^2+56l)
 =336l^2+112l.
```

So the proposed conductor/different degree comparison is exactly the genus formula in another form.

It is an identity, not an obstruction.

A distributional conductor theorem tied to the exact cuboid branch types would be genuinely new and remains soft-parked.

## W25 — Lefschetz-pencil total singularity budget

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

For a generic Lefschetz pencil in a surface line bundle `L`, the critical-point count is

```
3L^2+2K.L+c2(S).
```

With `L=D_l`:

```
Ncrit
 =1008l^2+224l+80.
```

Compare

```
Delta=168l^2+56l.
```

The pencil budget has asymptotic coefficient six times larger.  A single carrier defect fits comfortably; there is no total Euler-budget overload.

Also a pencil deliberately containing the prescribed highly singular carrier need not be Lefschetz at that fiber.

Monodromy/slope refinements remain open, but the total-budget test is dead.

## Round E result

```
W21 architecture HARD / direction SOFT
W22 architecture HARD / direction SOFT
W23 architecture HARD / direction SOFT
W24 architecture HARD / direction SOFT
W25 architecture HARD / direction SOFT

PROMOTE = none
```

Continue broad search; do not deepen these five from this checkpoint.
