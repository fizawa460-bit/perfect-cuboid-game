# MB104 Z39 — complete P-null curve finite-degree reduction — 2026-09-19

Status: **PRE-AUDIT EXACT FINITE-DEGREE REDUCTION / NO CREDIT**

## Purpose

After Z38, finite formal restriction to the already-known null curves is exhausted. Before assuming
semiampleness or a contraction whose exceptional locus is complete, first determine how large an
**unknown** nonexceptional integral curve with

```text
P.R=0
```

could be.

This produces an exact finite gate.

## Input

For any nonexceptional integral curve `R` on the smooth cuboid resolution put

```text
e = H.R > 0,
M_i = E_i.R >= 0.
```

For the balanced ray

```text
P = 7H - 4 sum_(i in Sigma) E_i,
|Sigma|=14.
```

The retained Z21 A1 root-lattice Hodge projection is

```text
R^2 + (1/2) sum_(all 48 i) M_i^2 <= e^2/16.
```

If `P.R=0`, then

```text
7e = 4 sum_(i in Sigma) M_i.
```

Write

```text
M = sum_(i in Sigma) M_i = 7e/4.
```

Because M is an integer and gcd(7,4)=1,

```text
4 | e.
```

## Cauchy plus Hodge

Cauchy on the 14 supported exceptional intersections gives

```text
sum_(i in Sigma) M_i^2
 >= M^2/14
 = (49e^2/16)/14
 = 7e^2/32.
```

Discarding the nonnegative squares from the other 34 exceptional curves only weakens the Hodge
bound, hence

```text
R^2
 <= e^2/16 - (1/2)*(7e^2/32)
 = -3e^2/64.
```

## Adjunction

Since `R` is integral,

```text
p_a(R) >= 0.
```

With `K=H`, adjunction gives

```text
R^2 + e = 2p_a(R)-2 >= -2,
```

so

```text
R^2 >= -e-2.
```

Combining both inequalities,

```text
-e-2 <= -3e^2/64,
3e^2 <= 64e+128.
```

The positive root of the quadratic is

```text
(64 + 16 sqrt(22))/6 < 24.
```

Therefore

```text
e <= 23.
```

Together with `4|e`:

```text
e in {4,8,12,16,20}.
```

Thus every nonexceptional integral `P`-null curve lies in five hyperplane degrees.

The remaining obvious null curves are the unsupported exceptional curves `E_j`, for which
`P.E_j=0). Supported exceptional curves have `P.E_i=8>0`.

## Consequence

Completeness of the null locus is now a finite Picard-lattice problem, not an unbounded curve
classification problem.

A retained exact lattice interface exists in Stage33-07. At exact head

```text
dbf98cacc6d1349ead658ef064fefe48f6d5e4f4
```

`stage32_picard_marking_retained.py` locks the Stage32 rank-64 Picard marking, including the
positive-definite rank-63 `H^perp` data and all 140 known-class rows. Stage33-09 also supplies the
exact INDLIST-to-Magma Picard basis bridge.

Therefore the next gate is concrete:

```text
MB104-Z40-P-NULL-PICARD64-FINITE-ENUMERATION
```

Enumerate lattice classes of degree

```text
4,8,12,16,20
```

that satisfy

```text
P.R=0,
p_a(R)>=0,
R.C_known>=0
```

for every known irreducible curve not equal to R, and then determine which surviving classes are
already represented by the known null curves. This is a numerical-effectivity filter only; a
surviving lattice class is not automatically an effective curve.

## Source locks

Current compact branch:

- Z21 re-audit note blob `c45c4468bd3eb0a88ff2543f2b65af3458d71c4a`.

Stage33 retained Picard interface:

- PR #1468 exact head `dbf98cacc6d1349ead658ef064fefe48f6d5e4f4`;
- `stages/stage33/33-07/stage32_picard_marking_retained.py`
  blob `5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7`;
- retained Stage32 Picard core SHA256
  `de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870`;
- pinned Stoll source blob
  `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Firewalls

```text
P_null_nonexceptional_degree_set={4,8,12,16,20}
complete_null_locus_classified=false
effectivity_of_unknown_lattice_classes=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
