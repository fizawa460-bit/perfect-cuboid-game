# Stage32 MB104 — known-conic closure of low incidence and balanced-16 quotient

Status: **RETAINED UNIFORM-RAY REDUCTION / INC15+INC14 CLOSED / BALANCED INC16 = FOUR AUT ORBITS / WHOLE SPAN5 OPEN / MB104 INCOMPLETE / NO CREDIT**

This leaf continues the audited MB104 checkpoint at exact head `39a56d2a9abda0c051145172ff61d67eef0bdb14`. The scope remains the displayed genus-one span-five Picard ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,  l>=1,
```

with `|Sigma|>=14` and box-node support span equal to `P^5`. It does not cover arbitrary unequal exceptional coefficients.

## Input geometry

The retained known-conic adapter gives 32 smooth conics. Starting from

```text
a1=0,
a2=-b3,
a3=-b2,
b1=-c,
```

the exact nine-generator `Aut(S)` node action produces one orbit of exactly 32 six-node conic supports.

For a known conic `Q` meeting `n_Q` supported nodes,

```text
D_l.Q = 14l - 4l n_Q.
```

Hence `n_Q>=4` forces `Q` as a fixed component of every effective divisor in `|D_l|` and excludes an irreducible member of the displayed ray.

## Incidence 14: all five ambient orbits close

The five exact representative support masks are

```text
0000185aa566   orbit 96
00033c123303   orbit 192
00033c123330   orbit 192
0005185aa524   orbit 384
0005185aa581   orbit 384
```

The verifier reconstructs the `Aut(S)` action, checks that these orbits are pairwise disjoint and have total size

```text
96+192+192+384+384 = 1248,
```

matching the retained complete incidence-14 ambient population.

For every representative, exactly two of the 32 known conics contain six of the 14 supported nodes. Thus each representative has

```text
D_l.Q = 14l - 24l = -10l < 0
```

for two known conics. By automorphism transport, every incidence-14 ambient orbit is excluded for the displayed uniform ray.

This subsumes the earlier direct section-factorization closure of the size-96 orbit and closes the other four incidence-14 orbits as well.

## Incidence 15: every possible N>=14 support closes

The unique incidence-15 ambient orbit has size 256. A representative has support mask

```text
111919162121.
```

The full 15-node support meets three known conics in incidence

```text
[6,6,6].
```

A support-span-five carrier inside this ambient node set can use `N=14` or `N=15` box nodes. Every one of the fifteen possible one-node omissions remains rank six and therefore still spans the same `P^5`. For every such 14-node subset, the three negative known-conic incidences are exactly

```text
[6,6,5].
```

Hence every `N=14` or `N=15` support in the incidence-15 ambient orbit has a fixed known conic. The entire incidence-15 orbit is excluded for the displayed uniform ray.

## Surviving incidence 16 supports

The previous capacity leaf left only balanced `N=14` supports:

- incidence-16 size-3 ambient orbit: 32 supports on a representative, with elliptic-quartic counts `(7,7,7,7)`;
- incidence-16 size-24 ambient orbit: 64 supports on a representative, with counts `(7,7)`.

Every retained balanced support has rank six, so it spans a unique ambient `P^5`. Therefore supports transported to distinct ambient hyperplanes cannot coincide. The global population is exactly

```text
3*32 + 24*64 = 1632.
```

The exact `Aut(S)` quotient of these 1,632 supports has only four orbits:

```text
canonical mask   orbit size
0000770000ff       48
00007b0000ff       48
000707000f0f      768
00070b000f0f      768
```

The first two meet 16 of the 32 representative supports in the size-3 ambient class; the last two meet 32 of the 64 representative supports in the size-24 ambient class. Their orbit-size sum is `1632`.

Thus the displayed uniform P5 ray has been reduced from the complete 1,655 ambient-hyperplane list to four exact support orbits.

## Why the retained low-degree test-curve library stops here

The same exhaustive replay transports one retained incidence-16 elliptic quartic under `Aut(S)` and obtains exactly 12 eight-node elliptic-quartic supports.

For every one of the 96 representative balanced supports:

```text
maximum supported nodes on any of the 32 known conics = 2,
maximum supported nodes on any of the 12 elliptic quartics = 7.
```

Therefore

```text
known conic:       D_l.Q >= 14l-8l = 6l > 0,
elliptic quartic:  D_l.Q >= 28l-28l = 0.
```

No retained low-degree conic/quartic test curve has negative pairing on the balanced hard core.

The zero-pairing quartics have a rigid orbitwise pattern:

- each size-48 support orbit has four `n_Q=7` quartics, and every supported node lies on exactly two of them;
- each size-768 support orbit has two `n_Q=7` quartics, and every supported node lies on exactly one of them.

An irreducible effective carrier in class `D_l` would therefore have to be disjoint on the resolution from these zero-pairing quartics. Downstairs it shares their box nodes, so this becomes an exceptional-landing/tangential compatibility question. The retained local-jet wall explicitly leaves such landing and first-jet freedom open; no contradiction is claimed here.

## Consequence

For the displayed uniform genus-one P5 ray:

```text
incidence 24: closed by fixed components,
incidence 20: closed by fixed components,
incidence 19: closed by fixed components,
incidence 16: exactly four balanced-support Aut(S) orbits survive,
incidence 15: closed by known conics,
incidence 14: all five ambient orbits closed by known conics.
```

So the next useful leaf is no longer generic low-incidence section factorization. It is the four-orbit balanced-16 hard core, with the most plausible new lever being exceptional landing / tangent compatibility against the zero-pairing elliptic quartics, or a genuinely stronger Picard/effective-cone input.

## Verification

`verify_mb104_genus1_span5_known_conic_balanced_quotient.py` performs a fail-closed source-lock preflight, reconstructs the exact 48-node model and order-1536 `Aut(S)` action, builds the 32 known conics and 12 elliptic quartics, checks all incidence-14/15 supports, enumerates the 32+64 balanced representative supports, and computes their global four-orbit quotient.

No MB-dedicated automatic workflow is required by the active mission. Exact-head CI is not claimed for this research verifier; hostile audit should execute it directly.

## Firewalls

- This closes only the displayed **uniform** P5 Picard ray outside the four balanced incidence-16 support orbits.
- The four balanced support orbits are not excluded.
- Arbitrary genus-one span-five Picard classes with unequal exceptional coefficients remain open.
- Genus-one support-span six and genus-zero full-span six remain open.
- No population-wide finite degree window is proved.
- MB104 remains incomplete; finite Picard enumeration remains unreleased.
- No receiver, theorem, endpoint, Perfect-Cuboid, or merge credit.
