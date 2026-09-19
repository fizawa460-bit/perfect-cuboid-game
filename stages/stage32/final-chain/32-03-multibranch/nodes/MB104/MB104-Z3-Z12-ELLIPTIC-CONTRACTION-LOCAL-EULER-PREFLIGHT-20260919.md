# MB104 Z3+Z12 — elliptic-contraction local-Euler preflight — 2026-09-19

Status: **PARALLEL PRE-AUDIT THRESHOLD REDUCTION / EXTERNAL LOCAL-INVARIANT WALL / NO CREDIT**

## Purpose

Combine two original Z routes:

- Z3: exact null-locus geometry of the balanced incidence-16 primitive ray;
- Z12: BTVA support-specific symmetric-differential growth at the N=14 frontier.

The point is not to repeat ordinary BTVA on the 48 A1 nodes.  The new input is that a hypothetical irreducible carrier in |lP| is disjoint from the zero-pairing elliptic quartics, and Z3 now proves that these quartics are genuine components of the exact null locus of a big-nef ray.

A disjoint negative elliptic quartic may be contracted while the carrier avoids the resulting singular point.  Such a contraction could add a new local symmetric-differential Euler contribution not present in the ordinary N=14 A1 count.

## 1. Existing N=14 deficit

For the perfect-cuboid surface with 48 A1 points, BTVA gives the exact cubic coefficient for a curve meeting N box nodes:

```text
c_N = (144-11N)/108.
```

Thus

```text
c_14 = -5/54.
```

Any modified singular model / local-Euler accounting must add strictly more than

```text
5/54 * m^3 + O(m^2)
```

to recover positive cubic growth.

## 2. Contractible null elliptic quartics

For every surviving balanced support, the primitive ray

```text
P=7H-4 sum_(i in Sigma)E_i
```

is big and nef and its nonexceptional null curves are exactly the zero-pairing elliptic quartics.

Each such quartic has

```text
Q^2=-4,
P.Q=0,
O_Q(P)~=O_Q.
```

An irreducible effective carrier C in |lP| must be disjoint from Q.

A single smooth elliptic (-4)-curve is negative definite and is analytically contractible.  Contracting one such Q produces a normal surface singularity with exceptional divisor a smooth elliptic curve of self-intersection -4 (a simple-elliptic-type local model).  The carrier does not pass through the contracted point.

This gate uses only a **single** quartic contraction at a time, so intersections among multiple zero quartics do not need to be contracted simultaneously.

## 3. Exact local coefficient threshold

Write

```text
epsilon_4
```

for the leading cubic coefficient of the extra local regularity/Euler contribution supplied by one contracted (-4) elliptic exceptional curve in the BTVA/Wahl symmetric-differential count, relative to leaving that curve uncontracted on the smooth model.

Then:

### Surviving size-768 orbit

There are two zero-pairing quartics, but they intersect, so the clean shallow model contracts only one at a time.

A single contraction would repair the ordinary N=14 sign exactly if

```text
epsilon_4 > 5/54.
```

### Size-48 orbits

Their four zero quartics are pairwise disjoint on the smooth resolution.  If the local contributions add independently under simultaneous contraction, positivity would follow if

```text
4 epsilon_4 > 5/54,
```

i.e.

```text
epsilon_4 > 5/216.
```

Even without simultaneous additivity, a one-quartic contraction has the same universal threshold 5/54.

## 4. Literature/source audit

The currently source-locked explicit local-Euler technology is for quotient singularities, especially A_n:

- BTVA 2022 computes the A1 contribution used in the perfect-cuboid N=13 theorem;
- Bruin--Ilten--Xu 2025 gives explicit quasi-polynomial local Euler characteristics for A_n singularities;
- Asega--De Oliveira--Weiss 2025 develops quotient-singularity cotangent-bigness invariants and extension results, again in the quotient/A_n setting.

A targeted academic search did not locate a source-complete formula for the symmetric-power cotangent local Euler characteristic of a simple elliptic surface singularity with exceptional elliptic curve of self-intersection -4.

Therefore no numerical value of epsilon_4 is imported or guessed here.

## 5. What would constitute progress

This route is now reduced to one local invariant.

Useful success shapes:

```text
(A) derive/source-lock epsilon_4 and prove epsilon_4 > 5/54:
    -> ordinary N14 deficit is repaired already after one zero-quartic contraction;

(B) prove 5/216 < epsilon_4 <= 5/54:
    -> potentially closes the two size-48 orbits using four disjoint contractions,
       but not the surviving size-768 orbit via one contraction;

(C) prove epsilon_4 <= 5/216:
    -> this contraction-enhanced BTVA route cannot repair N14 even for size-48;

(D) show BTVA/Wahl local-Euler formalism cannot be applied to this non-quotient contraction:
    -> freeze this hybrid route.
```

## 6. Interpretation

This is a genuine composition of the original Z3 and Z12 routes:

```text
Z3 supplies exact disjoint negative elliptic null curves;
Z12 supplies the exact missing cubic amount 5/54.
```

The remaining question is local and independent of l.

No carrier exclusion is claimed until the local coefficient is source-complete.

## Firewalls

```text
epsilon4_computed=false
N14_BTVA_repaired=false
size48_orbits_excluded=false
surviving768_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
