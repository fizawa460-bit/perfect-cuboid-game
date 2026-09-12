# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / UNIFORM P5 BALANCED HARD CORE 1632 -> 864 / ZERO-QUARTIC ROUTE EXHAUSTED ON SURVIVORS / GLOBAL SINGULARITY-CONDUCTOR FRONTIER / P6 OPEN / NO CREDIT**

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

## Ambient support classification and fixed-component closures

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

Incidence `16` leaves exactly `1632` balanced `N=14` supports, with support-orbit quotient

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

## One size-768 orbit is closed by two-quartic gluing

The two size-768 representatives have zero quartics

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0,
```

meeting transversely at two smooth points.

For `00070b000f0f`, the exact gluing cycle monodromy is

```text
17+12*sqrt(2),
```

which is never a root of unity. Therefore every section of `O(D_l)` vanishes on both zero quartics for every `l>=1`; the whole size-768 support orbit is excluded as an irreducible member of the displayed uniform ray.

Thus

```text
1632 -> 864
```

and the surviving support orbits are

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768.
```

Evidence:

- `GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-OBSTRUCTION.md`
- matching certificate/verifier.

## Null-union and primitive restriction results on the 864 survivors

The Picard/hyperflex calculation gives

```text
O_Q(D_l) ~= O_Q
```

for every zero-pairing retained elliptic quartic and every `l>=1`.

For the two size-48 support orbits, the four zero quartics are pairwise disjoint on the minimal resolution. Their union gives no gluing monodromy obstruction but forces `h1(D_l)>=4`. A primitive degree-seven jet computation then gives

```text
h0(A)=124,
h1(A)=4,
rank(jet_4)=220,
rank(H0(A)->H0(Z4,O_Z4(A))) >= 2.
```

The support stabilizer is transitive on the four zero quartics, so all four are nonfixed in `|A|`; powers give nonfixedness in `|D_l|` for every `l>=1`.

For `000707000f0f`, the connected two-quartic gluing line bundle is trivial, so gluing alone also does not close the orbit. The primitive ambiguity is now resolved exactly:

```text
C = 6H-3 sum E_i:
  h0(C)=122, h1(C)=0,

A = 7H-4 sum E_i:
  h0(A)=124, h1(A)=4,
  rank_Q(i)(jet_4)=220.
```

The proof uses the support hyperplane

```text
L=c-a1-a2-i*a3,
```

whose multiplication injects the 122-dimensional triple-vanishing degree-six space into `H0(A)`, together with two explicit exact degree-seven sections outside the complete `L`-multiple subspace. One of them restricts nontrivially to `Q0`. Stabilizer transport gives nonfixedness of `Q1`, and powers give the result for every `l>=1`.

Evidence:

- `GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-WALL.md`
- `GENUS1-SPAN5-BALANCED16-SIZE48-DEGREE7-RESTRICTION-RANK.md`
- `GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md`
- matching certificates/verifiers.

### Exact retained conclusion

On all three surviving support orbits, every known zero-pairing elliptic quartic is nonfixed for every `l>=1`.

Therefore the following routes are exhausted on the surviving uniform-ray core:

- negative pairing with the retained conic/quartic library;
- static exceptional landing-value avoidance;
- hidden nontrivial `Pic^0` restriction on a zero quartic;
- zero-quartic union gluing monodromy;
- zero-quartic global restriction/fixedness.

No surviving orbit is closed by nonfixedness itself.

## Global singularity/conductor frontier

For an integral member `C_l in |D_l|` of normalization genus one,

```text
p_a(D_l)=1+168l^2+56l,
Delta_total=168l^2+56l.
```

The retained Lu--Miyaoka adapter gives

```text
n_ordinary_node_or_triple(C_l) >= max(0,112l-224).
```

Hence for `l>=3`, a hypothetical carrier cannot realize essentially all genus defect in a single complicated cusp while having no ordinary nodes/triples. The required ordinary singularity population grows linearly with `l`.

This is not yet a contradiction: the total delta budget is quadratic. The active problem is to combine the forced `Omega(l)` ordinary singularities with canonical degree, conductor/branch accounting, fibration ramification, global interpolation, or a stronger source-supported singular-curve inequality so as to bound `l`, force a forbidden incidence, or exclude the 864 supports.

## Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-GLOBAL-SINGULARITY-CONDUCTOR`:

1. seek a stronger global inequality controlling singularity count/type against `K.C=112l`, `C^2=336l^2`, and normalization genus one;
2. translate any such inequality into the retained branch/conductor semantics without double-counting box-node contributions;
3. test whether the forced ordinary nodes/triples can be charged through one or more genus-five fibrations only with an additional global tangent condition;
4. if no contradiction is available, isolate the exact missing invariant rather than reopening fixed finite local-jet counting;
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
