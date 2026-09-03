# Stage32 post-1490 O210 Bolza six-Weierstrass collision delta bound

Scope: fixed recovered V6 class `g1-d186` only, at the exact extremal profile
`O=210`, `q'=4`. This note consumes the exact birational correspondence /
`D4 direct-sum D4` trace reduction and the retained 48-node marked incidence.
It gives a support-forced lower bound on the singularity defect of the
correspondence image. It does not construct or exclude a carrier.

## Retained exact inputs

Let

`F=(f1,f2): Y -> Gamma subset C0 x C0`

be the pair map. The preceding exact reduction proves that `F` is birational,
so `Y` is the normalization of the integral curve `Gamma`. Its normalization
has genus 106 and its bidegree is `(105,81)`.

The common quadratic cover is the simultaneous pullback of the
hyperelliptic double cover `C0 -> X(4)` through both factor maps. At the O210
extremal profile the normalized cover `pi:Y->N` is ramified at exactly the
210 odd exceptional contacts. The exact contact histogram is

`210 x m1 + 28 x m2`.

At an exceptional contact, the retained 48-node marking gives one first-factor
cusp and one second-factor cusp. The unique point of `Y` over an odd `m1`
contact maps under `(f1,f2)` to the corresponding pair of ramification points
of `C0->X(4)`, i.e. to a pair of the six Weierstrass points of the Bolza curve.

The marked incidence realizes only 12 of the 36 possible ordered
Weierstrass pairs; each realized pair consists of four exceptional nodes.

## Exact pair masses

For exceptional label `j=93,...,140`, let `M_j=C.E_j`, read directly from the
last 48 entries of the source-locked recovered V6 all-140 pairing vector.
At node `j`, write `y_j` for its number of `m2` contacts. Since every contact
has multiplicity one or two,

`0 <= y_j <= floor(M_j/2)`

and the number of odd `m1` contacts at that node is `M_j-2*y_j`.

Aggregate over the four nodes belonging to one marked cusp pair `p`:

`M_p = sum_j M_j`,
`c_p = sum_j floor(M_j/2)`,
`y_p = sum_j y_j`,
`n_p = M_p - 2*y_p`.

The exact replay reconstructs from the retained incidence and witness, rather
than trusting a copied table, the following 12 `(M_p,c_p)` values:

- `(43,41): (5,1)`
- `(42,44): (5,2)`
- `(39,37): (21,10)`
- `(38,40): (25,11)`
- `(35,33): (24,10)`
- `(34,36): (18,7)`
- `(35,36): (19,9)`
- `(34,33): (35,17)`
- `(38,37): (28,13)`
- `(39,40): (34,16)`
- `(43,44): (32,14)`
- `(42,41): (20,10)`.

Their masses sum to 266. Globally `sum y_p=28`, hence `sum n_p=210`.

Each integer `0<=y_p<=c_p` is realizable at the pair-allocation level because
each node contributes a full interval `0,...,floor(M_j/2)`, and Minkowski sums
of integer intervals are integer intervals. Thus the optimization below loses
nothing at the nodewise histogram-allocation layer.

## Delta lower bound from normalization collisions

If `n_p` distinct normalization points of the birational curve `Gamma` map to
the same point of the smooth surface `C0 x C0`, then the local germ of `Gamma`
has at least `n_p` branches there. For a reduced curve singularity on a smooth
surface,

`delta = sum_i delta(branch_i) + sum_{i<j} I(branch_i,branch_j)`,

and every intersection multiplicity between two distinct local branches is at
least one. Therefore

`delta_p >= binom(n_p,2)`.

A source for this standard branch formula is
*Duality for Poincare series of surfaces and delta invariant of curves*,
Research in the Mathematical Sciences (2024),
DOI `10.1007/s40687-024-00457-8`, equation (36) and Example 4.3.

Consequently every O210 carrier satisfies

`delta >= sum_p binom(M_p-2*y_p,2)`

subject to `0<=y_p<=c_p` and `sum y_p=28`.

The accompanying exact dynamic program over only 12 pairs gives

`delta >= 1924`.

One minimizing pair allocation is

`y=(0,0,0,2,2,0,0,7,4,7,6,0)`

in the pair order displayed above, giving

`n=(5,5,21,21,20,18,19,21,20,20,20,20)`.

This has `sum y=28`, `sum n=210`, and
`sum binom(n_p,2)=1924`.

## Consequence in the D4 direct-sum D4 trace lattice

The exact correspondence identity from the preceding leaf is

`Q(T)=8586-delta`.

Hence the six-Weierstrass collision constraint sharpens the trace bound to

`Q(T) <= 6662`.

Since the trace lattice is exactly `D4 direct-sum D4`, the exact theta-series
prefix through `Q<=6662` (`half-trace <=3331`) contains

`1,999,581,686,774,833`

integral endomorphisms, including zero.

Thus this geometric collision constraint is substantial but still
nonexcluding. Materializing the residual Rosati lattice is still neither
storage-safe nor mathematically useful.

## Verdict / next datum

O210 remains OPEN. The useful next exact datum is no longer an endomorphism
box enumeration. The quotient

`q:X -> C0 x C0`

is an etale V4 cover. For the carrier image curve upstairs, singular collisions
of `Gamma` arise from intersections with its nontrivial deck translates.
An exact computation of those translate-intersection numbers from the retained
V6/Picard class, or an equivalent source-locked quotient singularity invariant,
can constrain the collision pattern beyond the coarse lower bound above.

Firewalls:

- the delta bound is necessary only;
- pair-level `m2` allocation is not analytic realization;
- an integral endomorphism is not a geometric correspondence;
- O186/O188 and the Abel-Jacobi-zero closure remain closed;
- FULL178 remains inactive;
- no receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
