# Stage35-EX Goal4AR source lock — full Brauer–Manin orthogonality is endpoint-equivalent on the source-marked local relaxation

Scope: continue provisionally after exact-head-green Goal4AQ while audited authority remains V74 / Goal4AK. This leaf derives a formal consequence of the exact Goal4AQ unit-character endpoint equivalence. It does not compute the transcendental Brauer group and does not prove a Brauer–Manin obstruction, E1, Stage35, or any perfect-cuboid theorem.

## Exact inputs

Goal4AQ fixes the source-marked local relaxation

```text
A_src^loc = U_PC(R)^+ x U_PC(Q_2)^src x product'_{l odd} U_PC(Q_l)
```

and the unit-character subgroup

```text
B_unit subset Br_a(U) subset Br(U).
```

At exact head `c1dc9ff4d84a87d6301e78c00d35b69aa16a07f7`, aggregate run `34281502796` is green and verifies

```text
(A_src^loc)^(B_unit) != empty
iff U_PC(Q)^src,+ != empty
iff Stage35 E1-counterexample population != empty.            (AQ)
```

The last equivalence is the hostile-audited 35EX-31 population adapter.

## Full Brauer set inclusion

For any adelic population `A` and subgroups `B1 subset B2 subset Br(U)`, orthogonality gives

```text
A^(B2) subset A^(B1).
```

Hence

```text
(A_src^loc)^(Br(U)) subset (A_src^loc)^(B_unit).                (1)
```

If the left side of `(1)` is nonempty, Goal4AQ immediately gives a positive source-marked rational endpoint.

## Converse by a diagonal rational point

Conversely, suppose

```text
P in U_PC(Q)^src,+.
```

Its diagonal adelic point belongs to `A_src^loc`: positivity gives the real condition, the exact source marking gives the Q_2 condition, and a rational point is integral for almost all finite primes after choosing the retained integral model.

For every `alpha in Br(U)`, evaluation of `alpha` at the diagonal rational point is a global Brauer class over Q. Global reciprocity gives

```text
sum_v inv_v alpha(P) = 0.
```

Therefore the diagonal adele lies in

```text
(A_src^loc)^(Br(U)).                                             (2)
```

Combining `(1)`, `(2)`, and `(AQ)` yields

```text
(A_src^loc)^(Br(U)) != empty
iff (A_src^loc)^(B_unit) != empty
iff U_PC(Q)^src,+ != empty
iff Stage35 E1-counterexample population != empty.              (AR-EQUIV)
```

## Route consequence

The full Brauer–Manin set on this exact source-marked local relaxation is endpoint-equivalent. Computing the entire transcendental Brauer group is not required to establish that equivalence.

This does **not** prove that every finite or specially chosen additional Brauer class is useless. A finite explicit algebraic or transcendental class could still provide a shorter sufficient obstruction if its evaluation set were empty. Goal4AR only says that the complete Brauer–Manin condition, taken as a whole, is neither weaker nor stronger than actual rational-endpoint existence on this relaxation.

Accordingly:

- `FULL_BRAUER_BM_ROUTE_ENDPOINT_EQUIVALENT=true`;
- `TRANSCENDENTAL_BRAUER_GROUP_COMPUTED=false`;
- `FINITE_TRANSCENDENTAL_SHORTCUT_RULED_OUT=false`;
- `BRAUER_MANIN_OBSTRUCTION_OBTAINED=false`.

Because Goal4AQ/Goal4AR materially changes the arithmetic interpretation of the active Brauer route, the Cycle Exploration Safety Protocol trigger 4 applies: the next route selection should run a fresh `EXHAUSTIVE_VIEW_AUDIT` with `BLIND_REDISCOVERY` before parking or selecting another arithmetic route.

## Credit firewall

Certified provisionally only:

- inclusion of the full Brauer–Manin set in the Goal4AQ unit-character set;
- diagonal rational points are orthogonal to all of `Br(U)` by global reciprocity;
- the exact equivalence `(AR-EQUIV)` on `A_src^loc`;
- the full Brauer route, as a complete obstruction on this relaxation, is endpoint-equivalent.

Not certified:

- emptiness or nonemptiness of either side of `(AR-EQUIV)`;
- the transcendental Brauer group;
- nonexistence of a useful finite additional Brauer class;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
