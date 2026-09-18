# Stage32 MB104 — W31 Lazarsfeld--Mukai elementary-transform audit — corrected — 2026-09-18

Status: **TESTED ARCHITECTURE HARD-DROP / TAUTOLOGICAL DESTABILIZER / BROADER LM DIRECTION SOFT-PARK / NO CREDIT**

## Construction

For a hypothetical carrier `C in |D_l|`, put

```
A=O_C(H),
V=H0(S,O_S(H)), dim V=7.
```

The elementary transform is

```
0 -> F -> V tensor O_S -> i_*A -> 0,
E=F^vee.
```

It has

```
rank(E)=7,
c1(E)=D_l,
c2(E)=H.D_l=112l,
Delta_BG(E)=-224l(9l-7)<0.
```

The first preflight therefore correctly detected slope instability.

## Structural resolution

However, `A` is not an intrinsic new line bundle on the carrier: it is the restriction of the globally generated surface line bundle `O_S(H)`.

Use the ambient evaluation sequence

```
0 -> M_H -> V tensor O_S -> O_S(H) -> 0.
```

The kernel of

```
O_S(H) -> i_*O_C(H)
```

is

```
O_S(H-D_l).
```

Comparing the two evaluation sequences gives

```
0 -> M_H -> F -> O_S(H-D_l) -> 0.
```

Dualizing gives the explicit extension

```
0 -> O_S(D_l-H) -> E -> M_H^vee -> 0.       (*)
```

Thus the putative Bogomolov destabilizer is already visible before any instability theorem.

Its `H`-slope is

```
H.(D_l-H)=112l-16,
```

whereas

```
mu_H(E)=H.D_l/7=16l.
```

For every `l>=1`,

```
112l-16 > 16l.
```

So `O_S(D_l-H)` is an explicit destabilizing line subbundle of `E`.

The earlier second-scan numerical witness `B=H` was precisely this subbundle written as `D_l-B`.

## Decision

The rank-seven ambient-hyperplane LM construction produces **no new geometric datum**.  Its negative discriminant merely rediscovers the tautological extension `(*)`.

```
tested_architecture_status = HARD-DROP
broader_direction_status   = SOFT-PARK
PROMOTE                     = false
DEEP                        = false
```

A non-tautological LM/coherent-system route would need a line bundle or subsystem on the carrier that does not simply extend from a globally generated line bundle on `S`.

No credit changes.
