# Stage32 32-01-178 N358 — joint transport/support saturation cut

Status: `RESEARCH_CANDIDATE_NO_MAIN_CREDIT`.

N357 separately maximizes omitted exceptional mass and omitted exceptional support on the same three balanced `2 x 2` transportation components. N358 records the first strict incompatibility between those two optimistic maxima. It consumes no new arithmetic/Picard hypothesis: it only asks whether the N356 mass maximum and N357 support maximum can be attained simultaneously.

## Audited input boundary

N357 is already hostile-audited and consumed by Stage32 MAIN. Its authoritative retained frontier is

- `17,128` strata;
- `47,598,978,285,064,933,810,198` compressed terminals.

Keep N357 notation. Let `d=2h`, let `a,b,c` be the three stored exceptional block sums, `M=a+b+c`, `s` the support of the ten stored exceptional coordinates, and `K=ceil((d-16g+16)/4)`. N356 gives the optimistic exceptional-mass cap

```text
Cmax = min(3d, 3d+c-b).
```

N357 gives omitted-support capacity

```text
Srem = S0 + SA + S3,
S0 = min(16,d),
SA = min(13,d-a,d-2a+4,h+5),
S3 = min(9,d-b-c,d-2b,d-2c+1).
```

## Joint saturation lemma

Assume

```text
b >= c,
h-b >= 5,
e = 3d+c-b.
```

Because `b>=c`, the N356 global mass cap is `Cmax=3d+c-b`. Equality `e=Cmax` forces the balanced split `n1=n2=h` and forces each independent transportation component to attain its own mass maximum.

In the third component put

```text
B = h-b,
C = h-c.
```

Then `0 <= B <= C`, and the omitted mass in this component must saturate at

```text
r = d-2b = 2B.
```

Orient the third component so the omitted variables are

- `u`: the one omitted label in the fixed-`b` cell;
- `x`: total omitted mass in one four-label cross cell;
- `y`: total omitted mass in the other four-label cross cell;
- the fixed-`c` cell has no omitted label.

The balanced transportation constraints include

```text
u+x <= B,
u+y <= B,
x <= C,
y <= C,
u,x,y >= 0.
```

At saturation `u+x+y=2B`. Adding the first two inequalities gives `2u+x+y<=2B`; substituting the saturated mass gives `u=0`. Therefore the one-slot `u` edge cannot contribute support. The two four-label cross cells contribute at most four positive omitted coordinates each, so the third-component support is at most `8`.

The hypothesis `B>=5` makes N357's separate third-component support cap equal to `9`, because

```text
B+C >= 10,
2B >= 10,
2C+1 >= 11.
```

Thus exactly on this saturation face the joint mass/support geometry improves N357 by one support unit:

```text
Sjoint = Srem - 1.
```

Every genuine extension on that face must satisfy the new necessary condition

```text
s + min(e-M, Srem-1) >= K.
```

Away from the displayed saturation hypotheses, N358 makes no new claim and retains the N357 condition unchanged.

## Sharpness of the one-unit loss

The loss is exactly one, not merely an upper bound. When `B>=5` and `C>=B`, the saturated assignment `u=0, x=B, y=B` has support `8`; at mass `2B-1`, `u=1, x=B-1, y=B-1` has support `9`. Hence the incompatibility occurs precisely at third-component mass saturation.

## Strict FULL178 witnesses

The cut is nonredundant on the current N357 frontier. For each K=48 boundary row

```text
g0-d174,
g0-d176,
g1-d190,
g1-d192,
```

take `e=3d` and `a=b=c=h-5`. Choose all ten stored exceptional coordinates positive with those block sums and the existing N355 symmetry/parity rules. Then

```text
M=3(h-5),
s=10,
b-c=0=3d-e,
S0=16,
SA=13,
S3=9,
Srem=38.
```

N357 therefore accepts on equality: `10+38=48=K`. N358 forces the third-component support from `9` to `8`, so `10+37=47<K` and rejects. The accompanying verifier constructs an explicit legal prefix in each of the four rows; their normal-block multiplicities alone give a strictness lower bound of

```text
(4*174+1) + (4*176+1) + (4*190+1) + (4*192+1) = 2,932
```

compressed terminals. This is only a lower-bound witness, not an all-178 N358 census.

## Credit firewall / next bounded unit

- N358 has zero MAIN pruning credit until an exact retained-frontier census is frozen and independently hostile-audited.
- The current N357 authoritative residual is unchanged by this research checkpoint.
- No FULL178 completion, N350 producer registration, production COMPLETE, N104 release, receiver/theorem/endpoint/Stage32/Perfect-Cuboid credit is asserted.
- No heavy compute and no merge authorization.

Next bounded unit: reuse the locked N357 retained-prefix machinery to count the exact incremental rejection from the conditional one-support saturation cut, then freeze the result for `stage32-01-178-audit`.
