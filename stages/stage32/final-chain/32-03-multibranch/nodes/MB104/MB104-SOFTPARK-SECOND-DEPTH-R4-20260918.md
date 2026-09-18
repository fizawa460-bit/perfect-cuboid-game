# Stage32 MB104 — SOFT-PARK second-depth screening Round 4 — 2026-09-18

Status: **ROUND 4 COMPLETE / NO THIRD-DEPTH ADVANCE / ALL SIX PARKED OR ABSORBED / NO MATHEMATICAL CREDIT**

## Scope

Round 4 revisits the deformation/obstruction family:

```
W1   smaller Bogomolov--Reider / canonical subcluster
W21  lower-rank polar / degeneracy construction
W22  stable-map obstruction / negative virtual dimension
W24  distributional conductor / different
W27  reduced / cosection semiregularity
W28  multiplier / adjoint interpolation
```

The target remains

```
D_l=7lH-4l sum E_i,
D_l^2=336l^2,
K.D_l=112l,
Delta=168l^2+56l,
g(normalization)=1.
```

Promotion requires a source-complete all-`l` contradiction or an explicit large-`l` cutoff.

## W1 — absorbed by W16

The original full-defect Serre package uses

```
c1=D_l-K,
c2=Delta,
```

with

```
(D_l-K)^2-4Delta
 = -336l^2-448l+16 <0.
```

So the full cluster cannot force Bogomolov instability.

The only viable repair is exactly the one already isolated in W16: produce a **canonical proper** lci Cayley--Bacharach subscheme of only linear size and ensure that its Serre extension is non-split.

Round 1 already showed that a source-complete cluster with

```
length Z_l <=112l
```

would give

```
(D_l-K)^2-4 length Z_l
 >=336l^2-672l+16>0
```

for every `l>=2`.

Thus W1 has no distinct second-depth content left: its useful continuation is W16.

**Disposition: PARK_ABSORBED_BY_W16.**

## W21 — lower-rank polar / degeneracy capacity

The rank-three first-jet bundle was already too large:

```
c2(J^1(O(D_l)))=1008l^2+224l+80.
```

The most optimistic lower-rank replacement would use the rank-two cotangent twist

```
Omega_S^1 tensor O(D_l).
```

For a rank-two bundle twisted by a line bundle,

```
c2(Omega_S^1(D_l))
 = c2(S)+K.D_l+D_l^2
 =80+112l+336l^2.
```

Even if one granted a source-complete rank-two polar section whose zero scheme contained the entire relevant singularity defect, the numerical capacity would satisfy

```
c2(Omega_S^1(D_l))-Delta
 =168l^2+56l+80>0.
```

So even this idealized rank-two capacity is still too large to force an overload.

There is an additional structural issue: the divisor section has a canonical first jet, but not a globally defined ordinary derivative in `Omega_S^1(D_l)` without extra choices.  A cuboid-specific quotient/degeneracy bundle with substantially smaller Chern coefficient would therefore be a genuinely new architecture, not a continuation of the present polar count.

**Disposition: PARK_COEFFICIENT_TOO_LARGE.**

## W22 — stable-map obstruction / negative expected dimension

For an immersed elliptic normalization map

```
f:E->S
```

the normal line has

```
deg N_f=-112l,
h0(N_f)=0,
h1(N_f)=112l.
```

The fixed-target expected dimension is therefore `-112l`.

Negative expected dimension is not emptiness: an isolated obstructed map may exist.

A natural strengthening is cosection localization by a holomorphic two-form.  Kiem--Li show that a holomorphic two-form localizes the **virtual fundamental class** of the stable-map moduli to the degeneracy locus of the form.  This is a virtual-cycle statement; it does not say that all actual stable maps outside that locus are absent.

Likewise semiregularity can kill actual obstruction classes without turning an existing isolated map into a contradiction.

**Disposition: PARK_VIRTUAL_NOT_EXISTENCE.**

External source:
Young-Hoon Kiem and Jun Li, *Gromov--Witten invariants of varieties with holomorphic 2-forms*, arXiv:0707.2986.

## W24 — distributional conductor / different

Because the carrier is a Cartier divisor on a smooth surface, the total dualizing/conductor degree is already fixed by adjunction:

```
deg conductor =2Delta=336l^2+112l.
```

This is an identity, so only **distribution** could help.

At each of the fourteen active A1 nodes there are `8l` minimal smooth transverse branches in the packet.  The retained sharp A1 conductor wall proves that for `r` such branches the contracted reduced germ can achieve

```
delta=r-1.
```

Therefore the complete active support may consume only

```
14(8l-1)=112l-14
```

units of delta in the sharp local model.

The total required defect is

```
Delta=168l^2+56l.
```

Hence the unconstrained remainder can be as large as

```
Delta-(112l-14)
 =168l^2-56l+14.
```

There is no contradiction: the quadratic defect can live in higher contact or off-support singularities.  A distributional conductor theorem useful for MB104 would have to prohibit that remainder, not merely repackage the total conductor identity.

**Disposition: PARK_SHARP_A1_LINEAR_ONLY.**

## W27 — reduced / map semiregularity

The ordinary semiregularity target has dimension

```
p_g=h^2(O_S)=7,
```

while the normal obstruction space for an immersed normalization has dimension

```
h1(N_f)=112l.
```

So even a maximally ranked classical semiregularity map leaves a kernel of dimension at least

```
112l-7.
```

More recent map-semiregularity theory does enlarge the range of situations in which deformations are unobstructed.  Nishinou proves unobstructedness criteria for codimension-one immersed maps and applications to equisingular deformations of nodal curves on surfaces.

But unobstructedness is not an existence obstruction here: since `h0(N_f)=0`, an unobstructed existing map may simply be an isolated smooth point of its deformation functor.

Thus neither ordinary nor map-semiregularity produces an all-`l` contradiction from the current MB104 data.

**Disposition: PARK_UNOBSTRUCTEDNESS_NOT_EMPTINESS.**

External source:
Takeo Nishinou, *Obstructions to deforming maps from curves to surfaces*, J. Math. Soc. Japan 76 (2024), 51--71, DOI 10.2969/jmsj/86878687.

## W28 — multiplier / adjoint interpolation

The connectedness version was already hard-dead because the geometry is of general type rather than log-Fano.

For interpolation, the natural intrinsic ideal attached to a reduced Cartier curve is the adjoint/conductor ideal.  Its full singularity package records the same total genus defect `Delta`.  Feeding a full `Delta`-size zero-dimensional package into a Serre/Bogomolov argument returns the W1 negative-discriminant wall.

Therefore a useful multiplier/adjoint route would again need to extract a **proper canonical smaller subscheme** with enough dependency to force instability or interpolation failure.

That is exactly W16's missing input.  Without such a source-complete proper subcluster, W28 does not define a distinct closing mechanism.

**Disposition: PARK_ABSORBED_BY_W16.**

## Round-4 selection

```
ADVANCE_FOR_THIRD_DEPTH:
  none

PARK / ABSORB:
  W1   -> W16
  W21  rank-two idealized polar capacity still too large
  W22  virtual/cosection localization does not imply actual emptiness
  W24  A1 conductor distribution is sharply only linear in packet branches
  W27  semiregularity/unobstructedness does not contradict isolated existence
  W28  -> W16 proper canonical CB/adjoint subcluster problem
```

Cumulative third-depth candidates remain

```
W4, W16, W20.
```

High reserve:

```
W5.
```

Other reserves:

```
W13, W17, W23.
```

No mathematical closure or downstream credit is claimed.

## Final second-depth round

The only broader SOFT-PARK directions not yet screened at this depth are

```
W3   Aut(S)-norm / representation-theoretic invariant section
W7   singular/abelian-cover BMY corrections
W9   specialization with a receiver-preserving compactification
W12  receiver-preserving explicit degeneration
W25  Lefschetz/monodromy/slope refinement
```

Round 5 should screen exactly these five, then freeze the second-depth portfolio and compare the surviving third-depth candidates before deeper work.
