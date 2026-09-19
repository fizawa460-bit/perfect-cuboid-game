# MB104 — Z40B global fibration optimum reduction — 2026-09-19

Status: **EXACT GLOBAL FIBRATION LOWER BOUND / SIZE48 OPTIMUM CLOSED / SIZE768 REDUCED TO DEGREES 10,12 / ZERO CREDIT**

## Input

For any one of the three surviving balanced supports,

```text
P = 7H - 4 sum_(i in Sigma) E_i.
```

Z40B proves that for every nonexceptional integral curve R whose image is not contained in the
unique support hyperplane L,

```text
M_Sigma := sum_(i in Sigma) E_i.R <= e := H.R,
```

hence

```text
P.R = 7e - 4M_Sigma >= 3e.                    (Z40B-GLOBAL)
```

A smooth general fiber of a fibration cannot be contained in the fixed hyperplane L: if every
general member of a moving pencil were contained in L, their union would be contained in L,
contradicting that they cover the surface.

Therefore (Z40B-GLOBAL) applies to every general fiber F.

The 2026 Stoll--Testa low-degree classification gives

```text
H.F >= 8.
```

## 1. Size48: the rank-3 fibration is globally optimal

For the two surviving size48 support orbits, the corrected rank-3 fibration audit exhibits

```text
H.G=8,
P.G=24.
```

For an arbitrary fibration fiber F,

```text
P.F >= 3 H.F >= 24.
```

Thus

```text
min over ALL fibrations P.F = 24
```

for both size48 support orbits.

This is not restricted to the 28 Stoll--Testa degree-eight fibrations.

Consequently the best possible Riemann--Hurwitz ramification budget obtainable from any fibration
on the cuboid surface is exactly

```text
2l(P.F) >= 48l,
```

and the imported rank-3 fibration attains equality.

Therefore:

```text
searching for an unknown fibration with a smaller ramification budget
is CLOSED for size48.
```

Any stronger conductor/polar argument for the size48 orbits must use simultaneous directions,
higher jets, collision geometry, or another invariant; it cannot improve by choosing a lower
P-degree fibration.

## 2. Size768: only degree 10 or 12 could improve the known value 40

For the surviving size768 orbit, a known rank-3 fiber gives

```text
H.G=8,
P.G=40.
```

Suppose an unknown fibration fiber F improves this:

```text
P.F < 40.
```

By Z40B,

```text
3e <= P.F < 40,
```

so

```text
e=H.F <= 13.
```

Adjunction for a smooth fiber gives

```text
e = 2g(F)-2,
```

hence e is even.

The degree-eight case is source-completely exhausted by the 28 Stoll--Testa fibrations, whose
minimum on this support is 40.

Therefore the only possible improving degrees are

```text
e=10 or e=12.
```

No degree >=14 fiber can improve 40 because

```text
P.F >= 3e >= 42.
```

This turns the previously open higher-degree fibration question into two exact finite lattice
shells.

## 3. Contact requirements in the two remaining shells

Write

```text
M=sum_(i in Sigma) E_i.F.
```

### Degree 10

```text
P.F = 70-4M <40,
M<=10.
```

Thus

```text
M in {8,9,10},
P.F in {38,34,30}.
```

The general fiber has genus 6 and is canonically embedded in a P5 hyperplane.

### Degree 12

```text
P.F = 84-4M <40,
M<=12.
```

Hence necessarily

```text
M=12,
P.F=36.
```

So the degree-12 shell is an equality case of the Z33/Z40B support-hyperplane contact bound:

```text
M=e.
```

The general fiber has genus 7.

## 4. Degree-10 residual reduction

A smooth genus-6 canonical fiber of degree 10 spans a P5, hence lies in a unique hyperplane.
The complete hyperplane section has degree 16, so its residual divisor

```text
D=H-F
```

is effective of degree 6.

Numerically,

```text
H.D=6,
D^2=-4,
F.D=10.
```

Stoll--Testa Theorem 17 proves that there is no integral sextic on the cuboid surface.

Therefore any degree-10 fibration candidate forces D to be a reducible effective divisor whose
positive-degree irreducible components are among the classified degree-2/4 curves.

This converts the degree-10 shell into a finite residual-configuration problem on the retained
known-curve intersection matrix.

## 5. Next exact computation

The remaining fibration-improvement problem for the size768 support is now:

```text
A. degree 10:
   enumerate reducible degree-6 residual divisors D=H-F made from classified low-degree
   components plus exceptional components, require F=H-D to be primitive nef,
   F^2=0 and P.F in {30,34,38}.

B. degree 12:
   enumerate primitive nef isotropic Picard64 classes with
   H.F=12,
   sum_Sigma E_i.F=12,
   P.F=36.
```

If both are empty, then

```text
min over ALL fibrations P.F =40
```

for the size768 survivor as well, and the rank-3 fibration is globally optimal on all three
balanced hard-core orbits.

## Firewalls

```text
size48_global_fibration_optimum_proved=true
size768_global_fibration_optimum_proved=false
size768_improving_degree_set=[10,12]
main_credit_changed=false
theorem_credit=false
endpoint_credit=false
MB104_complete=false
merge_authorized=false
```
