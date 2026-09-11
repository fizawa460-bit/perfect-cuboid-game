# Stage36 36-09EZ — residual-core nullity controlled-radical search

## Entry authority

36-09EY was promoted exact-green at V284, head `d3aef78cb57e15a5b371d7137dc61fda846c09ed`, CI `34413590057 / 102673330087`. The exact usable reduction is

```text
rank_F2(M)=k+rank_F2(H),
dim_F2 Sel^2(E_rho,p/Q)=nullity_F2(H).
```

Thus a fixed parameter is Sel2-dimension two exactly when its residual core after legal deterministic leaf peeling has nullity two.

## Search family

Retain the EW/EX one-variable family

```text
K = 729,
a = 2u,
b = 2u+K,
q = 4u+K,
s = (8u^2-K^2)/7,
t = (8u^2+8Ku+K^2)/41,
u = 17627 (mod 34440).
```

For this progression the same shallow dyadic branch and EH mod-5 no-3-torsion screen used in EX remain available. Exact factorization of the five values `u,b,q,s,t` supplies the labelled radical support; no primality-of-all-five hypothesis is imposed.

## Bounded discovery, exact candidate certification

A bounded discovery scan over the first 1000 progression points (`u=17627+34440*j`, `0<=j<1000`) proposed 29 new `u` values beyond the already promoted EW/EX hits. This leaf does **not** claim that the 29-list exhausts that window; the retained verifier certifies the listed candidates individually.

```text
6974507, 7146707, 7422227, 9695267, 9867467,
11279507, 11451707, 11761667, 11933867, 13483667,
14930147, 15377867, 15446747, 16548827, 19476227,
22334747, 22885787, 24160067, 24883307, 26088707,
28292867, 29291627, 29636027, 30565907, 31013627,
31426907, 31530227, 31840187, 31943507.
```

For every listed value the verifier:

1. factors `u,b,q,s,t` exactly using deterministic Miller-Rabin plus Pollard-rho recursion and checks the labelled support sets are disjoint;
2. builds the exact support matrix from the actual radical primes and Legendre symbols;
3. performs deterministic legal leaf peeling and checks residual-core nullity exactly two, equivalently rank `2n-2`;
4. rechecks the EH screens: `|D|` is nonsquare for the no-4-torsion branch and the exact 3-division polynomial has no root mod 5;
5. checks the four-point literal orbit is disjoint from the previously promoted 76 fixed parameters and from all other new orbits.

The 29 candidates produce 29 disjoint four-point literal orbits, hence 116 new provisional fixed-parameter exclusions. If exact-head CI is green, the registry may promote `76 -> 192`.

## Compression effect

No new full-pattern template is needed. The 29 exact rows include both leaf-only and genuine residual cores; all are accepted by the single EY invariant `nullity(H)=2`. The residual `(size,rank)` pairs observed are

```text
(2,0) x14, (11,9) x3, (12,10) x1, (13,11) x1,
(14,12) x2, (15,13) x2, (16,14) x5, (17,15) x1.
```

This is evidence that the residual-core criterion scales beyond the 17 promoted pattern templates, but it is still finite fixed-parameter evidence. `exact_sufficient_template_count` remains 17.

## Next leaf

After CI promotion, continue to

```text
36-09FA_RHO_RESIDUAL_CORE_TYPE_PARAMETRIC_REALIZATION_PREFLIGHT
```

with the goal of replacing more finite hits by a parametric residual-core condition rather than accumulating full-pattern hashes.

## Credit firewall

This leaf does not prove completeness of the 1000-point discovery window, does not prove infinitely many hits, does not classify all residual-core types, does not establish a uniform Sel2-dimension-two theorem, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
