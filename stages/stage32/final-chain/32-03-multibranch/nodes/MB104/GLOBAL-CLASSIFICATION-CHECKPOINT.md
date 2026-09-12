# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / UNIFORM P5 BALANCED HARD CORE REDUCED 1632 -> 864 / ONE 768 ORBIT CLOSED BY ZERO-QUARTIC GLUING / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of `R8<d/4+O(1)` remains frozen until a genuinely new lever appears.

The most recent hostile-audited retained boundary is exact head

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`. The present continuation is newer retained work and has not yet been hostile-audited.

## Hard sectors and span semantics

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

`span` refers to the box-node support, not containment of the carrier curve in its support hyperplane.

## Displayed uniform genus-one P5 ray

```text
D_l=7lH-4l sum_{i in Sigma}E_i,
|Sigma|=14,
d=112l,
l>=1.
```

For a retained test curve `Q` of degree `e=H.Q` meeting `n_Q` supported nodes,

```text
D_l.Q=l(7e-4n_Q).
```

## Ambient support classification and closures

The exact node-spanned `P^5` hyperplane population is

```text
14:1248, 15:256, 16:27, 19:48, 20:48, 24:28,
```

with 12 `Aut(S)` ambient orbits

```text
14: 96,192,192,384,384
15: 256
16: 3,24
19: 48
20: 48
24: 4,24.
```

For the displayed uniform ray, incidence `24`, `20`, `19`, `15`, and all five incidence-`14` orbits are closed by retained fixed-component arguments.

## Original incidence-16 balanced hard core

Capacity leaves leave exactly `N=14` balanced supports. Globally:

```text
3*32 + 24*64 = 1632.
```

Their complete support-orbit quotient was

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

Known conics and elliptic quartics have no negative pairing on these supports. Static landing-value avoidance also does not close them.

## Zero-quartic Pic^0 and cohomology walls

For every zero-pairing retained elliptic quartic `Q`, exact hyperflex transport gives

```text
O_Q(D_l) ~= O_Q
```

for all `l>=1`. Thus nontrivial degree-zero restriction does not force `Q` fixed.

For one zero quartic,

```text
0 -> O(D_l-Q) -> O(D_l) -> O_Q -> 0
```

has equal Euler characteristics on the first two terms and

```text
H^2(D_l)=H^2(D_l-Q)=0.
```

If `r` is the restriction rank,

```text
h0(D_l)=h0(D_l-Q)+r,
h1(D_l)=h1(D_l-Q)+r,
r in {0,1},
h1(D_l)>=1.
```

The obvious single-quartic Kawamata--Viehweg route is structurally blocked because another zero quartic always has negative intersection with the adjoint residual.

Evidence:

- `GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-*`
- `GENUS1-SPAN5-BALANCED16-RESTRICTION-COHOMOLOGY-*`.

## Support stabilizer reduction: fixedness is all-or-none

For the four canonical balanced supports, exact support stabilizer orders and zero-quartic orbits are

```text
mask             |G_Sigma|   zero quartics   zero-quartic orbit
0000770000ff         32             4                 4
00007b0000ff         32             4                 4
000707000f0f          2             2                 2
00070b000f0f          2             2                 2.
```

Thus on each support orbit the zero quartics form one stabilizer orbit. Since `D_l` is stabilizer-invariant,

```text
one zero quartic fixed <=> all zero quartics fixed,
```

and their individual restriction ranks are simultaneously `0` or simultaneously `1`.

Evidence:

- `GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION.md`
- matching certificate/verifier.

## New closure: nontrivial two-quartic gluing kills `00070b000f0f`

The two size-768 representatives have the same two zero quartics

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0.
```

They meet transversely at exactly two smooth points

```text
R_±=[1:1:i:0:0:±sqrt(2):1].
```

For `000707000f0f`, the omitted nodes are `P27` on `Q0` and `P35` on `Q1`. Explicit hyperflex trivializations give the same gluing ratio `-i` at both `R_+` and `R_-`, so the restriction to the connected union is trivial. This orbit survives this leaf.

For `00070b000f0f`, the omitted nodes are `P26` and `P35`. The two gluing ratios differ, with cycle monodromy

```text
mu = ((2+sqrt(2))/(2-sqrt(2)))^2
   = 17+12sqrt(2).
```

Since `mu>1` in the positive real embedding,

```text
mu^l != 1
```

for every `l>=1`. Therefore

```text
H^0(Q0 union Q1, O(D_l))=0.
```

Every global section of `O(D_l)` vanishes on both zero quartics; they are fixed components. Hence no irreducible effective divisor in the displayed uniform ray exists on this support orbit. By automorphism transport, the entire size-768 orbit represented by

```text
00070b000f0f
```

is closed.

Evidence:

- `GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-OBSTRUCTION.md`
- `GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json`
- `verify_mb104_balanced16_two_quartic_gluing.py`.

## Updated uniform-P5 hard core

The balanced population drops

```text
1632 -> 864.
```

Surviving support orbits are exactly

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768.
```

The second size-768 orbit is no longer part of the displayed uniform-ray frontier.

## Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-THREE-ORBIT-RESTRICTION`:

1. decide restriction/nonfixedness for `000707000f0f`, where the connected two-quartic union has trivial gluing;
2. classify strict-transform intersections for the four zero quartics of the two size-48 supports and determine whether their union imposes any gluing obstruction;
3. if union geometry does not close them, test explicit global degree-`7l` interpolation / multibranch first-jet gluing;
4. seek a whole-null-locus semiampleness/effective-cone input only if source-supported;
5. keep genus-one support-span `P^6` and genus-zero full-span `P^6` active in parallel.

## Firewalls

- support-span five is not closed;
- the displayed uniform P5 ray is not fully closed: three balanced support orbits of total size `864` survive;
- arbitrary unequal exceptional coefficients are not covered;
- genus-one P6 and genus-zero P6 remain open;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and finite Picard enumeration is unreleased;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
