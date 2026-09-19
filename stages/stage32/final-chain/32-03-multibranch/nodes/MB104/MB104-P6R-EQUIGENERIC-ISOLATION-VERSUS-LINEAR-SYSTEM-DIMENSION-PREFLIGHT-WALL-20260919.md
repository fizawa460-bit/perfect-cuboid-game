# MB104 P6R — equigeneric isolation versus linear-system dimension preflight wall — 2026-09-19

Status: **PRE-AUDIT EXACT EXPECTED-DIMENSION WALL / NO CREDIT**

## Exact numerical input

For the smooth minimal cuboid surface,

```text
p_g=7,
q=0,
chi(O_S)=8,
K_S=H,
K^2=16.
```

For the hostile ray

```text
P^2=336,
K.P=112.
```

Hence Riemann--Roch gives, for `D=lP`,

```text
chi(O_S(lP))
 = chi(O_S) + (D.(D-K))/2
 = 8 + (336 l^2 - 112 l)/2
 = 168 l^2 - 56 l + 8.
```

For a hypothetical integral member `C in |lP|` with normalization genus one,

```text
p_a(C)=1+(C^2+K.C)/2
      =1+168 l^2+56 l,
delta(C)=p_a-g
        =168 l^2+56 l.
```

## Expected-dimension comparison

If one were allowed to treat the total delta invariant as `delta(C)` independent conditions on the complete linear system, then even under the optimistic vanishing identity

```text
dim |lP| = chi(O_S(lP))-1
         =168 l^2-56 l+7
```

one would obtain

```text
dim |lP| - delta(C)
 = 7 - 112 l < 0
```

for every `l>=1`.

This is numerically strong but it is not a valid exclusion theorem by itself.

## Why P6F does not supply the missing independence theorem

P6F proves, using Dedieu--Sernesi,

```text
H^0(C, A tensor O_C(C)) = 0
```

for any hypothetical genus-one carrier. Equivalently, the reduced tangent cone to the equigeneric locus at `[C]` is zero.

Thus a hypothetical carrier is an isolated, highly superabundant point of the equigeneric locus.

That conclusion is compatible with the negative expected dimension above. It does not imply that the conductor/delta conditions impose independent linear conditions on the ambient complete linear system. In fact, P6F says precisely that the local equigeneric geometry is exceptional rather than a regular Severi situation.

No retained T-smoothness, nodal-independence, semiregularity, or Severi-regularity theorem applies to this singularity package strongly enough to upgrade

```text
expected dimension < 0
```

to emptiness.

## Disposition

The exact quadratic terms cancel:

```text
linear-system RR growth : +168 l^2 - 56 l,
genus-drop delta        : +168 l^2 + 56 l,
difference              : 7 - 112 l.
```

So the heuristic pressure is maximal already at `l=1`, but the missing ingredient is qualitative rather than numerical: independence/regularity of the singularity conditions.

P6R is therefore parked as an expected-dimension wall.

## Routing consequence

The P6 chain has now accumulated several independent walls around the same isolated hostile support. A better use of the current branch is the finite-first Z-lane reduction added in Z33C.

The archived uniform-ray quotient leaves exactly four balanced incidence-16 Aut(S) support orbits:

```text
0000770000ff   orbit 48
00007b0000ff   orbit 48
000707000f0f   orbit 768
00070b000f0f   orbit 768
```

Next leaf:

```text
MB104-Z33D-BALANCED16-FOUR-ORBIT-EQUALITY-GATE
```

Target: combine the new Z33A equality/simple-contact rules with the already-retained zero-pairing elliptic-quartic profiles on these four exact hard-core orbits before reopening any general-m Hilbert machinery.

## Firewalls

```text
delta_independent_conditions_assumed=false
negative_expected_dimension_used_as_emptiness=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
