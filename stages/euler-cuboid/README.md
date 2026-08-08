# Euler-cuboid side — face-diagonal-first research track

> **ROLE:** independent research track beside the existing space-diagonal-first stages
>
> **STATUS:** bootstrap / artificial-seed construction
>
> **IMPORTANT:** this track does not modify or reinterpret the active `stages/stage13/` work.

## 1. Purpose

This directory starts the **face-diagonal-first** side of the perfect-cuboid research.

The existing Stage13 line approaches the problem from the space-diagonal side.  This track deliberately starts from the opposite direction: first construct and classify cuboids having integral **face diagonals**, without using integrality of the space diagonal as an entry condition.

The long-term ladder is

```text
exactly one integral face
    -> two integral faces
    -> three integral faces (Euler brick)
    -> compare with / approach the perfect-cuboid condition
```

The first task is intentionally elementary and constructive: build clean artificial seed examples in each canonical face direction before attempting asymptotics or large enumeration.

## 2. Canonical notation

Use positive integer edges in canonical order

```text
0 < a < b < c
```

and, unless a task explicitly says otherwise, primitive normalization

```text
gcd(a,b,c) = 1.
```

Define the three face diagonals

```text
d_ab^2 = a^2 + b^2
d_ac^2 = a^2 + c^2
d_bc^2 = b^2 + c^2
```

and the space diagonal

```text
D^2 = a^2 + b^2 + c^2.
```

For the bootstrap tasks, **`D` is not an acceptance condition**.  It may be integral or nonintegral; the one-face classification is determined only by the three face diagonals.

## 3. Initial exactly-one populations

Split the artificial seeds into three canonical directions.

### `ab`

```text
d_ab is integral
d_ac is nonintegral
d_bc is nonintegral
```

### `ac`

```text
d_ac is integral
d_ab is nonintegral
d_bc is nonintegral
```

### `bc`

```text
d_bc is integral
d_ab is nonintegral
d_ac is nonintegral
```

These are the three first populations to construct and validate independently.

## 4. Bootstrap plan

```text
E-1a  construct artificial primitive ab-only seeds
E-1b  construct artificial primitive ac-only seeds
E-1c  construct artificial primitive bc-only seeds
E-1d  verify exact-one classification and remove duplicates/scalings
E-1e  compare the three construction mechanisms
```

Only after all three directions have reliable seeds should this track move to systematic enumeration or density questions.

## 5. Next structural step

After exactly-one seeds are understood, introduce the three exactly-two-face types

```text
ab+ac
ab+bc
ac+bc
```

and finally the three-face condition

```text
d_ab, d_ac, d_bc all integral,
```

which is the Euler-brick population.

The space diagonal remains a separate condition until a later bridge to the perfect-cuboid problem is explicitly introduced.

## 6. Separation from the space-diagonal track

Keep this directory logically independent from `stages/stage13/` while both investigations are active.

```text
stages/stage13/       space-diagonal-first side
stages/euler-cuboid/  face-diagonal-first / Euler side
```

Shared notation or later theorems may eventually be bridged explicitly, but no current Stage13 file should be edited merely to start this track.

## 7. Immediate next task

Start with `E-1a`: produce several small primitive canonical `ab-only` artificial examples, record the construction rule, and verify all three face-square tests exactly.
