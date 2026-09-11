# Stage32 32-01-178 N357 — transport-aware exceptional support capacity

Status: `RESEARCH_CHECKPOINT_CONDITIONAL_ON_N356_AUDIT_NO_MAIN_CREDIT`.

This node is deliberately **not** a continuation of N356 authority. N356 is still `AUDIT_REQUIRED` on PR #1775. N357 only records a stronger conditional consequence of the same optimistic 3-component transport geometry so that research can continue without self-granting N356 audit credit.

## Input geometry

Use the N356 12-cell intersection graph of the two six-block exceptional partitions. It is three disjoint `2 x 2` components, four exceptional labels per nonempty cell. The stored ten exceptional prefix coordinates occupy three cells:

- `a = E101+E102+E103`; its cell has one omitted label;
- `b = E97+E98+E99`; its cell has one omitted label;
- `c = E93+E94+E95+E96`; this is the unique stored cell with no omitted label.

Let `s` be support among the ten stored exceptional coordinates, `M` their total mass, and let `K=ceil((d-16g+16)/4)` be the already-audited exceptional-support lower bound. Write `h=d/2`; all FULL178 degrees are even.

For a hypothetical genuine extension, let the two factor degrees be `n1,n2` with `n1+n2=d`. Every positive omitted exceptional coordinate consumes at least one unit of both its row-block and column-block mass budget. Therefore the maximum number of omitted positive coordinates is bounded by a unit-capacity max-flow on the same transport graph, with edge capacities equal to the number of omitted labels in each cell.

## Exact optimistic support capacities

The support max-flow is symmetric and concave in `(n1,n2)`. With fixed `n1+n2=d`, every component is simultaneously maximized at the balanced split `n1=n2=h`. At that split the three component capacities are exactly:

```text
S0 = min(16, d)
SA = min(13, d-a, d-2a+4, h+5)
S3 = min(9, d-b-c, d-2b, d-2c+1)
```

Here:

- `S0` is the all-omitted `2 x 2` component (16 omitted slots);
- `SA` is the component whose `a` cell has exactly one omitted slot (13 omitted slots total);
- `S3` is the component containing opposite fixed cells `b,c`, where the `c` cell has zero omitted slots and the `b` cell has one (9 omitted slots total).

Thus every genuine extension satisfies the support upper bound

```text
S_omit <= Srem := S0 + SA + S3 <= 38.
```

The total omitted support is also at most the omitted mass `e-M`. Consequently the new necessary condition is

```text
s + min(e-M, Srem) >= K.
```

N220 used the coarser optimistic suffix bound

```text
s + min(e-M, 38) >= K.
```

so N357 is zero-loss relative to genuine extensions and can only strengthen N220/N356; it never labels an N220-rejected prefix a survivor.

## Why the formulas are exact

Each component is a small capacitated bipartite flow. At the balanced split the min-cut families reduce to the displayed terms.

For the `a` component, row/column residual capacities are `(h-a,h)` on both sides and omitted-cell capacities are `(1,4;4,4)`. The non-dominated cuts are exactly `13`, `d-a`, `d-2a+4`, and `h+5`.

For the `b,c` component, omitted-cell capacities are `(4,0;1,4)` after orienting the saturated `c` cell as the zero edge. The non-dominated cuts are exactly `9`, `d-b-c`, `d-2b`, and `d-2c+1`.

The all-omitted component contributes `min(16,2n1,2n2)`, hence `min(16,d)` at balance. Max-flow as a minimum of affine cut capacities is concave; transposition gives symmetry in `n1,n2`, so the fixed-sum maximum is attained at equality. The three balanced maxima are simultaneously attainable because all three components use the same balanced factor degrees.

## Strictness witness inside existing scalar/N355/N356 constraints

Take

```text
g=0, d=100, e=200, h=50, K=29
(x0,x1,x2,x3,x5,x6,x7,x8,x9,x10)
= (0,50,50,0,0,0,0,0,0,0).
```

Then `a=50`, `b=50`, `c=0`, `M=100`, `s=2`. The canonical prefix symmetry/parity rules hold, N355 has `max(a,b,c)=h`, N356 has `b-c=50 <= 3d-e=100`, and N220 has `2+min(38,100)=40 >=29`.

But N357 gives

```text
S0=16, SA=4, S3=0, Srem=20,
2+min(100,20)=22 < 29,
```

so the prefix is impossible. Therefore the support-capacity route is strictly stronger, not a restatement of N220 or N356.

A symbolic exact replay for the whole `(g,d,e)=(0,100,200)` stratum gives:

```text
N356 exceptional-prefix count = 49,048,088,431,446
N357 support-aware count       = 49,030,556,814,634
incremental exceptional reject =     17,531,616,812
normal x4 block                =                901
incremental terminal reject    = 15,795,986,747,612
```

These numbers are research evidence only until N356 itself is externally hostile-audited and N357 receives its own retained census/audit boundary.

## K=48 boundary corollary

When `K=48`, N220 acceptance already forces all ten stored coordinates positive and at least 38 units of omitted mass. Hence N357 requires `Srem=38`. For the large boundary rows this is equivalent to

```text
a <= h-5,
b <= h-5,
c <= h-4,
b+c <= d-9.
```

In particular:

- `g0-d176`: `a<=83`, `b<=83`, `c<=84`, `b+c<=167`;
- `g1-d192`: `a<=91`, `b<=91`, `c<=92`, `b+c<=183`.

These are conditional candidate cuts only; no MAIN pruning count is assigned here.

## Firewalls / next unit

- N356 external hostile audit is still required before any N357 promotion path.
- No N356 or N357 MAIN pruning credit is granted here.
- No N350 producer registration, production COMPLETE, N104 release, FULL178 completion, theorem/receiver/endpoint/Stage32 closure, or Perfect Cuboid claim.
- No heavy compute and no merge authorization.

Next bounded research unit: build the exact all-178 symbolic census carrying `Srem` and freeze it as a candidate only after N356 audit disposition is known.
